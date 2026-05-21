# Reppo Swarm — Running Ledger

Append-only audit trail for the reppo-swarm chain. The trading agent reads
the "Minted strategies" table to avoid re-minting; the digest appends to it.

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
