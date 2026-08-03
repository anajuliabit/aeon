*goal tracker — 2026-08-03*

summary: 7 goals — 1 at risk, 2 needs attention, 4 blocked, 0 on track, 0 done. 0 status shifts vs 8-02; today opens PR #165 7d-past-touch escalation window + rolls ISS-025 T+5 day-20 slip.

AT RISK
• priorities.md 60d stale — 1d idle, 176 mentions/14d (flat; mentions are meta-flag nudges, no refresh work)
  → action: operator refresh priorities.md; audit vault inbox 43d cold streak

NEEDS ATTENTION
• PR #165 docs(skill-graph) d15 CONFLICTING — 1d idle, 280 mentions/14d (↑ activity, status flat; 7d-past-touch escalation window OPEN today)
  → action: rebase PR #165 onto main; ship in 8-03 weekly-batch merge window
• PR #171 fresh self-improve ~64h — 1d idle, 271 mentions/14d (↑ activity, status flat; ci-skills-json FAILURE 3-consec shared with #172)
  → action: investigate ci-skills-json shared failure across PRs #171 + #172

BLOCKED
• ISS-025 cost-report hand-off T+5 day-20 SLIPPED — 1d idle, 494 mentions/14d (flat; sr=0.12 durable weakest chronic-failure, 15-consec heartbeat DEGRADED)
  → action: operator direct-author dangerouslyDisableSandbox pivot at .github/workflows/aeon.yml:479-495
• 12:00 UTC batch DARK day-37 — 1d idle, 418 mentions/14d (↑ activity, status flat; 8-skill cluster frozen since 6-28, 41st consec clean CG day)
  → action: trigger manual 12:00Z batch to force ISS-027 signature capture
• ISS-028 kill-test workaround-chain — 1d idle, 351 mentions/14d (↑ activity, status flat; kill-test d5 NEGATIVE, workaround-chain n=18+ durable 12-UTC-day span)
  → action: reopen PR #167 scope at weekly-review 8-03; patch sub-agent + skill-graph surfaces
• operator on-chain config day-58 — 1d idle, 153 mentions/14d (↑ activity, status flat; defi-monitor NO_CONFIG, keys missing)
  → action: operator populate memory/on-chain-watches.yml + add ALCHEMY_API_KEY + ETHERSCAN_API_KEY

sources: logs=ok, git=ok, gh_pr=ok, gh_issue=ok(empty), cron-state=ok
