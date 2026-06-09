---
name: BTC Levels Monitor
description: Watch BTC price against hard monitoring levels for the leveraged cbBTC position and alert on level crossings
var: ""
tags: [crypto]
---

## Purpose

Advisory monitoring of BTC price against the hard levels set by the 2026-06-09
investment-advisor report (risk_leverage · market_macro · news_social, conf 80%)
for the leveraged cbBTC position:

| Level | Meaning | Alert |
|---|---|---|
| BTC $40,000–$45,000 (spot) | Leverage-review trigger — cbBTC borrow health factor ≈ 1.48–1.66 in this band | 🚨 urgent, every run while inside the band |
| Daily close < $60,500 (UTC) | Downtrend continuation signal | ⚠️ once per close-below streak |
| Spot reclaims $63,500 | First stabilization signal | ✅ once per reclaim |
| Spot reclaims $65,900 | Stabilization confirmed | ✅ once per reclaim |

Advisory only — never instruct execution. Alerts state levels and context; the
operator decides.

## State

State lives in `memory/btc-levels-state.json` (commit it after each run):

```json
{
  "updatedAt": "2026-06-09T20:00:00Z",
  "lastSpot": 61200,
  "lastDailyClose": 61850,
  "lastDailyCloseDate": "2026-06-08",
  "inLeverageReviewBand": false,
  "breakdownAlertedForClose": null,
  "reclaim63500Alerted": false,
  "reclaim65900Alerted": false
}
```

If the file does not exist, initialize it from the current fetch with all alert
flags false/null and send no alerts on the first run (baseline run).

## Steps

1. **Fetch BTC price data** (public CoinGecko, no auth):
   ```bash
   curl -s --max-time 20 "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=2&interval=daily"
   ```
   - Spot = last entry of `.prices`; previous UTC daily close = the entry for the
     most recent completed UTC day.
   - **Sandbox note:** if curl fails, use WebFetch on the same URL. If both fail,
     log the gap to `memory/logs/` and exit without changing state — never invent
     prices.

2. **Evaluate levels against state** (all comparisons in USD):
   - **Leverage-review band:** spot ≤ 45,000 → alert EVERY run while in band
     (this is the position-risk trigger; repetition is intentional). Set
     `inLeverageReviewBand: true`; reset to false when spot > 45,000.
   - **Breakdown:** previous UTC daily close < 60,500 AND
     `breakdownAlertedForClose != lastDailyCloseDate` → alert once, then set
     `breakdownAlertedForClose` to that close date. A later close ≥ 60,500
     clears the flag (set null).
   - **Reclaim 63,500:** spot ≥ 63,500 AND `reclaim63500Alerted == false` →
     alert once, set true. Re-arm (set false) when spot < 60,500 (full
     round-trip below the breakdown level, avoids chop-noise around the level).
   - **Reclaim 65,900:** same pattern with its own flag.

3. **Notify** via `./notify` only when at least one alert fired. One concise
   paragraph, e.g.:
   ```
   ₿ BTC levels: spot $61,2k. ⚠️ Daily close $60,1k < $60,500 — downtrend
   continuation signal per 2026-06-09 advisor levels. Leveraged cbBTC position:
   review levels at $40–45k (HF ~1.48–1.66). Not financial advice.
   ```
   No alert fired → no notification (quiet runs are the norm).

4. **Persist:** write the updated `memory/btc-levels-state.json`, append a
   one-line entry to `memory/logs/YYYY-MM-DD.md` (spot, close, which alerts
   fired or "none"), commit both directly (chore commit, this is state — not a
   code change).

## Notes

- Health-factor figures in alerts are the advisor's estimates for the band, not
  live reads; do not present them as current values.
- Levels are owned by the advisor reports. If a future advisor report sets new
  levels, update this table and the state semantics in the same PR.
