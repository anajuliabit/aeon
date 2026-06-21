# Skill Evals — 2026-06-21

**Verdict:** SKILL_EVALS_REGRESSED
**Coverage:** 14/44 (32%) ↑8pp vs prior 24% (fleet shrunk from ~57 → 44 enabled; reppo-* skills removed)
**Diff:** 3 new fail · 0 fixed · 1 still failing · 10 stable

> **Timing note:** skill-evals runs at 06:00 UTC (Sunday). Several log-based skills (token-alert 12:00 UTC, skill-health 18:00 UTC) had not yet run at eval time. The most recent log file `memory/logs/2026-06-21.md` is used for all `memory/logs/*.md` checks; patterns for those skills are absent. token-alert's FAIL may be a timing artefact; skill-health's FAIL is backed by 26 consecutive cron failures.

## Action Queue
1. Investigate skill-health — missing_pattern:### skill-health|SKILL_HEALTH|HEALTH: (26 consecutive failures, 0.26 success_rate; ISS-024)
2. Investigate token-alert — missing_pattern:### token-alert|TOKEN_ALERT (currently dispatched at eval time; timing issue likely; ISS-023)
3. Patch evals.json:monitor-polymarket — skill is disabled; remove entry to stop spurious FAIL/PASS churn (ISS-022)
4. Patch evals.json:hacker-news-digest — disabled skill, pattern never matches; remove entry or replace with `hn-digest:` sub-bullet pattern (failing since 2026-05-31, still unresolved)
5. Dispatch cost-report — no article since 2026-06-01 (20d; missed June 15 weekly run; now STALE past 14d threshold)
6. Add evals.json entry for skill-freshness — daily 08:00 UTC, active; `articles/skill-freshness-*.md`, pattern `FRESHNESS_OK|FRESHNESS_REGRESSED`
7. Add evals.json entry for morning-brief — daily 07:00 UTC; `memory/logs/*.md`, pattern `### morning-brief`
8. Add evals.json entry for btc-levels — 4-hourly; `memory/logs/*.md`, pattern `btc-levels`

## Regressions (NEW_FAIL)
| Skill | Status | Root cause | Issue |
|-------|--------|------------|-------|
| skill-health | NEW_FAIL | missing_pattern:### skill-health\|SKILL_HEALTH\|HEALTH: — 26 consecutive failures per cron-state; last success 2026-06-19 | ISS-024 |
| token-alert | NEW_FAIL | missing_pattern:### token-alert\|TOKEN_ALERT — skill dispatched at 13:45 UTC, pattern absent from 06:00 UTC log snapshot; 2 consecutive failures in cron-state | ISS-023 |
| monitor-polymarket | NEW_FAIL | missing_pattern:### monitor-polymarket\|## Polymarket\|POLYMARKET — disabled skill; prior PASS was spurious (all-caps `POLYMARKET` no longer present in today's log; prior eval flagged this as noise) | ISS-022 |

## Still Failing
| Skill | Status | Root cause | Issue | Failing since |
|-------|--------|------------|-------|---------------|
| hacker-news-digest | FAIL | missing_pattern:### hacker-news-digest\|## Hacker News\|HN_DIGEST — skill disabled, never writes pattern | none filed | 2026-05-31 |

## Full Results
| Skill | Status | Diff | Root cause | Quality | Words | Last output |
|-------|--------|------|------------|---------|-------|-------------|
| heartbeat | PASS | STABLE | — | unknown | ~9,000 | memory/logs/2026-06-21.md |
| skill-health | FAIL | NEW_FAIL | missing_pattern:### skill-health\|SKILL_HEALTH\|HEALTH: | unknown | ~9,000 | memory/logs/2026-06-21.md |
| token-alert | FAIL | NEW_FAIL | missing_pattern:### token-alert\|TOKEN_ALERT (timing) | unknown | ~9,000 | memory/logs/2026-06-21.md |
| monitor-polymarket | FAIL | NEW_FAIL | missing_pattern:POLYMARKET (disabled; spurious prior PASS) | unknown | ~9,000 | memory/logs/2026-06-21.md |
| hacker-news-digest | FAIL | STILL_FAIL | missing_pattern:### hacker-news-digest (disabled) | unknown | ~9,000 | memory/logs/2026-06-21.md |
| cost-report | STALE | PASS→STALE | stale_file (2026-06-01; 20d; 2× weekly=14d; missed June 15 auto-run) | unknown | 689 | articles/cost-report-2026-06-01.md |
| changelog | STALE | STABLE | stale_file (2026-03-19; 94d; disabled; 2× daily=2d) | unknown | ~620 | articles/changelog-2026-03-19.md |
| repo-pulse | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| push-recap | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| fork-fleet | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-article | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-actions | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| deep-research | NO_OUTPUT | STABLE | no_file_match (disabled, workflow_dispatch) | unknown | — | — |
| rss-digest | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |

## Coverage Gaps (enabled in aeon.yml, missing from evals.json)
Coverage ticked up 8pp purely because ~13 reppo-* skills were removed from aeon.yml (fleet shrunk 57 → 44 enabled), not because specs were added. Of 44 enabled skills, 40 remain uncovered.

- skill-freshness — inferred pattern: `articles/skill-freshness-*.md` (`FRESHNESS_OK|FRESHNESS_REGRESSED`) [daily 08:00 UTC]
- morning-brief — inferred pattern: `memory/logs/*.md` (`### morning-brief`) [daily 07:00 UTC]
- btc-levels — inferred pattern: `memory/logs/*.md` (`btc-levels`) [4-hourly]
- narrative-tracker — inferred pattern: `memory/logs/*.md` (`### narrative-tracker` or `NARRATIVE_TRACKER_OK`) [daily 13:30 UTC]
- defi-overview — inferred pattern: `memory/logs/*.md` (`### defi-overview`) [daily 12:00 UTC]
- security-digest — inferred pattern: `articles/security-digest-*.md` [daily 14:00 UTC]
- evening-recap — inferred pattern: `memory/logs/*.md` (`### evening-recap`) [daily 21:00 UTC]
- reflect — inferred pattern: `memory/logs/*.md` (`## Weekly Reflect|reflect`) [daily 18:00 UTC]
- agent-buzz — inferred pattern: `memory/logs/*.md` (`### agent-buzz|AGENT_BUZZ`) [daily 17:30 UTC]
- action-converter — inferred pattern: `memory/logs/*.md` (`## Action Converter|ACTION_CONVERTER`) [daily 18:00 UTC]
+30 more (morning-brief already listed; token-movers, on-chain-monitor, defi-monitor, token-pick, market-context-refresh, unlock-monitor, aixbt-pulse, search-skill, deal-flow, reg-monitor, skill-security-scan, vuln-scanner, autoresearch, list-digest, goal-tracker, skill-analytics, self-improve, thought-review, fork-cohort, skill-evals, skill-update-check, fleet-control, weekly-review, weekly-shiplog, operator-scorecard, fork-skill-digest, fork-skill-gap, skill-graph, daily-routine, github-trending)

## Sources
- evals.json=ok · cron-state=ok · skill-health=ok (partial; 4 per-skill files, none for evals.json skills) · eval-audit=fail (sandbox restriction; in-memory fallback used; enabled_total=44) · prior-article=ok (articles/skill-evals-2026-06-14.md)
