#!/bin/bash
set -euo pipefail

TODAY=$(date -u +%Y-%m-%d)
PARENT_REPO="anajuliabit/aeon"
STATE_FILE="memory/topics/fork-cohort-state.json"
ARTICLE_FILE="articles/fork-cohort-${TODAY}.md"

echo "=== Fork Cohort Tracker ==="
echo "Date: ${TODAY}"
echo "Parent: ${PARENT_REPO}"

# Step 2: List forks
echo "Fetching forks list..."
FORK_LIST=$(gh api "repos/${PARENT_REPO}/forks" --paginate \
  --jq '[.[] | select(.archived != true and .disabled != true) | {full_name, owner: .owner.login, default_branch, pushed_at, stargazers_count, created_at}]')

FORK_COUNT=$(echo "$FORK_LIST" | jq 'length')
echo "Found ${FORK_COUNT} active forks"

if [ "${FORK_COUNT}" -eq 0 ]; then
  echo "FORK_COHORT_NO_FORKS" > /tmp/fork-cohort-status.txt
  exit 0
fi

echo "$FORK_LIST" > /tmp/fork-list.json

# Step 3 & 4: Process each fork - get last run and enabled skills
echo "Processing forks (max 80)..."

FORKS=$(echo "$FORK_LIST" | jq -r '.[] | @base64')
FORK_INDEX=0
MAX_FORKS=80

declare -A FORK_DATA
declare -A BUCKET_COUNTS
BUCKET_COUNTS[POWER]=0
BUCKET_COUNTS[ACTIVE]=0
BUCKET_COUNTS[STALE]=0
BUCKET_COUNTS[COLD]=0
BUCKET_COUNTS[UNREADABLE]=0

RUNS_CHECKED=0
AEON_CHECKED=0
UNREADABLE_COUNT=0

