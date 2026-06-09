# Capital-2× Program — Design Spec

**Date:** 2026-06-09
**Repos:** `anajuliabit/investiments` (data + dashboard), `anajuliabit/aeon` (advisor + automation)
**Approved approach:** Ledger first (Approach 1), phases 1+2 in parallel, then 3, then 4.

## Goal

Double net worth (`snapshot.totalUsd`) by **2027-12-31** (~+56%/yr required pace from
2026-06-09). Risk envelope is **asymmetric**: a protected core (stables, the cbBTC
borrow structure at current exposure, locked vesting) plus an aggressive **risk sleeve
capped at 15–20% of net worth** (liquid alts + tactical positions). Execution is
**manual, weekly-ish** — the system optimizes for few, high-conviction, accountable
calls with explicit levels, not high-frequency signals.

## Current state (what exists)

- Live snapshot: Zerion + Hyperliquid + Baseline + Morpho borrows + Sablier vesting
  schedules; analytics (assets, allocation, btc, vesting, reconcile). Single
  `cache/snapshot.json`, overwritten per refresh — **no history**.
- Advisor (daily 13:00 UTC, claude-fable-5 on Claude subscription, Virtuals fallback):
  5 analysts + debate + PM; data = DefiLlama yields/fees/protocols, CoinGecko
  global/BTC/held-token, Fear&Greed, X search. **No liquidity/volume, funding,
  unlock-calendar, or macro-calendar data. No memory of past recommendations.**
- Alerts: btc-levels skill (4-hourly hard levels), notify-vesting (claims/unlocks).

## Phase 1 — History ledger + performance (investiments)

**`history-store.ts`** (new): `recordDay(snapshot, dir)` upserts one JSON line per UTC
day into `history.jsonl` (atomic rewrite, same pattern as cache-store). Entry:

```json
{"date":"2026-06-09","totalUsd":0,"grossAssetsUsd":0,"totalLiabilitiesUsd":0,
 "stableUsd":0,"btcQty":0,"btcPriceUsd":0,"healthFactor":null,
 "topAssets":[{"symbol":"cbBTC","valueUsd":0}],
 "vestingLockedUsd":0,"vestingClaimableUsd":0}
```

Same-day refreshes overwrite that date's entry (latest wins). Called from the server's
refresh path after a successful snapshot write.

**`performance.ts`** (new, pure): given the ledger + a baseline entry, compute:
- `pnl`: 1d/7d/30d/since-baseline absolute + %.
- `maxDrawdownPct` (peak-to-trough on totalUsd).
- `benchmark`: BTC buy-and-hold — `(baseline.totalUsd / baseline.btcPriceUsd) ×
  latest.btcPriceUsd` vs actual totalUsd.
- `pace`: target = `2 × baseline.totalUsd` at 2027-12-31; trajectory value today =
  `baseline.totalUsd × 2^(elapsedDays/totalDays)`; report on/off pace delta and
  required CAGR from today.

**Endpoints:** `GET /api/history?days=N` (ledger slice), `GET /api/performance`
(computed object). Same Basic-auth guard as the rest.

**Dashboard:** PERFORMANCE panel — pace gauge (actual vs trajectory), PnL row,
benchmark-vs-BTC line, max drawdown. Renders only when history has ≥ 2 entries.

**Durability:** `HISTORY_DIR` env (default `cache/`). Railway's filesystem is
ephemeral — **operator action: attach a Railway volume and set `HISTORY_DIR` to its
mount path**, otherwise history resets on each deploy (server logs a warning when
`HISTORY_DIR` is unset in production). Baseline overridable via `BASELINE_USD` +
`BASELINE_DATE` env for continuity if the ledger ever resets.

## Phase 2 — Decision-grade market data (aeon)

Prefetch additions in `scripts/advisor/prefetch-data.sh` (all keyless/public):
- **GeckoTerminal** top pools for MAMO + REPPO (Base): liquidity USD, 24h volume →
  `gt-liquidity.json`. Generic: derived from held micro-caps where a pool exists.
