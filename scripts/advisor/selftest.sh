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

# --- run.sh recommendation fixture (shared by the Telegram filter checks) ---
RECS='[
 {"symbol":"BTC","direction":"increase","level":67000,"invalidateLevel":61000,"horizonDays":30,"title":"Add BTC","action":"deploy","rationale":"reclaim"},
 {"symbol":"REPPO","direction":"decrease","level":0.42,"invalidateLevel":0.5,"horizonDays":60,"title":"Trim REPPO","action":"trim"},
 {"symbol":null,"direction":"hold","level":null,"invalidateLevel":null,"horizonDays":30,"title":"Hold","action":"wait"},
 {"symbol":"MAMO","direction":"increase","level":null,"invalidateLevel":null,"horizonDays":30,"title":"Add MAMO","action":"buy"},
 {"symbol":"USDC","direction":"increase","level":1,"invalidateLevel":null,"horizonDays":30,"title":"Deploy USDC","action":"vault"}]'

# --- run.sh Telegram trade filter: directional recs surface, holds don't ---
TGTRADES=$(printf '%s' "$RECS" | jq -r '[.[] | select(.direction == "increase" or .direction == "decrease" or .direction == "hedge")] | length')
check "telegram surfaces all directional recs (incl decrease)" "$TGTRADES" "4"
TGEMPTY=$(printf '%s' '[{"direction":"hold","symbol":null}]' | jq -r '[.[] | select(.direction == "increase" or .direction == "decrease" or .direction == "hedge")] | length')
check "telegram trade list empty on all-hold report" "$TGEMPTY" "0"

# --- run.sh short-term trades: side-aware re-filter ---
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

# --- anthropic-gateway.sh: provider resolution + usepod routing (sourced) ---
GW="$(cd "$(dirname "$0")/.." && pwd)/anthropic-gateway.sh"
# Source in a subshell with controlled env; echo the resolved exports.
gw() { # GATEWAY, USEPOD_TOKEN, USEPOD_MODEL, MODEL  -> "BASEURL|MODEL|AUTH"
  ( export GATEWAY="$1" USEPOD_TOKEN="${2-}" USEPOD_MODEL="${3-}" MODEL="${4-}" \
      BANKR_LLM_KEY="" VIRTUALS_API_KEY=""
    . "$GW" >/dev/null 2>&1
    printf '%s|%s|%s' "${ANTHROPIC_BASE_URL:-}" "${GATEWAY_MODEL:-}" "${ANTHROPIC_AUTH_TOKEN:-}" )
}
check "gw usepod base url"   "$(gw usepod SECRET '' claude-opus-4-7 | cut -d'|' -f1)" "https://api.usepod.ai/proxy/SECRET"
check "gw usepod model default" "$(gw usepod SECRET '' claude-opus-4-7 | cut -d'|' -f2)" "deepseek-v3.2"
check "gw usepod model override" "$(gw usepod SECRET qwen-3.5 claude-opus-4-7 | cut -d'|' -f2)" "qwen-3.5"
check "gw usepod auth literal" "$(gw usepod SECRET '' x | cut -d'|' -f3)" "unused"
check "gw direct no base url" "$(gw direct '' '' claude-opus-4-7 | cut -d'|' -f1)" ""
check "gw direct keeps model" "$(gw direct '' '' claude-opus-4-7 | cut -d'|' -f2)" "claude-opus-4-7"
check "gw bankr base url"     "$( ( export GATEWAY=bankr BANKR_LLM_KEY=k USEPOD_TOKEN='' VIRTUALS_API_KEY='' MODEL=m; . "$GW" >/dev/null 2>&1; printf '%s' "${ANTHROPIC_BASE_URL:-}") )" "https://llm.bankr.bot"
check "gw virtuals base url"  "$( ( export GATEWAY=virtuals VIRTUALS_API_KEY=k USEPOD_TOKEN='' BANKR_LLM_KEY='' MODEL=m; . "$GW" >/dev/null 2>&1; printf '%s' "${ANTHROPIC_BASE_URL:-}") )" "https://compute.virtuals.io"
# Redaction: the usepod notice must NOT leak the token.
GW_NOTICE="$( ( export GATEWAY=usepod USEPOD_TOKEN=SUPERSECRET MODEL=x; . "$GW" 2>/dev/null ) )"
check "gw usepod notice redacted" "$(printf '%s' "$GW_NOTICE" | grep -c 'SUPERSECRET')" "0"
check "gw usepod notice has marker" "$(printf '%s' "$GW_NOTICE" | grep -c '<redacted>')" "1"
# Missing token -> non-zero.
( export GATEWAY=usepod USEPOD_TOKEN='' MODEL=x; . "$GW" >/dev/null 2>&1 ); check "gw usepod missing token fails" "$?" "1"
# Production mode: sourced under `set -e` with the `|| exit 1` contract MUST halt the
# caller (set -e alone does NOT abort on a sourced return — callers append || exit 1).
GW_REACHED="$(GATEWAY=usepod USEPOD_TOKEN='' MODEL=x bash -c 'set -euo pipefail; . "'"$GW"'" >/dev/null 2>&1 || exit 1; echo REACHED' 2>/dev/null)"
check "gw missing token halts set -e caller" "$GW_REACHED" ""
# Provider from aeon.yml config when GATEWAY unset.
GW_CFG_DIR="$(mktemp -d)"; printf 'gateway:\n  provider: usepod\n' > "$GW_CFG_DIR/aeon.yml"
check "gw reads provider from aeon.yml" "$( cd "$GW_CFG_DIR" && ( export USEPOD_TOKEN=T MODEL=x; unset GATEWAY; . "$GW" >/dev/null 2>&1; printf '%s' "${GATEWAY:-}") )" "usepod"

