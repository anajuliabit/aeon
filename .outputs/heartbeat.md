Heartbeat complete.

## Summary

Ran the **heartbeat** skill for 2026-06-15 (~09:48 UTC). All priority checks done; status page regenerated.

**P0 — Failed & stuck (no fresh items):**
- `chain:investment-advisor` — carry fail (dropped from `aeon.yml`, off-table per spec).
- `btc-levels` — failed 05:42Z, **recovered 07:38Z** (sr 96%, cf 0). Already surfaced in today's morning-brief.
- Stuck: `skill-freshness` (6-14, ~25h, already notified 6-14 14:55Z), `fork-cohort` (6-14, ~14h, 2nd consecutive Sunday tick, covered 6-14 20:25Z), and 4 Monday weekly carryovers awaiting today's ticks.
- **Recovery:** `cost-report` cleared at 07:45Z (Monday tick).
- No consecutive_failures ≥3, no chronic sr<0.5. Heartbeat self-check OK (~13.3h since last success).

**P1:** 1 open PR (#112, ~16h, under threshold). 0 urgent issues.
**P2/P3:** ISS-019 + INDEX flips carried in MEMORY.md; `fork-skill-gap` still never-run.

**Dedup:** every finding is already in the last-48h logs → **no notification sent**.

**Files modified:**
- `docs/status.md` — regenerated, Overall 🔴 DEGRADED, 42 skill rows, `cost-report` flipped to ✅. Token pulse omitted (no `articles/token-report-*.md`).
- `memory/logs/2026-06-15.md` — appended heartbeat log entry.

`HEARTBEAT_OK · STATUS_PAGE=DEGRADED` — wrote docs/status.md, no notify (dedup).

**Follow-up (carried, operator-side):** file ISS-019 (weekly-limit wave, 6d overdue); flip ISS-007/009/010/016 in INDEX (5d overdue).
