import json

m = json.load(open('/home/runner/work/aeon/aeon/.token-pick-tmp/cg-markets.json'))
btc = next(c for c in m if c['symbol']=='btc')
eth = next(c for c in m if c['symbol']=='eth')
btc7 = btc.get('price_change_percentage_7d_in_currency') or 0
eth7 = eth.get('price_change_percentage_7d_in_currency') or 0
btc24 = btc.get('price_change_percentage_24h_in_currency') or 0
eth24 = eth.get('price_change_percentage_24h_in_currency') or 0
print(f"BTC 24h={btc24:.2f}% 7d={btc7:.2f}%")
print(f"ETH 24h={eth24:.2f}% 7d={eth7:.2f}%")
print()

t = json.load(open('/home/runner/work/aeon/aeon/.token-pick-tmp/cg-trending.json'))
trending_syms = set()
print('=== Trending coins (top 15) ===')
for c in t.get('coins', [])[:15]:
    item = c.get('item', {})
    data = item.get('data', {}) or {}
    cap = data.get('market_cap', 'n/a')
    chg = (data.get('price_change_percentage_24h', {}) or {}).get('usd')
    sym = (item.get('symbol') or '').upper()
    trending_syms.add(sym)
    chg_s = f"{chg:.1f}%" if isinstance(chg,(int,float)) else "n/a"
    print(f"  #{item.get('market_cap_rank')} {sym} ({item.get('name')[:30]}) mcap={cap} 24h={chg_s}")

print()
print('=== Top scoring candidates (dedup: XLM, LIT excluded) ===')
already_picked = {'XLM','LIT'}

def score(c):
    s = 0
    breakdown = []
    c24 = c.get('price_change_percentage_24h_in_currency') or 0
    c7 = c.get('price_change_percentage_7d_in_currency') or 0
    sym = c['symbol'].upper()
    if c24 > 0:
        s += 1; breakdown.append('24h+1')
    if c7 > 0:
        s += 1; breakdown.append('7d+1')
    if c24 > 5 and c7 > 5:
        s += 2; breakdown.append('both>5%+2')
    if sym in trending_syms:
        s += 2; breakdown.append('trending+2')
    vol = c.get('total_volume') or 0
    mcap = c.get('market_cap') or 1
    vmc = vol/mcap if mcap else 0
    if vmc >= 0.20:
        s += 3; breakdown.append(f'vmc{vmc:.2f}+3')
    elif vmc >= 0.10:
        s += 2; breakdown.append(f'vmc{vmc:.2f}+2')
    if c7 > btc7 and c7 > eth7:
        s += 2; breakdown.append('RS_BTC_ETH+2')
    return s, breakdown, vmc

ranked = []
for c in m:
    if (c.get('market_cap') or 0) < 20_000_000:
        continue
    sym = c['symbol'].upper()
    if sym in already_picked:
        continue
    s, br, vmc = score(c)
    ranked.append((s, c, br, vmc))

ranked.sort(key=lambda x: -x[0])
for s, c, br, vmc in ranked[:15]:
    sym = c['symbol'].upper()
    px = c.get('current_price') or 0
    c24 = c.get('price_change_percentage_24h_in_currency') or 0
    c7 = c.get('price_change_percentage_7d_in_currency') or 0
    mcap = (c.get('market_cap') or 0)/1e9
    print(f"  {sym:8s} score={s:2d} px=${px:.4f} 24h={c24:+6.1f}% 7d={c7:+6.1f}% mcap=${mcap:.2f}B vmc={vmc:.2f} {br}")

print()
# also show today's XLM for reference
xlm = next((c for c in m if c['symbol']=='xlm'), None)
if xlm:
    s, br, vmc = score(xlm)
    px = xlm.get('current_price') or 0
    c24 = xlm.get('price_change_percentage_24h_in_currency') or 0
    c7 = xlm.get('price_change_percentage_7d_in_currency') or 0
    mcap = (xlm.get('market_cap') or 0)/1e9
    print(f"=== Reference: today's pick XLM === score={s} px=${px:.4f} 24h={c24:+.1f}% 7d={c7:+.1f}% mcap=${mcap:.2f}B vmc={vmc:.2f} {br}")
