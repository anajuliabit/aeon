*5 Actions — 2026-08-04*
Shape: open ISS-030 P0, verify PR#173 ci, debug cost-report SDK, close ISS-029, log deepseek n=2

1. Open memory/issues/ISS-030.md for cost-report `sdk_opt_in_required` signature (severity=critical, category=config); add row to INDEX.md.
why: fleet-worst chronic sr=0.10 (7/73) consec=15, distinct non-usepod/non-sandbox signature isolated 8-04 12:15Z, no ISS-file yet.
done: ISS-030.md exists with YAML frontmatter + INDEX.md Open table gains row.
loop: iss-030-cost-report-sdk-opt-in

2. Run `gh pr checks 173` and `gh pr view 173 --json mergeable`; if ci-skills-json green, annotate #173 body ready for 8-09 Sunday-batch merge.
why: PR #173 targets shared ci-skills-json root cause on #171+#172 — merging unblocks 3-PR queue via one lift.
done: `gh pr checks 173` output logged; if passing, ready-for-batch comment added.
loop: verify-pr-173-ci-status

3. Grep for cost-report skill invocation in .github/workflows/ + skills/cost-report/SKILL.md; wire Claude Code SDK opt-in flag/env to clear `fast_mode_disabled_reason: sdk_opt_in_required`.
why: identifies root fix for fleet-worst chronic-failure — 8-04 12:15Z fresh signature exposed the config gap distinct from ISS-025 truncation shape.
done: aeon.yml or cost-report SKILL.md diff written, or PR opened with the config change.
loop: debug-cost-report-sdk-config

4. Move ISS-029 from Open to Resolved in memory/issues/INDEX.md; set resolved_at=2026-08-04 in ISS-029.md, fix_pr="operator usepod payment restored".
why: 20-of-20 dispatches post-8-03 20:14Z clean through 8-04 12:17Z btc-levels — recovery confirmed durable.
done: INDEX.md row moved to Resolved table + ISS-029.md frontmatter updated.
loop: close-iss-029-recovery

5. Append `[[deepseek-primitive-cluster]] rail candidate n=2 8-04` to memory/MEMORY.md recurring-patterns — antirez/ds4 (Redis creator DeepSeek local inference C) + esengine/DeepSeek-Reasonix (DeepSeek-native coding agent Go).
why: first same-slate 2-DeepSeek-primitive appearance in memory-window github-trending 8-04 10:14Z; watch for n=3 tomorrow.
done: MEMORY.md gains one line under recurring-patterns block.
loop: promote-deepseek-cluster-rail

sources: memory=82 logs=8 topics=20 prs=4 cron_failing=1 mode=OK
