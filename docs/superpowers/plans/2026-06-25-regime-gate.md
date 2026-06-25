# Advisor Regime Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Compute a deterministic BTC risk-on/off regime score before the advisor swarm and make it the master gate — a strong PM prior plus a code-enforced BEAR long-size halving — to stop momentum-chasing into downtrends.

**Architecture:** New pure `scripts/advisor/regime.sh` reads already-cached prefetch JSON (cg-btc/hl-funding/fng) and emits `{score,band,signals}`. `run.sh` computes it pre-swarm, injects it as a datablock into every analyst + PM prompt, halves new long notionals when BEAR, and adds it to the report + Telegram line. No new APIs.

**Tech Stack:** Bash + jq + python3 (float math), GitHub Actions. Offline tests in `scripts/advisor/selftest.sh`.

**Branch:** `regime` worktree off `main` (`.worktrees/regime`). Issue #139.

**Verified data shapes (origin/main prefetch):**
- `cg-btc.json` = CoinGecko `market_chart?days=30` → `.prices` is `[[ms,usd],…]`, **hourly** (~720 pts). Daily closes = every 24th element (existing pattern: `[.prices[]?|.[1]] | [range(0;length;24) as $i|.[$i]]`).
- `fng.json` = alternative.me `fng/?limit=1` → `.data[0].value` is a **string** ("0".."100"), single current reading (no history).
- `hl-funding.json` = `[{coin,fundingHourly,openInterest,markPx}]` for BTC & ETH. BTC funding = `[.[]|select(.coin=="BTC")|.fundingHourly]|first` (hourly rate, e.g. 0.0000125).

---

## File Structure

- **Create** `scripts/advisor/regime.sh` — pure score computer; reads `$D/*.json`, emits one JSON. Only real logic; unit-tested.
- **Modify** `scripts/advisor/run.sh` — compute regime pre-swarm; inject datablock into analyst + PM prompts; halve BEAR long notionals; add `regime` to report; Telegram line.
- **Modify** `advisor/prompts/portfolio_manager.md` — regime master-prior section.
- **Modify** `scripts/advisor/selftest.sh` — offline assertions (score bands, graceful UNKNOWN, BEAR halving).

---

## Task 1: `scripts/advisor/regime.sh` + tests

**Files:**
- Create: `scripts/advisor/regime.sh`
- Test: `scripts/advisor/selftest.sh` (append before final pass/fail line)

- [ ] **Step 1: Write the failing tests**

Append to `scripts/advisor/selftest.sh` before the final `[ "$FAIL" -eq 0 ] && echo "selftest: ALL PASS" ...` line:

