import json
import sys
import math

# Load data
with open('/home/runner/.claude/projects/-home-runner-work-aeon-aeon/e2603b6b-a037-47c5-98e8-f297e260f96d/tool-results/b6rsyoxqj.txt', 'r') as f:
    market_data = json.load(f)

with open('/home/runner/.claude/projects/-home-runner-work-aeon-aeon/e2603b6b-a037-47c5-98e8-f297e260f96d/tool-results/bzkpdgi5w.txt', 'r') as f:
    trending_data = json.load(f)

# Filter stablecoins
stablecoin_ids = {'tether', 'usd-coin', 'dai', 'first-digital-usd', 'usde', 'tusd', 'usdd', 'pyusd', 'fdusd', 'paxg'}
stablecoin_symbol_prefixes = {'USD', 'EUR', 'GBP'}
stablecoin_name_keywords = {'stablecoin'}

def is_stablecoin(coin):
    if coin['id'] in stablecoin_ids:
        return True
    if coin['symbol'].upper().startswith(tuple(stablecoin_symbol_prefixes)):
        return True
    if 'name' in coin and any(kw in coin['name'].lower() for kw in stablecoin_name_keywords):
        return True
    return False

# Apply filters
filtered = []
for coin in market_data:
    # Skip stablecoins
    if is_stablecoin(coin):
        continue
    # Skip low volume (< $1M)
    if coin.get('total_volume', 0) < 1_000_000:
        continue
    filtered.append(coin)

# Sort by 24h % change
winners = sorted(filtered, key=lambda x: x.get('price_change_percentage_24h_in_currency', -float('inf')), reverse=True)
losers = sorted(filtered, key=lambda x: x.get('price_change_percentage_24h_in_currency', float('inf')))

# Get top 10 each
top_winners = winners[:10]
top_losers = losers[:10]

# Extract trending coins
trending_coins = trending_data.get('coins', [])[:7]
trending_details = []
for item in trending_coins:
    coin_info = item.get('item', {})
    trending_details.append({
        'id': coin_info.get('id'),
        'name': coin_info.get('name'),
        'symbol': coin_info.get('symbol', '').upper(),
        'market_cap_rank': coin_info.get('market_cap_rank'),
        'price': coin_info.get('data', {}).get('price'),
        'price_change_percentage_24h': coin_info.get('data', {}).get('price_change_percentage_24h', {}).get('usd')
    })

# Helper to format numbers
def fmt_number(n):
    if n is None:
        return None
    if n >= 1_000_000_000:
        return f'${n/1_000_000_000:.1f}B'
    if n >= 1_000_000:
        return f'${n/1_000_000:.1f}M'
    if n >= 1_000:
        return f'${n/1_000:.1f}K'
    return f'${n:.2f}'

# Compute market pulse
top_100_by_mcap = sorted([c for c in filtered if c.get('market_cap_rank', float('inf')) <= 100], key=lambda x: x.get('market_cap_rank', float('inf')))
top_100 = top_100_by_mcap[:100]
positive_count = sum(1 for c in top_100 if c.get('price_change_percentage_24h_in_currency', 0) > 0)
positive_ratio = positive_count / len(top_100) if top_100 else 0

# Get median change
changes = [c.get('price_change_percentage_24h_in_currency', 0) for c in top_100[:50]]
changes.sort()
median_change = changes[len(changes)//2] if changes else 0

market_pulse = f"{positive_count}/100 top coins are {'green' if positive_ratio > 0.5 else 'red'}, median {median_change:+.1f}%"

print('Market pulse:', market_pulse)
print('\nTop winners:')
for i, coin in enumerate(top_winners, 1):
    print(f"{i}. {coin['symbol'].upper()} ({coin['name']}) — ${coin['current_price']:.4f}  +{coin['price_change_percentage_24h_in_currency']:.1f}% / 7d {coin['price_change_percentage_7d_in_currency']:+.1f}% / 1h {coin['price_change_percentage_1h_in_currency']:+.1f}%  •  {fmt_number(coin['total_volume'])} / #{coin['market_cap_rank']}")

print('\nTop losers:')
for i, coin in enumerate(top_losers, 1):
    print(f"{i}. {coin['symbol'].upper()} ({coin['name']}) — ${coin['current_price']:.4f}  {coin['price_change_percentage_24h_in_currency']:+.1f}% / 7d {coin['price_change_percentage_7d_in_currency']:+.1f}% / 1h {coin['price_change_percentage_1h_in_currency']:+.1f}%  •  {fmt_number(coin['total_volume'])} / #{coin['market_cap_rank']}")

print('\nTrending:')
for i, coin in enumerate(trending_details, 1):
    if coin['price_change_percentage_24h']:
        change_str = f"{coin['price_change_percentage_24h']:+.1f}%"
    else:
        change_str = "N/A"
    print(f"{i}. {coin['name']} ({coin['symbol']}) — #{coin['market_cap_rank']}, ${coin['price']:.4f}, 24h {change_str}")