# Skill Analytics — 2026-06-24

**Verdict:** 2 scheduled skill(s) didn't run this window — fork-skill-gap

*Window: last 7d · 828 runs across 44 skills · 34.2% success · 32 anomalies*

## Anomalies

| Flag | Skill | Detail | Action |
|------|-------|--------|--------|
| 🔴 SILENT | fork-skill-gap | scheduled `0 21 * * 0` but zero runs in window | check workflow / scheduler |
| 🔴 SILENT | operator-scorecard | scheduled `30 10 * * 1` but zero runs in window | check workflow / scheduler |
| 🟠 LOW_SUCCESS | cost-report | 2.6% over 39 runs | review failures |
| 🟠 LOW_SUCCESS | vuln-scanner | 3.8% over 26 runs | review failures |
| 🟠 LOW_SUCCESS | skill-evals | 12.5% over 8 runs | review failures |
| 🟠 LOW_SUCCESS | security-digest | 13.9% over 36 runs | review failures |
| 🟠 LOW_SUCCESS | search-skill | 15.0% over 40 runs | review failures |
| 🟠 LOW_SUCCESS | market-context-refresh | 15.6% over 45 runs | review failures |
| 🟠 LOW_SUCCESS | narrative-tracker | 18.9% over 37 runs | review failures |
| 🟠 LOW_SUCCESS | list-digest | 19.4% over 36 runs | review failures |
| 🟠 LOW_SUCCESS | agent-buzz | 21.9% over 32 runs | review failures |
| 🟠 LOW_SUCCESS | skill-health | 22.6% over 31 runs | review failures |
| 🟠 LOW_SUCCESS | goal-tracker | 23.3% over 30 runs | review failures |
| 🟠 LOW_SUCCESS | reflect | 23.3% over 30 runs | review failures |
| 🟠 LOW_SUCCESS | github-trending | 24.0% over 25 runs | review failures |
| 🟠 LOW_SUCCESS | action-converter | 24.1% over 29 runs | review failures |
| 🟠 LOW_SUCCESS | skill-freshness | 28.6% over 21 runs | review failures |
| 🟠 LOW_SUCCESS | evening-recap | 29.2% over 24 runs | review failures |
| 🟠 LOW_SUCCESS | fleet-control | 30.8% over 39 runs | review failures |
| 🟠 LOW_SUCCESS | heartbeat | 32.7% over 49 runs | review failures |
| 🟠 LOW_SUCCESS | skill-analytics | 33.3% over 3 runs | review failures |
| 🟠 LOW_SUCCESS | thought-review | 41.4% over 29 runs | review failures |
| 🟠 LOW_SUCCESS | aixbt-pulse | 43.3% over 30 runs | review failures |
| 🟠 LOW_SUCCESS | daily-routine | 43.8% over 16 runs | review failures |
| 🟠 LOW_SUCCESS | defi-overview | 50.0% over 18 runs | review failures |
| 🟠 LOW_SUCCESS | token-pick | 52.9% over 17 runs | review failures |
| 🟠 LOW_SUCCESS | token-alert | 54.5% over 11 runs | review failures |
| 🟠 LOW_SUCCESS | btc-levels | 54.8% over 62 runs | review failures |
| 🟠 LOW_SUCCESS | morning-brief | 58.3% over 12 runs | review failures |
| 🟠 LOW_SUCCESS | defi-monitor | 63.6% over 11 runs | review failures |
| 🟠 LOW_SUCCESS | reg-monitor | 66.7% over 3 runs | review failures |
| 🟠 LOW_SUCCESS | token-movers | 69.2% over 13 runs | review failures |

> **Note:** The 30 LOW_SUCCESS flags predominantly reflect the systemic `output_tokens=0` sandbox-truncation cluster documented in MEMORY.md (ISS-019/020/021/024/025). Skills with recent successful runs (e.g. reg-monitor 6-24, defi-monitor 6-24, token-movers 6-24) are recovering within this run-count window. This is an infrastructure anomaly, not a capability regression.

## Top runners (by run count)

| # | Skill | Runs | Success | Last status | Dominant exit |
|---|-------|------|---------|-------------|---------------|
| 1 | btc-levels | 62 | 54.8% | success | uncategorized |
| 2 | heartbeat | 49 | 32.7% | success | ok |
| 3 | market-context-refresh | 45 | 15.6% | success | ok |
| 4 | search-skill | 40 | 15.0% | success | uncategorized |
| 5 | cost-report | 39 | 2.6% | success | uncategorized |
| 6 | fleet-control | 39 | 30.8% | success | uncategorized |
| 7 | narrative-tracker | 37 | 18.9% | success | ok |
| 8 | list-digest | 36 | 19.4% | success | ok |
| 9 | security-digest | 36 | 13.9% | success | ok |
| 10 | agent-buzz | 32 | 21.9% | success | ok |
| 11 | skill-health | 31 | 22.6% | success | partial |
| 12 | aixbt-pulse | 30 | 43.3% | success | ok |
| 13 | goal-tracker | 30 | 23.3% | success | ok |
| 14 | reflect | 30 | 23.3% | success | ok |
| 15 | action-converter | 29 | 24.1% | success | ok |

