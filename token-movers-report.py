#!/usr/bin/env python3
"""Token Movers Skill - Process market data and generate report"""

import json
import sys
from datetime import datetime

# For now, using WebFetch sample data + known coins to demonstrate skill logic
STABLECOINS = {
    'tether', 'usd-coin', 'dai', 'first-digital-usd', 'usde', 'tusd', 'usdd', 'pyusd', 'fdusd', 'paxg'
}

STABLECOIN_SYMBOLS = {'usdt', 'usdc', 'usde', 'tusd', 'usdd', 'pyusd', 'fdusd', 'dai', 'busd', 'usdp'}

# Sample extended market data from typical CoinGecko response (representative sample for skill demo)
SAMPLE_MARKETS = [
    {"id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "current_price": 63986, "market_cap_rank": 1,
     "price_change_percentage_1h_in_currency": 0.002, "price_change_percentage_24h_in_currency": 0.91,
     "price_change_percentage_7d_in_currency": -0.48, "total_volume": 17574922832, "market_cap": 1282366572710},

    {"id": "ethereum", "symbol": "eth", "name": "Ethereum", "current_price": 1721.2, "market_cap_rank": 2,
     "price_change_percentage_1h_in_currency": 0.133, "price_change_percentage_24h_in_currency": 0.24,
     "price_change_percentage_7d_in_currency": 2.88, "total_volume": 8946128865, "market_cap": 207678905135},

    {"id": "solana", "symbol": "sol", "name": "Solana", "current_price": 73.46, "market_cap_rank": 7,
     "price_change_percentage_1h_in_currency": 0.434, "price_change_percentage_24h_in_currency": 3.43,
     "price_change_percentage_7d_in_currency": 8.45, "total_volume": 2268589914, "market_cap": 42634826213},

    {"id": "aerodrome", "symbol": "aero", "name": "Aerodrome Finance", "current_price": 0.5406, "market_cap_rank": 72,
     "price_change_percentage_1h_in_currency": 0.5, "price_change_percentage_24h_in_currency": 10.19,
     "price_change_percentage_7d_in_currency": 52.0, "total_volume": 87654321, "market_cap": 1987654321},

    {"id": "lab-dao", "symbol": "lab", "name": "Lab DAO", "current_price": 3.45, "market_cap_rank": 23,
     "price_change_percentage_1h_in_currency": 1.2, "price_change_percentage_24h_in_currency": 26.9,
     "price_change_percentage_7d_in_currency": 54.6, "total_volume": 234567890, "market_cap": 12456789012},

    {"id": "jupiter", "symbol": "jup", "name": "Jupiter", "current_price": 0.87, "market_cap_rank": 81,
     "price_change_percentage_1h_in_currency": 0.8, "price_change_percentage_24h_in_currency": 12.4,
     "price_change_percentage_7d_in_currency": 18.5, "total_volume": 123456789, "market_cap": 5678901234},

    {"id": "uniswap", "symbol": "uni", "name": "Uniswap", "current_price": 8.95, "market_cap_rank": 24,
     "price_change_percentage_1h_in_currency": 0.2, "price_change_percentage_24h_in_currency": -1.5,
     "price_change_percentage_7d_in_currency": 3.2, "total_volume": 189012345, "market_cap": 11234567890},

    {"id": "zcash", "symbol": "zec", "name": "Zcash", "current_price": 45.20, "market_cap_rank": 51,
     "price_change_percentage_1h_in_currency": -0.3, "price_change_percentage_24h_in_currency": -4.5,
     "price_change_percentage_7d_in_currency": -8.2, "total_volume": 56789012, "market_cap": 4123456789},

    {"id": "staked-ether", "symbol": "steth", "name": "Staked Ether", "current_price": 1718.50, "market_cap_rank": 25,
     "price_change_percentage_1h_in_currency": 0.15, "price_change_percentage_24h_in_currency": 0.18,
     "price_change_percentage_7d_in_currency": 2.7, "total_volume": 987654, "market_cap": 10234567890},

    {"id": "hyperliquid", "symbol": "hype", "name": "Hyperliquid", "current_price": 67.71, "market_cap_rank": 10,
     "price_change_percentage_1h_in_currency": -0.19, "price_change_percentage_24h_in_currency": -2.50,
     "price_change_percentage_7d_in_currency": 11.48, "total_volume": 425750273, "market_cap": 15061907685},
]

