Heartbeat complete.

`HEARTBEAT_OK · STATUS_PAGE=DEGRADED — wrote docs/status.md`

## Summary

**Findings (all dedup — no notify sent):**
- **P0:** 5 🕸 stuck skills — fork-cohort ~97h (P0-novel, ISS-032 filing overdue ~49h past 48h threshold) + 4 Mon-batch ISS-031 carryovers (search-skill/unlock-monitor/skill-security-scan/deal-flow, self-clear next Mon 8-17). 3 consec≥3 fires (all ISS-031). 12-skill chronic sr<0.5 cohort unchanged. Heartbeat self-check clean (~5h since last success).
- **P1:** 4 open PRs, all within weekly-batch cadence. 0 urgent issues.
- **P2:** MEMORY.md flags already surfaced this UTC-day.
- **P3:** No missing skills; evening 18Z batch fired clean, next = btc-levels 20:15Z.

**Files modified:**
- `docs/status.md` — wholesale rewrite (Overall 🔴 DEGRADED, 15 open issues, 43 enabled skills, no token pulse section — no `articles/token-report-*.md` exists)
- `memory/logs/2026-08-12.md` — heartbeat log entry appended

**Notify decision:** skipped per dedup rule (all findings appear in last 48h logs across morning-brief, prior heartbeats, skill-health, goal-tracker, reflect).
