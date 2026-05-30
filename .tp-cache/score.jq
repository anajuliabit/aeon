def trending: ["ALLO","BONK","H","HBAR","HYPE","INJ","LAB","NEAR","PENGU","TAO","VVV","XLM","XMR","ZAMA","ZEC"];
def btc7d: -1.5251662496822833;
def eth7d: -0.7236828031460731;
.[] |
  select(.market_cap != null and .market_cap > 20000000) |
  . as $c |
  ($c.symbol | ascii_upcase) as $sym |
  ($c.price_change_percentage_24h_in_currency // 0) as $p24 |
  ($c.price_change_percentage_7d_in_currency // 0) as $p7 |
  (if ($c.market_cap > 0) then ($c.total_volume / $c.market_cap) else 0 end) as $vmc |
  (trending | index($sym)) as $tr |
  (if $p24 > 0 then 1 else 0 end) as $s1 |
  (if $p7 > 0 then 1 else 0 end) as $s2 |
  (if ($p24 > 5 and $p7 > 5) then 2 else 0 end) as $s3 |
  (if $tr != null then 2 else 0 end) as $s4 |
  (if $vmc >= 0.20 then 3 elif $vmc >= 0.10 then 2 else 0 end) as $s5 |
  (if ($p7 > btc7d and $p7 > eth7d) then 2 else 0 end) as $s6 |
  ($s1 + $s2 + $s3 + $s4 + $s5 + $s6) as $score |
  {sym: $sym, name: $c.name, rank: $c.market_cap_rank, price: $c.current_price, p24: $p24, p7: $p7, mcap: $c.market_cap, vol: $c.total_volume, vmc: $vmc, trending: ($tr != null), score: $score, breakdown: ("p24>0:\($s1) p7>0:\($s2) both>5:\($s3) trend:\($s4) vmc:\($s5) rsBE:\($s6)")} |
  select(.score >= 5)
