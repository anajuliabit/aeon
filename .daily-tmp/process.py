#!/usr/bin/env python3
"""Process token-movers + papers + HN data and emit a unified summary."""
import json, sys, re
from datetime import datetime, timezone

# ------------- TOKEN MOVERS -------------
STABLES = {
    "tether","usd-coin","dai","first-digital-usd","usde","tusd","usdd","pyusd",
    "fdusd","paxg","gold-tether","staked-frax-ether","ondo-us-dollar-yield",
}
WRAPPED = {
    "wrapped-bitcoin","wrapped-eth","weth","wbtc","staked-ether",
    "wrapped-steth","wrapped-beacon-eth","lido-staked-ether","ethena-usde",
    "binance-staked-sol","jito-staked-sol","mantle-staked-ether",
    "rocket-pool-eth","msol","weeth","wrapped-eeth","coinbase-wrapped-staked-eth",
    "kelp-dao-restaked-eth","renzo-restaked-eth","binance-bridged-usdt-bnb-smart-chain",
    "bridged-wrapped-steth-base","wrapped-eth-mantle-bridge","mantle-staked-ether",
    "rocket-pool-eth","ether-fi-staked-eth",
}

def fmt_price(p):
    if p is None: return "n/a"
    if p >= 1000: return f"${p:,.0f}"
    if p >= 1: return f"${p:.3g}"
    if p >= 0.01: return f"${p:.4f}"
    return f"${p:.6f}"

def fmt_pct(p):
    if p is None: return "n/a"
    return f"{p:+.1f}%"

def fmt_abbr(n):
    if n is None: return "n/a"
    if n >= 1e9: return f"${n/1e9:.1f}B"
    if n >= 1e6: return f"${n/1e6:.0f}M"
    if n >= 1e3: return f"${n/1e3:.0f}K"
    return f"${n:.0f}"

with open(".daily-tmp/cg-markets.json") as f:
    markets = json.load(f)

filtered = []
for m in markets:
    sym = (m.get("symbol") or "").upper()
    cid = m.get("id","")
    vol = m.get("total_volume") or 0
    if vol < 1_000_000: continue
    if cid in STABLES or cid in WRAPPED: continue
    if sym.startswith(("USD","EUR","GBP")): continue
    if "stablecoin" in (m.get("name") or "").lower(): continue
    filtered.append(m)

# Sort by 24h change
def chg24(m): return m.get("price_change_percentage_24h") or 0
def chg7d(m): return m.get("price_change_percentage_7d_in_currency") or 0
def chg1h(m): return m.get("price_change_percentage_1h_in_currency") or 0

filtered_sorted_up = sorted(filtered, key=chg24, reverse=True)
filtered_sorted_dn = sorted(filtered, key=chg24)

winners = filtered_sorted_up[:10]
losers  = filtered_sorted_dn[:10]

# trending
with open(".daily-tmp/cg-trending.json") as f:
    trending = json.load(f)
trending_coins = trending.get("coins", [])[:7]

# Tags
def tags_for(m):
    tags = []
    sym = (m.get("symbol") or "").upper()
    rank = m.get("market_cap_rank") or 999
    mcap = m.get("market_cap") or 0
    c24 = chg24(m); c7 = chg7d(m); c1 = chg1h(m)
    trending_ids = {t.get("item",{}).get("id") for t in trending_coins}
    in_trending = m.get("id") in trending_ids
    if in_trending and c24 > 0: tags.append("TRENDING+UP")
    if in_trending and c24 < 0: tags.append("TRENDING+DOWN")
    if c24 > 15 and c7 > 25: tags.append("BREAKOUT")
    if c24 > 20 and c7 < 0: tags.append("FADE")
    if c24 < -10 and (m.get("total_volume") or 0) > 0 and mcap > 0 and m["total_volume"]/mcap > 0.25:
        tags.append("CAPITULATION")
    if rank > 150 and c24 > 30: tags.append("PUMP-RISK")
    if mcap and mcap < 50_000_000 and "PUMP-RISK" not in tags: tags.append("MICROCAP")
    if rank and rank <= 20: tags.append("MAJOR")
    return tags[:2]

