#!/usr/bin/env bash
# scripts/advisor/selftest.sh — offline fixtures for the advisor shell logic.
# No network, no creds: exercises the jq/python decision rules of grade-recs.sh
# and run-weekly.sh against synthetic data. Exits non-zero on any failure.
# Run locally or in CI before shipping changes to the advisor scripts.
set -uo pipefail
FAIL=0
check() { # desc, got, want
  if [ "$2" = "$3" ]; then echo "ok   $1"; else echo "FAIL $1: got [$2] want [$3]"; FAIL=1; fi
}

# --- grade-recs.sh direction rules ---
rule() { # direction, movePct -> result
  case "$1" in
    increase) python3 -c "m=$2; print('hit' if m>=5 else 'miss' if m<=-5 else 'neutral')" ;;
    decrease|hedge) python3 -c "m=$2; print('hit' if m<=-5 else 'miss' if m>=5 else 'neutral')" ;;
    hold) python3 -c "m=$2; print('miss' if m<=-25 else 'neutral')" ;;
  esac
}
check "increase +8 → hit"      "$(rule increase 8)"    "hit"
check "increase -6 → miss"     "$(rule increase -6)"   "miss"
check "increase +2 → neutral"  "$(rule increase 2)"    "neutral"
check "decrease -7 → hit"      "$(rule decrease -7)"   "hit"
check "hedge +6 → miss"        "$(rule hedge 6)"       "miss"
check "hold -30 → miss"        "$(rule hold -30)"      "miss"
check "hold -10 → neutral"     "$(rule hold -10)"      "neutral"

# --- grade-recs.sh sanitizers ---
SYM=$(printf '%s' '{"symbol":"<BTC/>"}' | jq -r '.symbol // empty' | tr '[:upper:]' '[:lower:]' | tr -cd 'a-z0-9')
check "symbol sanitizer strips markup" "$SYM" "btc"
DIR_IN="rm -rf /"; case "$DIR_IN" in increase|decrease|hold|hedge) DIR_OUT="$DIR_IN" ;; *) DIR_OUT="hold" ;; esac
check "direction allowlist defaults to hold" "$DIR_OUT" "hold"
check "detail printf handles negative floats" "$(printf '%s %+.1f%% over %sd vs "%s"' btc -3.456 30 decrease)" 'btc -3.5% over 30d vs "decrease"'

