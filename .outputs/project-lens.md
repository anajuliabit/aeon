## Summary

Executed `project-lens` skill with operator-supplied lens `sherwood.sh` (treated verbatim per Phase 2). Angle classified as **Ecosystem map** — both projects answer the same agent-authority question at different layers (Sherwood: capital via ERC-4626 + Guardian timelock; aeon: compute via cron + versioned `SKILL.md` + workflow-dispatch shell-injection guard).

**Thesis** (falsifiable): within 18–24 months "the agent holds the keys" will be a regulatory red flag, not a feature claim — frameworks that constrain agents as proposers (capital or code) outlast custodial ones. Falsifiable on mid-2028 check of largest agent-managed Base treasuries + most-forked agent frameworks.

**Self-edit gates** (Phase 6): all passed first pass — title `who holds the agent's key` doesn't name aeon; first 2 paragraphs anchor to WEF + NIST + supervised-autonomy framing before naming; 5 external citations across 5 distinct domains (weforum.org, joneswalker.com, docs.sherwood.sh, globalcustody.pro, github.com); 6 specific project references (472 stars / 147 forks, self-description quote, cron/SKILL.md architecture, PR #222 with `^[a-zA-Z0-9_-]+$` regex, PR #269 HoundFlow 6 onchain skills, PRs #267+#268 capabilities + secrets manifest); 912 total words (~830 body, within 700–1000); 0 banned-phrase hits; closing forward claim specific enough to be wrong.

**Files**:
- `articles/project-lens-2026-06-01.md` (created)
- `memory/project-lens-angles.md` (created — first project-lens article in repo, no 14-day rotation conflict)
- `memory/logs/2026-06-01.md` (appended Project Lens section)
- `.pending-notify/1780333525-project-lens.md` (staged — sandbox blocks `./notify "$(cat ...)"` arg-passing per MEMORY-noted pattern; post-run delivery picks it up)

**Follow-ups**: none. Future project-lens runs should rotate angle category (Ecosystem map used today, blocked through 2026-06-15).

Sources:
- [AI agent autonomy and governance — World Economic Forum, March 2026](https://www.weforum.org/stories/2026/03/ai-agent-autonomy-governance/)
- [NIST's AI Agent Standards Initiative — Jones Walker](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/nists-ai-agent-standards-initiative-why-autonomous-ai-just-became-washingtons.html?id=102mkh6)
- [Sherwood Protocol docs](https://docs.sherwood.sh/)
- [Complete 2026 Guide to AI in Global Custody](https://www.globalcustody.pro/p/the-complete-2026-guide-to-ai-in-global-custody)
- [aaronjmars/aeon — GitHub](https://github.com/aaronjmars/aeon)
Executed the `project-lens` skill with operator override `var=sherwood.sh`. Wrote an industry-comparison article framing Aeon (cron + bash + git) and Sherwood (ERC-4626 vault + optimistic governance) as two stacks for the same agent-safety primitive: a seam between proposal and signed execution.

**Files created:**
- `articles/project-lens-2026-06-01.md` — 934 words, title "the seam between proposal and execution," 4 inline external citations, 8 specific Aeon references, all 10 Phase 6 self-edit gates passed first try
- `memory/project-lens-angles.md` — first-run seed of the angle-history log (was absent)
- `.pending-notify/1780334045-project-lens.md` — notification staged for post-run delivery (sandbox arg-passing pattern)

**Files modified:**
- `memory/logs/2026-06-01.md` — appended `## Project Lens` entry with full Phase-by-Phase trace

**Thesis (28 words, falsifiable):** mandate-over-custody is a property of process separation, not cryptography — Sherwood and Aeon implement the same proposal/execution seam, one as a vault, one as a cron job, both work.

**Follow-up:** none for this skill. The article makes a falsifiable forward claim ("the runtime camp will discover this in a postmortem") that's worth re-reading in ~6 months when the next round of agent-runtime postmortems lands.
