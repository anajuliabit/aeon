#!/usr/bin/env bash
# scripts/advisor/run.sh — Virtuals single-shot advisory orchestrator.
#
# Pipeline (all inference via scripts/llm.sh on Virtuals, model claude-opus-4-8):
#   prefetch already ran -> .investiments-cache/advisor/*.json
#   per analyst: prompt(template + relevant datablocks) | llm.sh -> JSON finding -> POST /finding
#   debate: debate.md + findings -> JSON -> POST /debate
#   PM: portfolio_manager.md + findings + debate -> report JSON -> POST /report + Telegram summary
#
# Advisory only. Prints ONLY non-sensitive status lines (role + ok/gap) — never dollar amounts.
#
# DRY_RUN: set ADVISOR_DRY_RUN=1 to do everything EXCEPT POSTs + Telegram; instead each produced
# JSON is printed to stdout for local validation (no side effects).
#
# Runs OUTSIDE the Claude sandbox (workflow step with full env).
set -uo pipefail

export VIRTUALS_MODEL=claude-opus-4-8   # NEVER deepseek; free + hallucination-safe on Virtuals.

BASE="${INVESTIMENTS_BASE_URL:-https://investiments-production.up.railway.app}"
DATE=$(date -u +%Y-%m-%d)

# Build the Basic-auth token at runtime from the dashboard creds (avoids
# pre-encoding mistakes). DASHBOARD_USER defaults to "admin" (investiments default).
DASHBOARD_USER="${DASHBOARD_USER:-admin}"
AUTH=$(printf '%s:%s' "$DASHBOARD_USER" "${DASHBOARD_PASSWORD:-}" | base64 | tr -d '\n')
NOW_ISO=$(date -u +%Y-%m-%dT%H:%M:%SZ)
DRY="${ADVISOR_DRY_RUN:-0}"

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
LLM="$ROOT/scripts/llm.sh"
PROMPTS="$ROOT/advisor/prompts"
D="$ROOT/.investiments-cache/advisor"
WORK="$D/work"
mkdir -p "$WORK"

FINDINGS="$WORK/findings.json"   # accumulator: JSON array of analyst findings
echo "[]" > "$FINDINGS"
GAPS=()                          # roles that failed

# ---------------------------------------------------------------------------
# extract_json: strip ``` fences then emit the first balanced {...}.
# The extractor python lives in a tempfile so the LLM output stays on STDIN
# (a `python3 - <<HEREDOC` would consume the heredoc as stdin, not the pipe).
# ---------------------------------------------------------------------------
EXTRACTOR="$WORK/extract_json.py"
cat > "$EXTRACTOR" <<'PY'
import sys
s = sys.stdin.read()
s = s.replace("```json", "").replace("```JSON", "").replace("```", "")
start = s.find("{")
if start < 0:
    sys.exit(0)
depth = 0
in_str = False
esc = False
for i in range(start, len(s)):
    c = s[i]
    if in_str:
        if esc:
            esc = False
        elif c == "\\":
            esc = True
        elif c == '"':
            in_str = False
    else:
        if c == '"':
            in_str = True
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                sys.stdout.write(s[start:i+1])
                sys.exit(0)
PY

extract_json() {
  python3 "$EXTRACTOR"
}

# complete: pipe a prompt to llm.sh, extract + validate JSON; retry once on failure.
# Prints validated JSON to stdout, or nothing (returns 1) on second failure.
complete() {
  local prompt="$1"
  local raw json
  raw="$(printf '%s' "$prompt" | "$LLM" 2>/dev/null || true)"
  json="$(printf '%s' "$raw" | extract_json)"
  if [ -n "$json" ] && printf '%s' "$json" | jq -e . >/dev/null 2>&1; then
    printf '%s' "$json"; return 0
  fi
  raw="$(printf '%s\n\nReturn ONLY valid JSON, no prose.' "$prompt" | "$LLM" 2>/dev/null || true)"
  json="$(printf '%s' "$raw" | extract_json)"
  if [ -n "$json" ] && printf '%s' "$json" | jq -e . >/dev/null 2>&1; then
    printf '%s' "$json"; return 0
  fi
  return 1
}

