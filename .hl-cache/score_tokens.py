#!/usr/bin/env python3
import json
import sys

OUT = open('.hl-cache/tp-scores.txt', 'w')
def p(*a, **k): print(*a, **k, file=OUT)

with open('.hl-cache/cg-markets-tp.json') as f:
    data = json.load(f)
with open('.hl-cache/cg-trending-tp.json') as f:
    trend = json.load(f)

trending_syms = set(c['item']['symbol'].upper() for c in trend.get('coins', []))

btc = next(c for c in data if c['symbol'] == 'btc')
eth = next(c for c in data if c['symbol'] == 'eth')
btc_24 = btc['price_change_percentage_24h_in_currency'] or 0
btc_7d = btc['price_change_percentage_7d_in_currency'] or 0
eth_24 = eth['price_change_percentage_24h_in_currency'] or 0
eth_7d = eth['price_change_percentage_7d_in_currency'] or 0

p(f"BENCH: BTC 24h {btc_24:+.2f}% 7d {btc_7d:+.2f}% ${btc['current_price']:,.0f}")
p(f"       ETH 24h {eth_24:+.2f}% 7d {eth_7d:+.2f}% ${eth['current_price']:,.0f}")
p(f"TRENDING CG: {sorted(trending_syms)[:25]}")
p('')

DEDUP = {'HUMAN', 'H', 'DEXE', 'WLD', 'SENT', 'MORPHO'}
EXCLUDE = {'USDT','USDC','DAI','USDE','FDUSD','BUSD','TUSD','USDS','PYUSD','WBTC',
           'WETH','WBETH','STETH','WSTETH','WEETH','CBETH','METH','SUSDE','SUSDS',
           'EZETH','RETH','WBT','BSC-USD','USD1','LBTC','SOLVBTC','USD0','USDX','BUIDL','BSCH'}

cands = []
for c in data:
    sym = c['symbol'].upper()
    mcap = c.get('market_cap') or 0
    vol = c.get('total_volume') or 0
    p24 = c.get('price_change_percentage_24h_in_currency') or 0
    p7 = c.get('price_change_percentage_7d_in_currency') or 0
    price = c.get('current_price') or 0
    if mcap < 20_000_000: continue
    if sym in DEDUP or sym in EXCLUDE: continue
    score = 0; b = []
    if p24 > 0: score += 1; b.append('24+')
    if p7 > 0: score += 1; b.append('7+')
    if p24 > 5 and p7 > 5: score += 2; b.append('both+5')
    if sym in trending_syms: score += 2; b.append('trend')
    vmc = vol / mcap if mcap else 0
    if vmc >= 0.20: score += 3; b.append(f'v/mc{vmc:.2f}+3')
    elif vmc >= 0.10: score += 2; b.append(f'v/mc{vmc:.2f}+2')
    if p7 > btc_7d and p7 > eth_7d: score += 2; b.append('RS')
    cands.append((score, vmc, sym, c.get('name',''), price, mcap, vol, vmc, p24, p7, b))

cands.sort(key=lambda x: (-x[0], -x[1]))
p(f"TOP 30 CANDIDATES (excl 7d-dedup {DEDUP}):")
p(f"{'sym':<10} {'name':<22} {'price':>10} {'24h%':>7} {'7d%':>7} {'mcap':>8} {'vol':>7} {'v/mc':>5} {'sc':>3}  notes")
for s, vmc, sym, name, price, mcap, vol, vmc2, p24, p7, b in cands[:30]:
    mb = mcap/1e9; vm = vol/1e6
    p(f"{sym:<10} {name[:22]:<22} ${price:>9.4g} {p24:>+6.2f}% {p7:>+6.2f}% ${mb:>6.2f}B ${vm:>5.0f}M {vmc2:>5.2f}  {s:>2}/10  {','.join(b)}")