# --- per-skill usepod_model: extraction regexes + resolution chain ---
GWP="$(cd "$(dirname "$0")/.." && pwd)/anthropic-gateway.sh"
PS_DIR="$(mktemp -d)"
cat > "$PS_DIR/aeon.yml" <<'EOF'
gateway:
  provider: usepod
skills:
  heavyskill: { enabled: true, schedule: "0 12 * * *", usepod_model: "llama-4" }
  bothskill: { enabled: true, model: "claude-sonnet-4-6", usepod_model: "llama-4" }
  plainskill: { enabled: true, model: "claude-sonnet-4-6" }
  bareskill: { enabled: true }
EOF
# These two sed expressions MUST match the ones used in .github/workflows/aeon.yml.
skill_model()  { grep "^  $1:" "$PS_DIR/aeon.yml" | sed -n 's/.*[ ,{]model: *"\([^"]*\)".*/\1/p'; }
usepod_model() { grep "^  $1:" "$PS_DIR/aeon.yml" | sed -n 's/.*usepod_model: *"\([^"]*\)".*/\1/p'; }
resolve() { # skill -> GATEWAY_MODEL
  local u; u="$(usepod_model "$1")"
  ( cd "$PS_DIR"; export GATEWAY=usepod USEPOD_TOKEN=T MODEL="$(skill_model "$1")"; \
    [ -n "$u" ] && export USEPOD_MODEL="$u"; . "$GWP" >/dev/null 2>&1; printf '%s' "$GATEWAY_MODEL" )
}
check "usepod_model extracted for heavyskill" "$(usepod_model heavyskill)" "llama-4"
check "usepod_model empty for plainskill"     "$(usepod_model plainskill)" ""
check "SKILL_MODEL not fooled by usepod_model" "$(skill_model bothskill)" "claude-sonnet-4-6"
check "usepod_model on bothskill"              "$(usepod_model bothskill)" "llama-4"
check "resolve heavyskill -> llama-4"   "$(resolve heavyskill)" "llama-4"
check "resolve bothskill -> llama-4"    "$(resolve bothskill)" "llama-4"
check "resolve plainskill -> deepseek"  "$(resolve plainskill)" "deepseek-v3.2"
check "resolve bareskill -> deepseek"   "$(resolve bareskill)" "deepseek-v3.2"
check "resolve var-default for plainskill" "$( cd "$PS_DIR"; export GATEWAY=usepod USEPOD_TOKEN=T USEPOD_MODEL=qwen-3.5 MODEL=claude-sonnet-4-6; . "$GWP" >/dev/null 2>&1; printf '%s' "$GATEWAY_MODEL" )" "qwen-3.5"
# Drift guard: the sed regexes above are copies of the workflow's — assert the live
# workflow still contains both, so a future regex edit there can't silently diverge.
PS_WF="$(cd "$(dirname "$0")/../.." && pwd)/.github/workflows/aeon.yml"
check "workflow has tightened SKILL_MODEL regex" "$(grep -c 's/.*\[ ,{\]model: \*"' "$PS_WF")" "1"
check "workflow has usepod_model regex"          "$(grep -c 's/.*usepod_model: \*"' "$PS_WF")" "1"

