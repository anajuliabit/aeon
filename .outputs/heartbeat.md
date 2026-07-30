Heartbeat complete.

## Summary

Ran `skills/heartbeat/SKILL.md` at 21:09 UTC (69min lag off 20:00Z scheduled tick, consistent with observed dispatch-lag pattern).

**Files modified:**
- `docs/status.md` — refreshed with 43-skill table + **13 open issues** (up 11→13 after reflect filed ISS-027 + ISS-028 at 18:22Z), Overall 🔴 DEGRADED, next-run btc-levels 21:15 UTC
- `memory/logs/2026-07-30.md` — appended heartbeat entry with P0/P1/P2/P3 findings, delta since 15:16Z, dedup verdict

**Findings:**
- **P0:** 10-skill chronic-failure cohort persists (**8-consec heartbeat ticks verdict-string identity across ~49h span**)
- **P1:** 3 open PRs — #165 d11 + #167 d7 (past-gate) + #170 26h (crosses 24h stalled gate but weekly-batch cadence in-window)
- **P2 positive:** ISS-027 + ISS-028 doc-gap **CLOSED** at 18:22Z by reflect scope-absorb (24d load-bearing gap resolved, action-converter's 4-consec max-score-125 shape finally converts)
- **P3:** 21:00Z evening-recap + thought-review in dispatch-lag window (not yet escalation)

**Notification:** DEDUP_SKIP — all findings covered in 48h logs (chronic regime + iss-025 T-0 + PR queue all pre-notified; ISS-027/028 closure notified by reflect at 18:22Z).

**Output:** `HEARTBEAT_OK · STATUS_PAGE=DEGRADED — wrote docs/status.md · NOTIFY=DEDUP_SKIP`
