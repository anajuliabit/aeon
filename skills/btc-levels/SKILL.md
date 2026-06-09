---
name: BTC Levels Monitor
description: Watch BTC price against hard monitoring levels for the leveraged cbBTC position and alert on level crossings
commits: true
permissions:
  - contents:write
var: ""
tags: [crypto]
---

## Purpose

Advisory monitoring of BTC price against the hard levels set by the 2026-06-09
investment-advisor report (risk_leverage · market_macro · news_social, conf 80%)
for the leveraged cbBTC position:

| Level | Meaning | Alert |
|---|---|---|
| BTC spot ≤ $45,000 | Leverage-review trigger. Inside $40,000–$45,000 the cbBTC borrow health factor ≈ 1.48–1.66; below $40,000 it is WORSE than ~1.48 — say which case applies | 🚨 urgent, every run while spot ≤ $45,000 (fires on the baseline run too) |
| Daily close < $60,500 (UTC) | Downtrend continuation signal | ⚠️ once per qualifying daily close (max 1/day) |
| Spot reclaims $63,500 | First stabilization signal | ✅ once per reclaim cycle |
| Spot reclaims $65,900 | Stabilization confirmed | ✅ once per reclaim cycle |

Advisory only — never instruct execution. Alerts state levels and context; the
operator decides.

**Known limitation:** this skill samples every 4 hours; transient intra-window
spikes/dips between runs are not seen. That is acceptable for these decision
levels (daily-close and regime semantics). If the operator wants tighter
intraday granularity, enable the existing `price-threshold-alert` skill
(30-minute cadence) with explicit targets alongside this one.

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

**First run (no state file):** initialize from the current fetch. The
leverage-review trigger (spot ≤ $45,000) STILL fires on this baseline run — it
is the position-risk alarm and must never be suppressed. The breakdown and
reclaim alerts are informational regime signals and are NOT fired on the
baseline run: record the current situation in state (set
`breakdownAlertedForClose` to the current close date if that close is already
< $60,500; set the reclaim flags to true if spot is already above the level) so
only future crossings alert.

## Steps

1. **Fetch BTC price data** (public CoinGecko, no auth):
   ```bash
   curl -s --max-time 20 "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=2&interval=daily"
   ```
   - `.prices` contains daily snapshots taken at 00:00 UTC plus one final
     current-price point. Parse deterministically:
     - **Spot** = `.prices[-1][1]` (the current-price point).
     - **Previous completed UTC daily close** = `.prices[-2][1]` (the snapshot
       timestamped at today's 00:00 UTC). Its **close date** =
       the calendar day BEFORE that timestamp's date (a 00:00 UTC snapshot is
       the close of the prior day). Derive it from `.prices[-2][0]`.
   - **Sandbox note:** if curl fails, use WebFetch on the same URL. If both fail,
     log the gap to `memory/logs/` and exit without changing state — never invent
     prices.

2. **Evaluate levels against state** (all comparisons in USD):
   - **Leverage-review trigger:** spot ≤ 45,000 → alert EVERY run while it
     holds, including the baseline run (repetition is intentional — this is the
     position-risk alarm). In the message distinguish: 40,000 ≤ spot ≤ 45,000 →
     "review band, HF ≈ 1.48–1.66"; spot < 40,000 → "BELOW review band, HF
     worse than ~1.48 — urgent". Set `inLeverageReviewBand: true`; reset to
     false when spot > 45,000.
   - **Breakdown:** previous UTC daily close < 60,500 AND
     `breakdownAlertedForClose != <that close date>` → alert once for that
     close (so consecutive red closes each alert once — max 1/day), then set
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
   review trigger at ≤$45k (HF ~1.48–1.66 in the 40–45k band). Not financial
   advice.
   ```
   No alert fired → no notification (quiet runs are the norm).

4. **Persist:** write the updated `memory/btc-levels-state.json`, append a
   one-line entry to `memory/logs/YYYY-MM-DD.md` (spot, close, which alerts
   fired or "none"), commit both directly (chore commit, this is state — not a
   code change).

## Notes

- Health-factor figures in alerts are the advisor's estimates for the
  $40–45k band, not live reads; below $40k state only that HF is worse than
  ~1.48 — do not extrapolate a number.
- Levels are owned by the advisor reports. If a future advisor report sets new
  levels, update this table and the state semantics in the same PR.
