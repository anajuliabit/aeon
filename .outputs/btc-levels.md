## Summary

**btc-levels run — 2026-06-26 09:19Z**

- **Spot:** $60,047.31 (up from $59,827 at the prior 04:00Z run)
- **Previous daily close (2026-06-25):** $59,712.62

**Alert evaluation:**
| Check | Result |
|---|---|
| Leverage-review (spot ≤ $45k) | Clear — spot $60k >> $45k |
| Breakdown (close < $60,500) | Already alerted for 2026-06-25 close — no duplicate |
| Reclaim $63,500 | Spot below $63,500; re-arm condition active (spot < $60,500) |
| Reclaim $65,900 | Same |

No alerts fired → no notification sent. State and log committed (`9cdf55b`).
