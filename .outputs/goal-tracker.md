*Goal Tracker — 2026-07-19*

summary: 6 goals — 0 at risk, 0 needs attention, 0 on track, 6 blocked, 0 done (overall → flat, all 6 blockers persist across UTC-day rollover)

BLOCKED (sorted by blocker-age descending; days_since_last_activity all 0 today)
• operator on-chain config day-42 → day-43 — waiting on ALCHEMY_API_KEY + ETHERSCAN_API_KEY + `memory/on-chain-watches.yml` pool/position entries. defi-monitor NO_CONFIG carries.
  → action: add ALCHEMY + ETHERSCAN secrets and extend on-chain-watches.yml past 5 wallet-only entries with type:pool + type:position rows.
• 12:00 UTC batch DARK day-21 → day-22 — 8-skill 12:00Z cluster (defi-overview/token-pick/narrative-tracker/market-context-refresh/token-movers/on-chain-monitor/defi-monitor/aixbt-pulse) frozen at 2026-06-28 per ISS-027 scheduler routing block. Positive delta: 07:00Z morning-batch d3 durable-recover confirmed by daily-routine 07:14Z — sub-arc holds, main arc still dead.
  → action: fix ISS-027 12:00Z per-skill dispatch routing (token-alert + btc-levels fire clean same slot = scheduler-side, not skill code).
• cost-report STUCK d5 → d6 ~137h29m — last_status: dispatched 2026-07-13T20:44Z, cf=5, sr=0.10, ~20d since last_success 2026-06-29T13:59Z. ISS-025 sandbox-truncation family day-27, upstream block = ISS-025 capture-step PR.
  → action: merge ISS-025 capture-step PR (unblocks 15-skill sr<0.5 tail as byproduct).
• 3 self-improve PRs CONFLICTING past stall gates — PR #162 (daily-routine) T+5 day-6 ~188h · PR #163 (skill-security-scan) ~140h past 72h gate · PR #164 (investment-advisor) ~91h past 24h gate. All mergeable=UNKNOWN, blocks upstream rule-5 codification via improvement-PR-queue-locks-self-improve exit-gate.
  → action: close or force-rebase PR #162 #163 #164 against main.
• ISS-025 capture-step PR T+2 → T+3 day-4 — waiting on operator direct-author against `.github/workflows/aeon.yml:479-495`. Rule-5 workflow-file class blocks self-improve routing; operator direct-author is sole reliable path per n=4 auto-committed state drift primitive.
  → action: author operator PR against aeon.yml:479-495 chain-runner capture-step.
• CLAUDE.md rule-5 codification T+1 → T+2 — self-improve last_success 2026-07-17T18:55Z sr=0.46 unchanged, exit-gated on 3+ open PRs. 18:00Z fire tonight tests 2-consec improvement-PR-queue-locks-self-improve pattern.
  → action: ship CLAUDE.md rule-5 section direct (bypasses self-improve exit-gate lock, codifies auto-commit-drift n=4 for future cycles).

sources: logs=ok, git=ok, gh_pr=ok, gh_issue=ok, cron-state=ok
