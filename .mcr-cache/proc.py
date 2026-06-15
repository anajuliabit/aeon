import json
D='/home/runner/work/aeon/aeon/.mcr-cache/'
def load(p):
    with open(D+p) as f: return json.load(f)

g = load('cg_global.json')['data']
print("=== GLOBAL ===")
print('mcap_usd', g['total_market_cap']['usd'])
print('mcap_chg_24h_pct', g['market_cap_change_percentage_24h_usd'])
print('btc_dom', g['market_cap_percentage']['btc'])
print('eth_dom', g['market_cap_percentage']['eth'])
print('vol_usd', g['total_volume']['usd'])

ch = load('llama_chains.json')
tot = sum(c['tvl'] for c in ch)
print("\n=== TVL ===")
print('total_tvl_B', round(tot/1e9,2))
for c in sorted(ch,key=lambda x:x['tvl'],reverse=True)[:5]:
    print(c['name'], round(c['tvl']/1e9,2),'B')

pr = load('llama_protocols.json')
print("\n=== PROTOCOLS ===")
for p in sorted(pr,key=lambda x:x.get('tvl') or 0,reverse=True)[:8]:
    print(p['name'], round((p.get('tvl') or 0)/1e9,2),'B  7d%', round(p.get('change_7d') or 0,2))

dx = load('llama_dexs.json')
print("\n=== DEX ===")
print('total24h_B', round((dx.get('total24h') or 0)/1e9,2))
print('change_1d', dx.get('change_1d'))
print('change_7d', dx.get('change_7d'))

st = load('llama_stables.json')['peggedAssets']
tots = sum(a['circulating'].get('peggedUSD',0) for a in st if 'peggedUSD' in a.get('circulating',{}))
print("\n=== STABLES ===")
print('total_B', round(tots/1e9,2))
for a in sorted(st,key=lambda x:x['circulating'].get('peggedUSD',0),reverse=True)[:6]:
    print(a['symbol'], round(a['circulating'].get('peggedUSD',0)/1e9,2),'B')

print("\n=== POLY VOL ===")
for m in load('poly_vol.json'):
    try: op=json.loads(m.get('outcomePrices') or '[]')
    except: op=[]
    yes=float(op[0])*100 if op else None
    print(round(m.get('volume24hr') or 0), '|', round(float(m.get('liquidity') or 0)), '|', (round(yes,1) if yes is not None else 'na'), '|', (m.get('question') or '')[:75])

print("\n=== POLY LIQ ===")
for m in load('poly_liq.json'):
    try: op=json.loads(m.get('outcomePrices') or '[]')
    except: op=[]
    yes=float(op[0])*100 if op else None
    print(round(float(m.get('liquidity') or 0)), '|', round(m.get('volume24hr') or 0), '|', (round(yes,1) if yes is not None else 'na'), '|', (m.get('question') or '')[:75])
