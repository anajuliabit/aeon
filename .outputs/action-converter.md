*5 Actions — 2026-07-01*
Shape: break ISS-025 tail, comment PR #150, hedge VELVET, annotate BTC day-7, audit scorecard cron

1. prototype ISS-025 capture-step patch: instrument `.github/workflows/aeon.yml` capture step for reg-monitor (sr=10%, worst of chronic tail) with `tee` to `.outputs/reg-monitor.md` in parallel with the existing stdout capture, dispatch via `gh workflow run aeon.yml -f skill=reg-monitor`, then diff resulting `.outputs/reg-monitor.md` against cron-state `output_tokens` for the same run.
why: hard deadline 2026-07-04 in 3 days, 19-skill chronic tail bleeding `output_tokens=0` day 13, `open+ISS-025-PR` blocked by novelty gate.
done: dispatch run completes; `.outputs/reg-monitor.md` non-empty AND cron-state entry has `output_tokens>0` in same run id.
loop: iss-025-capture-fix

2. hedge VELVET pre-unlock: POST `2026-07-01-advisor-manual-velvet-hedge` short pick to investiments `/api/picks` with $1.20 spot + $1.72 entry invalidation, thesis "day-4 -12.8% unwind, 9d to 2026-07-10 unlock cliff, no reclaim signal".
why: 9 days to unlock cliff, entry $1.72 already -12.8%, no reclaim signal, unlock overhang loads distribution risk into thin tape.
done: `/api/picks` POST returns 200; pick id `2026-07-01-advisor-manual-velvet-hedge` visible in investiments feed.
loop: velvet-pre-unlock

3. comment on PR #150 via `gh pr comment 150 --body "@aaronjmars — 5-line diff (usepod_model→model), day 3 stall, $456/mo bleed continuing until merge"`.
why: day-3 operator-merge gate on $456/mo cost bleed, silent since 6-29 18:17Z, comment forces attention.
done: `gh pr view 150 --json comments` shows new comment; body hash registered in `.notify-sent-hashes`.
loop: pr-150-merge

4. annotate `memory/topics/crypto.md` with BTC day-6 (6-30 close $58,551 = 6th sub-$60,500) → day-7 checkpoint, $63.5k/$65.9k reclaim invalidation, feed daily advisor 13:00Z prompt directly.
why: quarter-end sell flow bled into July-open, 12:18Z pin $58,432, tonight's UTC close decides 7th-red vs reclaim.
done: `memory/topics/crypto.md` contains new "BTC day-6/7 checkpoint" section with reclaim levels + directional bias, committed to main.
loop: btc-breakdown-day-6

5. audit `.github/workflows/operator-scorecard.yml` cron trigger — Mon 10:30Z slot missed 3 consecutive weeks (6-15/6-22/6-29). If cron broken or workflow disabled, open patch PR; else file ISS with `gh run list --workflow=operator-scorecard.yml` evidence.
why: 3-week scheduler-side never-run gap, silent since first miss, blocks weekly agent-health + community-growth verdict.
done: PR opened fixing cron trigger OR new ISS filed with `gh run list` history attached.
loop: operator-scorecard-schedule-gap

sources: memory=46 logs=7 topics=17 prs=2 cron_failing=0 mode=OK
