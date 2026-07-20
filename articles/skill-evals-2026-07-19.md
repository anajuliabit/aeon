# Skill Evals — 2026-07-19

**Verdict:** SKILL_EVALS_OK
**Coverage:** 12/43 (28%) — unchanged vs prior (2026-07-12)
**Diff:** 0 new fail · 0 fixed · 0 still failing · 12 stable

> **Timing note:** skill-evals dispatched 22:00 UTC Sunday. All log-based skills have written today: heartbeat at 08:00/14:13/20:34 UTC, token-alert at 12:41 UTC, skill-health at 18:30 UTC. No timing-driven false-fails.
>
> **cost-report PASS→STALE:** Last article is 2026-06-29 (20d ago; 2× weekly = 14d threshold exceeded). ISS-025 (critical) is already open. No new issue filed — ISS-025 covers this. Assertions still pass on the existing file; this transition is not classified as NEW_FAIL by spec (STALE ∉ {FAIL, QUALITY_DEGRADED, NO_OUTPUT}) but is threshold-exceeded and worth tracking.

## Action Queue

1. Investigate cost-report — STALE 20d; ISS-025 open, weekly tick blocked since 2026-06-29
2. Add evals.json entry for skill-freshness — pattern: `articles/skill-freshness-*.md`, `FRESHNESS_OK|FRESHNESS_NO_CHANGE`
3. Add evals.json entry for morning-brief — pattern: `memory/logs/*.md`, `### morning-brief`
4. Add evals.json entry for btc-levels — pattern: `memory/logs/*.md`, `btc-levels`
5. Add evals.json entry for narrative-tracker — pattern: `memory/logs/*.md`, `### narrative-tracker|NARRATIVE_TRACKER_OK`
6. Add evals.json entry for security-digest — pattern: `articles/security-digest-*.md`, `KEV|CVE-`

+33 more uncovered enabled skills — see Coverage Gaps.

## Full Results

| Skill | Status | Diff | Root cause | Quality | Words | Last output |
|-------|--------|------|------------|---------|-------|-------------|
| heartbeat | PASS | STABLE | — | unknown | 18,115 | memory/logs/2026-07-19.md |
| token-alert | PASS | STABLE | — | unknown | 18,115 | memory/logs/2026-07-19.md |
| skill-health | PASS | STABLE | — | unknown | 18,115 | memory/logs/2026-07-19.md |
| cost-report | STALE | PASS→STALE | stale_file (20d since 2026-06-29; ISS-025 open) | unknown | 856 | articles/cost-report-2026-06-29.md |
| changelog | STALE | STABLE | stale_file (~122d; disabled) | unknown | 510 | articles/changelog-2026-03-19.md |
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
- narrative-tracker — inferred pattern: `memory/logs/*.md` (`### narrative-tracker|NARRATIVE_TRACKER_OK`) [daily]
- security-digest — inferred pattern: `articles/security-digest-*.md` (`KEV|CVE-`) [daily 14:00 UTC]
- github-trending — inferred pattern: `articles/github-trending-*.md` (`trending|Trending`) [daily 09:00 UTC]

+33 more (agent-buzz, daily-routine, evening-recap, reflect, token-pick, defi-overview, market-context-refresh, action-converter, search-skill, deal-flow, reg-monitor, skill-security-scan, vuln-scanner, autoresearch, list-digest, goal-tracker, skill-analytics, self-improve, thought-review, fork-cohort, skill-update-check, weekly-review, weekly-shiplog, fork-skill-digest, fork-skill-gap, skill-graph, on-chain-monitor, defi-monitor, token-movers, aixbt-pulse, unlock-monitor, operator-scorecard, morning-brief)

## Sources

- evals.json=ok · cron-state=ok · skill-health=ok (partial; 7 per-skill json files, none matching evals.json skills directly) · eval-audit=fail (sandbox restriction; in-memory fallback; enabled_total=43 per prior run + heartbeat 20:34Z log) · prior-article=ok (articles/skill-evals-2026-07-12.md)
