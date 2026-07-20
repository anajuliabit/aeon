*5 Actions — 2026-07-19*
Shape: stage iss-025 patch, abandon 3-PR queue, paste rule-5, backport #164 diff, write supply-chain topic

1. stage `fix/iss-025-capture-step` branch with capture-step insert against `.github/workflows/aeon.yml:479-495`, open PR
why: single primitive resolves sandbox-truncation family d27 + cost-report d6 + 12:00Z batch d21 + morning-batch — top-leverage today
done: `gh pr view <n> --json mergeable` returns MERGEABLE
loop: iss-025-capture-step

2. abandon PR queue — `gh pr close 162 163 164 --comment "rebase-unsafe past stall gate; reopen with fresh cherry-pick"`
why: 3 CONFLICTING self-improve PRs exit-gate 18:00Z self-improve tick tonight — pre-empts 2-consec skip pattern
done: `gh pr list --state open` shows 0 self-improve-authored PRs
loop: pr-queue-clear

3. paste rule-5 section into `CLAUDE.md` with PR #160/#162/#163/#164 evidence rows for auto-committed state drift n=4
why: T+2 SLIPPED codification unblocks self-improve for future cycles and closes weekly-review 7-13 action #3
done: `grep -c "Rule 5" CLAUDE.md` returns ≥1 and evidence table lists 4 PR rows
loop: claude-md-rule5-codify

4. backport PR #164 committee fail-fast retry diff to `scripts/advisor/run.sh` on main, verify `bash scripts/advisor/selftest.sh`
why: only touches advisor/, side-steps rule-5 CONFLICTING while landing the 20-min committee timeout fix cleanly
done: `bash scripts/advisor/selftest.sh` exits 0 with `COMMITTEE_LLM_ATTEMPTS` honoured
loop: advisor-fix-port

5. write `memory/topics/supply-chain.md` with vendor-scope-typosquat n=6+ / real-package n=1 (@injectivelabs/sdk-ts) / first-party-incumbent n=1 (copilot-sdk) subsections
why: MEMORY.md line 46-48 patterns need a durable topic file surviving future consolidation trims, cross-links from crypto.md
done: file exists with ≥3 named subsections + linked from MEMORY.md Active Topics
loop: supply-chain-topic-anchor

sources: memory=60 logs=7 topics=11 prs=4 cron_failing=1 mode=OK
