import json

base = '/home/runner/work/aeon/aeon/.token-pick-tmp'
with open(f'{base}/cg-trending.json') as f:
    trend = json.load(f)
with open(f'{base}/cg-markets.json') as f:
    markets = json.load(f)
with open(f'{base}/dex.json') as f:
    dex = json.load(f)

print("=== CG TRENDING (top 15) ===")
trending_syms = []
for i, c in enumerate(trend.get('coins', [])[:15]):
    item = c['item']
    trending_syms.append(item['symbol'].upper())
    print(f"  {i+1}. {item['symbol']:>10} ({item['name']:<28}) mcap_rank={item.get('market_cap_rank')}")

btc = next(c for c in markets if c['symbol'] == 'btc')
eth = next(c for c in markets if c['symbol'] == 'eth')
btc7 = btc.get('price_change_percentage_7d_in_currency') or 0
eth7 = eth.get('price_change_percentage_7d_in_currency') or 0
btc24 = btc.get('price_change_percentage_24h_in_currency') or 0
eth24 = eth.get('price_change_percentage_24h_in_currency') or 0
print(f"\n=== BENCHMARKS ===")
print(f"BTC: ${btc['current_price']:,.0f} 24h:{btc24:+.2f}% 7d:{btc7:+.2f}%")
print(f"ETH: ${eth['current_price']:,.2f} 24h:{eth24:+.2f}% 7d:{eth7:+.2f}%")

dex_syms = set()
for p in dex.get('pairs', [])[:80]:
    s = p.get('baseToken', {}).get('symbol', '')
    if s:
        dex_syms.add(s.upper())
print(f"\n=== DEX symbols ({len(dex_syms)}) ===")
print(sorted(dex_syms))

print(f"\n=== SCORING (top 250, mcap>=$20M, top 30 by signal score) ===")
candidates = []
for c in markets:
    sym = c['symbol'].upper()
    name = c['name']
    mcap = c.get('market_cap') or 0
    if mcap < 20_000_000:
        continue
    price = c.get('current_price') or 0
    vol = c.get('total_volume') or 0
    p24 = c.get('price_change_percentage_24h_in_currency') or 0
    p7 = c.get('price_change_percentage_7d_in_currency') or 0
    vmc = vol / mcap if mcap else 0

    score = 0
    breakdown = []
    if p24 > 0:
        score += 1; breakdown.append("24h+1")
    if p7 > 0:
        score += 1; breakdown.append("7d+1")
    if p24 > 5 and p7 > 5:
        score += 2; breakdown.append("both>5%+2")
    if sym in trending_syms:
        score += 2; breakdown.append("trending+2")
    if vmc >= 0.20:
        score += 3; breakdown.append("vmc>=0.20+3")
    elif vmc >= 0.10:
        score += 2; breakdown.append("vmc>=0.10+2")
    if p7 > btc7 and p7 > eth7:
        score += 2; breakdown.append("RS_BTC+ETH+2")
    if sym in dex_syms:
        score += 1; breakdown.append("dex+1")

    candidates.append({
        'sym': sym, 'name': name, 'price': price, 'mcap': mcap, 'vol': vol,
        'p24': p24, 'p7': p7, 'vmc': vmc, 'score': score, 'breakdown': breakdown,
        'id': c.get('id')
    })

candidates.sort(key=lambda x: x['score'], reverse=True)
for c in candidates[:30]:
    print(f"  {c['sym']:>10} score={c['score']:2d} | ${c['price']:.6g} 24h{c['p24']:+7.2f}% 7d{c['p7']:+8.2f}% | mcap=${c['mcap']/1e9:.3f}B vol=${c['vol']/1e6:.1f}M vmc={c['vmc']:.3f} | id={c['id']}")
    print(f"             {c['breakdown']}")