# --- run-weekly.sh validation gate ---
validate() {
  printf '%s' "$1" | jq -r '
    [ (if (.actions | length) > 3 then "more than 3 actions" else empty end),
      (.actions[]? | select(.entry == null or .exit == null or .invalidate == null)
        | "action \"\(.thesis[0:40])\" missing numeric entry/exit/invalidate"),
      (.actions[]? | select((.sleevePctAfter // 99) > 20)
        | "action \"\(.thesis[0:40])\" exceeds 20% sleeve cap"),
      (if (.paceVerdict.comment // "") == "" then "missing paceVerdict.comment" else empty end)
    ] | join("; ")' 2>/dev/null || echo "unparseable report"
}
GOOD='{"paceVerdict":{"comment":"ok"},"actions":[{"thesis":"t","entry":1,"exit":2,"invalidate":0.5,"sleevePctAfter":15}]}'
BAD='{"paceVerdict":{"comment":""},"actions":[{"thesis":"a","entry":null,"exit":1,"invalidate":1,"sleevePctAfter":25},{"thesis":"b","entry":1,"exit":1,"invalidate":1,"sleevePctAfter":5},{"thesis":"c","entry":1,"exit":1,"invalidate":1,"sleevePctAfter":5},{"thesis":"d","entry":1,"exit":1,"invalidate":1,"sleevePctAfter":5}]}'
check "validation passes a good report" "$(validate "$GOOD")" ""
V="$(validate "$BAD")"
case "$V" in *"more than 3 actions"*"missing numeric"*"20% sleeve cap"*"paceVerdict.comment"*) echo "ok   validation catches all four violations" ;; *) echo "FAIL validation: [$V]"; FAIL=1 ;; esac

# --- run-weekly.sh extract_json (non-greedy, survives trailing prose with braces) ---
EX() {
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
GOT=$(printf 'Here you go:\n{"a": {"b": 1}}\nNote: the cap (20%%} is a hard limit.' | EX)
check "extract_json stops at JSON boundary" "$GOT" '{"a": {"b": 1}}'
check "extract_json empty on garbage" "$(printf 'no json here }{' | EX)" ""

# --- macro calendar filter (next-14d window) ---
CAL='{"updated":"2026-06-09","coverage":{},"events":[{"date":"2026-06-10","type":"CPI"},{"date":"2026-09-16","type":"FOMC"}]}'
GOT=$(printf '%s' "$CAL" | jq -c --arg today "2026-06-09" --arg until "2026-06-23" '{updated, coverage, events: [.events[] | select(.date >= $today and .date <= $until)]} | .events | length')
check "macro filter keeps only in-window events" "$GOT" "1"

# --- notify-drawdown band logic ---
ddband() { local out=0 b; for b in 10 15 20 30; do if python3 -c "exit(0 if $1 >= $b else 1)"; then out=$b; fi; done; echo "$out"; }
check "dd 15.45 -> band 15" "$(ddband 15.45)" "15"
check "dd 9.9 -> band 0" "$(ddband 9.9)" "0"
check "dd 31 -> band 30" "$(ddband 31)" "30"

# --- run-weekly quarter-Kelly sizing jq ---
KSC='{"grades":[]}'
for i in $(seq 1 15); do KSC=$(printf '%s' "$KSC" | jq '.grades += [{"result":"hit"}]'); done
for i in $(seq 1 10); do KSC=$(printf '%s' "$KSC" | jq '.grades += [{"result":"miss"}]'); done
KOUT=$(printf '%s' "$KSC" | jq -c '([.grades[]? | select(.result == "hit")] | length) as $h | ([.grades[]? | select(.result == "miss")] | length) as $m | ($h + $m) as $n | if $n >= 20 then ($h / $n) as $p | {gradedSample: $n, quarterKellyPctOfNet: ((([(2 * $p - 1), 0] | max) / 4) * 100 | round)} else {gradedSample: $n} end')
check "kelly 60% hit rate -> 5% quarter-kelly" "$(printf '%s' "$KOUT" | jq -r '.quarterKellyPctOfNet')" "5"
KSMALL=$(printf '{"grades":[{"result":"hit"},{"result":"miss"}]}' | jq -c '([.grades[]? | select(.result == "hit")] | length) as $h | ([.grades[]? | select(.result == "miss")] | length) as $m | ($h + $m) as $n | if $n >= 20 then {kelly: true} else {gradedSample: $n} end')
check "kelly small sample gated" "$(printf '%s' "$KSMALL" | jq -r 'has("kelly") | tostring')" "false"

# --- notify-yield-delta jq selection ---
YFIX='{"data":[
 {"stablecoin":true,"symbol":"USDC","project":"morpho-blue","chain":"Base","tvlUsd":50000000,"apyBase":4.0},
 {"stablecoin":true,"symbol":"USDC","project":"maple","chain":"Ethereum","tvlUsd":80000000,"apyBase":6.2},
 {"stablecoin":true,"symbol":"USDT","project":"degenfarm","chain":"Base","tvlUsd":500000,"apyBase":40},
 {"stablecoin":false,"symbol":"WETH","project":"lido","chain":"Ethereum","tvlUsd":900000000,"apyBase":3.0}]}'
YOURS=$(printf '%s' "$YFIX" | jq -r '[.data[]? | select(.stablecoin == true and (.symbol // "" | ascii_downcase | test("usdc")) and (.project // "" | ascii_downcase | test("morpho")) and (.chain // "" | ascii_downcase == "base") and ((.tvlUsd // 0) >= 1000000))] | max_by(.apyBase // 0) | select(. != null) | .apyBase')
check "yield-delta venue proxy finds morpho/base/usdc" "$YOURS" "4.0"
YALLOW='["aave-v3","aave-v2","morpho","morpho-blue","morpho-v1","compound-v3","spark","sparklend","maple","fluid-lending","euler-v2"]'
YBEST=$(printf '%s' "$YFIX" | jq -r --argjson mintvl 20000000 --argjson allow "$YALLOW" '[.data[]? | select(.stablecoin == true and ((.tvlUsd // 0) >= $mintvl) and ((.apyBase // 0) > 0) and ((.project // "" | ascii_downcase) as $p | $allow | any(. == $p)))] | max_by(.apyBase) | select(. != null) | .apyBase')
check "yield-delta best excludes dust-TVL farm" "$YBEST" "6.2"
YFIX2=$(printf '%s' "$YFIX" | jq -c '.data += [{"stablecoin":true,"symbol":"USDT0","project":"altura","chain":"Hyperliquid L1","tvlUsd":34000000,"apyBase":17.5}]')
YBEST2=$(printf '%s' "$YFIX2" | jq -r --argjson mintvl 20000000 --argjson allow "$YALLOW" '[.data[]? | select(.stablecoin == true and ((.tvlUsd // 0) >= $mintvl) and ((.apyBase // 0) > 0) and ((.project // "" | ascii_downcase) as $p | $allow | any(. == $p)))] | max_by(.apyBase) | select(. != null) | .apyBase')
check "yield-delta excludes managed vaults (altura)" "$YBEST2" "6.2"

# --- notify-drawdown zero-peak resilience ---
ZH='[{"date":"2026-06-01","totalUsd":0},{"date":"2026-06-02","totalUsd":100},{"date":"2026-06-03","totalUsd":80}]'
ZDD=$(printf '%s' "$ZH" | jq '[.[] | select((.totalUsd // 0) > 0)] as $h | if ($h | length) < 2 then {today: null} else [range($h | length) as $i | {dd: ((([$h[range(0; $i + 1)].totalUsd] | max) as $peak | if $peak > 0 then ($peak - $h[$i].totalUsd) / $peak * 100 else 0 end))}] | {today: .[-1].dd} end' -c)
check "drawdown skips zero-total entries" "$(printf '%s' "$ZDD" | jq -r '.today')" "20"

# --- run.sh daily-pick staging: rec -> pick mapping + filter ---
# Every increase/decrease/hedge rec WITH a symbol is a candidate (hold dropped).
# side: increase->long, decrease/hedge->short. Entry = level||spot; stablecoins
# and entry-less recs are dropped downstream (bash, using the snapshot). Mirrors
# the jq/bash in run.sh step 5.
RECS='[
 {"symbol":"BTC","direction":"increase","level":67000,"invalidateLevel":61000,"horizonDays":30,"title":"Add BTC","action":"deploy","rationale":"reclaim"},
 {"symbol":"REPPO","direction":"decrease","level":0.42,"invalidateLevel":0.5,"horizonDays":60,"title":"Trim REPPO","action":"trim"},
 {"symbol":null,"direction":"hold","level":null,"invalidateLevel":null,"horizonDays":30,"title":"Hold","action":"wait"},
 {"symbol":"MAMO","direction":"increase","level":null,"invalidateLevel":null,"horizonDays":30,"title":"Add MAMO","action":"buy"},
 {"symbol":"USDC","direction":"increase","level":1,"invalidateLevel":null,"horizonDays":30,"title":"Deploy USDC","action":"vault"}]'
