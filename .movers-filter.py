#!/usr/bin/env python3
import json, statistics, sys

STABLE_IDS = {
    "tether","usd-coin","dai","first-digital-usd","usde","tusd","usdd","pyusd","fdusd","paxg",
    "ethena-usde","usds","susd","frax","lusd","gusd","usdp","usdb","crvusd","usd0","usdy",
    "ondo-us-dollar-yield","paypal-usd","binance-usd","usd0-liquid-bond","tether-gold",
    "ripple-usd","true-usd","gemini-dollar","dola-usd","xaut","staked-usde","mountain-protocol-usdm",
    "resolv-usr","world-liberty-financial-usd","falcon-finance-usdf","susds","savings-dai","sky-dollar"
}

def sym_is_stable(s):
    u = (s or "").upper()
    if u.startswith("USD") or u.startswith("EUR") or u.startswith("GBP"):
        return True
    if u in {"DAI","FDUSD","TUSD","USDE","PYUSD","FRAX","LUSD","CRVUSD","XAUT","PAXG","RLUSD","SUSDS","SDAI"}:
        return True
    return False

with open("/home/runner/work/aeon/aeon/.cg-markets.json") as f:
    data = json.load(f)

filt = []
for c in data:
    vol = c.get("total_volume") or 0
    if vol < 1_000_000:
        continue
    if c.get("id") in STABLE_IDS:
        continue
    if sym_is_stable(c.get("symbol","")):
        continue
    if "stablecoin" in (c.get("name","") or "").lower():
        continue
    if c.get("price_change_percentage_24h_in_currency") is None:
        continue
    filt.append(c)

def pack(c):
    return {
        "sym": (c.get("symbol") or "").upper(),
        "name": c.get("name"),
        "id": c.get("id"),
        "rank": c.get("market_cap_rank"),
        "price": c.get("current_price"),
        "pc1h": c.get("price_change_percentage_1h_in_currency"),
        "pc24h": c.get("price_change_percentage_24h_in_currency"),
        "pc7d": c.get("price_change_percentage_7d_in_currency"),
        "vol": c.get("total_volume"),
        "mcap": c.get("market_cap"),
    }

winners = sorted(filt, key=lambda c: -(c.get("price_change_percentage_24h_in_currency") or 0))[:12]
losers  = sorted(filt, key=lambda c:  (c.get("price_change_percentage_24h_in_currency") or 0))[:12]
top100 = filt[:100]
top50 = filt[:50]
pos = sum(1 for c in top100 if (c.get("price_change_percentage_24h_in_currency") or 0) > 0)
med50 = statistics.median([(c.get("price_change_percentage_24h_in_currency") or 0) for c in top50])

out = {
    "count": len(filt),
    "winners": [pack(c) for c in winners],
    "losers": [pack(c) for c in losers],
    "top100_positive": pos,
    "top100_total": len(top100),
    "top50_median": round(med50, 2),
}
json.dump(out, sys.stdout, indent=2)
