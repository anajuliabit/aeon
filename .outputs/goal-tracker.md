*Goal Tracker — 2026-08-13*

Summary: 10 goals — 0 at risk, 1 needs attention, 3 on track, 6 blocked, 0 done (overall → flat, fork-cohort ↓ degrading)

NEEDS ATTENTION
• iss-031 detect-usepod-402 gate — 0d idle, 5 activity/14d (new); deadline TODAY, script not shipped
  → ship `scripts/detect-usepod-402.sh` in 18Z self-improve window

BLOCKED
• fork-cohort P0 stuck ~110h — waiting on ISS-032 file-op since 8-11 18:40Z, ~5 owed cycles unfiled (↓ degrading)
  → file ISS-032 manually if 8-13 18Z action-converter punts a 6th time
• iss-028 workaround-chain n=41+ — waiting on operator batch-review of PR #177 (~4d) + PR #167 (flat)
  → merge PR #177 in weekly batch
• iss-027 12Z batch dark d47 — scheduler-side gap since 2026-06-28 (flat)
  → operator dispatcher-path fix or manual re-enable
• operator on-chain config day-68 — waiting on `memory/on-chain-watches.yml` + ALCHEMY/ETHERSCAN keys since 6-08 (flat)
  → operator adds YAML + API keys
• priorities.md 70d stale + vault inbox 52d cold — 7-consec zero-capture streak; refresh-ask 3d unactioned (flat)
  → operator refreshes priorities.md
• 4 Mon-batch stuck skills — search-skill / unlock-monitor / skill-security-scan / deal-flow, self-clear 8-17 (new)
  → wait for 8-17 Mon auto-clear or operator intraweek manual invoke

ON TRACK
• iss-030 cost-report 4-consec-week formal-pattern — 0d idle, 16 activity/14d; 8-11 20:08Z organic recovery = 2nd precedent, 8-17 Mon next deciding-test (flat)
• chronic-cohort-alone-degraded regime — 0d idle, 12 activity/14d; 13-skill composition holds ~180h span (flat)
• pr queue at 4 — 0d idle, 14 activity/14d; #179 (~44h) + #177 (~4d) + #176 (~4d) + #174 (~5d), all within weekly-batch cadence (flat)

Sources: logs=ok, git=ok(shallow), gh_pr=ok, gh_issue=ok, cron-state=ok
