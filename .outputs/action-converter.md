*5 Actions — 2026-07-29*
Shape: ship iss-025 handoff T-1, stub ISS-027/028 d23, triage PR#167 6d, refresh market-context pre-cascade

1. draft articles/iss-025-handoff.md summarizing cost-report 12% (7/58) + capture-step target (.github/workflows/aeon.yml:479-495), send via ./notify
why: weekly-review 7-27 action #1 due 2026-07-30 T-1; retires 4-consec-weekly slip; verb-pool exhausted per MEMORY line 5
done: file exists + ./notify exit 0 + hand-off flag in memory/logs/2026-07-30.md
loop: iss-025-hand-off-t-1

2. populate memory/issues/ISS-027.md with batch-dark 12:00Z 8-skill d31 signature (defi-overview/token-pick/token-movers/narrative-tracker/market-context-refresh/fleet-control/on-chain-monitor/defi-monitor), sibling to ISS-025 template
why: d23 doc-gap load-bearing per MEMORY line 7; 3-consec action-converter runs shaped this max-score (125); +3d past weekly-review 7-27 last-chance
done: memory/issues/ISS-027.md exists with YAML frontmatter + INDEX.md open table updated
loop: iss-027-file-doc-gap-d23

3. populate memory/issues/ISS-028.md capturing bash-`>` redirect regression n=10+ across 8-UTC-day span, workaround chain (Edit tool + curl -o + gh --jq stdout)
why: paired doc-gap with ISS-027; security-digest + reg-monitor + agent-buzz + list-digest all fired signature this UTC-day; d23 gap
done: memory/issues/ISS-028.md exists with YAML frontmatter + INDEX.md open table updated
loop: iss-028-file-doc-gap-d23

4. triage PR #167 with gh pr review comment on bash-redirect fix scope, decide rebase-vs-merge
why: 6d stalled since 7-23; direct root-cause fix that would eliminate the ISS-028 workaround chain firing every skill run
done: gh pr review --comment posted or gh pr merge --squash executed
loop: pr-167-decide-6d

5. refresh memory/topics/market-context.md with 7-29 tape snapshot (BTC $63.8k range, breadth 40/82 restore from 7-28's 8/82 flip, REPPO d2 post-capitulation)
why: skill-freshness 7-28 flagged 12d/296h WARN→STALE cascade ~16:00Z 2026-07-30 T-1; skill sits at 32% SR so manual save prevents auto-cascade
done: file mtime updated + baseline section reflects 7-29 top-100 breadth + tracked-token deltas
loop: market-context-stale-t-1

sources: memory=72 logs=7 topics=20 prs=2 cron_failing=10 mode=OK
