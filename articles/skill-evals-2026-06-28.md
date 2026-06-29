# Skill Evals — 2026-06-28

**Verdict:** SKILL_EVALS_REGRESSED
**Coverage:** 12/44 (27%) ↓5pp vs prior 32% (monitor-polymarket + hacker-news-digest removed from evals.json per 6-21 action items — intentional cleanup)
**Diff:** 1 new fail · 1 fixed · 2 still failing · 8 stable

> **Timing note:** skill-evals ran before heartbeat's ~08:00 UTC morning tick. Today's log (`memory/logs/2026-06-28.md`) has only btc-levels entries from 01:21Z and 05:06Z. All three log-based skills (heartbeat, token-alert, skill-health) wrote to `memory/logs/2026-06-27.md` yesterday (confirmed: `### Heartbeat — 08:18 UTC`, `### token-alert — ~12:08 UTC`, `skill-health — 18:10 UTC` all present). The heartbeat NEW_FAIL is a timing artefact; token-alert and skill-health are STILL_FAIL on timing + structural grounds (same as 6-21 eval). Cost-report is genuinely FIXED — 2026-06-24 article passes all assertions and is within the 14d staleness window.

## Action Queue
1. Schedule skill-evals after 21:00 UTC (or 22:00 UTC) to ensure all log-based skills have written for the day — eliminates timing-driven false-fails on heartbeat / token-alert / skill-health (ISS-026)
2. Investigate skill-health — missing_pattern:### skill-health|SKILL_HEALTH|HEALTH: (timing; last success 2026-06-27T18:16Z; sr 0.32; ISS-024)
3. Investigate token-alert — missing_pattern:### token-alert|TOKEN_ALERT (timing; last success 2026-06-27T12:43Z; sr 0.74; ISS-023)
4. Add evals.json entry for skill-freshness — daily 08:00 UTC, active; `articles/skill-freshness-*.md`, pattern `FRESHNESS_OK|FRESHNESS_NO_CHANGE`
5. Add evals.json entry for morning-brief — daily 07:00 UTC; `memory/logs/*.md`, pattern `### morning-brief`
6. Add evals.json entry for btc-levels — 4-hourly; `memory/logs/*.md`, pattern `btc-levels`
7. Add evals.json entry for narrative-tracker — daily 13:30 UTC; `memory/logs/*.md`, pattern `### narrative-tracker|NARRATIVE_TRACKER_OK`
8. Add evals.json entry for security-digest — daily 14:00 UTC; `articles/security-digest-*.md`, pattern `KEV|CVE-`

## Regressions (NEW_FAIL)
| Skill | Status | Root cause | Issue |
|-------|--------|------------|-------|
| heartbeat | NEW_FAIL | missing_pattern:heartbeat\|Heartbeat\|HEARTBEAT — timing artefact; skill-evals ran before 08:00 UTC morning tick; 2026-06-28.md has only btc-levels; skill healthy (sr 0.54, last_success 2026-06-27T20:22Z) | ISS-026 |

## Recovered (FIXED)
| Skill | Was | Now |
|-------|-----|-----|
| cost-report | STALE (articles/cost-report-2026-06-01.md, 20d old) | PASS (articles/cost-report-2026-06-24.md, 4d old — $237.60 / 67 runs / 0 anomalies) |

## Still Failing
| Skill | Status | Root cause | Issue | Failing since |
|-------|--------|------------|-------|---------------|
| token-alert | FAIL | missing_pattern:### token-alert\|TOKEN_ALERT — timing (runs 12:00 UTC; not yet in 2026-06-28.md); sr 0.74, genuinely healthy | ISS-023 | 2026-06-21 |
| skill-health | FAIL | missing_pattern:### skill-health\|SKILL_HEALTH\|HEALTH: — timing + structural (runs 18:00 UTC; sr 0.32) | ISS-024 | 2026-06-21 |

## Full Results
| Skill | Status | Diff | Root cause | Quality | Words | Last output |
|-------|--------|------|------------|---------|-------|-------------|
| heartbeat | FAIL | NEW_FAIL | missing_pattern:heartbeat (timing — pre-tick) | unknown | ~155 | memory/logs/2026-06-28.md |
| token-alert | FAIL | STILL_FAIL | missing_pattern:### token-alert (timing; ISS-023) | unknown | ~155 | memory/logs/2026-06-28.md |
| skill-health | FAIL | STILL_FAIL | missing_pattern:### skill-health (timing; ISS-024) | unknown | ~155 | memory/logs/2026-06-28.md |
| cost-report | PASS | FIXED | — | unknown | ~650 | articles/cost-report-2026-06-24.md |
| changelog | STALE | STABLE | stale_file (101d; disabled) | unknown | ~620 | articles/changelog-2026-03-19.md |
| repo-pulse | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| push-recap | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| fork-fleet | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-article | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-actions | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| deep-research | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| rss-digest | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |

> **Removed from scope (NEW_NO_COVERAGE):** monitor-polymarket and hacker-news-digest were in the 6-21 eval but removed from evals.json — per 6-21 Action Queue items 3 and 4 (disabled skills creating FAIL/PASS churn). Intentional cleanup, not a regression.

## Coverage Gaps (enabled in aeon.yml, missing from evals.json)
Coverage dropped 5pp (32%→27%) due to intentional evals.json cleanup (2 disabled-skill entries removed), not a fleet shrink. Of 44 enabled skills, only 4 have evals.json entries (heartbeat, cost-report, token-alert, skill-health). 40 enabled skills remain uncovered — same as 6-21. No new specs added since the last eval.

- skill-freshness — inferred pattern: `articles/skill-freshness-*.md` (`FRESHNESS_OK|FRESHNESS_NO_CHANGE`) [daily 08:00 UTC]
- morning-brief — inferred pattern: `memory/logs/*.md` (`### morning-brief`) [daily 07:00 UTC]
- btc-levels — inferred pattern: `memory/logs/*.md` (`btc-levels`) [4-hourly]
- narrative-tracker — inferred pattern: `memory/logs/*.md` (`### narrative-tracker|NARRATIVE_TRACKER_OK`) [daily 13:30 UTC]
- security-digest — inferred pattern: `articles/security-digest-*.md` (`KEV|CVE-`) [daily 14:00 UTC]

+35 more (defi-overview, token-pick, market-context-refresh, evening-recap, reflect, agent-buzz, action-converter, search-skill, deal-flow, reg-monitor, skill-security-scan, vuln-scanner, autoresearch, list-digest, goal-tracker, skill-analytics, self-improve, thought-review, fork-cohort, skill-update-check, fleet-control, weekly-review, weekly-shiplog, operator-scorecard, fork-skill-digest, fork-skill-gap, skill-graph, daily-routine, github-trending, on-chain-monitor, defi-monitor, token-movers, aixbt-pulse, unlock-monitor, self-improve)

## Sources
- evals.json=ok · cron-state=ok · skill-health=ok (partial; 4 per-skill json files, none matching evals.json skills directly) · eval-audit=fail (sandbox restriction; in-memory fallback used; enabled_total=44 per 2026-06-27 heartbeat) · prior-article=ok (articles/skill-evals-2026-06-21.md)