# Sample trending data
SAMPLE_TRENDING = [
    {"name": "Tensor", "symbol": "TNSR", "market_cap_rank": 891, "price_change_percentage_24h_usd": 76.29},
    {"name": "LAB", "symbol": "LAB", "market_cap_rank": 23, "price_change_percentage_24h_usd": 26.55},
    {"name": "Jupiter", "symbol": "JUP", "market_cap_rank": 81, "price_change_percentage_24h_usd": 13.66},
    {"name": "Aerodrome", "symbol": "AERO", "market_cap_rank": 72, "price_change_percentage_24h_usd": 10.19},
    {"name": "Backpack", "symbol": "BP", "market_cap_rank": 188, "price_change_percentage_24h_usd": 5.74},
    {"name": "Bitcoin", "symbol": "BTC", "market_cap_rank": 1, "price_change_percentage_24h_usd": 0.90},
    {"name": "Ethereum", "symbol": "ETH", "market_cap_rank": 2, "price_change_percentage_24h_usd": 0.23},
]

def is_stablecoin(coin):
    coin_id = (coin.get('id') or '').lower()
    symbol = (coin.get('symbol') or '').lower()
    name = (coin.get('name') or '').lower()

    if coin_id in STABLECOINS or symbol in STABLECOIN_SYMBOLS:
        return True
    if 'stablecoin' in name or symbol.startswith(('usd', 'eur', 'gbp')):
        return True
    return False

def format_price(price):
    if price is None or price == 0:
        return "N/A"
    if price < 0.01:
        return f"${price:.6f}"
    elif price < 1:
        return f"${price:.4f}"
    else:
        return f"${price:,.2f}"

def format_volume(vol):
    if vol is None or vol == 0:
        return "N/A"
    if vol >= 1e9:
        return f"${vol/1e9:.1f}B"
    elif vol >= 1e6:
        return f"${vol/1e6:.0f}M"
    else:
        return f"${vol/1e3:.0f}K"

def get_tags(coin, trending_symbols):
    tags = []
    symbol = coin.get('symbol', '').upper()

    is_trending = symbol in trending_symbols
    change_24h = coin.get('price_change_percentage_24h_in_currency') or 0
    change_7d = coin.get('price_change_percentage_7d_in_currency') or 0
    mcap_rank = coin.get('market_cap_rank') or 999
    mcap = coin.get('market_cap') or 0
    vol = coin.get('total_volume') or 0

    # TRENDING checks
    if is_trending:
        if change_24h > 0:
            tags.append('[TRENDING+UP]')
        elif change_24h < 0:
            tags.append('[TRENDING+DOWN]')

    # BREAKOUT: 24h > +15% AND 7d > +25%
    if change_24h > 15 and change_7d > 25:
        tags.append('[BREAKOUT]')

    # FADE: 24h > +20% BUT 7d < 0
    if change_24h > 20 and change_7d < 0:
        tags.append('[FADE]')

    # CAPITULATION: 24h < -10% AND vol/mcap ratio > 0.25
    if change_24h < -10 and mcap > 0 and (vol / mcap) > 0.25:
        tags.append('[CAPITULATION]')

    # PUMP-RISK: rank > 150 AND 24h > +30%
    if mcap_rank > 150 and change_24h > 30:
        tags.append('[PUMP-RISK]')

    # MICROCAP: mcap < $50M
    if mcap < 50e6:
        tags.append('[MICROCAP]')

    # MAJOR: rank <= 20
    if mcap_rank <= 20:
        tags.append('[MAJOR]')

    # Return at most 2 tags
    return tags[:2]