# --- regime.sh: deterministic risk-on/off score from cached data ---
RGM="$(cd "$(dirname "$0")" && pwd)/regime.sh"
rgm_dir() { # writes synthetic cache into a fresh $D, echoes the dir
  local d; d="$(mktemp -d)"
  # $1 = trend: up|down ; $2 = fng value ; $3 = btc fundingHourly
  local base=100000 step; [ "$1" = "up" ] && step=800 || step=-800
  python3 - "$d/cg-btc.json" "$base" "$step" <<'PY'
import json,sys
path,base,step=sys.argv[1],float(sys.argv[2]),float(sys.argv[3])
prices=[]; t=1700000000000
for day in range(31):
    p=base+step*day
    for h in range(24):
        prices.append([t,p]); t+=3600000
json.dump({"prices":prices},open(path,"w"))
PY
  printf '{"data":[{"value":"%s"}]}' "$2" > "$d/fng.json"
  printf '[{"coin":"BTC","fundingHourly":%s,"openInterest":1,"markPx":1}]' "$3" > "$d/hl-funding.json"
  echo "$d"
}
D1="$(rgm_dir up 55 0.0000125)"; R1="$(D="$D1" bash "$RGM")"
check "regime uptrend band BULL" "$(printf '%s' "$R1" | jq -r '.band')" "BULL"
D2="$(rgm_dir down 45 0.0000125)"; R2="$(D="$D2" bash "$RGM")"
check "regime downtrend band BEAR" "$(printf '%s' "$R2" | jq -r '.band')" "BEAR"
# Tuning drift guard: downtrend must stay decisively BEAR (score margin under the
# 35 cutoff). Current downtrend score is 34; assert <=35 so a drift past the cutoff
# trips the test while real BEAR readings pass.
check "regime downtrend score <=35" "$(printf '%s' "$R2" | jq -r '.score<=35')" "true"
D3="$(rgm_dir up 92 0.0000125)"; R3="$(D="$D3" bash "$RGM")"
check "regime greed<=neutral score" "$(python3 -c "import json,sys;a=json.loads(sys.argv[1]);b=json.loads(sys.argv[2]);print('yes' if a['score']<=b['score'] else 'no')" "$R3" "$R1")" "yes"
D4="$(rgm_dir up 55 0.0008)"; R4="$(D="$D4" bash "$RGM")"
check "regime hot-funding lowers score" "$(python3 -c "import json,sys;a=json.loads(sys.argv[1]);b=json.loads(sys.argv[2]);print('yes' if a['score']<b['score'] else 'no')" "$R4" "$R1")" "yes"
D5="$(mktemp -d)"; printf '{"data":[{"value":"50"}]}' > "$D5/fng.json"
R5="$(D="$D5" bash "$RGM")"; RC5=$?
check "regime sparse -> UNKNOWN" "$(printf '%s' "$R5" | jq -r '.band')" "UNKNOWN"
check "regime sparse exit 0" "$RC5" "0"

# Volatility actually exercised: a high-variance series (alternating +/-5% daily
# closes) has REAL intraday variance, so its volatility sub-signal must be LOWER
# than the calm linear uptrend fixture (whose smooth ramp pins vol at the cap).
rgm_dir_vola() { # writes a fresh $D with a high-variance cg-btc series; echoes dir
  local d; d="$(mktemp -d)"
  python3 - "$d/cg-btc.json" <<'PY'
import json,sys
path=sys.argv[1]
prices=[]; t=1700000000000; p=100000.0
for day in range(31):
    p=p*(1.05 if day%2==0 else 0.95)   # alternating +/-5% day over day
    for h in range(24):
        prices.append([t,p]); t+=3600000
json.dump({"prices":prices},open(path,"w"))
PY
  printf '{"data":[{"value":"50"}]}' > "$d/fng.json"
  printf '[{"coin":"BTC","fundingHourly":0.0000125,"openInterest":1,"markPx":1}]' > "$d/hl-funding.json"
  echo "$d"
}
DV="$(rgm_dir_vola)"; RV="$(D="$DV" bash "$RGM")"
VOL_HI="$(printf '%s' "$RV" | jq -r '.signals.volatility')"
VOL_CALM="$(printf '%s' "$R1" | jq -r '.signals.volatility')"
check "regime high-variance vol < calm vol" \
  "$(python3 -c "import sys;print('yes' if float(sys.argv[1])<float(sys.argv[2]) else 'no')" "$VOL_HI" "$VOL_CALM")" "yes"

