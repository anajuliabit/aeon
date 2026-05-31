# Skill Evals — 2026-05-31

**Verdict:** SKILL_EVALS_RECOVERED
**Coverage:** 14/29 (48%) ↑ vs prior 41% (+7 pp)
**Diff:** 0 new fail · 3 fixed · 0 still failing · 9 stable · 2 new-spec (failing) · 2 spec-removed

## Action Queue
1. Patch evals.json:hacker-news-digest — required_pattern `### hacker-news-digest|## Hacker News|HN_DIGEST` never matches; skill is disabled (enabled:false) and hn-digest runs inline within daily-routine as `- hn-digest:` sub-bullet; update pattern to `hn-digest:` or defer spec until skill is re-enabled standalone
2. Patch evals.json:monitor-polymarket — skill is disabled (enabled:false), produces no standalone log entries; pattern `### monitor-polymarket|## Polymarket|POLYMARKET` will never match until skill is re-enabled; remove entry or add `expected_cadence: workflow_dispatch` guard
3. Add evals.json entry for morning-brief — active daily (07:00 UTC), output `memory/logs/*.md`, pattern `### morning-brief`
4. Add evals.json entry for skill-freshness — active daily (08:00 UTC), output `articles/skill-freshness-*.md`, pattern `FRESHNESS_OK|FRESHNESS_REGRESSED|FRESHNESS_NO_CHANGE`
5. Add evals.json entry for evening-recap — active daily (21:00 UTC), output `memory/logs/*.md`, pattern `## Evening Recap|evening-recap`

## Recovered (FIXED)
| Skill | Was | Now |
|-------|-----|-----|
| cost-report | NO_OUTPUT (first run not yet due at bootstrap) | PASS |
| token-alert | NO_OUTPUT (wrong output_pattern in prior spec) | PASS |
| skill-health | NO_OUTPUT (wrong output_pattern in prior spec) | PASS |

## Full Results
| Skill | Status | Diff | Root cause | Quality | Words | Last output |
|-------|--------|------|------------|---------|-------|-------------|
| heartbeat | PASS | STABLE | — | unknown | >7,000 | memory/logs/2026-05-30.md |
| cost-report | PASS | FIXED | — | unknown | ~520 | articles/cost-report-2026-05-25.md |
| token-alert | PASS | FIXED | — | unknown | >7,000 | memory/logs/2026-05-30.md |
| skill-health | PASS | FIXED | — | unknown | >7,000 | memory/logs/2026-05-30.md |
| changelog | STALE | STABLE | stale_file (2026-03-19; 73d; cron daily, 2× threshold = 2d); skill disabled | unknown | ~620 | articles/changelog-2026-03-19.md |
| hacker-news-digest | FAIL | NEW_PASS | missing_pattern:### hacker-news-digest\|## Hacker News\|HN_DIGEST — skill disabled; hn-digest runs inline in daily-routine with `- hn-digest:` format | unknown | >7,000 | memory/logs/2026-05-30.md |
| monitor-polymarket | FAIL | NEW_PASS | missing_pattern:### monitor-polymarket\|## Polymarket\|POLYMARKET — skill disabled (enabled:false); no standalone log entries | unknown | >7,000 | memory/logs/2026-05-30.md |
| repo-pulse | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| push-recap | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| fork-fleet | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-article | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-actions | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| deep-research | NO_OUTPUT | STABLE | no_file_match (workflow_dispatch, disabled) | unknown | — | — |
| rss-digest | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |

**Spec changes vs prior:** `hn-digest` and `polymarket` removed from evals.json (orphaned keys with no matching skill name in aeon.yml); replaced by `hacker-news-digest` and `monitor-polymarket` which ARE valid aeon.yml keys — but both are currently disabled, causing immediate FAIL on required_pattern. Coverage count rises 12→14 because both new keys match real skill names (even though disabled). Quality cross-check: no per-skill quality files found for any evals.json skill; `memory/skill-health/` holds `reppo-digest.json` and `search-skill.json` only — not in evals scope.

## Coverage Gaps (enabled in aeon.yml, missing from evals.json)
- morning-brief — inferred pattern: `memory/logs/*.md` (### morning-brief)
- skill-freshness — inferred pattern: `articles/skill-freshness-*.md`
- evening-recap — inferred pattern: `memory/logs/*.md` (## Evening Recap)
- github-trending — inferred pattern: `memory/logs/*.md` (### github-trending)
- defi-overview — inferred pattern: `memory/logs/*.md` (### defi-overview)
- goal-tracker — inferred pattern: `memory/logs/*.md` (### goal-tracker)
- reflect — inferred pattern: `memory/logs/*.md` (### reflect)
- action-converter — inferred pattern: `memory/logs/*.md` (## Action Converter)
- agent-buzz — inferred pattern: `memory/logs/*.md` (### agent-buzz)
- vibecoding-digest — inferred pattern: `memory/logs/*.md` (## Vibecoding Digest)
+9 more — token-pick, defi-overview, market-context-refresh, code-health, fleet-control, reppo-digest, reppo-orchestrator, search-skill, skill-evals itself

## Sources
- evals.json=ok · cron-state=ok · skill-health=ok (partial; last-report.json present, 2 per-skill quality records for non-evals skills) · eval-audit=fail (sandbox restriction; in-memory fallback used) · prior-article=ok (articles/skill-evals-2026-05-24.md)
