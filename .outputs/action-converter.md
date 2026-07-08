*5 Actions — 2026-07-08*
Shape: audit scheduler, route ISS-025, codify batch + aixbt dead-slots, archive SLX day-14

1. audit `.github/workflows/aeon.yml` schedule blocks (grep `cron`/`schedule:`/`0 12`/`0 9`/`0 21`/`30 10`); write findings to `.tmp/aeon-yml-schedule-audit.md`, name common root cause across 12z-batch/aixbt/op-scorecard dead-slots
why: 3 scheduler-side never-runs (batch day-12, aixbt day-10, op-scorecard day-8) share dispatch-layer symptom — one audit unblocks all three
done: `.tmp/aeon-yml-schedule-audit.md` written with cron grep + shared-cause hypothesis + next PR shape
loop: 12z-batch-dispatch

2. update `memory/issues/ISS-025.md` — set `authored_by: operator` in frontmatter, append Resolution-Blocked section citing self-improve 2026-07-07T18:32Z rule-5 structural block on `.github/workflows/*` edits
why: weekly-review 7-13 is T-5; routing verdict lives in one log line, not the ISS file — persists the block signal for operator lift
done: `ISS-025.md` YAML has `authored_by: operator` field + section referencing self-improve run and rule-5 clause
loop: iss-025-routing-test

3. file `memory/issues/ISS-027.md` codifying 12:00Z batch-6 scheduler-side never-run pattern; add Open row to `INDEX.md`; category `config`, severity `high`, affected_skills = [token-pick, defi-overview, token-movers, on-chain-monitor, defi-monitor, market-context-refresh]
why: 7-07 action-converter claimed filing but no file on disk; 7-08 12:54Z token-alert catch-up confirmed 12-day dispatch void — carry-forward closes today
done: `ISS-027.md` frontmatter + INDEX Open row appended
loop: batch-dispatch

4. archive SLX open pick in `memory/topics/crypto.md` — append 2026-07-08 close entry: 6-24 entry $0.4753 → 7-05 last CG print $0.256 = -46% recut-overdue day-14, rank #372, mcap $62M, position past every trigger
why: 5th consecutive daily-routine surface with no action; weekly-review 7-06 operator-slot routing needs a close-on-record; removes ~40 char/day noise from daily-routine tail
done: crypto.md has SLX 2026-07-08 close section + no more open-pick language for SLX below that line
loop: slx-recut-blown

5. file `memory/issues/ISS-028.md` codifying aixbt-pulse 09/21Z dead-slot pattern (day-10 confirmed 7-08 09:04Z hb; last_success 2026-06-28T21:21Z ~236h stale = 9.8× twice-daily interval); add Open row to `INDEX.md`
why: distinct cron slot from ISS-027 (twice-daily vs 12:00Z single); separate ISS keeps diagnostic paths clean when scheduler-audit lands
done: `ISS-028.md` frontmatter + INDEX Open row appended
loop: aixbt-dead-slot

sources: memory=76 logs=14 topics=11 prs=0 cron_failing=0 mode=OK
