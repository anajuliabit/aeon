*goal tracker — 2026-08-07*

9 goals — 0 at risk, 0 needs attention, 3 on track, 5 blocked, 1 done (overall ↑ improving; iss-029 clears to done, chronic-cohort + morning-08z-slot enter as new on-track observations)

ON TRACK
• chronic-cohort-alone-degraded regime — 0d idle, 7 activity/14d (new; 4th 24h durability gate crossed 8-07 09:15Z, cross-3-full-utc-day)
• morning-08z-slot-dark sub-rail — 0d idle, 6 activity/14d (new; formal-pattern promoted n=3 → n=4-consec 8-07 09:15Z heartbeat)
• iss-030 cost-report sdk_opt_in_required — 0d idle, 10 activity/14d (→ flat; consec 18→0 organic 8-04, chronic sr=10%, deciding-test 8-10 mon 07z)

BLOCKED
• iss-028 workaround-chain (n=30+, 16-utc-day span) — waiting on root-cause investigation since 2026-07-22 (pr #167 fix-scope narrow)
  → Action: widen pr #167 fix-scope to sub-agent + list-digest + skill-graph + append + url-encoded surfaces before 8-10 weekly-review
• 12:00 utc batch dark (iss-027) d41 — waiting on operator scheduler-config since 2026-06-28 (8-skill cluster frozen)
  → Action: file weekly-review 8-10 escalation with 8-skill list + standalone-inline substitution proof
• pr queue at 4 — waiting on pr #173 ci trigger (~90h cold) blocking #171 + #172, plus #165 d19 conflicting to 8-10 sunday-batch
  → Action: push empty commit to pr #173 to nudge ci trigger before 8-10 sunday-batch (t-2)
• operator on-chain config d62 — waiting on operator alchemy_api_key + etherscan_api_key + on-chain-watches.yml since 2026-06-07
  → Action: tag operator in weekly-review 8-10 refresh-ask with concrete config-diff (no automated path)
• priorities.md d64 stale + vault inbox d47 cold — waiting on operator refresh (thought-review skill-spec ownership) since 2026-06-04
  → Action: tag operator in weekly-review 8-10 refresh-ask (no automated write path)

DONE
• iss-029 usepod 402 recovery — completed 2026-08-04 (44h+ clean, index.md resolved section)

Sources: logs=ok, git=ok, gh_pr=ok, gh_issue=ok, cron-state=ok
