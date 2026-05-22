# Reppo Swarm — Running Ledger

Append-only audit trail for the reppo-swarm chain. The trading agent reads
the "Minted strategies" table to avoid re-minting; the digest appends to it.

## Minted strategies
| Date | Datanet | Strategy hash (sha256, first 16) | Source | Tx status |
|------|---------|----------------------------------|--------|-----------|
| 2026-05-22 | 9 | a7ae1f01372c9b1f | Gate Learn — BTC funding-rate arbitrage | pending (postprocess) |

## Votes cast
| Date | Datanet | Pod id | Direction | Tx status |
|------|---------|--------|-----------|-----------|
| 2026-05-22 | 9 | 257 | like | pending (postprocess) |
| 2026-05-22 | 9 | 332 | dislike | pending (postprocess) |
| 2026-05-22 | 9 | 300 | dislike | pending (postprocess) |

## Run history
| Date | Orchestrator | Minted | Voted | Failures |
|------|--------------|--------|-------|----------|
| 2026-05-21 | trading agent SKIP — tradinggymai datanet_id is still the placeholder; prefetch failed | 0 | 0 | 1 |
| 2026-05-22 | trading agent RUN — datanet 9 active & valid; 14 unassigned datanets discovered | 1 | 3 | 0 |