# Candidate filter (jq) — symbol present + actionable direction. USDC/level-less
# still pass here; stablecoin + entry checks run in bash (need the snapshot).
CAND=$(printf '%s' "$RECS" | jq -c '[.[] | select(.symbol != null)
  | select(.direction == "increase" or .direction == "decrease" or .direction == "hedge")]')
check "pick candidates include trims + drop holds" "$(printf '%s' "$CAND" | jq -r 'length')" "4"
# side mapping
sidemap() { [ "$1" = "increase" ] && echo long || echo short; }
check "side increase -> long"  "$(sidemap increase)" "long"
check "side decrease -> short" "$(sidemap decrease)" "short"
check "side hedge -> short"    "$(sidemap hedge)"    "short"
# stablecoin skip (snapshot isStable OR known ticker)
SNAPFIX='{"analytics":{"assets":[{"symbol":"USDC","isStable":true},{"symbol":"REPPO","isStable":false}]},"positions":[{"symbol":"REPPO","price":0.40},{"symbol":"MAMO","price":0.0085}]}'
isstable() { printf '%s' "$SNAPFIX" | jq -r --arg s "$1" '[.analytics.assets[]? | select((.symbol|ascii_downcase)==$s)|.isStable]|(first//false)'; }
check "stablecoin USDC skipped" "$(isstable usdc)" "true"
check "non-stable REPPO kept"   "$(isstable reppo)" "false"
# entry fallback to snapshot spot when level absent (MAMO has no level)
spot() { printf '%s' "$SNAPFIX" | jq -r --arg s "$1" '[.positions[]?|select((.symbol|ascii_downcase)==$s)|.price]|map(select(.!=null and .>0))|(first//empty)'; }
check "entry falls back to spot for level-less rec" "$(spot mamo)" "0.0085"
# invalidation orientation drop: short with inv<=entry must be nulled
INVOK=$(jq -n --argjson entry 0.42 --arg side short --argjson inv 0.30 '
  if $inv==null then null elif $side=="long" and $inv<$entry then $inv elif $side=="short" and $inv>$entry then $inv else null end')
check "mis-oriented short invalidation dropped" "$INVOK" "null"
PICKID=$(printf '%s' "$RECS" | jq -r '.[0] | "2026-06-14-advisor-daily-" + (.symbol | ascii_downcase)')
check "pick id namespaced -daily-" "$PICKID" "2026-06-14-advisor-daily-btc"

# --- run.sh Telegram trade filter: directional recs surface, holds don't ---
TGTRADES=$(printf '%s' "$RECS" | jq -r '[.[] | select(.direction == "increase" or .direction == "decrease" or .direction == "hedge")] | length')
check "telegram surfaces all directional recs (incl decrease)" "$TGTRADES" "4"
TGEMPTY=$(printf '%s' '[{"direction":"hold","symbol":null}]' | jq -r '[.[] | select(.direction == "increase" or .direction == "decrease" or .direction == "hedge")] | length')
check "telegram trade list empty on all-hold report" "$TGEMPTY" "0"

# --- run.sh short-term trades: side-aware re-filter + pick mapping ---
# LONG needs target>entry & invalidate<entry; SHORT needs target<entry &
# invalidate>entry. Non-held, coingeckoId required. Mirrors run.sh step 5a.
STTR_IN='{"trades":[
 {"symbol":"WIF","coingeckoId":"dogwifcoin","side":"long","entry":2.0,"target":2.6,"invalidate":1.7,"horizonDays":10,"conviction":"HIGH","thesis":"x"},
 {"symbol":"PEPE","coingeckoId":"pepe","side":"short","entry":0.001,"target":0.0008,"invalidate":0.0012,"horizonDays":10,"conviction":"MEDIUM","thesis":"overextended pump, unlock"},
 {"symbol":"REPPO","coingeckoId":"reppo","side":"long","entry":0.02,"target":0.03,"invalidate":0.015,"horizonDays":14,"conviction":"MEDIUM","thesis":"held — drop"},
 {"symbol":"BADL","coingeckoId":"badl","side":"long","entry":1.0,"target":0.9,"invalidate":0.8,"horizonDays":10,"conviction":"HIGH","thesis":"long target<entry — drop"},
 {"symbol":"BADS","coingeckoId":"bads","side":"short","entry":1.0,"target":1.2,"invalidate":0.9,"horizonDays":10,"conviction":"HIGH","thesis":"short target>entry — drop"},
 {"symbol":"NOID","coingeckoId":null,"side":"long","entry":1.0,"target":2.0,"invalidate":0.5,"horizonDays":10,"conviction":"HIGH","thesis":"no id — drop"}]}'
