HEARTBEAT_OK · STATUS_PAGE=DEGRADED — wrote docs/status.md

## Summary
- Read `memory/MEMORY.md` + last 2 days of logs for context; pulled `memory/cron-state.json`, `memory/issues/INDEX.md`, `aeon.yml`.
- **P0**: 0 failed, **13 stuck** (11 weekly rate-limit carry-overs from 6-06/6-07/6-08 + 2 daily hangs `list-digest` 6-10T17:24 / `fleet-control` 6-10T16:10). `btc-levels` self-recovered overnight (00:40 + 05:49 UTC clean). 0 chronic. Heartbeat self-check OK (~12.8h ago).
- **P1**: 0 open PRs, 0 urgent issues.
- **P2/P3**: 3 never-run (autoresearch / fork-skill-gap / operator-scorecard); memory follow-ups already tracked in this morning's brief.
- **Dedup**: every P0 finding appears in last 48h logs (yesterday's 3 heartbeats + 07:26Z morning-brief). **No notification sent.**
- Regenerated `docs/status.md` — Overall 🔴 DEGRADED, 44 skill rows sorted last-run desc, Token pulse omitted (no `articles/token-report-*.md`), Next scheduled `token-alert at 12:00 UTC`.
- Files modified: `docs/status.md`, `memory/logs/2026-06-11.md`.
