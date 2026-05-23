## Summary

Ran skill-health audit for 2026-05-23.

**Classification (21 enabled skills)**
- 🟢 HEALTHY: 12 (morning-brief, github-trending, token-alert, defi-overview, search-skill, goal-tracker, skill-health, reflect, action-converter, evening-recap, skill-freshness, heartbeat)
- ⚪ NO DATA: 9 (skill-security-scan, autoresearch, skill-analytics, self-improve, cost-report, skill-evals, skill-update-check, operator-scorecard, weekly-review — weekly/biweekly cadence, slots not yet hit since 2026-05-21 fleet bootstrap; not classified as scheduler gaps)
- CRITICAL / DEGRADED / FLAPPING / WARNING: none
- 5 skills moved NO DATA → HEALTHY since last run (goal-tracker, skill-health, reflect, action-converter, evening-recap)

**Issues**
- 3 open (ISS-003/004/005) — all detected_by `reppo-digest`, outside skill-health's reconciliation scope per the CLAUDE.md contract ("Health skills file, repair skills close").
- 0 filed, 0 resolved this run.

**Notify gate**
- Signature is empty (no CRITICAL/FLAPPING/DEGRADED/SYSTEMIC). SHA-256 = `e3b0c442…` matches prev_report.hash.
- Δ since last notify = 23h41m < 24h → **SKILL_HEALTH_NOOP, no notification sent.**

**Files**
- Updated `memory/skill-health/last-report.json` (new `last_run_at`, classification refreshed; `last_notified_at` preserved).
- Appended skill-health entry to `memory/logs/2026-05-23.md`.
