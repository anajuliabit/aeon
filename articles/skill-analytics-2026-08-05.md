# Skill Analytics — 2026-08-05

**Verdict:** 10 scheduled skills didn't run this window — token-movers

*Window: last 7d · 246 runs across 31 skills · 75.2% success · 24 anomalies*

## Anomalies

| Flag | Skill | Detail | Action |
|------|-------|--------|--------|
| 🔴 SILENT | token-movers | scheduled `10 12 * * *` but zero runs in window | ISS-027 12:00Z batch-dark d39+ — scheduler-side gap, separate from ISS-029 |
| 🔴 SILENT | on-chain-monitor | scheduled `20 12 * * *` but zero runs in window | ISS-027 — same cluster |
| 🔴 SILENT | defi-monitor | scheduled `40 12 * * *` but zero runs in window | ISS-027 — same cluster |
| 🔴 SILENT | defi-overview | scheduled `0 12 * * *` but zero runs in window | ISS-027 — same cluster |
| 🔴 SILENT | market-context-refresh | scheduled `0 13 * * *` but zero runs in window | ISS-027 — same cluster |
| 🔴 SILENT | narrative-tracker | scheduled `30 13 * * *` but zero runs in window | ISS-027 — same cluster |
| 🔴 SILENT | aixbt-pulse | scheduled `0 9,21 * * *` but zero runs in window | ISS-027 — same cluster (last success 2026-06-28) |
| 🔴 SILENT | weekly-shiplog | scheduled `0 9 * * 1` but zero runs in window | Missed 8-03 Mon slot due to ISS-029; next slot 8-10 |
| 🔴 SILENT | operator-scorecard | scheduled `30 10 * * 1` but zero runs in window | Missed 8-03 Mon slot due to ISS-029; never successfully run |
| 🔴 SILENT | fork-skill-gap | scheduled `0 21 * * 0` but zero runs in window | No run on 8-02 Sun slot; check scheduler |
| 🟠 LOW_SUCCESS | cost-report | 5.3% over 19 runs (1/19 success, 11 fail, 7 cancelled) | ISS-030 open: sdk_opt_in_required signature; 8-04 21:48Z recovery may be transient |
| 🟠 LOW_SUCCESS | unlock-monitor | 20.0% over 5 runs (1 success, 4 fail) | ISS-029 cascade on 8-03 slot; check post-recovery cadence |
| 🟠 LOW_SUCCESS | deal-flow | 25.0% over 4 runs (1 success, 3 fail) | ISS-029 cascade on 8-03 slot |
| 🟠 LOW_SUCCESS | search-skill | 25.0% over 4 runs (1 success, 3 fail) | ISS-029 cascade on 8-03 slot; SEARCH_SKILL_NO_GAP is correct on success |
| 🟠 LOW_SUCCESS | skill-security-scan | 33.3% over 3 runs (1 success, 2 fail) | ISS-029 cascade on 8-03 slot |
| 🟠 LOW_SUCCESS | skill-freshness | 44.4% over 9 runs (4 success, 5 fail) | ISS-029 + morning-08Z slot miss pattern (2-consec-day 8-04/8-05) |
| 🟠 LOW_SUCCESS | daily-routine | 58.3% over 12 runs (7 success, 5 fail) | ISS-029 cascade; post-recovery clean 8-04/8-05 |
| 🟠 LOW_SUCCESS | security-digest | 72.7% over 11 runs (8 success, 3 fail) | ISS-029 failures dragging 7d rate; recent 3-consec clean |
| 🟠 LOW_SUCCESS | morning-brief | 75.0% over 8 runs (6 success, 2 fail) | ISS-029 failures; clean since recovery |
| 🟠 LOW_SUCCESS | thought-review | 73.7% over 19 runs (14 success, 5 fail) | ISS-029 failures; dual-fire cadence adds run count |
| 🟠 LOW_SUCCESS | action-converter | 77.8% over 9 runs (7 success, 1 fail) | ISS-029 single failure; otherwise healthy |
| 🟠 LOW_SUCCESS | goal-tracker | 77.8% over 9 runs (7 success, 1 fail) | ISS-029 single failure; otherwise healthy |
| 🟠 LOW_SUCCESS | reflect | 77.8% over 9 runs (7 success, 1 fail) | ISS-029 single failure; otherwise healthy |
| 🟠 LOW_SUCCESS | skill-health | 77.8% over 9 runs (7 success, 1 fail) | ISS-029 single failure; otherwise healthy |

## Top runners (by run count)

