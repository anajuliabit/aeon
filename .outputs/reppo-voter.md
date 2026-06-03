## reppo-voter — run output

- **Gate:** RUN (orchestrator's `reppo-plan` shows `reppo-trading-agent: RUN` for datanet 9, `valid:true` + ACTIVE).
- **Epoch:** 101 — **pods seen:** 61.
- **Filtered (do-not-vote):**
  - 59 **out-of-epoch** (`validityEpoch != 101`)
  - 0 fresh **already-voted** (all 19 in `voted_pod_ids` sit at epochs ≤100, already covered by the out-of-epoch sweep)
  - 11 **own pods** via ledger wallet-shortcode cross-ref — 478/492 (0x9a15..37e6, 13th + 14th mints), 463 (0xbb10), 462 (0xd475), 412 (0x7fda), 413 (0x71dfc0), 395 (0x8def), 399 (0xebe1), 392 (0x2b33), 406 (0x3200), 402 (0x0ddf); all also out-of-epoch. Own-pods prefetch returned `count:0` again — ISS-016 carries 9th consecutive run.
- **Eligible:** 2 pods (507, 508).

### Votes queued
| Pod | Direction | Reason |
|-----|-----------|--------|
| 507 | DISLIKE | HotBot v4 raw Trades & Learning export (Jun 01–Jun 03); no labeled per-trade fields (market/direction/size/leverage/fill price), no aggregate metrics (win rate/Sharpe/MDD), no HL tx hashes — off-rubric NO. |
| 508 | DISLIKE | HotBot v4 raw Signal Intelligence export (Jun 01–Jun 03); strategy/signal scan dump without executed trades, missing aggregate metrics + HL tx verification — off-rubric NO. |

**ISS-005 / all-DISLIKE flag — ON.** Both eligible pods voted DISLIKE, zero LIKE on a non-empty eligible set. Pattern matches the 49 prior off-rubric HotBot v4 exports in the ledger (rubric-driven, not a curation-signal degradation), but flagged per the guard for operator review.

No prompt-injection attempts detected in pod metadata.

## Summary
- Queued 2 DISLIKE vote intents (`.pending-reppo/vote-507-dislike.json`, `.pending-reppo/vote-508-dislike.json`) for epoch-101 HotBot v4 raw exports on datanet 9.
- Files modified: `memory/logs/2026-06-03.md` (appended `### reppo-voter` entry).
- Files created: `.pending-reppo/vote-507-dislike.json`, `.pending-reppo/vote-508-dislike.json`.
- Follow-ups: `scripts/postprocess-reppo.sh` will execute the intents and append `## Execution Results` to the voter output; on-chain outcomes will be recorded by the digest step. ISS-016 own_pods prefetch `count:0` still active (defensive ledger cross-ref carrying the gap).