```bash
# --- regime.sh: deterministic risk-on/off score from cached data ---
RGM="$(cd "$(dirname "$0")" && pwd)/regime.sh"
rgm_dir() { # writes synthetic cache into a fresh $D, echoes the dir
  local d; d="$(mktemp -d)"
  # $1 = trend: up|down ; $2 = fng value ; $3 = btc fundingHourly
  local base=100000 step; [ "$1" = "up" ] && step=800 || step=-800
  # 31 daily closes (hourly array, 24 pts/day) — emit prices [[ms,usd],...]
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
# Strong uptrend, neutral funding, FNG 55 -> BULL (>=60)
D1="$(rgm_dir up 55 0.0000125)"; R1="$(D="$D1" bash "$RGM")"
check "regime uptrend band BULL" "$(printf '%s' "$R1" | jq -r '.band')" "BULL"
# Downtrend -> BEAR (<=35)
D2="$(rgm_dir down 45 0.0000125)"; R2="$(D="$D2" bash "$RGM")"
check "regime downtrend band BEAR" "$(printf '%s' "$R2" | jq -r '.band')" "BEAR"
# Extreme greed caps sentiment: same uptrend, FNG 92 scores LOWER than FNG 55
D3="$(rgm_dir up 92 0.0000125)"; R3="$(D="$D3" bash "$RGM")"
check "regime greed<=neutral score" "$(python3 -c "import json,sys;a=json.loads(sys.argv[1]);b=json.loads(sys.argv[2]);print('yes' if a['score']<=b['score'] else 'no')" "$R3" "$R1")" "yes"
# Extreme positive funding lowers score vs neutral, same uptrend+fng
D4="$(rgm_dir up 55 0.0008)"; R4="$(D="$D4" bash "$RGM")"
check "regime hot-funding lowers score" "$(python3 -c "import json,sys;a=json.loads(sys.argv[1]);b=json.loads(sys.argv[2]);print('yes' if a['score']<b['score'] else 'no')" "$R4" "$R1")" "yes"
# Only 1 input present -> UNKNOWN, graceful exit 0
D5="$(mktemp -d)"; printf '{"data":[{"value":"50"}]}' > "$D5/fng.json"
R5="$(D="$D5" bash "$RGM")"; RC5=$?
check "regime sparse -> UNKNOWN" "$(printf '%s' "$R5" | jq -r '.band')" "UNKNOWN"
check "regime sparse exit 0" "$RC5" "0"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `bash scripts/advisor/selftest.sh`
Expected: FAIL — `regime.sh` missing, `bash "$RGM"` errors; band assertions mismatch. Final `selftest: FAILURES`.

- [ ] **Step 3: Create `scripts/advisor/regime.sh`**

```bash
#!/usr/bin/env bash
# scripts/advisor/regime.sh — deterministic BTC risk-on/off score (0-100) + band.
# Reads the prefetched cache ($D/cg-btc.json, hl-funding.json, fng.json); emits ONE
# JSON object: {score, band, signals:{momentum,funding,volatility,sentiment}, asOf}.
# Pure: no network, no LLM. Missing inputs are omitted and weights renormalize; with
# <2 signals -> band UNKNOWN / score null. Never aborts the caller. No `set -x`.
set -uo pipefail
D="${D:-$(cd "$(dirname "$0")/../.." && pwd)/.investiments-cache/advisor}"
now="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo "")"

W_MOM="${REGIME_W_MOMENTUM:-0.40}"; W_FUND="${REGIME_W_FUNDING:-0.25}"
W_VOL="${REGIME_W_VOLATILITY:-0.20}"; W_SENT="${REGIME_W_SENTIMENT:-0.15}"
BEAR_MAX="${REGIME_BEAR_MAX:-35}"; BULL_MIN="${REGIME_BULL_MIN:-60}"

# Daily closes (every 24th hourly point) as a space list, or empty.
CLOSES="$(jq -r '[.prices[]? | .[1]] | [range(0; length; 24) as $i | .[$i]] | @tsv' \
  "$D/cg-btc.json" 2>/dev/null | tr '\t' ' ' || true)"
FNG="$(jq -r '.data[0].value // empty' "$D/fng.json" 2>/dev/null || true)"
FUND="$(jq -r '[.[]? | select(.coin=="BTC") | .fundingHourly] | first // empty' \
  "$D/hl-funding.json" 2>/dev/null || true)"

# Compute the composite in python (floats); emit the final JSON.
CLOSES="$CLOSES" FNG="$FNG" FUND="$FUND" \
W_MOM="$W_MOM" W_FUND="$W_FUND" W_VOL="$W_VOL" W_SENT="$W_SENT" \
BEAR_MAX="$BEAR_MAX" BULL_MIN="$BULL_MIN" NOW="$now" python3 <<'PY'
import os, json, statistics, math
def fenv(k):
    v=os.environ.get(k,"").strip()
    try: return float(v)
    except: return None
closes=[float(x) for x in os.environ.get("CLOSES","").split() if x.strip()]
fng=fenv("FNG"); fund=fenv("FUND")
wm,wf,wv,ws=fenv("W_MOM"),fenv("W_FUND"),fenv("W_VOL"),fenv("W_SENT")
bear_max,bull_min=fenv("BEAR_MAX"),fenv("BULL_MIN")
sig={}
# Momentum: latest vs 7d & 30d(full-window) MA. above both ~100, below both ~0, one ~50.
if len(closes)>=8:
    last=closes[-1]; ma7=statistics.mean(closes[-7:]); ma30=statistics.mean(closes)
    above=(1 if last>ma7 else 0)+(1 if last>ma30 else 0)
    drift=max(-0.15,min(0.15,(last-ma30)/ma30)) if ma30 else 0
    sig["momentum"]=round(max(0,min(100, above*30 + 20 + (drift/0.15)*20)))
