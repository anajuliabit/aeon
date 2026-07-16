*5 Actions — 2026-07-16*
Shape: operator ISS-025 T-0 PR, rebase #163/#164 before stall gates, close #162, re-scope rule-5

1. Operator: open a PR editing `.github/workflows/aeon.yml:479-495` to fix ISS-025 capture-step outputTokens truncation (deadline T-0 today).
why: unblocks cost-report STUCK d3 + 8-skill batch-dark d19 + sandbox-truncation family day-24; weekly-review 7-13 action #1 priority 20.
done: PR opened against main touching aeon.yml lines 479-495 with a chain-runner capture-step diff.
loop: iss-025-capture-step-t0

2. Rebase PR #163 `fix/self-improve-2026-07-13` onto main and land before the 18:09Z 72h stall gate.
why: CONFLICTING at ~68h and ~3h from 72h gate; doc-only skill-security-scan patch, rule-5 clean, ready to ship.
done: PR #163 merged into main, or explicit rebase commit pushed with mergeStateStatus flipping off DIRTY.
loop: pr-163-rebase

3. Add a "Skill authoring boundaries" section to CLAUDE.md codifying rule-5 across workflow + script class (T-1 tomorrow).
why: PR #164 CONFLICTING flip today extends rule-5 past workflow-file class to script-file class; codification must re-scope before 7-17.
done: commit lands section in CLAUDE.md naming PRs #160/#162/#163/#164 as the 4-tick evidence base.
loop: claude-md-rule5-rescope

4. Close PR #162 `fix/self-improve-2026-07-11` as superseded — CONFLICTING day-5, XAI fallback logic already advanced past its diff.
why: T+2 deadline-missed day-3 rollover; keeping it open masks the pipeline health signal and blocks the next self-improve cycle.
done: PR #162 closed with a comment naming the T+2 slip + supersession by later XAI fallback commits.
loop: pr-162-close

5. Rebase PR #164 `fix/self-improve-2026-07-15` onto main before the 19:31Z 24h stall gate.
why: CONFLICTING at ~19h20m from auto-committed state drift on `memory/token-usage.csv` + `.outputs/self-improve-*.json`; rule-5 script-class extension test.
done: PR #164 rebased and pushed before 19:31Z, or explicit close decision recorded in the PR thread.
loop: pr-164-rebase

sources: memory=54 logs=8 topics=8 prs=3 cron_failing=1 mode=OK
