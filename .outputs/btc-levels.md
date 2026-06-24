## Summary

**btc-levels run — 2026-06-24T16:38Z**

- **Spot**: $60,319.53 | **Daily close** (2026-06-23): $62,651.93

**Level evaluation:**
| Level | Result |
|---|---|
| ≤ $45,000 leverage-review trigger | Not triggered |
| Daily close < $60,500 breakdown | Not triggered (close $62,651 ≥ $60,500) |
| Reclaim $63,500 | Re-armed — spot dipped below $60,500 |
| Reclaim $65,900 | Re-armed — spot dipped below $60,500 |

**Alerts fired: none** → No notification sent (quiet run per spec).

**State changes:** Both `reclaim63500Alerted` and `reclaim65900Alerted` were reset to `false` (spot completed a full round-trip below $60,500). Next time spot reclaims $63,500 or $65,900, the alerts will fire again.

**Watch:** Spot at $60,319 is below the $60,500 breakdown threshold. If today's UTC daily close (2026-06-24) settles below $60,500, the breakdown alert will fire on the next run.
