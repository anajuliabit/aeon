#!/usr/bin/env bash
# scripts/advisor/notify-drawdown.sh — portfolio drawdown Telegram alert.
#
# Reads /api/history and alerts when the CURRENT drawdown from the all-time
# ledger peak crosses into a deeper band (10% / 15% / 20% / 30%). Stateless
# dedupe: it alerts only when TODAY's band is deeper than YESTERDAY's, so each
# band fires once per leg down (and re-arms after recovery to a shallower band).
#
# Deterministic — no LLM. Runs OUTSIDE the Claude sandbox (workflow step with
# full env). Silently no-ops without creds/Telegram or with < 3 ledger days.
set -uo pipefail

BASE="https://investiments-production.up.railway.app"
BANDS="${DRAWDOWN_BANDS:-10 15 20 30}"

DASHBOARD_USER="${DASHBOARD_USER:-admin}"
if [ -z "${DASHBOARD_PASSWORD:-}" ] || [ -z "${TELEGRAM_BOT_TOKEN:-}" ] || [ -z "${TELEGRAM_CHAT_ID:-}" ]; then
  echo "notify-drawdown: creds or telegram not configured — skipping"; exit 0
fi
AUTH=$(printf '%s:%s' "$DASHBOARD_USER" "$DASHBOARD_PASSWORD" | base64 | tr -d '\n')

HISTORY=$(curl -fsS --max-time 30 -H "Authorization: Basic ${AUTH}" "$BASE/api/history" 2>/dev/null || true)
N=$(printf '%s' "$HISTORY" | jq 'length' 2>/dev/null || echo 0)
if [ "${N:-0}" -lt 3 ]; then
  echo "notify-drawdown: ledger too short ($N days) — skipping"; exit 0
fi

# Drawdown (pct from running peak) at the latest entry and at the previous one.
DD=$(printf '%s' "$HISTORY" | jq '
  [.[] | select((.totalUsd // 0) > 0)] as $h
  | if ($h | length) < 2 then {today: null, prev: null} else
      [range($h | length) as $i |
        {date: $h[$i].date,
         dd: ((([$h[range(0; $i + 1)].totalUsd] | max) as $peak
              | if $peak > 0 then ($peak - $h[$i].totalUsd) / $peak * 100 else 0 end))}]
      | {today: .[-1], prev: .[-2]}
    end' 2>/dev/null || true)
TODAY_DD=$(printf '%s' "$DD" | jq -r '.today.dd // empty')
PREV_DD=$(printf '%s' "$DD" | jq -r '.prev.dd // empty')
if [ -z "$TODAY_DD" ] || [ -z "$PREV_DD" ]; then
  echo "notify-drawdown: dd computation failed"; exit 0
fi

band() { # ddPct -> deepest band crossed (0 if none)
  local out=0 b
  for b in $BANDS; do
    if python3 -c "exit(0 if $1 >= $b else 1)"; then out=$b; fi
  done
  echo "$out"
}
TODAY_BAND=$(band "$TODAY_DD")
PREV_BAND=$(band "$PREV_DD")

echo "notify-drawdown: dd today $(printf '%.1f' "$TODAY_DD")% (band $TODAY_BAND), prev $(printf '%.1f' "$PREV_DD")% (band $PREV_BAND)"
if [ "$TODAY_BAND" -le "$PREV_BAND" ] || [ "$TODAY_BAND" -eq 0 ]; then
  echo "notify-drawdown: no new band crossed"; exit 0
fi

TOTAL=$(printf '%s' "$HISTORY" | jq -r '.[-1].totalUsd // empty')
case "$TOTAL" in (*[!0-9.]*|"") TOTAL=0 ;; esac
MSG=$(printf '📉 Portfolio drawdown alert: −%.1f%% from the ledger peak (crossed the %s%% band). Net worth ~$%.0fk. Review the risk sleeve and the cbBTC structure per the 2× program rules. Not financial advice.' \
  "$TODAY_DD" "$TODAY_BAND" "$(python3 -c "print($TOTAL/1000)")")
curl -fsS --max-time 20 "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
  --data-urlencode "chat_id=${TELEGRAM_CHAT_ID}" \
  --data-urlencode "text=$MSG" >/dev/null 2>&1 \
  && echo "notify-drawdown: sent (band $TODAY_BAND)" \
  || echo "::warning::notify-drawdown: telegram send failed"
