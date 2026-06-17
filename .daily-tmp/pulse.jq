map(select(
  (.id | test("tether|usd-coin|^dai$|^usds$|usde|first-digital|true-usd|paxos|frax|^busd$|liquity-usd|gho|crvusd|pyusd|stusdt|usd0$|fdusd|ousd|sdai|usdd|^usdr$|^susd$|usdp$|^vai$|alusd|mim$"; "i") | not)
  and (.symbol | ascii_upcase | test("^(USDT|USDC|DAI|USDS|USDE|FDUSD|TUSD|FRAX|BUSD|LUSD|GHO|CRVUSD|PYUSD|USDD|USDP|GUSD|USDX|RUSD|XAUT|PAXG|USYC|SDAI|MIM|VAI|SUSD|FXUSD|ALUSD)$") | not)
  and (.id | test("wrapped|weth|wbtc|steth|reth|wsteth|cbeth|wbeth"; "i") | not)
  and (.total_volume // 0) >= 1000000
  and (.price_change_percentage_24h_in_currency != null)
)) |
{
  total: length,
  green: ([.[] | select(.price_change_percentage_24h_in_currency > 0)] | length),
  median_top50: ([.[0:50][].price_change_percentage_24h_in_currency] | sort | .[(length/2|floor)]),
  btc: (.[] | select(.symbol=="btc") | {p:.current_price, c24:.price_change_percentage_24h_in_currency, c7:.price_change_percentage_7d_in_currency}),
  eth: (.[] | select(.symbol=="eth") | {p:.current_price, c24:.price_change_percentage_24h_in_currency, c7:.price_change_percentage_7d_in_currency}),
  sol: (.[] | select(.symbol=="sol") | {p:.current_price, c24:.price_change_percentage_24h_in_currency, c7:.price_change_percentage_7d_in_currency})
}
