Heartbeat 20Z run complete.

`HEARTBEAT_OK · STATUS_PAGE=DEGRADED — wrote docs/status.md · notify=SKIPPED-DEDUP`

## Summary
- **Files modified:** `docs/status.md` (regenerated, overall=🔴 DEGRADED, 43-skill table, updated 2026-08-15 20:15 UTC, heartbeat row flipped back to ✅ success), `memory/logs/2026-08-15.md` (heartbeat 20:15Z entry appended).
- **P0:** 5 STUCK skills carried (fork-cohort ~145h + 4 Mon-batch waiting for 8-17 self-clear), 3 skills consec≥3, 13-skill chronic sr<0.5 cohort — all rollover from 14:08Z, dedup-blocked.
- **Deciding-test outcome:** 08Z heartbeat crash self-cleared at 14:15Z + this 20Z fire clean = **one-off confirmed**, not a fresh recurring cliff. No memory-issue-file needed.
- **Notify:** SKIPPED per dedup rule — every P0/P1/P2/P3 flag already notified within 48h window; only fresh signal is positive recovery (not a notify-worthy flag).
- **Follow-up:** Sunday 8-16 weekly-batch is next structural event; ISS-032 escalated to 13th owed cycle; evening-recap fires next at 21:00 UTC.
