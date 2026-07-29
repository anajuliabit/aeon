map(select(
  (.id | test("tether|usd-coin|^dai$|first-digital-usd|usde|tusd|usdd|pyusd|fdusd|paxg|usual-usd|frax|lusd|susd|gusd|susds|olusd") | not) and
  (.symbol | test("^(usd|eur|gbp|steth|weth|wbtc|reth|cbeth|meth|wsteth|rseth|weeth|eeth|ezeth|sfrxeth|wbeth)$"; "i") | not) and
  (.total_volume // 0) >= 1000000
)) as $filtered |
{
  filtered_count: ($filtered | length),
  winners: ($filtered | sort_by(.price_change_percentage_24h) | reverse | .[:10] | map({rank: .market_cap_rank, symbol: (.symbol|ascii_upcase), name, price: .current_price, h1: (.price_change_percentage_1h_in_currency // 0), h24: (.price_change_percentage_24h // 0), d7: (.price_change_percentage_7d_in_currency // 0), vol: .total_volume, mcap: .market_cap})),
  losers: ($filtered | sort_by(.price_change_percentage_24h) | .[:10] | map({rank: .market_cap_rank, symbol: (.symbol|ascii_upcase), name, price: .current_price, h1: (.price_change_percentage_1h_in_currency // 0), h24: (.price_change_percentage_24h // 0), d7: (.price_change_percentage_7d_in_currency // 0), vol: .total_volume, mcap: .market_cap})),
  top100: ($filtered | map(select(.market_cap_rank <= 100))),
  top50: ($filtered | map(select(.market_cap_rank <= 50)))
} |
{
  filtered_count,
  winners,
  losers,
  top100_green: ([.top100[] | select(.price_change_percentage_24h > 0)] | length),
  top100_count: (.top100 | length),
  top50_median_pct: (.top50 | map(.price_change_percentage_24h) | sort | if length == 0 then 0 else .[length/2|floor] end)
}
