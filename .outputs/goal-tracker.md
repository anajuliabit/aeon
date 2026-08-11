goal-tracker — 2026-08-11

summary: 9 goals — 0 at-risk, 0 needs-attention, 4 on-track, 4 blocked, 1 done (overall → flat)

ON TRACK
• iss-030 cost-report 4-consec-week formal-pattern — 0d idle, 15 activity/14d (→ flat) — n=3 same-signature intra-18h 8-10 20:32z + 8-11 08:19z + 8-11 14:14z, consec=33 sr=7%
• chronic-cohort-alone-degraded regime — 0d idle, 10 activity/14d (→ flat) — 12+ consec-tick durability ~131h span, composition-stable through today
• fork-cohort stuck p0 novel — 0d idle, 8 activity/14d (new) — 67h+ dispatched, 48h escalation threshold ~19:05z tonight
• pr queue at 3 — 0d idle, 13 activity/14d (→ flat) — #174 87h no-CI, #176 skill-graph regen, #177 iss-028 doc

BLOCKED
• iss-028 workaround-chain n=39+ — waiting on operator batch-review of #167 (fix-scope-narrow) + #177 (doc) since 2026-07-30
  → action: operator merges pr #167 + pr #177 in weekly batch
• iss-027 12z batch dark d45 — waiting on scheduler-side gap fix since 2026-06-28
  → action: operator escalates 8-skill scheduler batch-dark gap
• operator on-chain config day-66 — waiting on operator secrets since 2026-06-07
  → action: operator adds on-chain-watches.yml + alchemy_api_key + etherscan_api_key
• priorities.md 68d stale — waiting on operator refresh since 2026-06-04
  → action: operator refreshes priorities.md in weekly-review slot

DONE
• weekly-shiplog 8-10 — completed 2026-08-10

sources: logs=ok, git=ok, gh_pr=ok, gh_issue=ok, cron-state=ok
