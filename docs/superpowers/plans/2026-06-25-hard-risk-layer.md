# Hard Risk Layer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the flat conviction-split short-term sizing with a deterministic risk layer — drawdown de-gross + volatility targeting + per-position cap + per-direction (correlation) cap — so the advisor can't oversize a volatile pick or stack big correlated longs.

**Architecture:** New `scripts/advisor/risk-size.sh` (bash wrapper + embedded python) takes the trades array + net worth + drawdown% + cg-markets vol proxies and returns sized trades. It replaces the inline sizing jq at `run.sh:487-493` and runs BEFORE the existing regime BEAR halving (defense-in-depth stack). Drawdown comes from `/api/history` (reusing notify-drawdown's jq). No new APIs.

**Tech Stack:** Bash + python3 (sizing math), jq, GitHub Actions. Offline tests in `scripts/advisor/selftest.sh`.

**Branch:** `.worktrees/risklayer` off `main`. Issue #140.

**Verified shapes (origin/main):**
- `cg-markets.json` = array; each `{id, symbol, price_change_percentage_24h, price_change_percentage_7d_in_currency, …}` (top-100 by mcap). Picks carry `coingeckoId` → match on `.id`.
- Trades array: `{trades:[{symbol, coingeckoId, side, conviction, entry, target, invalidate, …}]}`; sizing sets `sizeUsd`/`sizePctNet`.
- `/api/history` = `[{date, totalUsd}]`; current drawdown = `(runningPeak − current)/peak × 100` (notify-drawdown.sh:29-36).
- Inline sizing to replace: `run.sh:484-493`; regime BEAR halving immediately follows at `run.sh:494-500` (must stay AFTER risk-size).

---

## File Structure

- **Create** `scripts/advisor/risk-size.sh` — the 4-stage sizer (DD de-gross → vol-target → per-position cap → per-direction cap). Pure; reads trades on stdin, env for net/dd/cg-markets path; emits sized trades. The only real logic; unit-tested.
- **Modify** `scripts/advisor/run.sh` — add `/api/history` drawdown fetch; replace the inline sizing jq with a `risk-size.sh` call (kept BEFORE the BEAR halving); add `risk` to report + Telegram.
- **Modify** `scripts/advisor/selftest.sh` — offline assertions for the 4 stages + degrade.

---

## Task 1: `scripts/advisor/risk-size.sh` + tests

**Files:**
- Create: `scripts/advisor/risk-size.sh`
- Test: `scripts/advisor/selftest.sh` (append before the final pass/fail line)

- [ ] **Step 1: Write the failing tests**

Append to `scripts/advisor/selftest.sh` before the final `[ "$FAIL" -eq 0 ] && echo "selftest: ALL PASS" ...` line:

```bash
# --- risk-size.sh: vol-target + caps + DD de-gross ---
RSZ="$(cd "$(dirname "$0")" && pwd)/risk-size.sh"
RS_DIR="$(mktemp -d)"
# cg-markets with two coins: CALM (24h 5%, 7d 5%) and WILD (24h 40%, 7d 40%)
cat > "$RS_DIR/cg-markets.json" <<'EOF'
[{"id":"calm","symbol":"calm","price_change_percentage_24h":5,"price_change_percentage_7d_in_currency":5},
 {"id":"wild","symbol":"wild","price_change_percentage_24h":40,"price_change_percentage_7d_in_currency":40}]
EOF
rsz() { # trades-json ; RISK_NET ; RISK_DD  -> sized trades json
  printf '%s' "$1" | RISK_NET="$2" RISK_DD="${3:-0}" RISK_MKT="$RS_DIR/cg-markets.json" bash "$RSZ"
}
# Vol-target: equal MEDIUM longs, calm gets MORE than wild.
T2='{"trades":[{"symbol":"CALM","coingeckoId":"calm","side":"long","conviction":"MEDIUM"},{"symbol":"WILD","coingeckoId":"wild","side":"long","conviction":"MEDIUM"}]}'
O2="$(rsz "$T2" 400000 0)"
check "vol-target calm > wild" "$(printf '%s' "$O2" | jq -r '(.trades[]|select(.symbol=="CALM").sizeUsd) > (.trades[]|select(.symbol=="WILD").sizeUsd)')" "true"
# Per-position cap: one HIGH calm long at net 400000, cap 1.5% = 6000; budget 5%=20000 would give it ~20000 → clamped to 6000.
T1='{"trades":[{"symbol":"CALM","coingeckoId":"calm","side":"long","conviction":"HIGH"}]}'
O1="$(rsz "$T1" 400000 0)"
check "per-position cap 1.5pct" "$(printf '%s' "$O1" | jq -r '.trades[0].sizeUsd <= 6000')" "true"
# Direction cap: 5 calm HIGH longs, sum capped to 3% net = 12000.
T5='{"trades":[{"symbol":"A","coingeckoId":"calm","side":"long","conviction":"HIGH"},{"symbol":"B","coingeckoId":"calm","side":"long","conviction":"HIGH"},{"symbol":"C","coingeckoId":"calm","side":"long","conviction":"HIGH"},{"symbol":"D","coingeckoId":"calm","side":"long","conviction":"HIGH"},{"symbol":"E","coingeckoId":"calm","side":"long","conviction":"HIGH"}]}'
O5="$(rsz "$T5" 400000 0)"
check "direction cap long sum <=3pct" "$(printf '%s' "$O5" | jq -r '([.trades[]|select(.side=="long").sizeUsd]|add) <= 12000')" "true"
# DD de-gross: same single pick, DD 18 halves budget vs DD 5 → smaller (or equal-capped) size; use a small net so the cap doesn't mask it.
ODD0="$(rsz "$T1" 40000 5)"; ODD1="$(rsz "$T1" 40000 18)"
check "DD18 degrosses vs DD5" "$(printf '%s' "$ODD1" | jq -r --argjson a "$(printf '%s' "$ODD0" | jq '.trades[0].sizeUsd')" '.trades[0].sizeUsd < $a')" "true"
# Degrade: RISK_DISABLE=1 → plain conviction split (HIGH alone over budget 20000 → 20000, NO caps).
ODIS="$(printf '%s' "$T1" | RISK_DISABLE=1 RISK_NET=400000 RISK_MKT="$RS_DIR/cg-markets.json" bash "$RSZ")"
check "RISK_DISABLE conviction-split uncapped" "$(printf '%s' "$ODIS" | jq -r '.trades[0].sizeUsd')" "20000"
# sizePctNet consistency after caps.
check "sizePctNet matches sizeUsd" "$(printf '%s' "$O1" | jq -r '.trades[0].sizePctNet == ((.trades[0].sizeUsd/400000*1000)|round)/10')" "true"
```

(Note the DD test uses net=40000 so the budget — not the 1.5% per-position cap — is the binding constraint, making the de-gross observable.)

- [ ] **Step 2: Run tests to verify they fail**

Run: `bash scripts/advisor/selftest.sh`
Expected: FAIL — `risk-size.sh` missing, `bash "$RSZ"` errors. Final `selftest: FAILURES`.

- [ ] **Step 3: Create `scripts/advisor/risk-size.sh`**

```bash
#!/usr/bin/env bash
# scripts/advisor/risk-size.sh — deterministic short-term position sizing (issue #140).
# stdin: {"trades":[{symbol,coingeckoId,side,conviction,...}]}; stdout: same with
# sizeUsd/sizePctNet set + riskNote. Stages: DD de-gross → vol-target → per-position
# cap → per-direction cap. Env: RISK_NET (net worth), RISK_DD (current drawdown %),
# RISK_MKT (cg-markets.json path). RISK_DISABLE=1 → plain conviction-split (no caps).
# Pure: no network. Never crashes (bad input → conviction-split / echo fallback). No `set -x`.
set -uo pipefail
TRADES_IN="$(cat)"
RISK_NET="${RISK_NET:-0}" RISK_DD="${RISK_DD:-0}" RISK_MKT="${RISK_MKT:-}" \
RISK_DISABLE="${RISK_DISABLE:-0}" ST_RISK_PCT="${ST_RISK_PCT:-5}" \
RISK_DD_TRIGGER="${RISK_DD_TRIGGER:-15}" RISK_DD_TRIGGER2="${RISK_DD_TRIGGER2:-25}" \
RISK_DD_DEGROSS="${RISK_DD_DEGROSS:-0.5}" RISK_DD_DEGROSS2="${RISK_DD_DEGROSS2:-0.25}" \
RISK_MAX_POS_PCT="${RISK_MAX_POS_PCT:-1.5}" RISK_MAX_DIR_PCT="${RISK_MAX_DIR_PCT:-3.0}" \
RISK_VOL_FLOOR="${RISK_VOL_FLOOR:-3}" RISK_DEFAULT_VOL="${RISK_DEFAULT_VOL:-12}" \
TRADES_IN="$TRADES_IN" python3 <<'PY'
import os, json, math, sys
def f(k,d=0.0):
    try: return float(os.environ.get(k,"") or d)
    except: return d
def conv_mult(c): return 2.0 if str(c or "").upper().startswith("HIGH") else 1.0
try:
    data=json.loads(os.environ.get("TRADES_IN") or '{"trades":[]}')
    trades=data.get("trades") or []
    net=f("RISK_NET"); dd=f("RISK_DD"); st_pct=f("ST_RISK_PCT",5)
    disable=os.environ.get("RISK_DISABLE","0")=="1"
    budget=net*st_pct/100.0
    def conviction_split(tr, bud):
        wsum=sum(conv_mult(t.get("conviction")) for t in tr) or 0
        for t in tr:
            w=conv_mult(t.get("conviction"))
            t["sizeUsd"]=math.floor(bud*w/wsum) if wsum>0 else 0
        return tr
    if disable or net<=0 or not trades:
        trades=conviction_split(trades, budget)
    else:
        # 1) DD de-gross
        if dd>=f("RISK_DD_TRIGGER2",25): budget*=f("RISK_DD_DEGROSS2",0.25)
        elif dd>=f("RISK_DD_TRIGGER",15): budget*=f("RISK_DD_DEGROSS",0.5)
        # vol proxies from cg-markets, keyed by coingecko id
        vol={}
        try:
            mkt=json.load(open(os.environ["RISK_MKT"]))
            for m in mkt:
                cid=m.get("id")
                if cid is None: continue
                c24=abs(float(m.get("price_change_percentage_24h") or 0))
                c7=abs(float(m.get("price_change_percentage_7d_in_currency") or 0))
                vol[cid]=0.5*c24 + 0.5*(c7/math.sqrt(7))
        except Exception: pass
        floor=f("RISK_VOL_FLOOR",3); dflt=f("RISK_DEFAULT_VOL",12)
        # 2) vol-target weights
        ws=[]
        for t in trades:
            v=vol.get(t.get("coingeckoId"), dflt)
            v=max(floor, v if v>0 else dflt)
            ws.append(conv_mult(t.get("conviction"))/v)
        wsum=sum(ws) or 0
        for t,w in zip(trades,ws):
            t["sizeUsd"]=math.floor(budget*w/wsum) if wsum>0 else 0
        # 3) per-position cap (drop excess, no redistribute)
        poscap=net*f("RISK_MAX_POS_PCT",1.5)/100.0
        for t in trades:
            if t["sizeUsd"]>poscap:
                t["sizeUsd"]=math.floor(poscap); t["riskNote"]="pos-capped"
        # 4) per-direction cap (scale each side down to the cap)
        dircap=net*f("RISK_MAX_DIR_PCT",3.0)/100.0
        for side in ("long","short"):
            s=sum(t["sizeUsd"] for t in trades if (t.get("side") or "long")==side)
            if s>dircap and s>0:
                k=dircap/s
                for t in trades:
                    if (t.get("side") or "long")==side:
                        t["sizeUsd"]=math.floor(t["sizeUsd"]*k)
                        t["riskNote"]=(t.get("riskNote","")+",dir-scaled").lstrip(",")
    # recompute sizePctNet from final sizeUsd
    for t in trades:
        t["sizePctNet"]=round((t["sizeUsd"]/net*1000))/10 if net>0 else 0
    print(json.dumps({"trades":trades}))
except Exception as e:
    print(f"risk-size.sh: failed, emitting input unsized: {e}", file=sys.stderr)
    print(os.environ.get("TRADES_IN") or '{"trades":[]}')
PY
```

- [ ] **Step 4: Make executable**

Run: `chmod +x scripts/advisor/risk-size.sh`
Expected: no output.

- [ ] **Step 5: Run tests to verify they pass**

Run: `bash scripts/advisor/selftest.sh`
Expected: the new `vol-target`/cap/DD/`RISK_DISABLE`/`sizePctNet` checks `ok`, final `selftest: ALL PASS`. If a cap/threshold assertion is off, the test numbers derive from the defaults (net 400000: budget 20000, pos-cap 6000, dir-cap 12000) — fix the SCRIPT math, not the test thresholds.

- [ ] **Step 6: Syntax check**

Run: `bash -n scripts/advisor/risk-size.sh && echo "risk-size.sh OK"`
Expected: `risk-size.sh OK`

- [ ] **Step 7: Commit**

```bash
git add scripts/advisor/risk-size.sh scripts/advisor/selftest.sh
git commit -m "feat(advisor): risk-size.sh — vol-target + caps + DD de-gross sizing (issue #140)"
```

---

## Task 2: Wire into `run.sh` (drawdown fetch + sizing swap + report/Telegram)

**Files:**
- Modify: `scripts/advisor/run.sh` (sizing block ~480-493; report merge; Telegram)

- [ ] **Step 1: Compute current drawdown from /api/history**

Just BEFORE the sizing block (`# Position sizing:` comment, ~line 480), add (match the file's top-level indentation):
```bash
# Current drawdown % from the all-time ledger peak (for risk-size DD de-gross).
# Reuse the notify-drawdown computation; 0 if history is too short/unavailable.
RISK_DD="$(curl -fsS --max-time 30 -H "Authorization: Basic ${AUTH}" "$BASE/api/history" 2>/dev/null \
  | jq -r '[.[] | select((.totalUsd // 0) > 0)] as $h
      | if ($h|length) < 2 then 0
        else (([$h[].totalUsd] | max) as $peak
              | if $peak > 0 then ($peak - $h[-1].totalUsd)/$peak*100 else 0 end) end' 2>/dev/null || echo 0)"
[ -z "$RISK_DD" ] && RISK_DD=0
echo "advisor: portfolio drawdown ${RISK_DD}%"
```

- [ ] **Step 2: Replace the inline sizing jq with risk-size.sh**

Find the sizing jq assignment (`run.sh:487-493`: `TRADES="$(printf '%s' "$TRADES" | jq -c --argjson budget "$ST_BUDGET" --argjson total "$ST_TOTAL" '...sizeUsd...sizePctNet...')"`). Replace that whole assignment with:
```bash
          # Risk layer (issue #140): DD de-gross + vol-target + per-position + per-direction
          # caps. Runs BEFORE the regime BEAR halving below (defense in depth — both shrink
          # longs in a downtrend). RISK_DISABLE=1 → plain conviction-split fallback.
          TRADES="$(printf '%s' "$TRADES" \
            | RISK_NET="$ST_TOTAL" RISK_DD="$RISK_DD" RISK_MKT="$D/cg-markets.json" ST_RISK_PCT="$ST_RISK_PCT" \
              bash "$ROOT/scripts/advisor/risk-size.sh")"
```
Keep the `ST_RISK_PCT=`/`ST_TOTAL=` lines above (ST_TOTAL → RISK_NET). The `ST_BUDGET=` line is now unused by sizing — remove it to avoid a dead var, OR leave with a `# (now computed inside risk-size.sh)` comment. LEAVE the regime BEAR halving `if [ "${REGIME_BAND:-UNKNOWN}" = "BEAR" ]` block immediately AFTER, unchanged.

- [ ] **Step 3: Add `risk` to the report + Telegram**

In the report-merge `jq -n` (the one already carrying `--argjson regime`), add `--arg dd "$RISK_DD" --arg stp "$ST_RISK_PCT"` and `| .risk = {ddPct: ($dd|tonumber? // 0), budgetPct: ($stp|tonumber? // 5)}` to the filter. In the Telegram summary jq, pass `--arg dd "$RISK_DD"` and add a line `"RISK: DD " + (($dd|tonumber? // 0)|floor|tostring) + "%\n"` near the REGIME line.

- [ ] **Step 4: Verify**

Run:
```bash
bash -n scripts/advisor/run.sh && echo "run.sh OK"
grep -n "risk-size.sh\|RISK_DD\|api/history\|\.risk = " scripts/advisor/run.sh
A=$(grep -n "risk-size.sh" scripts/advisor/run.sh | head -1 | cut -d: -f1); B=$(grep -n "bear-halve.jq" scripts/advisor/run.sh | head -1 | cut -d: -f1); echo "risk-size@$A before bear-halve@$B"; [ "$A" -lt "$B" ] && echo "ORDER OK"
bash scripts/advisor/selftest.sh 2>&1 | tail -1
```
Expected: `run.sh OK`; grep shows DD fetch + risk-size call + report merge; `risk-size@<A> before bear-halve@<B>` with `ORDER OK` (A<B); `selftest: ALL PASS`.

- [ ] **Step 5: Commit**

```bash
git add scripts/advisor/run.sh
git commit -m "feat(advisor): wire risk-size + drawdown into run.sh, before regime halving (issue #140)"
```

---

## Task 3: Full suite + final review

- [ ] **Step 1: Full offline suite**

Run: `bash scripts/advisor/selftest.sh`
Expected: all `ok`, final `selftest: ALL PASS`, exit 0.

- [ ] **Step 2: Confirm stack order + fallback**

Run:
```bash
A=$(grep -n "risk-size.sh" scripts/advisor/run.sh | head -1 | cut -d: -f1)
B=$(grep -n "bear-halve.jq" scripts/advisor/run.sh | head -1 | cut -d: -f1)
echo "risk-size@$A bear-halve@$B"; [ "$A" -lt "$B" ] && echo "ORDER OK"
grep -c "RISK_DISABLE" scripts/advisor/risk-size.sh
```
Expected: A<B (`ORDER OK`); RISK_DISABLE guard present (≥1).

- [ ] **Step 3: End-to-end sizing sanity (offline, missing cg-markets → default vol)**

Run:
```bash
printf '%s' '{"trades":[{"symbol":"BTC","coingeckoId":"bitcoin","side":"long","conviction":"HIGH"},{"symbol":"X","coingeckoId":"wild","side":"long","conviction":"MEDIUM"},{"symbol":"Y","coingeckoId":"calm","side":"short","conviction":"MEDIUM"}]}' \
  | RISK_NET=400000 RISK_DD=0 RISK_MKT=/tmp/nope.json bash scripts/advisor/risk-size.sh | jq '.trades[]|{symbol,side,sizeUsd,sizePctNet,riskNote}'
```
Expected: no crash with a missing cg-markets path (all use RISK_DEFAULT_VOL); every sizeUsd ≤ 6000 (1.5% of 400k); long sum ≤ 12000; short ≤ 12000.

- [ ] **Step 4 (operator, needs creds): dry-run the advisor**

```bash
gh workflow run investment-advisor.yml -R anajuliabit/aeon
# log shows "advisor: portfolio drawdown X%"; staged short-term trades carry capped sizeUsd;
# report.risk present; DD>=15 halves budget; regime BEAR further halves longs on top.
```

---

## Self-Review

**Spec coverage:**
- §1 DD de-gross → Task 1 Step 3 (stage 1) + Task 2 Step 1 (history fetch) + DD test.
- §1 vol-target → Task 1 Step 3 (stage 2) + vol-target test.
- §1 per-position cap (drop excess) → stage 3 + cap test.
- §1 per-direction cap (scale down) → stage 4 + direction test.
- §2 wire + order (risk-size before BEAR halving) → Task 2 Steps 1-2 + Task 2/3 ORDER assertion.
- §2 report + Telegram → Task 2 Step 3.
- §3 testing (vol/caps/DD/degrade/pctNet) → Task 1 Step 1; degrade fallback → RISK_DISABLE test.
- Rollback (RISK_DISABLE) → Task 1 Step 3 + Task 3 Step 2.

**Placeholder scan:** none — full python + bash + commands.

**Type/name consistency:** `risk-size.sh`, env `RISK_NET`/`RISK_DD`/`RISK_MKT`/`RISK_DISABLE`/`ST_RISK_PCT`/`RISK_*`, fields `sizeUsd`/`sizePctNet`/`riskNote`, match key `coingeckoId`→cg-markets `.id`, defaults (net 400000 → budget 20000 / pos-cap 6000 / dir-cap 12000) consistent across python, tests, and run.sh wiring. risk-size runs before `lib/bear-halve.jq` (Task 2 Step 4 + Task 3 Step 2 enforce A<B).
