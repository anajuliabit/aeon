*5 Actions — 2026-07-06*
Shape: Author capture-step patch, close SLX -46%, diagnose cron gap, retire #149, flip MEMORY.md

1. Author the `aeon.yml:479-493` chain-runner capture-step patch and open a PR (emit fenced-block-in-assistant-text swap, ISS-025 root cause per PR #150/#156 downstream fixes).
why: entire 18-skill sr<0.5 chronic tail traces to this one Write-tool→CLI-result overwrite; day 12 of unshipped fix; 19:00Z weekly-review deadline just passed.
done: PR URL opened against main with diff at `aeon.yml:479-493` + closes ISS-025 in body.
loop: iss-025-capture-fix

2. Close the SLX pick in `memory/topics/crypto.md` picks table — mark CLOSED at $0.256 vs $0.4753 entry (-46%, day-12), stop the daily "recut overdue" resurface.
why: HIGH 9/10 6-24 entry past every recut trigger; intraday -29.6% capitulation + rank #372 = thesis broken, book the loss.
done: crypto.md picks table shows SLX row status=CLOSED with final drawdown line + exit price.
loop: slx-recut-blown

3. Diagnose the 07-06 fleet-wide morning-slot cron gap: probe GH Actions dispatch queue for the 07/08/09/12/13Z slots that produced 0 skill runs today.
why: only 3 dispatches so far today (unlock-monitor 11:00Z / btc-levels 01:28Z / hb 14:33Z catch-up); hb self-set 20:00Z re-eval tick is ~40min out.
done: root cause logged to `memory/topics/fleet.md` (queued-late vs holiday-cron catch-up vs sandbox skip) with `gh api /repos/.../actions/runs` evidence.
loop: fleet-morning-slot-gap-07-06

4. Retire PR #149 (docs skill-graph, day-8 stall, ~193h open) with a comment linking to PR #155 (day-0 fresh run from same skill, +68 skills · 4→5 depends_on · 9→21 shared_state).
why: two open PRs from same skill = reviewer confusion; #155 supersedes #149's payload; queue cleanup.
done: `gh pr close 149 --comment "superseded by #155"` executed.
loop: pr-149-supersede

5. Flip PR #154 (`fix(issues) close ISS-026`, merged 15:35Z) + PR #156 (`fix(aeon.yml) usepod_model cleanup`, merged 15:45Z) from `## Current Goals` to a `## Recently Cleared` block in `memory/MEMORY.md`.
why: 4h post-merge, downstream skills (goal-tracker/hb/action-converter) still read stale goal rows; the 12:00 UTC batch fix + ISS-026 INDEX bookkeeping are both durably resolved.
done: MEMORY.md diff moves 2 rows out of Current Goals with merge timestamps recorded.
loop: memory-md-consolidation

sources: memory=56L logs=7d topics=11 prs=2 cron_failing=0 mode=OK
