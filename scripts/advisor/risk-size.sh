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
RISK_VOL_CEIL="${RISK_VOL_CEIL:-150}" \
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
        degross=1.0
        if dd>=f("RISK_DD_TRIGGER2",25): degross=f("RISK_DD_DEGROSS2",0.25)
        elif dd>=f("RISK_DD_TRIGGER",15): degross=f("RISK_DD_DEGROSS",0.5)
        budget*=degross
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
        floor=f("RISK_VOL_FLOOR",3); dflt=f("RISK_DEFAULT_VOL",12); ceil=f("RISK_VOL_CEIL",150)
        ws=[]
        for t in trades:
            v=vol.get(t.get("coingeckoId"), dflt)
            v=min(ceil, max(floor, v if v>0 else dflt))
            ws.append(conv_mult(t.get("conviction"))/v)
        wsum=sum(ws) or 0
        for t,w in zip(trades,ws):
            t["sizeUsd"]=math.floor(budget*w/wsum) if wsum>0 else 0
        poscap=net*f("RISK_MAX_POS_PCT",1.5)/100.0
        for t in trades:
            if t["sizeUsd"]>poscap:
                t["sizeUsd"]=math.floor(poscap); t["riskNote"]="pos-capped"
        dircap=net*f("RISK_MAX_DIR_PCT",3.0)/100.0
        for side in ("long","short"):
            s=sum(t["sizeUsd"] for t in trades if (t.get("side") or "long")==side)
            if s>dircap and s>0:
                k=dircap/s
                for t in trades:
                    if (t.get("side") or "long")==side:
                        t["sizeUsd"]=math.floor(t["sizeUsd"]*k)
                        t["riskNote"]=(t.get("riskNote","")+",dir-scaled").lstrip(",")
    for t in trades:
        t["sizePctNet"]=round((t["sizeUsd"]/net*1000))/10 if net>0 else 0
    print(json.dumps({"trades":trades}))
except Exception as e:
    print(f"risk-size.sh: failed, emitting safe fallback: {e}", file=sys.stderr)
    raw=os.environ.get("TRADES_IN") or ""
    try:
        json.loads(raw); print(raw)          # valid JSON in → echo through
    except Exception:
        print('{"trades":[]}')                # garbage in → guaranteed-valid out
PY
