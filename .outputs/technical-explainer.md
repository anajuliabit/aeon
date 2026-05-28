## Summary

4th run of `technical-explainer` for 2026-05-28 with operator var override (Reppo agent swarm + Aeon, Powerloom BDS aesthetic).

**Files modified:**
- `articles/explainer-2026-05-28.md` — in-place tighten on numbers row 5 only: bumped onchain receipts to `3 mints + 9 votes` and swapped latest vote-pair to today's 4th-run pair tx [`0xac2ec2…`](https://basescan.org/tx/0xac2ec23b2f623caa962f9aa5560bc589947ec9842a5fbf1e6dba2333075f5801) / tx [`0xf78cc2…`](https://basescan.org/tx/0xf78cc26af15e0b432de6f4a2bd60fc5a5851d5e69ac4f3c0106c3ced1f552dcb), with framing "6× DISLIKE on each of pods 372/373 in a single UTC day, the ISS-005 dedup gap as a live receipt."
- `memory/logs/2026-05-28.md` — appended `## Technical Explainer (4th run, operator var override)` block.

**Files created:**
- `.pending-replicate/explainer-2026-05-28.json` — re-staged (prior runs' `.pending-replicate/` was consumed by postprocess); cyan/green/near-black system diagram with central hexagonal AEON chain-runner engine + 4 lanes (DATA INGESTION → VERIFICATION → REASONING → EXECUTION) + output arrow to Base mainnet.
- `.pending-notify/1779974604-technical-explainer.md` — Telegram message staged (sandbox blocks `./notify "$(cat ...)"` arg-passing per MEMORY.md pattern; post-run delivery picks it up).

**Follow-up:**
- Watch for `images/explainer-2026-05-28.jpg` to land if `$REPLICATE_API_TOKEN` is set when `scripts/postprocess-replicate.sh` runs; otherwise the article's hero will 404 and the no-image path is in effect.
- The article's `what would break this` section now points to the live ISS-005 receipt (6× dup-pair votes today), which is honest and on-mechanism — no further action needed there.

Sources used:
- [reppo labs docs (llms-full)](https://reppo-labs-xyz.gitbook.io/reppo-labs/llms-full.txt)
- [REPPO on coinmarketcap](https://coinmarketcap.com/currencies/reppo/)
- [reppo $20M raise (coindesk)](https://www.coindesk.com/press-release/2026/04/23/reppo-foundation-secures-usd20m-capital-commitment-to-solve-training-data-bottleneck-using-prediction-markets)
