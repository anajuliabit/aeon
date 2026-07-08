# Skill Analytics — 2026-07-08

**Verdict:** 11 scheduled skill(s) didn't run this window — 12:00 UTC batch cluster dark for 10 days (8 skills, ISS-027), Monday scheduler gaps (3 skills)

*Window: last 7d · 236 runs across 30 skills · 100% GH-success · 11 anomalies*

> Note: "100% GH-success" reflects GitHub Actions workflow conclusion (`success`/`failure`). The systemic `output_tokens=0` sandbox-truncation cluster (ISS-019/020/021/025) causes runs to exit 0 with no output — those appear as GH successes. Lifetime success rates in cron-state (38–72% for many skills) reflect pre-window history and the output-quality reality. The fleet-wide GH-success rate in this window is inflated by this known bug.

## Anomalies

| Flag | Skill | Detail | Action |
|------|-------|--------|--------|
| 🔴 SILENT | token-movers | daily `10 12 * * *` — zero runs since 2026-06-28 (10 days) | 12:00 UTC batch scheduler gap (ISS-027) |
| 🔴 SILENT | on-chain-monitor | daily `20 12 * * *` — zero runs since 2026-06-28 (10 days) | 12:00 UTC batch scheduler gap (ISS-027) |
| 🔴 SILENT | defi-monitor | daily `40 12 * * *` — zero runs since 2026-06-28 (10 days) | 12:00 UTC batch scheduler gap (ISS-027) |
| 🔴 SILENT | defi-overview | daily `0 12 * * *` — zero runs since 2026-06-28 (10 days) | 12:00 UTC batch scheduler gap (ISS-027) |
| 🔴 SILENT | token-pick | daily `0 12 * * *` — zero runs since 2026-06-28 (10 days) | 12:00 UTC batch scheduler gap (ISS-027) |
| 🔴 SILENT | market-context-refresh | daily `0 13 * * *` — zero runs since 2026-06-28 (10 days) | 12:00 UTC batch scheduler gap (ISS-027) |
| 🔴 SILENT | narrative-tracker | daily `30 13 * * *` — zero runs since 2026-06-28 (10 days) | 12:00 UTC batch scheduler gap (ISS-027) |
| 🔴 SILENT | aixbt-pulse | twice daily `0 9,21 * * *` — zero runs since 2026-06-28 (10 days) | dead-slot confirmed, scheduler-side; XAI quota also exhausted |
| 🔴 SILENT | operator-scorecard | Monday `30 10 * * 1` — never run (not in cron-state; 8+ consecutive Monday misses) | scheduler-side never-run, chronic |
| 🔴 SILENT | weekly-shiplog | Monday `0 9 * * 1` — missed July 7 (last 2026-06-29) | scheduler gap |
| 🔴 SILENT | cost-report | Monday `0 7 * * 1` — missed July 7 (last 2026-06-29) | scheduler gap |

Root cause for the 12:00 UTC cluster: ISS-027 (codified 2026-07-07). PR #156 (`usepod_model:` drift fix) merged 2026-07-06 but dispatcher matcher/YAML nesting issue persists — 7-07 and 7-08 12:00Z ticks dispatched only token-alert + btc-levels. Operator-scorecard + Monday-batch gaps are a separate chronic scheduler-side never-run pattern.

## Top runners (by run count)

| # | Skill | Runs | Success | Last status | Dominant exit |
|---|-------|------|---------|-------------|---------------|
| 1 | btc-levels | 50 | 100% | success | uncategorized (quiet-run pattern, no _OK marker) |
| 2 | heartbeat | 26 | 100% | success | ok (HEARTBEAT_OK) |
| 3 | thought-review | 16 | 100% | success | uncategorized |
| 4 | action-converter | 10 | 100% | success | ok (ACTION_CONVERTER_OK) |
| 5 | goal-tracker | 10 | 100% | success | ok (GOAL_TRACKER_OK) |
| 6 | list-digest | 10 | 100% | success | ok (LIST_DIGEST_OK) |
| 7 | reflect | 10 | 100% | success | ok (REFLECT_OK) |
| 8 | skill-health | 10 | 100% | success | ok (SKILL_HEALTH_OK / PARTIAL) |
| 9 | agent-buzz | 9 | 100% | success | ok (AGENT_BUZZ_OK) |
| 10 | evening-recap | 9 | 100% | success | uncategorized |
| 11 | search-skill | 9 | 100% | success | quiet (SEARCH_SKILL_NO_GAP day-15) |
| 12 | security-digest | 9 | 100% | success | quiet (empty tiers, silent per spec) |
| 13 | token-alert | 8 | 100% | success | ok (TOKEN_ALERT_OK / triggered twice) |
| 14 | skill-freshness | 8 | 100% | success | ok/skip_unchanged (FRESHNESS_OK/NO_CHANGE) |
| 15 | morning-brief | 7 | 100% | success | ok (MORNING_BRIEF_OK) |

