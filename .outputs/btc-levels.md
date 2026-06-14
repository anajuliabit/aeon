## Summary

**btc-levels run — 2026-06-14 20:25Z**

Data fetched from CoinGecko (curl succeeded, no fallback needed):
- **Spot:** $63,856.55
- **Previous daily close (2026-06-13):** $64,377.58

Level evaluation:
| Level | Result |
|---|---|
| Spot ≤ $45,000 (leverage-review) | Clear — $63,857 |
| Daily close < $60,500 (breakdown) | Clear — $64,378 |
| Reclaim $63,500 | Already alerted (flag armed) |
| Reclaim $65,900 | Not reached |

**No alerts fired → no notification sent.**

Files updated: `memory/btc-levels-state.json`, `memory/logs/2026-06-14.md`. Committed as `2f0f173`.
