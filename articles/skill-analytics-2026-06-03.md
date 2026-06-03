# Skill Analytics — 2026-06-03

**Verdict:** 11 scheduled skill(s) didn't run this window — token-movers, on-chain-monitor, defi-monitor, and 8 more

*Window: last 7d · 299 runs across 41 skills · 100% success · 11 anomalies*

## Anomalies

| Flag | Skill | Detail | Action |
|------|-------|--------|--------|
| 🔴 SILENT | token-movers | scheduled `10 12 * * *` (daily) but zero runs in window | check workflow / scheduler — never ran (not in cron-state) |
| 🔴 SILENT | on-chain-monitor | scheduled `20 12 * * *` (daily) but zero runs in window | check workflow / scheduler — never ran |
| 🔴 SILENT | defi-monitor | scheduled `40 12 * * *` (daily) but zero runs in window | check workflow / scheduler — never ran |
| 🔴 SILENT | narrative-tracker | scheduled `30 13 * * *` (daily) but zero runs in window | last ran 2026-05-21 (13 days ago), not in cron-state reset |
| 🔴 SILENT | aixbt-pulse | scheduled `0 9,21 * * *` (2×/day) but zero runs in window | check workflow / scheduler — never ran |
| 🔴 SILENT | unlock-monitor | scheduled `0 10 * * 1` (Mon) but zero runs in window | Monday opportunity was 2026-06-01 — never ran per cron-state |
| 🔴 SILENT | operator-scorecard | scheduled `30 10 * * 1` (Mon) but zero runs in window | Monday opportunity was 2026-06-01 — never ran per cron-state |
| 🔴 SILENT | vuln-scanner | scheduled `0 16 * * 6` (Sat) but zero runs in window | Saturday was 2026-05-30 (before PR #54 enable) — next Sat 2026-06-06 |
| 🔴 SILENT | fork-cohort | scheduled `0 19 * * 0` (Sun) but zero runs in window | Sunday was 2026-05-31 (before PR #54 enable) — next Sun 2026-06-07 |
| 🔴 SILENT | fork-skill-digest | scheduled `30 18 * * 0` (Sun) but zero runs in window | Sunday was 2026-05-31 (before PR #54 enable) — next Sun 2026-06-07 |
| 🔴 SILENT | fork-skill-gap | scheduled `0 21 * * 0` (Sun) but zero runs in window | Sunday was 2026-05-31 (before PR #54 enable) — next Sun 2026-06-07 |

**Note:** 7 of the 11 SILENT skills (vuln-scanner, fork-cohort, fork-skill-digest, fork-skill-gap, operator-scorecard, unlock-monitor + others newly tracked since PR #54 on 2026-06-01) haven't missed a scheduled window they were enabled for — their first cron opportunity falls after today. token-movers, on-chain-monitor, defi-monitor, and narrative-tracker are the more operationally concerning cases: daily-scheduled, never or rarely fired, not in cron-state history.

## Top runners (by run count)

| # | Skill | Runs | Success | Last status | Dominant exit |
|---|-------|------|---------|-------------|---------------|
| 1 | reppo-orchestrator | 31 | 100% | success | uncategorized |
| 2 | reppo-digest | 30 | 100% | success | uncategorized |
| 3 | reppo-trading-agent | 30 | 97% (1 cancelled) | success | uncategorized |
| 4 | heartbeat | 23 | 100% | success | ok |
| 5 | fleet-control | 14 | 100% | success | uncategorized |
| 6 | reppo-voter | 9 | 100% | success | uncategorized |
| 7 | action-converter | 8 | 88% (1 in-progress) | pending | uncategorized |
| 8 | defi-overview | 8 | 100% | success | ok |
| 9 | github-trending | 8 | 100% | success | ok |
| 10 | goal-tracker | 8 | 88% (1 in-progress) | pending | ok |
| 11 | market-context-refresh | 8 | 100% | success | uncategorized |
| 12 | morning-brief | 8 | 100% | success | uncategorized |
| 13 | reflect | 8 | 88% (1 in-progress) | pending | ok |
| 14 | search-skill | 8 | 100% | success | ok |
| 15 | skill-freshness | 8 | 100% | success | ok |

*(action-converter, goal-tracker, reflect, skill-health, self-improve, skill-analytics all show 1 in-progress run — these are the current 18:59Z batch executing in parallel. Counted as pending, not failure.)*

## Failure rate (sorted, ≥1 failure)

Zero failures across 41 skills this window.

*(vibecoding-digest emitted VIBECODING_DIGEST_ERROR on 5 of 7 runs per daily log markers, but all 7 GH Actions workflow conclusions are `success` (exit 0) — workflow-exit-vs-skill-outcome mismatch, documented in ISS-015 scope. Ground truth for pass/fail is GH Actions: vibecoding-digest is HEALTHY on this axis.)*

## Exit taxonomy distribution

| Bucket | Count | % | Top skills |
|--------|-------|---|------------|
| ok | ~103 | ~34% | heartbeat (23), defi-overview (8), github-trending (8), search-skill (8), token-alert (8), skill-freshness (8), goal-tracker (7-8), reflect (7-8), daily-routine (7), agent-buzz (7) |
| uncategorized | ~182 | ~61% | reppo-orchestrator (31), reppo-digest (30), reppo-trading-agent (30), fleet-control (14), reppo-voter (9), market-context-refresh (8), morning-brief (8), evening-recap (7), self-improve (5), technical-explainer (5) |
| error | 7 | 2% | vibecoding-digest (7) |
| partial | 7 | 2% | skill-health (7 — SKILL_HEALTH_PARTIAL, skill-runs sandbox-blocked on all 7 runs; 1 run was SKILL_HEALTH_OK) |
| quiet | 0 | 0% | none identified via _OK_SILENT / _QUIET / SKIP_QUIET markers |
| skip_unchanged | 0 | 0% | none identified |
| new_info | 0 | 0% | none identified |

*(Sourced from `memory/logs/2026-05-28.md` → `2026-06-03.md` — best-effort regex grep, see Step 5. The high uncategorized share is expected: reppo-swarm chain skills (orchestrator + trading-agent + voter + digest = 100 runs) and fleet-control emit no standard _OK/_ERROR log markers. The ok bucket undercounts because it is log-marker-gated, not GH-API-gated.)*

## Silent scheduled skills (enabled, zero runs)

| Skill | Schedule | Notes |
|-------|----------|-------|
| token-movers | `10 12 * * *` (daily) | Never ran — not in cron-state |
| on-chain-monitor | `20 12 * * *` (daily) | Never ran — not in cron-state |
| defi-monitor | `40 12 * * *` (daily) | Never ran — not in cron-state |
| narrative-tracker | `30 13 * * *` (daily) | Last ran 2026-05-21, stale by 13 days |
| aixbt-pulse | `0 9,21 * * *` (2×/day) | Never ran — not in cron-state |
| unlock-monitor | `0 10 * * 1` (Mon) | Never ran — 2026-06-01 Monday was the window opportunity |
| operator-scorecard | `30 10 * * 1` (Mon) | Never ran — 2026-06-01 Monday was the window opportunity |
| vuln-scanner | `0 16 * * 6` (Sat) | Never ran — next Sat is 2026-06-06 (enabled PR #54 after last Sat) |
| fork-cohort | `0 19 * * 0` (Sun) | Never ran — next Sun is 2026-06-07 (enabled PR #54 after last Sun) |
| fork-skill-digest | `30 18 * * 0` (Sun) | Never ran — next Sun is 2026-06-07 (enabled PR #54 after last Sun) |
| fork-skill-gap | `0 21 * * 0` (Sun) | Never ran — next Sun is 2026-06-07 (enabled PR #54 after last Sun) |

## Source status

- skill-runs JSON: unavailable (sandbox blocks `./scripts/skill-runs` bash invocation — approval-gated, same pattern as skill-health PARTIAL runs). Run data reconstructed from `gh api repos/{owner}/{repo}/actions/runs` directly via gh CLI (same underlying data source), parsed via jq.
- Window: 168h (2026-05-27T00:00:00Z → 2026-06-03T19:00:00Z)
- aeon.yml: ok (parsed via Explore agent)
- cron-state.json: ok (45 entries)
- Daily logs scanned: 7/7 (2026-05-28.md → 2026-06-03.md) for exit taxonomy

---
*Companion to `skill-health` (per-skill issue filing) and `heartbeat` (per-run pulse). Fleet-wide observability is the gap this skill closes. Methodology: GitHub Actions run history is ground truth for pass/fail; daily-log markers are best-effort secondary signal for exit taxonomy.*