*(Counts from GH Actions API pages 1–4, covering approximately July 2–8. July 1 runs appear on pages 4–5 and may overlap with pre-window contamination due to API pagination behavior — see Source status.)*

## Failure rate (sorted, ≥1 failure)

Zero failures detected in the 7-day window per GH Actions conclusions across 30 skills. The fleet ran clean at the workflow-exit-code level.

**Caveat:** This does not mean zero-quality runs. The `output_tokens=0` sandbox-truncation cluster (ISS-019/020/021/025) causes GH Actions to report `success` while Claude produces no output. Lifetime cron-state success rates tell the real story for affected skills: skill-analytics (13%), reg-monitor (14%), security-digest (30%), market-context-refresh (32%), narrative-tracker (33%), search-skill (37%), skill-health (39%), reflect (43%), action-converter (42%). The recent 7-day GH window cannot distinguish these phantom-successes from real successes.

## Exit taxonomy distribution

Sourced from `memory/logs/*.md` — best-effort regex grep (10–20% miss rate expected). Dominant buckets estimated from log scan across 8 daily log files (2026-07-01 through 2026-07-08).

| Bucket | Est. Count | Est. % | Top skills |
|--------|-----------|--------|------------|
| ok | ~175 | ~74% | heartbeat, action-converter, goal-tracker, reflect, skill-health, token-alert, morning-brief, daily-routine, github-trending, list-digest, agent-buzz |
| quiet | ~35 | ~15% | search-skill (NO_GAP day-15), security-digest (empty tiers), vuln-scanner (CLEAN), skill-freshness (NO_CHANGE days) |
| uncategorized | ~25 | ~11% | btc-levels (quiet-run log pattern, no _OK marker), thought-review, evening-recap |
| skip_unchanged | ~1 | <1% | skill-freshness (fingerprint-identical days) |
| ok_silent | — | — | — |
| new_info | — | — | — |
| error / partial | ~0 | ~0% | (none in log window; SKILL_HEALTH_PARTIAL appears but is a data-source flag, not a skill failure) |

## Silent scheduled skills (enabled, zero runs in window)

**12:00 UTC batch cluster — 8 skills dark for 10 days (since 2026-06-28):**
- token-movers (`10 12 * * *`)
- on-chain-monitor (`20 12 * * *`)
- defi-monitor (`40 12 * * *`)
- defi-overview (`0 12 * * *`)
- token-pick (`0 12 * * *`)
- market-context-refresh (`0 13 * * *`)
- narrative-tracker (`30 13 * * *`)
- aixbt-pulse (`0 9,21 * * *`) ← also XAI quota-blocked

**Monday scheduler gaps — 3 skills:**
- operator-scorecard (`30 10 * * 1`) — never run (chronic, 8+ weeks)
- weekly-shiplog (`0 9 * * 1`) — missed July 7
- cost-report (`0 7 * * 1`) — missed July 7

Root cause for batch cluster: ISS-027 (action-converter codified 2026-07-07). PR #156 fixed `usepod_model:` drift but scheduler-side gap (chain-config, YAML nesting, or dispatcher matcher) still blocks the full 12:00 batch. PR #156 merged 2026-07-06. The ISS-025 capture-step PR (per ISS-009 root-cause) remains un-authored and un-shipped as of this run — weekly-review deadline 2026-07-13.

## Source status

- skill-runs JSON: `gh api` (direct) — used paginated API calls with per-page jq aggregation; pages 1–4 cover July 2–8, page 5 shows early-window + pre-window contamination. Shell script `./scripts/skill-runs` blocked by sandbox permissions (consistent with SKILL_HEALTH_PARTIAL pattern in all prior skill-health runs).
- Window: 168h (2026-07-01T~18:30Z → 2026-07-08T~18:30Z)
- aeon.yml: ok — full skill inventory read, enabled/cron/reactive classification complete
- cron-state.json: ok — 51 entries, last_dispatch cross-referenced to determine SILENT flags
- Daily logs scanned: 8/8 (2026-07-01 through 2026-07-08) for exit taxonomy; best-effort regex grep

---
*Companion to `skill-health` (per-skill issue filing) and `heartbeat` (per-run pulse). Fleet-wide observability is the gap this skill closes. Methodology: GitHub Actions run history is ground truth for pass/fail; daily-log markers are best-effort secondary signal for exit taxonomy.*
