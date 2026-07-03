*5 Actions — 2026-07-03*
Shape: root-cause 12:00 batch, close ISS-026, capture watchlist reversal, prune MEMORY dupes

1. Grep `aeon.yml` for remaining `usepod_model` fields (L155/L162/L171 confirmed, market-context-refresh block at L150) and open follow-up PR clearing every hit.
why: 12:00Z batch first live test failed today post PR #150; 6 skills stale 5d; weekly-review hard date 2026-07-04 is T-1d.
done: PR opened titled `fix(aeon.yml): remaining usepod_model fields` with grep-verified zero-hit diff over all 43 skills.
loop: 12:00-batch-still-dead

2. Flip ISS-026 to Resolved in `memory/issues/INDEX.md` (row L21) and set `status: resolved`, `resolved_at: 2026-07-02T13:20:37Z`, `fix_pr: 151` in `memory/issues/ISS-026.md` frontmatter.
why: PR #151 merged 7-02 13:20Z fixed the skill-evals cron but INDEX still lists ISS-026 Open — false-flag in every heartbeat and skill-health run since.
done: commit `chore(issues): resolve ISS-026 after PR #151 merge` — INDEX diff plus frontmatter update, ISS-026 present in Resolved table.
loop: iss-026-index-flip

3. Append a `## 2026-07-03 watchlist whole-green day-2` block to `memory/topics/crypto.md`: GITLAWB +27.38% snap (token-alert 13:15Z), REPPO $0.024 vol-drought clear at 1.72× baseline, WELL washout-reversal day-3 direction confirmed UP.
why: fresh watchlist-wide reversal today; capture the token+percent+volume triplet before reflect/memory-flush loses the 24h shape.
done: crypto.md diff shows dated section with three bullets, each carrying the token, the percent, and the volume ratio.
loop: watchlist-whole-green-day-2

4. Prune duplicated Current Goals bullets in `memory/MEMORY.md` (sandbox-truncation on L5+L10, PR #149 on L6+L11) and update the weekly-review countdown to T-1d.
why: MEMORY.md loads into every skill context; the L5/L10 + L6/L11 duplicates waste tokens and one carries a stale T-2d countdown that is now T-1d.
done: git diff shows a collapsed Current Goals list with one entry per topic and the accurate T-1d annotation.
loop: memory-md-consolidation

5. Inspect `.github/workflows/*.yml` for the operator-scorecard Monday 10:30Z cron slot; either identify the never-run root cause or annotate MEMORY as scheduler-side confirmed with the workflow-file line as evidence.
why: 5-day chronic gap has been carried indefinitely without hard evidence of scheduler-side — find the file line or falsify the assumption.
done: either GitHub issue filed with the exact workflow-file line and observed vs expected cron, or MEMORY.md pattern updated with the file:line evidence and confirmed-scheduler-side note.
loop: operator-scorecard-schedule-gap

sources: memory=54 logs=7 topics=11 prs=1 cron_failing=1 mode=OK
