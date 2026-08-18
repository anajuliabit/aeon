## Summary

**btc-levels run — 2026-08-18T00:23Z. Quiet.**

| Check | Value | Result |
|---|---|---|
| Spot | $64,418 | Clear — above all review bands |
| Close 2026-08-17 | $64,491 | Clear — above $60,500 breakdown level |
| Leverage-review (≤$45k) | Not triggered | `inLeverageReviewBand` stays false |
| Reclaim $63,500 | Already alerted | Flag stays true, re-arm not triggered |
| Reclaim $65,900 | $64,418 < $65,900 | Not yet reached |

No alerts fired. No notification sent. State and log committed (`aa5ae88`).
