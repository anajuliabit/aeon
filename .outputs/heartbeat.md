`HEARTBEAT_OK · STATUS_PAGE=DEGRADED`

**Findings (all deduped, notification skipped per 48h window):**
- **P0 chronic tail unchanged** — 18-skill sr<0.5 cluster (ISS-019/020/021/025 sandbox-truncation systemic day-16). No `last_status: failed` rows, no stuck-dispatched rows, all `consecutive_failures = 0`. Self-check ok (last hb 12.5h ago).
- **P1** PR #155 day-3 stall (~63.6h, supersede-dup after PR #149 merged 7-06); PR #160 operator activity 14.5h old under 24h threshold; zero urgent issues.
- **P2** SLX day-14 catastrophic -46%; ISS-025 capture-step PR day-16 unshipped (deadline 7-13).
- **P3** 12:00Z batch dark day-11; aixbt-pulse dead-slot day-10 CONFIRMED (7-08 09:00Z tick not in run list); operator-scorecard Mon 7-06 miss day-8.

**Status page:** `docs/status.md` regenerated — 43 enabled skills sorted by last_success desc (evening-recap 22:03Z now tops; was stale in prior render), 3 never-run rows at bottom, 12 open issues, verdict DEGRADED, next-run pointer token-alert @ 12:00Z.

**Delta vs 7-07 20:29Z hb:** day-N counter ticks only (SLX 13→14, batch d10→d11, aixbt-pulse d9→d10, ISS-025 d15→d16). No fresh signal.