# POST helper (skipped in DRY_RUN). Args: path, json-body
post() {
  local path="$1" body="$2"
  if [ "$DRY" = "1" ]; then return 0; fi
  curl -fsS --max-time 30 -X POST "$BASE$path" \
    -H "Authorization: Basic ${AUTH}" \
    -H "Content-Type: application/json" \
    -d "$body" >/dev/null 2>&1 || echo "::warning::advisor: POST $path failed"
}

# Wrap a cached file (or a jq slice) as a delimited datablock. No-op if file absent/empty.
# Args: label, file, [jq-filter]
datablock() {
  local label="$1" file="$2" filt="${3:-.}"
  [ -f "$D/$file" ] || return 0
  local content
  content="$(jq -c "$filt" "$D/$file" 2>/dev/null || true)"
  [ -n "$content" ] || return 0
  printf '<<<DATA %s>>>\n%s\n<<<END>>>\n' "$label" "$content"
}

# Held symbols (lowercase) from the snapshot, for filtering big feeds. Empty if no snapshot.
held_symbols() {
  [ -f "$D/snapshot.json" ] || return 0
  jq -r '[.analytics.assets[]?.symbol // .positions[]?.symbol // empty] | map(ascii_downcase) | unique | join(" ")' \
    "$D/snapshot.json" 2>/dev/null || true
}

# ---------------------------------------------------------------------------
# 0. Snapshot gate
# ---------------------------------------------------------------------------
if [ ! -f "$D/snapshot.json" ] || ! jq -e '.totalUsd' "$D/snapshot.json" >/dev/null 2>&1; then
  echo "advisor: no portfolio snapshot — aborting analysts"
  REPORT=$(jq -n --arg ts "$NOW_ISO" '{
    generatedAt: $ts,
    summary: "Run aborted: portfolio snapshot unavailable.",
    recommendations: [],
    findings: [],
    debate: {turns: []},
    modelInfo: {analysts: "claude-opus-4-8 (Virtuals)", pm: "claude-opus-4-8 (Virtuals)"},
    dataSources: {used: [], unavailable: ["snapshot"]},
    gaps: ["snapshot"],
    disclaimer: "Not financial advice. For informational purposes only."
  }')
  if [ "$DRY" = "1" ]; then
    echo "----- REPORT (abort) -----"; printf '%s\n' "$REPORT" | jq .
  else
    post "/api/advisor/report" "$(jq -n --arg d "$DATE" --argjson r "$REPORT" '{date:$d, report:$r}')"
    if [ -n "${TELEGRAM_BOT_TOKEN:-}" ] && [ -n "${TELEGRAM_CHAT_ID:-}" ]; then
      curl -fsS --max-time 20 "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
        --data-urlencode "chat_id=${TELEGRAM_CHAT_ID}" \
        --data-urlencode "text=⚠️ Advisor run aborted: no portfolio snapshot. Not financial advice." \
        >/dev/null 2>&1 || echo "::warning::advisor: telegram send failed"
    fi
  fi
  exit 0
fi

# ---------------------------------------------------------------------------
# 1. Init run
# ---------------------------------------------------------------------------
post "/api/advisor/run" "$(jq -n --arg d "$DATE" '{date:$d}')"
echo "advisor: run initialized ($DATE)"

HELD="$(held_symbols)"

