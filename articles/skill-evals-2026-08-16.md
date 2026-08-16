# Skill Evals — 2026-08-16

**Verdict:** SKILL_EVALS_OK
**Coverage:** 12/43 (28%) — unchanged vs prior (2026-08-09)
**Diff:** 0 new fail · 0 fixed · 0 still failing · 12 stable

> **Timing note:** skill-evals dispatched Sunday 22:00 UTC. Log-based skills have written today: heartbeat at 08:33, 14:10, 20:15 UTC; token-alert at 12:33 UTC; skill-health at 18:19 UTC; evening-recap at 21:32 UTC. No timing-driven false-fails.
>
> **Week-over-week:** zero regressions, zero recoveries — a fully stable cycle for the 2nd consecutive week. The same 4 enabled skills (heartbeat, token-alert, skill-health, cost-report) continue to pass; the 8 disabled skills remain at STALE/NO_OUTPUT unchanged. Skill-graph ARCHITECTURE_OK (8-16) confirms 43 enabled skills and 191 total — fleet steady-state.
>
> **Coverage note:** Action Queue items 1–5 are identical to 2026-08-09 suggestions (skill-freshness, morning-brief, security-digest, evening-recap, github-trending). None were added to evals.json in the past 7 days. Operator pick-up still requested.

## Action Queue

1. Add evals.json entry for skill-freshness — pattern: `articles/skill-freshness-*.md`, `FRESHNESS_OK|FRESHNESS_NO_CHANGE` [daily 08:00 UTC — highest-priority add]
2. Add evals.json entry for morning-brief — pattern: `memory/logs/*.md`, `### morning-brief|MORNING_BRIEF_OK` [daily 07:00 UTC]
3. Add evals.json entry for security-digest — pattern: `memory/logs/*.md`, `### security-digest|SECURITY_DIGEST_OK` [daily 14:00 UTC]
4. Add evals.json entry for evening-recap — pattern: `memory/logs/*.md`, `### Evening Recap|EVENING_RECAP` [daily 21:00 UTC]
5. Add evals.json entry for github-trending — pattern: `memory/logs/*.md`, `### github-trending|GITHUB_TRENDING_OK` [daily 09:00 UTC]

+34 more — see Coverage Gaps

## Full Results

| Skill | Status | Diff | Root cause | Quality | Words | Last output |
|-------|--------|------|------------|---------|-------|-------------|
| heartbeat | PASS | STABLE | — | unknown | 15,513 (log) | memory/logs/2026-08-16.md |
| token-alert | PASS | STABLE | — | unknown | 15,513 (log) | memory/logs/2026-08-16.md |
| skill-health | PASS | STABLE | — | unknown | 15,513 (log) | memory/logs/2026-08-16.md |
| cost-report | PASS | STABLE | — | unknown | 683 | articles/cost-report-2026-08-11.md |
| changelog | STALE | STABLE | stale_file (~150d; disabled) | unknown | 510 | articles/changelog-2026-03-19.md |
| repo-pulse | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| push-recap | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| fork-fleet | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-article | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-actions | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| deep-research | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| rss-digest | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |

## Coverage Gaps (enabled in aeon.yml, missing from evals.json)

Coverage 12/43 (28%). 4 of 12 evals.json skills are enabled (heartbeat, token-alert, skill-health, cost-report); 39 enabled skills remain uncovered.

- skill-freshness — inferred pattern: `articles/skill-freshness-*.md` (`FRESHNESS_OK|FRESHNESS_NO_CHANGE`) [daily 08:00 UTC — files present at articles/skill-freshness-2026-08-16.md]
- morning-brief — inferred pattern: `memory/logs/*.md` (`### morning-brief|MORNING_BRIEF_OK`) [daily 07:00 UTC]
- security-digest — inferred pattern: `memory/logs/*.md` (`### security-digest|SECURITY_DIGEST_OK`) [daily 14:00 UTC]
- evening-recap — inferred pattern: `memory/logs/*.md` (`### Evening Recap|EVENING_RECAP`) [daily 21:00 UTC]
- github-trending — inferred pattern: `memory/logs/*.md` (`### github-trending|GITHUB_TRENDING_OK`) [daily 09:00 UTC]

+34 more (action-converter, agent-buzz, autoresearch, btc-levels, daily-routine, deal-flow, defi-monitor, defi-overview, aixbt-pulse, fork-cohort, fork-skill-digest, fork-skill-gap, goal-tracker, list-digest, market-context-refresh, narrative-tracker, on-chain-monitor, operator-scorecard, reflect, reg-monitor, search-skill, self-improve, skill-analytics, skill-evals, skill-graph, skill-security-scan, skill-update-check, thought-review, token-movers, token-pick, unlock-monitor, vuln-scanner, weekly-review, weekly-shiplog)

## Sources

- evals.json=ok · cron-state=ok · skill-health=ok (partial; 9 per-skill json files in memory/skill-health/) · eval-audit=fail (requires sandbox approval; fell back to in-memory coverage check) · prior-article=ok (articles/skill-evals-2026-08-09.md)
