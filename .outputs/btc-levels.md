## Summary

**btc-levels run — 2026-06-17 ~09:17Z**

- **Spot:** $64,913.58 (down from $65,817 at last run)
- **Daily close (Jun 16):** $65,598.94

Level evaluation:
- Leverage-review (≤$45k): clear
- Breakdown (close < $60,500): clear — close at $65,598
- Reclaim $63,500: flag already `true`, not re-armed (spot still above $60,500)
- Reclaim $65,900: spot pulled back below $65,900 but flag stays `true` (re-arm requires round-trip below $60,500 to avoid chop-noise)

No alerts fired. No notification sent. State updated and committed.
