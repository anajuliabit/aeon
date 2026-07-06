#!/usr/bin/env bash
# Fork cohort skill runner
set -euo pipefail

TODAY="2026-07-05"
PARENT_REPO="aaronjmars/aeon"
STATE_FILE="memory/topics/fork-cohort-state.json"
RESULTS_FILE=".fork-cohort-results.json"
NOW_TS=$(date -u +%s)

mkdir -p articles

echo "=== Fork Cohort Run: $TODAY ==="
echo "Fetching top 80 forks by pushed_at..."

# Get sorted top 80 forks
FORKS_JSON=$(gh api "repos/${PARENT_REPO}/forks" --paginate \
  --jq '[.[] | select(.archived != true and .disabled != true) | {full_name, owner: .owner.login, default_branch, pushed_at, stargazers_count, created_at}]' \
  | jq -s 'add | sort_by(.pushed_at) | reverse | .[0:80]')

TOTAL_AVAILABLE=$(gh api "repos/${PARENT_REPO}/forks" --paginate --jq '[.[] | select(.archived != true and .disabled != true)]' | jq -s 'add | length')
SCANNED=$(echo "$FORKS_JSON" | jq 'length')

echo "Total available: $TOTAL_AVAILABLE, scanning: $SCANNED"

# Initialize results accumulator
echo '{}' > "$RESULTS_FILE"

RUNS_OK=0
RUNS_TOTAL=0
AEON_OK=0
AEON_TOTAL=0
UNREADABLE_N=0

# Process each fork
while IFS= read -r fork_json; do
  FULL_NAME=$(echo "$fork_json" | jq -r '.full_name')
  OWNER=$(echo "$fork_json" | jq -r '.owner')
  DEFAULT_BRANCH=$(echo "$fork_json" | jq -r '.default_branch // "main"')
  STARS=$(echo "$fork_json" | jq -r '.stargazers_count // 0')
  CREATED_AT=$(echo "$fork_json" | jq -r '.created_at // ""')

  echo -n "  $FULL_NAME ... "
  RUNS_TOTAL=$((RUNS_TOTAL + 1))

  # Get last run
  HTTP_CODE=$(gh api "repos/${FULL_NAME}/actions/runs?per_page=1" --include 2>/dev/null | head -1 | awk '{print $2}' || echo "0")

  LAST_RUN_RAW=$(gh api "repos/${FULL_NAME}/actions/runs?per_page=1" \
    --jq '.workflow_runs[0].updated_at // empty' 2>/dev/null || echo "")

  # Check if 404 (Actions disabled)
  GH_STATUS=$(gh api "repos/${FULL_NAME}/actions/runs?per_page=1" --include 2>&1 | head -1 || echo "")

  WAS_404=0
  if echo "$GH_STATUS" | grep -q "404"; then
    WAS_404=1
    LAST_RUN=""
  else
    LAST_RUN="$LAST_RUN_RAW"
    RUNS_OK=$((RUNS_OK + 1))
  fi

  # Compute days since run
  if [ -z "$LAST_RUN" ] || [ "$WAS_404" = "1" ]; then
    DAYS_SINCE="null"
    DAYS_FLOAT=99999
  else
    # Parse ISO8601 to epoch
    RUN_TS=$(date -u -d "$LAST_RUN" +%s 2>/dev/null || echo "0")
    DIFF=$((NOW_TS - RUN_TS))
    DAYS_FLOAT=$(echo "$DIFF" | awk '{printf "%.1f", $1/86400}')
    DAYS_SINCE="$DAYS_FLOAT"
  fi

  # Classify initially (before POWER check)
  ENABLED_COUNT=0

  if [ "$WAS_404" = "1" ]; then
    BUCKET="COLD"
  elif [ "$DAYS_FLOAT" = "99999" ]; then
    BUCKET="COLD"
  elif awk "BEGIN{exit !($DAYS_FLOAT > 365)}"; then
    BUCKET="COLD"
  elif awk "BEGIN{exit !($DAYS_FLOAT < 7)}"; then
    # Check enabled skills for POWER threshold
    AEON_TOTAL=$((AEON_TOTAL + 1))
    AEON_CONTENT=$(gh api "repos/${FULL_NAME}/contents/aeon.yml?ref=${DEFAULT_BRANCH}" \
      --jq '.content' 2>/dev/null || echo "")
    if [ -n "$AEON_CONTENT" ]; then
      # Count enabled: true lines (non-comment)
      ENABLED_COUNT=$(echo "$AEON_CONTENT" | base64 -d 2>/dev/null \
        | grep -v '^\s*#' | grep -cE 'enabled:\s*true' || echo "0")
      AEON_OK=$((AEON_OK + 1))
    fi
    if [ "$ENABLED_COUNT" -ge 5 ] 2>/dev/null; then
      BUCKET="POWER"
    else
      BUCKET="ACTIVE"
    fi
  else
    BUCKET="STALE"
  fi

  echo "$BUCKET (last=${LAST_RUN:0:10}, enabled=$ENABLED_COUNT)"

  # Append to results JSON
  ENTRY=$(jq -n \
    --arg bucket "$BUCKET" \
    --arg last_run "${LAST_RUN}" \
    --argjson days_since "$([ "$DAYS_SINCE" = "null" ] && echo null || echo \"$DAYS_SINCE\")" \
    --argjson enabled_count "$ENABLED_COUNT" \
    --argjson stars "$STARS" \
    --arg default_branch "$DEFAULT_BRANCH" \
    --arg owner "$OWNER" \
    --arg created_at "$CREATED_AT" \
    '{bucket: $bucket, last_run: (if $last_run == "" then null else $last_run end), days_since_run: $days_since, enabled_count: $enabled_count, stargazers: $stars, default_branch: $default_branch, owner: $owner, created_at: $created_at}')

  # Merge into results
  CURRENT=$(cat "$RESULTS_FILE")
  echo "$CURRENT" | jq --arg key "$FULL_NAME" --argjson val "$ENTRY" '. + {($key): $val}' > "${RESULTS_FILE}.tmp"
  mv "${RESULTS_FILE}.tmp" "$RESULTS_FILE"

