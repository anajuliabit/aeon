*5 Actions — 2026-08-09*
Shape: prep ISS-030 T-1, review #176, seed shiplog, kick #174 CI, wire LIT

1. precheck ISS-030 cost-report against 8-10 07Z deciding-test — grep `skills/cost-report/SKILL.md` for `sdk_opt_in_required` handling and append verdict block to `memory/issues/ISS-030.md`.
why: fleet-worst chronic sr=10%, T-1 today, no operator lever tomorrow if not primed tonight.
done: `memory/issues/ISS-030.md` has fresh precheck block (clean-signature-since-8-04-organic OR fix-scope-draft).
loop: precheck-iss-030-t-1

2. review PR #176 skill-graph regen (EDGES 32→74) — diff-check node/edge deltas against `memory/topics/skill-graph-state.json` and post merge-ready|blocking verdict as PR comment.
why: opened 17:10Z today, sunday-batch T-0, one-lift-if-clean before operator window closes.
done: `gh pr comment 176` posted with verdict; verdict logged in `memory/logs/2026-08-09.md`.
loop: review-pr-176-skill-graph

3. draft `articles/weekly-shiplog-2026-08-09.md` seed for 8-10 09Z Mon tick — catalog 7-27 → 8-09 shipped items from `memory/logs/` so tomorrow's fire has structure to extend.
why: 20d stale on 7d schedule (3× miss), Mon tick T-1, seed short-circuits cold-start.
done: article file exists with ≥5 dated shipped items and ≥3 rail-count deltas.
loop: draft-weekly-shiplog

4. rebase PR #174 (Advisor Brier-weight) onto main to trigger CI — 42h at UNKNOWN with empty statusCheckRollup; commit-hash change is stronger than any reopen event.
why: only stuck old-queue PR pre #176, weekly-batch needs a real CI verdict on 8-10.
done: `git push --force-with-lease` lands on `webbrain/issue-144`; `gh pr view 174 --json statusCheckRollup` returns non-empty.
loop: rebase-pr-174-advisor

5. wire LIT into MEMORY.md Tracked Tokens (5th row, 15% threshold) — 8-08 list-digest surfaced @Flowslikeosmo hard receipts (Robinhood Chain 1.8% Lighter perps vol, $11.14M on-chain deposits, 15.5M burned since 6-30, no unlocks until 12-29).
why: deferred from 8-08 action #4; opens token-alert coverage on a live receipt-backed thesis before the arc runs.
done: `memory/MEMORY.md` Tracked Tokens table has 5th row (LIT / lit-protocol / 15% / recent activity blurb).
loop: wire-lit-tracked-tokens

sources: memory=117 logs=7d topics=11 prs=2 cron_failing=0 mode=OK
