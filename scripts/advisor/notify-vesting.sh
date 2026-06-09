#!/usr/bin/env bash
# scripts/advisor/notify-vesting.sh — vesting claim/unlock Telegram alerts.
#
# Reads analytics.vesting from the prefetched snapshot (see prefetch-data.sh)
# and notifies when:
#   1. a vesting position has a claimable balance >= $CLAIM_MIN_USD (daily
#      reminder until claimed — claiming zeroes claimableUsd and silences it);
#   2. the next unlock is within UPCOMING_DAYS (heads-up before the tranche).
#
# Deterministic — no LLM. Runs OUTSIDE the Claude sandbox (workflow step with
# full env), same as run.sh. Silently no-ops without snapshot or Telegram env.
set -uo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
SNAP="$ROOT/.investiments-cache/advisor/snapshot.json"
CLAIM_MIN_USD="${CLAIM_MIN_USD:-50}"
UPCOMING_DAYS="${UPCOMING_DAYS:-3}"

[ -f "$SNAP" ] || { echo "notify-vesting: no snapshot — skipping"; exit 0; }
[ -n "${TELEGRAM_BOT_TOKEN:-}" ] && [ -n "${TELEGRAM_CHAT_ID:-}" ] || {
  echo "notify-vesting: telegram not configured — skipping"; exit 0;
}

NOW_S=$(date -u +%s)
HORIZON_S=$((NOW_S + UPCOMING_DAYS * 86400))

# Claimable now: unlocked-but-unwithdrawn balance above the floor.
CLAIMS="$(jq -r --argjson min "$CLAIM_MIN_USD" '
  [.analytics.vesting[]? | select((.claimableUsd // 0) >= $min)
   | "• \(.symbol // "?") (\(.protocol)): \(.claimableQty | floor) claimable (~$\(.claimableUsd | floor)) — claim it"]
  | join("\n")' "$SNAP" 2>/dev/null || true)"

# Upcoming unlocks inside the horizon.
UPCOMING="$(jq -r --argjson now "$NOW_S" --argjson hor "$HORIZON_S" '
  [.analytics.vesting[]? | select(.nextUnlockAt != null)
   | (.nextUnlockAt | sub("\\.[0-9]+Z$"; "Z") | fromdateiso8601? // empty) as $t
   | select($t > $now and $t <= $hor)
   | "• \(.symbol // "?") (\(.protocol)): \(.nextUnlockQty | floor) (~$\(.nextUnlockUsd // 0 | floor)) unlocks \(.nextUnlockAt[0:10])"]
  | join("\n")' "$SNAP" 2>/dev/null || true)"

[ -z "$CLAIMS" ] && [ -z "$UPCOMING" ] && { echo "notify-vesting: nothing to report"; exit 0; }

MSG="🔓 Vesting update"
[ -n "$CLAIMS" ] && MSG="$MSG
Claimable now:
$CLAIMS"
[ -n "$UPCOMING" ] && MSG="$MSG
Unlocking within ${UPCOMING_DAYS}d:
$UPCOMING"
MSG="$MSG
Not financial advice."

curl -fsS --max-time 20 "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
  --data-urlencode "chat_id=${TELEGRAM_CHAT_ID}" \
  --data-urlencode "text=$MSG" >/dev/null 2>&1 \
  && echo "notify-vesting: sent" \
  || echo "::warning::notify-vesting: telegram send failed"
