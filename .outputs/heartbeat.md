`HEARTBEAT_OK · STATUS_PAGE=DEGRADED — wrote docs/status.md`

## Summary
- **P0 scan**: 5 STUCK skills (fork-cohort ~115h, search-skill/unlock-monitor ~95h, skill-security-scan/deal-flow ~93h); 3 consec≥3 (unlock-monitor=7, deal-flow=6, skill-security-scan=3); 13-skill chronic cohort with sr<0.5. Heartbeat self-check OK (last_success ~6.5h ago).
- **Dedup verdict**: every flag documented in 8-13 logs and 8-14 08:05Z heartbeat → no `./notify` fire (silent).
- **Status page**: regenerated `docs/status.md` — overall 🔴 DEGRADED, 15 open issues, 43-skill table sorted by last-run desc, next scheduled run btc-levels at 16:15 UTC. Token pulse section omitted (no `articles/token-report-*.md` exists).
- **Files modified**: `docs/status.md` (wholesale rewrite), `memory/logs/2026-08-14.md` (heartbeat 14:37Z log entry appended).
- **Follow-up**: ISS-032 filing still owed (9th cycle if 18Z batch also passes without filing); ISS-031 detect-usepod-402 gate +1d overdue; 8-17 Mon batch auto-clear window for the 4 Mon-scheduled STUCK skills.
