*5 Actions — 2026-08-12*
Shape: file iss-032, ship usepod-402 gate, audit workflow race, open reg-monitor fix, nudge #174

1. file `memory/issues/ISS-032.md` for fork-cohort state-update-race — run 31330721650 cancelled 8-09 19:35:47Z, cron-state marker never cleared, ~93h stuck since 8-09 19:05Z dispatch
why: 45h past 48h escalation threshold, action-converter proposed 8-11 18:40Z but never filed; blocks fork-cohort restart
done: `memory/issues/ISS-032.md` exists + `INDEX.md` Open table row added with severity=high category=config
loop: fork-cohort-stuck-93h

2. ship `scripts/detect-usepod-402.sh` operator-page gate for ISS-031 signature — 8-13 deadline is tomorrow, only 1 workday left
why: 2nd 7d-recurrence of ISS-029 shape crosses signature threshold; stopgap fix per weekly-review 8-10 owned action
done: script exists + executable + calls `./notify` on 402 signature detection + wired into `.github/workflows/chain-runner.yml` postprocess path
loop: iss-031-detect-usepod-gate

3. audit `.github/workflows/aeon.yml` commit-results + update-cron-state steps for Run-step cancellation-handling — root cause of ISS-032
why: fix at workflow-layer prevents next fork-cohort stall recurrence next Mon 8-17 dispatch; investigation-heavy but concrete
done: log block in `memory/logs/2026-08-12.md` naming exact line ranges in aeon.yml + verdict on whether steps clear dispatched marker on cancellation + proposed patch shape
loop: fork-cohort-workflow-audit

4. open reg-monitor self-improve PR baking CFTC HTML-fallback into `skills/reg-monitor/SKILL.md` step 1C — 2-consec-observation 8-05 + 8-12 confirms endpoint 404 durable
why: today's fire needed runtime pivot to HTML path; PR removes the pivot from every future Wed-cycle fire
done: PR opened via `gh pr create` on branch `fix/reg-monitor-cftc-html-fallback` naming CFTC RSS endpoint + fallback URL + step 1C edit
loop: reg-monitor-cftc-rss-404-durable

5. nudge PR #174 (Advisor Brier-weight) CI kick via close-reopen or empty-commit push — 4d+ CI-cold, mergeable=UNKNOWN, empty statusCheckRollup, weekly-batch T-4 to 8-16
why: external webbrain-one contributor blocked by unfiring CI; queue-full self-improve exit-gate stays disengaged until this clears
done: `gh pr view 174 --json statusCheckRollup` returns non-empty array
loop: pr-174-ci-cold-4d

sources: memory=95 logs=13 topics=20 prs=4 cron_failing=3 mode=OK