# Volatility: 14d daily-return stdev annualized; low vol high score.
if len(closes)>=15:
    rets=[math.log(closes[i]/closes[i-1]) for i in range(len(closes)-13,len(closes)) if closes[i-1]>0]
    if rets:
        vol=statistics.pstdev(rets)*math.sqrt(365)
        sig["volatility"]=round(max(0,min(100,(1.2-vol)/(1.2-0.3)*100)))
# Funding: neutral ~70; hot positive lowers, negative raises (contrarian).
if fund is not None:
    sig["funding"]=round(max(0,min(100, 70 - (fund/0.0005)*50)))
# Sentiment: FNG direct but fade extremes (>80 greed caps, <20 fear floors up).
if fng is not None:
    s=fng
    if fng>80: s=80-(fng-80)*1.5
    if fng<20: s=20+(20-fng)*0.5
    sig["sentiment"]=round(max(0,min(100,s)))
wmap={"momentum":wm,"funding":wf,"volatility":wv,"sentiment":ws}
present={k:v for k,v in sig.items()}
if len(present)<2:
    print(json.dumps({"score":None,"band":"UNKNOWN","signals":present,"asOf":os.environ.get("NOW","")}))
else:
    wsum=sum(wmap[k] for k in present)
    score=round(sum(present[k]*wmap[k] for k in present)/wsum)
    band="BEAR" if score<=bear_max else ("BULL" if score>=bull_min else "NEUTRAL")
    print(json.dumps({"score":score,"band":band,"signals":present,"asOf":os.environ.get("NOW","")}))
PY
```

- [ ] **Step 4: Make executable**

Run: `chmod +x scripts/advisor/regime.sh`
Expected: no output.

- [ ] **Step 5: Run tests to verify they pass**

Run: `bash scripts/advisor/selftest.sh`
Expected: the 6 new `regime …` checks `ok`, final `selftest: ALL PASS`. If a band check is off, tune the weights/maps in Step 3 (NOT the test thresholds) until uptrend→BULL and downtrend→BEAR.

- [ ] **Step 6: Syntax check**

Run: `bash -n scripts/advisor/regime.sh && echo "regime.sh OK"`
Expected: `regime.sh OK`

- [ ] **Step 7: Commit**

```bash
git add scripts/advisor/regime.sh scripts/advisor/selftest.sh
git commit -m "feat(advisor): regime.sh — deterministic BTC risk-on/off score (issue #139)"
```

---

## Task 2: Wire regime into `run.sh` (compute + inject + report + notify)

**Files:**
- Modify: `scripts/advisor/run.sh` (after `PROMPTS=` ~line 61 region for compute; analyst loop ~256; report merge ~348; telegram ~654)

- [ ] **Step 1: Compute regime pre-swarm**

In `scripts/advisor/run.sh`, find the pre-analyst region (after `PROMPTS="$ROOT/advisor/prompts"`, before the `ANALYSTS=` loop ~line 256). Add (match surrounding top-level indentation):

```bash
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
```

- [ ] **Step 2: Inject the regime datablock into analyst + PM prompts**

Add the regime block so every analyst AND the PM see it. In the `ANALYSTS` loop where each `prompt="$(cat "$tmpl") … $(role_data "$role")"` is built, and in the PM assembly (`pm_prompt="$(cat "$PROMPTS/portfolio_manager.md") …"`), add this line near the top of each prompt's data section:

```bash
$(datablock regime regime.json '.')
```
(The `datablock` helper reads `$D/regime.json`, written in Step 1.)

- [ ] **Step 3: Add `regime` to the posted report**

Find the report-merge `jq -n` (~line 348, `REPORT="$(jq -n --argjson rpt "$REPORT" ...`). Add `--argjson regime "$REGIME_JSON"` to its args and `| .regime = $regime` to the filter body.

