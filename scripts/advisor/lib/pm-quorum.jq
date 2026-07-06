# pm-quorum.jq — deterministic PM-committee aggregator (NO LLM).
#
# Shared by scripts/advisor/run.sh (committee_pm path) and the selftest, so the
# two can't drift apart (same pattern as lib/bear-halve.jq).
#
# Input : array of committee members
#           [{model, ok, latencyMs, recommendations:[rec...]}, ...]
# Arg   : $quorum (int) — minimum number of DISTINCT ok-models that must agree on
#         the same (symbol, direction) for a recommendation to reach consensus.
# Output: {consensus:[rec...], dissent:[rec...]}
#         Recs are grouped by (SYMBOL, direction). Each emitted rec is the first
#         member's rec enriched with:
#           .urgency        — MOST CONSERVATIVE (lowest) urgency across supporters
#           .level          — median level across supporters (nulls/≤0 ignored)
#           .targetPriceUsd — median target/price across supporters
#           .support[]      — distinct models that agreed
#           .consensusPct   — round(support / ok-member-count * 100)
#         Groups with support ≥ $quorum go to .consensus; everything else (incl.
#         single-member recs) goes to .dissent — nothing is dropped.
def urg2n: ({"low":1,"medium":2,"high":3}[(. // "low") | ascii_downcase] // 2);
def n2urg: ["low","medium","high"][(. - 1)] // "medium";
def median:
  (map(select(. != null and . > 0)) | sort) as $s
  | ($s | length) as $l
  | if $l == 0 then null
    elif ($l % 2) == 1 then $s[($l / 2 | floor)]
    else (($s[$l/2 - 1] + $s[$l/2]) / 2) end;

([.[] | select(.ok == true)]) as $ok
| ($ok | length) as $n
| ([$ok[] | . as $m | (.recommendations // [])[] | {model: $m.model, rec: .}]) as $flat
| ( $flat
    | group_by((.rec.symbol // "" | ascii_upcase) + "|" + (.rec.direction // "hold"))
    | map(
        ([.[].model] | unique) as $support
        | ($support | length) as $sc
        | ([.[].rec]) as $recs
        | ($recs[0] + {
            urgency: ([$recs[] | .urgency | urg2n] | min | n2urg),
            level: ([$recs[] | .level] | median),
            targetPriceUsd: ([$recs[] | (.targetPriceUsd // .price // .target)] | median),
            support: $support,
            consensusPct: (if $n > 0 then (($sc / $n * 100) | round) else 0 end)
          }) as $merged
        | {rec: $merged, supportCount: $sc}
      )
  ) as $groups
| {
    consensus: [$groups[] | select(.supportCount >= $quorum) | .rec],
    dissent:   [$groups[] | select(.supportCount <  $quorum) | .rec]
  }
