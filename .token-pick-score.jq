def trending_ids: ["siren-2","bittensor","velvet","spacex-xstocks","pudgy-penguins","venice-token","solana","near","hyperliquid","zcash","monero","aerodrome-finance","sui","official-trump","ondo-finance"];
def dedup: ["WLD","SENT","MORPHO","MON","HUMAN","HOME","HYPE"];

# benchmarks: BTC 7d ~5.19, ETH 7d ~8.48 (from the data)
. as $all |
($all[] | select(.symbol == "btc") | .price_change_percentage_7d_in_currency) as $btc7 |
($all[] | select(.symbol == "eth") | .price_change_percentage_7d_in_currency) as $eth7 |

[ $all[] | select(.market_cap > 20000000) |
  . as $m |
  (.market_cap // 0) as $mcap |
  (.total_volume // 0) as $vol |
  (.price_change_percentage_24h_in_currency // 0) as $p24 |
  (.price_change_percentage_7d_in_currency // 0) as $p7 |
  (if $mcap > 0 then $vol/$mcap else 0 end) as $vmc |
  {
    sym: (.symbol | ascii_upcase),
    id: .id,
    px: .current_price,
    p24: $p24, p7: $p7, mcap: $mcap, vol: $vol, vmc: $vmc,
    dedup: ((.symbol | ascii_upcase) as $s | (dedup | index($s)) != null),
    score: (
      (if $p24 > 0 then 1 else 0 end) +
      (if $p7 > 0 then 1 else 0 end) +
      (if ($p24 > 5 and $p7 > 5) then 2 else 0 end) +
      (if (trending_ids | index(.id)) != null then 2 else 0 end) +
      (if $vmc >= 0.20 then 3 elif $vmc >= 0.10 then 2 else 0 end) +
      (if ($p7 > $btc7 and $p7 > $eth7) then 2 else 0 end)
    ),
    breakdown: [
      (if $p24 > 0 then "24h+1" else empty end),
      (if $p7 > 0 then "7d+1" else empty end),
      (if ($p24 > 5 and $p7 > 5) then "both>+5%+2" else empty end),
      (if (trending_ids | index(.id)) != null then "trending+2" else empty end),
      (if $vmc >= 0.20 then "vmc+3" elif $vmc >= 0.10 then "vmc+2" else empty end),
      (if ($p7 > $btc7 and $p7 > $eth7) then "RS+2" else empty end)
    ] | join("|")
  }
] | sort_by(-.score) | .[0:35] | .[] |
  "\(.score)/9 \(.sym)\(if .dedup then "(DEDUP)" else "" end)\tpx=\(.px)\t24h=\(.p24|tonumber|. * 100 | round / 100)%\t7d=\(.p7|tonumber|. * 100 | round / 100)%\tmcap=\(.mcap/1000000|round)M\tvol=\(.vol/1000000|round)M\tvmc=\(.vmc|. * 1000 | round / 1000)\t\(.breakdown)\t(id=\(.id))"