- [ ] **Step 4: Prepend a regime line to the Telegram summary**

Find the Telegram summary build (~line 620–650, the `jq` composing the message before `sendMessage` ~654). Pass `--arg band "$REGIME_BAND" --arg score "$REGIME_SCORE"` into that jq and prepend `"REGIME: " + $band + " " + $score + "/100\n"` to the message string (one line at the top).

- [ ] **Step 5: Verify run.sh parses + regime reachable**

Run:
```bash
bash -n scripts/advisor/run.sh && echo "run.sh OK"
grep -n "regime.sh\|REGIME_BAND\|datablock regime\|\.regime = \$regime" scripts/advisor/run.sh
```
Expected: `run.sh OK`; grep shows the compute line, two datablock injections (analyst + PM), and the report merge.

- [ ] **Step 6: Commit**

```bash
git add scripts/advisor/run.sh
git commit -m "feat(advisor): compute + inject regime into swarm, report, and Telegram (issue #139)"
```

---

## Task 3: PM prior + BEAR long-size halving (enforcement)

**Files:**
- Modify: `advisor/prompts/portfolio_manager.md`
- Modify: `scripts/advisor/run.sh` (short-term sizing ~471; daily-pick staging)

- [ ] **Step 1: Add the regime master-prior to the PM prompt**

In `advisor/prompts/portfolio_manager.md`, insert ABOVE the `### Actionability requirement` section:

```markdown
### Regime gate (master prior)
A `regime` datablock gives a deterministic BTC risk-on/off score (0–100) + band. It
overrides the bias toward action:
- **BEAR** (≤35): default to NO new long risk — favor trims, hedges, stables, shorts.
  The mandatory forward-looking opportunity may be a CONDITIONAL re-entry ("if regime
  flips BULL / BTC reclaims $X"), not a live long. A live new long needs an explicit
  override reason naming what the score misses.
- **NEUTRAL** (35–60): new risk allowed, high-bar, half-conviction.
- **BULL** (≥60): normal sleeve.
- **UNKNOWN**: proceed normally (no regime data).
State the regime band + score in your summary's first sentence.
```

- [ ] **Step 2: Halve BEAR long notionals (short-term trades)**

After the short-term sizing jq (~line 471, setting `.sizeUsd`/`.sizePctNet`) and BEFORE the `.shortTermTrades` merge (~line 472), add:

```bash
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
```

- [ ] **Step 3: Halve BEAR long notionals (daily directional picks)**

First READ the daily-pick staging block (the `while read rec … SIDE=long; [ "$DIR" = "increase" ] || SIDE=short …` loop, ~line 490–550) to confirm whether the POST body carries `notionalUsd`. Two cases:
- **If the daily PICK JSON sets `notionalUsd`:** right before its POST, add:
  ```bash
  if [ "${REGIME_BAND:-UNKNOWN}" = "BEAR" ] && [ "$SIDE" = "long" ]; then
    PICK="$(printf '%s' "$PICK" | jq -c '.notionalUsd = ((.notionalUsd // 1000) / 2 | floor)')"
    echo "advisor: regime BEAR — halved long daily pick $SYM notional"
  fi
  ```
- **If daily picks have NO notional at staging** (server assigns $1k): skip the size change; instead add `| .regimeHalved = true` to the PICK jq when BEAR+long, and log it — note in the commit that daily-pick notional is server-assigned so only the flag is set. (Short-term trades in Step 2 carry the variable sizing and the main exposure — they are the load-bearing fix.)

- [ ] **Step 4: Verify**

Run:
```bash
bash -n scripts/advisor/run.sh && echo "run.sh OK"
grep -n "Regime gate (master prior)" advisor/prompts/portfolio_manager.md
grep -n "regime BEAR — halved" scripts/advisor/run.sh
```
Expected: `run.sh OK`; prompt section present; ≥1 halving log line.