# F2: latest-bar sampling — a NON-24-aligned series (730 points, not a multiple of
# 24) whose FINAL bar is a sharp crash. The fixed reverse-anchored downsample makes
# closes[-1] the TRUE last price, so the crash must drag the score materially down
# (or flip the band to BEAR). Against the OLD index-0 forward sampling the crash bar
# is never sampled (730 % 24 != 0), so the score would be UNCHANGED — this test
# FAILS before F1 and PASSES after.
rgm_dir_crash() { # $1 = "crash" to override the final bar with a -40% crash, else clean
  local d; d="$(mktemp -d)"
  python3 - "$d/cg-btc.json" "${1:-clean}" <<'PY'
import json,sys
path,mode=sys.argv[1],sys.argv[2]
prices=[]; t=1700000000000; p=100000.0
# 730 points total (NOT a multiple of 24) on a steady uptrend.
N=730
for i in range(N):
    p=100000.0+40.0*i           # smooth ramp up
    prices.append([t,p]); t+=3600000
if mode=="crash":
    prices[-1][1]=prices[-1][1]*0.60   # final bar crashes -40%
json.dump({"prices":prices},open(path,"w"))
PY
  printf '{"data":[{"value":"55"}]}' > "$d/fng.json"
  printf '[{"coin":"BTC","fundingHourly":0.0000125,"openInterest":1,"markPx":1}]' > "$d/hl-funding.json"
  echo "$d"
}
DCL="$(rgm_dir_crash clean)"; RCL="$(D="$DCL" bash "$RGM")"
DCR="$(rgm_dir_crash crash)"; RCR="$(D="$DCR" bash "$RGM")"
check "regime latest-bar crash drags score down (F1/F2)" \
  "$(python3 -c "import json,sys;c=json.loads(sys.argv[1]);x=json.loads(sys.argv[2]);print('yes' if (x['band']=='BEAR' or x['score'] < c['score']-5) else 'no')" "$RCL" "$RCR")" "yes"

# #1 graceful degradation: corrupt cg-btc (non-numeric closes, jq null) + valid
# fng+funding must NOT crash. Exit 0, valid JSON, band UNKNOWN or NEUTRAL (momentum
# can't be computed, so a non-NEUTRAL band is forbidden).
DC="$(mktemp -d)"
printf '{"prices":[[1,"abc"],[2,null]]}' > "$DC/cg-btc.json"
printf '{"data":[{"value":"50"}]}' > "$DC/fng.json"
printf '[{"coin":"BTC","fundingHourly":0.0000125,"openInterest":1,"markPx":1}]' > "$DC/hl-funding.json"
RC_OUT="$(D="$DC" bash "$RGM")"; RC_RC=$?
check "regime corrupt cg-btc exit 0" "$RC_RC" "0"
check "regime corrupt cg-btc valid JSON" "$(printf '%s' "$RC_OUT" | jq -e . >/dev/null 2>&1 && echo ok)" "ok"
check "regime corrupt cg-btc band not BULL/BEAR" \
  "$(printf '%s' "$RC_OUT" | jq -r 'if .band=="UNKNOWN" or .band=="NEUTRAL" then "ok" else "bad" end')" "ok"

# #3 degraded state must NOT read BULL: missing cg-btc (only fng+funding) renormalizes
# to a risk-ON score, but with momentum absent the band MUST clamp to NEUTRAL.
DM="$(mktemp -d)"
printf '{"data":[{"value":"45"}]}' > "$DM/fng.json"
printf '[{"coin":"BTC","fundingHourly":0.0000125,"openInterest":1,"markPx":1}]' > "$DM/hl-funding.json"
RM_OUT="$(D="$DM" bash "$RGM")"; RM_RC=$?
check "regime missing cg-btc exit 0" "$RM_RC" "0"
check "regime missing cg-btc band NEUTRAL (not BULL)" "$(printf '%s' "$RM_OUT" | jq -r '.band')" "NEUTRAL"

# --- regime BEAR halves long short-term notionals, leaves shorts ---
# Uses the SHARED filter (scripts/advisor/lib/bear-halve.jq) so run.sh and the
# selftest can't drift apart. F4: a size-1 long halves DOWN to 0 — dust is dropped,
# and zero-sized trades are skipped at staging (defensive in a downtrend).
BHJQ="$(cd "$(dirname "$0")" && pwd)/lib/bear-halve.jq"
BEAR_IN='{"trades":[{"symbol":"A","side":"long","sizeUsd":1000,"sizePctNet":2.0},{"symbol":"B","side":"short","sizeUsd":800,"sizePctNet":1.6},{"symbol":"C","side":"long","sizeUsd":1,"sizePctNet":0.1}]}'
BEAR_OUT="$(printf '%s' "$BEAR_IN" | jq -c -f "$BHJQ")"
check "BEAR halves long sizeUsd"   "$(printf '%s' "$BEAR_OUT" | jq -r '.trades[0].sizeUsd')" "500"
check "BEAR leaves short sizeUsd"  "$(printf '%s' "$BEAR_OUT" | jq -r '.trades[1].sizeUsd')" "800"
check "BEAR drops size-1 long to 0 (dust)" "$(printf '%s' "$BEAR_OUT" | jq -r '.trades[2].sizeUsd')" "0"
# F1: bear-halve is case-insensitive on side — an uppercase LONG still halves.
BCASE="$(printf '%s' '{"trades":[{"symbol":"U","side":"LONG","sizeUsd":1000,"sizePctNet":2.0}]}' | jq -c -f "$BHJQ")"
check "F1 bear-halve halves uppercase LONG" "$(printf '%s' "$BCASE" | jq -r '.trades[0].sizeUsd')" "500"

