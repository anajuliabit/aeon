*5 Actions — 2026-07-20*
Shape: submit iss-025 patch, resolve pr-164, revise memory.md, land pr-165, draft supply-chain topic

1. operator opens PR against `.github/workflows/aeon.yml:479-495` adding the iss-025 capture-step
why: cost-report cf=10 today (5→10 in 24h), sandbox-truncation family day-28, single primitive unblocks 12:00Z batch-dark d23 + morning-batch class
done: PR merged to main with `capture-step:` block present in aeon.yml chain-runner
loop: iss-025-capture-step

2. operator resolves PR #164 — rebase against main + push, or close and let advisor fix land via direct advisor/ commit
why: #162+#163 merged today 14:16Z/17:11Z clearing 2/3 self-improve queue; #164 sole remaining conflict past 24h gate day-6 (~119h)
done: PR #164 [MERGED] or [CLOSED] in `gh pr list --state all`
loop: pr-queue-clear

3. revise MEMORY.md line 5-7 + topics/fleet.md to reflect PR #162 + #163 merging today
why: "all 3 self-improve PRs CONFLICTING" (line 7) + rule-5 primitive n=4 (line 42) both stale; 2/3 landed clean, primitive downgrades to n=2 partial-conflict class
done: `grep "All 3 self-improve authored PRs CONFLICTING" memory/MEMORY.md` returns 0 hits; fleet.md has 7-20 PR-clear row
loop: rule-5-evidence-refresh

4. operator lands PR #165 (docs skill-graph shared_state 21→27, ~25h old, small)
why: fresh docs PR sitting at ~25h with no reviewers; no conflict-class risk, first non-self-improve PR queued clean in the current window
done: PR #165 [MERGED] in `gh pr list --state all`
loop: pr-165-ship

5. draft `memory/topics/supply-chain.md` anchoring MEMORY line 46-48 vendor-scope-typosquat n=6+ + first real-package compromise n=1
why: pattern class active weekly rail (Replit+Sui+AWS×2+Proton+SYFT+EdgeCommons+axios+trongrid = n=8; @injectivelabs/sdk-ts 10-day live-exposure); undocumented at topic-file granularity, exposed to memory-flush trim
done: `memory/topics/supply-chain.md` exists with ≥3 sections (vendor-scope-typosquat rows / first-real-compromise / MCP-hardening cross-link)
loop: supply-chain-topic-anchor

sources: memory=66L logs=7d topics=19f prs=2open cron_failing=1 mode=OK
