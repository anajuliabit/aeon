# Skill Evals — 2026-08-02

**Verdict:** SKILL_EVALS_RECOVERED
**Coverage:** 12/43 (28%) — unchanged vs prior (2026-07-26)
**Diff:** 0 new fail · 2 fixed · 0 still failing · 10 stable

> **Timing note:** skill-evals dispatched after 22:00 UTC Sunday. All log-based skills have written today: heartbeat at 09:30 + 15:10 + 20:15 UTC, token-alert at 12:12 UTC, skill-health at 18:21 UTC. Evening recap fired at 21:41 UTC. No timing-driven false-fails.
>
> **Key recovery:** Both STILL_FAIL entries from 2026-07-26 (token-alert + skill-health) now PASS. The `### token-alert — 12:12 UTC` heading and `TOKEN_ALERT_OK` appeared in today's log; `### skill-health — 18:23 UTC` and `SKILL_HEALTH_NOOP` likewise. ISS-023 and ISS-024 were already resolved (2026-07-05) — no new issue actions needed.
>
> **Pattern correction for coverage gaps:** Prior eval (2026-07-26) suggested `articles/security-digest-*.md` and `articles/github-trending-*.md` as inferred output patterns. Neither path exists — both skills write to `memory/logs/*.md`. See Action Queue items 3 and 5.

## Action Queue

1. Add evals.json entry for skill-freshness — pattern: `articles/skill-freshness-*.md`, `FRESHNESS_OK|FRESHNESS_NO_CHANGE` [daily 08:00 UTC; files confirmed present]
2. Add evals.json entry for morning-brief — pattern: `memory/logs/*.md`, `### morning-brief|MORNING_BRIEF_OK` [daily 07:00 UTC]
3. Add evals.json entry for security-digest — pattern: `memory/logs/*.md`, `### security-digest|SECURITY_DIGEST_OK` [daily 14:00 UTC; prior-eval's `articles/security-digest-*.md` path was wrong — no such files exist]
4. Add evals.json entry for evening-recap — pattern: `memory/logs/*.md`, `### Evening Recap|Evening-recap|EVENING_RECAP` [daily 21:00 UTC]
5. Add evals.json entry for github-trending — pattern: `memory/logs/*.md`, `### github-trending|GITHUB_TRENDING_OK` [daily 09:00 UTC; prior-eval's `articles/github-trending-*.md` path was wrong — no such files exist]

+34 more — see Coverage Gaps

## Recovered (FIXED)

| Skill | Was | Now |
|-------|-----|-----|
| token-alert | FAIL (missing_pattern:### token-alert\|TOKEN_ALERT) | PASS |
| skill-health | FAIL (missing_pattern:### skill-health\|SKILL_HEALTH\|HEALTH:) | PASS |

## Full Results

| Skill | Status | Diff | Root cause | Quality | Words | Last output |
|-------|--------|------|------------|---------|-------|-------------|
| heartbeat | PASS | STABLE | — | unknown | large | memory/logs/2026-08-02.md |
| token-alert | PASS | FIXED | — | unknown | large | memory/logs/2026-08-02.md |
| skill-health | PASS | FIXED | — | unknown | large | memory/logs/2026-08-02.md |
| cost-report | PASS | STABLE | — | unknown | 200+ | articles/cost-report-2026-07-27.md |
| changelog | STALE | STABLE | stale_file (~136d; disabled) | unknown | 510+ | articles/changelog-2026-03-19.md |
| repo-pulse | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| push-recap | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| fork-fleet | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-article | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| repo-actions | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| deep-research | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |
| rss-digest | NO_OUTPUT | STABLE | no_file_match (disabled) | unknown | — | — |

## Coverage Gaps (enabled in aeon.yml, missing from evals.json)

Coverage 12/43 (28%). 4 of 12 evals.json skills are enabled (heartbeat, token-alert, skill-health, cost-report); 39 enabled skills remain uncovered.

- skill-freshness — inferred pattern: `articles/skill-freshness-*.md` (`FRESHNESS_OK|FRESHNESS_NO_CHANGE`) [daily 08:00 UTC — files confirmed present, highest-priority add]
- morning-brief — inferred pattern: `memory/logs/*.md` (`### morning-brief|MORNING_BRIEF_OK`) [daily 07:00 UTC]
- security-digest — inferred pattern: `memory/logs/*.md` (`### security-digest|SECURITY_DIGEST_OK`) [daily 14:00 UTC — corrected from prior eval's wrong articles/ path]
- evening-recap — inferred pattern: `memory/logs/*.md` (`Evening Recap|EVENING_RECAP`) [daily 21:00 UTC]
- github-trending — inferred pattern: `memory/logs/*.md` (`### github-trending|GITHUB_TRENDING_OK`) [daily 09:00 UTC — corrected from prior eval's wrong articles/ path]

+34 more (btc-levels, narrative-tracker, list-digest, agent-buzz, daily-routine, reflect, action-converter, goal-tracker, thought-review, search-skill, deal-flow, reg-monitor, skill-security-scan, vuln-scanner, autoresearch, self-improve, skill-analytics, fork-cohort, skill-update-check, weekly-review, weekly-shiplog, fork-skill-digest, fork-skill-gap, skill-graph, on-chain-monitor, defi-monitor, token-movers, aixbt-pulse, unlock-monitor, operator-scorecard, defi-overview, token-pick, market-context-refresh, narrative-tracker)

## Sources

- evals.json=ok · cron-state=ok · skill-health=ok (partial; 9 per-skill json files in memory/skill-health/) · eval-audit=fail (sandbox restriction) · prior-article=ok (articles/skill-evals-2026-07-26.md)
