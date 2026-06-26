HEARTBEAT_OK · STATUS_PAGE=DEGRADED — wrote docs/status.md

## Summary

**Heartbeat 20:14 UTC (evening tick):**
- **P0:** clean — 0 failed/stuck, cf=0 across all 42 dispatched skills, no skill at cf≥3. Heartbeat self-check 6.1h ago, healthy.
- **P0 chronic:** 20-skill `output_tokens=0` sandbox-truncation tail unchanged from 14:05Z run (ISS-019/020/021/024/025 cluster), worst vuln-scanner 7% / reg-monitor 10% / cost-report 10%.
- **P1:** 0 open PRs — PR #147 (advisor risk-layer #140 impl) merged this afternoon. 0 urgent issues.
- **P2:** sandbox-truncation systemic, XAI quota day 11, on-chain config day 19, BTC breakdown confirmed — all carried, all in last-48h logs.
- **P3:** all 44 enabled skills accounted for, 3 never-run on workflow_dispatch or weekly schedule.

**Dedup:** every finding is a same-signature continuation of items already covered in last-48h logs → no notification fired.

**Status page:** rewrote `docs/status.md` — verdict 🔴 DEGRADED, 41 enabled-skill rows sorted last-run desc, 3 never-run sunk to bottom, 14 open issues unchanged, token-pulse section omitted (no `articles/token-report-*.md` on disk). Next scheduled: btc-levels at 20:15 UTC.

**Files modified:** `docs/status.md` (refreshed timestamps + verdict), `memory/logs/2026-06-26.md` (appended Heartbeat 20:14 UTC findings).
