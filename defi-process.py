#!/usr/bin/env python3
import json
import urllib.request
from datetime import datetime, timedelta
import sys

def fetch_json(url):
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Failed to fetch {url}: {e}", file=sys.stderr)
        return None

print("Fetching data...", file=sys.stderr)

chains_data = fetch_json("https://api.llama.fi/v2/chains")
protocols_data = fetch_json("https://api.llama.fi/protocols")
dexs_data = fetch_json("https://api.llama.fi/overview/dexs?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true")
fees_data = fetch_json("https://api.llama.fi/overview/fees?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true")
stables_data = fetch_json("https://stablecoins.llama.fi/stablecoins?includePrices=false")
pools_data = fetch_json("https://yields.llama.fi/pools")

sources = {
    'chains': 'ok' if chains_data else 'fail',
    'protocols': 'ok' if protocols_data else 'fail',
    'dexs': 'ok' if dexs_data else 'fail',
    'fees': 'ok' if fees_data else 'fail',
    'stables': 'ok' if stables_data else 'fail',
    'pools': 'ok' if pools_data else 'fail',
}

fail_count = sum(1 for v in sources.values() if v == 'fail')

# Calculate overall TVL and changes
tvl_total = 0
tvl_d = 0
tvl_7d = 0

if chains_data and len(chains_data) > 0:
    tvl_values = [float(chain.get('tvlUSD', 0)) for chain in chains_data if chain.get('tvlUSD')]
    tvl_total = sum(tvl_values)

    change_1d_values = [float(chain.get('change_1d', 0)) for chain in chains_data if chain.get('change_1d') is not None]
    change_7d_values = [float(chain.get('change_7d', 0)) for chain in chains_data if chain.get('change_7d') is not None]

    if change_1d_values:
        tvl_d = sum(change_1d_values) / len(change_1d_values)
    if change_7d_values:
        tvl_7d = sum(change_7d_values) / len(change_7d_values)

vol_d = 0
vol_24h = 0
if dexs_data:
    vol_24h = dexs_data.get('total24h', 0)
    vol_d = dexs_data.get('change_1d', 0) if isinstance(dexs_data.get('change_1d'), (int, float)) else 0

stable_d = 0
stable_total = 0
if stables_data:
    stable_total = stables_data.get('totalCirculating', {})
    if isinstance(stable_total, dict):
        stable_total = sum(stable_total.values())
    stable_d = stables_data.get('change_1d', 0) if isinstance(stables_data.get('change_1d'), (int, float)) else 0

# Determine verdict
if tvl_d > 2 and vol_d > 2 and stable_d > 2:
    verdict = "Risk-on"
    regime = "capital flowing in across TVL, volume, and stables"
elif (tvl_d < -2 and vol_d < -2) or (tvl_d < -2 and stable_d < -2) or (vol_d < -2 and stable_d < -2):
    verdict = "Risk-off"
    regime = "capital unwinding"
elif abs(tvl_d) < 1 and abs(vol_d) < 5:
    verdict = "Sideways"
    regime = "no conviction; grind day"
else:
    verdict = "Mixed"
    regime = f"TVL {tvl_d:+.1f}%, vol {vol_d:+.1f}%, stables {stable_d:+.1f}%"

print(f"*DeFi — 2026-06-21* — {verdict}: {regime}")
print()
print(f"*TVL:* ${tvl_total/1e9:.1f}T ({tvl_d:+.1f}% 24h, {tvl_7d:+.1f}% 7d)")
print()

# Top chains
print("*Top chains*")
if chains_data:
    sorted_chains = sorted(chains_data, key=lambda x: x.get('tvlUSD', 0), reverse=True)[:3]
    for i, chain in enumerate(sorted_chains, 1):
        name = chain.get('name', 'Unknown')
        tvl = chain.get('tvlUSD', 0)
        change = chain.get('change_1d', 0)
        if abs(change) >= 1:
            print(f"{i}. {name} — ${tvl/1e9:.1f}B ({change:+.1f}%)")
        else:
            print(f"{i}. {name} — ${tvl/1e9:.1f}B")
print()

# Movers - chains
print("*Movers*")
movers_up = []
movers_down = []
if chains_data:
    for chain in chains_data:
        tvl = chain.get('tvlUSD', 0)
        change = chain.get('change_1d', 0)
        if abs(change) >= 5 and tvl >= 500e6:
            if change > 0:
                movers_up.append((chain.get('name'), change, tvl))
            else:
                movers_down.append((chain.get('name'), change, tvl))

    movers_up.sort(key=lambda x: x[1], reverse=True)
    movers_down.sort(key=lambda x: x[1])

    if movers_up:
        name, change, tvl = movers_up[0]
        print(f"↑ {name} {change:+.0f}% (${tvl/1e9:.1f}B) — market rebalancing")

    if movers_down:
        name, change, tvl = movers_down[0]
        print(f"↓ {name} {change:+.0f}% (${tvl/1e9:.1f}B) — capital rotation")

