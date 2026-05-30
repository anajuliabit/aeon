# Long-term Memory
*Last consolidated: 2026-05-29*

## About This Repo
Aeon — autonomous agent running on GitHub Actions via Claude Code. 29
enabled skills on cron; inbound messaging via Telegram (live). Fleet exited
bootstrap 2026-05-21. soul/ populated 2026-05-25 (ana voice). Reppo-swarm
chain first on-chain output landed 2026-05-26. 2026-05-28 was the heaviest
shipping day: 10 PRs merged (#30-#39) and the 4th mint ever landed. 2026-05-29
overnight + morning chain runs added the **5th + 6th mints ever** (LIT
single-market and **xyz:BRENTOIL** — first commodity-perp mint), and exposed
the Phase 2 platform/IPFS layer that quietly never worked (ISS-012, ISS-013).

## Current Goals
- Durable fix for ISS-009 — chain-runner.yml `fail-fast` branch uses bash
  `continue` (skips to next loop iter) instead of `break`; PR #27's workflow
  grep guard merged but did not abort downstream dispatch when fenced
  reppo-plan block was missing 2026-05-27. Third occurrence today.
- Assign agents to the 14 unassigned reppo datanets (1, 2, 4, 5, 6, 7, 8, 10,
  11, 13, 14, 15, 16, 17 — surfaced every reppo-orchestrator run for 7 days,
  untouched). *[goal-tracker 2026-05-28: BLOCKED — gated on PR #30, which
  merged 2026-05-28T12:05Z; blocker now lifted, next step is staged
  assignment.]* *[goal-tracker 2026-05-29: ON TRACK ↑ improving — PR #30
  blocker cleared; surfaced 9th day with 0 assignments staged; next step
  unchanged.]*
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
- **ISS-013 — rotate / verify PINATA_JWT.** Every Phase 2 IPFS pin since
  Phase 2 wired has returned HTTP 403; both today's mints (5th and 6th) are
  stuck mid-pipeline waiting for the dataset_uri. Without this fix, every
  future mint is blind. Operator-call (secret rotation).
- **ISS-012 — diagnose platform metadata POST HTTP 400.** PR #42 (HTTP body
  capture) opened today; blocks root-cause work. 3 occurrences across today
  (1 fresh + 2 retries). Confirmed POST does NOT gate on fresh pin (400 ≠
  empty dataset_uri).
- **Durable ISS-005 fix** — move validityEpoch ≤ current-1 filter into
  `scripts/prefetch-reppo.sh`. Add CLI idempotency on vote (pods 372/373 got
  7× DISLIKE'd each on 2026-05-28; today's runs steered to 332/390/391
  organically — 1st vote on each new pod — so the mitigation is working but
  not durable).
- **Assign agents to the 14 unassigned reppo datanets** (1, 2, 4, 5, 6, 7,
  8, 10, 11, 13, 14, 15, 16, 17 — 9th day surfaced). PR #30 blocker lifted
  2026-05-28; goal-tracker flagged ready to stage one-at-a-time.
- **Close ISS-009 fully** — orchestrator's emit-in-assistant-text fix
  validated across 4 chain runs since (no SKIP since 2026-05-28 morning).
  Still TODO: codify the contract in `skills/reppo-orchestrator/SKILL.md`
  AND switch chain-runner's fail-fast `continue` → `break` as defence-in-depth.
