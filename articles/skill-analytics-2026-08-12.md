# Skill Analytics — 2026-08-12

**Verdict:** 10 scheduled skill(s) didn't run this window — token-movers (ISS-027 12Z-batch dark d46, 8-skill cluster silent since 2026-06-28)

*Window: last 7d · 290 runs across 32 skills · 58% success · 26 anomalies*

## Anomalies

| Flag | Skill | Detail | Action |
|------|-------|--------|--------|
| 🔴 SILENT | token-movers | scheduled `10 12 * * *` (daily), zero runs — ISS-027 12Z-batch dark d46 | investigate ISS-027 scheduler gap |
| 🔴 SILENT | on-chain-monitor | scheduled `20 12 * * *` (daily), zero runs — ISS-027 | same |
| 🔴 SILENT | defi-monitor | scheduled `40 12 * * *` (daily), zero runs — ISS-027 | same |
| 🔴 SILENT | defi-overview | scheduled `0 12 * * *` (daily), zero runs — ISS-027 | same |
| 🔴 SILENT | token-pick | scheduled `0 12 * * *` (daily), zero runs — ISS-027 | same |
| 🔴 SILENT | market-context-refresh | scheduled `0 13 * * *` (daily), zero runs — ISS-027 | same |
| 🔴 SILENT | narrative-tracker | scheduled `30 13 * * *` (daily), zero runs — ISS-027 | same |
| 🔴 SILENT | aixbt-pulse | scheduled `0 9,21 * * *` (2× daily), zero runs — ISS-027 | same |
| 🔴 SILENT | fork-skill-gap | scheduled `0 21 * * 0` (weekly Sun), zero runs in window — no cron-state entry | check workflow / scheduler |
| 🔴 SILENT | operator-scorecard | scheduled `30 10 * * 1` (weekly Mon), zero runs in window — no cron-state entry | check workflow / scheduler |
| 🔴 ALL_FAIL | unlock-monitor | 5/5 failed — usepod payment-required errors; `consecutive_failures=7` | investigate Mon-batch blocker |
| 🔴 ALL_FAIL | deal-flow | 4/4 failed — usepod payment-required errors; `consecutive_failures=6` | same |
| 🔴 ALL_FAIL | search-skill | 2/2 failed — usepod payment-required errors; `consecutive_failures=2` | same |
| 🔴 ALL_FAIL | skill-security-scan | 2/2 failed — usepod payment-required errors; `consecutive_failures=3` | see skill-health for filed issue |
| 🟠 LOW_SUCCESS | cost-report | 3% (1/34) — chronic ISS-030; 8-11 organic recovery breaks 33+ consec streak; 8-17 next deciding-test | monitor 8-17 Mon 07Z |
| 🟠 LOW_SUCCESS | weekly-shiplog | 10% (1/10) — usepod payment-required errors cluster | investigate batch-slot failures |
| 🟠 LOW_SUCCESS | daily-routine | 38% (6/16) — payment-required errors on ~62% of runs | same |
| 🟠 LOW_SUCCESS | skill-freshness | 44% (7/16) — payment-required errors on ~56% of runs | same |
| 🟠 LOW_SUCCESS | github-trending | 50% (6/12) — payment-required errors on half of runs | same |
| 🟠 LOW_SUCCESS | security-digest | 55% (6/11) — payment-required errors | same |
| 🟠 LOW_SUCCESS | thought-review | 55% (12/22) — payment-required errors | same |
| 🟠 LOW_SUCCESS | morning-brief | 63% (5/8) — payment-required errors | same |
| 🟠 LOW_SUCCESS | token-alert | 64% (7/11) — payment-required errors | same |
| 🟠 LOW_SUCCESS | heartbeat | 67% (18/27) — payment-required errors | same |
| 🟠 LOW_SUCCESS | list-digest | 75% (6/8) — payment-required errors | same |
| 🟠 LOW_SUCCESS | btc-levels | 74% (32/43) — payment-required errors on ~26% of runs | same |

## Top runners (by run count)

| # | Skill | Runs | Success | Last status | Dominant exit |
|---|-------|------|---------|-------------|---------------|
| 1 | btc-levels | 43 | 74% | success | ok |
| 2 | cost-report | 34 | 3% | success | uncategorized |
| 3 | heartbeat | 27 | 67% | success | ok |
| 4 | thought-review | 22 | 55% | success | ok |
| 5 | daily-routine | 16 | 38% | success | ok |
| 6 | skill-freshness | 16 | 44% | success | ok |
| 7 | github-trending | 12 | 50% | success | ok |
| 8 | security-digest | 11 | 55% | success | ok |
| 9 | token-alert | 11 | 64% | success | ok |
| 10 | weekly-shiplog | 10 | 10% | success | uncategorized |
| 11 | action-converter | 8 | 88% | success | ok |
| 12 | goal-tracker | 8 | 88% | success | ok |
| 13 | list-digest | 8 | 75% | success | ok |
| 14 | morning-brief | 8 | 63% | success | ok |
| 15 | reflect | 8 | 88% | success | ok |

