#!/usr/bin/env bash
# scripts/advisor/grade-recs.sh — deterministic recommendation grading.
#
# For each daily advisor report in the last LOOKBACK_DAYS whose recommendations
# have matured (report date + horizonDays <= today) and are not yet graded:
#   - symbol recs: CoinGecko price at report date vs date+horizon; graded by
#     direction correctness (>=5% in the called direction = hit, >=5% against =
#     miss, else neutral; "hold" is neutral unless <= -25% = miss; "hedge" is
#     graded like "decrease" — it calls for reducing net exposure).
#   - no-symbol recs (portfolio-level): /api/history totalUsd growth over the
#     horizon vs the 2x pace trajectory growth (beat = hit, trail >5% = miss).
#   - unmappable symbols (absent from advisor/token-refs.json) grade neutral
#     with an explanatory detail.
# Grades are POSTed back to /api/advisor/scorecard (idempotent upsert).
#
# Deterministic — no LLM. Runs OUTSIDE the Claude sandbox with DASHBOARD creds.
# Sandbox note: must run from a workflow step with full env (like run.sh).
set -uo pipefail

BASE="https://investiments-production.up.railway.app"
LOOKBACK_DAYS="${LOOKBACK_DAYS:-120}"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
REFS="$ROOT/advisor/token-refs.json"
TODAY_S=$(date -u +%s)

DASHBOARD_USER="${DASHBOARD_USER:-admin}"
if [ -z "${DASHBOARD_PASSWORD:-}" ]; then
  echo "grade-recs: DASHBOARD_PASSWORD not set — skipping"; exit 0
fi
AUTH=$(printf '%s:%s' "$DASHBOARD_USER" "$DASHBOARD_PASSWORD" | base64 | tr -d '\n')

api() { # path -> body (empty on failure)
  curl -fsS --max-time 30 -H "Authorization: Basic ${AUTH}" "$BASE$1" 2>/dev/null || true
}

# CoinGecko daily price for a coin id around a unix-seconds moment (±12h window).
cg_price_at() { # id, unixSec -> price or empty
  local from=$(( $2 - 43200 )) to=$(( $2 + 43200 ))
  curl -fsS --max-time 30 \
    "https://api.coingecko.com/api/v3/coins/$1/market_chart/range?vs_currency=usd&from=${from}&to=${to}" \
    2>/dev/null | jq -r '.prices[0][1] // empty' 2>/dev/null || true
}

SCORECARD=$(api /api/advisor/scorecard)
HISTORY=$(api /api/history)
GRADES="[]"