# Market pulse
top100 = filtered[:100]
green_top100 = sum(1 for m in top100 if chg24(m) > 0)
top50_sorted = sorted([chg24(m) for m in filtered[:50]])
median_top50 = top50_sorted[len(top50_sorted)//2] if top50_sorted else 0

print(f"=== MARKET PULSE ===")
print(f"green_top100: {green_top100}/100 · median_top50_24h: {median_top50:+.1f}%")
print()

print("=== WINNERS ===")
for m in winners:
    sym = (m.get("symbol") or "").upper()
    name = m.get("name","")
    rank = m.get("market_cap_rank")
    price = fmt_price(m.get("current_price"))
    c24 = fmt_pct(chg24(m))
    c7  = fmt_pct(chg7d(m))
    c1h = fmt_pct(chg1h(m))
    vol = fmt_abbr(m.get("total_volume"))
    tags = "[" + "][".join(tags_for(m)) + "]" if tags_for(m) else ""
    print(f"{sym} ({name}) {price}  24h {c24} / 7d {c7} / 1h {c1h}  • {vol} / #{rank}  {tags}")

print()
print("=== LOSERS ===")
for m in losers:
    sym = (m.get("symbol") or "").upper()
    name = m.get("name","")
    rank = m.get("market_cap_rank")
    price = fmt_price(m.get("current_price"))
    c24 = fmt_pct(chg24(m))
    c7  = fmt_pct(chg7d(m))
    c1h = fmt_pct(chg1h(m))
    vol = fmt_abbr(m.get("total_volume"))
    tags = "[" + "][".join(tags_for(m)) + "]" if tags_for(m) else ""
    print(f"{sym} ({name}) {price}  24h {c24} / 7d {c7} / 1h {c1h}  • {vol} / #{rank}  {tags}")

print()
print("=== TRENDING ===")
for t in trending_coins:
    it = t.get("item",{})
    name = it.get("name","")
    sym = (it.get("symbol") or "").upper()
    rank = it.get("market_cap_rank")
    d = it.get("data") or {}
    price = d.get("price") or 0
    try:
        pct = d.get("price_change_percentage_24h",{}).get("usd")
    except: pct = None
    print(f"{name} ({sym}) — #{rank}  ${price}  24h {fmt_pct(pct)}")

# ------------- HF PAPERS -------------
print()
print("=== PAPERS ===")
with open(".daily-tmp/hf-daily.json") as f:
    papers = json.load(f)
ranked = sorted(papers, key=lambda p: -(p.get("paper",{}).get("upvotes") or 0))
for p in ranked[:6]:
    pp = p.get("paper",{})
    pid = pp.get("id")
    title = pp.get("title","")
    upv = pp.get("upvotes") or 0
    authors = ", ".join(a.get("name","") for a in (pp.get("authors") or [])[:3])
    summary = (pp.get("summary") or "")[:300].replace("\n"," ")
    print(f"id={pid} upv={upv} title={title}")
    print(f"  authors: {authors}")
    print(f"  summary: {summary}")

# ------------- HN STORIES -------------
print()
print("=== HN ===")
with open(".daily-tmp/hn-front.json") as f:
    front = json.load(f)
hits = front.get("hits", [])
def hn_score(h):
    pts = h.get("points") or 0
    nc  = h.get("num_comments") or 0
    return pts + 1.5 * nc

ranked_hn = sorted(hits, key=hn_score, reverse=True)
for h in ranked_hn[:15]:
    title = h.get("title","")
    url   = h.get("url","")
    pts   = h.get("points") or 0
    nc    = h.get("num_comments") or 0
    obj_id = h.get("objectID")
    print(f"id={obj_id} pts={pts} c={nc} | {title}")
    print(f"  url={url}")
