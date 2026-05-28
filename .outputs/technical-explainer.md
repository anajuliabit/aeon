## Summary

Refined the technical explainer for `articles/explainer-2026-05-28.md` (3rd run today with the same operator var) — tightened the image prompt to match the Powerloom BDS reference more directly: central hexagonal **AEON chain-runner** engine node with cyan `#22d3ee` fan-out arrows + lime-green `#22c55e` inline annotations, 4 stacked lanes (DATA INGESTION → VERIFICATION → REASONING → EXECUTION), single thicker output arrow to a **Base mainnet** node. Body unchanged except for adding the latest vote-pair tx links (`0x8d3b0d…` / `0x7563fe…`) into the "numbers that anchor it" row.

**Files modified:**
- `articles/explainer-2026-05-28.md` — sharpened image-prompt comment + updated vote-tx links
- `.pending-replicate/explainer-2026-05-28.json` — re-staged Replicate request (overwrote prior 2nd-run payload)
- `memory/logs/2026-05-28.md` — appended "Technical Explainer (3rd run, operator var override)" section
- `.pending-notify/1779973765-technical-explainer.md` — staged notification

**Follow-up:** image lands at `images/explainer-2026-05-28.jpg` if `scripts/postprocess-replicate.sh` runs with `REPLICATE_API_TOKEN` set; otherwise hero-image line in the article will 404 and the no-image path applies.
