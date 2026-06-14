# Skill Evals — 2026-06-14

**Verdict:** SKILL_EVALS_RECOVERED
**Coverage:** 14/57 (24%) ↓24pp vs prior 48% ⚠ COVERAGE CLIFF
**Diff:** 0 new fail · 1 fixed · 1 still failing · 12 stable

> **Timing note:** Today's log (memory/logs/2026-06-14.md) only contained btc-levels entries (pre-08:00 UTC; daily skills haven't fired yet). All memory/logs/*.md pattern checks used memory/logs/2026-06-13.md as the most recent complete daily log.

## Action Queue
1. Patch evals.json:monitor-polymarket — pattern `POLYMARKET` too broad; matched narrative-tracker content (`POLYMARKET US DEBUT`), not skill output; tighten to `### monitor-polymarket` only
2. Patch evals.json:hacker-news-digest — pattern never matches disabled skill; hn-digest runs inline in daily-routine as `- hn-digest:` sub-bullet; update pattern to `hn-digest:` or remove entry (same as 2026-05-31 action queue, still unresolved)
3. Dispatch cost-report — June 8 dispatch stuck at `dispatched`; last article 13d old (borderline 2× weekly cadence); next auto-run June 15 (tomorrow)
4. Add evals.json entry for btc-levels — active 4-hourly (20 runs); `memory/logs/*.md`, pattern `btc-levels`
5. Add evals.json entry for morning-brief — active daily 07:00 UTC (20 runs); `memory/logs/*.md`, pattern `### morning-brief`
6. Add evals.json entry for skill-freshness — active daily (19 runs); `articles/skill-freshness-*.md`, pattern `FRESHNESS_OK|FRESHNESS_REGRESSED|FRESHNESS_NO_CHANGE`
7. Add evals.json entry for narrative-tracker — active daily (7 runs); `memory/logs/*.md`, pattern `### narrative-tracker`
8. +39 more uncovered enabled skills — see Coverage Gaps

## Recovered (FIXED)
| Skill | Was | Now |
|-------|-----|-----|
| monitor-polymarket | FAIL (missing_pattern) | PASS ⚠ spurious — `POLYMARKET` matched from narrative-tracker log entry, not from the skill itself (disabled). Tighten pattern per action 1. |

## Still Failing
| Skill | Status | Root cause | Issue | Failing since |
|-------|--------|------------|-------|---------------|
| hacker-news-digest | FAIL | missing_pattern:### hacker-news-digest\|## Hacker News\|HN_DIGEST | none filed | 2026-05-31 |

## Full Results
| Skill | Status | Diff | Root cause | Quality | Words | Last output |
|-------|--------|------|------------|---------|-------|-------------|
| heartbeat | PASS | STABLE | — | unknown | ~11,600 | memory/logs/2026-06-13.md |
| cost-report | PASS | STABLE | — (June 8 dispatch stuck; see action 3) | unknown | 689 | articles/cost-report-2026-06-01.md |
| token-alert | PASS | STABLE | — | unknown | ~11,600 | memory/logs/2026-06-13.md |
| skill-health | PASS | STABLE | — | unknown | ~11,600 | memory/logs/2026-06-13.md |
| monitor-polymarket | PASS | FIXED | spurious — see Recovered note | unknown | ~11,600 | memory/logs/2026-06-13.md |
| hacker-news-digest | FAIL | STILL_FAIL | missing_pattern:### hacker-news-digest\|## Hacker News\|HN_DIGEST (skill disabled) | unknown | ~11,600 | memory/logs/2026-06-13.md |
| changelog | STALE | STABLE | stale_file (2026-03-19; 87d; cron schedule 0 16 * * * but skill disabled; 2× daily threshold = 2d) | unknown | ~620 | articles/changelog-2026-03-19.md |
| repo-pulse | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| push-recap | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| fork-fleet | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-article | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-actions | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| deep-research | NO_OUTPUT | STABLE | no_file_match (disabled, workflow_dispatch) | unknown | — | — |
| rss-digest | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |

## Coverage Gaps (enabled in aeon.yml, missing from evals.json)
Coverage has fallen from 48% → 24% (24pp drop) since 2026-05-31 because ~28 new skills were added to the fleet without corresponding eval specs.

- btc-levels — inferred pattern: `memory/logs/*.md` (btc-levels) [4-hourly, 20 runs]
- morning-brief — inferred pattern: `memory/logs/*.md` (### morning-brief) [daily, 20 runs]
- evening-recap — inferred pattern: `memory/logs/*.md` (### evening-recap) [daily, 20 runs]
- fleet-control — inferred pattern: `memory/logs/*.md` (### fleet-control) [daily, 27 runs]
- skill-freshness — inferred pattern: `articles/skill-freshness-*.md` [daily, 19 runs]
- narrative-tracker — inferred pattern: `memory/logs/*.md` (### narrative-tracker) [daily, 7 runs]
- goal-tracker — inferred pattern: `memory/logs/*.md` (### goal-tracker) [daily, 19 runs]
- defi-overview — inferred pattern: `memory/logs/*.md` (### defi-overview) [daily, 23 runs]
- security-digest — inferred pattern: `articles/security-digest-*.md` [daily, 9 runs]
- thought-review — inferred pattern: `memory/logs/*.md` (### Thought Review) [daily, 9 runs]
+33 more (action-converter, agent-buzz, reflect, github-trending, token-pick, token-movers, market-context-refresh, aixbt-pulse, on-chain-monitor, defi-monitor, daily-routine, list-digest, self-improve, skill-analytics, vuln-scanner, reg-monitor, weekly-review, weekly-shiplog, fork-cohort, search-skill, reppo-digest, reppo-orchestrator, reppo-voter, reppo-trading-agent, deal-flow, skill-graph, skill-update-check, skill-evals itself, and others)

## Sources
- evals.json=ok · cron-state=ok · skill-health=ok (partial; 4 per-skill files for non-evals skills) · eval-audit=fail (sandbox restriction; in-memory fallback used; enabled_total estimate ~57) · prior-article=ok (articles/skill-evals-2026-05-31.md)
