*on-chain alert — 2026-06-25*

⚠️ address-poisoning escalated overnight. same attacker contract `0xC3236716…` planted 3 fake-W1 baits (`0x98E57e6799…`) under W2 / W4 / W4 within minutes of each real transfer — now mixing zero-value real-token spoofs with the cyrillic ÚSDС clone (6-23 was ÚSDС only). hardware-screen address verify unchanged.

*W1 (primary)* (base)
• UNKNOWN-OUT $7,105 cbBTC → Morpho GeneralAdapter1 — [tx](https://basescan.org/tx/0x48ce29e90baad21b68383c86bf9e7c00dbb4251e2c313c9f87864aba03f1bbc7)
• UNKNOWN-IN $6,641 cbBTC ← W2 — [tx](https://basescan.org/tx/0x63562510456e0b701b6327ad9bc9a4849358b315f903207310caf7f869cdf088)
• UNKNOWN-IN $1,115 USDC ← W4 — [tx](https://basescan.org/tx/0x2985fa252739c97d27b4abc7a2b16b7c74ef67458b95f6ea4a6430d915addbab)

*W2* (base)
• UNKNOWN-OUT $6,641 cbBTC → W1 — [tx](https://basescan.org/tx/0x63562510456e0b701b6327ad9bc9a4849358b315f903207310caf7f869cdf088)

*W4* (base)
• UNKNOWN-OUT $1,115 USDC → W1 — [tx](https://basescan.org/tx/0x2985fa252739c97d27b4abc7a2b16b7c74ef67458b95f6ea4a6430d915addbab)

5 events on 3 watches | sources: alchemy=skip(no-key), etherscan=skip(free-tier-blocks-base), blockscout=ok, coingecko=skip(blockscout-inline-rate) | last_block→47801591