# --- risk-size.sh: vol-target + caps + DD de-gross ---
RSZ="$(cd "$(dirname "$0")" && pwd)/risk-size.sh"
RS_DIR="$(mktemp -d)"
cat > "$RS_DIR/cg-markets.json" <<'EOF'
[{"id":"calm","symbol":"calm","price_change_percentage_24h":5,"price_change_percentage_7d_in_currency":5},
 {"id":"wild","symbol":"wild","price_change_percentage_24h":40,"price_change_percentage_7d_in_currency":40}]
EOF
rsz() { # trades-json ; RISK_NET ; RISK_DD  -> sized trades json
  printf '%s' "$1" | RISK_NET="$2" RISK_DD="${3:-0}" RISK_MKT="$RS_DIR/cg-markets.json" bash "$RSZ"
}
T2='{"trades":[{"symbol":"CALM","coingeckoId":"calm","side":"long","conviction":"MEDIUM"},{"symbol":"WILD","coingeckoId":"wild","side":"long","conviction":"MEDIUM"}]}'
O2="$(rsz "$T2" 400000 0)"
check "vol-target calm > wild" "$(printf '%s' "$O2" | jq -r '(.trades[]|select(.symbol=="CALM").sizeUsd) > (.trades[]|select(.symbol=="WILD").sizeUsd)')" "true"
T1='{"trades":[{"symbol":"CALM","coingeckoId":"calm","side":"long","conviction":"HIGH"}]}'
O1="$(rsz "$T1" 400000 0)"
check "per-position cap 1.5pct" "$(printf '%s' "$O1" | jq -r '.trades[0].sizeUsd <= 6000')" "true"
T5='{"trades":[{"symbol":"A","coingeckoId":"calm","side":"long","conviction":"HIGH"},{"symbol":"B","coingeckoId":"calm","side":"long","conviction":"HIGH"},{"symbol":"C","coingeckoId":"calm","side":"long","conviction":"HIGH"},{"symbol":"D","coingeckoId":"calm","side":"long","conviction":"HIGH"},{"symbol":"E","coingeckoId":"calm","side":"long","conviction":"HIGH"}]}'
O5="$(rsz "$T5" 400000 0)"
check "direction cap long sum <=3pct" "$(printf '%s' "$O5" | jq -r '([.trades[]|select(.side=="long").sizeUsd]|add) <= 12000')" "true"
# DD de-gross shrinks the BUDGET (not the fixed caps). Use 5 MEDIUM longs at net=40000:
# budget 5%=2000 split 5 ways = 400 each (< pos-cap 1.5%*40000=600, so budget binds);
# DD18 halves budget -> ~200 each. DD5 (no trigger) stays ~400.
TDD='{"trades":[{"symbol":"A","coingeckoId":"calm","side":"long","conviction":"MEDIUM"},{"symbol":"B","coingeckoId":"calm","side":"long","conviction":"MEDIUM"},{"symbol":"C","coingeckoId":"calm","side":"long","conviction":"MEDIUM"},{"symbol":"D","coingeckoId":"calm","side":"long","conviction":"MEDIUM"},{"symbol":"E","coingeckoId":"calm","side":"long","conviction":"MEDIUM"}]}'
DSUM0="$(printf '%s' "$TDD" | RISK_NET=40000 RISK_DD=5  RISK_MKT="$RS_DIR/cg-markets.json" bash "$RSZ" | jq '[.trades[].sizeUsd]|add')"
DSUM1="$(printf '%s' "$TDD" | RISK_NET=40000 RISK_DD=18 RISK_MKT="$RS_DIR/cg-markets.json" bash "$RSZ" | jq '[.trades[].sizeUsd]|add')"
check "DD18 degrosses budget vs DD5" "$( [ "$DSUM1" -lt "$DSUM0" ] && echo yes )" "yes"
ODIS="$(printf '%s' "$T1" | RISK_DISABLE=1 RISK_NET=400000 RISK_MKT="$RS_DIR/cg-markets.json" bash "$RSZ")"
check "RISK_DISABLE conviction-split uncapped" "$(printf '%s' "$ODIS" | jq -r '.trades[0].sizeUsd')" "20000"
check "sizePctNet matches sizeUsd" "$(printf '%s' "$O1" | jq -r '.trades[0].sizePctNet == ((.trades[0].sizeUsd/400000*1000)|round)/10')" "true"
# Bad price (inf-ish vol) must NOT zero a single legit pick — degrades to a positive (capped) size.
cat > "$RS_DIR/cg-bad.json" <<'EOF'
[{"id":"bad","symbol":"bad","price_change_percentage_24h":1e9,"price_change_percentage_7d_in_currency":1e9}]
EOF
OBAD="$(printf '%s' '{"trades":[{"symbol":"BAD","coingeckoId":"bad","side":"long","conviction":"HIGH"}]}' | RISK_NET=400000 RISK_DD=0 RISK_MKT="$RS_DIR/cg-bad.json" bash "$RSZ")"
check "bad price does not zero pick" "$(printf '%s' "$OBAD" | jq -r '.trades[0].sizeUsd > 0')" "true"
# Garbage stdin → valid JSON out (never poisons downstream jq).
OGARB="$(printf '%s' 'not json {{{' | RISK_NET=400000 RISK_MKT="$RS_DIR/cg-markets.json" bash "$RSZ")"
check "garbage stdin -> valid json" "$(printf '%s' "$OGARB" | jq -e 'has("trades")' >/dev/null 2>&1 && echo ok)" "ok"

