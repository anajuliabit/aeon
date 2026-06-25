#!/usr/bin/env bash
# scripts/advisor/run.sh — single-shot advisory orchestrator.
#
# Pipeline (inference via scripts/llm-claude.sh, claude-fable-5 on the Claude
# subscription when CLAUDE_CODE_OAUTH_TOKEN is set; otherwise scripts/llm.sh on
# Virtuals, claude-opus-4-8):
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

export VIRTUALS_MODEL=claude-opus-4-8   # fallback backend; NEVER deepseek — hallucination-safe on Virtuals.

# Pinned production URL (canonical Railway domain — reaches the app; auth-guarded).
BASE="https://investiments-production.up.railway.app"
DATE=$(date -u +%Y-%m-%d)

# Build the Basic-auth token at runtime from the dashboard creds (avoids
# pre-encoding mistakes). DASHBOARD_USER defaults to "admin" (investiments default).
DASHBOARD_USER="${DASHBOARD_USER:-admin}"
AUTH=$(printf '%s:%s' "$DASHBOARD_USER" "${DASHBOARD_PASSWORD:-}" | base64 | tr -d '\n')
NOW_ISO=$(date -u +%Y-%m-%dT%H:%M:%SZ)
DRY="${ADVISOR_DRY_RUN:-0}"

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
# Backend selection. ADVISOR_LLM picks explicitly (usepod|claude|virtuals);
# the default "auto" keeps the historical behavior: Claude subscription
# (claude-fable-5 via Claude Code CLI) when an OAuth/API token is present,
# Virtuals otherwise. llm-claude.sh / llm-usepod.sh fall back to llm.sh on
# failure, so MODEL_LABEL reflects the primary backend. Sets LLM + MODEL_LABEL.
select_backend() {
  case "${ADVISOR_LLM:-auto}" in
    usepod)
      LLM="$ROOT/scripts/llm-usepod.sh"
      MODEL_LABEL="${USEPOD_MODEL:-deepseek-v3.2} (usepod)" ;;
    claude)
      LLM="$ROOT/scripts/llm-claude.sh"
      MODEL_LABEL="${CLAUDE_MODEL:-claude-fable-5} (Claude subscription)" ;;
    virtuals)
      LLM="$ROOT/scripts/llm.sh"
      MODEL_LABEL="${VIRTUALS_MODEL:-claude-opus-4-8} (Virtuals)" ;;
    auto|*)
      if [ -n "${CLAUDE_CODE_OAUTH_TOKEN:-}" ] || [ -n "${ANTHROPIC_API_KEY:-}" ]; then
        LLM="$ROOT/scripts/llm-claude.sh"
        MODEL_LABEL="${CLAUDE_MODEL:-claude-fable-5} (Claude subscription)"
      else
        LLM="$ROOT/scripts/llm.sh"
        MODEL_LABEL="${VIRTUALS_MODEL:-claude-opus-4-8} (Virtuals)"
      fi ;;
  esac
}
select_backend
PROMPTS="$ROOT/advisor/prompts"

# Shared accounting note injected into every agent prompt so the gross-vs-net
# difference isn't mistaken for a data discrepancy (see investiments reconcile()).
ACCOUNTING_NOTE='PORTFOLIO ACCOUNTING (do NOT report as a discrepancy): snapshot.totalUsd is NET worth = analytics.grossAssetsUsd minus analytics.totalLiabilitiesUsd. analytics.assets and allocation are GROSS (positive holdings only; loans excluded), so they sum to MORE than totalUsd by exactly analytics.totalLiabilitiesUsd (your debt). This gap is expected and already reconciled — never flag it as unresolved.

VESTING / LOCKED BALANCES: positions with type "locked" and the analytics.vesting entries are NON-TRANSFERABLE until they unlock — they CANNOT be sold, trimmed, rebalanced, or deployed now. Any sell/trim/reallocate recommendation must apply ONLY to the liquid (non-locked) portion of a token, and must state the liquid amount it applies to. analytics.vesting carries the schedule where known (claimableQty/claimableUsd = unlocked and claimable right now; nextUnlockAt/nextUnlockQty = next tranche; endAt = fully vested). Use unlock dates for forward planning (e.g. "on the next unlock, consider...") instead of recommending sales of locked balances.'
D="$ROOT/.investiments-cache/advisor"
WORK="$D/work"
mkdir -p "$WORK"

