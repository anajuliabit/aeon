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