done < <(echo "$FORKS_JSON" | jq -c '.[]')

echo ""
echo "=== Processing complete ==="
echo "runs_ok=$RUNS_OK/$RUNS_TOTAL aeon_yml=$AEON_OK/$AEON_TOTAL"

# Compute totals from results
RESULTS=$(cat "$RESULTS_FILE")

COUNT_POWER=$(echo "$RESULTS" | jq '[to_entries[] | select(.value.bucket == "POWER")] | length')
COUNT_ACTIVE=$(echo "$RESULTS" | jq '[to_entries[] | select(.value.bucket == "ACTIVE")] | length')
COUNT_STALE=$(echo "$RESULTS" | jq '[to_entries[] | select(.value.bucket == "STALE")] | length')
COUNT_COLD=$(echo "$RESULTS" | jq '[to_entries[] | select(.value.bucket == "COLD")] | length')
COUNT_UNREADABLE=$(echo "$RESULTS" | jq '[to_entries[] | select(.value.bucket == "UNREADABLE")] | length')

N_TOTAL=$((COUNT_POWER + COUNT_ACTIVE + COUNT_STALE + COUNT_COLD + COUNT_UNREADABLE))
N_RUNNING=$((COUNT_POWER + COUNT_ACTIVE))
PCT=$(awk "BEGIN{printf \"%d\", ($N_RUNNING/$N_TOTAL)*100}")

echo "POWER=$COUNT_POWER ACTIVE=$COUNT_ACTIVE STALE=$COUNT_STALE COLD=$COUNT_COLD UNREADABLE=$COUNT_UNREADABLE"
echo "Running: $N_RUNNING/$N_TOTAL ($PCT%)"

# Load prior state
PRIOR=$(cat "$STATE_FILE" 2>/dev/null || echo '{"forks":{},"last_run":null}')
PRIOR_LAST_RUN=$(echo "$PRIOR" | jq -r '.last_run // "null"')
IS_FIRST_RUN=0
[ "$PRIOR_LAST_RUN" = "null" ] && IS_FIRST_RUN=1

echo "Prior run: $PRIOR_LAST_RUN, first_run=$IS_FIRST_RUN"

# Compute transitions
LEVELED_UP=""
REVIVED=""
WENT_STALE=""
NEW_ACTIVE=""
WENT_COLD=""
DROPPED=""

LU_COUNT=0
REV_COUNT=0
WS_COUNT=0
NA_COUNT=0
WC_COUNT=0
DR_COUNT=0