# F1: mixed-case side ("Long"/"LONG") must still bucket into the direction cap and
# be normalized to lowercase on output (otherwise it escapes the cap entirely).
TCASE='{"trades":[{"symbol":"A","coingeckoId":"calm","side":"Long","conviction":"HIGH"},{"symbol":"B","coingeckoId":"calm","side":"LONG","conviction":"HIGH"},{"symbol":"C","coingeckoId":"calm","side":"Long","conviction":"HIGH"},{"symbol":"D","coingeckoId":"calm","side":"long","conviction":"HIGH"},{"symbol":"E","coingeckoId":"calm","side":"long","conviction":"HIGH"}]}'
OCASE="$(rsz "$TCASE" 400000 0)"
check "F1 mixed-case side hits direction cap" "$(printf '%s' "$OCASE" | jq -r '([.trades[].sizeUsd]|add) <= 12000')" "true"
check "F1 side normalized to lowercase"      "$(printf '%s' "$OCASE" | jq -r '[.trades[].side]|unique|join(",")')" "long"
# F2: a negative net must never yield negative sizes.
ONEG="$(rsz "$T1" -5000 0)"
check "F2 negative net -> no negative size" "$(printf '%s' "$ONEG" | jq -r '[.trades[].sizeUsd]|all(. >= 0)')" "true"
# F3: a tiny/seed account (sub-$1 per-position cap) is NOT zeroed by the cap.
OTINY="$(rsz "$T1" 50 0)"
check "F3 tiny account not zeroed by pos-cap" "$(printf '%s' "$OTINY" | jq -r '.trades[0].sizeUsd > 0')" "true"

# Risk layer is the sizing authority: a 0-sized short-term trade must be SKIPPED at
# staging, never rewritten to the legacy $1000 default.
STG='{"shortTermTrades":[{"symbol":"Z","sizeUsd":0,"side":"long"},{"symbol":"P","sizeUsd":3000,"side":"long"}]}'
# staged set = trades with sizeUsd>0 (the guard); notional = sizeUsd (no 1000 default)
STAGED="$(printf '%s' "$STG" | jq -c '[.shortTermTrades[] | select((.sizeUsd // 0) > 0) | {symbol, notionalUsd: (.sizeUsd // 0)}]')"
check "0-size short-term trade skipped" "$(printf '%s' "$STAGED" | jq -r 'length')" "1"
check "no \$1000 default for risk-sized" "$(printf '%s' "$STAGED" | jq -r '.[0].notionalUsd')" "3000"

# --- PM committee: deterministic quorum aggregator (shared lib/pm-quorum.jq) ---
# Three canned members (all ok) vote. BTC/increase has 3 supporters => consensus;
# ETH/decrease (deepseek only) and SOL/increase (qwen only) are single-member =>
# dissent, never dropped. Most-conservative urgency = min(high,med,low)=low;
# level = median(67000,66000,65000)=66000; consensusPct = 3/3 = 100.
PMQ="$(cd "$(dirname "$0")" && pwd)/lib/pm-quorum.jq"
CMEMBERS='[
 {"model":"deepseek-v3.2","ok":true,"latencyMs":1200,"recommendations":[
   {"symbol":"BTC","direction":"increase","urgency":"high","level":67000,"title":"Add BTC"},
   {"symbol":"ETH","direction":"decrease","urgency":"medium","level":3500,"title":"Trim ETH"}]},
 {"model":"qwen-3.5","ok":true,"latencyMs":1500,"recommendations":[
   {"symbol":"BTC","direction":"increase","urgency":"medium","level":66000,"title":"BTC add"},
   {"symbol":"SOL","direction":"increase","urgency":"low","level":150,"title":"SOL"}]},
 {"model":"llama-4","ok":true,"latencyMs":900,"recommendations":[
   {"symbol":"btc","direction":"increase","urgency":"low","level":65000,"title":"btc"}]}]'
