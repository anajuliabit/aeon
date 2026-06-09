## Reppo Voter — Run Summary

**Gate decision:** `RUN` (datanet 9 TradingGymAI valid + ACTIVE).
**Current epoch:** 103.
**Pods seen:** 79.
**Filtered:**
- Out-of-epoch (`validityEpoch != "103"`): **69**
- Already-voted (in `voted_pod_ids`): **4** — 839, 838, 762, 761
- Own pod (ledger wallet-shortcode workaround): **1** — pod 841 (`HL perps 52m, 0x06ce..164b: 250 trades` = today's 20th-mint AAVE pod for 0x06cecfba)
- **Eligible: 5**

**Queued votes (2 LIKE / 3 DISLIKE — not all-DISLIKE):**

| Pod | Direction | Reason |
|-----|-----------|--------|
| 832 | LIKE | `0x3dd4..7a81` 23-trade canonical snapshot for this wallet in epoch 103 |
| 824 | LIKE | `0x9984..95ba` 10-trade distinct clean dataset; non-redundant HL perp format |
| 828 | DISLIKE | Exact duplicate of pod 832 (same wallet, same 23 trades, different IPFS) |
| 825 | DISLIKE | Superseded 21-trade subset of wallet 0x3dd4..7a81's pod 832 |
| 764 | DISLIKE | Oldest 17-trade subset of same wallet; also 2,227 community downvotes |

No prompt-injection attempts detected in any pod metadata.

**Notes for the operator:**
- The four `0x3dd4..7a81` pods (17/21/23/23 trades) look like progressive snapshot spam from a single contributor — 832 chosen as canonical, the other three downvoted as redundant subsets/duplicates.
- The earlier voter run today queued these same 5 pods, yet none appear in `voted_pod_ids` while the other 4 (839/838/762/761) did land — likely either (a) those tx reverted on-chain (per-epoch wallet vote cap?), or (b) the prefetch cache snapshot pre-dated postprocess execution. Re-queued this run per skill spec since the filter cache currently flags them eligible.

**Files written:**
- `.pending-reppo/vote-832-like.json`
- `.pending-reppo/vote-824-like.json`
- `.pending-reppo/vote-828-dislike.json`
- `.pending-reppo/vote-825-dislike.json`
- `.pending-reppo/vote-764-dislike.json`
- `memory/logs/2026-06-09.md` — appended `### reppo-voter` entry

`scripts/postprocess-reppo.sh` will execute these intents after the skill exits and append on-chain results to the output.
