[.[] |
  select((.change_1d // null) != null) |
  select((.change_1d // 0) >= -75 and (.change_1d // 0) <= 75) |
  select((.tvl // 0) > 0) |
  select((.category // "") != "CEX" and (.category // "") != "Chain") |
  {chain: .chain, tvl: .tvl, change_1d: (.change_1d // 0), prev_tvl: (.tvl / (1 + (.change_1d // 0) / 100))}] |
group_by(.chain) |
map({
  chain: .[0].chain,
  tvl_now: ([.[].tvl] | add),
  tvl_prev: ([.[].prev_tvl] | add),
  count: length
}) |
map(. + {change_pct: (if .tvl_prev > 0 then ((.tvl_now - .tvl_prev) / .tvl_prev * 100) else 0 end)}) |
sort_by(.tvl_now) | reverse | .[:30]
