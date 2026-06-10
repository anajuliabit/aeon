#!/bin/bash
set -e
cd /home/runner/work/aeon/aeon

TRENDING_SYMS=$(jq -r '.coins[].item.symbol | ascii_upcase' .token-pick-tmp/cg-trending.json | head -15 | tr '\n' '|' | sed 's/|$//')
DEX_SYMS=$(jq -r '.pairs[].baseToken.symbol // empty | ascii_upcase' .token-pick-tmp/dex-trending.json | sort -u | tr '\n' '|' | sed 's/|$//')

BTC7=$(jq -r '.[] | select(.symbol=="btc") | .price_change_percentage_7d_in_currency' .token-pick-tmp/cg-markets.json)
ETH7=$(jq -r '.[] | select(.symbol=="eth") | .price_change_percentage_7d_in_currency' .token-pick-tmp/cg-markets.json)

echo "TRENDING: $TRENDING_SYMS"
echo "BTC7: $BTC7  ETH7: $ETH7"
echo

jq --arg trending "$TRENDING_SYMS" --arg dex "$DEX_SYMS" --argjson btc7 "$BTC7" --argjson eth7 "$ETH7" -r '
  ($trending | split("|")) as $T |
  ($dex | split("|")) as $D |
  .[] | select((.market_cap // 0) >= 20000000) |
  . as $c |
  (.symbol | ascii_upcase) as $sym |
  (.price_change_percentage_24h_in_currency // 0) as $p24 |
  (.price_change_percentage_7d_in_currency // 0) as $p7 |
  ((.total_volume // 0) / (.market_cap // 1)) as $vmc |
  [
    (if $p24 > 0 then 1 else 0 end),
    (if $p7 > 0 then 1 else 0 end),
    (if ($p24 > 5 and $p7 > 5) then 2 else 0 end),
    (if ($T | index($sym)) then 2 else 0 end),
    (if $vmc >= 0.20 then 3 elif $vmc >= 0.10 then 2 else 0 end),
    (if ($p7 > $btc7 and $p7 > $eth7) then 2 else 0 end),
    (if ($D | index($sym)) then 1 else 0 end)
  ] as $parts |
  ($parts | add) as $score |
  "\($score)\t\($sym)\t\(.id)\t$\(.current_price)\t24h:\($p24|tostring|.[0:6])%\t7d:\($p7|tostring|.[0:6])%\tmcap:$\((.market_cap/1000000)|floor)M\tvol:$\((.total_volume/1000000)|floor)M\tvmc:\($vmc|tostring|.[0:5])\ttrending:\(($T | index($sym))!=null)\tdex:\(($D | index($sym))!=null)\tparts:\($parts|tojson)"
' .token-pick-tmp/cg-markets.json | sort -rn -k1 | head -30
