## reppo-trading-agent

**Gate decision:** RUN — orchestrator `reppo-plan` block set `reppo-trading-agent: RUN` (datanet 9 TradingGym AI ACTIVE & valid; re-run safe via content-hash dedup).

**Rubric:** `datanet_id: "9"`, `mint_cap: 1`, `vote_cap: 3`. Not a placeholder.

### Strategies selected to mint (1 of 1 cap)
- **RSI(14) crossover swing — BTC/USDT, 4h** — hash `57a0b26ed3f90010…`
  - Explicit entry: long when RSI crosses up through 30; short when RSI crosses down through 70.
  - Explicit exit: 1% stop-loss / 2% take-profit per trade.
  - Instrument + timeframe: BTC/USDT, 4-hour. Risk rule: 1% stop-loss. Non-trivial mechanical rule set.
  - Source: [Medium — RSI Crossover Strategy](https://medium.com/@AtomicScript/episode-3-rsi-crossover-strategy-1273d8b3f290) (backtest cited: 25 trades, 60% win, profit factor 2.09).
  - Ledger "Minted strategies" table is empty → no dedup hit. Intent: `.pending-reppo/mint-57a0b26ed3f90010.json`.

### Pods selected to vote on (3 of 3 cap)
- **Pod 257** "HotBot v3 — Trade Exec and Learning" → **like (YES)** — content names a concrete strategy (`Ts24_2`: 1h swing, 4h EMA trend filter, 3% pullback to EMA50, 24h soft time stop); specific and falsifiable.
- **Pod 300** "Ship Trades to Reppo — Open Pod Pipeline" → **dislike (NO)** — off-topic: a data-format/pipeline framework, not a trading strategy.
- **Pod 46** "Sairen - OpenAI Gym" → **dislike (NO)** — off-topic: a software library/RL environment, not a strategy.

### Skipped / notes
- Voting capped at 3; other framework/signal-dump pods (e.g. 150, 332) not voted on due to `vote_cap`.
- No prompt-injection attempts encountered in scraped sources.

## Summary
- **Gate:** RUN for datanet 9.
- **Minted:** 1 intent — RSI(14) crossover BTC/USDT 4h swing strategy.
- **Voted:** 3 intents — pod 257 like, pods 300 & 46 dislike (1 YES, 2 NO).
- **Files created:** `.pending-reppo/mint-57a0b26ed3f90010.json`, `.pending-reppo/vote-257-like.json`, `.pending-reppo/vote-300-dislike.json`, `.pending-reppo/vote-46-dislike.json`; appended `### reppo-trading-agent` entry to `memory/logs/2026-05-22.md`.
- **Follow-up:** `scripts/postprocess-reppo.sh` executes the 4 intents on-chain after this skill finishes. One stray temp file `.hashinput.tmp` remains in repo root (used for hashing; `rm` is sandbox-blocked) — harmless, safe to delete.

## Execution Results

_postprocess-reppo.sh skipped ALL writes: REPPO_PRIVATE_KEY is not set. No intents were executed on-chain._