- [ ] **Step 5: Add a selftest for the BEAR halving filter**

Append to `scripts/advisor/selftest.sh` before the final pass/fail line:

```bash
# --- regime BEAR halves long short-term notionals, leaves shorts ---
BEAR_IN='{"trades":[{"symbol":"A","side":"long","sizeUsd":1000,"sizePctNet":2.0},{"symbol":"B","side":"short","sizeUsd":800,"sizePctNet":1.6}]}'
BEAR_OUT="$(printf '%s' "$BEAR_IN" | jq -c '
  {trades: [ .trades[] | if (.side // "long") == "long"
    then .sizeUsd = ((.sizeUsd // 0)/2|floor) | .sizePctNet = (((.sizePctNet // 0)*10/2|round)/10) | .regimeHalved=true
    else . end ]}')"
check "BEAR halves long sizeUsd"   "$(printf '%s' "$BEAR_OUT" | jq -r '.trades[0].sizeUsd')" "500"
check "BEAR leaves short sizeUsd"  "$(printf '%s' "$BEAR_OUT" | jq -r '.trades[1].sizeUsd')" "800"
```

- [ ] **Step 6: Run suite + commit**

Run: `bash scripts/advisor/selftest.sh` → `selftest: ALL PASS`.
```bash
git add advisor/prompts/portfolio_manager.md scripts/advisor/run.sh scripts/advisor/selftest.sh
git commit -m "feat(advisor): regime PM prior + BEAR long-size halving (issue #139)"
```

---

## Task 4: Full suite + final review

- [ ] **Step 1: Full offline suite**

Run: `bash scripts/advisor/selftest.sh`
Expected: all `ok`, final `selftest: ALL PASS`, exit 0.

- [ ] **Step 2: Confirm graceful disable exists**

Run: `grep -n 'REGIME_DISABLE' scripts/advisor/run.sh`
Expected: shows the guard (instant rollback path).

- [ ] **Step 3 (operator, needs creds): dry-run the advisor**

```bash
gh workflow run investment-advisor.yml -R anajuliabit/aeon
# log shows: "advisor: regime <BAND> (<score>/100)"; report carries .regime;
# if BEAR, "regime BEAR — halved long ..." appears when a long pick is staged.
```
Expected: regime line in log, regime in report, no run failure. If `regime UNKNOWN` on a live run, check the cg-btc/hl-funding/fng cache shapes vs Task 1 assumptions and adjust jq paths.

---

## Self-Review

**Spec coverage:**
- §1 regime.sh (4 signals, weights, bands, graceful UNKNOWN) → Task 1.
- §2 wire into run.sh (compute + datablock inject) → Task 2 Steps 1–2.
- §3 PM prior → Task 3 Step 1.
- §4 BEAR size filter (shrink not drop) → Task 3 Steps 2–3 + test Step 5.
- §5 report + notify → Task 2 Steps 3–4.
- Testing (bands, greed cap, hot funding, sparse→UNKNOWN, BEAR halving) → Task 1 Step 1 + Task 3 Step 5.
- Rollback (REGIME_DISABLE) → Task 2 Step 1 + Task 4 Step 2.

**Placeholder scan:** none. Task 3 Step 3 carries an explicit READ-first conditional (daily-pick POST body shape) with both branches specified — short-term trades (Step 2) are the primary, fully-specified exposure.

**Type/name consistency:** `regime.sh`, env `REGIME_DISABLE`/`REGIME_W_*`/`REGIME_BEAR_MAX`/`REGIME_BULL_MIN`, vars `REGIME_JSON`/`REGIME_BAND`/`REGIME_SCORE`, file `$D/regime.json`, datablock label `regime`, fields `score`/`band`/`signals{momentum,funding,volatility,sentiment}`, flag `regimeHalved`, bands BEAR/NEUTRAL/BULL/UNKNOWN — identical across regime.sh, run.sh, the PM prompt, and the tests. The BEAR-halving jq in Task 3 Step 2 is byte-identical to the one pinned by the Task 3 Step 5 test.
