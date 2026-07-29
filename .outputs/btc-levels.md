## Summary

Ran **btc-levels** at 17:37Z.

**Data fetched:** CoinGecko `market_chart?days=2&interval=daily` succeeded via curl.

| | Value |
|---|---|
| Spot | $63,811.69 |
| Daily close (2026-07-28) | $63,881.94 |

**Level evaluation:**
- Leverage-review (≤$45k): no — spot $63.8k well above trigger
- Breakdown (close <$60,500): no — close $63,882 above threshold
- Reclaim $63,500: no alert — already flagged true from prior run
- Reclaim $65,900: no — spot below level; re-arm condition (spot <$60,500) not met

**No alerts fired. No notification sent.** State updated, log entry appended, committed.
