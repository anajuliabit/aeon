import json

m = json.load(open('.tm-cache/cg-markets.json'))
t = json.load(open('.tm-cache/cg-trending.json'))

print("markets count:", len(m))
print("trending count:", len(t.get('coins', [])))

# --- Filter ---
STABLE_IDS = {'tether','usd-coin','dai','first-digital-usd','usde','ethena-usde','tusd','true-usd',
              'usdd','pyusd','paypal-usd','fdusd','paxos-standard','paxg','pax-gold','usds','sky-dollar',
              'binance-usd','frax','usdt0','blackrock-usd','ethena-staked-usde','usdtb','susds','susde',
              'ondo-us-dollar-yield','global-dollar','falcon-finance','resolv-usr','wrapped-eeth'}
WRAPPED_IDS = {'wrapped-bitcoin','weth','wrapped-steth','staked-ether','wrapped-beacon-eth',
               'coinbase-wrapped-btc','binance-bridged-usdt-bnb-smart-chain','wrapped-eeth',
               'rocket-pool-eth','mantle-staked-ether','renzo-restaked-eth','kelp-dao-restaked-eth',
               'lombard-staked-btc','solv-btc','jupiter-staked-sol','binance-staked-sol','msol',
               'jito-staked-sol','liquid-staked-ethereum','bridged-wrapped-steth-scroll'}

def is_stable(c):
    sym = (c.get('symbol') or '').upper()
    name = (c.get('name') or '').lower()
    cid = c.get('id') or ''
    if cid in STABLE_IDS: return True
    if 'stablecoin' in name or 'usd' in name and 'yield' in name: return True
    if sym.startswith('USD') or sym.startswith('EUR') or sym.startswith('GBP'): return True
    # near-peg detection: price ~1.0 with tiny moves
    p = c.get('current_price') or 0
    ch = c.get('price_change_percentage_24h')
    if 0.95 <= p <= 1.05 and ch is not None and abs(ch) < 0.5:
        return True
    return False

filtered = []
for c in m:
    if is_stable(c): continue
    if c.get('id') in WRAPPED_IDS: continue
    vol = c.get('total_volume') or 0
    if vol < 1_000_000: continue
    if c.get('price_change_percentage_24h') is None: continue
    filtered.append(c)

print("filtered survivors:", len(filtered))

# --- Market pulse ---
top100 = filtered[:100] if len(filtered) >= 100 else filtered
green = sum(1 for c in top100 if (c.get('price_change_percentage_24h') or 0) > 0)
top50 = filtered[:50]
import statistics
med50 = statistics.median([c.get('price_change_percentage_24h') or 0 for c in top50])
btc = next((c for c in m if c['id']=='bitcoin'), None)
eth = next((c for c in m if c['id']=='ethereum'), None)
sol = next((c for c in m if c['id']=='solana'), None)
def fmt_major(c):
    return f"{c['symbol'].upper()} ${c['current_price']:,.0f} {c.get('price_change_percentage_24h',0):+.1f}% / 7d {c.get('price_change_percentage_7d_in_currency') or 0:+.1f}%"
print(f"PULSE: {green}/{len(top100)} top-100 green, median top-50 24h {med50:+.2f}%")
print("BTC:", fmt_major(btc) if btc else "n/a")
print("ETH:", fmt_major(eth) if eth else "n/a")
print("SOL:", fmt_major(sol) if sol else "n/a")

# --- Sort winners/losers ---
by24 = sorted(filtered, key=lambda c: c.get('price_change_percentage_24h') or 0)
losers = by24[:10]
winners = list(reversed(by24[-10:]))

def cap_abbr(v):
    if v is None: return "n/a"
    if v >= 1e9: return f"${v/1e9:.1f}B"
    if v >= 1e6: return f"${v/1e6:.0f}M"
    return f"${v/1e3:.0f}K"

def price_fmt(p):
    if p is None: return "n/a"
    if p >= 1: return f"${p:,.4g}"
    if p >= 0.01: return f"${p:.4f}"
    return f"${p:.6f}"

# trending set
trending_syms = set()
trending = []
for item in t.get('coins', [])[:7]:
    d = item['item']
    sym = (d.get('symbol') or '').upper()
    trending_syms.add(sym)
    data = d.get('data') or {}
    ch = (data.get('price_change_percentage_24h') or {}).get('usd')
    trending.append({'name': d.get('name'), 'sym': sym, 'rank': d.get('market_cap_rank'),
                     'price': data.get('price'), 'ch24': ch})

def tags(c, is_winner=None):
    out = []
    sym = c['symbol'].upper()
    ch24 = c.get('price_change_percentage_24h') or 0
    ch7 = c.get('price_change_percentage_7d_in_currency') or 0
    rank = c.get('market_cap_rank') or 9999
    mcap = c.get('market_cap') or 0
    vol = c.get('total_volume') or 0
    volmcap = (vol/mcap) if mcap else 0
    in_trend = sym in trending_syms
    if in_trend and ch24 > 0 and is_winner: out.append('TRENDING+UP')
    if in_trend and ch24 < 0 and is_winner is False: out.append('TRENDING+DOWN')
    if ch24 > 15 and ch7 > 25: out.append('BREAKOUT')
    if ch24 > 20 and ch7 < 0: out.append('FADE')
    if ch24 < -10 and volmcap > 0.25: out.append('CAPITULATION')
    if rank > 150 and ch24 > 30: out.append('PUMP-RISK')
    if mcap and mcap < 50_000_000: out.append('MICROCAP')
    if rank <= 20: out.append('MAJOR')
    return out[:2]

def line(c, is_winner):
    sym = c['symbol'].upper()
    ch24 = c.get('price_change_percentage_24h') or 0
    ch7 = c.get('price_change_percentage_7d_in_currency') or 0
    ch1 = c.get('price_change_percentage_1h_in_currency') or 0
    return {
        'sym': sym, 'name': c['name'], 'rank': c.get('market_cap_rank'),
        'price': price_fmt(c.get('current_price')),
        'ch24': ch24, 'ch7': ch7, 'ch1': ch1,
        'vol': cap_abbr(c.get('total_volume')), 'mcap': cap_abbr(c.get('market_cap')),
        'tags': tags(c, is_winner)
    }

print("\n=== WINNERS ===")
for c in winners:
    l = line(c, True)
    print(f"{l['sym']} ({l['name']}) {l['price']} {l['ch24']:+.1f}% / 7d {l['ch7']:+.1f}% / 1h {l['ch1']:+.1f}% • {l['vol']} / #{l['rank']} {l['tags']}")

print("\n=== LOSERS ===")
for c in losers:
    l = line(c, False)
    print(f"{l['sym']} ({l['name']}) {l['price']} {l['ch24']:+.1f}% / 7d {l['ch7']:+.1f}% / 1h {l['ch1']:+.1f}% • {l['vol']} / #{l['rank']} {l['tags']}")

print("\n=== TRENDING ===")
for tr in trending:
    pr = price_fmt(tr['price'])
    ch = f"{tr['ch24']:+.1f}%" if tr['ch24'] is not None else "n/a"
    extra = ''
    if tr['sym'] in trending_syms: pass
    print(f"{tr['name']} ({tr['sym']}) #{tr['rank']} {pr} 24h {ch}")
