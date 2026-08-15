*Goal Tracker — 2026-08-15*

Summary: 9 goals — 1 at risk, 0 needs attention, 2 on track, 6 blocked, 0 done (overall → flat, degrading on fork-cohort + iss-031)

AT RISK
• iss-031 detect-usepod-402 gate deadline — +2d overdue, `scripts/detect-usepod-402.sh` still absent per 14:08Z heartbeat file-check (was +1d ↓ degrading)
  → Action: ship `scripts/detect-usepod-402.sh` preflight gate once operator clears self-improve exit-gate

BLOCKED
• fork-cohort iss-032 unfiled — 12th+ owed cycle at ~140h stuck, memory-window unprecedented depth (was 9th+ ↓ degrading)
  → Action: operator hand-file `memory/issues/ISS-032.md` — INDEX.md verified still ends at ISS-031
• self-improve pr queue exit-gate engaged n=3 — #177/#179/#180 self-improve-shaped block new authoring per claude.md primitive (new goal, → flat)
  → Action: operator merge 3+ PRs from #174/#176/#177/#179/#180 via sunday 8-16 weekly-batch
• 4 mon-batch stuck skills — ~119h stuck since 8-10 (search-skill / unlock-monitor / skill-security-scan / deal-flow); iss-031 usepod-402 aftermath (→ flat)
  → Action: wait for 8-17 mon auto-clear or trigger manual usepod dispatcher recovery
• 12z batch dark d49 — iss-027 8-skill cluster frozen since 6-28 (→ flat)
  → Action: operator restore 12z scheduler slot for 8-skill batch
• operator on-chain config day-70 — defi-monitor NO_CONFIG (→ flat, ageing)
  → Action: operator populate `memory/on-chain-watches.yml` + set ALCHEMY_API_KEY + ETHERSCAN_API_KEY
• priorities.md 72d stale + vault inbox 54d cold + 9-consec zero-capture streak — 10-day mark 8-16 = memory-window record if unbroken (→ flat, ageing)
  → Action: operator refresh `vault/priorities.md` + process 2026-06-22 inbox capture

ON TRACK
• pr queue at 5 open — #174 crosses 7d weekly-review stall band today, sunday 8-16 weekly-batch imminent (→ flat)
• `[[chronic-cohort-alone-degraded]]` regime — 13-skill composition ~210h span holds unchanged (→ flat)

Sources: logs=ok, git=ok(1), gh_pr=ok, gh_issue=ok, cron-state=ok
