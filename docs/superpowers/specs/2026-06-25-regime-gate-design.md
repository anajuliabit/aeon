# Advisor regime gate (risk-on/off) — design

**Date:** 2026-06-25
**Status:** Approved (design); implementation pending
**Author:** Ana (with Claude Code)
**Repo:** aeon
**Issue:** #139 (finding #1 of the finance-advisor review)

## Problem

The investment advisor has no risk-on/off regime awareness. "Flat / no new risk" is
never its default — the PM prompt's *actionability requirement* obliges at least one
forward-looking opportunity every run, so the swarm always seeks a trade. The paper
track record shows the cost: momentum LONGS opened into extended pumps mean-reverted
(−$1.1k, 29% win rate). A regime-gated approach is the single biggest risk-adjusted
return lever in the research (a BTC-regime-gated strategy posts Sharpe 1.27 / −27% DD
largely by being flat ~83% of the time; ref: Artemis).

## Decision

Compute a deterministic BTC risk-on/off score BEFORE the swarm, and make it the master
gate. Settled during brainstorming:

1. **Hard prior + pick filter** (not prompt-only, not display-only): the score is a
   strong PM/analyst prior AND a deterministic guard on pick staging the LLM can't
   override.
2. **4 signals from already-cached data** — no new APIs (on-chain flows are a separate
   issue). Momentum, funding, volatility, sentiment.
3. **BEAR shrinks long size** (halves notional) rather than dropping — keeps every pick
   on the ledger and gradeable, just smaller.
4. **Enforce on day one** (not shadow) — PM prior + size filter live on first deploy.

## Design

### 1. New `scripts/advisor/regime.sh` (pure, deterministic; no LLM, no network)

Reads the already-prefetched cache (`$D/*.json`) and emits ONE JSON object to stdout:
```json
{"score": 0-100, "band": "BEAR|NEUTRAL|BULL|UNKNOWN",
 "signals": {"momentum": N, "funding": N, "volatility": N, "sentiment": N},
 "asOf": "<ISO>"}
```

**Signals (each normalized 0–100, then weighted):**

| Signal | Weight | Source (cached) | Computation |
|---|---|---|---|
| Momentum | 0.40 | `cg-btc.json` (`prices` → daily closes) | latest close vs 7d & 30d simple MAs; above both → ~100, below both → ~0, mixed → ~50 |
| Funding | 0.25 | `hl-funding.json` | neutral funding → ~60; extreme POSITIVE (crowded longs, fragile) *lowers* score; extreme negative (washed out) *raises* it — contrarian |
| Volatility | 0.20 | `cg-btc.json` closes | 14d realized vol (stdev of daily log returns, annualized); low vol → high score, high vol → low (risk-off) via a clamped linear map |
| Sentiment | 0.15 | `fng.json` (Fear&Greed 0–100) | use directly BUT fade extremes: FNG > 80 (greed) caps the sentiment sub-score (overheated), FNG < 20 (fear) floors it up slightly (capitulation) |

Composite `score = Σ weight·signal`, rounded. **Bands:** BEAR ≤ 35 · NEUTRAL 35–60 ·
BULL ≥ 60 (`REGIME_BEAR_MAX=35`, `REGIME_BULL_MIN=60` — env-overridable). All weights are
env-overridable constants (`REGIME_W_MOMENTUM=0.40`, …).

**Graceful degradation:** any missing/unparseable input → that signal is omitted and
weights renormalize over present signals; if <2 signals available → `band:"UNKNOWN"`,
`score:null`. `regime.sh` never exits non-zero in a way that aborts the run (caller treats
failure as UNKNOWN).

No `set -x`. bash-3.2 compatible (selftest runs on macOS). Numerics via `python3`/`jq`
(never hand-rolled float math in pure bash).

### 2. Wire into `scripts/advisor/run.sh` (pre-swarm)

