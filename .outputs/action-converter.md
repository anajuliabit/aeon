*5 Actions — 2026-08-01*
Shape: wire ISS-025 fix, annotate ISS-028 scope-narrowness, compact MEMORY, audit PR #171, distill memory-paper

1. Wire ISS-025 hand-off PR against `.github/workflows/aeon.yml:479-495` capture-step overwrite (emit fenced block in assistant text, not Write tool).
why: T+2 day-17 SLIPPED past 7-30 deadline; cost-report sr=0.12 (7/58) weakest chronic-failure durable, weekly-review 8-03 rolls d19.
done: branch pushed + `gh pr create` for aeon.yml capture-step fix.
loop: wire-iss-025-t-plus-2-d17

2. Annotate `memory/issues/ISS-028.md` with PR #167 fix-scope narrowness — heartbeat/security-digest surfaces resolved, daily-routine hn-digest + github-trending + list-digest + agent-buzz still block.
why: kill-test d2 NEGATIVE confirmed today at 3 call-sites; workaround-chain n=15+ across 11-UTC-day span 7-22→8-01.
done: ISS-028.md gets Post-fix-investigation section listing 4 unresolved call-sites + n=15 count.
loop: annotate-iss-028-scope-narrowness

3. Compact `memory/MEMORY.md` — dedupe duplicate "## Recently Cleared" header (lines 14 + 31), refresh Tracked Tokens Recent Activity for 8-01 12:00Z prints, fold 3 fresh rails ([[skill-pack-primitive-rail]] n=5→n=6 via reverse-skill, [[large-cap-single-day-flip]] NEW n=3 HOLO/PUMP/UNI, [[MCP-spec-maturity-vs-ecosystem-security]] n=2 Ruflo+Dynatrace).
why: two "Recently Cleared" sections is a hygiene bug; 3 rail deltas + 4 token prints drift-risk pre-reflect 18:00Z.
done: MEMORY.md single Recently Cleared block + Tracked Tokens table 8-01 data + 3 rail lines under Recurring patterns.
loop: compact-memory-md-hygiene

4. Audit `gh pr diff 171` (self-improve github-trending 12-17 candidate cap fix, 23h open) and post inline notes if the fix hardcodes vs derives the cap from 5-consec fetch pattern.
why: sub-25 fetch pattern crossed 5-consec durable rail 8-01 (7-28→8-01 range 12-17); operator batch-merge cadence 8-03 = 2d out.
done: `gh pr review 171` comment posted OR approval left with rationale in body.
loop: audit-pr-171-diff

5. Distill the Filesystem-Memory paper (arXiv 2607.26637, today's paper-pick) into `memory/topics/memory-architecture.md` as 5 bullets covering the MEMORY.md-index-plus-topics-plus-logs shape Aeon runs.
why: paper studies our exact architecture; two load-bearing findings (organized stores halve retrieval cost; organization erodes for all but strongest agent) map onto reflect skill drift.
done: new file `memory/topics/memory-architecture.md` with 5 bullets + arxiv citation.
loop: category:learn

sources: memory=82L logs=8d topics=~20 prs=2 cron_failing=10 mode=OK