# --- Regime gate (deterministic risk-on/off; issue #139) ---
if [ "${REGIME_DISABLE:-0}" = "1" ]; then
  REGIME_JSON='{"band":"UNKNOWN","score":null}'
else
  REGIME_JSON="$(D="$D" bash "$ROOT/scripts/advisor/regime.sh" 2>/dev/null || echo '{"band":"UNKNOWN","score":null}')"
fi
printf '%s' "$REGIME_JSON" > "$D/regime.json"
REGIME_BAND="$(printf '%s' "$REGIME_JSON" | jq -r '.band // "UNKNOWN"')"
REGIME_SCORE="$(printf '%s' "$REGIME_JSON" | jq -r '.score // "n/a"')"
echo "advisor: regime $REGIME_BAND ($REGIME_SCORE/100)"

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
# stdout is the JSON channel, so all diagnostics go to stderr. The LLM's own
# stderr (auth errors, gateway 504s, "empty completion", Virtuals fallback) is
# captured and surfaced on total failure instead of being discarded — otherwise
# a dead token looks identical to a model that just produced no JSON.
complete() {
  local prompt="$1"
  local raw json errf
  errf="$(mktemp)"
  raw="$(printf '%s' "$prompt" | "$LLM" 2>"$errf" || true)"
  json="$(printf '%s' "$raw" | extract_json)"
  if [ -n "$json" ] && printf '%s' "$json" | jq -e . >/dev/null 2>&1; then
    rm -f "$errf"; printf '%s' "$json"; return 0
  fi
  raw="$(printf '%s\n\nReturn ONLY valid JSON, no prose.' "$prompt" | "$LLM" 2>>"$errf" || true)"
  json="$(printf '%s' "$raw" | extract_json)"
  if [ -n "$json" ] && printf '%s' "$json" | jq -e . >/dev/null 2>&1; then
    rm -f "$errf"; printf '%s' "$json"; return 0
  fi
  if [ -s "$errf" ]; then
    echo "advisor: LLM call failed — $(tr '\n' ' ' < "$errf" | head -c 500)" >&2
  else
    echo "advisor: LLM call failed — no stderr; output had no parseable JSON (len=${#raw})" >&2
  fi
  rm -f "$errf"
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
  REPORT=$(jq -n --arg ts "$NOW_ISO" --arg mi "$MODEL_LABEL" '{
    generatedAt: $ts,
    summary: "Run aborted: portfolio snapshot unavailable.",
    recommendations: [],
    findings: [],
    debate: {turns: []},
    modelInfo: {analysts: $mi, pm: $mi},
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
      datablock funding hl-funding.json '.'
      datablock macro macro-upcoming.json '.'
      ;;
    yield_allocation)
      # Include per-position protocol/type so deployed stables (e.g. USDC in a
      # Morpho vault) are distinguishable from idle wallet balances.
      datablock snapshot snapshot.json '{totalUsd, positions: [.positions[]? | {protocol, type, chain, symbol, valueUsd}], analytics:{allocation:.analytics.allocation, assets:.analytics.assets, vesting:[.analytics.vesting[]? | del(.upcoming)], grossAssetsUsd:.analytics.grossAssetsUsd, totalLiabilitiesUsd:.analytics.totalLiabilitiesUsd}}'
      datablock yields yields.json '[.data[]? | select(.stablecoin == true) | {project,symbol,chain,tvlUsd,apyBase,apyReward,apy}] | sort_by(-(.tvlUsd // 0)) | .[0:40]'
      datablock fees fees.json '{total24h: .total24h, protocols: [.protocols[]? | {name, total24h, total7d}] | .[0:30]}'
      datablock liquidity gt-liquidity.json '.'
      ;;
    market_macro)
      datablock cg_global cg-global.json '{total_market_cap_usd: .data.total_market_cap.usd, market_cap_pct: .data.market_cap_percentage, market_cap_change_24h: .data.market_cap_change_percentage_24h_usd}'
      datablock cg_btc cg-btc.json '{daily_closes_usd: ([.prices[]? | .[1]] | [range(0; length; 24) as $i | .[$i]]), latest_usd: (.prices[-1][1]? // null)}'
      datablock fng fng.json '.'
      datablock x_search x-search.json '.'
      datablock funding hl-funding.json '.'
      datablock macro macro-upcoming.json '.'
      ;;
    fundamentals)
      # vesting + locked slice so micro-cap recommendations (e.g. MAMO/REPPO)
      # distinguish locked balances (with unlock dates) from liquid ones.
      datablock snapshot snapshot.json '{totalUsd, analytics:{assets:.analytics.assets, vesting:[.analytics.vesting[]? | del(.upcoming)], grossAssetsUsd:.analytics.grossAssetsUsd, totalLiabilitiesUsd:.analytics.totalLiabilitiesUsd}, locked: [.positions[]? | select(.type == "locked") | {protocol, symbol, valueUsd}]}'
      datablock protocols protocols.json '[.[]? | {name, symbol, tvl, change_1d, change_7d}] | sort_by(-(.tvl // 0)) | .[0:60]'
      datablock fees fees.json '{protocols: [.protocols[]? | {name, total24h, total7d}] | .[0:40]}'
      datablock cg_held cg-held.json '[.[]?] | group_by(.symbol) | map(max_by(.market_cap // 0) | {symbol, name, market_cap, fully_diluted_valuation, circulating_supply, total_supply, price_change_percentage_24h})'
      datablock cg_markets cg-markets.json '[.[]? | {symbol, name, market_cap, fully_diluted_valuation, circulating_supply, total_supply, price_change_percentage_24h}] | .[0:60]'
      datablock liquidity gt-liquidity.json '.'
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
$ACCOUNTING_NOTE
HELD SYMBOLS (from snapshot): ${HELD:-unknown}

