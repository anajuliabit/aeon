import json
import statistics as st

with open('.cg-markets.json') as f:
    markets = json.load(f)

STABLE_IDS = {'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg',
              'binance-usd','frax','true-usd','susd','gusd','lusd','usdp','usdj','vai','ousd','rsv','musd',
              'usds','sky-dollar','usd1-wlf','usd1','paypal-usd','mim','crvusd','dola','origin-dollar',
              'reserve-rights-token','euro-coin','eurc','stasis-eurs','xsgd','xidr','ageur','seur',
              'tether-eurt','tether-gold','xaut','usdg','usdx','usdy','usds-token','usdtb','wlfi-usd1',
              'usds-savings-dao','sdai','ethena-usde','ethena-staked-usde','susds',
              'staked-frax','sfrax','sfrxeth','gho','prisma-mkusd','syrupusdc','blackrock-usd-institutional-digital-liquidity-fund',
              'ondo-us-dollar-yield','usual-usd','mountain-protocol-usdm','usd0','usd0pp','m-by-m0',
              'cash','first-digital-savings-account','usdcsy','sui-bridged-usdt-sui'}

WRAPPED_IDS = {'wrapped-bitcoin','wrapped-steth','staked-ether','weth','wrapped-eeth','wbeth',
               'binance-staked-eth','rocket-pool-eth','renbtc','hbtc','bitcoin-bep2','wrapped-solana',
               'msol','jito-staked-sol','staked-sol','liquid-staked-sol','blackrock-wbtc','tbtc',
               'liquid-staked-ethereum','wrapped-beacon-eth','wsteth','reth','bedrock-uniBTC',
               'wrapped-hype','staked-hype','lombard-staked-btc','solv-protocol-solvbtc',
               'solv-btc','solvbtc','ether-fi-staked-eth','ankreth','coinbase-wrapped-btc',
               'kelp-dao-restaked-eth','swell-restaked-eth','renzo-restaked-eth','bedrock-unibtc',
               'lido-staked-ether','wrapped-bnb','binance-bridged-usdt-bnb-smart-chain',
               'binance-bridged-usdc-bnb-smart-chain','wrapped-avax','wrapped-staked-ether',
               'wrapped-tao','wrapped-near','arbitrum-bridged-wbtc-arbitrum-one','wrapped-tron','wrapped-eth'}

def is_stable(c):
    if c.get('id','') in STABLE_IDS: return True
    sym = (c.get('symbol') or '').upper()
    name = (c.get('name') or '').lower()
    if sym.startswith('USD') or sym.startswith('EUR') or sym.startswith('GBP'): return True
    if 'stablecoin' in name or 'pegged' in name: return True
    if name.startswith('savings ') or name.startswith('staked usd'): return True
    return False

def is_wrapped(c):
    if c.get('id','') in WRAPPED_IDS: return True
    name = (c.get('name') or '').lower()
    sym = (c.get('symbol') or '').lower()
    if name.startswith('wrapped') or name.startswith('lido staked') or name.startswith('coinbase wrapped'): return True
    if sym in ('wbtc','weth','wsol','steth','wsteth','reth','msol','jitosol','wbeth','bnsol','tbtc','lbtc','solvbtc','unibtc','wsei','wsui','cbbtc','cbeth','wbnb','rseth','ezeth','weeth'): return True
    return False

VOL_FLOOR = 1_000_000
filtered = [c for c in markets if not is_stable(c) and not is_wrapped(c) and (c.get('total_volume') or 0) >= VOL_FLOOR
            and c.get('price_change_percentage_24h_in_currency') is not None]

with open('.cg-trending.json') as f:
    trend = json.load(f)
trending_coins = trend.get('coins', [])
trending_ids = set()
for tc in trending_coins:
    item = tc.get('item', {})
    if item.get('id'):
        trending_ids.add(item['id'])

