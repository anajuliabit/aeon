## Summary

**btc-levels 16:36Z — quiet run, no notification sent.**

- **Spot:** $59,596 (down $617 from the 12:17Z run's $60,213)
- **2026-06-27 UTC daily close:** $59,943 (< $60,500 breakdown level)

**Level checks:**
| Check | Result |
|---|---|
| Spot ≤ $45,000 (leverage-review) | No — spot $59,596 >> $45k |
| Daily close < $60,500 (breakdown) | Already alerted for 2026-06-27 close — skip |
| Spot ≥ $63,500 (reclaim) | No |
| Spot ≥ $65,900 (reclaim) | No |

Spot is back below $60k and the re-arm condition (spot < $60,500) is active for reclaim flags, but they're already false. State updated and committed.
