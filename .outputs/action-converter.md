*5 Actions — 2026-08-05*
Shape: trigger PR#173 CI, draft cost-report fix, unblock #165, probe 08Z-slot-dark, codify CFTC fallback

1. push empty commit to `fix/self-improve-2026-08-03` branch to trigger ci-skills-json on PR #173
why: 40h dark with mergeable=UNKNOWN + empty statusCheckRollup; one CI pass unblocks 3-PR queue at 8-10 Sunday-batch T-5
done: `gh pr view 173 --json statusCheckRollup` returns non-empty check array
loop: push-commit-PR-173

2. draft PR removing `model: claude-sonnet-4-6` override on cost-report at aeon.yml:276 so it inherits opus-4-7 default
why: fleet-worst chronic sr=10% via ISS-030 `sdk_opt_in_required` signature; 8-10 Mon weekly-tick is the deciding-test
done: PR opened targeting `aeon.yml` line 276 with skill-health ISS-030 reference in body
loop: draft-cost-report-model-drop

3. resolve PR #165 rebase conflicts against origin/main (docs skill-graph shared_state 21→27) before 8-09 Sunday-batch
why: d17 CONFLICTING sole past-gate survivor + T-4 to weekly-batch merge window; docs skill-graph refresh gates fleet-map correctness
done: `gh pr view 165 --json mergeable` returns MERGEABLE
loop: resolve-PR-165-conflicts

4. probe scheduler for `[[morning-08Z-slot-dark]]` — grep `.github/workflows/` for `"0 8"` cron entries and confirm heartbeat + skill-freshness fire paths not muted
why: 2-consec 08Z co-miss (8-04 + 8-05) heartbeat + skill-freshness; 8-06 miss promotes to formal-pattern
done: written verdict in `memory/topics/fleet.md` (scheduler-bug vs. workflow-file bug vs. GH-Actions cadence-drift)
loop: probe-08Z-slot-dark

5. codify HTML fallback for CFTC RSS 404 in `skills/reg-monitor/SKILL.md` step 1C (add `https://www.cftc.gov/PressRoom/PressReleases` as documented fallback path)
why: reg-monitor Wed 8-05 hit CFTC RSS 404, HTML fallback worked; codify before 8-12 Wed re-fire; SKILL currently only lists RSS URL
done: PR opened modifying `skills/reg-monitor/SKILL.md` step 1C with fallback URL + skills.json regen
loop: codify-CFTC-RSS-fallback

sources: memory=83L logs=10d topics=~20 prs=4 cron_failing=1 mode=OK