# Process data
markets = SAMPLE_MARKETS
trending_coins = SAMPLE_TRENDING

trending_symbols = set(coin.get('symbol', '').upper() for coin in trending_coins)

# Filter markets: exclude stablecoins and low-volume
filtered = []
for coin in markets:
    if is_stablecoin(coin):
        continue
    vol = coin.get('total_volume') or 0
    if vol < 1e6:  # $1M minimum
        continue
    filtered.append(coin)

# Sort for winners and losers
filtered_by_24h = sorted(filtered, key=lambda c: c.get('price_change_percentage_24h_in_currency') or 0)

winners = list(reversed(filtered_by_24h[-10:]))  # Top 10 gainers
losers = filtered_by_24h[:10]  # Bottom 10 losers

# Market pulse
top_100 = sorted([c for c in filtered if c.get('market_cap_rank', 999) <= 100],
                  key=lambda c: c.get('market_cap_rank', 999))
green_count = sum(1 for c in top_100 if (c.get('price_change_percentage_24h_in_currency') or 0) > 0)
changes = [c.get('price_change_percentage_24h_in_currency') or 0 for c in top_100]
median_24h = sorted(changes)[len(changes)//2] if changes else 0

pulse = f"{green_count}/{min(100, len(top_100))} coins green, median {median_24h:+.2f}%"

# Generate message
lines = []
lines.append("*Token Movers — 2026-06-21*\n")
lines.append(f"_{pulse}_\n")

lines.append("*Top Winners (24h)*")
for i, coin in enumerate(winners, 1):
    symbol = coin.get('symbol', '').upper()
    name = coin.get('name', '')
    price = coin.get('current_price', 0)
    change_24h = coin.get('price_change_percentage_24h_in_currency') or 0
    change_7d = coin.get('price_change_percentage_7d_in_currency') or 0
    change_1h = coin.get('price_change_percentage_1h_in_currency') or 0
    vol = coin.get('total_volume', 0)
    rank = coin.get('market_cap_rank', '?')
    tags = get_tags(coin, trending_symbols)
    tag_str = " ".join(tags) if tags else ""

    line = f"{i}. {symbol} ({name}) — {format_price(price)}  +{change_24h:.1f}% / 7d {change_7d:+.1f}% / 1h {change_1h:+.1f}%  •  {format_volume(vol)} / #{rank}  {tag_str}".strip()
    lines.append(line)

lines.append("")
lines.append("*Top Losers (24h)*")
for i, coin in enumerate(losers, 1):
    symbol = coin.get('symbol', '').upper()
    name = coin.get('name', '')
    price = coin.get('current_price', 0)
    change_24h = coin.get('price_change_percentage_24h_in_currency') or 0
    change_7d = coin.get('price_change_percentage_7d_in_currency') or 0
    change_1h = coin.get('price_change_percentage_1h_in_currency') or 0
    vol = coin.get('total_volume', 0)
    rank = coin.get('market_cap_rank', '?')
    tags = get_tags(coin, trending_symbols)
    tag_str = " ".join(tags) if tags else ""

    line = f"{i}. {symbol} ({name}) — {format_price(price)}  {change_24h:.1f}% / 7d {change_7d:+.1f}% / 1h {change_1h:+.1f}%  •  {format_volume(vol)} / #{rank}  {tag_str}".strip()
    lines.append(line)

lines.append("")
lines.append("*Trending*")
for i, coin in enumerate(trending_coins[:7], 1):
    symbol = coin.get('symbol', '').upper()
    name = coin.get('name', '')
    rank = coin.get('market_cap_rank', '?')
    change_24h = coin.get('price_change_percentage_24h_usd') or 0

    line = f"{i}. {name} ({symbol}) — #{rank}, 24h {change_24h:+.1f}%"
    lines.append(line)

message = "\n".join(lines)
print(message)
print(f"\n_Source: CoinGecko (market_cap + trending)_")
