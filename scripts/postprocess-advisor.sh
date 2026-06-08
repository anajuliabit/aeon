#!/usr/bin/env bash
# Post-process advisor skill output AFTER Claude exits, with full env access.
# Skills write JSON to .pending-advisor/; this POSTs each to the private investiments API,
# and sends .pending-advisor/telegram.txt to Telegram directly. No-op if nothing queued.
#
#   run.json                       → POST /api/advisor/run
#   finding-<role>.json            → POST /api/advisor/finding   (wraps as {date,role,finding})
#   debate.json                    → POST /api/advisor/debate    (wraps as {date,debate})
#   report.json                    → POST /api/advisor/report    (wraps as {date,report})
#   telegram.txt                   → Telegram sendMessage
set -uo pipefail

DIR=".pending-advisor"
[ -d "$DIR" ] || { echo "postprocess-advisor: nothing queued, skipping"; exit 0; }

BASE="${INVESTIMENTS_BASE_URL:-https://investiments-production.up.railway.app}"
TODAY=$(date -u +%Y-%m-%d)

post() { # $1=path  $2=json-body
  if [ -z "${INVESTIMENTS_BASIC_AUTH:-}" ]; then
    echo "::warning::postprocess-advisor: INVESTIMENTS_BASIC_AUTH not set, cannot POST $1"; return 0
  fi
  curl -fsS --max-time 30 -X POST \
    -H "Authorization: Basic ${INVESTIMENTS_BASIC_AUTH}" \
    -H "content-type: application/json" \
    -d "$2" "${BASE}${1}" >/dev/null \
    && echo "postprocess-advisor: POST $1 ok" \
    || echo "::warning::postprocess-advisor: POST $1 failed"
}

# run init
if [ -f "$DIR/run.json" ]; then
  post "/api/advisor/run" "$(jq -n --arg d "$TODAY" '{date:$d}')"
fi

# findings (one per role)
shopt -s nullglob
for f in "$DIR"/finding-*.json; do
  role=$(jq -r '.role // empty' "$f")
  [ -z "$role" ] && { echo "::warning::$f missing .role, skipping"; continue; }
  body=$(jq -n --arg d "$TODAY" --arg r "$role" --slurpfile fnd "$f" \
    '{date:$d, role:$r, finding:$fnd[0]}')
  post "/api/advisor/finding" "$body"
done

# debate
if [ -f "$DIR/debate.json" ]; then
  body=$(jq -n --arg d "$TODAY" --slurpfile deb "$DIR/debate.json" '{date:$d, debate:$deb[0]}')
  post "/api/advisor/debate" "$body"
fi

# report
if [ -f "$DIR/report.json" ]; then
  body=$(jq -n --arg d "$TODAY" --slurpfile rep "$DIR/report.json" '{date:$d, report:$rep[0]}')
  post "/api/advisor/report" "$body"
fi

# telegram summary (direct — bypasses ./notify so nothing commits to public main)
if [ -f "$DIR/telegram.txt" ] && [ -n "${TELEGRAM_BOT_TOKEN:-}" ] && [ -n "${TELEGRAM_CHAT_ID:-}" ]; then
  TEXT=$(cat "$DIR/telegram.txt")
  curl -fsS --max-time 30 -X POST \
    "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
    --data-urlencode "chat_id=${TELEGRAM_CHAT_ID}" \
    --data-urlencode "text=${TEXT}" \
    --data-urlencode "disable_web_page_preview=true" >/dev/null \
    && echo "postprocess-advisor: telegram sent" \
    || echo "::warning::postprocess-advisor: telegram send failed"
fi

exit 0
