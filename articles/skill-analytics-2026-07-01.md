# Skill Analytics — 2026-07-01

**Verdict:** 2 scheduled skill(s) didn't run this window — fork-skill-gap, operator-scorecard

*Window: last 7d · ~270 runs across 42 skills · 99.6% success · 3 anomalies*

## Anomalies

| Flag | Skill | Detail | Action |
|------|-------|--------|--------|
| 🔴 SILENT | fork-skill-gap | scheduled `0 21 * * 0` but zero runs in window (June 28 Sunday 21:00 slot missed) | check workflow / scheduler — not in cron-state, appears never to have run |
| 🔴 SILENT | operator-scorecard | scheduled `30 10 * * 1` but zero runs in window (June 29 Monday 10:30 slot missed) | known scheduler-side gap per MEMORY.md; "Mon 10:30Z slot perpetually MISSED" |
| 🟠 LOW_SUCCESS | cost-report | 29% success over 7 runs (2 success, 1 failure, 4 cancelled) | review failure root cause; 11% lifetime success per cron-state (ISS still open?) |

> **Note:** fleet-control is marked `enabled: false` in aeon.yml but ran 10 times in the window — manual dispatches or stale scheduler state. Not flagged by anomaly taxonomy (not in SCHEDULED_SKILLS), but worth verifying scheduler sync.

## Top runners (by run count)

| # | Skill | Runs | Success | Last status | Dominant exit |
|---|-------|------|---------|-------------|---------------|
| 1 | btc-levels | 47 | 100% | success | ok |
| 2 | heartbeat | 23 | 100% | success | ok |
| 3 | thought-review (24) | 15 | 100% | success | uncategorized |
| 4 | fleet-control | 10 | 100% | success | uncategorized |
| 5 | aixbt-pulse | 10 | 100% | success | uncategorized |
| 6 | action-converter | 8 | 100% | success | ok |
| 7 | agent-buzz | 8 | 100% | success | ok |
| 8 | daily-routine | 8 | 100% | success | ok |
| 9 | github-trending | 8 | 100% | success | uncategorized |
| 10 | goal-tracker | 8 | 100% | success | ok |
| 11 | list-digest | 8 | 100% | success | ok |
| 12 | morning-brief | 8 | 100% | success | uncategorized |
| 13 | reflect | 8 | 100% | success | ok |
| 14 | search-skill | 8 | 100% | success | uncategorized |
| 15 | security-digest | 8 | 100% | success | ok |

*(skill-freshness, skill-health, token-alert each also at 8 runs — all 100%)*

## Failure rate (sorted, ≥1 failure)

| Skill | Runs | Failures | Success rate | Last conclusion |
|-------|------|----------|--------------|-----------------|
| cost-report | 7 | 1 | 29% (2/7, 4 cancelled) | success |

*(fork-skill-digest had 1 cancelled run with 0 successes but total < 2 — not classified as ALL_FAIL)*

Zero outright failures across all other 41 active skills this window.

## Exit taxonomy distribution

| Bucket | Count | % | Top skills |
|--------|-------|---|------------|
| ok | ~20 skills | ~48% | heartbeat, daily-routine, skill-freshness, token-alert, agent-buzz, list-digest, goal-tracker, reflect, action-converter, security-digest, narrative-tracker, defi-monitor, defi-overview, on-chain-monitor, token-movers |
| uncategorized | ~21 skills | ~50% | btc-levels, thought-review, github-trending, search-skill, morning-brief, evening-recap, market-context-refresh, token-pick, fleet-control, aixbt-pulse |
| partial | 1 skill | ~2% | skill-health (SKILL_HEALTH_PARTIAL — sandbox blocks skill-runs CLI, 5+ of 8 runs used cron-state-only fallback) |
| skip_unchanged | 0 | 0% | — |
| new_info | 0 | 0% | — |
| error | 0 | 0% | — |

*(Sourced from memory/logs/2026-06-24.md through 2026-07-01.md — 8 log files scanned, best-effort regex. ~50% uncategorized rate expected for skills without explicit _OK markers in log format.)*

## Silent scheduled skills (enabled, zero runs)

| Skill | Schedule | Expected run(s) in window |
|-------|----------|--------------------------|
| fork-skill-gap | `0 21 * * 0` | June 28 21:00 UTC (Sunday) |
| operator-scorecard | `30 10 * * 1` | June 29 10:30 UTC (Monday) |

> Both skills have zero cron-state entries — they appear to have never run. Known chronic gaps per fleet-health snapshot 2026-06-30.

## Notable observations

- **12:00 batch stalled**: token-movers, token-pick, defi-overview, defi-monitor, on-chain-monitor, market-context-refresh all have only 5 runs (June 24–28 only) vs 7+ expected. Last dispatches in cron-state: 2026-06-28. Three consecutive days (June 29–July 1) with no 12:00 batch firing. Not SILENT (runs exist in window) but scheduler drift worth investigating — possible chain with PR #150 (`usepod_model` → `model:`) still unmerged at ~44h.
- **fork-skill-digest**: 1 cancelled run on June 28, stuck since June 28 18:38Z dispatch — per MEMORY.md "~68h+ carry". Beyond the 48h dedup window; next Sunday (July 5) fresh dispatch.
- **fleet-control disabled but active**: 10 runs in window with enabled: false in aeon.yml. Scheduler sync needed.

## Source status

- skill-runs JSON: sandbox-blocked (`./scripts/skill-runs` requires approval in this surface); fallback to `gh api repos/{owner}/{repo}/actions/runs --paginate` with jq aggregation
- Window: 168h (2026-06-24 ~19:13Z → 2026-07-01 ~19:13Z); API query used `created>=2026-06-24` (slightly wider boundary, ~11 extra runs from June 24 00:00–19:13 may be included)
- Total captured: ~270 runs across 6 paginated API pages (confirmed 5 pages × 49–57 runs + ~11 partial 6th page)
- aeon.yml: ok
- cron-state.json: ok (44 skills tracked)
- Daily logs scanned: 8/8 for exit taxonomy (2026-06-24 through 2026-07-01)

---
*Companion to `skill-health` (per-skill issue filing) and `heartbeat` (per-run pulse). Fleet-wide observability is the gap this skill closes. Methodology: GitHub Actions run history is ground truth for pass/fail; daily-log markers are best-effort secondary signal for exit taxonomy.*
