# Skill Evals — 2026-07-05

**Verdict:** SKILL_EVALS_RECOVERED
**Coverage:** 12/43 (28%) ↑1pp vs prior 27%
**Diff:** 0 new fail · 3 fixed · 0 still failing · 9 stable

> **Timing note:** skill-evals is now scheduled at 22:00 UTC Sunday (per `aeon.yml` — comment references ISS-026). All three log-based skills have written for the day: heartbeat at 10:01 UTC and 14:47 UTC, token-alert at 12:57 UTC, skill-health at 18:03 UTC. The timing-driven false-fails from prior evals (ISS-023/ISS-024/ISS-026) self-resolved once the schedule was pushed late. ISS-023, ISS-024, ISS-026 are closed this run.

## Action Queue
1. Add evals.json entry for skill-freshness — daily 08:00 UTC; `articles/skill-freshness-*.md`, pattern `FRESHNESS_OK|FRESHNESS_NO_CHANGE`
2. Add evals.json entry for morning-brief — daily 07:00 UTC; `memory/logs/*.md`, pattern `### morning-brief`
3. Add evals.json entry for btc-levels — 4-hourly; `memory/logs/*.md`, pattern `btc-levels`
4. Add evals.json entry for narrative-tracker — daily; `memory/logs/*.md`, pattern `### narrative-tracker|NARRATIVE_TRACKER_OK`
5. Add evals.json entry for security-digest — daily 14:00 UTC; `articles/security-digest-*.md`, pattern `KEV|CVE-`

+34 more uncovered enabled skills — see Coverage Gaps.

## Recovered (FIXED)
| Skill | Was | Now |
|-------|-----|-----|
| heartbeat | FAIL/NEW_FAIL (ISS-026 — timing, skill-evals ran before 08:00 UTC tick) | PASS (### heartbeat — 10:01 UTC + 14:47 UTC in memory/logs/2026-07-05.md) |
| token-alert | FAIL/STILL_FAIL (ISS-023 — missing_pattern, timing) | PASS (### token-alert — 12:57 UTC · TOKEN_ALERT in memory/logs/2026-07-05.md) |
| skill-health | FAIL/STILL_FAIL (ISS-024 — missing_pattern, timing + structural) | PASS (### skill-health — 18:03 UTC · HEALTH: DEGRADED in memory/logs/2026-07-05.md) |

## Full Results
| Skill | Status | Diff | Root cause | Quality | Words | Last output |
|-------|--------|------|------------|---------|-------|-------------|
| heartbeat | PASS | FIXED | — | unknown | 10,017 | memory/logs/2026-07-05.md |
| token-alert | PASS | FIXED | — | unknown | 10,017 | memory/logs/2026-07-05.md |
| skill-health | PASS | FIXED | — | unknown | 10,017 | memory/logs/2026-07-05.md |
| cost-report | PASS | STABLE | — | unknown | 856 | articles/cost-report-2026-06-29.md |
| changelog | STALE | STABLE | stale_file (~108d; disabled) | unknown | 510 | articles/changelog-2026-03-19.md |
| repo-pulse | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| push-recap | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| fork-fleet | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-article | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-actions | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| deep-research | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| rss-digest | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |

## Coverage Gaps (enabled in aeon.yml, missing from evals.json)
Coverage ticked +1pp (27%→28%) due to enabled_total dropping from 44→43. evals.json unchanged at 12 entries. 39 enabled skills remain uncovered — same as 6-28.

- skill-freshness — inferred pattern: `articles/skill-freshness-*.md` (`FRESHNESS_OK|FRESHNESS_NO_CHANGE`) [daily 08:00 UTC]
- morning-brief — inferred pattern: `memory/logs/*.md` (`### morning-brief`) [daily 07:00 UTC]
- btc-levels — inferred pattern: `memory/logs/*.md` (`btc-levels`) [4-hourly]
- narrative-tracker — inferred pattern: `memory/logs/*.md` (`### narrative-tracker|NARRATIVE_TRACKER_OK`) [daily]
- security-digest — inferred pattern: `articles/security-digest-*.md` (`KEV|CVE-`) [daily 14:00 UTC]
- github-trending — inferred pattern: `articles/github-trending-*.md` (`trending|Trending`) [daily 09:00 UTC]

+33 more (agent-buzz, daily-routine, evening-recap, reflect, token-pick, defi-overview, market-context-refresh, action-converter, search-skill, deal-flow, reg-monitor, skill-security-scan, vuln-scanner, autoresearch, list-digest, goal-tracker, skill-analytics, self-improve, thought-review, fork-cohort, skill-update-check, fleet-control, weekly-review, weekly-shiplog, operator-scorecard, fork-skill-digest, fork-skill-gap, skill-graph, on-chain-monitor, defi-monitor, token-movers, aixbt-pulse, unlock-monitor)

## Sources
- evals.json=ok · cron-state=ok · skill-health=ok (partial; 6 per-skill json files, none matching evals.json skills directly) · eval-audit=fail (sandbox restriction; in-memory fallback used; enabled_total=43 per 2026-07-05 heartbeat) · prior-article=ok (articles/skill-evals-2026-06-28.md)