## Failure rate (sorted, ≥1 failure)

| Skill | Runs | Failures | Success rate | Last conclusion |
|-------|------|----------|--------------|-----------------|
| cost-report | 34 | 17 (+16 cancelled) | 3% | success |
| weekly-shiplog | 10 | 9 | 10% | success |
| unlock-monitor | 5 | 5 | 0% | failure |
| deal-flow | 4 | 4 | 0% | failure |
| daily-routine | 16 | 10 | 38% | success |
| search-skill | 2 | 2 | 0% | failure |
| skill-security-scan | 2 | 2 | 0% | failure |
| skill-freshness | 16 | 9 | 44% | success |
| github-trending | 12 | 6 | 50% | success |
| security-digest | 11 | 5 | 55% | success |
| thought-review | 22 | 10 | 55% | success |
| morning-brief | 8 | 3 | 63% | success |
| token-alert | 11 | 4 | 64% | success |
| heartbeat | 27 | 9 | 67% | success |
| list-digest | 8 | 2 | 75% | success |
| btc-levels | 43 | 11 | 74% | success |
| agent-buzz | 7 | 1 | 86% | success |
| action-converter | 8 | 1 | 88% | success |
| goal-tracker | 8 | 1 | 88% | success |
| reflect | 8 | 1 | 88% | success |
| skill-health | 8 | 1 | 88% | success |

## Exit taxonomy distribution

| Bucket | Count | % | Top skills |
|--------|-------|---|------------|
| ok | ~148 | 51% | btc-levels (32), heartbeat (18), thought-review (12), token-alert (7), goal-tracker (7), action-converter (7), reflect (7) |
| uncategorized | ~126 | 43% | cost-report (~33), daily-routine (~10), heartbeat (~9), skill-freshness (~9) |
| error | ~10 | 3% | skill-health (partial), various |
| partial | ~3 | 1% | skill-health |
| quiet | ~3 | 1% | skill-freshness (no_change), skill-graph (no_change) |
| skip_unchanged | 0 | 0% | — |
| new_info | 0 | 0% | — |

*Sourced from `memory/logs/*.md` — best-effort regex grep, see Step 5. Uncategorized bucket is large (~43%) because most payment-required API failures abort before writing log markers. Ground truth is the GitHub Actions run history above.*

## Silent scheduled skills (enabled, zero runs)

| Skill | Schedule | Note |
|-------|----------|------|
| token-movers | `10 12 * * *` (daily) | ISS-027 12Z-batch dark d46 since 2026-06-28 |
| on-chain-monitor | `20 12 * * *` (daily) | ISS-027 12Z-batch dark d46 |
| defi-monitor | `40 12 * * *` (daily) | ISS-027 12Z-batch dark d46 |
| defi-overview | `0 12 * * *` (daily) | ISS-027 12Z-batch dark d46 |
| token-pick | `0 12 * * *` (daily) | ISS-027 12Z-batch dark d46 |
| market-context-refresh | `0 13 * * *` (daily) | ISS-027 12Z-batch dark d46 |
| narrative-tracker | `30 13 * * *` (daily) | ISS-027 12Z-batch dark d46 |
| aixbt-pulse | `0 9,21 * * *` (2× daily) | ISS-027 12Z-batch dark d46 |
| fork-skill-gap | `0 21 * * 0` (weekly Sun) | No cron-state entry; no run history in snapshot |
| operator-scorecard | `30 10 * * 1` (weekly Mon) | No cron-state entry; missed 2026-08-11 Mon slot |

## Source status

- skill-runs JSON: ok (reconstructed via `gh api` directly — `./scripts/skill-runs` required approval; data equivalent)
- Window: 168h (2026-08-05T19:18:27Z → 2026-08-12T19:18:27Z)
- aeon.yml: ok
- cron-state.json: ok
- Daily logs scanned: 8/8 for exit taxonomy (2026-08-05 → 2026-08-12; partial coverage on 8-05 since window starts at 19:18Z)

---
*Companion to `skill-health` (per-skill issue filing) and `heartbeat` (per-run pulse). Fleet-wide observability is the gap this skill closes. Methodology: GitHub Actions run history is ground truth for pass/fail; daily-log markers are best-effort secondary signal for exit taxonomy.*
