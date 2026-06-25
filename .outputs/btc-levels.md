## Summary

**BTC Levels run complete — no alerts fired.**

| Check | Value | Result |
|---|---|---|
| Spot | $59,441 | — |
| Jun-24 daily close | $60,909 | ≥ $60,500 → no breakdown alert |
| Leverage-review (≤$45k) | $59,441 | well above → no |
| Reclaim $63,500 | $59,441 < level | not triggered |
| Reclaim $65,900 | $59,441 < level | not triggered |

Spot ticked up slightly from $59,317 (last run at 16:39Z) to $59,441. The June 24 close held at $60,909, comfortably above the $60,500 breakdown threshold. The binary signal MEMORY flagged — whether today's (June 25) UTC close lands below $60,500 — won't be visible until midnight UTC when the next CoinGecko daily snapshot captures it.

Files committed: `memory/btc-levels-state.json`, `memory/logs/2026-06-25.md`.
