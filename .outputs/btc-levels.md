## Summary

**btc-levels run — 2026-08-11T00:37Z**

- **Spot**: $63,925.49
- **Daily close (2026-08-10)**: $63,915.71

**Level evaluation:**
| Level | Threshold | Result |
|---|---|---|
| Leverage-review | ≤ $45,000 | Not triggered ($63,925) |
| Breakdown signal | Close < $60,500 | Not triggered ($63,915 > $60,500) |
| Reclaim $63,500 | ≥ $63,500, not yet alerted | Already alerted (no re-arm until dip < $60,500) |
| Reclaim $65,900 | ≥ $65,900, not yet alerted | Not reached ($63,925 < $65,900) |

No alerts fired — quiet run. State updated and committed (`memory/btc-levels-state.json`, `memory/logs/2026-08-11.md`). Next alert will fire if spot dips below $60,500 (re-arms reclaim flags + triggers breakdown) or reclaims $65,900.
