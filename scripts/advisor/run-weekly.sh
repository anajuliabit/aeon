#!/usr/bin/env bash
# scripts/advisor/run-weekly.sh — weekly conviction report (Capital-2x phase 4).
#
# Gathers the week's daily advisor findings + performance/pace + scorecard +
# market datablocks, makes ONE inference call (llm-claude.sh: claude-fable-5 on
# the subscription, Virtuals fallback), validates the hard constraints (<=3
# actions, numeric levels, sleeve <= 20%), retries once naming the violation,
# then POSTs as type=weekly and sends a Telegram summary. Idempotent per date.
#
# Runs OUTSIDE the Claude sandbox (workflow step with full env), like run.sh.
set -uo pipefail

BASE="https://investiments-production.up.railway.app"
DATE=$(date -u +%Y-%m-%d)
NOW_ISO=$(date -u +%Y-%m-%dT%H:%M:%SZ)
DRY="${WEEKLY_DRY_RUN:-0}"

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
LLM="$ROOT/scripts/llm-claude.sh"
PROMPTS="$ROOT/advisor/prompts"
D="$ROOT/.investiments-cache/advisor"

DASHBOARD_USER="${DASHBOARD_USER:-admin}"
if [ -z "${DASHBOARD_PASSWORD:-}" ]; then
  echo "run-weekly: DASHBOARD_PASSWORD not set — aborting"; exit 1
fi
AUTH=$(printf '%s:%s' "$DASHBOARD_USER" "$DASHBOARD_PASSWORD" | base64 | tr -d '\n')

api() { curl -fsS --max-time 30 -H "Authorization: Basic ${AUTH}" "$BASE$1" 2>/dev/null || true; }

datablock() { # label, content (skip when empty/null)
  [ -n "$2" ] && [ "$2" != "null" ] && printf '<<<DATA %s>>>\n%s\n<<<END>>>\n' "$1" "$2"
}

filecache() { # label, file, jq-filter
  [ -f "$D/$2" ] || return 0
  local content
  content="$(jq -c "${3:-.}" "$D/$2" 2>/dev/null || true)"
  datablock "$1" "$content"
}

# --- Gather context ---
PERFORMANCE=$(api /api/performance | jq -c '.' 2>/dev/null || true)
SCORECARD_RAW=$(api /api/advisor/scorecard)
SCORECARD=$(printf '%s' "$SCORECARD_RAW" | jq -c '{accuracy, recent: (.grades | sort_by(.gradedAt) | reverse | .[0:15])}' 2>/dev/null || true)

