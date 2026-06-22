*5 Actions — 2026-06-21*
Shape: root-cause iss-024, diagnose iss-022 cluster, unstick token-alert, merge #129, seed defi watches

1. root-cause `iss-024` skill-health 26-consecutive-fail loop in `memory/issues/ISS-024.md`.
why: head of today's skill-evals action queue — canary skill blind = whole fleet observability degraded.
done: `root_cause:` field populated, status flipped open → investigating.
loop: iss-024-investigate

2. diagnose `iss-022` sandbox-truncation cluster — 8 skills hit output_tokens=0 between 12:14z and 14:17z today.
why: extends iss-019/020/021; chronic-failure tail jumped 11 → 24 skills, all on this driver.
done: iss-022 lists the 8 affected skills + first-suspected-cause line; status set to investigating.
loop: iss-022-diagnose

3. cancel hung `token-alert` dispatch and re-fire — last_dispatch 13:45z, status=dispatched, 96min elapsed, cf=2.
why: first time token-alert hung mid-dispatch; reppo/gitlawb/well/mamo alerts paused while it sits.
done: stuck gh workflow run cancelled, fresh dispatch fired, cron-state last_status=success.
loop: token-alert-unstick

4. merge PR #129 (`skill-graph/2026-06-21`) — doc-only, retired_skills -4, shared_state_edges 195→9.
why: auto-generated, ~6h old, nothing gated on it; clears the open-PR slot for tomorrow.
done: #129 squashed to main, branch deleted.
loop: pr-129-merge

5. add a `type: pool` or `type: position` entry to `memory/on-chain-watches.yml` (morpho/aave/curve).
why: defi-monitor 14d no_config; wallets seeded but pool/position list is empty.
done: ≥1 `type: pool` or `type: position` watch in watches.yml; next defi-monitor run logs ≥1 position.
loop: defi-monitor-config

sources: memory=42 lines logs=7 days topics=11 files prs=1 open cron_failing=1 mode=OK