# Quorum = ceil(N/2) over ok members; N=3 -> 2.
CN=$(printf '%s' "$CMEMBERS" | jq '[.[]|select(.ok==true)]|length')
CQUORUM=$(( (CN + 1) / 2 ))
check "committee quorum ceil(3/2)=2" "$CQUORUM" "2"
CAGG=$(printf '%s' "$CMEMBERS" | jq -c --argjson quorum "$CQUORUM" -f "$PMQ")
check "quorum picks 1 consensus"        "$(printf '%s' "$CAGG" | jq -r '.consensus|length')" "1"
check "quorum consensus is BTC"         "$(printf '%s' "$CAGG" | jq -r '.consensus[0].symbol')" "BTC"
check "quorum most-conservative urgency"  "$(printf '%s' "$CAGG" | jq -r '.consensus[0].urgency')" "low"
check "quorum median level"             "$(printf '%s' "$CAGG" | jq -r '.consensus[0].level')" "66000"
check "quorum consensusPct 100"         "$(printf '%s' "$CAGG" | jq -r '.consensus[0].consensusPct')" "100"
check "quorum support lists 3 models"   "$(printf '%s' "$CAGG" | jq -r '.consensus[0].support|length')" "3"
check "quorum keeps single-member as dissent (not dropped)" "$(printf '%s' "$CAGG" | jq -r '.dissent|length')" "2"
check "quorum dissent has ETH + SOL"    "$(printf '%s' "$CAGG" | jq -r '[.dissent[].symbol]|sort|join(",")')" "ETH,SOL"
# Raising the quorum above the max support (3) yields zero consensus, all dissent.
CAGG3=$(printf '%s' "$CMEMBERS" | jq -c --argjson quorum 4 -f "$PMQ")
check "quorum too-high -> no consensus" "$(printf '%s' "$CAGG3" | jq -r '.consensus|length')" "0"
check "quorum too-high -> all dissent"  "$(printf '%s' "$CAGG3" | jq -r '.dissent|length')" "3"

# --- PM committee: degradation path (<2 ok members) falls back to single-model ---
# Mirrors run.sh: OK_N = ok members; OK_N < 2 => "degrade" (single-model PM path).
DMEMBERS='[{"model":"a","ok":true,"latencyMs":10,"recommendations":[]},
 {"model":"b","ok":false,"latencyMs":0,"recommendations":[]},
 {"model":"c","ok":false,"latencyMs":0,"recommendations":[]}]'
DOKN=$(printf '%s' "$DMEMBERS" | jq '[.[]|select(.ok==true)]|length')
check "committee counts only ok members" "$DOKN" "1"
check "committee <2 ok -> degrade path" "$([ "$DOKN" -ge 2 ] && echo committee || echo degrade)" "degrade"
GMEMBERS='[{"model":"a","ok":true,"latencyMs":10,"recommendations":[]},
 {"model":"b","ok":true,"latencyMs":20,"recommendations":[]}]'
GOKN=$(printf '%s' "$GMEMBERS" | jq '[.[]|select(.ok==true)]|length')
check "committee >=2 ok -> committee path" "$([ "$GOKN" -ge 2 ] && echo committee || echo degrade)" "committee"

# --- PM committee: report.committee block shape ---
# Mirrors the run.sh assembly: {members,consensus,dissent}; members carry
# model/ok/latencyMs/recommendations.
CJSON=$(jq -n --argjson members "$CMEMBERS" --argjson agg "$CAGG" \
  '{members:$members, consensus:$agg.consensus, dissent:$agg.dissent}')
check "committee block has members/consensus/dissent" \
  "$(printf '%s' "$CJSON" | jq -r 'has("members") and has("consensus") and has("dissent")')" "true"
check "committee members carry model/ok/latencyMs/recommendations" \
  "$(printf '%s' "$CJSON" | jq -r '.members[0]|(has("model") and has("ok") and has("latencyMs") and has("recommendations"))')" "true"
# modelInfo.pm shape when committee is on: {committee[],chair,quorum}.
PMI=$(printf '%s' "deepseek-v3.2,qwen-3.5,llama-4" | jq -R --argjson q 2 \
  '{committee:(split(",")|map(gsub("^\\s+|\\s+$";""))|map(select(length>0))), chair:null, quorum:$q}')