while IFS= read -r line; do
  FORK_NAME=$(echo "$line" | jq -r '.key')
  NEW_BUCKET=$(echo "$line" | jq -r '.value.bucket')
  FORK_OWNER=$(echo "$line" | jq -r '.value.owner')
  FORK_ENABLED=$(echo "$line" | jq -r '.value.enabled_count')
  FORK_DSR=$(echo "$line" | jq -r '.value.days_since_run // "null"')
  FORK_LR=$(echo "$line" | jq -r '.value.last_run // "null"')
  FORK_CREATED=$(echo "$line" | jq -r '.value.created_at // ""')

  OLD_BUCKET=$(echo "$PRIOR" | jq -r --arg k "$FORK_NAME" '.forks[$k].bucket // "null"')

  if [ "$OLD_BUCKET" = "null" ]; then
    # New fork
    if [ "$NEW_BUCKET" = "ACTIVE" ] || [ "$NEW_BUCKET" = "POWER" ]; then
      NEW_ACTIVE="$NEW_ACTIVE\n- @${FORK_OWNER} — \`${FORK_NAME}\` (created ${FORK_CREATED:0:10}, last run ${FORK_DSR}d ago)"
      NA_COUNT=$((NA_COUNT + 1))
    fi
  else
    if [ "$NEW_BUCKET" = "POWER" ] && [ "$OLD_BUCKET" != "POWER" ]; then
      LEVELED_UP="$LEVELED_UP\n- @${FORK_OWNER} — \`${FORK_NAME}\` (+${FORK_ENABLED} skills enabled, last run ${FORK_DSR}d ago)"
      LU_COUNT=$((LU_COUNT + 1))
    elif [ "$OLD_BUCKET" = "POWER" ] && [ "$NEW_BUCKET" = "ACTIVE" ]; then
      DROPPED="$DROPPED\n- @${FORK_OWNER} — \`${FORK_NAME}\` (now ACTIVE, ${FORK_ENABLED} skills enabled, last run ${FORK_DSR}d ago)"
      DR_COUNT=$((DR_COUNT + 1))
    elif ( [ "$OLD_BUCKET" = "ACTIVE" ] || [ "$OLD_BUCKET" = "POWER" ] ) && [ "$NEW_BUCKET" = "STALE" ]; then
      WENT_STALE="$WENT_STALE\n- @${FORK_OWNER} — \`${FORK_NAME}\` (last run ${FORK_DSR}d ago, dropped from ${OLD_BUCKET})"
      WS_COUNT=$((WS_COUNT + 1))
    elif [ "$OLD_BUCKET" = "STALE" ] && ( [ "$NEW_BUCKET" = "ACTIVE" ] || [ "$NEW_BUCKET" = "POWER" ] ); then
      OLD_LAST_RUN=$(echo "$PRIOR" | jq -r --arg k "$FORK_NAME" '.forks[$k].last_run // "unknown"')
      OLD_DATE="${OLD_LAST_RUN:0:10}"
      REVIVED="$REVIVED\n- @${FORK_OWNER} — \`${FORK_NAME}\` (last run ${FORK_DSR}d ago, was last seen ${OLD_DATE})"
      REV_COUNT=$((REV_COUNT + 1))
    elif ( [ "$OLD_BUCKET" = "ACTIVE" ] || [ "$OLD_BUCKET" = "POWER" ] ) && [ "$NEW_BUCKET" = "COLD" ]; then
      WENT_COLD="$WENT_COLD\n- @${FORK_OWNER} — \`${FORK_NAME}\` (last run ${FORK_LR:0:10})"
      WC_COUNT=$((WC_COUNT + 1))
    fi
  fi
done < <(echo "$RESULTS" | jq -c 'to_entries[]')

echo "Transitions: LU=$LU_COUNT REV=$REV_COUNT WS=$WS_COUNT NA=$NA_COUNT WC=$WC_COUNT DR=$DR_COUNT"

# Pick verdict
if [ "$IS_FIRST_RUN" = "1" ]; then
  VERDICT="COLD START: $N_TOTAL forks, $N_RUNNING running"
elif [ "$LU_COUNT" -gt 0 ]; then
  VERDICT="LEVELED_UP: $LU_COUNT fork(s) crossed POWER threshold"
elif [ "$REV_COUNT" -gt 0 ]; then
  VERDICT="REVIVED: $REV_COUNT stale fork(s) running again"
elif [ "$WS_COUNT" -gt 0 ]; then
  VERDICT="WENT_STALE: $WS_COUNT active fork(s) went quiet"
