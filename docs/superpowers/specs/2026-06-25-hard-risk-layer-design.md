# Hard risk layer — design

**Date:** 2026-06-25
**Status:** Approved (design); implementation pending
**Author:** Ana (with Claude Code)
**Repo:** aeon
**Issue:** #140 (finding #2 of the finance-advisor review)

## Problem

Short-term pick sizing is a flat `5%`-of-net sleeve split conviction-weighted
(HIGH=2× MEDIUM) — `run.sh:487-493`. No volatility targeting (a +40% memecoin is
sized like a major), no per-position cap, no correlation awareness (5 alt-longs all
high-beta to BTC look diversified but converge to beta-1 in a crash), and no
portfolio-drawdown response. LLM trading agents reliably post "high return, huge
drawdown" from exactly this — overconfident, unbounded sizing.

## Decision

Add a deterministic risk layer that replaces the inline sizing with vol-targeted,
hard-capped, drawdown-aware sizing. Settled during brainstorming:

1. **Proxy from cached data** — no new per-asset history fetches. Vol proxy from
   `cg-markets.json` 24h/7d moves; drawdown from `/api/history`. (True
   CVaR/covariance deferred — needs per-asset price history = many rate-limited calls.)
2. **All 4 mechanisms** — vol-target sizing + per-position cap + per-direction
   (correlation) cap + drawdown de-gross.
