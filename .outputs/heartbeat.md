*heartbeat — 2026-06-16 20:25z*

🔴 stuck: 14:29z cron tick stalled a 4-skill batch — heartbeat (14:00 fire), narrative-tracker, market-context-refresh, security-digest all dispatched together and none wrote `success` ~6h later. heartbeat's row will flip ✅ on next refresh (this 20:00 tick is what regenerated the status page); narrative/market-context/security-digest are real day-misses.

🟡 stalled: pr #122 fix(docs) crossed 24h threshold — opened 6-15 19:13z, now ~25h, action needed (approve/merge).

carry (no fresh notify, in last 48h logs): deal-flow stuck 8d since 6-08; fork-cohort stuck 49h since 6-14; pr #112 stalled 50h; iss-019 unfiled / index flips / watches.yml seed / xai quota wall — all in memory goals.

status page: docs/status.md regenerated → 🔴 degraded. 43 enabled rows, 5 🕸 stuck (4 fresh 14:29z + fork-cohort + deal-flow — fork-cohort/deal-flow counted once each, the batch is the new news). open issues 7, next scheduled evening-recap 21:00z.
