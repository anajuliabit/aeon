#!/bin/bash
# Check workflow runs for active fork candidates
# Output: full_name|last_run_iso|bucket_hint

check_fork() {
  local fn="$1"
  local branch="${2:-main}"

  # Get last run
  local last_run
  local http_code
  last_run=$(gh api "repos/${fn}/actions/runs?per_page=1" --jq '.workflow_runs[0].updated_at // "NONE"' 2>/dev/null)
  local exit_code=$?

  if [ $exit_code -ne 0 ] || [ -z "$last_run" ]; then
    echo "${fn}|null|UNREADABLE"
    return
  fi

  if [ "$last_run" = "NONE" ] || [ "$last_run" = "null" ]; then
    echo "${fn}|null|COLD"
    return
  fi

  # Compute days since run (approximate, using date)
  local now_epoch
  local run_epoch
  now_epoch=$(date -d "2026-07-19T20:00:00Z" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "2026-07-19T20:00:00Z" +%s 2>/dev/null)
  run_epoch=$(date -d "${last_run}" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "${last_run}" +%s 2>/dev/null)

  if [ -z "$now_epoch" ] || [ -z "$run_epoch" ]; then
    echo "${fn}|${last_run}|ACTIVE_CANDIDATE"
    return
  fi

  local days_diff=$(( (now_epoch - run_epoch) / 86400 ))

  if [ $days_diff -ge 7 ]; then
    if [ $days_diff -ge 365 ]; then
      echo "${fn}|${last_run}|COLD"
    else
      echo "${fn}|${last_run}|STALE"
    fi
    return
  fi

  # Within 7 days - check aeon.yml for enabled count
  local enabled_count
  enabled_count=$(gh api "repos/${fn}/contents/aeon.yml?ref=${branch}" --jq '.content' 2>/dev/null | base64 -d 2>/dev/null | grep -cE "^[^#]*enabled: *true" 2>/dev/null || echo "0")

  if [ -z "$enabled_count" ]; then
    enabled_count=0
  fi

  if [ "$enabled_count" -ge 5 ] 2>/dev/null; then
    echo "${fn}|${last_run}|POWER|${enabled_count}"
  else
    echo "${fn}|${last_run}|ACTIVE|${enabled_count}"
  fi
}

# Process list of forks passed as arguments
for fn in "$@"; do
  check_fork "$fn"
done