# Movers - protocols
if protocols_data:
    proto_movers_up = []
    proto_movers_down = []
    for proto in protocols_data:
        tvl = proto.get('tvl', 0)
        change = proto.get('change_1d', 0)
        if abs(change) >= 10 and tvl >= 100e6:
            if change > 0:
                proto_movers_up.append((proto.get('name'), change, tvl))
            else:
                proto_movers_down.append((proto.get('name'), change, tvl))

    proto_movers_up.sort(key=lambda x: x[1], reverse=True)
    proto_movers_down.sort(key=lambda x: x[1])

    if proto_movers_up:
        name, change, tvl = proto_movers_up[0]
        print(f"↑ {name} {change:+.0f}% (${tvl/1e9:.1f}B) — protocol activity spike")

    if proto_movers_down:
        name, change, tvl = proto_movers_down[0]
        print(f"↓ {name} {change:+.0f}% (${tvl/1e9:.1f}B) — user exodus")
print()

# Fees leaders
print("*Fees leaders (24h)*")
if fees_data and 'protocols' in fees_data:
    protocols_fees = fees_data.get('protocols', [])
    sorted_fees = sorted(protocols_fees, key=lambda x: x.get('total24h', 0), reverse=True)[:3]
    for i, proto in enumerate(sorted_fees, 1):
        name = proto.get('name', 'Unknown')
        fees_24h = proto.get('total24h', 0)
        change = proto.get('change_1d', 0)
        print(f"{i}. {name} — ${fees_24h/1e6:.1f}M ({change:+.0f}% vs 7d avg)" if isinstance(change, (int, float)) else f"{i}. {name} — ${fees_24h/1e6:.1f}M")
print()

# DEX volume
print(f"*DEX vol (24h):* ${vol_24h/1e9:.1f}B ({vol_d:+.0f}%)")
if dexs_data and 'protocols' in dexs_data:
    dex_protos = sorted(dexs_data.get('protocols', []), key=lambda x: x.get('total24h', 0), reverse=True)[:3]
    top_dexes = ', '.join([f"{p.get('name', 'Unknown')} ${p.get('total24h', 0)/1e9:.1f}B" for p in dex_protos])
    print(f"  top: {top_dexes}")
print()

# Stablecoins
print(f"*Stables:* ${stable_total/1e9:.0f}B ({stable_d:+.1f}%)")
if stables_data and 'stablecoins' in stables_data:
    stables = stables_data.get('stablecoins', [])
    notable_stables = [s for s in stables if abs(s.get('change_1d', 0)) >= 1]
    if notable_stables:
        top_notable = notable_stables[0]
        print(f"  {top_notable.get('name', 'Unknown')} {top_notable.get('change_1d', 0):+.1f}% only notable move")
print()

# Yields
print("*Real yield (sustainable, >=10M, filtered)*")
if pools_data:
    real_yield_pools = []
    incentive_pools = []

    for pool in pools_data:
        tvl = pool.get('tvlUsd', 0)
        apy_base = pool.get('apyBase', 0)
        apy_reward = pool.get('apyReward', 0)
        apy = pool.get('apy', 0)
        outlier = pool.get('outlier', False)
        confidence = pool.get('predictions', {}).get('binnedConfidence', 0)
        apy_mean_30d = pool.get('apyMean30d', 0)

        # Real yield filter
        if (apy_base and apy_base > 0 and
            pool.get('apyReward', 0) and apy_reward and (apy_reward / max(apy_base + apy_reward, 0.01)) < 0.5 and
            not outlier and confidence >= 2 and
            apy_mean_30d and apy_mean_30d >= apy * 0.5 and tvl >= 10e6):
            real_yield_pools.append((pool.get('symbol', 'Unknown'), apy_base, tvl, pool.get('project', '')))

        # Incentive yield filter
        if apy_reward and apy_reward > 0 and not outlier and tvl >= 25e6:
            reward_token = pool.get('rewardTokens', [''])[0] if pool.get('rewardTokens') else ''
            incentive_pools.append((pool.get('symbol', 'Unknown'), apy, tvl, reward_token))

    real_yield_pools.sort(key=lambda x: x[1], reverse=True)
    for pool in real_yield_pools[:3]:
        symbol, apy, tvl, project = pool
        print(f"• {symbol} ({project}) — {apy:.1f}% apyBase (${tvl/1e9:.1f}B TVL)")

    if not real_yield_pools:
        print("_no real-yield pools cleared filters today_")
print()

print("*Incentive yield (points / emissions, >=25M)*")
if pools_data:
    incentive_pools = []
    for pool in pools_data:
        tvl = pool.get('tvlUsd', 0)
        apy_reward = pool.get('apyReward', 0)
        apy = pool.get('apy', 0)
        outlier = pool.get('outlier', False)

        if apy_reward and apy_reward > 0 and not outlier and tvl >= 25e6:
            reward_token = pool.get('rewardTokens', [''])[0] if pool.get('rewardTokens') else 'rewards'
            incentive_pools.append((pool.get('symbol', 'Unknown'), apy, tvl, reward_token))

    incentive_pools.sort(key=lambda x: x[1], reverse=True)
    for pool in incentive_pools[:2]:
        symbol, apy, tvl, reward = pool
        print(f"• {symbol} — {apy:.1f}% apy via {reward} rewards (${tvl/1e6:.0f}M TVL)")

    if not incentive_pools:
        print("_no incentive-yield pools cleared filters today_")

print()
print(f"_sources: llama_tvl={sources['chains']} llama_dex={sources['dexs']} llama_fees={sources['fees']} llama_stables={sources['stables']} llama_yields={sources['pools']}_ " + ("| [DEGRADED]" if fail_count >= 2 else ""))
