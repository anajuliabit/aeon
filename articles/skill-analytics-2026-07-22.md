# Skill Analytics — 2026-07-22

**Verdict:** 8 scheduled skill(s) didn't run this window — token-movers + 7 others (ISS-027 batch-dark cluster + aixbt-pulse dead-slot)

*Window: last 7d · 200 runs across 32 skills · 98% success · 9 anomalies*

## Anomalies

| Flag | Skill | Detail | Action |
|------|-------|--------|--------|
| 🔴 SILENT | token-movers | scheduled `10 12 * * *` but zero runs in window | ISS-027 scheduler blockage (batch-dark d25+) |
| 🔴 SILENT | defi-monitor | scheduled `40 12 * * *` but zero runs in window | ISS-027 batch-dark cluster |
| 🔴 SILENT | defi-overview | scheduled `0 12 * * *` but zero runs in window | ISS-027 batch-dark cluster |
| 🔴 SILENT | market-context-refresh | scheduled `0 13 * * *` but zero runs in window | ISS-027 batch-dark cluster |
| 🔴 SILENT | narrative-tracker | scheduled `30 13 * * *` but zero runs in window | ISS-027 batch-dark cluster |
| 🔴 SILENT | on-chain-monitor | scheduled `20 12 * * *` but zero runs in window | ISS-027 batch-dark cluster |
| 🔴 SILENT | token-pick | scheduled `0 12 * * *` but zero runs in window | ISS-027 batch-dark cluster |
| 🔴 SILENT | aixbt-pulse | scheduled `0 9,21 * * *` but zero runs in window | dead-slot d24 per memory |
| 🟠 LOW_SUCCESS | cost-report | 17% success over 6 runs (1 ok / 4 failed / 1 cancelled) | ISS-025 sandbox-truncation |

**Context:** The 8 SILENT skills are a known durable failure — the ISS-027 per-skill scheduler blockage has kept the 12:00 UTC batch frozen since 2026-06-28 (~24 days). This is a pre-existing infrastructure issue tracked in memory, not a regression discovered this run. cost-report LOW_SUCCESS is ISS-025 (sandbox-truncation family); it did fire successfully once this window (2026-07-20 19:08Z) after a long streak of failures.

## Top runners (by run count)

| # | Skill | Runs | Success % | Last status | Dominant exit |
|---|-------|------|-----------|-------------|---------------|
| 1 | btc-levels | 41 | 100% | success | quiet |
| 2 | heartbeat | 22 | 100% | success | ok |
| 3 | thought-review (24) | 13 | 100% | success | ok |
| 4 | action-converter | 8 | 88% | in_progress | ok |
| 5 | agent-buzz | 8 | 100% | success | ok |
| 6 | github-trending | 8 | 100% | success | ok |
| 7 | goal-tracker | 8 | 88% | in_progress | ok |
| 8 | list-digest | 8 | 100% | success | ok |
| 9 | reflect | 8 | 88% | in_progress | ok |
| 10 | security-digest | 8 | 100% | success | ok |
| 11 | skill-health | 8 | 88% | in_progress | quiet |
| 12 | token-alert | 8 | 100% | success | quiet |
| 13 | evening-recap | 7 | 100% | success | ok |
| 14 | skill-freshness | 7 | 100% | success | quiet |
| 15 | cost-report | 6 | 17% | success | error |

*Note: action-converter/goal-tracker/reflect/skill-health success% computed as success/total; 1 in_progress each (evening batch still running). cost-report success% = 1/(1+4+1) = 17%.*

## Failure rate (sorted, ≥1 failure)

| Skill | Runs | Failures | Success rate | Last conclusion |
|-------|------|----------|--------------|-----------------|
| cost-report | 6 | 4 | 17% | success |

Zero failures across all other 31 active skills this window.

## Exit taxonomy distribution

| Bucket | Count | % | Top skills |
|--------|-------|---|------------|
| ok | ~121 | ~61% | heartbeat, thought-review, security-digest, agent-buzz, github-trending |
| quiet | ~64 | ~32% | btc-levels, skill-health, token-alert, skill-freshness |
| error | ~4 | ~2% | cost-report |
| uncategorized | ~11 | ~5% | in-progress + cancelled runs, single-run skills w/ no log markers |

*Sourced from `memory/logs/*.md` — best-effort regex grep (step 5). btc-levels quiet-dominant = ~40/41 runs produce "alerts: none" (SKIP_QUIET pattern); skill-health quiet-dominant = SKILL_HEALTH_NOOP on flat-classification days. No skill in this window is ALL_SKIP (btc-levels had 1 reclaim-fire; skill-health had 1 NOTIFY tick).*

## Silent scheduled skills (enabled, zero runs)

| Skill | Schedule | Known cause |
|-------|----------|-------------|
| token-movers | `10 12 * * *` | ISS-027 per-skill scheduler blockage |
| on-chain-monitor | `20 12 * * *` | ISS-027 per-skill scheduler blockage |
| defi-monitor | `40 12 * * *` | ISS-027 per-skill scheduler blockage |
| defi-overview | `0 12 * * *` | ISS-027 per-skill scheduler blockage |
| token-pick | `0 12 * * *` | ISS-027 per-skill scheduler blockage |
| market-context-refresh | `0 13 * * *` | ISS-027 per-skill scheduler blockage |
| narrative-tracker | `30 13 * * *` | ISS-027 per-skill scheduler blockage |
| aixbt-pulse | `0 9,21 * * *` | dead-slot d24 (last success 2026-06-28T21:21Z) |

All 8 are pre-existing durable failures per memory. The 7-skill 12:00Z batch cluster (token-movers through market-context-refresh) has been frozen since 2026-06-28; narrative-tracker and aixbt-pulse are co-affected. No new entrants to the silent cluster this week.

## Source status

- skill-runs JSON: ok (gh api paginated, 200 runs fetched directly)
- Window: 168h (2026-07-15T~18:47Z → 2026-07-22T~18:47Z)
- aeon.yml: ok (enabled skills cross-referenced via grep)
- cron-state.json: ok (consecutive_failures = 0 for all skills)
- Daily logs scanned: 7/7 (2026-07-16 through 2026-07-22) for exit taxonomy

---
*Companion to `skill-health` (per-skill issue filing) and `heartbeat` (per-run pulse). Fleet-wide observability is the gap this skill closes. Methodology: GitHub Actions run history is ground truth for pass/fail; daily-log markers are best-effort secondary signal for exit taxonomy.*