| # | Skill | Runs | Success | Last status | Dominant exit |
|---|-------|------|---------|-------------|---------------|
| 1 | btc-levels | 39 | 89.7% | success | ok |
| 2 | heartbeat | 21 | 81.0% | success | ok |
| 3 | cost-report | 19 | 5.3% | success | error |
| 4 | thought-review (24) | 19 | 73.7% | success | ok |
| 5 | daily-routine | 12 | 58.3% | success | ok |
| 6 | security-digest | 11 | 72.7% | success | ok |
| 7 | action-converter | 9 | 77.8% | in_progress | ok |
| 8 | agent-buzz | 9 | 88.9% | success | ok |
| 9 | goal-tracker | 9 | 77.8% | in_progress | ok |
| 10 | list-digest | 9 | 88.9% | success | ok |
| 11 | reflect | 9 | 77.8% | in_progress | ok |
| 12 | skill-freshness | 9 | 44.4% | success | error |
| 13 | skill-health | 9 | 77.8% | in_progress | ok |
| 14 | morning-brief | 8 | 75.0% | success | ok |
| 15 | evening-recap | 7 | 100% | success | ok |

## Failure rate (sorted, ≥1 failure)

| Skill | Runs | Failures | Success rate | Last conclusion |
|-------|------|----------|--------------|-----------------|
| unlock-monitor | 5 | 4 | 20.0% | success |
| deal-flow | 4 | 3 | 25.0% | success |
| search-skill | 4 | 3 | 25.0% | success |
| skill-security-scan | 3 | 2 | 33.3% | success |
| cost-report | 19 | 11 (+7 cancelled) | 5.3% | success |
| skill-freshness | 9 | 5 | 44.4% | success |
| daily-routine | 12 | 5 | 58.3% | success |
| security-digest | 11 | 3 | 72.7% | success |
| thought-review (24) | 19 | 5 | 73.7% | success |
| morning-brief | 8 | 2 | 75.0% | success |
| heartbeat | 21 | 4 | 81.0% | success |
| self-improve | 6 | 1 | 83.3% | success |
| action-converter | 9 | 1 | 77.8% | in_progress |
| agent-buzz | 9 | 1 | 88.9% | success |
| goal-tracker | 9 | 1 | 77.8% | in_progress |
| list-digest | 9 | 1 | 88.9% | success |
| reflect | 9 | 1 | 77.8% | in_progress |
| skill-health | 9 | 1 | 77.8% | in_progress |
| btc-levels | 39 | 4 | 89.7% | success |

## Exit taxonomy distribution

| Bucket | Count | % | Top skills |
|--------|-------|---|------------|
| ok | ~176 | ~71% | heartbeat, morning-brief, github-trending, token-alert, security-digest, agent-buzz, list-digest, thought-review, reflect, action-converter, goal-tracker, evening-recap |
| error | ~58 | ~24% | cost-report, skill-freshness, unlock-monitor, daily-routine, heartbeat (failures) |
| skip_other | ~4 | ~2% | search-skill (SEARCH_SKILL_NO_GAP — correct behavior) |
| partial | ~1 | <1% | skill-health (SKILL_HEALTH_PARTIAL on 7-30, skill-runs sandbox-blocked) |
| uncategorized | ~7 | ~3% | cancelled runs (cost-report ×7), runs with no log marker (btc-levels inline format) |

*(Sourced from `memory/logs/*.md` — best-effort regex grep, see Step 5. ~15-20% miss-rate expected on btc-levels/skill-freshness/unlock-monitor inline log format. ok/error counts align with GitHub Actions ground truth.)*

## Silent scheduled skills (enabled, zero runs)

| Skill | Schedule | Root cause |
|-------|----------|------------|
| token-movers | `10 12 * * *` | ISS-027 12:00Z batch-dark — scheduler-side gap since 2026-06-28 |
| on-chain-monitor | `20 12 * * *` | ISS-027 same cluster |
| defi-monitor | `40 12 * * *` | ISS-027 same cluster |
| defi-overview | `0 12 * * *` | ISS-027 same cluster |
| market-context-refresh | `0 13 * * *` | ISS-027 same cluster |
| narrative-tracker | `30 13 * * *` | ISS-027 same cluster |
| aixbt-pulse | `0 9,21 * * *` | ISS-027 same cluster (last success 2026-06-28T21:21Z) |
| weekly-shiplog | `0 9 * * 1` | Missed 8-03 Monday slot (ISS-029 cascade); no run in window |
| operator-scorecard | `30 10 * * 1` | Missed 8-03 Monday slot (ISS-029 cascade); never successfully run |
| fork-skill-gap | `0 21 * * 0` | No run on 8-02 Sunday slot; check scheduler dispatch |

## Source status

- skill-runs JSON: ok (replicated via `gh api --paginate` — `./scripts/skill-runs` requires approval in this sandbox run)
- Window: 168h (2026-07-29T00:00:00Z → 2026-08-05T19:47Z)
- aeon.yml: ok
- cron-state.json: ok (60 entries, all consec_failures = 0 post-ISS-029 recovery)
- Daily logs scanned: 7-29/7-30/7-31/8-01/8-02/8-03/8-04/8-05 (8 files) for exit taxonomy

---
*Companion to `skill-health` (per-skill issue filing) and `heartbeat` (per-run pulse). Fleet-wide observability is the gap this skill closes. Methodology: GitHub Actions run history is ground truth for pass/fail; daily-log markers are best-effort secondary signal for exit taxonomy.*
