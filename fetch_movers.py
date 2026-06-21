#!/usr/bin/env python3
import json
import urllib.request
import urllib.error
import sys
from datetime import datetime

# Fetch markets data
try:
    with urllib.request.urlopen("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false&price_change_percentage=1h,24h,7d", timeout=10) as response:
        markets = json.loads(response.read().decode('utf-8'))
        print(f"Markets: {len(markets)} coins fetched", file=sys.stderr)
except Exception as e:
    print(f"Markets fetch failed: {e}", file=sys.stderr)
    markets = []

# Fetch trending data
try:
    with urllib.request.urlopen("https://api.coingecko.com/api/v3/search/trending", timeout=10) as response:
        trending_data = json.loads(response.read().decode('utf-8'))
        trending = trending_data.get('coins', [])
        print(f"Trending: {len(trending)} coins fetched", file=sys.stderr)
except Exception as e:
    print(f"Trending fetch failed: {e}", file=sys.stderr)
    trending = []

if not markets:
    print("ERROR: Markets data failed to fetch", file=sys.stderr)
    sys.exit(1)

# Define stablecoin exclusions
stablecoins = {'tether', 'usd-coin', 'dai', 'first-digital-usd', 'usde', 'tusd', 'usdd', 'pyusd', 'fdusd', 'paxg'}

# Filter: exclude stablecoins and low-volume coins
filtered = []
for coin in markets:
    coin_id = coin.get('id', '').lower()
    symbol = coin.get('symbol', '').upper()
    name = coin.get('name', '')

    # Check if stablecoin
    if coin_id in stablecoins:
        continue
    if symbol.startswith(('USD', 'EUR', 'GBP')):
        continue
    if 'stablecoin' in name.lower():
        continue

    # Check volume
    volume = coin.get('total_volume') or 0
    if volume < 1_000_000:
        continue

    filtered.append(coin)

print(f"After filtering: {len(filtered)} coins (excluded stables/low-volume)", file=sys.stderr)

# Sort for winners and losers
winners = sorted(filtered, key=lambda x: x.get('price_change_percentage_24h') or 0, reverse=True)[:10]
losers = sorted(filtered, key=lambda x: x.get('price_change_percentage_24h') or 0)[:10]

# Calculate market pulse (top 100)
top100 = sorted(filtered, key=lambda x: x.get('market_cap_rank') or 999)[:100]
green_count = sum(1 for c in top100 if (c.get('price_change_percentage_24h') or 0) > 0)
median_24h = sorted([c.get('price_change_percentage_24h') or 0 for c in top100])[len(top100)//2]

print("\n### MARKET PULSE")
print(f"Green coins (top 100): {green_count}/100 ({100*green_count/len(top100):.1f}%)")
print(f"Median 24h change: {median_24h:+.2f}%")

print("\n### TOP 10 WINNERS (24h)")
for i, coin in enumerate(winners, 1):
    sym = coin.get('symbol', '').upper()
    name = coin.get('name', '')
    price = coin.get('current_price', 0)
    chg24h = coin.get('price_change_percentage_24h', 0) or 0
    chg7d = coin.get('price_change_percentage_7d') or 0
    chg1h = coin.get('price_change_percentage_1h') or 0
    vol = coin.get('total_volume', 0) or 0
    mcap_rank = coin.get('market_cap_rank', 'N/A')
    print(f"{i}. {sym} ({name}) — ${price:.4g}  +{chg24h:.1f}% / 7d {chg7d:+.1f}% / 1h {chg1h:+.1f}%  •  ${vol/1e9:.2f}B / #{mcap_rank}")

print("\n### TOP 10 LOSERS (24h)")
for i, coin in enumerate(losers, 1):
    sym = coin.get('symbol', '').upper()
    name = coin.get('name', '')
    price = coin.get('current_price', 0)
    chg24h = coin.get('price_change_percentage_24h', 0) or 0
    chg7d = coin.get('price_change_percentage_7d') or 0
    chg1h = coin.get('price_change_percentage_1h') or 0
    vol = coin.get('total_volume', 0) or 0
    mcap_rank = coin.get('market_cap_rank', 'N/A')
    print(f"{i}. {sym} ({name}) — ${price:.4g}  {chg24h:.1f}% / 7d {chg7d:+.1f}% / 1h {chg1h:+.1f}%  •  ${vol/1e9:.2f}B / #{mcap_rank}")

print("\n### TOP 7 TRENDING")
for i, coin in enumerate(trending[:7], 1):
    item = coin.get('item', {})
    name = item.get('name', '')
    sym = item.get('symbol', '').upper()
    rank = item.get('market_cap_rank', 'N/A')
    price = item.get('data', {}).get('price', 0)
    print(f"{i}. {name} ({sym}) — #{rank}, ${price:.4g}")

# Build signal tags for winners
print("\n### SIGNAL ANALYSIS")

def compute_tags(coin, trending_ids):
    tags = []
    chg24h = coin.get('price_change_percentage_24h') or 0
    chg7d = coin.get('price_change_percentage_7d') or 0
    mcap = coin.get('market_cap') or 0
    mcap_rank = coin.get('market_cap_rank') or 999
    vol = coin.get('total_volume') or 0

    is_trending = coin.get('id') in trending_ids

    # [TRENDING+UP]
    if is_trending and chg24h > 0:
        tags.append("[TRENDING+UP]")
    # [TRENDING+DOWN]
    elif is_trending and chg24h < 0:
        tags.append("[TRENDING+DOWN]")
    # [BREAKOUT]
    elif chg24h > 15 and chg7d > 25:
        tags.append("[BREAKOUT]")
    # [FADE]
    elif chg24h > 20 and chg7d < 0:
        tags.append("[FADE]")
    # [CAPITULATION]
    elif chg24h < -10 and (vol / mcap if mcap > 0 else 0) > 0.25:
        tags.append("[CAPITULATION]")
    # [PUMP-RISK]
    elif mcap_rank > 150 and chg24h > 30:
        tags.append("[PUMP-RISK]")
    # [MICROCAP]
    if mcap < 50_000_000:
        tags.append("[MICROCAP]")
    # [MAJOR]
    if mcap_rank <= 20:
        tags.append("[MAJOR]")

    return tags[:2]  # max 2 tags

trending_ids = set(c.get('item', {}).get('id') for c in trending)
print("Trending IDs:", len(trending_ids))

notable = []
for coin in winners + losers:
    tags = compute_tags(coin, trending_ids)
    if any(tag in ['[TRENDING+UP]', '[BREAKOUT]', '[CAPITULATION]', '[PUMP-RISK]'] for tag in tags):
        sym = coin.get('symbol', '').upper()
        chg24h = coin.get('price_change_percentage_24h') or 0
        notable.append(f"{sym}: {', '.join(tags)} (+{chg24h:.1f}% 24h)" if chg24h > 0 else f"{sym}: {', '.join(tags)} ({chg24h:.1f}% 24h)")

if notable:
    print("\n### NOTABLE SIGNALS")
    for n in notable[:4]:
        print(f"• {n}")

print(f"\nGenerated: {datetime.utcnow().isoformat()}Z", file=sys.stderr)
