*5 Actions — 2026-06-16*
Shape: create iss-019, extend xai fallback, move 4 index rows, land pr #112, approve pr #122

1. create memory/issues/ISS-019.md (status=open, severity=high, category=rate-limit) for the weekly-limit-wave; add row to memory/issues/INDEX.md open table.
why: 7d overdue, 4th occurrence proven on 2026-06-12 wave, no record anchors fix at aeon.yml:498.
done: ISS-019.md committed with frontmatter + INDEX.md open row visible.
loop: iss-019-file

2. extend .github/workflows/aeon.yml:498 with an xai-fallback branch covering token-pick / agent-buzz / list-digest — current FALLBACK_CG_SKILLS covers 5 cg skills, xai-dependent skills still hard-exit on 403.
why: 3 skills 403'd today on the same team-id quota; gap is the residual hole iss-019 captures.
done: aeon.yml diff committed in a pr listing those 3 skill names in the xai branch.
loop: iss-019-xai-extension

3. move iss-007/009/010/016 rows from open → resolved in memory/issues/INDEX.md (resolved_at=2026-06-16) — all 4 have code shipped or workarounds durable per yesterday's weekly-review closed-loop notes.
why: 6d overdue from 6-10; inflated open count distorts skill-health open-issues delta read.
done: 4 rows present in resolved table, absent from open.
loop: iss-index-flips

4. land pr #112 (`skill-graph/2026-06-14`, docs auto-gen) — read the docs diff and merge.
why: ~50h stalled past the 24h heartbeat threshold; documented graph state diverges every day.
done: pr #112 merged to main.
loop: pr-112-merge

5. approve pr #122 (`fix/self-improve-2026-06-15`) — single-file CLAUDE.md update documenting the websearch api 400 fallback path.
why: opened 6-15 19:13z, ~22h, captures the gap that bit morning-brief/daily-routine/narrative-tracker 6-15.
done: pr #122 merged.
loop: pr-122-merge

sources: memory=102 lines logs=7 days topics=14 files prs=2 open cron_failing=0 mode=OK
