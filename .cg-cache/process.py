#!/usr/bin/env python3
import json

with open('.cg-cache/markets.json') as f:
    markets = json.load(f)
with open('.cg-cache/trending.json') as f:
    trending = json.load(f)

STABLE_IDS = {'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg','usds','ethena-usde','frax','usdt0','susds','ondo-us-dollar-yield','blackrock-usd-institutional-digital-liquidity-fund','sky-dollar','resolv-usr','falcon-usd','m0-foundation','tether-eurt','usdx-money-usdx','tether-gold','staked-frax'}
WRAPPED_IDS = {'wrapped-bitcoin','wrapped-steth','staked-ether','weth','wbeth','wrapped-eeth','rocket-pool-eth','coinbase-wrapped-btc','lombard-staked-btc','jito-staked-sol','binance-staked-sol','marinade-staked-sol','liquid-staked-ether','solv-protocol-solvbtc','renzo-restaked-eth','kelp-dao-restaked-eth','mantle-staked-ether','mantle-restaked-eth','tbtc','m-by-m0','susds','sky-dollar','ondo-us-dollar-yield','staked-frax-ether','rocket-pool','stader-ethx','frax-ether'}

def is_stable(c):
    if c['id'] in STABLE_IDS: return True
    sym = (c.get('symbol') or '').upper()
    name = (c.get('name') or '').lower()
    if sym.startswith('USD') or sym.startswith('EUR') or sym.startswith('GBP'): return True
    if 'stablecoin' in name or 'stable coin' in name: return True
    # peg-near-1 detector
    p = c.get('current_price') or 0
    if 0.97 <= p <= 1.03 and abs(c.get('price_change_percentage_24h') or 0) < 0.5 and c.get('market_cap_rank') and c['market_cap_rank'] <= 200:
        return True
    return False

filtered = []
for c in markets:
    if is_stable(c): continue
    if c['id'] in WRAPPED_IDS: continue
    vol = c.get('total_volume') or 0
    if vol < 1_000_000: continue
    if c.get('price_change_percentage_24h') is None: continue
    filtered.append(c)

# Tags
def tags_for(c, in_trending, list_name):
    tags = []
    p24 = c.get('price_change_percentage_24h') or 0
    p7d = c.get('price_change_percentage_7d_in_currency') or 0
    rank = c.get('market_cap_rank') or 9999
    mcap = c.get('market_cap') or 0
    vol = c.get('total_volume') or 0
    vol_mcap = vol/mcap if mcap > 0 else 0

    if in_trending and list_name == 'win':
        tags.append('TRENDING+UP')
    if in_trending and list_name == 'lose':
        tags.append('TRENDING+DOWN')
    if p24 > 15 and p7d > 25:
        tags.append('BREAKOUT')
    if p24 > 20 and p7d < 0:
        tags.append('FADE')
    if p24 < -10 and vol_mcap > 0.25:
        tags.append('CAPITULATION')
    if rank > 150 and p24 > 30:
        tags.append('PUMP-RISK')
    if mcap < 50_000_000:
        tags.append('MICROCAP')
    if rank <= 20:
        tags.append('MAJOR')
    return tags[:2]

trending_ids = set()
trending_syms = set()
for t in trending.get('coins', []):
    item = t.get('item', {})
    trending_ids.add(item.get('id'))
    trending_syms.add((item.get('symbol') or '').lower())

# Sort
winners = sorted(filtered, key=lambda c: c.get('price_change_percentage_24h') or 0, reverse=True)[:10]
losers = sorted(filtered, key=lambda c: c.get('price_change_percentage_24h') or 0)[:10]

# Trending
trending_items = []
for t in trending.get('coins', [])[:7]:
    item = t.get('item', {})
    data = item.get('data', {})
    trending_items.append({
        'name': item.get('name'),
        'symbol': (item.get('symbol') or '').upper(),
        'id': item.get('id'),
        'rank': item.get('market_cap_rank'),
        'price': data.get('price'),
        'change_24h': (data.get('price_change_percentage_24h') or {}).get('usd'),
    })