STHELD="reppo mamo well usdc"
STFILT=$(printf '%s' "$STTR_IN" | jq -c --arg held "$STHELD" '
  ($held|ascii_downcase|split(" ")) as $h
  | {trades:[.trades[]? | (.side // "long") as $side | (.symbol // "" | ascii_downcase) as $sym
      | select(.symbol!=null and .coingeckoId!=null and (.entry//0)>0 and (($h|index($sym))|not)
        and (if $side=="short"
             then (.target//0)>0 and (.target<.entry) and ((.invalidate//0)==0 or (.invalidate>.entry))
             else (.target//0)>(.entry) and ((.invalidate//0)==0 or (.invalidate<.entry)) end))]
    | .[0:5]}')
check "sttrade keeps valid long + short, drops rest" "$(printf '%s' "$STFILT" | jq -r '.trades|length')" "2"
check "sttrade keeps WIF long" "$(printf '%s' "$STFILT" | jq -r '[.trades[]|select(.symbol=="WIF")]|length')" "1"
check "sttrade keeps PEPE short" "$(printf '%s' "$STFILT" | jq -r '[.trades[]|select(.symbol=="PEPE" and .side=="short")]|length')" "1"
check "sttrade drops held/mis-oriented/no-id" "$(printf '%s' "$STFILT" | jq -r '[.trades[]|select(.symbol|test("REPPO|BADL|BADS|NOID"))]|length')" "0"
STSHORT=$(printf '%s' "$STFILT" | jq -c '[.trades[]|select(.side=="short")][0] | {side, entryPriceUsd:.entry,
  invalidationPriceUsd:(if (.invalidate//0)<=0 then null elif .side=="short" and .invalidate>.entry then .invalidate elif .side!="short" and .invalidate<.entry then .invalidate else null end)}')
check "sttrade short keeps inv above entry" "$(printf '%s' "$STSHORT" | jq -r '"\(.side) \(.invalidationPriceUsd)"')" "short 0.0012"
# Cap: many valid ideas are kept up to 5 (was 2). 7 valid longs -> 5.
STMANY=$(jq -nc '{trades:[range(0;7) as $i | {symbol:("T"+($i|tostring)), coingeckoId:("id"+($i|tostring)), side:"long", entry:1.0, target:1.5, invalidate:0.8}]}' \
  | jq -c '{trades:[.trades[]? | (.side//"long") as $side | select(.symbol!=null and .coingeckoId!=null and (.entry//0)>0
      and (if $side=="short" then (.target//0)>0 and (.target<.entry) and ((.invalidate//0)==0 or (.invalidate>.entry))
           else (.target//0)>(.entry) and ((.invalidate//0)==0 or (.invalidate<.entry)) end))] | .[0:5]}')
check "sttrade cap keeps up to 5 ideas" "$(printf '%s' "$STMANY" | jq -r '.trades|length')" "5"

# --- run.sh sizing: conviction-weighted split of a 5%-of-net budget ---
# net 390000 → budget 19500; weights HIGH=2, MEDIUM=1; 2 HIGH + 3 MED = 7.
# HIGH = floor(19500*2/7)=5571; MED = floor(19500*1/7)=2785; sum 19497 ≤ budget.
SZIN='[{"conviction":"HIGH"},{"conviction":"HIGH"},{"conviction":"MEDIUM"},{"conviction":"MEDIUM"},{"conviction":"MEDIUM"}]'
SZ=$(printf '%s' "$SZIN" | jq -c --argjson budget 19500 --argjson total 390000 '
  . as $t | ([$t[] | (if ((.conviction//"")|ascii_upcase|startswith("HIGH")) then 2 else 1 end)]|add//0) as $wsum
  | [ $t[] | (if ((.conviction//"")|ascii_upcase|startswith("HIGH")) then 2 else 1 end) as $w
      | (if $wsum>0 then (($budget*$w/$wsum)|floor) else 0 end) as $sz
      | {conviction, sizeUsd:$sz, sizePctNet:(if $total>0 then (($sz/$total*1000)|round)/10 else 0 end)} ]')
check "sizing HIGH = floor(2/7 of budget)" "$(printf '%s' "$SZ" | jq -r '.[0].sizeUsd')" "5571"
check "sizing MEDIUM = floor(1/7 of budget)" "$(printf '%s' "$SZ" | jq -r '.[2].sizeUsd')" "2785"
check "sizing total stays within budget" "$(printf '%s' "$SZ" | jq -r '[.[].sizeUsd]|add <= 19500')" "true"
check "sizing pct-of-net computed" "$(printf '%s' "$SZ" | jq -r '.[0].sizePctNet')" "1.4"

# --- run.sh complete(): LLM failure must surface, not be swallowed ---
# Regression: a dead token once produced a silent "PM gap" because complete()
# piped the LLM's stderr to /dev/null. Load the real complete() against a stub
# LLM that fails like an auth error and assert the reason reaches stderr.
COMPLETE_DIR="$(cd "$(dirname "$0")" && pwd)"
CT_TMP="$(mktemp -d)"
cat > "$CT_TMP/fakellm.sh" <<'EOF'
#!/usr/bin/env bash
cat >/dev/null
echo "llm.sh: API error: invalid x-api-key" >&2
exit 1
EOF
chmod +x "$CT_TMP/fakellm.sh"
sed -n '/^cat > "\$EXTRACTOR" <<.PY.$/,/^PY$/p' "$COMPLETE_DIR/run.sh" | sed '1d;$d' > "$CT_TMP/extract_json.py"
EXTRACTOR="$CT_TMP/extract_json.py"
extract_json() { python3 "$EXTRACTOR"; }
LLM="$CT_TMP/fakellm.sh"
eval "$(sed -n '/^complete() {/,/^}/p' "$COMPLETE_DIR/run.sh")"
CT_OUT="$(complete "ping" 2>"$CT_TMP/err")"; CT_RC=$?
check "complete() returns 1 on LLM failure" "$CT_RC" "1"
check "complete() emits no stdout on failure" "$CT_OUT" ""
check "complete() surfaces the LLM error to stderr" \
  "$(grep -c 'LLM call failed.*invalid x-api-key' "$CT_TMP/err")" "1"

# --- run.sh select_backend(): ADVISOR_LLM selector ---
SB_DIR="$(cd "$(dirname "$0")" && pwd)"
# Run the real select_backend() in a clean subshell with controlled env.
sb() { # ADVISOR_LLM, CLAUDE_CODE_OAUTH_TOKEN, VIRTUALS_MODEL, USEPOD_MODEL -> "LLM|LABEL"
  ADVISOR_LLM="$1" CLAUDE_CODE_OAUTH_TOKEN="$2" ANTHROPIC_API_KEY="" \
    VIRTUALS_MODEL="${3:-}" USEPOD_MODEL="${4:-}" CLAUDE_MODEL="" ROOT="/fake/root" \
    bash -c 'unset LLM MODEL_LABEL
      '"$(sed -n '/^select_backend() {/,/^}/p' "$SB_DIR/run.sh")"'
      select_backend; printf "%s|%s" "$LLM" "$MODEL_LABEL"' 2>/dev/null
}
check "select usepod -> llm-usepod.sh"      "$(sb usepod '' '' '' | cut -d'|' -f1)" "/fake/root/scripts/llm-usepod.sh"
check "select usepod default label"         "$(sb usepod '' '' '' | cut -d'|' -f2)" "deepseek-v3.2 (usepod)"
check "select usepod honors USEPOD_MODEL"   "$(sb usepod '' '' qwen-3.5 | cut -d'|' -f2)" "qwen-3.5 (usepod)"
check "select claude explicit"              "$(sb claude '' '' '' | cut -d'|' -f1)" "/fake/root/scripts/llm-claude.sh"
check "select virtuals explicit"            "$(sb virtuals 'tok' '' '' | cut -d'|' -f1)" "/fake/root/scripts/llm.sh"
check "auto + claude token -> claude"       "$(sb auto 'tok' '' '' | cut -d'|' -f1)" "/fake/root/scripts/llm-claude.sh"
check "auto + no token -> virtuals"         "$(sb auto '' 'kimi' '' | cut -d'|' -f1)" "/fake/root/scripts/llm.sh"
check "auto + no token label"               "$(sb auto '' 'kimi' '' | cut -d'|' -f2)" "kimi (Virtuals)"
check "unset ADVISOR_LLM behaves as auto"   "$(sb '' 'tok' '' '' | cut -d'|' -f1)" "/fake/root/scripts/llm-claude.sh"

# --- llm-usepod.sh: redaction + fallback (offline, stubbed) ---
UP_DIR="$(cd "$(dirname "$0")/.." && pwd)"   # repo scripts/ dir ($0=scripts/advisor/selftest.sh, so dirname/.. = scripts/)
UP_TMP="$(mktemp -d)"

# Redactor: load the real redact() from llm-usepod.sh and check it scrubs the token.
eval "$(sed -n '/^redact() {/,/^}/p' "$UP_DIR/llm-usepod.sh")"
RED_IN='curl failed for https://api.usepod.ai/proxy/SECRETTOKEN/v1/chat/completions now'
check "redact scrubs usepod token" \
  "$(printf '%s' "$RED_IN" | redact)" \
  'curl failed for https://api.usepod.ai/proxy/<redacted>/v1/chat/completions now'
check "redact leaves non-usepod text" \
  "$(printf '%s' 'no secrets here' | redact)" 'no secrets here'

# Fallback: USEPOD_TOKEN unset + a stub Virtuals llm.sh on a fake root -> usepod
# defers to Virtuals and returns the stub's output.
mkdir -p "$UP_TMP/scripts"
cp "$UP_DIR/llm-usepod.sh" "$UP_TMP/scripts/llm-usepod.sh"
cat > "$UP_TMP/scripts/llm.sh" <<'EOF'
#!/usr/bin/env bash
cat >/dev/null
echo '{"ok":"virtuals-stub"}'
EOF
chmod +x "$UP_TMP/scripts/llm.sh" "$UP_TMP/scripts/llm-usepod.sh"
FB_OUT="$(USEPOD_TOKEN='' VIRTUALS_API_KEY='present' bash "$UP_TMP/scripts/llm-usepod.sh" 'ping' 2>/dev/null)"
check "usepod falls back to Virtuals when token unset" "$FB_OUT" '{"ok":"virtuals-stub"}'

# --- research-prefetch.sh: safe failure when unusable (offline) ---
RP="$(cd "$(dirname "$0")/.." && pwd)/research-prefetch.sh"   # $0=scripts/advisor/selftest.sh, so dirname/.. = scripts/
# Unconfigured (no XAI_API_KEY) -> exit 1, no stdout.
RP_OUT="$(env -u XAI_API_KEY bash "$RP" 'find cheap polymarket bets' 2>/dev/null)"; RP_RC=$?
check "research-prefetch exits 1 without XAI_API_KEY" "$RP_RC" "1"
check "research-prefetch emits no stdout without key" "$RP_OUT" ""
# Empty query (key present but blank prompt) -> exit 1, no stdout.
RP_OUT2="$(XAI_API_KEY=dummy bash "$RP" '   ' 2>/dev/null)"; RP_RC2=$?
check "research-prefetch exits 1 on empty query" "$RP_RC2" "1"
check "research-prefetch emits no stdout on empty query" "$RP_OUT2" ""

# --- build-fallback-prompt.sh: research-grounded vs degraded prompt ---
BFP="$(cd "$(dirname "$0")/.." && pwd)/build-fallback-prompt.sh"
# With RESEARCH -> research-grounded prompt.
P_RESEARCH="$(SOURCE=telegram MESSAGE='find cheap polymarket bets' RESEARCH='- Market X underpriced (link, 2026-06-17)' bash "$BFP")"
check "research prompt includes LIVE RESEARCH" "$(printf '%s' "$P_RESEARCH" | grep -c 'LIVE RESEARCH')" "1"
check "research prompt includes the digest"    "$(printf '%s' "$P_RESEARCH" | grep -c 'Market X underpriced')" "1"
check "research prompt omits degraded line"     "$(printf '%s' "$P_RESEARCH" | grep -c 'degraded text-only fallback')" "0"
# Without RESEARCH -> degraded prompt.
P_DEGRADED="$(SOURCE=telegram MESSAGE='hi' bash "$BFP")"
check "degraded prompt has degraded line"        "$(printf '%s' "$P_DEGRADED" | grep -c 'degraded text-only fallback')" "1"
check "degraded prompt omits LIVE RESEARCH"      "$(printf '%s' "$P_DEGRADED" | grep -c 'LIVE RESEARCH')" "0"

# --- tg-chunk.sh: line-boundary chunking under the Telegram limit ---
TGC="$(cd "$(dirname "$0")/.." && pwd)/tg-chunk.sh"
# Consume NUL-delimited stdin -> "<count> <maxchunklen>" (portable: read -d '').
tgstats() { local c n=0 m=0; while IFS= read -r -d '' c; do n=$((n+1)); [ "${#c}" -gt "$m" ] && m="${#c}"; done; echo "$n $m"; }

SHORT="$(printf 'alpha\nbeta\ngamma')"
check "tg-chunk short -> 1 chunk"       "$(printf '%s' "$SHORT" | bash "$TGC" | tgstats | cut -d' ' -f1)" "1"
check "tg-chunk short reassembles"      "$(printf '%s' "$SHORT" | bash "$TGC" | tr -d '\0')" "$SHORT"

# ~6100 chars across 120 lines (50 'x' + newline each) -> multiple chunks, each <=4000.
LONG="$(for i in $(seq 1 120); do printf 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n'; done)"
set -- $(printf '%s' "$LONG" | bash "$TGC" | tgstats)
check "tg-chunk long -> >=2 chunks"     "$([ "$1" -ge 2 ] && echo yes)" "yes"
check "tg-chunk long chunks <=4000"     "$([ "$2" -le 4000 ] && echo yes)" "yes"
check "tg-chunk long reassembles"       "$(printf '%s' "$LONG" | bash "$TGC" | tr -d '\0')" "$LONG"

# Single 5000-char line, no newline -> hard-split into >=2 chunks, each <=4000.
BIG="$(printf 'y%.0s' $(seq 1 5000))"
set -- $(printf '%s' "$BIG" | bash "$TGC" | tgstats)
check "tg-chunk overlong line -> >=2"   "$([ "$1" -ge 2 ] && echo yes)" "yes"
check "tg-chunk overlong line <=4000"   "$([ "$2" -le 4000 ] && echo yes)" "yes"

# Exactly 4000 chars -> 1 chunk.
B4000="$(printf 'z%.0s' $(seq 1 4000))"
check "tg-chunk exactly 4000 -> 1 chunk" "$(printf '%s' "$B4000" | bash "$TGC" | tgstats | cut -d' ' -f1)" "1"

[ "$FAIL" -eq 0 ] && echo "selftest: ALL PASS" || { echo "selftest: FAILURES"; exit 1; }