$(datablock regime regime.json '.')
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
for f in snapshot yields fees protocols cg-global cg-btc fng cg-held cg-markets x-search; do
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
$ACCOUNTING_NOTE
Use generatedAt = \"$NOW_ISO\".

$(datablock regime regime.json '.')
<<<DATA findings>>>
$PM_FINDINGS
<<<END>>>
<<<DATA debate>>>
$PM_DEBATE
<<<END>>>
$(datablock memory advisor-memory.json '.')"

REPORT="$(complete "$pm_prompt")" || true
if [ -z "$REPORT" ] || ! printf '%s' "$REPORT" | jq -e '.summary' >/dev/null 2>&1; then
  echo "advisor: PM gap — synthesizing minimal report"
  REPORT=$(jq -n --arg ts "$NOW_ISO" --arg mi "$MODEL_LABEL" '{
    generatedAt: $ts, summary: "Report generation incomplete; see findings.",
    recommendations: [], findings: [], debate: {turns: []},
    modelInfo: {analysts: $mi, pm: $mi},
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
  --argjson regime "$REGIME_JSON" \
  --arg mi "$MODEL_LABEL" \
  '$rpt
   | .regime = $regime
   | .findings = (if (.findings // [] | length) > 0 then .findings else $findings end)
   | .debate = (if (.debate.turns // [] | length) > 0 then .debate else $debate end)
   | .dataSources = (.dataSources // {})
   | .dataSources.used = (if (.dataSources.used // [] | length) > 0 then .dataSources.used else $used end)
   | .dataSources.unavailable = (if (.dataSources.unavailable // [] | length) > 0 then .dataSources.unavailable else $unavail end)
   | .gaps = (if (.gaps // [] | length) > 0 then .gaps else $gaps end)
   | .modelInfo = {analysts: $mi, pm: $mi}
   | .disclaimer = (.disclaimer // "Not financial advice. For informational purposes only.")')"

echo "advisor: report assembled"

# ---------------------------------------------------------------------------
# 5a. Short-term trades — fundamentals + news + momentum, LONG or SHORT, sized
#     to the ≤1% moonshot sleeve. Three stages (all OUTSIDE the LLM's tool-less
#     completion): (1) deterministic jq shortlist of liquid, non-held, non-stable
#     movers from cg-markets; (2) per-candidate Grok x_search (news/X/catalysts);
#     (3) one LLM decision over momentum + fundamentals + news. Defensive
#     side-aware re-filter; merged onto the report, staged, surfaced on Telegram.
# ---------------------------------------------------------------------------
HELD_LC="$(held_symbols)"
TRADES='{"trades":[]}'
SHORTLIST='[]'
if [ -f "$D/cg-markets.json" ]; then
  SHORTLIST="$(jq -c --arg held "${HELD_LC:-}" '
    ($held|ascii_downcase|split(" ")) as $h
    | [ .[]?
        | {symbol:((.symbol//"")|ascii_upcase), id, price:.current_price, mcap:.market_cap,
           vol24h:.total_volume, c24:(.price_change_percentage_24h // 0),
           c7:(.price_change_percentage_7d_in_currency // 0)}
        | select(.id != null and (.price // 0) > 0 and (.mcap // 0) > 0 and (.vol24h // 0) > 0)
        | select((.vol24h / .mcap) >= 0.05)
        | ((.symbol|ascii_downcase)) as $s
        | select(($h | index($s)) | not)
        | select(($s | test("^(usdc|usdt|usds|dai|usde|usdtb|frax|tusd|fdusd|pyusd|gusd)$")) | not)
      ]
    | sort_by( - (if (.c7) < 0 then -(.c7) else (.c7) end) )
    | .[0:8]' "$D/cg-markets.json" 2>/dev/null || echo '[]')"
fi
SL_N="$(printf '%s' "$SHORTLIST" | jq 'length' 2>/dev/null || echo 0)"
echo "advisor: short-term shortlist — $SL_N candidate(s)"

# Per-candidate Grok x_search (news / X / catalysts, last 7 days). Best-effort:
# a failed lookup just yields an empty news note for that symbol.
NEWS='{}'
if [ "$SL_N" -gt 0 ] && [ -n "${XAI_API_KEY:-}" ]; then
  XTO=$(date -u +%Y-%m-%d)
  XFROM=$(date -u -d "7 days ago" +%Y-%m-%d 2>/dev/null || date -u -v-7d +%Y-%m-%d)
  while read -r sym id; do
    [ -z "$sym" ] && continue
    XBODY=$(jq -n --arg m "grok-4-1-fast" \
      --arg p "Recent news, catalysts, funding, listings, hacks, token unlocks, and X sentiment for the crypto project $sym ($id) in the last 7 days. State clearly anything BULLISH or BEARISH for a 1-2 week trade. Factual, cite handles/sources, no hype." \
      --argjson tools "[{\"type\":\"x_search\",\"from_date\":\"$XFROM\",\"to_date\":\"$XTO\"}]" \
      '{model:$m, input:[{role:"user",content:$p}], tools:$tools}')
    RESP=$(curl -fsS --max-time 120 -X POST "https://api.x.ai/v1/responses" \
      -H "Content-Type: application/json" -H "Authorization: Bearer $XAI_API_KEY" \
      -d "$XBODY" 2>/dev/null || echo '')
    TXT=$(printf '%s' "$RESP" | jq -r '[.output[]?.content[]?.text] | join(" ")' 2>/dev/null)
    [ -z "$TXT" ] && TXT=$(printf '%s' "$RESP" | jq -r '.output_text // ""' 2>/dev/null)
    if [ -n "$TXT" ]; then
      NEWS=$(printf '%s' "$NEWS" | jq -c --arg s "$sym" --arg t "$TXT" '.[$s] = ($t[0:1200])')
      echo "advisor: researched $sym (x_search ok)"
    else
      echo "advisor: researched $sym (no news)"
    fi
  done < <(printf '%s' "$SHORTLIST" | jq -r '.[] | "\(.symbol) \(.id)"')
fi

if [ "$SL_N" -gt 0 ]; then
  st_prompt="$(cat "$PROMPTS/short_term_trades.md")
Use horizon 7-14 days.

<<<DATA SHORTLIST (screened liquid movers; momentum + price)>>>
$SHORTLIST
<<<END>>>
<<<DATA NEWS (Grok x_search per candidate; untrusted)>>>
$NEWS
<<<END>>>
$(datablock FUNDAMENTALS_protocols protocols.json '[.[]? | {name, symbol, tvl, change_1d, change_7d}] | sort_by(-(.tvl // 0)) | .[0:60]')
$(datablock FUNDAMENTALS_fees fees.json '{protocols: [.protocols[]? | {name, total24h, total7d}] | .[0:40]}')
$(datablock fng fng.json '.')"
  TRADES="$(complete "$st_prompt")" || true
  if [ -z "$TRADES" ] || ! printf '%s' "$TRADES" | jq -e '.trades' >/dev/null 2>&1; then
    TRADES='{"trades":[]}'
  fi
fi

# Defensive side-aware re-filter (held / coingeckoId / orientation) over the
# prompt rules so a drifting model can't push a junk or mis-oriented trade.
# LONG needs target>entry & invalidate<entry; SHORT needs target<entry & invalidate>entry.
TRADES="$(printf '%s' "$TRADES" | jq -c --arg held "${HELD_LC:-}" '
  ($held|ascii_downcase|split(" ")) as $h
  | {trades: [.trades[]?
      | (.side // "long") as $side
      | (.symbol // "" | ascii_downcase) as $sym
      | select(.symbol != null and .coingeckoId != null and (.entry // 0) > 0
               and (($h|index($sym)) | not)
               and (if $side == "short"
                    then (.target // 0) > 0 and (.target < .entry) and ((.invalidate // 0) == 0 or (.invalidate > .entry))
                    else (.target // 0) > (.entry) and ((.invalidate // 0) == 0 or (.invalidate < .entry)) end))
    ] | .[0:5]}')"

# Position sizing: split a short-term-risk budget (default 5% of net worth) across
# the selected trades, conviction-weighted (HIGH = 2× MEDIUM). Deterministic so the
# dollar amounts are reproducible from the report, not LLM-guessed. Override the
# budget pct with ST_RISK_PCT.
ST_RISK_PCT="${ST_RISK_PCT:-5}"
ST_TOTAL="$(jq -r '.totalUsd // 0' "$D/snapshot.json" 2>/dev/null || echo 0)"
ST_BUDGET="$(awk "BEGIN{printf \"%.2f\", ($ST_TOTAL * $ST_RISK_PCT) / 100}")"
TRADES="$(printf '%s' "$TRADES" | jq -c --argjson budget "$ST_BUDGET" --argjson total "$ST_TOTAL" '
  .trades as $t
  | ([$t[] | (if ((.conviction // "") | ascii_upcase | startswith("HIGH")) then 2 else 1 end)] | add // 0) as $wsum
  | {trades: [ $t[]
      | (if ((.conviction // "") | ascii_upcase | startswith("HIGH")) then 2 else 1 end) as $w
      | .sizeUsd = (if $wsum > 0 then (($budget * $w / $wsum) | floor) else 0 end)
      | .sizePctNet = (if $total > 0 then (((.sizeUsd / $total) * 1000) | round) / 10 else 0 end) ]}')"
if [ "${REGIME_BAND:-UNKNOWN}" = "BEAR" ]; then
  TRADES="$(printf '%s' "$TRADES" | jq -c '
    {trades: [ .trades[]
      | if (.side // "long") == "long"
        then .sizeUsd = ((.sizeUsd // 0) / 2 | floor)
             | .sizePctNet = (((.sizePctNet // 0) * 10 / 2 | round) / 10)
             | .regimeHalved = true
        else . end ]}')"
  echo "advisor: regime BEAR — halved long short-term notionals"
fi
REPORT="$(jq -n --argjson rpt "$REPORT" --argjson st "$TRADES" '$rpt | .shortTermTrades = ($st.trades // [])')"
echo "advisor: short-term trades — $(printf '%s' "$TRADES" | jq '.trades | length') selected; sized from ${ST_RISK_PCT}% (\$$(printf '%.0f' "$ST_BUDGET")) of net \$$(printf '%.0f' "$ST_TOTAL")"

# ---------------------------------------------------------------------------
# 5. Stage every actionable rec (increase/decrease/hedge with a symbol) as a
#    pick, so trims and adds both land in the track record alongside token-pick
#    and the weekly run. side: increase => long; decrease/hedge => short (a trim
#    is graded as "was reducing here timely" — hit if price then fell). The
#    entry price is the rec's .level when given, else the symbol's spot from the
#    snapshot. STABLECOINS are skipped: a USDC yield/deploy move has no price
#    thesis and would pollute win-rate. A mis-oriented invalidation is dropped
#    (set null) so the pick still lands. Daily picks use an "-advisor-daily-" id
#    so they never collide with the weekly run's "-advisor-" ids on the same date.
# ---------------------------------------------------------------------------
REFS="$ROOT/advisor/token-refs.json"
SNAP="$D/snapshot.json"
STAGED=0
CANDIDATES=0
# Process substitution (not a pipe) so STAGED/CANDIDATES survive into this shell;
# a `jq | while` loop would mutate them only in the pipe's subshell.
while read -r rec; do
  CANDIDATES=$((CANDIDATES + 1))
  SYM=$(printf '%s' "$rec" | jq -r '.symbol')
  DIR=$(printf '%s' "$rec" | jq -r '.direction')
  SYM_KEY=$(printf '%s' "$SYM" | tr '[:upper:]' '[:lower:]' | tr -cd 'a-z0-9')
  CG_ID=$(jq -r --arg s "$SYM_KEY" '.[$s] // empty' "$REFS" 2>/dev/null)
  if [ -z "$CG_ID" ]; then
    echo "advisor: no coingecko id for $SYM — rec not tracked as pick"; continue
  fi
  # Stablecoin? (isStable in the snapshot, or a known stable ticker.) Skip — no price bet.
  ISSTABLE=$(jq -r --arg s "$SYM_KEY" '[.analytics.assets[]?
    | select(((.symbol // "") | ascii_downcase | gsub("[^a-z0-9]";"")) == $s) | .isStable] | (first // false)' \
    "$SNAP" 2>/dev/null || echo false)
  case "$SYM_KEY" in usdc|usdt|usds|dai|usde|usdtb|frax|tusd) ISSTABLE=true ;; esac
  if [ "$ISSTABLE" = "true" ]; then
    echo "advisor: $SYM is a stablecoin move (no price thesis) — not tracked as pick"; continue
  fi
  # Entry: explicit .level, else spot price for the symbol from the snapshot positions.
  LEVEL=$(printf '%s' "$rec" | jq -r '.level // empty')
  ENTRY=""
  if [ -n "$LEVEL" ] && awk "BEGIN{exit !($LEVEL>0)}" 2>/dev/null; then
    ENTRY="$LEVEL"
  else
    ENTRY=$(jq -r --arg s "$SYM_KEY" '[.positions[]?
      | select(((.symbol // "") | ascii_downcase | gsub("[^a-z0-9]";"")) == $s)
      | .price] | map(select(. != null and . > 0)) | (first // empty)' "$SNAP" 2>/dev/null)
  fi
  if [ -z "$ENTRY" ]; then
    echo "advisor: $SYM has no level or spot price — not tracked as pick"; continue
  fi
  SIDE=long; [ "$DIR" = "increase" ] || SIDE=short
  PICK=$(printf '%s' "$rec" | jq -c \
    --arg d "$DATE" --arg cg "$CG_ID" --arg side "$SIDE" --argjson entry "$ENTRY" '
    (.invalidateLevel) as $inv
    # Drop a mis-oriented invalidation (server rejects long inv>=entry / short inv<=entry).
    | (if $inv == null then null
       elif $side == "long"  and $inv < $entry then $inv
       elif $side == "short" and $inv > $entry then $inv
       else null end) as $invOK
    | {
        id: ($d + "-advisor-daily-" + (.symbol | ascii_downcase)),
        source: "advisor",
        symbol: .symbol,
        coingeckoId: $cg,
        side: $side,
        entryPriceUsd: $entry,
        targetPriceUsd: null,
        invalidationPriceUsd: $invOK,
        horizonDays: (.horizonDays // 30),
        conviction: "UNSTATED",
        thesis: ((.title // "advisor call") + " — " + (.action // "")
                 + (if .rationale then " | " + .rationale else "" end))
      }')
  # Daily picks carry no notionalUsd (server assigns a fixed $1k). Annotate with
  # regimeHalved as a forward hook for future server-side sizing — NOTE: nothing
  # reads this field yet, so it has no effect on the $1k notional today. The real
  # variable BEAR exposure rides on short-term trades, which ARE halved above.
  if [ "${REGIME_BAND:-UNKNOWN}" = "BEAR" ] && [ "$SIDE" = "long" ]; then
    PICK="$(printf '%s' "$PICK" | jq -c '.regimeHalved = true')"
    echo "advisor: regime BEAR — flagged long daily pick $SYM (notional server-assigned; flag is a no-op today)"
  fi
  if [ "$DRY" = "1" ]; then
    echo "----- PICK $SYM ($SIDE) -----"; printf '%s\n' "$PICK" | jq .
    STAGED=$((STAGED + 1))
  else
    # Capture the HTTP status so the CI log proves whether the pick landed
    # (the silent `post` helper hid POST failures — and successes).
    code=$(curl -sS --max-time 30 -o /dev/null -w "%{http_code}" -X POST "$BASE/api/picks" \
      -H "Authorization: Basic ${AUTH}" -H "Content-Type: application/json" \
      -d "$PICK" 2>/dev/null || echo "000")
    if [ "$code" = "200" ] || [ "$code" = "201" ]; then
      echo "advisor: pick staged $SYM $SIDE (HTTP $code)"; STAGED=$((STAGED + 1))
    else
      echo "::warning::advisor: pick POST $SYM failed (HTTP $code)"
    fi
  fi
done < <(printf '%s' "$REPORT" | jq -c '.recommendations[]?
  | select(.symbol != null)
  | select(.direction == "increase" or .direction == "decrease" or .direction == "hedge")')
echo "advisor: staged $STAGED/$CANDIDATES actionable pick(s)"

# Read-back verification (skipped in DRY): confirm the store actually persisted
# today's advisor-daily picks — distinguishes "POST 200 but not stored" from a
# genuine persistence problem (e.g. ephemeral Railway FS).
if [ "$DRY" != "1" ] && [ "$STAGED" -gt 0 ]; then
  BACK=$(curl -sS --max-time 30 -H "Authorization: Basic ${AUTH}" "$BASE/api/picks" 2>/dev/null \
    | jq --arg d "$DATE" '[.[]? | select(.id | startswith($d + "-advisor-daily-"))] | length' 2>/dev/null || echo "?")
  echo "advisor: read-back found $BACK today's advisor-daily pick(s) in store"
fi

# Stage short-term trades as picks (source advisor, long OR short, "-advisor-sttrade-" id).
STB_STAGED=0
while read -r b; do
  [ -z "$b" ] && continue
  SYM=$(printf '%s' "$b" | jq -r '.symbol')
  TSIDE=$(printf '%s' "$b" | jq -r '.side // "long"')
  PICK=$(printf '%s' "$b" | jq -c --arg d "$DATE" '
    (.side // "long") as $side
    | {
        id: ($d + "-advisor-sttrade-" + (.symbol | ascii_downcase)),
        source: "advisor",
        symbol: .symbol,
        coingeckoId: .coingeckoId,
        side: $side,
        entryPriceUsd: .entry,
        targetPriceUsd: .target,
        invalidationPriceUsd: (if (.invalidate // 0) <= 0 then null
                               elif $side == "short" and .invalidate > .entry then .invalidate
                               elif $side != "short" and .invalidate < .entry then .invalidate
                               else null end),
        horizonDays: (.horizonDays // 14),
        conviction: (.conviction // "UNSTATED"),
        notionalUsd: (if (.sizeUsd // 0) > 0 then .sizeUsd else 1000 end),
        thesis: (("SHORT-TERM " + ($side | ascii_upcase) + " — ") + (.thesis // ""))
      }')
  if [ "$DRY" = "1" ]; then
    echo "----- STTRADE $SYM ($TSIDE) -----"; printf '%s\n' "$PICK" | jq .
    STB_STAGED=$((STB_STAGED + 1))
  else
    code=$(curl -sS --max-time 30 -o /dev/null -w "%{http_code}" -X POST "$BASE/api/picks" \
      -H "Authorization: Basic ${AUTH}" -H "Content-Type: application/json" \
      -d "$PICK" 2>/dev/null || echo "000")
    if [ "$code" = "200" ] || [ "$code" = "201" ]; then
      echo "advisor: short-term trade staged $SYM $TSIDE (HTTP $code)"; STB_STAGED=$((STB_STAGED + 1))
    else
      echo "::warning::advisor: short-term trade POST $SYM failed (HTTP $code)"
    fi
  fi
done < <(printf '%s' "$REPORT" | jq -c '.shortTermTrades[]?')
echo "advisor: staged $STB_STAGED short-term trade(s)"

# Telegram: .summary + the actionable trades (directional recs), so the operator
# sees the trims/adds/hedges — not just whatever defensive "hold" the PM ranked
# first. Falls back to an explicit "no trades" line on a purely defensive day.
TG="$(printf '%s' "$REPORT" | jq -r --arg d "$DATE" --arg band "$REGIME_BAND" --arg score "$REGIME_SCORE" '
  ([.recommendations[]? | select(.direction == "increase" or .direction == "decrease" or .direction == "hedge")]) as $trades
  | (.shortTermTrades // []) as $buys
  | "REGIME: " + $band + (if $score == "n/a" then "" else " " + $score + "/100" end) + "\n"
    + "📊 Advisor (" + $d + "): " + (.summary // "(no summary)") + "\n"
    + (if ($trades | length) == 0
       then "No new trades — defensive stance (see dashboard)."
       else "Potential trades:\n" + ([$trades[0:5][]
         | "• [" + (.urgency // "?") + "] " + ((.direction // "?") | ascii_upcase) + " "
           + (.symbol // "portfolio")
           + (if .level != null then " @ $" + (.level | tostring) else "" end)
           + (if .invalidateLevel != null then " (inv $" + (.invalidateLevel | tostring) + ")" else "" end)
           + " — " + (.title // .action // "")] | join("\n"))
       end)
    + "\n\n" + (if ($buys | length) == 0
       then "🎯 Short-term trades: none qualify today."
       else "🎯 Short-term trades (sized from a 5% short-term sleeve):\n" + ([$buys[]
         | "• " + (.conviction // "?") + " " + ((.side // "long") | ascii_upcase) + " " + (.symbol // "?")
           + (if (.sizeUsd // 0) > 0 then " ~$" + (.sizeUsd | tostring) + " (" + ((.sizePctNet // 0) | tostring) + "% net)" else "" end)
           + " · $" + ((.entry // 0) | tostring) + " → $" + ((.target // 0) | tostring)
           + (if .invalidate then " (inv $" + (.invalidate | tostring) + ")" else "" end)
           + " / " + ((.horizonDays // 14) | tostring) + "d"
           + (if (.thesis // "") != "" then "\n   ↳ " + (.thesis | .[0:240]) else "" end)] | join("\n"))
       end)
    + "\nNot financial advice."')"

if [ "$DRY" = "1" ]; then
  echo "----- REPORT -----"; printf '%s\n' "$REPORT" | jq .
  echo "----- TELEGRAM -----"; printf '%s\n' "$TG"
  echo "advisor: DRY_RUN — no POST/Telegram fired (model=$MODEL_LABEL)"
  exit 0
fi

post "/api/advisor/report" "$(jq -n --arg d "$DATE" --argjson r "$REPORT" '{date:$d, report:$r}')"
echo "advisor: report posted"

if [ -n "${TELEGRAM_BOT_TOKEN:-}" ] && [ -n "${TELEGRAM_CHAT_ID:-}" ]; then
  curl -fsS --max-time 20 "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
    --data-urlencode "chat_id=${TELEGRAM_CHAT_ID}" \
    --data-urlencode "text=${TG}" \
    >/dev/null 2>&1 || echo "::warning::advisor: telegram send failed"
  echo "advisor: telegram sent"
fi

echo "advisor: done ($DATE)"
