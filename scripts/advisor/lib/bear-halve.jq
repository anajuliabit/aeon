# BEAR regime halving for short-term trades. Single source of truth, shared by
# run.sh (regime BEAR branch) and selftest.sh so they can't drift apart.
# Input/Output: {trades:[{side, sizeUsd, sizePctNet, ...}, ...]}.
# LONG trades are halved (size + pct) and tagged .regimeHalved=true; SHORTs pass
# through untouched. F4: a halved long floors DOWN to 0 — flooring dust to 0 makes
# downstream staging SKIP it (zero-sized trades are dropped at staging), the
# defensive behavior we want in a downtrend. (The old min-1 floor predated that
# skip — it only existed to dodge a now-removed $1000 default — and perversely kept
# $1 dust longs alive in BEAR, inverting the de-risk.)
# Side is lowercased so a "Long"/"LONG" value still buckets as a long.
{
  trades: [
    .trades[]
    | if ((.side // "long") | ascii_downcase) == "long"
      then
        .sizeUsd = ((.sizeUsd // 0) / 2 | floor)
        | .sizePctNet = (((.sizePctNet // 0) * 10 / 2 | round) / 10)
        | .regimeHalved = true
      else .
      end
  ]
}
