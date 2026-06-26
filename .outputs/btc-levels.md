## Summary

**Run: btc-levels 2026-06-26T16:51Z**

- **Spot:** $60,064.61 (up from last run's $59,462)
- **Previous UTC daily close (2026-06-25):** $59,712.62

**Level evaluation:**
| Level | Result |
|---|---|
| Leverage review (≤$45k) | Clear — spot well above |
| Breakdown (close < $60,500) | Close qualifies but `breakdownAlertedForClose` already set to "2026-06-25" — no duplicate |
| Reclaim $63,500 | No — spot $60,064 < $63,500 |
| Reclaim $65,900 | No — spot $60,064 < $65,900 |
| Re-arm reclaim flags | Spot < $60,500 → holds both flags false |

No alerts fired. No notification sent. State updated, log appended, committed.
