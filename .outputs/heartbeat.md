Heartbeat complete.

## Summary

Ran the **heartbeat** skill for 2026-06-12 20:30 UTC. This is the first heartbeat to clear since 6-11 15:03 — the 6-11 20:00, 6-12 08:00, and 6-12 14:00 slots all hung in a fresh rate-limit wave, so no alert had reached the operator.

**Key finding — recurring weekly-limit wave back (ISS-018):** ~12 daily skills hung at `last_status=dispatched` between 07:05–14:57 UTC today, *including heartbeat's own 08:00 and 14:00 runs*. The cause is confirmed by a diagnostic split:
- The 5 `FALLBACK_CG_SKILLS` (defi-overview / token-movers / token-pick / token-alert / market-context-refresh) all **succeeded** via the Virtuals fresh-fetch fallback.
- Every non-fallback skill dispatched in the same window **hung** (on-chain-monitor / defi-monitor both stuck at 12:42).

That split rules out an external API and points squarely at the claude weekly limit. The fleet **self-recovered** after the midday reset — the entire 16:00–18:16 evening cluster ran clean. Residual gap: non-CG daily skills (on-chain/defi-monitor, narrative-tracker, security-digest, search-skill, morning slate) have no fallback and just hang.

**Actions taken:**
- **Notification queued** to `.pending-notify/heartbeat-msg.md` (command-substitution sandbox-blocked → documented fallback). Fresh notify warranted: the 6-12 wave and the hung heartbeats are not in the last 48h logs.
- **Regenerated `docs/status.md`** — Overall 🔴 DEGRADED, updated timestamp 20:30 UTC, 42-skill table sorted last-run desc, fallback-split prose.
- **Logged** full findings to `memory/logs/2026-06-12.md`.

**Files modified:** `docs/status.md`, `memory/logs/2026-06-12.md`, `.pending-notify/heartbeat-msg.md`.

**Follow-up (carried, operator/goal-gated):** ISS-018.md still unfiled — today is the 4th occurrence, strengthening the case that it recurs weekly and that non-CG dailies need a fallback path. INDEX flips (ISS-007/009/010/016) and datanet RUBRIC.md remain overdue.

Verdict: **HEARTBEAT_ATTENTION · STATUS_PAGE=DEGRADED**
