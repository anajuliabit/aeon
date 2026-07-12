# Skill Evals — 2026-07-12

**Verdict:** SKILL_EVALS_OK
**Coverage:** 12/43 (28%) — unchanged vs prior (2026-07-05)
**Diff:** 0 new fail · 0 fixed · 0 still failing · 12 stable

> **Timing note:** skill-evals scheduled 22:00 UTC Sunday per `aeon.yml`. Log-based skills have all written for today: heartbeat at 08:55 UTC + 14:16 UTC, token-alert at 12:45 UTC, skill-health at 18:39 UTC. No timing-driven false-fails.

## Action Queue

1. Add evals.json entry for skill-freshness — daily 08:00 UTC; `articles/skill-freshness-*.md`, pattern `FRESHNESS_OK|FRESHNESS_NO_CHANGE`
2. Add evals.json entry for morning-brief — daily 07:00 UTC; `memory/logs/*.md`, pattern `### morning-brief`
3. Add evals.json entry for btc-levels — 4-hourly; `memory/logs/*.md`, pattern `btc-levels`
4. Add evals.json entry for narrative-tracker — daily; `memory/logs/*.md`, pattern `### narrative-tracker|NARRATIVE_TRACKER_OK`
5. Add evals.json entry for security-digest — daily 14:00 UTC; `articles/security-digest-*.md`, pattern `KEV|CVE-`

+34 more uncovered enabled skills — see Coverage Gaps.

## Full Results

| Skill | Status | Diff | Root cause | Quality | Words | Last output |
|-------|--------|------|------------|---------|-------|-------------|
| heartbeat | PASS | STABLE | — | unknown | 17,329 | memory/logs/2026-07-12.md |
| token-alert | PASS | STABLE | — | unknown | 17,329 | memory/logs/2026-07-12.md |
| skill-health | PASS | STABLE | — | unknown | 17,329 | memory/logs/2026-07-12.md |
| cost-report | PASS | STABLE | — (13d since 6-29; 2× = 14d, not stale yet — next tick Mon 7-13) | unknown | 856 | articles/cost-report-2026-06-29.md |
| changelog | STALE | STABLE | stale_file (~115d; disabled) | unknown | 510 | articles/changelog-2026-03-19.md |
| repo-pulse | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| push-recap | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| fork-fleet | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-article | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-actions | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| deep-research | NO_OUTPUT | STABLE | no_file_match (disabled, workflow_dispatch) | unknown | — | — |
| rss-digest | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |

## Coverage Gaps (enabled in aeon.yml, missing from evals.json)

Coverage unchanged at 12/43 (28%). 4 of the 12 evals.json skills are enabled (heartbeat, token-alert, skill-health, cost-report); 39 enabled skills remain uncovered.

- skill-freshness — inferred pattern: `articles/skill-freshness-*.md` (`FRESHNESS_OK|FRESHNESS_NO_CHANGE`) [daily 08:00 UTC]
- morning-brief — inferred pattern: `memory/logs/*.md` (`### morning-brief`) [daily 07:00 UTC]
- btc-levels — inferred pattern: `memory/logs/*.md` (`btc-levels`) [4-hourly]
- narrative-tracker — inferred pattern: `memory/logs/*.md` (`### narrative-tracker|NARRATIVE_TRACKER_OK`) [daily]
- security-digest — inferred pattern: `articles/security-digest-*.md` (`KEV|CVE-`) [daily 14:00 UTC]
- github-trending — inferred pattern: `articles/github-trending-*.md` (`trending|Trending`) [daily 09:00 UTC]

+33 more (agent-buzz, daily-routine, evening-recap, reflect, token-pick, defi-overview, market-context-refresh, action-converter, search-skill, deal-flow, reg-monitor, skill-security-scan, vuln-scanner, autoresearch, list-digest, goal-tracker, skill-analytics, self-improve, thought-review, fork-cohort, skill-update-check, weekly-review, weekly-shiplog, fork-skill-digest, fork-skill-gap, skill-graph, on-chain-monitor, defi-monitor, token-movers, aixbt-pulse, unlock-monitor, operator-scorecard, morning-brief)

## Sources

- evals.json=ok · cron-state=ok · skill-health=ok (partial; 7 per-skill json files, none matching evals.json skills directly) · eval-audit=fail (sandbox restriction; in-memory fallback used; enabled_total=43 per aeon.yml grep + heartbeat log) · prior-article=ok (articles/skill-evals-2026-07-05.md)
