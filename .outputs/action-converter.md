*5 Actions — 2026-05-24*
Shape: Ship PR #9, open ISS-005 PR, bundle operator unblocks, draft soul, triage datanets.

1. Squash-merge PR #9 via `gh pr merge 9 --squash --delete-branch`, then add a `## Tracked Tokens` table to memory/MEMORY.md with REPPO/HYPER/VVV rows plus Price Floor / Price Ceiling columns.
why: PR #9 is 24h+ stale; merging closes the silently-skipped token-alert rules already flagged in today's 12:00 log.
done: PR #9 closed and `## Tracked Tokens` table exists in MEMORY.md with three rows and Floor/Ceiling columns.
loop: pr-9-token-alert

2. Open a PR closing ISS-005 — patch scripts/prefetch-reppo.sh to record per-pod validityEpoch + currentEpoch, then patch skills/reppo-trading-agent/SKILL.md to drop pods where validityEpoch != currentEpoch before voting.
why: ISS-005 is the only on-chain blocker not needing operator action — every vote dry-run today reverted POD_NOT_VALID_FOR_EPOCH.
done: PR opened touching both files; description references ISS-005; reppo-digest dry-run on the branch shows 0 vote reverts.
loop: iss-005-epoch-filter

3. Bundle ISS-004 + ISS-006 operator unblocks: write exact `reppo grant-access --subnet <id from configs/datanets/tradinggymai.md>` and `reppo lock <amount> --duration <secs>` into memory/issues/ISS-004.md and ISS-006.md "Operator action" sections, then send one combined ./notify with both commands.
why: Both issues are operator-only and both block reppo-trading-agent today — one ping beats two.
done: both ISS files have an "Operator action" section with a copy-pasteable CLI; one combined ./notify sent.
loop: iss-004-grant + iss-006-lock

4. Draft soul/SOUL.draft.md from 14 days of logs (Telegram exchanges, write-tweet runs, the "Yes redo" correction on the Base summer thread) — fill all 5 sections (Identity, Worldview, Interests, Background, Boundaries) with at least 3 lines each, as `.draft.md` so operator approves before promoting.
why: 5+ content skills run neutral voice daily; a draft seeds operator review and could ship voice this week.
done: soul/SOUL.draft.md exists with all 5 sections populated (>=3 lines each).
loop: soul-empty

5. Triage 14 unassigned reppo datanets into memory/topics/reppo.md — read configs/datanets/*.md, append `## Datanet triage 2026-05-24` section with top-3 highest-leverage datanets, each with a one-line scope and a proposed agent skill name.
why: Orchestrator surfaces these every run, 7+ days untouched — triage gives the next agent a real queue.
done: memory/topics/reppo.md has the new section with 3 named datanets + 3 proposed agent skill names.
loop: unassigned-datanets

sources: memory=47 logs=4 topics=4 prs=1 cron_failing=0 mode=OK
