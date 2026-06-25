#!/usr/bin/env bash
# scripts/advisor/regime.sh — deterministic BTC risk-on/off score (0-100) + band.
# Reads the prefetched cache ($D/cg-btc.json, hl-funding.json, fng.json); emits ONE
# JSON object: {score, band, signals:{momentum,funding,volatility,sentiment}, asOf}.
# Pure: no network, no LLM. Missing inputs are omitted and weights renormalize; with
# <2 signals -> band UNKNOWN / score null. A non-NEUTRAL band (BULL/BEAR) requires the
# momentum signal; without it band clamps to NEUTRAL. Never aborts the caller: on ANY
# error it still emits valid UNKNOWN JSON and exits 0. No `set -x`.
set -uo pipefail
D="${D:-$(cd "$(dirname "$0")/../.." && pwd)/.investiments-cache/advisor}"
now="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo "")"

W_MOM="${REGIME_W_MOMENTUM:-0.40}"; W_FUND="${REGIME_W_FUNDING:-0.25}"
W_VOL="${REGIME_W_VOLATILITY:-0.20}"; W_SENT="${REGIME_W_SENTIMENT:-0.15}"
BEAR_MAX="${REGIME_BEAR_MAX:-35}"; BULL_MIN="${REGIME_BULL_MIN:-60}"

CLOSES="$(jq -r '[.prices[]? | .[1]] | [range(0; length; 24) as $i | .[$i]] | @tsv' \
  "$D/cg-btc.json" 2>/dev/null | tr '\t' ' ' || true)"
FNG="$(jq -r '.data[0].value // empty' "$D/fng.json" 2>/dev/null || true)"
FUND="$(jq -r '[.[]? | select(.coin=="BTC") | .fundingHourly] | first // empty' \
  "$D/hl-funding.json" 2>/dev/null || true)"

CLOSES="$CLOSES" FNG="$FNG" FUND="$FUND" \
W_MOM="$W_MOM" W_FUND="$W_FUND" W_VOL="$W_VOL" W_SENT="$W_SENT" \
BEAR_MAX="$BEAR_MAX" BULL_MIN="$BULL_MIN" NOW="$now" python3 <<'PY'
import os, json, statistics, math
try:
    def fenv(k):
        v=os.environ.get(k,"").strip()
        try: return float(v)
        except: return None
    # jq can emit the literal `null` (or other junk) for missing closes; keep
    # only finite floats so a single bad token can't crash the parse.
    closes=[]
    for x in os.environ.get("CLOSES","").split():
        try:
            v=float(x)
            if v==v and v not in (float("inf"),float("-inf")): closes.append(v)
        except: pass
    fng=fenv("FNG"); fund=fenv("FUND")
    wm,wf,wv,ws=fenv("W_MOM"),fenv("W_FUND"),fenv("W_VOL"),fenv("W_SENT")
    bear_max,bull_min=fenv("BEAR_MAX"),fenv("BULL_MIN")
    sig={}
    if len(closes)>=8:
        last=closes[-1]; ma7=statistics.mean(closes[-7:]); ma30=statistics.mean(closes)
        above=(1 if last>ma7 else 0)+(1 if last>ma30 else 0)
        drift=max(-0.15,min(0.15,(last-ma30)/ma30)) if ma30 else 0
        sig["momentum"]=round(max(0,min(100, above*30 + 20 + (drift/0.15)*20)))
    if len(closes)>=15:
        # 13 daily log-returns over the trailing window; guard both operands so a
        # zero/negative close can't blow up math.log.
        rets=[math.log(closes[i]/closes[i-1]) for i in range(len(closes)-13,len(closes)) if closes[i-1]>0 and closes[i]>0]
        if rets:
            vol=statistics.pstdev(rets)*math.sqrt(365)
            sig["volatility"]=round(max(0,min(45,(1.2-vol)/(1.2-0.3)*100)))
    if fund is not None:
        sig["funding"]=round(max(0,min(100, 70 - (fund/0.0005)*50)))
    if fng is not None:
        s=fng
        if fng>80: s=80-(fng-80)*2.5
        if fng<20: s=20+(20-fng)*0.5
        sig["sentiment"]=round(max(0,min(100,s)))
    wmap={"momentum":wm,"funding":wf,"volatility":wv,"sentiment":ws}
    present={k:v for k,v in sig.items()}
    if len(present)<2:
        print(json.dumps({"score":None,"band":"UNKNOWN","signals":present,"asOf":os.environ.get("NOW","")}, allow_nan=False))
    else:
        wsum=sum(wmap[k] for k in present)
        score=round(sum(present[k]*wmap[k] for k in present)/wsum)
        band="BEAR" if score<=bear_max else ("BULL" if score>=bull_min else "NEUTRAL")
        # Momentum (weight 0.40) is the only true price signal. Without it the
        # remaining signals (funding baseline 70, sentiment) renormalize to a
        # risk-ON score — backwards for a risk gate. A non-NEUTRAL band requires
        # momentum present; otherwise clamp to NEUTRAL but still report the score.
        if band!="NEUTRAL" and "momentum" not in present:
            band="NEUTRAL"
        print(json.dumps({"score":score,"band":band,"signals":present,"asOf":os.environ.get("NOW","")}, allow_nan=False))
except Exception:
    print(json.dumps({"score":None,"band":"UNKNOWN","signals":{},"asOf":os.environ.get("NOW","")}))
PY
