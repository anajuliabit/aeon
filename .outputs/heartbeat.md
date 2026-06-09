HEARTBEAT_OK · STATUS_PAGE=DEGRADED — wrote docs/status.md

## Summary
- **Heartbeat run**: 2026-06-09 ~08:56 UTC (08:00 cron slot). Self-check now OK (~12h since last success, clears yesterday's 67h self-stale flag).
- **P0**: All known — `chain:investment-advisor` failed (dropped from table since not in current aeon.yml); 26 stuck dispatches from yesterday's 6-08 rate-limit cluster; no new consecutive_failures or chronic. All dedup against 6-08 heartbeat log.
- **P1**: 0 open PRs, 0 urgent-labeled issues.
- **P2/P3**: ISS-009 sub-task (b) carry (dedup); 3 enabled-but-never-run skills (autoresearch / fork-skill-gap / operator-scorecard).
- **Recovery signals (already in today's morning-brief log)**: `chain:reppo-swarm` 06:24 cycle clean — mint 20 0x06cecfba AAVE +$85,196 landed. morning-brief / daily-routine / thought-review all ✅ this morning.
- **Notification**: None sent (every finding appears in last 48h logs).
- **Status page**: Regenerated `docs/status.md` — Overall 🔴 DEGRADED, 6 open issues, next run aixbt-pulse 09:00 UTC, 44 rows in the skill table. Token pulse section omitted (no `articles/token-report-*.md` file exists).
- **Files modified**: `docs/status.md`, `memory/logs/2026-06-09.md` (heartbeat entry appended).
