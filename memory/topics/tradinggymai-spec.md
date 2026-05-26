# TradingGymAI (Datanet 9) — Contributor Spec

Canonical source: operator-shared 2026-05-26 Telegram message. Preserved
verbatim below so future agents have the ground-truth, even if downstream
rubrics drift.

## Operator message (2026-05-26)

> Instructions for Data Contributors
>
> Share your Hyperliquid perp trading data and help train the next
> generation of AI trading agents. Include:
> - Trade details: market, direction, size, leverage, fill price
> - Your signal: why you entered (setup, indicator, pattern)
> - Outcome: PnL, win/loss, hold duration
> - Metrics: win rate, Sharpe ratio, max drawdown
> - Market context: trending-up, trending-down, ranging, high-volatility,
>   low-liquidity, news-driven
> - Timeframe: 1m, 15m, 1H, 4H, etc.
> - Verification: timestamps or transaction hashes
>
> Quality: Real trades OR high-fidelity replay using actual Hyperliquid
> OHLCV. JSON/CSV with clear labels. The cleaner your data, the higher
> your EVOF score. Quality beats quantity.

## Implications for the reppo-swarm chain

The pre-2026-05-26 rubric (`configs/datanets/tradinggymai.md`) asked for
strategy specs (entry/exit/risk rules, instrument+timeframe, non-trivial).
All 3 on-chain mints to date (Supertrend 8d478…, Ichimoku da7a3…, TTM
Squeeze 3abb4…) are strategy descriptions with no executed trades, no
PnL/Sharpe/MDD, no Hyperliquid OHLCV replay, no fill data. They pass the
old rubric but score poorly on EVOF under the real datanet criteria.

The aligned rubric (post-PR landing today) requires labeled trade datasets
(JSON or CSV) with all fields above. Expect mint cadence to drop — finding
X/Reddit posts that include backtest results with full metrics on
Hyperliquid OHLCV is much rarer than finding strategy descriptions.

## Vote-side implications

Pod voting under the new rubric:
- YES pods must be Hyperliquid-perp datasets with labeled trades, PnL,
  metrics, market context, and verification.
- NO for strategy-description pods (most of what's in the pod cache today
  — HotBot v4 raw exports, pipeline framework docs).
- NO for any pod not on Hyperliquid perps.