- **Hyperliquid funding**: `POST https://api.hyperliquid.xyz/info`
  (`metaAndAssetCtxs`) → BTC/ETH funding rates → `hl-funding.json`.
- **DefiLlama emissions/unlocks** for held tokens where listed → `unlocks.json`.
- **Macro calendar**: static curated `advisor/data/macro-calendar.json` (FOMC + US CPI
  dates 2026–2027, sourced from the Fed/BLS published schedules); prefetch filters to
  the next 14 days → `macro-upcoming.json`.

Datablock + prompt updates:
- `fundamentals` + `yield_allocation`: liquidity/volume block; **any trim/sell call on
  a micro-cap must state position size in days-of-daily-volume** and respect the
  locked/liquid split (already enforced).
- `market_macro`: funding rates + upcoming macro events.
- `risk_leverage`: funding (carry cost context for the cbBTC loan) + macro events.

## Phase 3 — Recommendation scorecard

- **PM prompt**: each recommendation gains structured fields:
  `{title, action, urgency, confidence, symbol?, direction: "increase"|"decrease"|
  "hold"|"hedge", level?: number, invalidateLevel?: number, horizonDays: 30|60|90}`.
- **investiments**: recommendations are already persisted per day (advisor-store).
  New `GET /api/advisor/scorecard` returns graded history + per-analyst accuracy.
  `POST /api/advisor/scorecard` upserts grades (auth-guarded, written by aeon).
- **aeon grading step** (`scripts/advisor/grade-recs.sh`, deterministic, weekly via the
  Monday workflow): for each rec older than its horizon and ungraded — fetch the
  symbol's price then/now (CoinGecko historical) and grade by direction correctness:
  price moved in the called direction ≥5% = hit, opposite ≥5% = miss, else neutral.
  `hold` grades neutral unless that asset drew down >25% (miss). Portfolio-level recs
  (no symbol) grade against totalUsd vs the pace trajectory. POST grades back;
  accumulate per-analyst tallies (recs carry their source analysts).

## Phase 4 — Weekly conviction report (aeon)

New workflow `weekly-conviction.yml` (Mondays 12:00 UTC, before the daily run):
prefetch (reuse advisor prefetch + history/performance/scorecard endpoints) → single
fable-5 PM-style prompt consuming: last 7 days of findings (from advisor-store),
performance + pace, scorecard accuracy, market data. Output (structured JSON, posted
as report type `weekly` + Telegram):
- **Pace verdict**: on/off trajectory, by how much, required CAGR restated.
- **Max 3 actions**, each: thesis, entry/exit/invalidate levels, size **within the
  15–20% risk sleeve** (sleeve = liquid non-core assets; explicitly excludes locked
  vesting, the stables reserve, and the cbBTC structure), horizon, and what would
  prove it wrong.
- **Risk check**: core untouched? sleeve within cap? upcoming unlocks/macro events
  that gate timing.

investiments: advisor-store accepts `type: "weekly"` reports; dashboard advisor panel
shows the latest weekly above the dailies.

## Review protocol (every phase)

Branch → implement → **multi-agent review Workflow** (spec-fidelity vs this doc,
repo-convention compliance, logic/edge-case review; adversarial verification per
finding; cap verifier fan-out to avoid the wedge seen on 2026-06-09) → fix confirmed
findings → PR → merge → live verification (tests, endpoint probes, or a dispatched
run as applicable).

## Error handling & testing

- All new fetchers: best-effort + isolated (return empty on failure, never throw) —
  matches hyperliquid/baseline/sablier pattern. Missing data degrades to "data
  unavailable" in prompts, never invented numbers.
- bun tests for history-store (upsert/atomicity), performance (pnl/drawdown/pace/
  benchmark math, incl. edge cases: single entry, gaps, baseline override), scorecard
  grading rules; shell scripts get `bash -n` + jq-logic fixtures like notify-vesting.
- Weekly report and grading are idempotent per date (re-runs overwrite, no dupes).

## Out of scope (explicitly)

Execution/automated trading, tax accounting, Unvest schedule integration (no public
indexer), paid data sources, intraday performance granularity.
