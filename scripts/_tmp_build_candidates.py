#!/usr/bin/env python3
"""Compute closed-trade counts and aggregate metrics per wallet."""
import json
import math
import glob
import os
import hashlib

DATANET = "9"
LEDGER_HASHES = {
    "8d47851b7762a319", "da7a36f4094a24f9", "3abb43986aea32fd",
    "397ee2e8e5e7e593", "9794ed8044e6e7ea", "7029a48db1b4e5db",
    "086b715f7a1de343", "0d4b168331d58f61", "e02fef4e76668a31",
    "a3ea5a0973858464", "06e7715d81cdedca", "956a3b01c98e6730",
    "dce17be300855e07",
}

results = []
for f in sorted(glob.glob(".hl-cache/user-fills-*.json")):
    addr = os.path.basename(f).replace("user-fills-", "").replace(".json", "")
    with open(f) as fh:
        data = json.load(fh)
    if isinstance(data, dict) and data.get("code") == "PREFETCH_FAILED":
        results.append({"addr": addr, "status": "ERROR"})
        continue
    if not isinstance(data, list) or len(data) == 0:
        results.append({"addr": addr, "status": "EMPTY", "n_fills": 0})
        continue
    dirs = set(x.get("dir") for x in data)
    has_perp = any(d and ("Open" in d or "Close" in d) for d in dirs)
    n_spot = sum(1 for x in data if x.get("dir") in ("Buy", "Sell", "Spot Dust Conversion") or (x.get("coin", "").startswith("@")))
    spot_pct = n_spot / len(data) if data else 0
    perp_fills = [x for x in data if x.get("dir") and ("Open" in x["dir"] or "Close" in x["dir"])]
    close_fills = [x for x in perp_fills if "Close" in x["dir"]]
    n_total = len(data)
    n_perp = len(perp_fills)
    n_close = len(close_fills)
    if n_close == 0:
        results.append({
            "addr": addr, "status": "NO_PERP_CLOSE" if not has_perp else "NO_CLOSE",
            "n_fills": n_total, "n_perp": n_perp, "spot_pct": round(spot_pct, 4)
        })
        continue
    pnls = [float(x.get("closedPnl", "0") or "0") for x in close_fills]
    sum_pnl = sum(pnls)
    wins = [p for p in pnls if p > 0]
    win_rate = len(wins) / len(pnls) if pnls else 0
    rets = []
    for x in close_fills:
        try:
            sz = float(x.get("sz", "0") or "0")
            px = float(x.get("px", "0") or "0")
            notional = sz * px
            pnl = float(x.get("closedPnl", "0") or "0")
            if notional > 0:
                rets.append(pnl / notional)
        except Exception:
            pass
    first_t = data[0]["time"]
    last_t = data[-1]["time"]
    span_ms = last_t - first_t
    days_covered = max(span_ms / 86400000, 1/86400)
    if rets:
        mean_r = sum(rets) / len(rets)
        var_r = sum((r - mean_r) ** 2 for r in rets) / len(rets)
        std_r = math.sqrt(var_r)
        annual_factor = math.sqrt(len(rets) * 365 / days_covered)
        sharpe = (mean_r / std_r * annual_factor) if std_r > 0 else 0
    else:
        sharpe = 0
    cum = 0
    peak = 0
    mdd = 0
    for p in pnls:
        cum += p
        if cum > peak:
            peak = cum
        dd = peak - cum
        if dd > mdd:
            mdd = dd
    mdd_pct = (mdd / peak * 100) if peak > 0 else (100.0 if sum_pnl < 0 else 0.0)
    canonical = f"trades:{DATANET}:{addr}:{first_t}:{last_t}:{n_close}"
    full_hash = hashlib.sha256(canonical.encode()).hexdigest()
    short_hash = full_hash[:16]
    dedup = short_hash in LEDGER_HASHES
    market_set = sorted(set(x.get("coin") for x in close_fills))
    results.append({
        "addr": addr,
        "status": ("DEDUP" if dedup else "SPOT_MIX" if spot_pct > 0.05 else "CAND"),
        "n_fills": n_total,
        "n_perp": n_perp,
        "n_close": n_close,
        "spot_pct": round(spot_pct, 4),
        "first_t": first_t,
        "last_t": last_t,
        "days_covered": round(days_covered, 4),
        "win_rate": round(win_rate, 4),
        "sum_pnl": round(sum_pnl, 2),
        "sharpe": round(sharpe, 2),
        "mdd_pct": round(mdd_pct, 2),
        "mdd_usd": round(mdd, 2),
        "canonical": canonical,
        "short_hash": short_hash,
        "full_hash": full_hash,
        "markets": market_set,
    })

def sort_key(r):
    status_order = {"CAND": 0, "SPOT_MIX": 1, "DEDUP": 2, "NO_CLOSE": 3,
                    "NO_PERP_CLOSE": 4, "EMPTY": 5, "ERROR": 6}
    return (status_order.get(r["status"], 99), -(r.get("sharpe") or 0))

for r in sorted(results, key=sort_key):
    if r["status"] in ("EMPTY", "ERROR"):
        print(f"{r['status']:14s} {r['addr']}")
    elif r["status"].startswith("NO_"):
        print(f"{r['status']:14s} {r['addr']} fills={r['n_fills']} perp={r.get('n_perp',0)} spot%={r.get('spot_pct',0)*100:.1f}")
    else:
        print(f"{r['status']:14s} {r['addr']} fills={r['n_fills']} close={r['n_close']} sharpe={r['sharpe']} pnl=${r['sum_pnl']:.2f} win={r['win_rate']*100:.1f}% mdd_pct={r['mdd_pct']:.2f}% spot%={r['spot_pct']*100:.1f} hash={r['short_hash']} days={r['days_covered']} mkts={','.join(r['markets'][:6])}")

with open(".tmp-candidates.json", "w") as fh:
    json.dump(results, fh, indent=2)