def fmt_price(p):
    if p is None: return "?"
    if p < 0.01: return f"${p:.6f}"
    if p < 1: return f"${p:.4f}"
    if p < 100: return f"${p:.3g}"
    if p < 10000: return f"${p:,.2f}"
    return f"${p:,.0f}"

def fmt_big(v):
    if v is None or v == 0: return "?"
    if v >= 1e9: return f"${v/1e9:.2f}B"
    if v >= 1e6: return f"${v/1e6:.0f}M"
    if v >= 1e3: return f"${v/1e3:.0f}K"
    return f"${v:.0f}"

def tags(c):
    out=[]
    p24 = c.get('price_change_percentage_24h_in_currency') or 0
    p7 = c.get('price_change_percentage_7d_in_currency') or 0
    rank = c.get('market_cap_rank') or 9999
    mcap = c.get('market_cap') or 0
    vol = c.get('total_volume') or 0
    vmc = vol/mcap if mcap else 0
    is_trend = c.get('id') in trending_ids
    if is_trend and p24 >= 5: out.append('TRENDING+UP')
    if is_trend and p24 <= -5: out.append('TRENDING+DOWN')
    if p24 > 15 and p7 > 25: out.append('BREAKOUT')
    if p24 > 20 and p7 < 0: out.append('FADE')
    if p24 < -10 and vmc > 0.25: out.append('CAPITULATION')
    if rank > 150 and p24 > 30: out.append('PUMP-RISK')
    if mcap and mcap < 50_000_000: out.append('MICROCAP')
    if rank <= 20: out.append('MAJOR')
    return out[:2]

winners = sorted(filtered, key=lambda c: c.get('price_change_percentage_24h_in_currency') or 0, reverse=True)[:10]
losers = sorted(filtered, key=lambda c: c.get('price_change_percentage_24h_in_currency') or 0)[:10]

print(f"Total: {len(markets)} -> filtered: {len(filtered)}")
print(f"Trending IDs ({len(trending_ids)})")

print("\n=== WINNERS ===")
for i,c in enumerate(winners,1):
    p24 = c.get('price_change_percentage_24h_in_currency') or 0
    p7 = c.get('price_change_percentage_7d_in_currency') or 0
    p1 = c.get('price_change_percentage_1h_in_currency') or 0
    mcap = c.get('market_cap') or 0
    vol = c.get('total_volume') or 0
    vmc = vol/mcap if mcap else 0
    t = tags(c)
    print(f"{i}. {c['symbol'].upper()} ({c['name']}) #{c['market_cap_rank']} {fmt_price(c['current_price'])} 24h{p24:+.1f}% 7d{p7:+.1f}% 1h{p1:+.1f}% vol={fmt_big(vol)} mcap={fmt_big(mcap)} vmc={vmc:.2f} {t}")

print("\n=== LOSERS ===")
for i,c in enumerate(losers,1):
    p24 = c.get('price_change_percentage_24h_in_currency') or 0
    p7 = c.get('price_change_percentage_7d_in_currency') or 0
    p1 = c.get('price_change_percentage_1h_in_currency') or 0
    mcap = c.get('market_cap') or 0
    vol = c.get('total_volume') or 0
    vmc = vol/mcap if mcap else 0
    t = tags(c)
    print(f"{i}. {c['symbol'].upper()} ({c['name']}) #{c['market_cap_rank']} {fmt_price(c['current_price'])} 24h{p24:+.1f}% 7d{p7:+.1f}% 1h{p1:+.1f}% vol={fmt_big(vol)} mcap={fmt_big(mcap)} vmc={vmc:.2f} {t}")