elif [ $((LU_COUNT + REV_COUNT + WS_COUNT + NA_COUNT + WC_COUNT + DR_COUNT)) -gt 0 ]; then
  TOTAL_TRANSITIONS=$((LU_COUNT + REV_COUNT + WS_COUNT + NA_COUNT + WC_COUNT + DR_COUNT))
  VERDICT="MOVEMENT: $TOTAL_TRANSITIONS bucket changes this week"
else
  VERDICT="STEADY: $N_RUNNING of $N_TOTAL running"
fi

echo "Verdict: $VERDICT"

# Prior deltas
PRIOR_POWER=$(echo "$PRIOR" | jq -r '.totals.power // 0')
PRIOR_ACTIVE=$(echo "$PRIOR" | jq -r '.totals.active // 0')
PRIOR_STALE=$(echo "$PRIOR" | jq -r '.totals.stale // 0')
PRIOR_COLD=$(echo "$PRIOR" | jq -r '.totals.cold // 0')

delta() { local new=$1 old=$2; local d=$((new - old)); if [ "$d" -gt 0 ]; then echo "+$d"; elif [ "$d" -lt 0 ]; then echo "$d"; else echo "0"; fi; }

DELTA_POWER=$(delta $COUNT_POWER $PRIOR_POWER)
DELTA_ACTIVE=$(delta $COUNT_ACTIVE $PRIOR_ACTIVE)
DELTA_STALE=$(delta $COUNT_STALE $PRIOR_STALE)
DELTA_COLD=$(delta $COUNT_COLD $PRIOR_COLD)

TRUNC_STR="false"
[ "$TOTAL_AVAILABLE" -gt 80 ] && TRUNC_STR="true"

