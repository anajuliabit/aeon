HEARTBEAT_OK · STATUS_PAGE=DEGRADED

## Summary

Heartbeat ran clean — every P0/P1/P2/P3 finding dedup'd against the 6-09 heartbeat (08:56 + 20:51 UTC), so no notification was sent. Self-check OK (last_success ~11.5h ago).

**Findings:**
- 11 stuck `last_status=dispatched` skills carry from the 2026-06-06/07/08 claude weekly rate-limit cluster — all weekly slots (Sat/Sun/Mon) that won't re-fire until their next cron tick. Drained from yesterday's 20 → 11 today as daily slots recovered.
- `chain:investment-advisor` still failed since 2026-06-08 — chain dropped from current `aeon.yml`, kept off status table.
- Recovery: `chain:reppo-swarm` 06:53 UTC cycle clean — landed mint 22 (BTC+XPL hft `0xcc12..57bf`) and mint 23 (1337 closes 7 perps Sharpe 427 `0x369daedb` +$104k win 100%) — first fully clean chain run since yesterday's 18:39 UTC digest failure.
- 0 open PRs, 0 urgent issues, 6 open ISS items (unchanged).

**Files modified:**
- `docs/status.md` — Overall=🔴 DEGRADED, 45-row skill table, 6 open issues, next run aixbt-pulse 09:00 UTC, token-pulse section omitted (no `articles/token-report-*.md`).
- `memory/logs/2026-06-10.md` — appended `### heartbeat` entry with full P0–P3 findings.
