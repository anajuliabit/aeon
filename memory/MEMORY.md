# Long-term Memory
*Last consolidated: 2026-05-28*

## About This Repo
Aeon — autonomous agent running on GitHub Actions via Claude Code. ~21
enabled skills on cron; inbound messaging via Telegram (live). Fleet exited
bootstrap 2026-05-21. soul/ populated 2026-05-25 (ana voice). Reppo-swarm
chain first on-chain output landed 2026-05-26. 2026-05-28 was the most
productive shipping day to date: 10 PRs merged (#30-#39) and the 4th mint
ever landed on the 6th chain run after rubric correction (PR #37).

## Current Goals
- Durable fix for ISS-009 — chain-runner.yml `fail-fast` branch uses bash
  `continue` (skips to next loop iter) instead of `break`; PR #27's workflow
  grep guard merged but did not abort downstream dispatch when fenced
  reppo-plan block was missing 2026-05-27. Third occurrence today.
- Assign agents to the 14 unassigned reppo datanets (1, 2, 4, 5, 6, 7, 8, 10,
  11, 13, 14, 15, 16, 17 — surfaced every reppo-orchestrator run for 7 days,
  untouched). *[goal-tracker 2026-05-28: BLOCKED — gated on PR #30, which
  merged 2026-05-28T12:05Z; blocker now lifted, next step is staged
  assignment.]*
- Close ISS-009 fully — root cause traced 2026-05-28 (chain-runner
  `aeon.yml:479-493` capture step `cp`s CLI `.result` over Write-tool output;
  fix path: emit fenced reppo-plan block in final assistant text). Codify
  the assistant-text contract in `skills/reppo-orchestrator/SKILL.md` AND
  switch chain-runner's fail-fast `continue` → `break` as defence-in-depth.
- Durable ISS-005 fix — move validityEpoch ≤ current-1 filter into
  `scripts/prefetch-reppo.sh`. Also add CLI idempotency on vote: pods
  372/373 got DISLIKE'd 7× each on 2026-05-28 (1 per run, no CLI dedup).
- Assign agents to the 14 unassigned reppo datanets (1, 2, 4, 5, 6, 7, 8, 10,
  11, 13, 14, 15, 16, 17 — 8th day surfaced).
- INDEX bookkeeping — close ISS-007 (PR #13/#26 merged), close ISS-010
  (PR #32 merged).

## Completed Goals
- Land PR #30 — completed 2026-05-28 (merged 12:05Z). Rewrote
  reppo-trading-agent to construct pods from HL public data (Hyperliquid
  leaderboard fills + IPFS pin + platform POST). Follow-on fixes #34
  (userFillsByTime so the window matches the 7d floor) and #37 (rank HL
  wallets by margin, drop 7d span floor, anti-regurgitation contract) also
  landed same day.
- Unblock reppo-swarm on-chain output — completed 2026-05-26. First mint
  (ETH Supertrend, tx 0x77f1…) + first vote (DISLIKE pod 373, tx 0x937d…)
  ever on-chain. 21st run (05-26 evening) shipped 3 on-chain (1 mint + 2
  votes, 0 failures — most productive run since chain launch).
  ISS-004 (PR #10/#19/#20), ISS-006 (PR #11/#23), ISS-008 (PR #21) all resolved.
- Populate `soul/` — completed 2026-05-25 (PR #12: SOUL.md 74L + STYLE.md 96L).
- Align tradinggymai rubric with operator-shared contributor spec —
  completed 2026-05-26 (PR #28). Spec preserved at [[tradinggymai-spec]].
- Land PR #30 — reppo-trading-agent rewrites pods from HL public data
  (merged 2026-05-28 12:05Z; follow-ups PR #34 `userFillsByTime` window,
  PR #37 rank-by-margin + drop span floor — together unlocked the 4th
  mint ever on 6th run, hash 397ee2e8e5e7e593, wallet 0x2b3349ff…33f7,
  110 closed trades, sharpe 110.3, win 0.7636).
- Unblock reppo-swarm on-chain output (2026-05-26). First mint
  (ETH Supertrend, tx 0x77f1…) + first vote (DISLIKE pod 373, tx 0x937d…).
- Populate `soul/` — 2026-05-25 (PR #12).
- Align tradinggymai rubric — 2026-05-26 (PR #28).
- Phantom-skill dispatch — 2026-05-28 (PR #32 closes ISS-010).
- skill-evals output_pattern realignment — 2026-05-28 (PR #31).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, recurring blockers, skill health.
- [Crypto research](topics/crypto.md) — defi-overview, narratives, token signals.
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit trail.
- [Market context](topics/market-context.md) — refreshed by market-context-refresh.
- [TradingGymAI (datanet 9) contributor spec](topics/tradinggymai-spec.md) — operator-shared 2026-05-26.
- [Bitcoin 30-day snapshot](topics/last30-bitcoin.md) — last30 baseline (stale, 05-21).

## Open Issues
- ISS-005 (high, prompt-bug) — vote pods fail POD_NOT_VALID_FOR_EPOCH; agent-side
  workaround live (filter validityEpoch ≤ current-1); durable prefetch fix +
  CLI vote-dedup both pending. Pods 372/373 7× DISLIKE'd each today.
- ISS-007 (medium, timeout) — Base RPC INTERNAL_ERROR; PR #13/#26 shipped.
  INDEX still shows open — bookkeeping queued.
- ISS-009 (high, prompt-bug) — root cause traced 2026-05-28 (chain-runner
  capture step overwrites Write-tool output with CLI `.result`). Fix path
  validated runs 2/3/4 today. Two follow-ups to fully close: codify
  emit-in-assistant-text in orchestrator SKILL.md, and switch chain-runner
  fail-fast `continue` → `break`.
- ISS-010 (medium, config) — fix shipped in PR #32 (merged 12:09Z). INDEX
  still shows open — bookkeeping queued.

## Open PRs
- 0 (PRs #30-#39 all merged 2026-05-28).

## Lessons Learned
- Reppo on-chain blockers cascade: ISS-002 → ISS-003 → ISS-004/005 → ISS-006
  → ISS-007 → ISS-008 → ISS-009. Took 6 days to fully unblock the cascade.
  Each fix exposed the next.
- Workflow-level guards only work if they actually abort the chain — bash
  `continue` in chain-runner's fail-fast branch silently skips to the next
  loop iteration. Use `break` or `exit`.
- Chain-runner's capture step (`aeon.yml:479-493`) silently overwrites
  Write-tool output with the CLI's final assistant `.result`. So skills that
  pass fenced blocks downstream must emit them in the assistant text, not
  via Write. (Diagnosed 2026-05-28 after 4 ISS-009 recurrences.)
- Cap surprises are on the *response*, not the *query window* — PR #30/#34
  widened HL's `userFillsByTime` window to 7d but the 2000-row response cap
  still collapsed every top-leaderboard wallet to <1 day span; only PR #37's
  wallet selection by margin (pnl/vlm) cleared the floor.
- Sandbox blocks `./notify "$(cat ...)"` arg-passing on command-substitution
  analyzer + `bash -c` wrapper. Stage to `.pending-notify/` and let post-run
  step deliver. Pattern now used by 12+ skills.
- Sandbox blocks Reddit (datacenter IP) and X.AI authed curl — use prefetch.
- Auto-recovery helpers (auto-approve, auto-grant, auto-lock) sometimes need
  retry-with-backoff because allowance/lock reads can be pre-confirmation stale.
- Reppo ledger rows are for on-chain-confirmed actions only — a queued intent
  is not a mint.
- Cost profile is cache-dominated (73% of spend is cache read+write). Standard
  "model-downgrade" filter misses Sonnet-rotation savings for high-cache
  skills (defi-overview, heartbeat, reppo-digest = 38% of weekly Opus spend).
  Operator-call territory.
- Memory consolidation: when a topic file grows, move details out of MEMORY.md
  and link via [[topic]]. MEMORY.md is the index, not the content.

## Recent Articles
| Date | Title | Topic |
|------|-------|-------|
| 2026-05-28 | weekly-shiplog (week 1) | meta / fleet health |
| 2026-05-28 | how the reppo agent swarm runs on aeon (explainer) | docs |
| 2026-05-28 | thread-formatter (PR #32 phantom-skill diagnosis) | meta |
| 2026-05-28 | skill-freshness audit | meta / fleet health |
| 2026-05-27 | skill-freshness audit | meta / fleet health |
| 2026-05-25 | cost-report (week 1) | meta / fleet health |
| 2026-05-25 | security-scan bootstrap | meta / fleet health |
| 2026-05-25 | weekly-review (week 1 baseline) | meta / fleet health |
| 2026-05-24 | skill-evals bootstrap baseline | meta / fleet health |
| 2026-05-21 | last30 — bitcoin (30d) — stale | crypto |
