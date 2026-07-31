## Summary

**btc-levels run — 2026-07-31T01:09Z**

- **Spot**: $64,927 | **Daily close (2026-07-29)**: $64,722
- **No alerts fired** — all levels clear:
  - Leverage-review ($45k): spot well above, `inLeverageReviewBand` stays false
  - Breakdown ($60,500 daily close): $64,722 comfortably above threshold
  - Reclaim $63,500: already alerted in a prior cycle (`reclaim63500Alerted=true`)
  - Reclaim $65,900: spot $64,927 hasn't crossed — watching
- No `./notify` sent (quiet run is the norm)
- State and log committed (chore commit, `aae98ac`)