# Quarter-Kelly sleeve ceiling from the measured hit rate (hits vs misses;
# neutrals excluded). Only meaningful once >= 20 graded directional calls.
SIZING=$(printf '%s' "$SCORECARD_RAW" | jq -c '
  ([.grades[]? | select(.result == "hit")] | length) as $h
  | ([.grades[]? | select(.result == "miss")] | length) as $m
  | ($h + $m) as $n
  | if $n >= 20 then
      ($h / $n) as $p
      | {gradedSample: $n, hitRate: ($p * 100 | round / 100),
         quarterKellyPctOfNet: ((([(2 * $p - 1), 0] | max) / 4) * 100 | round),
         rule: "cap sleevePctOfNet at min(quarterKellyPctOfNet, 20)"}
    else
      {gradedSample: $n, rule: "insufficient graded sample (<20) — default 15-20% band applies"}
    end' 2>/dev/null || true)

WEEK_FINDINGS="[]"
for d in 0 1 2 3 4 5 6; do
  DAY=$(date -u -d "-${d} days" +%Y-%m-%d 2>/dev/null || date -u -v-${d}d +%Y-%m-%d)
  RUN=$(api "/api/advisor/run?date=$DAY")
  SLIM=$(printf '%s' "$RUN" | jq -c '{date: .date,
    summary: (.report.summary // null),
    recommendations: [(.report.recommendations // [])[] | {title, urgency, confidence, symbol, direction}],
    theses: [(.findings // {}) | to_entries[] | {role: .key, thesis: .value.thesis}]}' 2>/dev/null || true)
  [ -n "$SLIM" ] && [ "$SLIM" != "null" ] && \
    WEEK_FINDINGS=$(printf '%s' "$WEEK_FINDINGS" | jq -c --argjson day "$SLIM" '. + [$day]')
done

PROMPT="$(cat "$PROMPTS/weekly_conviction.md")
$(datablock performance "$PERFORMANCE")
$(datablock scorecard "$SCORECARD")
$(datablock sizing "$SIZING")
$(datablock week_reports "$WEEK_FINDINGS")
$(filecache snapshot snapshot.json '{totalUsd, analytics:{allocation:.analytics.allocation, assets:.analytics.assets, vesting:[.analytics.vesting[]? | del(.upcoming)], grossAssetsUsd:.analytics.grossAssetsUsd, totalLiabilitiesUsd:.analytics.totalLiabilitiesUsd}}')
$(filecache liquidity gt-liquidity.json '.')
$(filecache funding hl-funding.json '.')
$(filecache macro macro-upcoming.json '.')"

# --- Validation gate ---
# Sleeve cap: 20% by default, tightened to the quarter-Kelly ceiling once the
# graded sample is large enough (mirrors the prompt's sizing rule — enforced
# here so a model that ignores it cannot ship an oversized action).
SLEEVE_CAP=$(printf '%s' "$SIZING" | jq -r 'if .quarterKellyPctOfNet != null then ([.quarterKellyPctOfNet, 20] | min) else 20 end' 2>/dev/null || echo 20)
case "$SLEEVE_CAP" in (*[!0-9.]*|"") SLEEVE_CAP=20 ;; esac
validate() { # report-json -> prints violation list (empty = valid)
  printf '%s' "$1" | jq -r --argjson cap "$SLEEVE_CAP" '
    [ (if (.actions | length) > 3 then "more than 3 actions" else empty end),
      (.actions[]? | select(.entry == null or .exit == null or .invalidate == null)
        | "action \"\(.thesis[0:40])\" missing numeric entry/exit/invalidate"),
      (.actions[]? | select((.sleevePctAfter // 99) > $cap)
        | "action \"\(.thesis[0:40])\" exceeds the \($cap)% sleeve cap"),
      (if (.paceVerdict.comment // "") == "" then "missing paceVerdict.comment" else empty end)
    ] | join("; ")' 2>/dev/null || echo "unparseable report"
}

extract_json() {
  python3 -c '
import json, sys
raw = sys.stdin.read()
dec = json.JSONDecoder()
i = raw.find("{")
while i != -1:
    try:
        obj, _ = dec.raw_decode(raw, i)
        if isinstance(obj, dict):
            print(json.dumps(obj))
            break
    except ValueError:
        pass
    i = raw.find("{", i + 1)
'
}

REPORT="$(printf '%s' "$PROMPT" | "$LLM" | extract_json)"
VIOLATIONS=""
if [ -n "$REPORT" ]; then VIOLATIONS="$(validate "$REPORT")"; else VIOLATIONS="empty completion"; fi

if [ -n "$VIOLATIONS" ]; then
  echo "run-weekly: retrying once (violations: $VIOLATIONS)"
  REPORT="$(printf '%s\n\nYOUR PREVIOUS ATTEMPT VIOLATED: %s\nFix those violations. Output ONLY the JSON object.' \
    "$PROMPT" "$VIOLATIONS" | "$LLM" | extract_json)"
  [ -n "$REPORT" ] && VIOLATIONS="$(validate "$REPORT")" || VIOLATIONS="empty completion"
fi

if [ -z "$REPORT" ]; then
  echo "::warning::run-weekly: no valid report produced — nothing posted"; exit 1
fi

# Surviving violations get flagged in-band rather than silently posted.
if [ -n "$VIOLATIONS" ]; then
  REPORT=$(printf '%s' "$REPORT" | jq --arg v "$VIOLATIONS" \
    '.riskCheck.gates = ((.riskCheck.gates // []) + ["DEGRADED REPORT — unresolved validation: " + $v])')
fi
REPORT=$(printf '%s' "$REPORT" | jq --arg ts "$NOW_ISO" '.generatedAt = $ts
  | .disclaimer = (.disclaimer // "Not financial advice. For informational purposes only.")')

# Deterministic vesting-policy enforcement (mirrors run.sh): REPPO is a standing
# conviction hold — a REPPO "decrease" action is reframed as optional, and its
# thesis says so; MAMO/WELL partial-sale actions get the sell-100% reminder.
REPORT=$(printf '%s' "$REPORT" | jq -c '
  .actions = [(.actions // [])[]
    | if (.symbol // "" | ascii_upcase) == "REPPO" and .direction == "decrease" then
        .thesis = "OPTIONAL (policy: REPPO conviction hold; profit-taking only) — " + (.thesis // "")
      elif ((.symbol // "" | ascii_upcase) as $s | ($s == "MAMO" or $s == "WELL")) and .direction == "decrease" then
        .thesis = ((.thesis // "") + " [policy: sell 100% of every MAMO/WELL unlock on claim.]")
      else . end]')

if [ "$DRY" = "1" ]; then
  echo "----- WEEKLY REPORT (dry) -----"; printf '%s\n' "$REPORT" | jq .
  exit 0
fi

if curl -fsS --max-time 30 -X POST "$BASE/api/advisor/report" \
    -H "Authorization: Basic ${AUTH}" -H "Content-Type: application/json" \
    -d "$(jq -n --arg d "$DATE" --argjson r "$REPORT" '{date: $d, type: "weekly", report: $r}')" >/dev/null 2>&1; then
  echo "run-weekly: weekly report posted"
  # Track each numeric action as a pick so weekly conviction calls land in
  # the same track record as token-pick. Actions without a mappable symbol
  # (portfolio-level advice) are skipped — grade-recs.sh covers those.
  REFS="$ROOT/advisor/token-refs.json"
  # Only directional calls become picks: increase = long, hedge = short.
  # decrease (reduce-a-long) and hold are de-risking moves, not bets —
  # mislabeling them as shorts would distort the track record.
  printf '%s' "$REPORT" | jq -c '.actions[]?
    | select(.symbol != null and .entry != null)
    | select(.direction == "increase" or .direction == "hedge")' |
  while read -r action; do
    SYM=$(printf '%s' "$action" | jq -r '.symbol')
    SYM_KEY=$(printf '%s' "$SYM" | tr '[:upper:]' '[:lower:]' | tr -cd 'a-z0-9')
    CG_ID=$(jq -r --arg s "$SYM_KEY" '.[$s] // empty' "$REFS" 2>/dev/null)
    if [ -z "$CG_ID" ]; then
      echo "run-weekly: no coingecko id for $SYM — action not tracked as pick"
      continue
    fi
    PICK=$(printf '%s' "$action" | jq -c --arg d "$DATE" --arg cg "$CG_ID" '{
      id: ($d + "-advisor-" + (.symbol | ascii_downcase)),
      source: "advisor",
      symbol: .symbol,
      coingeckoId: $cg,
      side: (if .direction == "hedge" then "short" else "long" end),
      entryPriceUsd: .entry,
      targetPriceUsd: .exit,
      invalidationPriceUsd: .invalidate,
      horizonDays: (.horizonDays // 30),
      conviction: "UNSTATED",
      thesis: (.thesis + " | wrong if: " + (.wrongIf // "unstated"))
    }')
    curl -fsS --max-time 30 -X POST "$BASE/api/picks" \
      -H "Authorization: Basic ${AUTH}" \
      -H "Content-Type: application/json" \
      -d "$PICK" >/dev/null 2>&1 \
      || echo "::warning::run-weekly: pick POST failed for $SYM"
  done
else
  echo "::warning::run-weekly: report POST failed"
fi

if [ -n "${TELEGRAM_BOT_TOKEN:-}" ] && [ -n "${TELEGRAM_CHAT_ID:-}" ]; then
  TG="$(printf '%s' "$REPORT" | jq -r --arg d "$DATE" '
    "🎯 Weekly conviction (" + $d + "): pace " + (if .paceVerdict.onPace then "ON" else "OFF" end) +
    " — " + (.paceVerdict.comment // "") + "\n" +
    (if (.actions | length) == 0 then "No new actions this week."
     else ([.actions[] | "• " + (.symbol // "portfolio") + " " + .direction + ": " + (.thesis[0:120])] | join("\n")) end) +
    "\nNot financial advice."')"
  curl -fsS --max-time 20 "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
    --data-urlencode "chat_id=${TELEGRAM_CHAT_ID}" \
    --data-urlencode "text=$TG" >/dev/null 2>&1 \
    && echo "run-weekly: telegram sent" \
    || echo "::warning::run-weekly: telegram send failed"
fi
echo "run-weekly: done ($DATE)"
