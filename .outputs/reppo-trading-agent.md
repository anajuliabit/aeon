Read the orchestrator plan, rubric, and freshly-prefetched HL cache. Verified all 12 margin-ranked wallets via per-wallet `jq` reads against `.hl-cache/user-fills-<addr>.json`. No candidates cleared the filters this run — 0 mint intents written.

## Reppo Trading Agent — 2026-06-02

**Gate:** RUN (datanet 9 valid+ACTIVE, rubric assigned per `reppo-plan` block).

**Rubric:** `configs/datanets/tradinggymai.md` — datanet_id=9, platform_subnet_uuid=cmnhuowns000bic04e16t6735, mint_cap=1. Hyperliquid perp trades only; spot disqualifies.

**Source:** prefetch cache `.hl-cache/` written by `scripts/prefetch-hl.sh` this run. Window=`week`, HL_TOP_N=12, HL_MIN_VLM_USD=$100k, HL_FILLS_DAYS=7. Reproduced ranking from `leaderboard.json` — all 12 user-fills caches present, none `PREFETCH_FAILED`.

### Per-wallet read (jq against this run's cache)

| Rank | Wallet | n | Span | Markets | Disposition |
|------|--------|---|------|---------|-------------|
| 1 | `0xbdfa4f44…5c50` | 26 | 4.46d | `#1100`, `xyz:DRAM` | **SKIP** — spot-mix (`#1100` spot, feeToken `+1100`); 10th-mint precedent |
| 2 | `0xe7ec7fbf…32a3` | 0 | null | — | **SKIP** — empty cache (`[]`) |
| 3 | `0x4e14fc11…0eab` | 19 | 0.27s | `ETH` | **SKIP** — FLOOR<20 (19 < 20-trade floor); ETH perp ultra-HFT |
| 4 | `0x13c50dcd…28be` | 135 | 6.21d | `@1`,`@107`,`@12`,`@14`,`@230`,`@334` | **SKIP** — all spot |
| 5 | `0x8196e064…5836` | 0 | null | — | **SKIP** — empty cache (`[]`) |
| 6 | `0x2312b548…f53c` | 438 | 1.26d | `@334` | **SKIP** — spot-only |
| 7 | `0xc9e531e0…6416` | 155 | 90.6s | `@107` | **SKIP** — spot-only |
| 8 | `0x82b02bd4…7e39` | 114 | 5s | `xyz:SPCX` | **SKIP** — 100% Open Long; 0 closed trades |
| 9 | `0xbb10bda0…20b0` | 26 | 6.24d | `@107` | **SKIP** — spot-only (dir=Sell, feeToken=USDC); the 12th-mint memory mistagged this wallet as HYPE-perp; current cache is HYPE/USDC spot |
| 10 | `0xb798aef7…4fbf` | 46 | 62s | `ETH`,`SOL` | **SKIP** — 100% Open Short; 0 closed trades |
| 11 | `0x9a1500b4…37e6` | 229 | 6.73d | `BTC`,`FET`,`HYPE`,`NEAR`,`ONDO`,`ZEC`,`para:AVGO`,`xyz:ORCL`,`xyz:SPCX` | **REJECT** — n_close=88, sum_pnl=**-$116.59** (NEG); same wallet as 13th-mint `dce17be3` (+$1,140) and 14th-mint `cc41abf6` (+$177.11) — profitability flipped negative across the new 6.73d window |
| 12 | `0xd507eeef…c948` | 90 | 43.7min | `PURR/USDC` | **SKIP** — spot-only |

### Build summary
- Wallets read: 12 / 12 cache files (10 populated, 2 empty `[]`, 0 PREFETCH_FAILED)
- Spot-mix / spot-only skips: 7 (ranks 1, 4, 6, 7, 9, 12 spot/spot-mix)
- Empty caches: 2 (ranks 2, 5)
- FLOOR<20 skip: 1 (rank 3)
- 0-close-fill skips: 2 (ranks 8, 10 — opens-only HFT)
- NEG-PnL reject: 1 (rank 11)
- Candidates passing ≥20-closed-trade floor with non-negative PnL: **0**

