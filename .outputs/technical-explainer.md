## Summary

Ran `skills/technical-explainer/SKILL.md` with var = the Reppo-swarm-on-Aeon explainer brief.

**Topic:** how the Reppo agent swarm runs on Aeon — data flow from on-chain Reppo state → orchestrator/trader/digest skill chain → mint/vote intent files → Base postprocess.

**Files created/modified:**
- `articles/explainer-2026-05-28.md` — 600-word structured explainer (setup, intuition pump, 6-step walkthrough, anchor numbers with citations, falsifier, why-it-matters, sources). Voice: ana lowercase, no marketing verbs, em-dash sparingly, concrete refs (PR #s, tx hashes, file paths).
- `.pending-replicate/explainer-2026-05-28.json` — Replicate request for the dark-mode 4-lane system diagram (DATA INGESTION → VERIFICATION → REASONING → EXECUTION with central "AEON chain-runner" engine node). Will be processed by `scripts/postprocess-replicate.sh` if `$REPLICATE_API_TOKEN` is set; otherwise hero image is skipped and text stands on its own.
- `memory/logs/2026-05-28.md` — appended `## Technical Explainer` block with topic, title, key idea, image status, primary source, file, notification status.
- `.pending-notify/1779972472-technical-explainer.md` — staged notification (sandbox-blocked `./notify "$(cat ...)"` pattern carried over from this morning's runs).

**Research:** 3 WebSearches + WebFetch on `reppo-labs-xyz.gitbook.io/reppo-labs/foundations/how-reppo-works.md` confirmed 48h epoch, linear vote-power decay, 45/45/5/5 emission split, 20k REPPO datanet lockup.

**Follow-up:** the article references `images/explainer-2026-05-28.jpg` — if `postprocess-replicate.sh` doesn't run with the token set, that path 404s in the rendered article. No other action needed.
