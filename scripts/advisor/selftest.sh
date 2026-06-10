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

[ "$FAIL" -eq 0 ] && echo "selftest: ALL PASS" || { echo "selftest: FAILURES"; exit 1; }
