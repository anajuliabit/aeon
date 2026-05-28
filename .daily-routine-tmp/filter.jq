def stablecoin_ids: ["tether","usd-coin","dai","first-digital-usd","ethena-usde","true-usd","usdd","paypal-usd","fdusd","pax-gold","usd0","usds","frax","liquity-usd","crvusd","mountain-protocol-usdm","ondo-us-dollar-yield","m-by-m0","ripple-usd","usdb","gho","mim","susds","ousd","resolv-usd","blackrock-usd-institutional-digital-liquidity-fund","apollo-diversified-credit-securitize-fund","susd","alusd","ethena-staked-usde","susde","sky-dollar","usdy"];
def wrapped_ids: ["wrapped-bitcoin","weth","wbeth","staked-ether","wrapped-steth","liquid-staked-ether","rocket-pool-eth","cbeth","coinbase-wrapped-btc","tbtc","wrapped-eeth","lombard-staked-btc","binance-staked-sol","jito-staked-sol","msol","jupiter-staked-sol","mev-protocol","kelp-dao-restaked-eth","etherfi-staked-eth","renzo-restaked-eth","binance-bitcoin","wsteth"];
def excluded: (stablecoin_ids + wrapped_ids);
def sym_is_stable: ascii_downcase | test("^(usd|eur|gbp|brl|euro|usdb|usdc|usdt|usdd|usde|usdp|usdf|usds|usdy|usd0|usdx)");

def filtered: [.[] |
  select((.id // "") as $i | (excluded | index($i)) | not) |
  select(.symbol | sym_is_stable | not) |
  select((.total_volume // 0) >= 1000000) |
  select((.market_cap // 0) > 0)
];

def shape: map({n: .name, s: .symbol, id: .id, r: .market_cap_rank, p: .current_price, h1: .price_change_percentage_1h_in_currency, h24: .price_change_percentage_24h, d7: .price_change_percentage_7d_in_currency, v: .total_volume, m: .market_cap});

filtered as $f |
{
  winners: ($f | sort_by(.price_change_percentage_24h) | reverse | .[0:15] | shape),
  losers:  ($f | sort_by(.price_change_percentage_24h) | .[0:15] | shape),
  pulse_top100: ($f | sort_by(.market_cap) | reverse | .[0:100] | {
    n: length,
    green: (map(select(.price_change_percentage_24h > 0)) | length),
    median: (map(.price_change_percentage_24h) | sort | .[(length/2|floor)])
  })
}
