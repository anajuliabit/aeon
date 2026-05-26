---
datanet_id: "9"
agent: reppo-trading-agent
mint_cap: 1
vote_cap: 3
---
# TradingGymAI — Datanet Rubric

Canonical contributor spec: `memory/topics/tradinggymai-spec.md`
(operator-shared 2026-05-26).

## Goal
Collect Hyperliquid perp trading data — real trades or high-fidelity
replays using actual Hyperliquid OHLCV — to train the next generation of
AI trading agents. A good pod is a clean, labeled dataset (JSON or CSV)
of trades plus the signal that fired, the outcome, the aggregate metrics,
and the market context. Quality beats quantity — EVOF scores cleaner,
better-labeled data higher.

## Mint criteria — a pod earns a mint if ALL hold
The pod is a Hyperliquid perp trading dataset (JSON or CSV with clearly
labeled fields/headers) that includes:
- **Trade details**: market, direction, size, leverage, fill price
- **Signal**: why each trade was entered (setup, indicator, pattern)
- **Outcome**: PnL, win/loss, hold duration
- **Metrics**: win rate, Sharpe ratio, max drawdown (aggregate across
  the dataset)
- **Market context**: at least one of trending-up, trending-down,
  ranging, high-volatility, low-liquidity, news-driven
- **Timeframe**: explicit (1m, 5m, 15m, 1H, 4H, daily, etc.)
- **Verification**: timestamps or transaction hashes for fills

The data must be real trades OR a high-fidelity replay using actual
Hyperliquid OHLCV. Strategy descriptions without executed trades, fills,
or backtest results on Hyperliquid OHLCV do NOT qualify. The pod must
not already be in the ledger (`memory/topics/reppo.md`).

## Vote YES if
- The pod meets the mint criteria above.
- Fields are clearly labeled (JSON keys or CSV headers).
- Trades are verifiable (timestamps or tx hashes).

## Vote NO if
- The pod is a strategy description without executed trades or a
  backtest on real Hyperliquid OHLCV.
- Required fields are missing (no PnL, no aggregate metrics, no market
  context, no verification, etc.).
- Trades are unverifiable (no timestamps, no tx hashes).
- The market is not Hyperliquid perps.
- Data is unlabeled (raw dump with no schema, no headers, no keys).
- It is spam, an advertisement, or duplicated content.

## Red flags (never mint / always NO)
- Promises of guaranteed returns or "risk-free" profit.
- Pump-and-dump, insider, or market-manipulation schemes.
- Content that is only a referral link, paid group promo, or token shill.
- Cherry-picked single-trade screenshots with no aggregate metrics.
