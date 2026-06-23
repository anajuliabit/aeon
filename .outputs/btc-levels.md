## Summary

**btc-levels run — 2026-06-23T04:21Z**

- **Spot:** $63,877 | **Daily close (2026-06-22):** $63,957
- All four levels evaluated — no alerts fired:
  - Leverage-review (≤$45k): clear
  - Breakdown (<$60,500 close): clear — close $63,957
  - Reclaim $63,500: already alerted, no re-arm (spot > $60,500)
  - Reclaim $65,900: spot below level, flag already set, no re-arm needed
- No notification sent (quiet run)
- State and log committed to `main`
