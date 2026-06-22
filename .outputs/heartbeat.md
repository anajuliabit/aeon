Heartbeat complete.

## Summary

**Verdict:** 🔴 DEGRADED · STATUS_PAGE=DEGRADED · NOTIFY=DEDUP_SKIP

**P0 findings (all dedup-blocked vs today's 14:37Z heartbeat):**
- `cost-report` failed cf=7 (was cf=3 at 14:37Z) — ISS-025 already filed by skill-health 19:08Z, extends sandbox-truncation cluster (ISS-019/020/021/024). Same skill/signature/day → no fresh notify.
- 22-skill chronic-failure tail (sr<0.5) identical to 14:37Z — all share `output_tokens=0` signature.
- `deal-flow` recovered (ran clean 14:45Z), no longer stuck.
- `chain:investment-advisor` failed since 6-08, off-table per spec.

**P1:** 0 open PRs · 0 urgent issues — clean.
**P2:** MEMORY.md flagged items unchanged.
**P3:** All daily skills within 2× interval; no fresh missing.

**Self-check:** heartbeat last_success ~5.5h ago — healthy.

**Files touched:**
- `docs/status.md` — regenerated (44 enabled skills, 14 open issues incl. new ISS-025, next run = evening-recap 21:00Z)
- `memory/logs/2026-06-22.md` — appended heartbeat 20:16Z entry

No notification sent (every P0/P1/P2 condition was within the 48h dedup window).