d=0
while [ "$d" -le "$LOOKBACK_DAYS" ]; do
  DATE=$(date -u -d "-${d} days" +%Y-%m-%d 2>/dev/null || date -u -v-${d}d +%Y-%m-%d)
  d=$((d + 1))
  RUN=$(api "/api/advisor/run?date=$DATE")
  RECS=$(printf '%s' "$RUN" | jq -c '.report.recommendations // []' 2>/dev/null || echo "[]")
  [ "$RECS" = "[]" ] && continue
  N=$(printf '%s' "$RECS" | jq 'length')

  i=0
  while [ "$i" -lt "$N" ]; do
    REC=$(printf '%s' "$RECS" | jq -c ".[$i]")
    IDX=$i
    i=$((i + 1))

    # Skip if already graded.
    DONE=$(printf '%s' "$SCORECARD" | jq --arg dt "$DATE" --argjson ix "$IDX" \
      '[.grades[]? | select(.date == $dt and .index == $ix)] | length' 2>/dev/null || echo 0)
    [ "${DONE:-0}" -gt 0 ] && continue

    HORIZON=$(printf '%s' "$REC" | jq -r '.horizonDays // empty')
    case "$HORIZON" in 30|60|90) ;; *) continue ;; esac # pre-phase-3 reports lack the contract → skip
    DATE_S=$(date -u -d "$DATE" +%s 2>/dev/null || date -u -j -f %Y-%m-%d "$DATE" +%s)
    MATURE_S=$(( DATE_S + HORIZON * 86400 ))
    [ "$MATURE_S" -gt "$TODAY_S" ] && continue # not matured yet

    TITLE=$(printf '%s' "$REC" | jq -r '.title // "untitled"')
    # Sanitize LLM-sourced fields before any further use: symbol to [a-z0-9],
    # direction to the closed enum (anything else grades as "hold").
    SYMBOL=$(printf '%s' "$REC" | jq -r '.symbol // empty' | tr '[:upper:]' '[:lower:]' | tr -cd 'a-z0-9')
    DIRECTION=$(printf '%s' "$REC" | jq -r '.direction // "hold"')
    case "$DIRECTION" in increase|decrease|hold|hedge) ;; *) DIRECTION="hold" ;; esac
    ANALYSTS=$(printf '%s' "$REC" | jq -c '.supportingRoles // []')
    RESULT="neutral"; DETAIL=""

    if [ -n "$SYMBOL" ]; then
      CGID=$(jq -r --arg s "$SYMBOL" '.[$s] // empty' "$REFS" 2>/dev/null || true)
      if [ -z "$CGID" ]; then
        DETAIL="unmapped symbol $SYMBOL (not in token-refs.json)"
      else
        P0=$(cg_price_at "$CGID" "$DATE_S"); sleep 2
        P1=$(cg_price_at "$CGID" "$MATURE_S"); sleep 2
        if [ -n "$P0" ] && [ -n "$P1" ]; then
          MOVE=$(python3 -c "print(($P1/$P0 - 1) * 100)")
          case "$DIRECTION" in
            increase) RESULT=$(python3 -c "m=$MOVE; print('hit' if m>=5 else 'miss' if m<=-5 else 'neutral')") ;;
            decrease|hedge) RESULT=$(python3 -c "m=$MOVE; print('hit' if m<=-5 else 'miss' if m>=5 else 'neutral')") ;;
            hold) RESULT=$(python3 -c "m=$MOVE; print('miss' if m<=-25 else 'neutral')") ;;
          esac
          DETAIL=$(printf '%s %+.1f%% over %sd vs "%s"' "$SYMBOL" "$MOVE" "$HORIZON" "$DIRECTION")
        else
          DETAIL="price data unavailable for $CGID"
        fi
      fi
    else
      # Portfolio-level: totalUsd growth over the horizon vs trajectory growth.
      # The T0 entry must be within 3 days of the rec date (a far-later first
      # entry would grade the rec against the wrong baseline).
      T0LIMIT=$(date -u -d "@$(( DATE_S + 3*86400 ))" +%Y-%m-%d 2>/dev/null || date -u -r "$(( DATE_S + 3*86400 ))" +%Y-%m-%d)
      T0=$(printf '%s' "$HISTORY" | jq --arg d0 "$DATE" --arg lim "$T0LIMIT" -r \
        '[.[] | select(.date >= $d0 and .date <= $lim)] | first.totalUsd // empty' 2>/dev/null || true)
      MATURE_DATE=$(date -u -d "@$MATURE_S" +%Y-%m-%d 2>/dev/null || date -u -r "$MATURE_S" +%Y-%m-%d)
      T1=$(printf '%s' "$HISTORY" | jq --arg d1 "$MATURE_DATE" -r '[.[] | select(.date >= $d1)] | first.totalUsd // empty' 2>/dev/null || true)
      if [ -n "$T0" ] && [ -n "$T1" ]; then
        # Required growth over the horizon on the $1M-by-2028-12-31 trajectory:
        # (1M/336948)^(horizon/934) (934-day runway 2026-06-10 → 2028-12-31;
        # grading approximation, matches investiments /api/performance pace).
        VERDICT=$(python3 -c "
actual = $T1/$T0 - 1
needed = (1000000/336948) ** ($HORIZON/934) - 1
print('hit' if actual >= needed else 'miss' if actual < needed - 0.05 else 'neutral')")
        RESULT="$VERDICT"
        PCT=$(python3 -c "print(($T1/$T0 - 1)*100)")
        DETAIL=$(printf 'portfolio %+.1f%% over %sd vs pace' "$PCT" "$HORIZON")
      else
        DETAIL="insufficient history to grade portfolio-level rec"
      fi
    fi

    GRADES=$(printf '%s' "$GRADES" | jq \
      --arg date "$DATE" --argjson index "$IDX" --arg title "$TITLE" \
      --arg symbol "$SYMBOL" --arg direction "$DIRECTION" --argjson horizon "$HORIZON" \
      --arg gradedAt "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --arg result "$RESULT" \
      --arg detail "$DETAIL" --argjson analysts "$ANALYSTS" \
      '. + [{date: $date, index: $index, title: $title,
             symbol: (if $symbol == "" then null else ($symbol | ascii_upcase) end),
             direction: $direction, horizonDays: $horizon, gradedAt: $gradedAt,
             result: $result, detail: $detail, analysts: $analysts}]')
  done
done

COUNT=$(printf '%s' "$GRADES" | jq 'length')
if [ "$COUNT" -eq 0 ]; then
  echo "grade-recs: nothing matured to grade"; exit 0
fi

if curl -fsS --max-time 30 -X POST "$BASE/api/advisor/scorecard" \
    -H "Authorization: Basic ${AUTH}" -H "Content-Type: application/json" \
    -d "$(jq -n --argjson g "$GRADES" '{grades: $g}')" >/dev/null 2>&1; then
  echo "grade-recs: posted $COUNT grades"
else
  echo "::warning::grade-recs: scorecard POST failed ($COUNT grades dropped)"
fi