## Failure rate (sorted, ≥1 failure)

| Skill | Runs | Failures | Success rate | Last conclusion |
|-------|------|----------|--------------|-----------------|
| vuln-scanner | 26 | 25 | 3.8% | success |
| narrative-tracker | 37 | 29 | 18.9% | success |
| security-digest | 36 | 28 | 13.9% | success |
| market-context-refresh | 45 | 35 | 15.6% | success |
| reflect | 30 | 23 | 23.3% | success |
| action-converter | 29 | 22 | 24.1% | success |
| goal-tracker | 30 | 22 | 23.3% | success |
| agent-buzz | 32 | 23 | 21.9% | success |
| skill-health | 31 | 22 | 22.6% | success |
| evening-recap | 24 | 17 | 29.2% | success |
| search-skill | 40 | 28 | 15.0% | success |
| list-digest | 36 | 25 | 19.4% | success |
| cost-report | 39 | 27 | 2.6% | success |
| fleet-control | 39 | 27 | 30.8% | success |
| skill-evals | 8 | 5 | 12.5% | success |
| thought-review | 29 | 17 | 41.4% | success |
| heartbeat | 49 | 28 | 32.7% | success |
| skill-freshness | 21 | 12 | 28.6% | success |
| aixbt-pulse | 30 | 17 | 43.3% | success |
| github-trending | 25 | 11 | 24.0% | success |
| btc-levels | 62 | 27 | 54.8% | success |
| morning-brief | 12 | 5 | 58.3% | success |
| daily-routine | 16 | 5 | 43.8% | success |
| defi-monitor | 11 | 4 | 63.6% | success |
| reg-monitor | 3 | 1 | 66.7% | success |
| skill-analytics | 3 | 1 | 33.3% | in_progress |
| defi-overview | 18 | 3 | 50.0% | success |
| token-pick | 17 | 3 | 52.9% | success |
| token-alert | 11 | 2 | 54.5% | success |
| token-movers | 13 | 2 | 69.2% | success |
| self-improve | 5 | 1 | 80.0% | success |

## Exit taxonomy distribution

| Bucket | Count | % | Top skills |
|--------|-------|---|------------|
| ok | 25 | 56.8% | narrative-tracker, heartbeat, defi-monitor, agent-buzz, list-digest, token-alert, token-movers, market-context-refresh, on-chain-monitor, defi-overview, security-digest, reg-monitor, goal-tracker, reflect, action-converter, aixbt-pulse, skill-freshness, github-trending, daily-routine, evening-recap, fork-cohort, fork-skill-digest, soul-builder, unlock-monitor, skill-graph |
| uncategorized | 17 | 38.6% | btc-levels, search-skill, cost-report, fleet-control, self-improve, vuln-scanner, thought-review, skill-evals, skill-analytics, deal-flow, fetch-tweets, project-lens, morning-brief, weekly-review, weekly-shiplog, skill-security-scan, skill-update-check |
| partial | 1 | 2.3% | skill-health |
| skip-other | 1 | 2.3% | token-pick |
| skip_unchanged | 0 | 0% | — |
| new_info | 0 | 0% | — |
| error | 0 | 0% | — |

*Sourced from `memory/logs/*.md` — best-effort regex grep, see Step 5. 12 log files scanned (8 primary dates + 4 supplementary). ~39% uncategorized reflects skills that emit status markers not yet indexed by the daily-log pattern.*

## Silent scheduled skills (enabled, zero runs)

| Skill | Schedule | Note |
|-------|----------|------|
| fork-skill-gap | `0 21 * * 0` (Sunday 21:00 UTC) | Last Sunday 6-21 should have fired; no cron-state entry — possible first run or scheduler miss |
| operator-scorecard | `30 10 * * 1` (Monday 10:30 UTC) | Last Monday 6-22 should have fired; no runs in GitHub Actions within 7d window |

## Source status

- skill-runs JSON: ok (fetched via `gh api` directly — `./scripts/skill-runs` sandbox-gated this run)
- Window: 168h (2026-06-17T18:54:04Z → 2026-06-24T~19:00:00Z)
- aeon.yml: ok
- cron-state.json: ok
- Daily logs scanned: 12/8 expected (8 primary dates + 4 supplementary overflow logs for 6-19 and 6-21)

---
*Companion to `skill-health` (per-skill issue filing) and `heartbeat` (per-run pulse). Fleet-wide observability is the gap this skill closes. Methodology: GitHub Actions run history is ground truth for pass/fail; daily-log markers are best-effort secondary signal for exit taxonomy.*
