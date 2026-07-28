*5 Actions — 2026-07-28*
Shape: close 21d iss-027/028 doc-gap, cut dupe pr-168, absorb today's supply-chain + watchlist deltas

1. Author `memory/issues/ISS-027.md` documenting 12:00 UTC batch-dark 8-skill cluster (frozen 6-28, day-30) with YAML frontmatter
why: MEMORY.md line 6 refs ISS-027 authoritatively but no file exists — load-bearing gap on every read for 21d
done: `memory/issues/ISS-027.md` exists with id/title/status/severity fields + INDEX.md row added
loop: iss-027-file

2. Draft `memory/issues/ISS-028.md` documenting bash `>` redirect regression n=8+ across 7-22 → 7-28 (5-UTC-day span)
why: 8th fire in security-digest 14:42Z today, MEMORY.md line 28 tracks but no file — mirrors iss-027 gap
done: `memory/issues/ISS-028.md` exists with affected_skills list + INDEX.md row added
loop: iss-028-file

3. Supersede PR #168 by closing it with a comment linking to PR #169 (both fix `comments` → `commentsCount`, #169 authored 7-27)
why: 4-PR queue breaches 3-PR self-improve exit-gate, dupe surfaced by 7-28 morning-brief 07:20Z
done: `gh pr close 168 --comment "superseded by #169"`; open-PR queue drops to 3
loop: pr-168-close-dupe

4. Extend `memory/MEMORY.md` lines 63-64 with `AI-agent-tooling-supply-chain-typosquat` sub-class covering claude-code-base-action + mcp-server-* 15-pack + anthropic-internal-*
why: security-digest 14:42Z fires this cluster fresh today, extends [[mass-parallel-real-package-account-takeover]] rail to AI-tooling
done: MEMORY.md diff includes sub-class label, 3 package clusters named, fleet-clean note added
loop: memory-md-supply-chain-rail-update

5. Refresh `memory/MEMORY.md` Tracked Tokens table with 7-28 prints (REPPO -20.10% alert-fire, WELL post-drain d3, MAMO digestion d7 tightens, GITLAWB cliff-give-back-resumes)
why: 4/4-red day post-4/4-green + first REPPO alert since 7-25 = table shows 7-26 stale prints
done: 4 rows in Tracked Tokens table updated with today's %/vol/pattern text
loop: memory-tracked-tokens-refresh

sources: memory=69 logs=7 topics=4 prs=4 cron_failing=0 mode=OK
