## Summary

**btc-levels run — 2026-07-01 17:03Z**

- **Spot:** $59,846 (up from $58,432 at 12:18Z)
- **Last daily close:** $58,550.75 (Jun 30 UTC)
- **Alerts fired:** none

Level check:
- Leverage trigger (≤$45k): not active
- Breakdown (close < $60,500): close is $58,550 — condition met, but Jun 30 was already alerted at 00:19Z; no re-fire
- Reclaim $63,500: spot $59,846 below level, not met
- Reclaim $65,900: not met

BTC has bounced ~$1,400 from the 12:18Z read ($58,432 → $59,846), still well below the $63,500 stabilization level. State updated (spot), log appended, both committed.
