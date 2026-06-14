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

[ "$FAIL" -eq 0 ] && echo "selftest: ALL PASS" || { echo "selftest: FAILURES"; exit 1; }
