import json

with open('.tmp_markets.json') as f:
    raw = json.load(f)

if not isinstance(raw, list):
    print("ERROR markets not a list:", raw)
    raise SystemExit(1)

print("total coins:", len(raw))

STABLE_IDS = {'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd',
              'pyusd','fdusd','paxg','ethena-usde','binance-usd','frax','true-usd',
              'usdt0','susds','usds','blackrock-usd','ondo-us-dollar-yield'}

def is_stable(c):
    sym = (c.get('symbol') or '').upper()
    name = (c.get('name') or '').lower()
    cid = c.get('id') or ''
    if cid in STABLE_IDS:
        return True
    if sym.startswith('USD') or sym.startswith('EUR') or sym.startswith('GBP'):
        return True
    if 'stablecoin' in name or 'usd' in name and 'yield' in name:
        return True
    return False

def num(c, k):
    v = c.get(k)
    return v if isinstance(v, (int, float)) else None

filtered = []
for c in raw:
    if is_stable(c):
        continue
    vol = num(c, 'total_volume')
    if vol is None or vol < 1_000_000:
        continue
    ch24 = num(c, 'price_change_percentage_24h_in_currency')
    if ch24 is None:
        ch24 = num(c, 'price_change_percentage_24h')
    if ch24 is None:
        continue
    filtered.append(c)

print("after filter:", len(filtered))

def ch(c, period):
    return c.get(f'price_change_percentage_{period}_in_currency')

# drop wrapped dupes - keep one rep of BTC/ETH/staked variants if dominating
def is_wrapped(c):
    sym = (c.get('symbol') or '').lower()
    return sym in {'wbtc','weth','steth','wsteth','wbeth','cbbtc','lbtc','reth','weeth','rseth','meth','solvbtc','cbeth','susde','ezeth','jitosol','msol','bnsol','stbtc','tbtc','clbtc'}

filtered_nowrap = [c for c in filtered if not is_wrapped(c)]

s24 = sorted(filtered_nowrap, key=lambda c: ch(c,'24h') if ch(c,'24h') is not None else 0)
winners = list(reversed(s24[-10:]))
losers = s24[:10]

def fmt(c):
    return {
        'name': c.get('name'),
        'sym': (c.get('symbol') or '').upper(),
        'rank': c.get('market_cap_rank'),
        'price': c.get('current_price'),
        'ch1h': ch(c,'1h'),
        'ch24h': ch(c,'24h'),
        'ch7d': ch(c,'7d'),
        'vol': c.get('total_volume'),
        'mcap': c.get('market_cap'),
        'id': c.get('id'),
    }

out = {'winners': [fmt(c) for c in winners], 'losers':[fmt(c) for c in losers]}

# market pulse
top100 = sorted(filtered_nowrap, key=lambda c: c.get('market_cap_rank') or 9999)[:100]
green = sum(1 for c in top100 if (ch(c,'24h') or 0) > 0)
top50 = top100[:50]
med_vals = sorted([ch(c,'24h') for c in top50 if ch(c,'24h') is not None])
median = med_vals[len(med_vals)//2] if med_vals else 0
out['pulse'] = {'green': green, 'total': len(top100), 'median50': round(median,2)}

# trending
with open('.tmp_trending.json') as f:
    tr = json.load(f)
trend = []
for item in tr.get('coins', [])[:7]:
    ci = item.get('item', {})
    data = ci.get('data', {})
    trend.append({
        'name': ci.get('name'),
        'sym': (ci.get('symbol') or '').upper(),
        'rank': ci.get('market_cap_rank'),
        'price': data.get('price'),
        'ch24h': (data.get('price_change_percentage_24h') or {}).get('usd'),
        'id': ci.get('id'),
    })
out['trending'] = trend

with open('.tmp_movers_out.json','w') as f:
    json.dump(out, f, indent=2)
print("WROTE out")
print(json.dumps(out['pulse']))
print("WIN:", [(w['sym'], round(w['ch24h'],1)) for w in out['winners']])
print("LOSE:", [(l['sym'], round(l['ch24h'],1)) for l in out['losers']])
print("TREND:", [t['sym'] for t in out['trending']])
