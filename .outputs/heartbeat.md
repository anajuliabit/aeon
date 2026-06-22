## Summary

Ran the heartbeat skill at 2026-06-22 08:33 UTC.

**Overall:** 🔴 DEGRADED · STATUS_PAGE=DEGRADED

**P0 findings (all dedup-blocked, no notify sent):**
- `token-alert` stuck mid-dispatch since 2026-06-21T13:45Z (~19h) — ISS-023
- `deal-flow` stuck since 2026-06-08 (~14d)
- `chain:investment-advisor` last_status=failed (2026-06-08, long-standing)
- 24 chronic-failure skills (success_rate < 0.5) — same sandbox-truncation cluster ISS-019/020/021/024

**Self-check:** heartbeat last_success 12.5h ago — healthy.

**Delta vs 2026-06-21 15:22Z heartbeat:** `fork-cohort` recovered (Sunday cycle ran clean, 100% sr).

**Files modified:**
- `docs/status.md` — regenerated (overall DEGRADED, 13 open issues, 44 enabled skills tracked, 3 never-run, token-pulse section omitted because no `articles/token-report-*.md` exists)
- `memory/logs/2026-06-22.md` — appended heartbeat log entry

**Follow-up:** None new — all blockers (sandbox-truncation systemic, XAI quota, operator on-chain config) tracked in MEMORY.md goals and awaiting operator action.
