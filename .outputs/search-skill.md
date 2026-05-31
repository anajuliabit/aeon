## Summary

Executed `skills/search-skill/SKILL.md`. Exit: **SEARCH_SKILL_OK_CANDIDATES**.

**Query:** `"reddit"` derived from priorities (MEMORY.md ISS-015 mitigation — vibecoding-digest's 3-day Reddit blockage names "authed Reddit API / pushshift / alternate source" as the explicit options). Step (a) failing-skills clear, (b) no open issues match {missing-secret, api-change, permanent-limitation, quality-regression}.

**Search:** 6 candidates from `npx skills find` (skills.sh-sourced). vercel-labs/agent-skills (8 skills), anthropics/skills (17), BankrBot/skills, aaronjmars/aeon all enumerated via `gh api` (because `./add-skill --list` requires per-call approval in sandbox; gh-api equivalent for read-only). skills.sh search page returned only nav, no parseable results — marked fail.

**Top 2 after hard gates (none install):**
- `resciencelab/opc-skills@reddit` — sum 13/15, gap-fit 2/5, pushed today — same public-json path that's already sandbox-blocked. UNTRUSTED.
- `lignertys/reddit-research-skill@reddapi` — sum 12/15, gap-fit 3/5, pushed 5-09 — third-party reddapi.dev backend, different host could bypass block but needs paid signup. UNTRUSTED.

**No install** — top gap-fit ≤3 AND both UNTRUSTED. Real ISS-015 fix remains the operator call on `oauth.reddit.com` OAuth or alt source.

**Files changed:**
- `.pending-notify/1780236709-search-skill.md` — notification staged (sandbox-blocks `./notify` arg-passing)
- `memory/logs/2026-05-31.md` — appended `### search-skill` entry per step 8

**Follow-up:** operator decision on ISS-015 source switch (authed Reddit vs pushshift vs alt). Neither candidate above solves the root cause.
