# Reppo Trading Agent — 2026-06-04 (2nd run)

**Gate**: RUN (datanet 9 valid + ACTIVE per orchestrator `reppo-plan: reppo-trading-agent: RUN`).

**Rubric**: `configs/datanets/tradinggymai.md` → datanet_id `"9"`, mint_cap 1. Goal: labeled Hyperliquid perp trade datasets with PnL/Sharpe/MDD/market context/verification.

## Margin-top-12 audit (per input contract — every count + span jq'd against this-run cache)

Cache mtimes 2026-06-04 06:11:21–27Z (all fresh, all from this-run `scripts/prefetch-hl.sh`). HL_WINDOW=week, HL_TOP_N=12, HL_MIN_VLM_USD=$100k, HL_FILLS_DAYS=7.

| Rank | Wallet | Margin | jq len | jq span (ms) | Closed | sum_pnl | Disposition |
|------|--------|--------|--------|--------------|--------|---------|-------------|
| 1 | 0x36874c19…7342067 | 32.10 | 134 | 9,264,161 | 0 | n/a | **SPOT-only SKIP** — 133 PURR/USDC + 2 Spot Dust Conversion |
| 2 | 0x4e14fc11…007c0eab | 25.09 | 19 | — | 19 | **−$215,804** | **FLOOR<20 + NEG-PnL REJECT** — 19 ETH Close-Long oid-slice |
| 3 | 0x13c50dcd…c7928be | 21.80 | 115 | 305,624,177 | 113 | **−$19,275** | **SPOT-only + NEG-PnL REJECT** — `@1`/`@107`/`@12`/`@14`/`@334` Sell |
| 4 | 0xbdfa4f44…52bf5c50 | 17.20 | 88 | 544,940,636 | 65 | +$28,002 gross | **SPOT-mix REJECT** — single `#1100` Settlement contributes +$40,991.70; perp-only (xyz:COPPER/DRAM/HOOD) = **−$12,990** NEG; rubric red-flag against single-event windfalls |
| 5 | 0xa87a233e…cb5f71b7 | 13.57 | 2 | — | 2 | — | **FLOOR<20 SKIP** — 2 FARTCOIN Close-Short |
| 6 | 0x8196e064…706b5836 | 12.24 | 0 | — | 0 | — | **EMPTY cache** |
| 7 | 0xb798aef7…7ec4fbf | 12.11 | 46 | 61,895 | 0 | — | **OPENS-only SKIP** — 23 ETH + 23 SOL Open Short |
| 8 | 0x82b02bd4…51a37e39 | 10.24 | 114 | 5,064 | 0 | — | **OPENS-only SKIP** — 114 xyz:SPCX Open Long |
| 9 | 0xd507eeef…7b7a59c948 | 9.54 | 90 | 2,623,445 | 90 | +$29,143 | **SPOT-only SKIP** — 90 PURR/USDC Sell |
| 10 | 0xc9e531e0…7286416 | 9.43 | 155 | 90,617 | 155 | +$128,881 | **SPOT-only SKIP** — 155 `@107` Sell |
| 11 | 0xbb10bda0…5d2b20b0 | 9.24 | 24 | — | 24 | +$30,304 | **SPOT-only SKIP** — 24 `@107` Sell (12th-mint wallet flipped HYPE-perp → `@107` spot since 2026-06-01) |
| 12 | 0x9a1500b4…d837e6 | 7.77 | 228 | 525,119,146 | 98 | **−$2,901** | **NEG-PnL + regression REJECT** — same wallet as 13th-mint dce17be3 (+$1,140 / Sharpe 9.98) and 14th-mint cc41abf6 (+$177.11 / Sharpe 0.84); regressed strictly per SKILL.md Step 4.2 |

**Bucket rollup**: 5 SPOT-only SKIPs · 1 SPOT-mix REJECT · 2 OPENS-only SKIPs · 1 EMPTY cache · 1 FLOOR<20 SKIP · 1 FLOOR+NEG REJECT · 1 NEG+regression REJECT.

## Mint intents written

**Zero.** No candidate cleared the rubric. `.pending-reppo/` untouched.

## Skipped / degraded

- 12/12 caches valid (no PREFETCH_FAILED markers); no WebFetch fallback needed.
- No prompt-injection discards (no external sources consulted).
- **8th consecutive dry trading-agent run** on identical structural saturation: spot-token dominance (`@N` / `PURR-USDC` / `#NNNN`), opens-only HFT, single-event Settlement windfalls masking NEG perp PnL, prior-mint wallet 0x9a1500b4 regressed (+$1,140 → +$177 → −$2,901).

## Summary
- Gate RUN cleared; rubric verified (datanet 9, mint_cap 1).
- 0 candidate datasets survived the ≥20-closed-trade floor + NEG-PnL guard + regression guard + spot-only/spot-mix gates.
- 0 mint intents written; `.pending-reppo/` untouched.
- SKILL.md Step 4.2 in-skill quality guard fired correctly on the 0x9a1500b4 re-mint attempt (sum_pnl regressed +$177 → −$2,901 vs prior mint cc41abf6), confirming the guard's design intent against the MEMORY-flagged precedent.
- Log line appended to `memory/logs/2026-06-04.md` under `### reppo-trading-agent (2nd run)`.
- Output also written to `.outputs/reppo-trading-agent.md` for downstream chain consumers.
- Operator follow-ups carried unchanged: prefetch-layer perp-only filter (`coin !~ /^@\d+$|\/USDC$|^#\d+$/`), `HL_MIN_VLM_USD` bump past the spot HFT cluster, or `HL_WINDOW` switch (day/month/allTime) — to make margin-top-12 actually reach perp directional traders instead of saturating on HL-spot HFT.
