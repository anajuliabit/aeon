HEARTBEAT_OK · STATUS_PAGE=DEGRADED — wrote docs/status.md

**Findings:**
- **P0 stuck**: fork-skill-digest still `dispatched` ~14h after 2026-06-28T18:38Z (cancelled run stranded the row). Already notified at yesterday's 20:18Z hb — within 48h dedup window, no re-notification.
- **P0 chronic**: 19-skill `output_tokens=0` sandbox-truncation tail unchanged (ISS-019/020/021/024/025 cluster, day 11).
- **P0 self-check**: heartbeat last_success ~12.5h ago, healthy.
- **P1**: 1 open PR (#149 docs(skill-graph), ~15.5h fresh). PR #148 fix(agent-buzz) cleared from open list (merged or closed). 0 urgent issues. 15 open issues unchanged.
- **P2**: sandbox-truncation day 11, XAI quota day 14 BLOCKED, on-chain config day 22, BTC breakdown EXTENDED day 4 (btc-levels 01:21Z fired alert for 6-28 close $59,612, alert was its own notification).
- **P3**: all 44 enabled skills accounted for; 3 never-run carry, no >2x-interval flags.

**No notification fired** — every finding is dedup-blocked within 48h logs.

**Files written:**
- `docs/status.md` — Overall 🔴 DEGRADED, btc-levels promoted to top (2026-06-29 05:12 UTC), 41 ran-rows + 3 never-run, 15 open issues, token-pulse section omitted (no `articles/token-report-*.md` on disk).
- `memory/logs/2026-06-29.md` — appended heartbeat run entry.

**Follow-up:** two 0-byte temp files (`.tmp_check.py`, `.tmp_skills.py`) left in working dir — the harness blocked `rm`/`mv`; the workflow's `git add -A` will sweep them in. Worth adding `.tmp_*` to `.gitignore` next session.
