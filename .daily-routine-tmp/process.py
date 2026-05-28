#!/usr/bin/env python3
import json, re, sys

STABLE_IDS = {
    "tether","usd-coin","dai","first-digital-usd","ethena-usde","true-usd","usdd",
    "paypal-usd","fdusd","pax-gold","usd0","usds","frax","liquity-usd","crvusd",
    "mountain-protocol-usdm","ondo-us-dollar-yield","m-by-m0","ripple-usd","usdb",
    "gho","mim","susds","ousd","blackrock-usd-institutional-digital-liquidity-fund",
    "apollo-diversified-credit-securitize-fund","susd","alusd","ethena-staked-usde",
    "susde","sky-dollar","usdy","resolv-usd","ousd-stablecoin","usdf","apxusd",
    "yusd","yields","apyusd","rwausdi"
}
WRAPPED_IDS = {
    "wrapped-bitcoin","weth","wbeth","staked-ether","wrapped-steth","liquid-staked-ether",
    "rocket-pool-eth","cbeth","coinbase-wrapped-btc","tbtc","wrapped-eeth",
    "lombard-staked-btc","binance-staked-sol","jito-staked-sol","msol",
    "kelp-dao-restaked-eth","etherfi-staked-eth","renzo-restaked-eth",
    "binance-bitcoin","wsteth","wrapped-beacon-eth","mantle-staked-ether",
    "stader-ethx","frax-ether","sfrxeth","jupiter-staked-sol","solv-protocol-solvbtc",
    "solv-protocol-staked-btc","binance-peg-weth"
}
EXCLUDED = STABLE_IDS | WRAPPED_IDS
SYM_STABLE = re.compile(r"^(usd|eur|gbp|brl|euro|usdb|usdc|usdt|usdd|usde|usdp|usdf|usds|usdy|usd0|usdx)", re.I)

with open(sys.argv[1]) as f:
    data = json.load(f)

def keep(c):
    if c.get("id") in EXCLUDED: return False
    sym = c.get("symbol") or ""
    if SYM_STABLE.match(sym): return False
    if (c.get("total_volume") or 0) < 1_000_000: return False
    if (c.get("market_cap") or 0) <= 0: return False
    if c.get("price_change_percentage_24h") is None: return False
    return True

filt = [c for c in data if keep(c)]

def shape(c):
    return {
        "n": c["name"],
        "s": c["symbol"],
        "id": c["id"],
        "r": c.get("market_cap_rank"),
        "p": c.get("current_price"),
        "h1": c.get("price_change_percentage_1h_in_currency"),
        "h24": c.get("price_change_percentage_24h"),
        "d7": c.get("price_change_percentage_7d_in_currency"),
        "v": c.get("total_volume"),
        "m": c.get("market_cap"),
    }

winners = sorted(filt, key=lambda c: c["price_change_percentage_24h"], reverse=True)[:15]
losers  = sorted(filt, key=lambda c: c["price_change_percentage_24h"])[:15]
top100 = sorted(filt, key=lambda c: c["market_cap"], reverse=True)[:100]
changes = sorted([c["price_change_percentage_24h"] for c in top100])
pulse = {
    "n": len(top100),
    "green": sum(1 for c in top100 if c["price_change_percentage_24h"] > 0),
    "median": changes[len(changes)//2] if changes else 0,
    "median_top50": sorted([c["price_change_percentage_24h"] for c in top100[:50]])[25] if top100 else 0,
}

out = {
    "winners": [shape(c) for c in winners],
    "losers":  [shape(c) for c in losers],
    "pulse":   pulse,
}
print(json.dumps(out, indent=2))
