# Reppo Swarm — Running Ledger

Append-only audit trail for the reppo-swarm chain. The trading agent reads
the "Minted strategies" table to avoid re-minting; the digest appends to it.
Rows are written ONLY for actions confirmed on-chain (a real tx) — a queued
intent is not a mint.

## Minted strategies
| Date | Datanet | Strategy hash (sha256, first 16) | Source | Tx status |
|------|---------|----------------------------------|--------|-----------|

## Votes cast
| Date | Datanet | Pod id | Direction | Tx status |
|------|---------|--------|-----------|-----------|

## Run history
| Date | Orchestrator | Minted | Voted | Failures |
|------|--------------|--------|-------|----------|
| 2026-05-21 | trading agent SKIP — tradinggymai datanet_id is still the placeholder; prefetch failed | 0 | 0 | 1 |
| 2026-05-22 | trading agent RUN — intents queued but postprocess skipped (REPPO_PRIVATE_KEY unset); 0 executed on-chain | 0 | 0 | 0 |
| 2026-05-22 | trading agent RUN (datanet 9) — 1 mint + 3 vote intents queued; postprocess skipped all (REPPO_PRIVATE_KEY unset); 0 executed on-chain; 14 unassigned datanets | 0 | 0 | 0 |
| 2026-05-22 | trading agent RUN (datanet 9) — 1 mint + 3 vote intents queued; postprocess ran dry-run-only, all 4 dry-runs failed (code UNKNOWN); 0 executed on-chain; 14 unassigned datanets | 0 | 0 | 4 |
| 2026-05-22 | trading agent RUN (datanet 9) — 1 mint (funding-rate carry) + 3 vote intents queued; postprocess ran dry-run-only, all 4 dry-runs failed (code UNKNOWN); 0 executed on-chain; 14 unassigned datanets | 0 | 0 | 4 |
| 2026-05-23 | trading agent RUN (datanet 9) — 1 mint (BTC 1H ORB, hash 1a0f07dc3cd24386) + 3 NO vote intents queued; postprocess ran dry-run-only, all 4 dry-runs failed (code UNKNOWN); 0 executed on-chain; 14 unassigned datanets | 0 | 0 | 4 |
| 2026-05-23 | trading agent RUN (datanet 9) — 1 mint (ETH/USDT 4H Bollinger mean-reversion, hash 60ea32bedbaf0d21) + 3 NO vote intents queued; postprocess dry-run-only: mint failed PUBLISHER_LACKS_SUBNET_ACCESS, 3 votes failed POD_NOT_VALID_FOR_EPOCH; 0 executed on-chain; 14 unassigned datanets | 0 | 0 | 4 |
| 2026-05-24 | trading agent RUN (datanet 9) — 1 mint (BTC perp 4H RSI/MACD/200EMA, hash 9412768ec7f019b5) + 2 of 3 vote intents (LIKE pod 344, DISLIKE pod 345) queued (only 2 pods at epoch 95 after ISS-005 filter); postprocess dry-run-only: mint reverted PUBLISHER_LACKS_SUBNET_ACCESS, vote-344 reverted INSUFFICIENT_VOTING_POWER (new ISS-006), vote-345 hit transient mainnet.base.org RPC error; 0 executed on-chain; 14 unassigned datanets | 0 | 0 | 3 |
| 2026-05-25 | trading agent RUN (datanet 9) — 1 mint (SOL-USDT 1H pullback-to-support multi-confluence long, hash 57d8f1d318d2a28d) + 3 DISLIKE vote intents (pods 300, 363, 364, all epoch 96) queued; postprocess dry-run-only: mint reverted PUBLISHER_LACKS_SUBNET_ACCESS (ISS-004), vote-300 + vote-364 reverted INSUFFICIENT_VOTING_POWER (ISS-006), vote-363 hit transient mainnet.base.org RPC error (2nd occurrence — new ISS-007); 0 executed on-chain; 14 unassigned datanets | 0 | 0 | 4 |
| 2026-05-25 | trading agent RUN re-run (datanet 9) — 1 mint (Keltner Channel breakout BTC perps 1H, 20-EMA ± 2×ATR(20) + volume + ATR-stop + 1% sizing, hash dc00ba485785d730) + 3 DISLIKE vote intents (pods 362, 365, 366, all epoch 96, all HotBot v4 raw signal/trade exports) queued; postprocess dry-run-only: mint reverted PUBLISHER_LACKS_SUBNET_ACCESS (ISS-004), vote-362 reverted INSUFFICIENT_VOTING_POWER (ISS-006), vote-365 + vote-366 both hit transient mainnet.base.org RPC INTERNAL_ERROR (ISS-007, 3rd + 4th occurrences, first time 2 in same batch); 0 executed on-chain; 14 unassigned datanets | 0 | 0 | 4 |
| 2026-05-25 | trading agent RUN 4th-run (datanet 9) — 1 mint (BTC perps daily Donchian channel breakout, 20/10 high-low + 200-EMA filter + 2×ATR(14) stop + 1% sizing, hash 57f34b45a8edb876) + 3 DISLIKE vote intents (pods 361, 365, 366, all epoch 96, all HotBot v4 raw trade/signal exports) queued; postprocess (dry_run_only=false): mint reverted PUBLISHER_LACKS_SUBNET_ACCESS (ISS-004) AND PR #10 auto-grant helper itself reverted INSUFFICIENT_ALLOWANCE (publisher's REPPO allowance to SubnetManager 0x2629…eE7A is 0, below 50-REPPO fee — new sub-blocker logged in ISS-004), real write skipped; votes 361/365/366 all reverted INSUFFICIENT_VOTING_POWER (ISS-006); 0 executed on-chain; 14 unassigned datanets | 0 | 0 | 4 |
