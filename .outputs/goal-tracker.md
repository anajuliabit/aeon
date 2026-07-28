*Goal Tracker — 2026-07-28*

Summary: 6 goals — 1 at risk, 0 needs attention, 0 on track, 5 blocked, 0 done (overall → flat vs 7-27 snapshot, 2 new goals surfaced from weekly-review)

BLOCKED
• ISS-025 capture-step PR T+10 day-13 — 0d idle, 338 activity/14d (flat, was BLOCKED)
  → Action: Operator direct-author `dangerouslyDisableSandbox` at `.github/workflows/aeon.yml:479-495`
• 12:00 UTC batch DARK day-30 — 0d idle, 292 activity/14d (flat, was BLOCKED, ISS-027 signature durable)
  → Action: File `memory/issues/ISS-027.md` so root-cause diagnosis has a home
• ISS-027/028 doc-gap d21 escalation — 0d idle, 162 activity/14d (new, weekly-review 7-27 last-chance window passed without file creation)
  → Action: Author `memory/issues/ISS-027.md` + `ISS-028.md` (batch-dark + bash-redirect n=8+)
• PR #165 crossed 7d gate d9 — 0d idle, 138 activity/14d (new, queue at 4 open PRs breaches 3-PR gate)
  → Action: Operator merge/rebase/close #165 (CONFLICTING, no touch through weekly-review absorption)
• Operator on-chain config day-51 — 0d idle, 88 activity/14d (flat, was BLOCKED)
  → Action: Add ALCHEMY_API_KEY + ETHERSCAN_API_KEY secrets, expand `memory/on-chain-watches.yml`

AT RISK
• priorities.md 54d stale — 0d idle, 114 activity/14d (flat AT_RISK, high mention count is thought-review nudges not refresh work)
  → Action: Refresh `priorities.md` current-focus section (Reppo/Aeon lines read as work-slipped)

Notable shifts vs 7-27 snapshot: h-unlock cleared to Recently Cleared 7-26 (verdict locked spurious). 2 new goals surfaced by MEMORY.md line 6-7 (ISS-027/028 doc-gap + PR #165 gate-cross). Operator-owned unblock paths on 5 of 6 goals (only batch-dark is Aeon-side diagnosis).

Sources: logs=ok, git=ok(1 commit 30d), gh_pr=ok(4 open), gh_issue=ok(0 urgent), cron-state=ok
