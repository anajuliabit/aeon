# Reppo Trading Agent — 2026-05-22

**Gate:** RUN (orchestrator plan: datanet 9 TradingGym AI active & valid, no run today).

**Rubric:** datanet_id 9, mint_cap 1, vote_cap 3.

## Strategies minted (1 of 1)
- **BTC funding-rate arbitrage (delta-neutral)** — hash `a7ae1f01372c9b1f`.
  Meets all mint criteria: explicit entry (BTC perp funding >0.01%/period →
  long BTC spot + short equal-notional BTC perp), explicit exit (close both
  legs when funding <0.005% or negative), instrument class + timeframe (BTC
  spot/perp, per funding period), risk rules (2-5x leverage with 50% margin
  buffer, stop at >3% basis divergence, rebalance on 5-10% BTC moves).
  Non-trivial and not in the ledger. Source: Gate Learn.

## Votes cast (3 of 3)
- **Pod 257** — `like`. Concrete testable strategy "Ts24_2" with explicit
  entry (EMA20>50, RSI 45-65, price>EMA200) and risk rules (24h time stop,
  5% trailing stop, 8% take profit), plus execution records on Hyperliquid.
- **Pod 332** — `dislike`. Raw signal-scan log only; no explicit
  entry/exit conditions and no risk rules — not implementable as a strategy.
- **Pod 300** — `dislike`. Off-topic: a data-format/pipeline framework for
  submitting pods, not a concrete trading strategy.

## Skipped / notes
- 29 other pods not voted on (vote_cap of 3 reached).
- Scraped sources treated as untrusted; no prompt-injection attempts detected.
