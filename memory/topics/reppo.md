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