# Per-role data context (only the role's relevant cached files, compacted with jq).
role_data() {
  case "$1" in
    risk_leverage)
      datablock snapshot snapshot.json '{totalUsd, positions, analytics}'
      ;;
    yield_allocation)
      datablock snapshot snapshot.json '{totalUsd, analytics:{allocation:.analytics.allocation, assets:.analytics.assets}}'
      datablock yields yields.json '[.data[]? | select(.stablecoin == true) | {project,symbol,chain,tvlUsd,apyBase,apyReward,apy}] | sort_by(-(.tvlUsd // 0)) | .[0:40]'
      datablock fees fees.json '{total24h: .total24h, protocols: [.protocols[]? | {name, total24h, total7d}] | .[0:30]}'
      ;;
    market_macro)
      datablock cg_global cg-global.json '{total_market_cap_usd: .data.total_market_cap.usd, market_cap_pct: .data.market_cap_percentage, market_cap_change_24h: .data.market_cap_change_percentage_24h_usd}'
      datablock cg_btc cg-btc.json '{daily_closes_usd: ([.prices[]? | .[1]] | [range(0; length; 24) as $i | .[$i]]), latest_usd: (.prices[-1][1]? // null)}'
      datablock fng fng.json '.'
      datablock x_search x-search.json '.'
      ;;
    fundamentals)
      datablock snapshot snapshot.json '{analytics:{assets:.analytics.assets}}'
      datablock protocols protocols.json '[.[]? | {name, symbol, tvl, change_1d, change_7d}] | sort_by(-(.tvl // 0)) | .[0:60]'
      datablock fees fees.json '{protocols: [.protocols[]? | {name, total24h, total7d}] | .[0:40]}'
      datablock cg_markets cg-markets.json '[.[]? | {symbol, name, market_cap, fully_diluted_valuation, circulating_supply, total_supply, price_change_percentage_24h}] | .[0:60]'
      ;;
    news_social)
      datablock fng fng.json '.'
      datablock x_search x-search.json '.'
      ;;
  esac
}

# ---------------------------------------------------------------------------
# 2. Analysts
# ---------------------------------------------------------------------------
ANALYSTS="risk_leverage yield_allocation market_macro fundamentals news_social"
for role in $ANALYSTS; do
  tmpl="$PROMPTS/$role.md"
  if [ ! -f "$tmpl" ]; then
    echo "advisor: $role gap (no template)"; GAPS+=("$role"); continue
  fi
  prompt="$(cat "$tmpl")
HELD SYMBOLS (from snapshot): ${HELD:-unknown}

$(role_data "$role")"
  finding="$(complete "$prompt")" || true
  if [ -n "$finding" ] && printf '%s' "$finding" | jq -e '.role' >/dev/null 2>&1; then
    echo "advisor: $role ok"
    jq --argjson f "$finding" '. + [$f]' "$FINDINGS" > "$FINDINGS.tmp" && mv "$FINDINGS.tmp" "$FINDINGS"
    if [ "$DRY" = "1" ]; then
      echo "----- FINDING $role -----"; printf '%s\n' "$finding" | jq .
    else
      post "/api/advisor/finding" "$(jq -n --arg d "$DATE" --arg r "$role" --argjson f "$finding" '{date:$d, role:$r, finding:$f}')"
    fi
  else
    echo "advisor: $role gap (no valid finding)"; GAPS+=("$role")
  fi
done

FINDINGS_JSON="$(cat "$FINDINGS")"

# ---------------------------------------------------------------------------
# 3. Debate
# ---------------------------------------------------------------------------
DEBATE='{"turns":[]}'
debate_prompt="$(cat "$PROMPTS/debate.md")

<<<DATA findings>>>
$FINDINGS_JSON
<<<END>>>"
debate_out="$(complete "$debate_prompt")" || true
if [ -n "$debate_out" ] && printf '%s' "$debate_out" | jq -e '.turns' >/dev/null 2>&1; then
  DEBATE="$debate_out"
  echo "advisor: debate ok"
  if [ "$DRY" = "1" ]; then
    echo "----- DEBATE -----"; printf '%s\n' "$DEBATE" | jq .
  else
    post "/api/advisor/debate" "$(jq -n --arg d "$DATE" --argjson db "$DEBATE" '{date:$d, debate:$db}')"
  fi
else
  echo "advisor: debate gap"; GAPS+=("debate")
fi

# ---------------------------------------------------------------------------
# 4. Portfolio manager -> report
# ---------------------------------------------------------------------------
USED=()
UNAVAIL=()
for f in snapshot yields fees protocols cg-global cg-btc fng cg-markets x-search; do
  if [ -f "$D/$f.json" ]; then USED+=("$f"); else UNAVAIL+=("$f"); fi
done
USED_JSON="$(printf '%s\n' "${USED[@]}" | jq -R . | jq -cs .)"
UNAVAIL_JSON="$(printf '%s\n' "${UNAVAIL[@]:-}" | jq -R 'select(length>0)' | jq -cs .)"
GAPS_JSON="$(printf '%s\n' "${GAPS[@]:-}" | jq -R 'select(length>0)' | jq -cs .)"

