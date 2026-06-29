*on-chain alert — 2026-06-28*
TL;DR: W1 received ~$33.5k REPPO from W3 then routed equal amount into the REPPO staking contract — operator wallet rotation, no exit.

*Wallet 1 (primary)* (base)
• UNKNOWN-IN $33.5k REPPO ← W3 — [tx](https://basescan.org/tx/0x94dfeb04f1338225277078b259558f35f98c3a65852d609a01fee8756e66bee8)
• UNKNOWN-OUT $33.5k REPPO → 0xc81F...68E8 (REPPO staking) — [tx](https://basescan.org/tx/0x096389a8439f6f8dec70f25ddc7bc9be22b7453728414b68d1e3400cda8fbbf5)
• UNKNOWN-OUT $6.6k USDC → Morpho GA1 (steakUSDC vault deposit) — [tx](https://basescan.org/tx/0xba5c8a9dabd3324b2dca7127a5ce2745d7b7f1a16b5f7173c8ef8be7b201171c)

*Wallet 3* (base)
• UNKNOWN-OUT $33.5k REPPO → W1 — [tx](https://basescan.org/tx/0x94dfeb04f1338225277078b259558f35f98c3a65852d609a01fee8756e66bee8)
• UNKNOWN-IN $28.2k REPPO ← 0xc81F...68E8 (REPPO staking withdraw) — [tx](https://basescan.org/tx/0x8529290de558fd2b272547228d478d7e337410104ec366a8e184c28fa0c814fb)

5 events on 2 watches | sources: blockscout=ok, coingecko=ok, alchemy=skipped(no_key), etherscan=skipped(chain_paywalled) | last_block→47930872
