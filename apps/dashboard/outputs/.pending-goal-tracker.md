*Goal Tracker — 2026-07-27*

Summary: 5 goals — 1 at risk, 0 needs attention, 1 on track, 3 blocked (overall → flat)

BLOCKED
• **ISS-025 capture-step PR** — T+10 day-11 (5d past slip), 370 activity/14d
  Verb-pool exhausted (12+ named verbs); downgraded actionable→reflect-scope, weekly-review hand-off.
  → Operator direct-author dangerouslyDisableSandbox pivot in .github/workflows/aeon.yml:479-495

• **12:00 UTC batch DARK** — d29 frozen (2026-06-28 21:00Z), 212 activity/14d
  8-skill cluster locked by ISS-027; same-slot clean fires confirm pattern-independent. 
  → Diagnose ISS-027 root cause or escalate

• **Operator on-chain config** — d50 blocked, 88 activity/14d, trend -52%
  ALCHEMY_API_KEY + ETHERSCAN_API_KEY missing from GitHub Actions secrets.
  → Add both secrets, optionally expand on-chain-watches.yml pool

ON TRACK
• **H unlock monitor** — 1d idle, 148 activity/14d (↑ improving +169%)
  Cliff-day 7-25 spurious verdict locked (H +5.8% no-signature 7-25, -4.0% drift 7-26)

AT RISK
• **priorities.md 52d stale** — 96 activity/14d, first 52d+ round-cross
  Last reviewed 2026-06-04; current-focus lines read as live-work-slipped.
  → Refresh priorities.md to shipped vs active work

Sources: logs=ok, git=ok, gh_pr=ok, gh_issue=ok, cron-state=ok
