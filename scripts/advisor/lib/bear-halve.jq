# BEAR regime halving for short-term trades. Single source of truth, shared by
# run.sh (regime BEAR branch) and selftest.sh so they can't drift apart.
# Input/Output: {trades:[{side, sizeUsd, sizePctNet, ...}, ...]}.
# LONG trades are halved (size + pct) and tagged .regimeHalved=true; SHORTs pass
# through untouched. F6: a positive long must never floor below 1 — flooring a
# tiny long to 0 makes downstream staging treat it as "no size" and substitute
# the $1000 default, which is LARGER and un-gated (inverting the halving). So a
# positive long clamps to a minimum of 1; only an already-zero/absent size -> 0.
{
  trades: [
    .trades[]
    | if (.side // "long") == "long"
      then
        .sizeUsd = (if (.sizeUsd // 0) > 0 then ([((.sizeUsd) / 2 | floor), 1] | max) else 0 end)
        | .sizePctNet = (((.sizePctNet // 0) * 10 / 2 | round) / 10)
        | .regimeHalved = true
      else .
      end
  ]
}
