*5 Actions — 2026-08-15*
Shape: author iss-032, push usepod-402, nudge pr-174 7d-stall, file iss-033 chain-drift, add spec-kit

1. author memory/issues/ISS-032.md + append INDEX.md row for fork-cohort stuck-in-flight
why: 10th+ owed cycle at ~145h since 8-09 19:05Z dispatch, operator manual-file only path per morning-brief 07:26Z
done: memory/issues/ISS-032.md exists + INDEX.md row appended
loop: iss-032-fork-cohort-stuck

2. push scripts/detect-usepod-402.sh runtime gate to close ISS-031
why: 8-13 gate deadline +2d overdue, morning-brief 07:03Z file-check confirms script still absent
done: scripts/detect-usepod-402.sh exists + executable + wired from workflow
loop: iss-031-usepod-detect-gate

3. nudge PR #174 (Advisor Brier-weight) via `gh pr comment 174` on CI-cold status
why: opened 8-08 00:31Z = 7d 17h now, first crossing of CLAUDE.md ~7d escalation rule, webbrain-one contributor blocked on CI
done: gh pr comment on #174 posted with concrete unblock question
loop: pr-174-crosses-7d-stall

4. file memory/issues/ISS-033.md documenting chain-output-header-date-drift as 4-consec formal pattern
why: rail-promoted 8-14 n=3, extends 4-consec-day 8-15 per daily-routine 10:15Z (4 chain sub-outputs 8d stale)
done: memory/issues/ISS-033.md exists + INDEX.md row + category=quality-regression
loop: chain-output-header-date-drift-4-consec

5. add `- github/spec-kit` to memory/watched-repos.md
why: 8-15 github-trending top-pick (128k GitHub-official spec-driven-dev toolkit, release-moment 3.2× baseline), direct overlap with Aeon spec/skill-first architecture
done: memory/watched-repos.md line added
loop: watched-repos-add-spec-kit

sources: memory=77L logs=15d topics=20 prs=5 cron_failing=3 mode=OK
