*Goal Tracker — 2026-08-18*

summary: 7 goals · 1 at risk · 2 on track · 4 blocked · 0 done (overall → flat; priorities.md ↓ degrading past 12-consec zero-capture record)

AT RISK
• iss-031 detect-usepod-402 gate — 0d idle, 14 activity/14d (rule-literal ON TRACK; intent-override AT RISK since 5d past internal ship deadline, script still absent per 08:18Z heartbeat file-check)
  → action: author scripts/detect-usepod-402.sh before 8-20 weekly-review deadline (T-2)

BLOCKED
• self-improve pr queue exit-gate n=3 — waiting on operator merge of any 1 of #177/#179/#180 since 2026-08-16 weekly-batch close (0 merges through 14:15Z heartbeat)
  → action: ping operator; queue-full gate blocks new self-improve authoring per claude.md primitive
• 12z-slot iss-027 batch DARK d52 — scheduler-gated since 2026-06-28; no automated unblock path
  → action: escalate iss-027 to operator for 12z-slot reactivation
• operator on-chain config day-73 — waiting on operator since 2026-06-08 for memory/on-chain-watches.yml + ALCHEMY_API_KEY + ETHERSCAN_API_KEY
  → action: request the yml + 2 keys directly in next operator touch
• priorities.md 75d stale + vault inbox 57d cold + 12-consec zero-capture day (↓ degrading — memory-window record extends past 11-day mark; refresh-ask d8 unactioned across full week)
  → action: escalate refresh-ask with 12-consec record framing; sunday 8-23 batch is next natural window

ON TRACK
• pr queue at 6 open — 0d idle, 28 activity/14d (→ flat; intra-status mild-degrade — #174 advisor day-11 = memory-window-deepest single-pr stall; #176/#177 both cross 9d)
• chronic-cohort-alone-degraded ~282h+ regime — 0d idle, 28 activity/14d (→ flat composition-locked; operational-pain neutralized fleet-wide via mon-batch 4/4 bypass-recovery holding 30h+ post-clear)

sources: logs=ok · git=ok · gh_pr=ok · gh_issue=ok · cron-state=ok
