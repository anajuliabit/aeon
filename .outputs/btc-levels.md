## Summary

**btc-levels run — 2026-08-08 04:41 UTC**

| Data | Value |
|---|---|
| Spot | $65,010.25 |
| Previous daily close (2026-08-06) | $64,289.46 |

**Level evaluation — no alerts fired:**
- Leverage-review (≤$45k): clear — spot $20k above trigger
- Breakdown (<$60,500 daily close): clear — close $3,789 above threshold
- Reclaim $63,500: already armed (`reclaim63500Alerted: true`) — no new notification
- Reclaim $65,900: spot $889 below level — not yet crossed

No `./notify` sent (quiet run is the norm). State and log committed.
