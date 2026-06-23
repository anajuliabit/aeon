Heartbeat complete. Summary follows.

## Summary

- **Verdict:** `HEARTBEAT_OK · STATUS_PAGE=DEGRADED`. The only NEW P0 signal is `cost-report` cf escalating 17→18 (fresh 07:35Z fail) — same ISS-025 sandbox-truncation root cause that today's 07:07Z morning-brief and 6-22 20:16Z heartbeat both already covered, so dedup blocked the notification.
- **Status page regenerated:** `docs/status.md` — 44 enabled-skill rows sorted last-run desc, cost-report bumped to ❌ failed cf=18 sr=14% at top, btc-levels/daily-routine/morning-brief/thought-review timestamps rolled to today, evening-recap/aixbt-pulse refreshed from last night, 14 open issues, 3 never-run at bottom, Token pulse section omitted (no `articles/token-report-*.md` on disk). Next scheduled: aixbt-pulse 09:00Z.
- **P0 self-check:** heartbeat last_success ~12h ago — healthy. No stuck-dispatched skills. Chronic-failure tail (22 skills sr<0.5) carried.
- **P1:** 0 open PRs, 0 urgent issues.
- **Files touched:** `docs/status.md`, `memory/logs/2026-06-23.md` (appended heartbeat block).
- **Follow-up:** ISS-025 still widening (cf=18) — same systemic sandbox-truncation root cause as ISS-019/020/021/024; durable fix is a fleet-level concern, not heartbeat's to solve. A stray `.tmp-extract-enabled.py` was created in the repo root during research; it is gitignored (`.tmp-*`) so won't be committed.
