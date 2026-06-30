*5 Actions — 2026-06-30*
Shape: Ship PR #150 + #149, draft ISS-025 capture PR, close VELVET pre-unlock

1. merge PR #150 fix(aeon.yml) `usepod_model` → `model` — 5-line diff, ~$456/mo savings.
why: opened 6-29 18:16Z (~20h, approaching 24h stall), cost-report 6-29 flagged 5 skills on Opus by typo
done: PR #150 merged into main
loop: pr-150-merge

2. draft the ISS-025 capture-step PR against `.github/workflows/aeon.yml` env-var redirect for the `output_tokens=0` cluster.
why: day 7 unshipped, weekly-review hard deadline 2026-07-04 (4d), 19-skill chronic tail bleeds every tick
done: branch pushed + PR opened with capture diff
loop: iss-025-capture-fix

3. merge PR #149 docs(skill-graph) NEW_SKILLS +68 SHARED_STATE 9→36.
why: anajuliabit's own PR, day 2 past 24h stall threshold (~45h+), self-merge with no review-block
done: PR #149 merged
loop: pr-149-stall

4. decide model tier (Sonnet vs Haiku) for the 3 remaining `usepod_model` entries — market-context-refresh / narrative-tracker / aixbt-pulse — append rationale to `topics/fleet.md`.
why: PR #150 covers 5 of 8 entries, the other 3 still drift on the next cost-report cycle
done: 3 named decisions written + commit on main
loop: usepod_model-remainders

5. close VELVET pick or set $1.40 stop — entry $1.72, current $1.50 (−12.8%), 10d to July-10 unlock cliff.
why: HIGH 11/10 pick day-3 unwound on quarter-end tape, unlock cliff makes hold-thru-bounce asymmetric
done: stop set in trade log OR pick marked CLOSED in `topics/crypto.md`
loop: velvet-pre-unlock

sources: memory=43 logs=8 topics=17 prs=2 cron_failing=0 mode=OK