for FORK_B64 in $FORKS; do
  if [ $FORK_INDEX -ge $MAX_FORKS ]; then
    echo "Truncated at ${MAX_FORKS} forks"
    break
  fi

  FORK=$(echo "$FORK_B64" | base64 -d)
  FULL_NAME=$(echo "$FORK" | jq -r '.full_name')
  OWNER=$(echo "$FORK" | jq -r '.owner')
  DEFAULT_BRANCH=$(echo "$FORK" | jq -r '.default_branch')
  CREATED_AT=$(echo "$FORK" | jq -r '.created_at')
  STARS=$(echo "$FORK" | jq -r '.stargazers_count')

  echo "  [$((FORK_INDEX + 1))/${FORK_COUNT}] ${FULL_NAME}..."

  # Get last run with retry
  LAST_RUN=""
  HTTP_CODE=$(curl -s -o /tmp/fork-runs.json -w "%{http_code}" \
    -H "Authorization: token ${GITHUB_TOKEN}" \
    "https://api.github.com/repos/${FULL_NAME}/actions/runs?per_page=1")

  if [ "$HTTP_CODE" = "200" ]; then
    LAST_RUN=$(jq -r '.workflow_runs[0].updated_at // empty' /tmp/fork-runs.json)
    RUNS_CHECKED=$((RUNS_CHECKED + 1))
  elif [ "$HTTP_CODE" = "404" ]; then
    # Actions disabled - treat as COLD
    LAST_RUN=""
    RUNS_CHECKED=$((RUNS_CHECKED + 1))
  elif [ "$HTTP_CODE" = "403" ]; then
    # Rate limit - retry after 60s
    echo "    Rate limited, retrying..."
    sleep 60
    HTTP_CODE=$(curl -s -o /tmp/fork-runs.json -w "%{http_code}" \
      -H "Authorization: token ${GITHUB_TOKEN}" \
      "https://api.github.com/repos/${FULL_NAME}/actions/runs?per_page=1")
    if [ "$HTTP_CODE" = "200" ]; then
      LAST_RUN=$(jq -r '.workflow_runs[0].updated_at // empty' /tmp/fork-runs.json)
      RUNS_CHECKED=$((RUNS_CHECKED + 1))
    else
      BUCKET="UNREADABLE"
      UNREADABLE_COUNT=$((UNREADABLE_COUNT + 1))
    fi
  else
    # 5xx error - retry after 10s
    sleep 10
    HTTP_CODE=$(curl -s -o /tmp/fork-runs.json -w "%{http_code}" \
      -H "Authorization: token ${GITHUB_TOKEN}" \
      "https://api.github.com/repos/${FULL_NAME}/actions/runs?per_page=1")
    if [ "$HTTP_CODE" = "200" ]; then
      LAST_RUN=$(jq -r '.workflow_runs[0].updated_at // empty' /tmp/fork-runs.json)
      RUNS_CHECKED=$((RUNS_CHECKED + 1))
    else
      BUCKET="UNREADABLE"
      UNREADABLE_COUNT=$((UNREADABLE_COUNT + 1))
    fi
  fi

  # Calculate days since run
  if [ -z "$LAST_RUN" ]; then
    DAYS_SINCE_RUN=999
  else
    NOW_TS=$(date -u +%s)
    LAST_RUN_TS=$(date -u -d "$LAST_RUN" +%s 2>/dev/null || echo "0")
    DAYS_SINCE_RUN=$(( (NOW_TS - LAST_RUN_TS) / 86400 ))
  fi

  # Classify bucket
  BUCKET="UNKNOWN"
  ENABLED_COUNT=0

  if [ "$DAYS_SINCE_RUN" -gt 365 ]; then
    BUCKET="COLD"
  elif [ "$DAYS_SINCE_RUN" -lt 7 ]; then
    # Need to check enabled skills for POWER classification
    BUCKET="ACTIVE"

    # Try to fetch aeon.yml
    AEON_CONTENT=$(gh api "repos/${FULL_NAME}/contents/aeon.yml?ref=${DEFAULT_BRANCH}" --jq '.content' 2>/dev/null | base64 -d 2>/dev/null || echo "")
    AEON_CHECKED=$((AEON_CHECKED + 1))

    if [ -n "$AEON_CONTENT" ]; then
      ENABLED_COUNT=$(echo "$AEON_CONTENT" | grep -E "enabled:\s*true" | wc -l | tr -d ' ')
      if [ "$ENABLED_COUNT" -ge 5 ]; then
        BUCKET="POWER"
      fi
    fi
  elif [ "$DAYS_SINCE_RUN" -ge 7 ]; then
    BUCKET="STALE"
  fi

  if [ "$BUCKET" != "UNREADABLE" ]; then
    BUCKET_COUNTS[$BUCKET]=$((BUCKET_COUNTS[$BUCKET] + 1))
  fi

  # Store fork data
  FORK_KEY="${FULL_NAME}"
  FORK_DATA["${FORK_KEY}"]=$(jq -n \
    --arg bucket "$BUCKET" \
    --arg last_run "$LAST_RUN" \
    --arg days "$DAYS_SINCE_RUN" \
    --arg enabled "$ENABLED_COUNT" \
    --arg owner "$OWNER" \
    --arg stars "$STARS" \
    --arg branch "$DEFAULT_BRANCH" \
    '{bucket: $bucket, last_run: $last_run, days_since_run: ($days | tonumber), enabled_count: ($enabled | tonumber), owner: $owner, stargazers: ($stars | tonumber), default_branch: $branch}')

  FORK_INDEX=$((FORK_INDEX + 1))
done

echo ""
echo "=== Summary ==="
echo "POWER: ${BUCKET_COUNTS[POWER]}"
echo "ACTIVE: ${BUCKET_COUNTS[ACTIVE]}"
echo "STALE: ${BUCKET_COUNTS[STALE]}"
echo "COLD: ${BUCKET_COUNTS[COLD]}"
echo "UNREADABLE: ${BUCKET_COUNTS[UNREADABLE]}"
echo ""
echo "Forks processed: ${FORK_INDEX}"
echo "Runs checked: ${RUNS_CHECKED}"
echo "Aeon.yml checked: ${AEON_CHECKED}"
echo "Unreadable: ${UNREADABLE_COUNT}"