# Build POWER roster
POWER_ROSTER=$(echo "$RESULTS" | jq -r '
  to_entries
  | map(select(.value.bucket == "POWER"))
  | sort_by(.value.enabled_count) | reverse
  | .[0:30]
  | .[]
  | "| \(.key) | @\(.value.owner) | \(.value.enabled_count) | \(.value.days_since_run // 0)d ago | \(.value.stargazers) |"
')

# Write article
ARTICLE_PATH="articles/fork-cohort-${TODAY}.md"

{
cat << ARTICLE_EOF
# Fork Activation Cohort — ${TODAY}

**Verdict:** ${VERDICT}

**Parent:** ${PARENT_REPO}
**Total forks:** ${N_TOTAL} · **Running (last 7d):** ${N_RUNNING} (${PCT}%)
ARTICLE_EOF

if [ "$TRUNC_STR" = "true" ]; then
  echo "_Note: Scanned top 80 of ${TOTAL_AVAILABLE} forks by recent push activity (truncated)._"
fi

cat << ARTICLE_EOF2

---

## Cohort breakdown

| Cohort | Count | Δ vs last week |
|--------|-------|----------------|
| POWER | ${COUNT_POWER} | ${DELTA_POWER} |
| ACTIVE | ${COUNT_ACTIVE} | ${DELTA_ACTIVE} |
| STALE | ${COUNT_STALE} | ${DELTA_STALE} |
| COLD | ${COUNT_COLD} | ${DELTA_COLD} |
ARTICLE_EOF2

if [ "$COUNT_UNREADABLE" -gt 0 ]; then
  echo "| UNREADABLE | ${COUNT_UNREADABLE} | 0 |"
fi

echo ""
echo "---"
echo ""
echo "## Movement this week"
echo ""

HAS_MOVEMENT=0
[ "$LU_COUNT" -gt 0 ] && HAS_MOVEMENT=1
[ "$REV_COUNT" -gt 0 ] && HAS_MOVEMENT=1
[ "$WS_COUNT" -gt 0 ] && HAS_MOVEMENT=1
[ "$NA_COUNT" -gt 0 ] && HAS_MOVEMENT=1
[ "$WC_COUNT" -gt 0 ] && HAS_MOVEMENT=1
[ "$DR_COUNT" -gt 0 ] && HAS_MOVEMENT=1

if [ "$HAS_MOVEMENT" = "0" ]; then
  echo "_No bucket changes this week._"
else
  if [ "$LU_COUNT" -gt 0 ]; then
    echo "### Leveled up to POWER"
    printf "%b\n" "$LEVELED_UP"
    echo ""
  fi
  if [ "$REV_COUNT" -gt 0 ]; then
    echo "### Revived (stale → running)"
    printf "%b\n" "$REVIVED"
    echo ""
  fi
  if [ "$WS_COUNT" -gt 0 ]; then
    echo "### Went stale (active → quiet)"
    printf "%b\n" "$WENT_STALE"
    echo ""
  fi
  if [ "$NA_COUNT" -gt 0 ]; then
    echo "### New forks running"
    printf "%b\n" "$NEW_ACTIVE"
    echo ""
  fi
  if [ "$WC_COUNT" -gt 0 ]; then
    echo "### Newly cold (was running, now silent >365d)"
    printf "%b\n" "$WENT_COLD"
    echo ""
  fi
  if [ "$DR_COUNT" -gt 0 ]; then
    echo "### Dropped from POWER"
    printf "%b\n" "$DROPPED"
    echo ""
  fi
fi

echo "---"
echo ""

if [ "$COUNT_POWER" -ge 1 ]; then
  echo "## POWER cohort roster"
  echo ""
  echo "| Fork | Owner | Enabled skills | Last run | Stars |"
  echo "|------|-------|----------------|----------|-------|"
  echo "$POWER_ROSTER"
  echo ""
  echo "---"
  echo ""
fi

echo "## Source status"
echo ""
echo "\`forks_list=ok · runs_lookup=${RUNS_OK}/${RUNS_TOTAL} · aeon_yml_lookup=${AEON_OK}/${AEON_TOTAL} · unreadable=${COUNT_UNREADABLE} · truncated=${TRUNC_STR}\`"

} > "$ARTICLE_PATH"

echo "Article written: $ARTICLE_PATH"

# Update state JSON
NEW_STATE=$(jq -n \
  --arg today "$TODAY" \
  --arg parent "$PARENT_REPO" \
  --argjson total "$N_TOTAL" \
  --argjson scanned "$SCANNED" \
  --argjson total_avail "$TOTAL_AVAILABLE" \
  --argjson power "$COUNT_POWER" \
  --argjson active "$COUNT_ACTIVE" \
  --argjson stale "$COUNT_STALE" \
  --argjson cold "$COUNT_COLD" \
  --argjson unreadable "$COUNT_UNREADABLE" \
  --argjson forks "$RESULTS" \
  '{
    last_run: $today,
    last_status: "FORK_COHORT_OK",
    parent_repo: $parent,
    totals: {
      total: $total,
      scanned: $scanned,
      total_available: $total_avail,
      truncated: ($total_avail > 80),
      power: $power,
      active: $active,
      stale: $stale,
      cold: $cold,
      unreadable: $unreadable
    },
    forks: $forks
  }')

echo "$NEW_STATE" > "$STATE_FILE"
echo "State written: $STATE_FILE"

# Determine exit status
TOTAL_TRANSITIONS=$((LU_COUNT + REV_COUNT + WS_COUNT + NA_COUNT + WC_COUNT + DR_COUNT))
if [ "$IS_FIRST_RUN" = "1" ] || [ "$TOTAL_TRANSITIONS" -gt 0 ]; then
  EXIT_STATUS="FORK_COHORT_OK"
elif [ "$VERDICT" = "STEADY: $N_RUNNING of $N_TOTAL running" ]; then
  EXIT_STATUS="FORK_COHORT_QUIET"
else
  EXIT_STATUS="FORK_COHORT_OK"
fi

echo ""
echo "EXIT_STATUS=$EXIT_STATUS"
echo "VERDICT=$VERDICT"

# Save summary
jq -n \
  --arg exit_status "$EXIT_STATUS" \
  --arg verdict "$VERDICT" \
  --argjson n_total "$N_TOTAL" \
  --argjson n_running "$N_RUNNING" \
  --argjson pct "$PCT" \
  --argjson power "$COUNT_POWER" \
  --argjson active "$COUNT_ACTIVE" \
  --argjson stale "$COUNT_STALE" \
  --argjson cold "$COUNT_COLD" \
  --argjson lu "$LU_COUNT" \
  --argjson rev "$REV_COUNT" \
  --argjson ws "$WS_COUNT" \
  --argjson na "$NA_COUNT" \
  --argjson wc "$WC_COUNT" \
  --arg article_path "$ARTICLE_PATH" \
  '{
    exit_status: $exit_status,
    verdict: $verdict,
    n_total: $n_total,
    n_running: $n_running,
    pct: $pct,
    counts: {power: $power, active: $active, stale: $stale, cold: $cold},
    transitions: {leveled_up: $lu, revived: $rev, went_stale: $ws, new_active: $na, went_cold: $wc},
    article_path: $article_path
  }' > .fork-cohort-summary.json

echo "Summary: .fork-cohort-summary.json"
echo "Done."