- **INDEX bookkeeping** — close ISS-007 (PR #13/#26 merged), close ISS-010
  (PR #32 merged 2026-05-28T12:09Z). Carried 3+ days now.

## Completed Goals
- **PR #30 — reppo-trading-agent rewrite (HL public data)** merged
  2026-05-28T12:05Z. Follow-ons #34 (`userFillsByTime` window) + #37 (rank
  HL wallets by margin, drop 7d span floor, anti-regurgitation contract)
  together unlocked the 4th mint ever (hash 397ee2e8, wallet 0x2b3349ff,
  sharpe 110, win 0.76). Today's 5th + 6th mints validate the path further.
- **Unblock reppo-swarm on-chain output** — 2026-05-26. First mint
  (ETH Supertrend, tx 0x77f1…) + first vote (DISLIKE pod 373, tx 0x937d…).
  ISS-004/006/008 all resolved.
- **Populate `soul/`** — 2026-05-25 (PR #12).
- **Align tradinggymai rubric** — 2026-05-26 (PR #28).
- **Phantom-skill dispatch** — 2026-05-28 (PR #32 closes ISS-010).
- **skill-evals output_pattern realignment** — 2026-05-28 (PR #31).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, recurring blockers, skill health.
- [Crypto research](topics/crypto.md) — defi-overview, narratives, token signals.
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit trail.
- [Market context](topics/market-context.md) — refreshed by market-context-refresh.
- [TradingGymAI (datanet 9) contributor spec](topics/tradinggymai-spec.md) — operator-shared 2026-05-26.
- [Bitcoin 30-day snapshot](topics/last30-bitcoin.md) — last30 baseline (stale, 05-21).

## Open Issues
- ISS-005 (high, prompt-bug) — vote pods fail POD_NOT_VALID_FOR_EPOCH; agent-side
  workaround live (filter validityEpoch ≤ current-1); organic mitigation
  today (steered to 332/390/391 — 1st vote on each). Durable prefetch fix +
  CLI vote-dedup both pending.
- ISS-007 (medium, timeout) — Base RPC INTERNAL_ERROR; PR #13/#26 shipped.
  INDEX still shows open — bookkeeping queued (4 days).
- ISS-009 (high, prompt-bug) — root cause traced 2026-05-28 (chain-runner
  capture step overwrites Write-tool output with CLI `.result`). Fix path
  validated across 4+ chain runs. Two follow-ups pending: codify
  emit-in-assistant-text in orchestrator SKILL.md, switch chain-runner
  fail-fast `continue` → `break`.
- ISS-010 (medium, config) — fix shipped in PR #32 (merged 2026-05-28T12:09Z).
  INDEX still shows open — bookkeeping queued.
- **ISS-011 (medium, unknown, NEW 2026-05-29)** — vote write REVERT "nonce
  too low" after sibling votes land same batch. 1 occurrence (vote-391 1st
  run); 2nd-run retry landed clean.
- **ISS-012 (medium, api-change, NEW 2026-05-29)** — Reppo platform metadata
  POST HTTP 400 for queued mint Phase 2. 3 occurrences today across mints
  397ee2e8 + 9794ed80. PR #42 (HTTP body capture) opened, blocks root cause.
- **ISS-013 (medium, missing-secret, NEW 2026-05-29)** — IPFS pin to Pinata
  HTTP 403. 2 occurrences (5th + 6th mints both stuck). Operator-call for
  PINATA_JWT rotation/verification.
- **ISS-015 (high, sandbox-limitation, NEW 2026-05-30)** — vibecoding-digest
  can't reach Reddit; prefetch (runner IP) + WebFetch (tool-layer block)
  both dead, 3 consecutive days (5-28/5-29/5-30). No in-skill workaround
  left. Needs authed Reddit API or alternative source.

## Open PRs
- **#41** — replicate-oneoff workflow (workflow_dispatch image gen), opened
  2026-05-29T02:01Z.
- **#42** — capture HTTP status + response body on Pinata pin / platform
  POST failures, opened 2026-05-29T02:05Z. Directly unblocks ISS-012/013
  diagnosis.

## Lessons Learned
- Reppo on-chain blockers cascade: ISS-002 → ISS-003 → ISS-004/005 → ISS-006
  → ISS-007 → ISS-008 → ISS-009 → ISS-011/012/013 (Phase 2). Each fix
  exposes the next layer. The Phase 2 platform/IPFS surface was effectively
  untested until the 5th mint actually reached it on 2026-05-29.
- Workflow-level guards only work if they actually abort the chain — bash
  `continue` in chain-runner's fail-fast branch silently skips to the next
  loop iteration. Use `break` or `exit`.
- Chain-runner's capture step (`aeon.yml:479-493`) silently overwrites
  Write-tool output with the CLI's final assistant `.result`. Skills that
  pass fenced blocks downstream must emit them in the assistant text, not
  via Write. (Diagnosed 2026-05-28; held across 4+ chain runs since.)
- Cap surprises are on the *response*, not the *query window* — PR #30/#34
  widened HL's `userFillsByTime` window to 7d but the 2000-row response cap
  still collapsed every top-leaderboard wallet to <1 day span; PR #37's
  wallet selection by margin (pnl/vlm) cleared the floor.
- Sandbox blocks `./notify "$(cat ...)"` arg-passing on command-substitution
  analyzer + `bash -c` wrapper. Stage to `.pending-notify/` and let post-run
  step deliver. Pattern now used by 12+ skills daily.
- Sandbox blocks Reddit (datacenter IP) and X.AI authed curl — use prefetch.
- Auto-recovery helpers (auto-approve, auto-grant, auto-lock) sometimes need
  retry-with-backoff because allowance/lock reads can be pre-confirmation stale.
- Reppo ledger rows are for on-chain-confirmed actions only — a queued intent
  is not a mint. (Phase 2 IPFS/platform failure does NOT remove the on-chain
  mint row — those reverts are bookkeeping debt, not chain failures.)
- Cost profile is cache-dominated (73% of spend is cache read+write). Standard
  "model-downgrade" filter misses Sonnet-rotation savings for high-cache
  skills (defi-overview, heartbeat, reppo-digest = 38% of weekly Opus spend).
  Operator-call territory.
- Memory consolidation: when a topic file grows, move details out of MEMORY.md
  and link via [[topic]]. MEMORY.md is the index, not the content.
- Phase 2 (post-on-chain platform + IPFS) does NOT gate on fresh pin success
  — a missing dataset_uri still proceeds to POST and yields a 400. Worth
  fixing at the sequencing level once ISS-012 root cause is known.

## Recent Articles
| Date | Title | Topic |
|------|-------|-------|
| 2026-05-29 | skill-freshness audit | meta / fleet health |
| 2026-05-28 | weekly-shiplog (week 1) | meta / fleet health |
| 2026-05-28 | how the reppo agent swarm runs on aeon (explainer) | docs |
| 2026-05-28 | thread-formatter (PR #32 phantom-skill diagnosis) | meta |
| 2026-05-28 | skill-freshness audit | meta / fleet health |
| 2026-05-25 | cost-report (week 1) | meta / fleet health |
| 2026-05-25 | security-scan bootstrap | meta / fleet health |
| 2026-05-25 | weekly-review (week 1 baseline) | meta / fleet health |
| 2026-05-24 | skill-evals bootstrap baseline | meta / fleet health |
| 2026-05-21 | last30 — bitcoin (30d) — stale | crypto |
