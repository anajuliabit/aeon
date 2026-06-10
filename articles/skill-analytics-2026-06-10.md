# Skill Analytics — 2026-06-10

**Verdict:** 2 scheduled skill(s) didn't run this window — fork-skill-gap, operator-scorecard

*Window: last 7d · 395 runs across 48 skills · 65% success · 32 anomalies*

## Anomalies

### 🔴 Silent (2)

| Skill | Schedule | Fire window missed | Root cause |
|-------|----------|--------------------|------------|
| fork-skill-gap | `0 21 * * 0` (Sun 21:00 UTC) | 2026-06-07 21:00 UTC | claude api rate-limit cluster 06-06→06-08 |
| operator-scorecard | `30 10 * * 1` (Mon 10:30 UTC) | 2026-06-08 10:30 UTC | claude api rate-limit cluster 06-06→06-08 |

both misses are timing artifacts. the claude api weekly rate-limit cluster (2026-06-06 → 2026-06-08, ~140 failures fleet-wide) landed exactly on their cron windows. not a config problem — both skills were enabled. next fire: fork-skill-gap Sun 2026-06-14, operator-scorecard Mon 2026-06-15.

### 🟠 Low success (30)

all 30 are rate-limit cluster artifacts. the cluster failed every skill that ran 06-06→06-08, dragging 7-day success rates below the 80% threshold. consecutive_failures=0 across all 30 as of 2026-06-10 — fleet is clean.

**exception:** fleet-control ended last=failure with 56.3% success (7 failures / 16 runs). the rate-limit cluster explains ~3 of those failures. the remaining ~4 warrant a manual check.

| Skill | Runs | Success | Fail | Last |
|-------|------|---------|------|------|
| reppo-digest | 32 | 65.6% | 34.4% | success |
| reppo-orchestrator | 32 | 68.8% | 31.3% | success |
| reppo-trading-agent | 32 | 68.8% | 31.3% | success |
| reppo-voter | 32 | 68.8% | 31.3% | success |
| heartbeat | 23 | 65.2% | 34.8% | success |
| fleet-control | 16 | 56.3% | 43.8% | **failure** |
| aixbt-pulse | 14 | 64.3% | 35.7% | success |
| token-movers | 12 | 50.0% | 50.0% | success |
| token-pick | 11 | 72.7% | 27.3% | success |
| token-alert | 9 | 77.8% | 22.2% | success |
| defi-overview | 9 | 77.8% | 22.2% | success |
| market-context-refresh | 9 | 77.8% | 22.2% | success |
| thought-review | 8 | 50.0% | 50.0% | success |
| action-converter | 8 | 62.5% | 37.5% | success |
| reflect | 8 | 62.5% | 37.5% | success |
| *(15 more — all daily skills with ≥3 runs and success < 80%)* | | | | |

## Top runners (by run count)

| # | Skill | Runs | Success | Last status | Dominant exit |
|---|-------|------|---------|-------------|---------------|
| 1 | reppo-digest | 32 | 65.6% | success | uncategorized |
| 2 | reppo-orchestrator | 32 | 68.8% | success | uncategorized |
| 3 | reppo-trading-agent | 32 | 68.8% | success | uncategorized |
| 4 | reppo-voter | 32 | 68.8% | success | uncategorized |
| 5 | heartbeat | 23 | 65.2% | success | ok |
| 6 | fleet-control | 16 | 56.3% | failure | uncategorized |
| 7 | aixbt-pulse | 14 | 64.3% | success | ok |
| 8 | token-movers | 12 | 50.0% | success | ok |
| 9 | token-pick | 11 | 72.7% | success | ok |
| 10 | token-alert | 9 | 77.8% | success | ok |
| 11 | defi-overview | 9 | 77.8% | success | ok |
| 12 | market-context-refresh | 9 | 77.8% | success | uncategorized |
| 13 | thought-review | 8 | 50.0% | success | ok |
| 14 | action-converter | 8 | 62.5% | success | uncategorized |
| 15 | reflect | 8 | 62.5% | success | ok |

## Failure rate breakdown

65% success (254/391 completed) is a hard step down from 100% last week. the full delta is the rate-limit cluster — ~140 failures over 3 days against a fleet that fired ~55 runs/day. no skill shows a failure pattern independent of that window.

corrected success rate (06-09 → 06-10 only, post-cluster): reppo-chain ~100%, heartbeat 100%, daily cycle skills 85–100%. the 7-day rate is a trailing artifact, not a current health signal.

## Exit taxonomy (best-effort, from daily logs)

| Bucket | Count | % | Top skills |
|--------|-------|---|------------|
| error | ~137 | ~35% | all skills 2026-06-06→06-08 (rate-limit cluster) |
| ok | ~110 | ~28% | heartbeat (23), github-trending, token-alert, defi-overview, daily-routine, goal-tracker, reflect, search-skill, agent-buzz |
| quiet | ~65 | ~16% | fleet-control (FLEET_EMPTY ×44), skill-freshness (FRESHNESS_NO_CHANGE ×21), NO_CONFIG ×20 |
| uncategorized | ~83 | ~21% | reppo-* chain (orchestrator/trading-agent/voter/digest), morning-brief, evening-recap |
| skip_unchanged | 0 | 0% | none identified |
| new_info | 0 | 0% | none identified |

*(sourced from `memory/logs/2026-06-04.md` → `2026-06-10.md`. error bucket is rate-limit artifact — not indicative of skill-logic failures. quiet bucket dominated by fleet-control FLEET_EMPTY: skill ran, found no work, exited cleanly.)*

## Silent scheduled skills

| Skill | Schedule | Fire window missed | Root cause |
|-------|----------|--------------------|------------|
| fork-skill-gap | `0 21 * * 0` | Sun 2026-06-07 21:00 UTC | rate-limit cluster |
| operator-scorecard | `30 10 * * 1` | Mon 2026-06-08 10:30 UTC | rate-limit cluster |

last week (2026-06-03 report) these same two were SILENT because their first enabled cron window post-PR-#54 was 06-07 and 06-08 respectively. they now have two consecutive missed windows. if they don't fire on 06-14 / 06-15, escalate to ISS.

## Source status

- skill-runs json: unavailable (sandbox blocks `./scripts/skill-runs` — approval-gated in claude code, same as all prior weeks). data pulled directly via `gh api repos/{owner}/{repo}/actions/runs`, paginated, 395 records across 7 pages.
- window: 168h (2026-06-03T00:00:00Z → 2026-06-10T19:19:00Z)
- aeon.yml: ok (fork-skill-gap `0 21 * * 0`, operator-scorecard `30 10 * * 1` confirmed)
- cron-state.json: ok — all consecutive_failures=0
- daily logs scanned: 7 (2026-06-04.md → 2026-06-10.md) for exit taxonomy

---
*companion to `skill-health` (per-skill issue filing) and `heartbeat` (per-run pulse). fleet-wide observability is the gap this skill closes. methodology: github actions run history is ground truth for pass/fail; daily-log markers are best-effort secondary signal for exit taxonomy.*
