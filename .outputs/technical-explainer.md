Task is small and linear; skipping TaskCreate. Done.

## Summary

Re-ran `skills/technical-explainer/SKILL.md` with the operator's var override (Reppo agent swarm + Aeon, Powerloom-style cyan/green system diagram with 4 labeled lanes).

**Files written/modified:**
- `articles/explainer-2026-05-28.md` — overwritten in place. Same title + key idea, refined body (numbers refreshed to 3 mints + 7 votes after today's 3rd-run vote pair), new HTML image-prompt comment matching the Powerloom direction.
- `.pending-replicate/explainer-2026-05-28.json` — new replicate request with the cyan #22d3ee / green #22c55e / near-black #0b1117 prompt, 4 stacked horizontal lanes (DATA INGESTION → VERIFICATION → REASONING → EXECUTION), central "AEON chain-runner" engine node fanning to each lane + output arrow to Base mainnet. Picked up by `scripts/postprocess-replicate.sh` if `$REPLICATE_API_TOKEN` is set; otherwise the article ships imageless per the skill's no-image path.
- `memory/logs/2026-05-28.md` — appended a `## Technical Explainer (2nd run, operator var override)` block.
- `.pending-notify/1779972500-technical-explainer.md` — notification staged for post-run delivery (sandbox blocks the inline `./notify "$(cat …)"` arg-passing pattern, per MEMORY.md).

**Follow-up:**
- If `REPLICATE_API_TOKEN` is unset at postprocess time, the article's `![hero]` line will 404 — text stands on its own.
- ISS-009 root cause (chain-runner `.result` overwriting `.outputs/`) is now the load-bearing example in the "how it actually works" walkthrough — referenced as the seam where the bug *is* the seam.