After prefetch, before the analyst loop:
```bash
REGIME_JSON="$(bash scripts/advisor/regime.sh 2>/dev/null || echo '{"band":"UNKNOWN","score":null}')"
REGIME_BAND="$(printf '%s' "$REGIME_JSON" | jq -r '.band // "UNKNOWN"')"
REGIME_SCORE="$(printf '%s' "$REGIME_JSON" | jq -r '.score // "n/a"')"
echo "advisor: regime $REGIME_BAND ($REGIME_SCORE/100)"
```
- **Inject as a datablock** into every analyst + PM prompt (reuse the existing `datablock`
  helper writing `$D/regime.json`): `<<<DATA regime>>> {score,band,signals} <<<END>>>`.

### 3. PM prior (prompt addition to `portfolio_manager.md`)

Add a section ABOVE the actionability requirement (so it gates it):
> **Regime gate (master prior).** A `regime` datablock gives a deterministic BTC risk-on/off
> score (0–100) + band. It overrides the bias toward action:
> - **BEAR** (≤35): default to NO new long risk — favor trims, hedges, stables, and
>   shorts. The mandatory forward-looking opportunity may be a CONDITIONAL re-entry
>   ("if regime flips BULL / BTC reclaims $X") rather than a live long. A live new long
>   requires an explicit override reason naming what the regime score misses.
> - **NEUTRAL** (35–60): new risk allowed but high-bar and half-conviction.
> - **BULL** (≥60): normal sleeve.
> - **UNKNOWN**: proceed as today (no regime data).
> State the regime band + score in your summary's first sentence.

### 4. Pick-size filter (`run.sh` staging, deterministic — the non-overridable guard)

In the short-term-trade sizing + daily-pick staging path: when `REGIME_BAND=BEAR`, **halve
the notional of every `side:"long"` pick** before POST (shorts/hedges unchanged). Log:
`advisor: regime BEAR — halved long X notional $N→$N/2`. NEUTRAL/BULL/UNKNOWN: unchanged.
This is the code-enforced backstop so a model that ignores the prompt still can't stack
full-size longs into a downtrend.

### 5. Report + notify

Add `regime:{score,band,signals}` to the posted advisor report JSON (extend the merge
step), and prepend one line to the Telegram summary: `REGIME: <BAND> <score>/100`.
Dashboard rendering is a follow-up (don't block on UI).

## Testing (`scripts/advisor/selftest.sh`, offline, no network)

`regime.sh` against synthetic `$D` fixtures (write tiny cg-btc/hl-funding/fng JSON to a
temp dir, point regime.sh at it via an env `D` override):
- Strong uptrend (closes rising) + low vol + neutral funding + FNG 55 → **BULL** (≥60).
- Downtrend + high vol → **BEAR** (≤35).
- Extreme greed (FNG 92) caps sentiment → score lower than the same setup at FNG 55.
- Extreme + funding (very positive) lowers score vs neutral funding, same prices.
- Only 1 input present → `band:"UNKNOWN"`, `score:null` (graceful), exit 0.
- Pick-size filter: a BEAR band halves a long pick's notional, leaves a short unchanged
  (extract the filter logic into a testable shell function or inline-eval, like the
  existing `sttrade`/`select_backend` tests).

## Boundaries / rollback

- Touches only: new `scripts/advisor/regime.sh`; `scripts/advisor/run.sh` (regime compute +
  inject + size filter + report field + notify line); `advisor/prompts/portfolio_manager.md`
  (prior); `scripts/advisor/selftest.sh` (tests).
- **Rollback:** set `REGIME_DISABLE=1` (run.sh skips compute → band UNKNOWN → behaves as
  today), or revert the prompt block. No other workflow/skill touched.
- Out of scope: on-chain-flow signals (needs API keys), CVaR sizing (#140), Brier weighting
  (#144), dashboard UI for the regime panel.

## Open assumptions (verify in the plan / a dry run)

- `cg-btc.json` carries ≥30 daily closes for the 30d MA + 14d vol. The prefetch pulls ~90d
  (`prices` array, daily). Confirm the array length + that it's daily-spaced in the plan;
  if shorter, fall back to the longest window available and note it in the signal.
- Weights (0.40/0.25/0.20/0.15) and bands (35/60) are best-effort from the Artemis/research
  priors — env-overridable, tunable after observing real scores. Not load-bearing.
- `hl-funding.json` shape (per-asset vs aggregate funding) — confirm the field path in the
  plan; if BTC funding isn't present, omit the funding signal (renormalize) rather than guess.
