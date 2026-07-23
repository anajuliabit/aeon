## Summary

**btc-levels 20:51Z** — quiet run.

- **Spot:** $65,074.72
- **Daily close (Jul 22):** $66,077.06

Level checks:
| Level | Result |
|---|---|
| Leverage-review (≤$45k) | Clear — spot $65k well above |
| Breakdown (close <$60.5k) | Clear — close $66,077 above threshold |
| Reclaim $63,500 | Already alerted (`reclaim63500Alerted=true`); re-arm below $60,500 not breached |
| Reclaim $65,900 | Spot $65,074 < $65,900 — below level; no alert |

No alerts fired, no notification sent. State and log committed.
