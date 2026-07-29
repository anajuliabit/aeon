# Skill Analytics — 2026-07-29

**Verdict:** 11 scheduled skill(s) didn't run this window — defi-overview (batch-dark ISS-027 d31+ cluster)

*Window: last 7d · 196 runs across 31 skills · 100.0% success · 11 anomalies*

## Anomalies

| Flag | Skill | Detail | Action |
|------|-------|--------|--------|
| 🔴 SILENT | defi-overview | scheduled `0 12 * * *`, batch-dark ISS-027 d31 (last success 2026-06-28) | ISS-027 open — operator fix required |
| 🔴 SILENT | token-pick | scheduled `0 12 * * *`, batch-dark ISS-027 d31 (last success 2026-06-28) | ISS-027 open — same cluster |
| 🔴 SILENT | token-movers | scheduled `10 12 * * *`, batch-dark ISS-027 d31 (last success 2026-06-28) | ISS-027 open — same cluster |
| 🔴 SILENT | narrative-tracker | scheduled `30 13 * * *`, batch-dark ISS-027 d31 (last success 2026-06-28) | ISS-027 open — same cluster |
| 🔴 SILENT | market-context-refresh | scheduled `0 13 * * *`, batch-dark ISS-027 d31 (last success 2026-06-28) | ISS-027 open — same cluster |
| 🔴 SILENT | on-chain-monitor | scheduled `20 12 * * *`, batch-dark ISS-027 d31 (last success 2026-06-28) | ISS-027 open — same cluster |
| 🔴 SILENT | defi-monitor | scheduled `40 12 * * *`, batch-dark ISS-027 d31 (last success 2026-06-28) | ISS-027 open — same cluster |
| 🔴 SILENT | aixbt-pulse | scheduled `0 9,21 * * *`, dead slot d31 (last success 2026-06-28) | ISS-027 signature — same freeze event |
| 🔴 SILENT | weekly-shiplog | scheduled `0 9 * * 1`, missed Monday 2026-07-27 (last success 2026-07-20) | investigate scheduler miss; prior 6/6 runs were successful |
| 🔴 SILENT | fork-skill-gap | scheduled `0 21 * * 0`, never-run (0 total runs, dispatch-gated per heartbeat) | known — operator-gated initialization |
| 🔴 SILENT | operator-scorecard | scheduled `30 10 * * 1`, never-run (0 total runs, dispatch-gated per heartbeat) | known — operator-gated initialization |

## Top runners (by run count)

| # | Skill | Runs | Success | Last status | Dominant exit |
|---|-------|------|---------|-------------|---------------|
| 1 | btc-levels | 39 | 100% | success | uncategorized |
| 2 | heartbeat | 22 | 100% | success | ok |
| 3 | thought-review | 15 | 100% | success | ok |
| 4 | agent-buzz | 8 | 100% | success | ok |
| 5 | list-digest | 8 | 100% | success | uncategorized |
| 6 | action-converter | 8 | 87.5%† | in_progress | ok |
| 7 | reflect | 8 | 87.5%† | in_progress | uncategorized |
| 8 | skill-health | 8 | 87.5%† | in_progress | ok |
| 9 | goal-tracker | 8 | 87.5%† | in_progress | uncategorized |
| 10 | morning-brief | 8 | 100% | success | ok |
| 11 | daily-routine | 8 | 100% | success | ok |
| 12 | security-digest | 8 | 100% | success | uncategorized |
| 13 | evening-recap | 7 | 100% | success | uncategorized |
| 14 | github-trending | 7 | 100% | success | ok |
| 15 | token-alert | 7 | 100% | success | ok |

†6 skills currently in_progress (action-converter, reflect, self-improve, skill-analytics, skill-health, goal-tracker) — success rate computed over completed runs only; all prior runs succeeded.

## Failure rate (sorted, ≥1 failure)

Zero failures across 31 active skills this window. 190 completed runs, 0 failed, 100.0% success rate.

