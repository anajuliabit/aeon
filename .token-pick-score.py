import json, os

base = '/home/runner/work/aeon/aeon'

with open(f'{base}/.token-pick-cg-markets.json') as f:
    mkts = json.load(f)

print(f"Total tokens: {len(mkts)}")

btc = next((m for m in mkts if m['symbol'].lower() == 'btc'), None)
eth = next((m for m in mkts if m['symbol'].lower() == 'eth'), None)
print(f"BTC: 24h={btc['price_change_percentage_24h_in_currency']:.2f}%, 7d={btc['price_change_percentage_7d_in_currency']:.2f}%, px=${btc['current_price']:,.0f}")
print(f"ETH: 24h={eth['price_change_percentage_24h_in_currency']:.2f}%, 7d={eth['price_change_percentage_7d_in_currency']:.2f}%, px=${eth['current_price']:,.0f}")

btc_7d = btc['price_change_percentage_7d_in_currency']
eth_7d = eth['price_change_percentage_7d_in_currency']

with open(f'{base}/.token-pick-cg-trending.json') as f:
    trending = json.load(f)
trend_ids = set(c['item']['id'] for c in trending.get('coins', []))
trend_syms_list = [c['item']['symbol'].upper() for c in trending.get('coins', [])]
print(f"Trending list ({len(trend_syms_list)}): {trend_syms_list}")

# Recent picks/dedup window (7 days)
DEDUP = {'WLD', 'SENT', 'MORPHO', 'MON', 'HUMAN', 'HOME', 'HYPE'}

results = []
for m in mkts:
    try:
        mcap = m.get('market_cap') or 0
        if mcap < 20_000_000:
            continue
        p24 = m.get('price_change_percentage_24h_in_currency') or 0
        p7 = m.get('price_change_percentage_7d_in_currency') or 0
        vol = m.get('total_volume') or 0
        vmc = vol / mcap if mcap else 0

        score = 0
        breakdown = []
        if p24 > 0:
            score += 1; breakdown.append('24h+1')
        if p7 > 0:
            score += 1; breakdown.append('7d+1')
        if p24 > 5 and p7 > 5:
            score += 2; breakdown.append('both>+5%+2')
        if m['id'] in trend_ids:
            score += 2; breakdown.append('trending+2')
        if vmc >= 0.20:
            score += 3; breakdown.append(f'vmc{vmc:.2f}+3')
        elif vmc >= 0.10:
            score += 2; breakdown.append(f'vmc{vmc:.2f}+2')
        if p7 > btc_7d and p7 > eth_7d:
            score += 2; breakdown.append(f'RS+2')

        sym = m['symbol'].upper()
        flag = ' (DEDUP)' if sym in DEDUP else ''
        results.append((score, sym, m['id'], m['current_price'], p24, p7, mcap, vol, vmc, '|'.join(breakdown), flag))
    except Exception as e:
        pass

results.sort(key=lambda x: -x[0])
print("\nTOP 40 BY SCORE (dedup-flagged):")
for r in results[:40]:
    print(f"  {r[0]}/9 {r[1]:10s}{r[10]:8s} px=${r[3]:.4g} 24h={r[4]:+.2f}% 7d={r[5]:+.2f}% mcap=${r[6]/1e9:.2f}B vol=${r[7]/1e6:.0f}M vmc={r[8]:.3f} (id={r[2]})")
print("\nFor the dedup-clean top 10 only:")
clean = [r for r in results if not r[10]]
for r in clean[:10]:
    print(f"  {r[0]}/9 {r[1]:10s} px=${r[3]:.4g} 24h={r[4]:+.2f}% 7d={r[5]:+.2f}% mcap=${r[6]/1e9:.2f}B vol=${r[7]/1e6:.0f}M vmc={r[8]:.3f} | {r[9]} (id={r[2]})")