print("\n=== TRENDING (top 7) ===")
trending_out = []
for i,tc in enumerate(trending_coins[:7],1):
    it = tc.get('item',{})
    d = it.get('data',{}) or {}
    pc_dict = d.get('price_change_percentage_24h') or {}
    pc = pc_dict.get('usd') if isinstance(pc_dict, dict) else None
    price = d.get('price')
    match = next((c for c in markets if c.get('id')==it.get('id')), None)
    if match:
        p24 = match.get('price_change_percentage_24h_in_currency') or 0
        t = tags(match)
        line = f"{i}. {it['name']} ({it['symbol']}) #{it.get('market_cap_rank','?')} {fmt_price(match['current_price'])} 24h{p24:+.1f}% {t}"
        trending_out.append({'name': it['name'], 'sym': it['symbol'], 'rank': it.get('market_cap_rank'),
                             'price': match['current_price'], 'p24': p24, 'tags': t})
    else:
        p24v = pc if pc is not None else 0
        line = f"{i}. {it['name']} ({it['symbol']}) #{it.get('market_cap_rank','?')} {fmt_price(price)} 24h{p24v:+.1f}% [outside-250]"
        trending_out.append({'name': it['name'], 'sym': it['symbol'], 'rank': it.get('market_cap_rank'),
                             'price': price, 'p24': p24v, 'tags': ['OUTSIDE-250']})
    print(line)

top100 = [c for c in filtered if (c.get('market_cap_rank') or 9999) <= 100]
top50 = [c for c in filtered if (c.get('market_cap_rank') or 9999) <= 50]
greens = sum(1 for c in top100 if (c.get('price_change_percentage_24h_in_currency') or 0) > 0)
m50 = st.median([c.get('price_change_percentage_24h_in_currency') or 0 for c in top50])
m100 = st.median([c.get('price_change_percentage_24h_in_currency') or 0 for c in top100])
print(f"\n=== PULSE ===")
print(f"top100: {greens}/{len(top100)} green, median top50: {m50:+.2f}%, median top100: {m100:+.2f}%")

top20 = [c for c in filtered if (c.get('market_cap_rank') or 9999) <= 20]
greens20 = sum(1 for c in top20 if (c.get('price_change_percentage_24h_in_currency') or 0) > 0)
m20 = st.median([c.get('price_change_percentage_24h_in_currency') or 0 for c in top20])
print(f"top20: {greens20}/{len(top20)} green, median: {m20:+.2f}%")

out = {
    'winners': [{'sym': c['symbol'].upper(), 'name': c['name'], 'id': c['id'],
                 'price': c['current_price'],
                 'p24': c.get('price_change_percentage_24h_in_currency'),
                 'p7': c.get('price_change_percentage_7d_in_currency'),
                 'p1': c.get('price_change_percentage_1h_in_currency'),
                 'vol': c.get('total_volume'), 'mcap': c.get('market_cap'),
                 'rank': c.get('market_cap_rank'),
                 'vmc': ((c.get('total_volume') or 0)/(c.get('market_cap') or 1)) if c.get('market_cap') else 0,
                 'tags': tags(c)}
                for c in winners],
    'losers': [{'sym': c['symbol'].upper(), 'name': c['name'], 'id': c['id'],
                'price': c['current_price'],
                'p24': c.get('price_change_percentage_24h_in_currency'),
                'p7': c.get('price_change_percentage_7d_in_currency'),
                'p1': c.get('price_change_percentage_1h_in_currency'),
                'vol': c.get('total_volume'), 'mcap': c.get('market_cap'),
                'rank': c.get('market_cap_rank'),
                'vmc': ((c.get('total_volume') or 0)/(c.get('market_cap') or 1)) if c.get('market_cap') else 0,
                'tags': tags(c)}
               for c in losers],
    'trending': trending_out,
    'pulse': {'greens100': greens, 'top100': len(top100),
              'greens20': greens20, 'top20': len(top20),
              'median50': m50, 'median100': m100, 'median20': m20},
    'filtered_count': len(filtered), 'total_count': len(markets),
}
with open('.cg-summary.json','w') as f:
    json.dump(out, f, indent=2)
print("\nSaved .cg-summary.json")
