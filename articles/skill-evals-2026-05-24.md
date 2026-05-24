# Skill Evals — 2026-05-24

**Verdict:** SKILL_EVALS_OK
**Coverage:** 12/29 (41%) (first run — bootstrap baseline established)
**Diff:** 0 new fail · 0 fixed · 0 still failing · 1 pass · 13 bootstrap (no prior to compare)

## Action Queue
1. Patch evals.json:token-alert — output_pattern `articles/token-alert-*.md` doesn't match actual output location (memory/logs/YYYY-MM-DD.md); skill succeeds but scores NO_OUTPUT every run
2. Patch evals.json:skill-health — output_pattern `articles/skill-health-*.md` doesn't match actual output location (memory/skill-health/last-report.json); update pattern and assertions
3. Patch evals.json:hn-digest — no `skills/hn-digest/` directory exists; orphaned spec entry; rename to `hacker-news-digest` or remove
4. Patch evals.json:polymarket — no `skills/polymarket/` directory exists; orphaned spec entry; rename to `monitor-polymarket` or remove
5. Add evals.json entry for skill-freshness — pattern: `articles/skill-freshness-*.md` (active daily, verified outputs 2026-05-22 and 2026-05-23)
6. Add evals.json entry for morning-brief — pattern: `memory/logs/*.md` (daily, verified output in 2026-05-23 log)
7. Add evals.json entry for evening-recap — pattern: `memory/logs/*.md` (daily 21:00 UTC, verified output in 2026-05-23 log)
8. Add evals.json entry for reflect — pattern: `memory/logs/*.md` (daily 18:00 UTC, verified output in 2026-05-23 log)

## Full Results
| Skill | Status | Diff | Root cause | Quality | Words | Last output |
|-------|--------|------|------------|---------|-------|-------------|
| heartbeat | PASS | NEW_PASS | — | unknown | ~3,300 | memory/logs/2026-05-23.md |
| changelog | STALE | BOOTSTRAP | stale_file (2026-03-19; 66d; cron daily, 2× threshold = 2d) | unknown | ~620 | articles/changelog-2026-03-19.md |
| cost-report | NO_OUTPUT | BOOTSTRAP | no_file_match (enabled weekly Mon; bootstrap 2026-05-21 Thu; not yet due) | unknown | — | — |
| deep-research | NO_OUTPUT | BOOTSTRAP | no_file_match (workflow_dispatch, disabled) | unknown | — | — |
| fork-fleet | NO_OUTPUT | BOOTSTRAP | no_file_match (disabled) | unknown | — | — |
| hn-digest | NO_OUTPUT | BOOTSTRAP | no_file_match (no skills/hn-digest/ dir; orphaned spec) | unknown | — | — |
| polymarket | NO_OUTPUT | BOOTSTRAP | no_file_match (no skills/polymarket/ dir; orphaned spec) | unknown | — | — |
| push-recap | NO_OUTPUT | BOOTSTRAP | no_file_match (disabled) | unknown | — | — |
| repo-actions | NO_OUTPUT | BOOTSTRAP | no_file_match (disabled) | unknown | — | — |
| repo-article | NO_OUTPUT | BOOTSTRAP | no_file_match (disabled) | unknown | — | — |
| repo-pulse | NO_OUTPUT | BOOTSTRAP | no_file_match (disabled) | unknown | — | — |
| rss-digest | NO_OUTPUT | BOOTSTRAP | no_file_match (disabled) | unknown | — | — |
| skill-health | NO_OUTPUT | BOOTSTRAP | no_file_match (outputs to memory/skill-health/, not articles/; 2 successful runs confirmed) | unknown | — | — |
| token-alert | NO_OUTPUT | BOOTSTRAP | no_file_match (outputs to memory/logs/, not articles/; 2 successful runs confirmed via cron-state) | unknown | — | — |

**Notes:**
- `heartbeat` checked against `memory/logs/2026-05-23.md` (most recent). All assertions pass: word count ~3,300 >> min 20; pattern "heartbeat" present × 3; no forbidden patterns.
- `changelog` checked against `articles/changelog-2026-03-19.md`. All content assertions pass (words ~620 >> 150; "commit/fix/feat/change" present; no forbidden patterns); marked STALE because file date is 66 days vs 2-day threshold. Skill is disabled — staleness expected.
- 8 of 12 NO_OUTPUT results are disabled skills: expected behavior, not failures.
- 2 NO_OUTPUT results (token-alert, skill-health) are enabled skills that run successfully; root cause is wrong output_pattern in evals.json (spec bug, not skill failure).
- 1 NO_OUTPUT (cost-report) is an enabled weekly skill that has not yet reached its first scheduled run since bootstrap.
- 2 NO_OUTPUT (hn-digest, polymarket) have no matching skill directory in skills/ — orphaned evals.json entries.
- Quality cross-check: no per-skill quality files found for any of the 14 evaluated skills. memory/skill-health/ contains last-report.json, reppo-digest.json, search-skill.json — none match evals.json scope.

## Coverage Gaps (enabled in aeon.yml, missing from evals.json)
- morning-brief — inferred pattern: `memory/logs/*.md`
- github-trending — inferred pattern: `memory/logs/*.md`
- defi-overview — inferred pattern: `memory/logs/*.md`
- search-skill — inferred pattern: `memory/logs/*.md`
- skill-security-scan — inferred pattern: `articles/skill-security-scan-*.md`
- autoresearch — inferred pattern: `memory/logs/*.md`
- goal-tracker — inferred pattern: `memory/logs/*.md`
- skill-analytics — inferred pattern: `articles/skill-analytics-*.md`
- self-improve — inferred pattern: `memory/logs/*.md`
- reflect — inferred pattern: `memory/logs/*.md`
+7 more — action-converter, evening-recap, skill-evals, skill-update-check, skill-freshness, weekly-review, operator-scorecard

## Sources
- evals.json=ok · cron-state=ok · skill-health=ok (partial; 2 quality records) · eval-audit=fail (sandbox restriction; in-memory fallback used) · prior-article=none (bootstrap)