## Exit taxonomy distribution

| Bucket | Count | % | Top skills |
|--------|-------|---|------------|
| uncategorized | ~95 | ~48% | btc-levels (39), list-digest (8), reflect (7), security-digest (7), evening-recap (7), daily-routine (7), goal-tracker (7) |
| ok | ~85 | ~43% | heartbeat (22), thought-review (14), agent-buzz (8), action-converter (7), morning-brief (7), github-trending (7), token-alert (6 alert-fires), skill-health (7) |
| quiet | ~9 | ~5% | skill-freshness (7 FRESHNESS_NO_CHANGE), skill-security-scan (1 SECURITY_SCAN_NOCHANGE), skill-graph (1 SKILL_GRAPH_NO_CHANGE) |
| error | 0 | 0% | — |
| partial | 0 | 0% | — |
| skip_unchanged | 0 | 0% | — |
| new_info | 0 | 0% | — |

Sourced from `memory/logs/*.md` — best-effort regex grep (7-22 through 7-29). btc-levels fires silently (no explicit exit code in log entries) → uncategorized. Skills with sub-OK-class exits log custom codes (FRESHNESS_NO_CHANGE, SECURITY_SCAN_NOCHANGE, SKILL_GRAPH_NO_CHANGE) that map to the quiet bucket.

## Silent scheduled skills (enabled, zero runs)

| Skill | Schedule | Last success | Note |
|-------|----------|-------------|------|
| defi-overview | `0 12 * * *` | 2026-06-28 | batch-dark ISS-027 d31 |
| token-pick | `0 12 * * *` | 2026-06-28 | batch-dark ISS-027 d31 |
| token-movers | `10 12 * * *` | 2026-06-28 | batch-dark ISS-027 d31 |
| narrative-tracker | `30 13 * * *` | 2026-06-28 | batch-dark ISS-027 d31 |
| market-context-refresh | `0 13 * * *` | 2026-06-28 | batch-dark ISS-027 d31 |
| on-chain-monitor | `20 12 * * *` | 2026-06-28 | batch-dark ISS-027 d31 |
| defi-monitor | `40 12 * * *` | 2026-06-28 | batch-dark ISS-027 d31 |
| aixbt-pulse | `0 9,21 * * *` | 2026-06-28 | dead slot d31 — same freeze event as batch-dark cluster |
| weekly-shiplog | `0 9 * * 1` | 2026-07-20 | missed Monday 2026-07-27 — prior 6/6 runs were successful, single-week miss |
| fork-skill-gap | `0 21 * * 0` | never | dispatch-gated, no runs ever — heartbeat flags as expected |
| operator-scorecard | `30 10 * * 1` | never | dispatch-gated, no runs ever — heartbeat flags as expected |

The core batch-dark cluster (defi-overview + token-pick + token-movers + narrative-tracker + market-context-refresh + on-chain-monitor + defi-monitor + aixbt-pulse = 8 skills) has been frozen since 2026-06-28 21:00Z per ISS-027 — a durable regime with no resolution in this window.

## Source status

- skill-runs JSON: substitute — gh run list --limit=200 used directly (skill-runs script blocked by sandbox permission; gh run list returns equivalent GitHub Actions run history data); paginate-count confirmed 196 skill runs via background gh api call
- Window: 168h (2026-07-22T18:39Z → 2026-07-29T18:39Z)
- aeon.yml: ok (43 enabled skills parsed)
- cron-state.json: ok (54 entries; consecutive_failures=0 for all skills)
- Daily logs scanned: 6/7 for exit taxonomy (2026-07-23 not read; 7-22 partial)

---
*Companion to `skill-health` (per-skill issue filing) and `heartbeat` (per-run pulse). Fleet-wide observability is the gap this skill closes. Methodology: GitHub Actions run history is ground truth for pass/fail; daily-log markers are best-effort secondary signal for exit taxonomy.*