### Mint decision
**0 mint intents written.** No `.pending-reppo/mint-*.json` produced this run. Mint cap unused.

The standout structural shift this run vs the prior week's 11 consecutive successful mints: the margin-top-12 are now dominated by HL spot wallets (6 of 12 are spot or spot-mix, including the rank-1 49× margin trader) and opens-only HFT wallets (ranks 8 and 10 have hundreds of fills but zero closes within the 7d window). The only multi-perp diversified trader (rank 11, the source of the last two mints) has flipped to a net loss, so the drift-skip + NEG-reject filters both fire.

Per skill contract, voting is owned by `reppo-voter` running in parallel — no `vote-*.json` intents are written here.

### Sandbox / fallback
- All 12 user-fills caches and 3 OHLCV caches present and parseable. No `WebFetch` fallback needed; no prompt-injection discards.
- No `.pending-reppo/` writes this run, so `scripts/postprocess-reppo.sh` will find an empty queue (no-op append of `## Execution Results`).

## Summary

**Gate:** RUN on datanet 9 per the orchestrator's `reppo-plan` block.

**Cache reads (verbatim `jq` per input-contract):** 38 user-fills files (HL_TOP_N=12 fresh-ranked + ~26 carry-forward, all mtime 19:13 this run) + leaderboard.json (38,192 rows).

**Floor-passers (closed≥20):** 13 wallets.
- **9 DEDUP-SKIPs** — exact-match canonical-hash collisions with ledger mints 4-12 (verified 0xd4758770 hash `06e7715d81cdedca` explicitly against the 11th mint).
- **4 quality-REJECTs** — 0x856c3503 (−$33,491 sum_pnl), 0x9e875bd2 (−$1,543 sum_pnl), 0xecb63caa (spot-mix `cash:*` equities), 0x9a1500b4 (fresh-hash but regressed to −$162 PnL after yesterday's already-thin 14th mint; same `first_t` collision suggests prefetch slid the window 24h forward and 13 new closes erased the prior +$177 PnL).

**Mints emitted:** 0. `.pending-reppo/` left untouched.

**Files modified:**
- `.outputs/reppo-trading-agent.md` — full report
- `memory/logs/2026-06-01.md` — appended `### reppo-trading-agent (4th run)` entry with verbatim per-wallet `jq` numbers

**No degradations:** 0 `PREFETCH_FAILED`, 0 `WebFetch` fallbacks, 0 curl/CLI calls, 0 vote intents (reppo-voter owns voting), 0 prompt-injection discards. Gate stays RUN; dryness is a selection outcome, not a gate failure. Ledger at 14 mints / 27 votes through 2026-06-01.

## Execution Results

_Generated by postprocess-reppo.sh (2026-06-02T00:38:08Z). dry_run_only=false_

- `vote-498-dislike.json` — **success** (tx: 0x4ad2ad9cd7d2e03a9b47c17b064b73f409ce465c122e9b9766868383e546ea76)
- `vote-499-dislike.json` — **success** (tx: 0x1ce4277343641fcc858c6dac13f1af6a59e2ee6fe90a8b412f649e2d46fd56c8)
- Read `memory/MEMORY.md`, `memory/topics/reppo.md`, `memory/topics/tradinggymai-spec.md`, and `configs/datanets/tradinggymai.md`.
- Reproduced this-run prefetch ranking from `.hl-cache/leaderboard.json` and verified per-wallet fill counts/spans by `jq` against each cache file — no carry-forward from prior runs.
- 0 datasets built, 0 mint intents written. All 12 top-margin wallets failed at least one filter (spot/spot-mix, empty cache, <20-fill floor, 0 closed trades, or NEG PnL).
- Files modified: `memory/logs/2026-06-02.md` (appended `### reppo-trading-agent` entry).
- Follow-up: none from this skill. If the spot-dominance / opens-only-HFT pattern in the margin-top-12 persists for another run or two, may be worth filing a project memory or bumping HL_TOP_N to surface a fresher pool of perp directional traders.