check "modelInfo.pm committee has 3 models" "$(printf '%s' "$PMI" | jq -r '.committee|length')" "3"
check "modelInfo.pm chair null (no phase 2)" "$(printf '%s' "$PMI" | jq -r '.chair')" "null"
check "modelInfo.pm quorum recorded"        "$(printf '%s' "$PMI" | jq -r '.quorum')" "2"

# --- llm-usepod.sh: NO_VIRTUALS_FALLBACK emits NO Virtuals call (offline stub) ---
# Token unset + a stub Virtuals llm.sh that TOUCHES a sentinel if invoked. With
# NO_VIRTUALS_FALLBACK=1 the script must exit non-zero, print nothing, and NEVER
# call the stub (sentinel absent) — preserving per-model attribution.
NV_DIR="$(cd "$(dirname "$0")/.." && pwd)"   # scripts/
NV_TMP="$(mktemp -d)"; mkdir -p "$NV_TMP/scripts"
cp "$NV_DIR/llm-usepod.sh" "$NV_TMP/scripts/llm-usepod.sh"
cat > "$NV_TMP/scripts/llm.sh" <<EOF
#!/usr/bin/env bash
cat >/dev/null
touch "$NV_TMP/virtuals-was-called"
echo '{"ok":"virtuals-stub"}'
EOF
chmod +x "$NV_TMP/scripts/llm.sh" "$NV_TMP/scripts/llm-usepod.sh"
NV_OUT="$(USEPOD_TOKEN='' VIRTUALS_API_KEY='present' NO_VIRTUALS_FALLBACK=1 bash "$NV_TMP/scripts/llm-usepod.sh" 'ping' 2>/dev/null)"; NV_RC=$?
check "NO_VIRTUALS_FALLBACK exits non-zero" "$NV_RC" "1"
check "NO_VIRTUALS_FALLBACK emits no stdout" "$NV_OUT" ""
check "NO_VIRTUALS_FALLBACK makes no Virtuals call" \
  "$([ -f "$NV_TMP/virtuals-was-called" ] && echo called || echo none)" "none"
# Control: WITHOUT the flag, the same setup DOES fall back to Virtuals (sentinel set).
CTRL_TMP="$(mktemp -d)"; mkdir -p "$CTRL_TMP/scripts"
cp "$NV_DIR/llm-usepod.sh" "$CTRL_TMP/scripts/llm-usepod.sh"
cat > "$CTRL_TMP/scripts/llm.sh" <<EOF
#!/usr/bin/env bash
cat >/dev/null
echo '{"ok":"virtuals-stub"}'
EOF
chmod +x "$CTRL_TMP/scripts/llm.sh" "$CTRL_TMP/scripts/llm-usepod.sh"
CTRL_OUT="$(USEPOD_TOKEN='' VIRTUALS_API_KEY='present' bash "$CTRL_TMP/scripts/llm-usepod.sh" 'ping' 2>/dev/null)"
check "without flag, fallback still reaches Virtuals" "$CTRL_OUT" '{"ok":"virtuals-stub"}'

# --- llm-usepod.sh: optional price-ceiling headers built only when env set ---
# The header-array construction lives in llm-usepod.sh; assert the exact array
# logic here (curl is never invoked offline). Empty env -> no headers.
build_price_headers() { # returns count of header tokens
  local PRICE_HEADERS=()
  [ -n "${USEPOD_MAX_PRICE_INPUT:-}" ]  && PRICE_HEADERS+=(-H "X-Pod-Max-Price-Input: ${USEPOD_MAX_PRICE_INPUT}")
  [ -n "${USEPOD_MAX_PRICE_OUTPUT:-}" ] && PRICE_HEADERS+=(-H "X-Pod-Max-Price-Output: ${USEPOD_MAX_PRICE_OUTPUT}")
  printf '%s' "${#PRICE_HEADERS[@]}"
}
check "no price ceilings -> 0 header tokens" "$(USEPOD_MAX_PRICE_INPUT='' USEPOD_MAX_PRICE_OUTPUT='' build_price_headers)" "0"
check "both ceilings -> 4 header tokens"     "$(USEPOD_MAX_PRICE_INPUT=5 USEPOD_MAX_PRICE_OUTPUT=8 build_price_headers)" "4"
check "one ceiling -> 2 header tokens"       "$(USEPOD_MAX_PRICE_INPUT=5 USEPOD_MAX_PRICE_OUTPUT='' build_price_headers)" "2"

[ "$FAIL" -eq 0 ] && echo "selftest: ALL PASS" || { echo "selftest: FAILURES"; exit 1; }
