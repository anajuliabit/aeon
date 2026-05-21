---
datanet_id: "REPLACE_WITH_MAINNET_TRADINGGYMAI_DATANET_ID"
agent: reppo-trading-agent
mint_cap: 1
vote_cap: 3
---
# TradingGymAI — Datanet Rubric

## Goal
Collect concrete, testable crypto/markets trading strategies suitable for
backtesting and reinforcement-learning environments. A good pod describes
a strategy precisely enough that an engineer could implement and evaluate
it without contacting the author.

## Mint criteria — a strategy earns a pod if ALL hold
- It states an explicit entry and exit condition (not just a thesis).
- It names the instrument class and timeframe (e.g. BTC perps, 4h).
- It includes at least one risk rule (stop, sizing, or max exposure).
- It is non-trivial — not "buy low sell high" or pure sentiment.
- It is not already in the ledger (memory/topics/reppo.md).

## Vote YES if
- The pod meets the mint criteria above.
- The strategy is specific, falsifiable, and on-topic for the datanet.

## Vote NO if
- The pod is vague, untestable, or missing entry/exit/risk rules.
- It is off-topic (not a markets trading strategy).
- It is spam, an advertisement, or duplicated content.

## Red flags (never mint / always NO)
- Promises of guaranteed returns or "risk-free" profit.
- Pump-and-dump, insider, or market-manipulation schemes.
- Content that is only a referral link, paid group promo, or token shill.