3. **Per-position overflow: drop the excess** (clamp, don't redistribute) — leans
   smaller/safer, keeps total ≤ budget.
4. **Stack with the regime gate** (#139, shipped) — risk-size sets disciplined sizes;
   THEN the existing regime BEAR long-halving applies on top. Both shrink longs in a
   downtrend, intentionally (defense in depth).

## Design

### 1. New `scripts/advisor/risk-size.sh` (pure, deterministic; numerics in python)

Replaces the inline sizing jq. Inputs (env/args): the `{trades:[{side,conviction,
symbol,coingeckoId,…}]}` array, net worth (`RISK_NET`), current drawdown pct
(`RISK_DD`), and the path to `cg-markets.json` (vol proxies). Output: same array with
`sizeUsd`/`sizePctNet` set + `riskNote` annotations. Never crashes — on missing inputs
it falls back to the current conviction-split (so a data gap can't zero out sizing).
`RISK_DISABLE=1` forces that fallback. No `set -x`.

Constants (all env-overridable): `ST_RISK_PCT=5`, `RISK_DD_TRIGGER=15`,
`RISK_DD_TRIGGER2=25`, `RISK_DD_DEGROSS=0.5`, `RISK_DD_DEGROSS2=0.25`,
`RISK_MAX_POS_PCT=1.5`, `RISK_MAX_DIR_PCT=3.0`, `RISK_VOL_FLOOR=3` (min daily-vol % to
avoid div-by-tiny), `RISK_DEFAULT_VOL=12` (assumed vol for symbols absent from
cg-markets — conservative, sizes them down).

**Mechanisms, applied in this order:**

1. **DD de-gross (budget gate).** `budget = ST_RISK_PCT% × net`. If
   `RISK_DD ≥ RISK_DD_TRIGGER2` (25%) → `budget ×= RISK_DD_DEGROSS2` (0.25);
   else if `≥ RISK_DD_TRIGGER` (15%) → `budget ×= RISK_DD_DEGROSS` (0.5). Log the
   trigger.

2. **Vol-target weights.** Per pick, vol proxy from `cg-markets.json`:
   `vol = max(RISK_VOL_FLOOR, blend)` where `blend = 0.5·|24h%| + 0.5·(|7d%|/sqrt(7))`
   (7d scaled to a daily-equivalent). Symbol not in cg-markets → `vol = RISK_DEFAULT_VOL`.
   Base weight `w = conviction_mult / vol` (HIGH=2, MED=1). Allocate
   `sizeUsd = budget × w / Σw` (floor).

3. **Per-position cap (drop excess).** Clamp each `sizeUsd` to
   `min(sizeUsd, RISK_MAX_POS_PCT% × net)`. Do NOT redistribute the clamped excess —
   total stays ≤ budget, intentionally conservative. Annotate `riskNote:"pos-capped"`.

4. **Per-direction (correlation) cap.** Sum `sizeUsd` over `side=="long"` and over
   `side=="short"` separately. If the long sum > `RISK_MAX_DIR_PCT% × net`, scale ALL
   longs down by `cap/longSum` (proportional); same for shorts independently. This is
   the "don't stack correlated longs" guard — a pragmatic proxy for pairwise
   correlation, treating all same-direction alt exposure as correlated to BTC. Annotate
   `riskNote:"dir-scaled"`.

Recompute `sizePctNet` from the final `sizeUsd` after all four steps, so the displayed
% always matches the dollar amount.

### 2. Wire into `run.sh`

- The advisor already prefetches `cg-markets.json` + `snapshot.json`. Add a `/api/history`
  fetch (reuse `notify-drawdown.sh`'s peak→current jq) to compute `RISK_DD` (current
  drawdown % from the all-time ledger peak); 0 if history too short.
- Replace the inline sizing jq (`run.sh:487-493`) with a call to `risk-size.sh`, passing
  `RISK_NET`, `RISK_DD`, and the trades.
- **Order:** `risk-size.sh` (DD de-gross + vol-target + caps) runs FIRST; the existing
  regime BEAR long-halving (`run.sh:489-497`, shared `lib/bear-halve.jq`) applies AFTER,
  on the already-disciplined sizes. Both reduce longs in a downtrend — intentional
  stacking. Add a comment at the seam documenting the order.
- Add a `risk:{budgetUsd, ddPct, degrossed, maxPosPct, maxDirPct}` block to the posted
  report; add a Telegram line: `RISK: $<budget> sleeve · DD <dd>%<degrossed?>`.

### 3. Testing (`scripts/advisor/selftest.sh`, offline, no network)

Extract the risk math so it's unit-testable (the python core takes JSON in/out). Cover:
- **Vol-target:** two equal-conviction longs, one with |24h%|=5 and one =40 → the calm one
  gets a larger `sizeUsd`.
- **Per-position cap:** a pick that would size to 3% net is clamped to 1.5%; the dropped
  excess is NOT redistributed (others unchanged, total drops).
- **Direction cap:** 5 longs each ~1% net (sum 5% > 3%) scale down so the long sum = 3% net;
  a lone short is untouched.
- **DD de-gross:** `RISK_DD=18` → budget halved vs `RISK_DD=5`; `RISK_DD=30` → quarter.
- **Degrade:** missing cg-markets path / `RISK_DISABLE=1` → output equals the current
  conviction-split (pin against the existing `run.sh:487-493` formula).
- **sizePctNet consistency:** final `sizePctNet` equals `round(sizeUsd/net*1000)/10` after caps.

### Boundaries / rollback

- Touches: new `scripts/advisor/risk-size.sh` (+ a `lib/*.jq` if the cap math is shared);
  `run.sh` (history fetch + sizing swap + report/Telegram); `selftest.sh`.
- `RISK_DISABLE=1` → conviction-split fallback (instant rollback). Regime gate (#139) and
  the swarm untouched.
- **Out of scope:** true CVaR/covariance + pairwise correlation (per-asset history),
  VaR/CVaR dashboard display, applying caps to the daily directional picks (those are
  server-assigned $1k; the variable exposure is the short-term sleeve this sizes).

## Open assumptions (verify in plan / dry run)

- `cg-markets.json` is top-100-by-mcap with `price_change_percentage_24h` +
  `..._7d_in_currency`. A picked symbol outside top-100 → no proxy → `RISK_DEFAULT_VOL`
  (conservative). Confirm the field names + that picks are matched by `coingeckoId`/symbol.
- `/api/history` returns the daily ledger `[{date,totalUsd}]`; drawdown =
  `(runningPeak − current)/peak`. Confirm shape (notify-drawdown.sh uses it).
- Caps/triggers (1.5% / 3% / 15%/25% / 0.5×/0.25×) and the vol blend are best-effort from
  the research priors — env-overridable, tune after observing real sizings in a dry run.
