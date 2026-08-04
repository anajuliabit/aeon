## Summary

**btc-levels run — 2026-08-04T12:16Z**

- **Spot:** $63,783.85
- **Previous daily close (2026-08-03):** $63,465.20

**Level evaluation:**
| Level | Threshold | Result |
|---|---|---|
| Leverage-review | spot ≤ $45,000 | Clear — spot $63.8k |
| Breakdown | close < $60,500 | Clear — close $63.5k |
| Reclaim $63,500 | spot ≥ $63,500 + flag=false | Already flagged — no new alert |
| Reclaim $65,900 | spot ≥ $65,900 + flag=false | Not reached |

**No alerts fired — quiet run.** No notification sent. State and log committed (`bd53d1a`).
