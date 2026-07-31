def stables: ["tether","usd-coin","dai","first-digital-usd","usde","tusd","usdd","pyusd","fdusd","paxg","ethena-usde","usds","susd","frax","lusd","gusd","usdp","usdb","crvusd","usd0","usdy","ondo-us-dollar-yield","paypal-usd","binance-usd","usd0-liquid-bond","tether-gold","ripple-usd","true-usd","gemini-dollar","dola-usd","xaut","staked-usde","mountain-protocol-usdm","usd-usde","resolv-usr","world-liberty-financial-usd","falcon-finance-usdf"];
def sym_is_stable(s): (s|ascii_upcase) as $u
  | ($u|startswith("USD")) or ($u|startswith("EUR")) or ($u|startswith("GBP"))
    or $u=="DAI" or $u=="FDUSD" or $u=="TUSD" or $u=="USDE" or $u=="PYUSD" or $u=="FRAX" or $u=="LUSD" or $u=="CRVUSD" or $u=="XAUT" or $u=="PAXG" or $u=="RLUSD";
map(select(
  (.total_volume // 0) >= 1000000 and
  (stables | index(.id) | not) and
  (sym_is_stable(.symbol) | not) and
  ((.name // "" | ascii_downcase | contains("stablecoin")) | not) and
  (.price_change_percentage_24h_in_currency != null)
)) as $filtered
| {
    count: ($filtered | length),
    winners: ($filtered | sort_by(-.price_change_percentage_24h_in_currency) | .[0:12] | map({symbol,name,id,rank:.market_cap_rank,price:.current_price,pc1h:.price_change_percentage_1h_in_currency,pc24h:.price_change_percentage_24h_in_currency,pc7d:.price_change_percentage_7d_in_currency,vol:.total_volume,mcap:.market_cap})),
    losers: ($filtered | sort_by(.price_change_percentage_24h_in_currency) | .[0:12] | map({symbol,name,id,rank:.market_cap_rank,price:.current_price,pc1h:.price_change_percentage_1h_in_currency,pc24h:.price_change_percentage_24h_in_currency,pc7d:.price_change_percentage_7d_in_currency,vol:.total_volume,mcap:.market_cap})),
    top100_positive: ($filtered | .[0:100] | map(select(.price_change_percentage_24h_in_currency>0)) | length),
    top100_total: ($filtered | .[0:100] | length),
    top50_median: ([$filtered | .[0:50] | .[].price_change_percentage_24h_in_currency] | sort | .[25])
  }
