Heartbeat complete. All findings deduped vs 48h logs → NOOP notification, no `./notify` call.

`HEARTBEAT_OK · STATUS_PAGE=DEGRADED`

**Findings:**
- **P0 cost-report state-change** — stuck→FAILED d7, cf 5→8 (+3 today), scheduler picked up Mon-weekly tick in 12:57Z batch instead of 07:00Z slot. ISS-025 sandbox-truncation signature. Deduped vs morning-brief 07:54Z focus #1.
- **P0 14-skill chronic sr<0.5 tail** — all ISS-025-family, all deduped.
- **P0 self-check ok** — heartbeat last_success ~18h42m ago, under 36h gate.
- **P1 PR #162 MERGED** — memory-stale delta (Current Goals lines 5-7 still list #162 CONFLICTING); down to 2 open self-improve PRs (#163+#164) + 1 new #165 docs. Memory-refresh candidate for reflect cycle.
- **P1 PR #164 stalled 5d**, PR #163 active today 14:19Z, PR #165 1-day-old.
- **P3 12:00Z batch dark d23** — 8-skill cluster frozen at 6-28, ISS-027 per-skill-blockage n=23 confirmed by token-alert/btc-levels/cost-report firing clean same slot.
- **P3 weekly-shiplog Mon-miss test NEGATIVE** — fired clean today 10:55Z, revises morning-brief focus #3.

**Status page:** overall 🔴 DEGRADED, 11 open issues, next scheduled skill-security-scan Mon 16:00Z (~41min). Wrote `docs/status.md` with 43 enabled skills sorted last-run desc; token-pulse omitted (no `articles/token-report-*.md`).

**Files modified:** `docs/status.md`, `memory/logs/2026-07-20.md`.
