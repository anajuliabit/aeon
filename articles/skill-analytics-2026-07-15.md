# Skill Analytics — 2026-07-15

**Verdict:** 10 scheduled skill(s) didn't run this window — aixbt-pulse (day-17 dark streak, ISS-027 scheduler block)

*Window: last 7d · 172 runs across 30 skills · 98.1% success · 11 anomalies*

## Anomalies

| Flag | Skill | Detail | Action |
|------|-------|--------|--------|
| 🔴 SILENT | aixbt-pulse | scheduled `0 9,21 * * *` (twice daily), zero runs since 2026-06-28 (day-17 dark) | ISS-027 scheduler fix — operator direct-author |
| 🔴 SILENT | token-pick | scheduled daily ~12:00Z, zero runs since 2026-06-28 (day-17 dark) | ISS-027 scheduler fix — operator direct-author |
| 🔴 SILENT | defi-overview | scheduled daily ~12:00Z, zero runs since 2026-06-28 (day-17 dark) | ISS-027 scheduler fix — operator direct-author |
| 🔴 SILENT | token-movers | scheduled daily ~12:00Z, zero runs since 2026-06-28 (day-17 dark) | ISS-027 scheduler fix — operator direct-author |
| 🔴 SILENT | on-chain-monitor | scheduled daily ~12:00Z, zero runs since 2026-06-28 (day-17 dark) | ISS-027 scheduler fix — operator direct-author |
| 🔴 SILENT | defi-monitor | scheduled daily ~12:00Z, zero runs since 2026-06-28 (day-17 dark) | ISS-027 scheduler fix — operator direct-author |
| 🔴 SILENT | market-context-refresh | scheduled daily ~12:00Z, zero runs since 2026-06-28 (day-17 dark) | ISS-027 scheduler fix — operator direct-author |
| 🔴 SILENT | narrative-tracker | scheduled daily ~12:00Z, zero runs since 2026-06-28 (day-17 dark) | ISS-027 scheduler fix — operator direct-author |
| 🔴 SILENT | weekly-shiplog | scheduled `0 9 * * 1` (Monday), zero runs since 2026-06-29 (15d stale — missed 7-13 Monday) | ISS-027 scheduler fix — operator direct-author |
| 🔴 SILENT | deal-flow | scheduled `0 14 * * 1` (Monday), zero runs in window (last 2026-07-06, missed 7-13 Monday) | ISS-027 scheduler fix — operator direct-author |
| 🟠 CONSECUTIVE_FAILURES | cost-report | 5-run failure streak (cf=5 from cron-state); 3 failures + 3 cancellations this window; last_success 2026-06-29 (16d ago) | see ISS-025; sandbox-truncation family — capture-step PR required |

## Top runners (by run count)

| # | Skill | Runs | Success | Last status | Dominant exit |
|---|-------|------|---------|-------------|---------------|
| 1 | btc-levels | 32 | 100% | success | quiet (alert-gated) |
| 2 | heartbeat | 19 | 100% | success | ok |
| 3 | thought-review | 14 | 100% | success | ok |
| 4 | morning-brief | 7 | 100% | success | ok |
| 5 | daily-routine | 7 | 100% | success | ok |
| 6 | evening-recap | 7 | 100% | success | ok |
| 7 | list-digest | 7 | 100% | success | ok |
| 8 | agent-buzz | 7 | 100% | success | ok |
| 9 | action-converter | 7 | 86%† | in_progress | ok |
| 10 | reflect | 7 | 86%† | in_progress | ok |
| 11 | skill-health | 7 | 86%† | in_progress | ok |
| 12 | goal-tracker | 7 | 86%† | in_progress | ok |
| 13 | security-digest | 6 | 100% | success | ok |
| 14 | skill-freshness | 6 | 100% | success | ok |
| 15 | cost-report | 6 | 0% | cancelled | error |

*† 6/7 runs completed as success; 1 currently in_progress (07-15 18:00Z even-day batch)*

## Failure rate (sorted, ≥1 failure)

| Skill | Runs | Failures | Success rate | Last conclusion |
|-------|------|----------|--------------|-----------------|
| cost-report | 6 | 3 | 0% | cancelled |

*3 additional runs cancelled (total 6 dispatches, 0 clean completions this window). Prior failures consistent with ISS-025 sandbox-truncation / outputTokens mid-JSON truncation.*

## Exit taxonomy distribution

| Bucket | Count | % | Top skills |
|--------|-------|---|------------|
| ok | ~105 | ~61% | agent-buzz, list-digest, action-converter, reflect, skill-health, goal-tracker, morning-brief, daily-routine, heartbeat, github-trending, token-alert |
| quiet | ~52 | ~30% | btc-levels (32 runs, most no-crossing exits), thought-review, evening-recap, skill-freshness |
| skip_other | ~1 | <1% | search-skill (SEARCH_SKILL_NO_GAP — fleet capability-complete day-19) |
| error | ~3 | ~2% | cost-report (3 failure exits) |
| uncategorized | ~11 | ~6% | skill-evals, fork-cohort, skill-graph, vuln-scanner, weekly-review, unlock-monitor, skill-security-scan |

*Sourced from `memory/logs/*.md` — best-effort regex grep, see SKILL.md Step 5. Ground truth for pass/fail is GitHub Actions run history above.*

## Silent scheduled skills (enabled, zero runs)

10 skills fired zero times despite active cron schedules:

| Skill | Schedule | Last success | Days dark |
|-------|----------|--------------|-----------|
| aixbt-pulse | `0 9,21 * * *` | 2026-06-28 | 17 |
| token-pick | daily ~12:00Z | 2026-06-28 | 17 |
| defi-overview | daily ~12:00Z | 2026-06-28 | 17 |
| token-movers | daily ~12:00Z | 2026-06-28 | 17 |
| on-chain-monitor | daily ~12:00Z | 2026-06-28 | 17 |
| defi-monitor | daily ~12:00Z | 2026-06-28 | 17 |
| market-context-refresh | daily ~12:00Z | 2026-06-28 | 17 |
| narrative-tracker | daily ~12:00Z | 2026-06-28 | 17 |
| weekly-shiplog | `0 9 * * 1` | 2026-06-29 | 16 |
| deal-flow | `0 14 * * 1` | 2026-07-06 | 9 |

Root cause: ISS-027 scheduler primitive block (aeon.yml workflow-file class) affects the 12:00Z batch cluster + Monday slot skills. Rule-5 constraint means operator direct-author is required to fix the aeon.yml scheduler entries.

Note: 7-13 (Monday) also saw skill-freshness, github-trending, and security-digest miss their 08:00Z / 09:00Z / 14:00Z slots despite running on other days — likely a transient GH Actions scheduling gap on that day rather than a permanent SILENT condition.

## Source status

- skill-runs JSON: gh api direct (--paginate, 2026-07-08 19:25Z → 2026-07-15 19:25Z)
- Window: 168h (2026-07-08T19:25:57Z → 2026-07-15T19:25:57Z)
- aeon.yml: ok
- cron-state.json: ok (consecutive_failures cross-referenced for cost-report cf=5)
- Daily logs scanned: 8/8 (2026-07-08 → 2026-07-15) for exit taxonomy

---
*Companion to `skill-health` (per-skill issue filing) and `heartbeat` (per-run pulse). Fleet-wide observability is the gap this skill closes. Methodology: GitHub Actions run history is ground truth for pass/fail; daily-log markers are best-effort secondary signal for exit taxonomy.*