# Compact view for the PM: drop bulky signals/concerns text, keep the decision-relevant fields.
# This keeps the PM prompt + output small enough to avoid Virtuals gateway timeouts (504).
PM_FINDINGS="$(printf '%s' "$FINDINGS_JSON" | jq -c '[.[] | {role, thesis, suggestedActions, error}]')"
PM_DEBATE="$(printf '%s' "$DEBATE" | jq -c '{turns: [.turns[]? | {side, points}]}')"

pm_prompt="$(cat "$PROMPTS/portfolio_manager.md")
Use generatedAt = \"$NOW_ISO\".

<<<DATA findings>>>
$PM_FINDINGS
<<<END>>>
<<<DATA debate>>>
$PM_DEBATE
<<<END>>>"

REPORT="$(complete "$pm_prompt")" || true
if [ -z "$REPORT" ] || ! printf '%s' "$REPORT" | jq -e '.summary' >/dev/null 2>&1; then
  echo "advisor: PM gap — synthesizing minimal report"
  REPORT=$(jq -n --arg ts "$NOW_ISO" '{
    generatedAt: $ts, summary: "Report generation incomplete; see findings.",
    recommendations: [], findings: [], debate: {turns: []},
    modelInfo: {analysts: "claude-opus-4-8 (Virtuals)", pm: "claude-opus-4-8 (Virtuals)"},
    dataSources: {used: [], unavailable: []}, gaps: [],
    disclaimer: "Not financial advice. For informational purposes only."
  }')
fi

# Merge accumulated findings/debate/gaps/dataSources so the POSTed report is always complete.
# Model-provided non-empty values win; otherwise fall back to our accumulated data.
REPORT="$(jq -n \
  --argjson rpt "$REPORT" \
  --argjson findings "$FINDINGS_JSON" \
  --argjson debate "$DEBATE" \
  --argjson used "$USED_JSON" \
  --argjson unavail "${UNAVAIL_JSON:-[]}" \
  --argjson gaps "${GAPS_JSON:-[]}" \
  '$rpt
   | .findings = (if (.findings // [] | length) > 0 then .findings else $findings end)
   | .debate = (if (.debate.turns // [] | length) > 0 then .debate else $debate end)
   | .dataSources = (.dataSources // {})
   | .dataSources.used = (if (.dataSources.used // [] | length) > 0 then .dataSources.used else $used end)
   | .dataSources.unavailable = (if (.dataSources.unavailable // [] | length) > 0 then .dataSources.unavailable else $unavail end)
   | .gaps = (if (.gaps // [] | length) > 0 then .gaps else $gaps end)
   | .modelInfo = {analysts: "claude-opus-4-8 (Virtuals)", pm: "claude-opus-4-8 (Virtuals)"}
   | .disclaimer = (.disclaimer // "Not financial advice. For informational purposes only.")')"

echo "advisor: report assembled"

if [ "$DRY" = "1" ]; then
  echo "----- REPORT -----"; printf '%s\n' "$REPORT" | jq .
  echo "advisor: DRY_RUN — no POST/Telegram fired (model=$VIRTUALS_MODEL)"
  exit 0
fi

post "/api/advisor/report" "$(jq -n --arg d "$DATE" --argjson r "$REPORT" '{date:$d, report:$r}')"
echo "advisor: report posted"

# Telegram summary: .summary + top 2 recommendations + disclaimer.
if [ -n "${TELEGRAM_BOT_TOKEN:-}" ] && [ -n "${TELEGRAM_CHAT_ID:-}" ]; then
  TG="$(printf '%s' "$REPORT" | jq -r --arg d "$DATE" '
    "📊 Advisor (" + $d + "): " + (.summary // "(no summary)") + "\n" +
    ([.recommendations[0:2][] | "• [" + (.urgency // "?") + "] " + (.title // .action // "")] | join("\n")) +
    "\nNot financial advice."')"
  curl -fsS --max-time 20 "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
    --data-urlencode "chat_id=${TELEGRAM_CHAT_ID}" \
    --data-urlencode "text=${TG}" \
    >/dev/null 2>&1 || echo "::warning::advisor: telegram send failed"
  echo "advisor: telegram sent"
fi

echo "advisor: done ($DATE)"
