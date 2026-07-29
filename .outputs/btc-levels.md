## Summary

**btc-levels** run at 12:20Z — quiet run, no notifications sent.

- **Spot:** $64,248.02
- **Daily close (2026-07-28):** $63,869.27

**Level checks:**
| Level | Threshold | Result |
|---|---|---|
| Leverage-review | spot ≤ $45,000 | Clear ($64,248) |
| Breakdown | daily close < $60,500 | Clear ($63,869) |
| Reclaim $63,500 | spot ≥ $63,500 AND not yet alerted | Already alerted |
| Reclaim $65,900 | spot ≥ $65,900 | Not yet ($64,248) |

State written to `memory/btc-levels-state.json`, log appended to `memory/logs/2026-07-29.md`, both committed. Next level to watch: $65,900 reclaim on the upside.