# Market pulse
top100 = filtered[:100]
green = sum(1 for c in top100 if (c.get('price_change_percentage_24h') or 0) > 0)
top50_changes = sorted([c.get('price_change_percentage_24h') or 0 for c in filtered[:50]])
median_top50 = top50_changes[len(top50_changes)//2] if top50_changes else 0
print(f"PULSE: {green}/100 top-100 green, median_top50={median_top50:.2f}")

def fmt_price(p):
    if p is None: return "?"
    if p >= 1000: return f"${p:,.0f}"
    if p >= 1: return f"${p:.2f}"
    if p >= 0.01: return f"${p:.4f}"
    if p >= 0.0001: return f"${p:.6f}"
    return f"${p:.8f}"

def fmt_abbr(v):
    if v is None: return "?"
    if v >= 1e9: return f"${v/1e9:.1f}B"
    if v >= 1e6: return f"${v/1e6:.0f}M"
    if v >= 1e3: return f"${v/1e3:.0f}K"
    return f"${v:.0f}"

def render(c, list_name):
    in_trending = c['id'] in trending_ids or c['symbol'].lower() in trending_syms
    tg = tags_for(c, in_trending, list_name)
    p24 = c.get('price_change_percentage_24h') or 0
    p7d = c.get('price_change_percentage_7d_in_currency') or 0
    p1h = c.get('price_change_percentage_1h_in_currency') or 0
    return {
        'symbol': c['symbol'].upper(),
        'name': c['name'],
        'price': fmt_price(c.get('current_price')),
        'p24': p24,
        'p7d': p7d,
        'p1h': p1h,
        'vol': fmt_abbr(c.get('total_volume')),
        'rank': c.get('market_cap_rank'),
        'tags': tg,
    }

print("\n=== WINNERS ===")
winners_r = [render(c, 'win') for c in winners]
for w in winners_r:
    tg = f" [{'/'.join(w['tags'])}]" if w['tags'] else ""
    print(f"  {w['symbol']} ({w['name']}) — {w['price']}  +{w['p24']:.1f}% / 7d {w['p7d']:+.1f}% / 1h {w['p1h']:+.1f}%  •  {w['vol']} / #{w['rank']}{tg}")

print("\n=== LOSERS ===")
losers_r = [render(c, 'lose') for c in losers]
for l in losers_r:
    tg = f" [{'/'.join(l['tags'])}]" if l['tags'] else ""
    print(f"  {l['symbol']} ({l['name']}) — {l['price']}  {l['p24']:.1f}% / 7d {l['p7d']:+.1f}% / 1h {l['p1h']:+.1f}%  •  {l['vol']} / #{l['rank']}{tg}")

print("\n=== TRENDING ===")
for t in trending_items:
    sym = t['symbol']
    name = t['name']
    rank = t['rank']
    price = fmt_price(t['price'])
    ch = t['change_24h']
    ch_str = f"{ch:+.1f}%" if ch is not None else "?"
    # tags for trending: check if it's also in winners/losers
    in_winners = any(w['symbol'] == sym for w in winners_r)
    in_losers = any(l['symbol'] == sym for l in losers_r)
    extras = []
    if in_winners: extras.append('TRENDING+UP')
    if in_losers: extras.append('TRENDING+DOWN')
    tg = f" [{'/'.join(extras)}]" if extras else ""
    print(f"  {sym} ({name}) — #{rank}, {price}, 24h {ch_str}{tg}")

# Save results for shell use
out = {
    'pulse': {'green100': green, 'median_top50': median_top50},
    'winners': winners_r,
    'losers': losers_r,
    'trending': [{'symbol': t['symbol'], 'name': t['name'], 'rank': t['rank'], 'price': fmt_price(t['price']), 'change_24h': t['change_24h']} for t in trending_items],
}
with open('.cg-cache/results.json', 'w') as f:
    json.dump(out, f, indent=2, default=str)
print("\nSaved .cg-cache/results.json")
