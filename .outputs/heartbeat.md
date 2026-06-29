HEARTBEAT_OK · STATUS_PAGE=DEGRADED — wrote docs/status.md

## Summary

Ran the heartbeat skill. Findings, all dedup-suppressed against the last 48h of logs (no notification fired):

- **P0 stuck:** `fork-skill-digest` still in `dispatched` state since 2026-06-28T18:38Z (~20h) — already surfaced in 6-28 20:18Z + 6-29 08:47Z hb ticks.
- **P0 chronic (sr<0.5):** 19-skill tail unchanged from morning tick — same `output_tokens=0` sandbox-truncation cluster (ISS-019/020/021/024/025) since 6-19.
- **P0 self-check:** heartbeat last_success ~6h10min ago, healthy.
- **P1:** 1 open PR (#149 docs(skill-graph), ~22h, just under 24h stall threshold). 0 urgent issues. 15 open issues unchanged.
- **P2:** BTC sub-$60.5k day 4, sandbox-truncation day 11, XAI quota day 14, on-chain config day 22 — all carried.
- **P3:** operator-scorecard Mon 10:30Z slot missed again (recurring scheduler-side gap; never-run since enabled).

Status page regenerated as 🔴 DEGRADED (15 open issues, fork-skill-digest 🕸 stuck, chronic tail). 41 enabled-skill rows sorted last-run desc + 3 never-run (autoresearch, fork-skill-gap, operator-scorecard). Token pulse section omitted — no `articles/token-report-*.md` on disk. Next scheduled: skill-security-scan at 16:00 UTC.

Files modified: `docs/status.md`, `memory/logs/2026-06-29.md`.
