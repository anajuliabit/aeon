#!/usr/bin/env python3
import json
import sys

# Read markets data
with open('/home/runner/work/aeon/aeon/.cg-markets.json', 'r') as f:
    markets = json.load(f)

# Read trending data
with open('/home/runner/work/aeon/aeon/.cg-trending.json', 'r') as f:
    trending_data = json.load(f)

# Extract trending coins array
trending_coins = trending_data.get('coins', [])

# Create output
output = {
    'markets': markets,
    'trending': trending_coins
}

# Write output
with open('/home/runner/work/aeon/aeon/.token-movers-output.json', 'w') as f:
    json.dump(output, f)

print(f"Markets: {len(markets)} coins")
print(f"Trending: {len(trending_coins)} coins")
print("Output file created successfully")
