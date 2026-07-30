# Skill Evals — 2026-07-26

**Verdict:** SKILL_EVALS_OK
**Coverage:** 12/43 (28%) — unchanged vs prior (2026-07-19)
**Diff:** 0 new fail · 0 fixed · 2 still failing · 10 stable

> **Timing note:** skill-evals dispatched 22:00 UTC Sunday. All log-based skills have written today: skill-health at 18:00 UTC, token-alert at 12:00 UTC, heartbeat at 09:36 UTC, 14:04 UTC, 20:47Z (confirmed in memory/logs/2026-07-26.md). No timing-driven false-fails.
>
> **cost-report:** Latest article is 2026-07-20 (6 days ago). Weekly schedule = ~7d cadence, so within expected window. ISS-025 remains open (critical sandbox truncation). Assertions pass on the existing file. Carries STILL_FAIL status from prior eval.

## Action Queue

1. Investigate skill-health — still failing on missing_pattern; 47% success rate per cron-state; documented ISS-024
2. Investigate token-alert — still failing on timing/pattern; 74% success rate per cron-state; documented ISS-023
3. Add evals.json entry for skill-freshness — pattern: `articles/skill-freshness-*.md`, `FRESHNESS_OK|FRESHNESS_NO_CHANGE`
4. Add evals.json entry for morning-brief — pattern: `memory/logs/*.md`, `### morning-brief`
5. Add evals.json entry for btc-levels — pattern: `memory/logs/*.md`, `btc-levels`
6. Add evals.json entry for narrative-tracker — pattern: `memory/logs/*.md`, `### narrative-tracker`
7. Add evals.json entry for security-digest — pattern: `articles/security-digest-*.md`, `KEV|CVE-`
8. Add evals.json entry for github-trending — pattern: `articles/github-trending-*.md`, `trending|Trending`

## Full Results

| Skill | Status | Diff | Root cause | Quality | Words | Last output |
|-------|--------|------|------------|---------|-------|-------------|
| heartbeat | PASS | STABLE | — | unknown | 18,115+ | memory/logs/2026-07-26.md |
| token-alert | FAIL | STILL_FAIL | missing_pattern:### token-alert\|TOKEN_ALERT | unknown | 18,115+ | memory/logs/2026-07-26.md |
| skill-health | FAIL | STILL_FAIL | missing_pattern:### skill-health\|SKILL_HEALTH\|HEALTH: | unknown | 18,115+ | memory/logs/2026-07-26.md |
| cost-report | PASS | STABLE | — | unknown | 606 | articles/cost-report-2026-07-20.md |
| changelog | STALE | STABLE | stale_file (~133d; disabled) | unknown | 510 | articles/changelog-2026-03-19.md |
| repo-pulse | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| push-recap | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| fork-fleet | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-article | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-actions | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| deep-research | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| rss-digest | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |

## Coverage Gaps (enabled in aeon.yml, missing from evals.json)

Coverage 12/43 (28%). 4 of 12 evals.json skills are enabled (heartbeat, token-alert, skill-health, cost-report); 39 enabled skills remain uncovered.

- skill-freshness — inferred pattern: `articles/skill-freshness-*.md` (`FRESHNESS_OK|FRESHNESS_NO_CHANGE`) [daily 08:00 UTC]
- morning-brief — inferred pattern: `memory/logs/*.md` (`### morning-brief`) [daily 07:00 UTC]
- btc-levels — inferred pattern: `memory/logs/*.md` (`btc-levels`) [4-hourly]
- narrative-tracker — inferred pattern: `memory/logs/*.md` (`### narrative-tracker`) [daily 13:30 UTC]
- security-digest — inferred pattern: `articles/security-digest-*.md` (`KEV|CVE-`) [daily 14:00 UTC]
- github-trending — inferred pattern: `articles/github-trending-*.md` (`trending|Trending`) [daily 09:00 UTC]

+33 more (agent-buzz, daily-routine, evening-recap, reflect, token-pick, defi-overview, market-context-refresh, action-converter, search-skill, deal-flow, reg-monitor, skill-security-scan, vuln-scanner, autoresearch, list-digest, goal-tracker, skill-analytics, self-improve, thought-review, fork-cohort, skill-update-check, weekly-review, weekly-shiplog, fork-skill-digest, fork-skill-gap, skill-graph, on-chain-monitor, defi-monitor, token-movers, aixbt-pulse, unlock-monitor, operator-scorecard, fork-cohort)

## Sources

- evals.json=ok · cron-state=ok · skill-health=ok (partial; 8 per-skill json files per memory/skill-health) · eval-audit=unavailable (sandbox restriction) · prior-article=ok (articles/skill-evals-2026-07-19.md)
