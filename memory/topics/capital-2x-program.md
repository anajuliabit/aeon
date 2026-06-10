# Capital-2× Program (north star)

**Goal: double net worth by 2027-12-31.**

## Envelope
- **Asymmetric portfolio:** protected core (stables reserve, cbBTC structure,
  locked vesting) + risk sleeve **capped at 15–20% of net worth**.
- **Moonshot sub-sleeve (added 2026-06-10):** up to **1% of net worth inside
  the risk sleeve** for the daily token-pick's short-term bets.
  - Per pick **≤0.5%** (HIGH tier) / **≤0.25%** (MEDIUM).
  - Max **2 open** at any time; never top up losers.
  - Taken picks logged in the dashboard journal.

## Product-lens batch (expanded 2026-06-10)
- **Decision journal** — operator actions feed advisor memory via `/api/journal`.
- **Dashboard adds** — stress-test scenarios, equity curve, risk metrics,
  unlock calendar, drawdown band alerts.
- **Quarter-Kelly sleeve sizing** — validator-enforced once ≥20 graded calls.
- **Yield-delta alerts** — on real-yield / incentive-yield positions.

## Infrastructure shipped
- Daily history ledger + pace gauge on the dashboard (`/api/performance`).
- Decision-grade market data in the daily advisor (liquidity, funding,
  FOMC/CPI calendar).
- Recommendation scorecard (`grade-recs.sh`, Mondays).
- Weekly conviction report (`weekly-conviction.yml`, Mondays 12:00 UTC, max
  3 actions with entry/exit/invalidate levels).
- **`skills/btc-levels`** (4-hourly) — alerts on hard-level crossings for
  the leveraged cbBTC position. State: `memory/btc-levels-state.json`.
  Triggers per 2026-06-09 advisor (conf 80%):
  - leverage-review at BTC **$40–45k** (HF ~1.48–1.66)
  - daily close **< $60,500** = downtrend continuation
  - reclaim of **$63,500–$65,900** = stabilization

## Spec
`docs/superpowers/specs/2026-06-09-capital-2x-program-design.md`
