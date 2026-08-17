`HEARTBEAT_OK · STATUS_PAGE=DEGRADED — wrote docs/status.md · notify=SKIPPED (dedup)`

## Summary
- **Files modified:** `docs/status.md` (rewrote wholesale — 🔴 DEGRADED verdict, 43 enabled skills, 15 open issues, next-run btc-levels 08:15Z), `memory/logs/2026-08-17.md` (appended heartbeat entry + summary).
- **P0 findings:** 1 fresh-fail (cost-report 08:00Z — matches chronic ISS-030 sdk_opt_in_required signature) + 4 stuck mon-batch skills (search-skill/unlock-monitor/deal-flow/skill-security-scan, ISS-031 aftermath, auto-clear window today) + 3 API-degradation (unlock=7, deal=6, scan=3) + 10-skill chronic cohort holds. Heartbeat self-check clean (12h since last success; 6-consec-clean streak post 8-15 crash).
- **P1:** PR queue at 6 unchanged; #174/#176/#177 all cross 7d weekly-review stall band; self-improve exit-gate ENGAGED n=3. No urgent issues.
- **P2/P3:** All flagged items in MEMORY.md (11-consec zero-capture, on-chain config d72, ISS-031 detect-script overdue). 12Z batch DARK d51 (round-51 crossing).
- **Notification:** SKIPPED — every finding appears in the morning-brief 07:31Z (40 min ago) or MEMORY.md per SKILL.md dedup rule.
- **Follow-up:** 10Z unlock-monitor / 14Z search-skill+deal-flow / 16Z skill-security-scan mon-batch auto-clear tests are today's ISS-031 recovery decider; 10:30Z operator-scorecard first-ever fire; 14Z next heartbeat re-evaluates.
