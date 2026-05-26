# Long-term Memory
*Last consolidated: 2026-05-26*

## About This Repo
Aeon — autonomous agent running on GitHub Actions via Claude Code. ~21 skills
enabled on cron; inbound messaging via Telegram (live). Fleet exited bootstrap
2026-05-21. soul/ populated 2026-05-25 (ana voice). Reppo-swarm chain first
on-chain output (mint + vote) landed 2026-05-26 after 5 days of stacked blockers.

## Current Goals
- Assign agents to the 14 unassigned reppo datanets (surfaced every run, untouched
  all week).
- Align reppo-trading-agent + datanet-9 rubric with the operator-shared canonical
  contributor spec (Hyperliquid perp trade datasets with PnL/Sharpe/MDD/market
  context/verification — not strategy descriptions). Spec preserved at
  `memory/topics/tradinggymai-spec.md`. PR in flight.

## Completed Goals
- Unblock reppo-swarm on-chain output — completed 2026-05-26. 1st mint
  (tx 0x77f1386fb6fe3209bbf1a380b2be64f1f1c2c557416c9c7c0d31486a7e48a61f) + 1st
  vote (tx 0x937d9f3cc006e805bd2ace1b110e71e29fa659052c12b88a8ce3079c5136a455)
  both landed on-chain today; ISS-004 / ISS-006 / ISS-008 all resolved by
  PRs #10 / #23 / #21. Originally tracked three operator/config actions:
  ISS-004 (subnet grant — PR #10 merged 2026-05-25 adds auto-grant helper, awaits
  on-chain verification), ISS-005 (per-pod epoch validity in prefetch + agent
  filter — agent-side workaround already live), ISS-006 (lock REPPO for voting
  power — PR #11 merged 2026-05-25 adds lock helper, awaits on-chain verification).
- Populate `soul/` so content skills stop running in neutral voice — completed
  2026-05-25 (PR #12 populated `soul/SOUL.md` 74L + `soul/STYLE.md` 96L from
  `~/code/social`).
- Unblock reppo-swarm on-chain output. Operator actions still outstanding:
  ISS-004 (subnet grant) and ISS-006 (lock REPPO for voting power). ISS-005
  agent-side workaround live; ISS-007 (RPC retry) has PR #13 in flight.
- Assign agents to the 14 unassigned reppo datanets (surfaced every run, untouched
  all week).
- Populate `soul/` so content skills (write-tweet, article, digest, etc.) stop
  running in neutral voice — PR #12 in flight.
- Lock in reppo on-chain output — verify the next several reppo-swarm runs keep
  minting + voting cleanly now that the ISS-004/006/008 cascade has cleared.
  Watch for ISS-005's durable prefetch fix and the ISS-009 fenced-block regression.
- Assign agents to the 14 unassigned reppo datanets (1, 2, 4, 5, 6, 7, 8, 10, 11,
  13, 14, 15, 16, 17 — surfaced every reppo-orchestrator run for 6 days, untouched).

## Completed Goals
- Unblock reppo-swarm on-chain output — completed 2026-05-26. First mint (ETH
  Supertrend, tx 0x77f1…) + first vote (DISLIKE pod 373, tx 0x937d…) ever on-chain.
  2 mints + 1 vote landed across runs 17 + 19. ISS-004 (PR #10/#19/#20),
  ISS-006 (PR #11/#23), ISS-008 (PR #21) all resolved.
- Populate `soul/` — completed 2026-05-25 (PR #12: SOUL.md 74L + STYLE.md 96L).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, recurring blockers, skill health.
- [Crypto research](topics/crypto.md) — defi-overview, narratives, token signals.
- [Bitcoin 30-day snapshot](topics/last30-bitcoin.md) — last30 baseline (stale, 05-21).
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit trail.
- [TradingGymAI (datanet 9) contributor spec](topics/tradinggymai-spec.md) — operator-shared 2026-05-26.

## Open Issues
- ISS-005 (high, prompt-bug) — vote pods fail POD_NOT_VALID_FOR_EPOCH; agent-side
  workaround live (filter validityEpoch ≤ current-1); durable prefetch + agent-prompt
  fix still pending. With epoch-97 alone yielding only 2 pods, vote_cap=3 is now
  bottlenecked.
- ISS-007 (medium, timeout) — Base RPC `INTERNAL_ERROR`; PR #13 retry merged,
  PR #26 widened budget today. INDEX.md still shows open — leave for action-converter.

## Open PRs
- None (8 PRs merged today: #19/#20/#21/#23/#24/#25/#26 + #22 closed unmerged).

## Lessons Learned
- Reppo on-chain blockers cascade: ISS-002 → ISS-003 → ISS-004/005 → ISS-006 →
  ISS-007 → ISS-008 → ISS-009. Took 6 days to fully unblock. Each fix exposed
  the next — assume more surface as real writes scale.
- Auto-recovery helpers (auto-approve, auto-grant, auto-lock) sometimes need
  retry-with-backoff because allowance/lock reads can be pre-confirmation stale
  (PR #20, PR #26 widened budgets after first-pass failures).
- Sandbox blocks Reddit (datacenter IP) and X.AI authed curl — use the prefetch pattern.
- `./notify "$(cat ...)"` arg-passing intermittently fails in sandbox — stage to
  `.pending-notify/` and let the post-run step pick it up (defi-overview pattern).
- Orchestrator skills that pass fenced blocks to downstream chain steps must
  treat the block as non-negotiable (ISS-009: LLM emitted only `## Summary`, broke
  trading-agent gate). PR #24 hardened the prompt.
- "code: UNKNOWN" was a wrapping bug in postprocess-reppo.sh (PR #8) — once the raw
  CLI error surfaces, the actual blockers are usually config or prompt issues.
- Reppo ledger rows are for on-chain-confirmed actions only — a queued intent is not a mint.
- Cost profile is cache-dominated (73% of spend is cache read+write). The
  standard "model-downgrade" filter misses Sonnet-rotation savings for
  high-cache skills (defi-overview, heartbeat, reppo-digest = 38% of weekly Opus
  spend). Operator-call territory, not auto-fix.
- skill-evals's evals.json carries wrong `output_pattern` entries for skills that
  write to `memory/logs/` (token-alert, skill-health) or have no skills/ directory
  (hn-digest, polymarket) — action queue from 2026-05-24, still unworked.

## Recent Articles
| Date | Title | Topic |
|------|-------|-------|
| 2026-05-26 | skill-freshness audit | meta / fleet health |
| 2026-05-25 | cost-report (week 1) | meta / fleet health |
| 2026-05-25 | security-scan bootstrap | meta / fleet health |
| 2026-05-25 | weekly-review (week 1 baseline) | meta / fleet health |
| 2026-05-25 | skill-freshness audit | meta / fleet health |
| 2026-05-24 | skill-evals bootstrap baseline | meta / fleet health |
| 2026-05-21 | The 100x Fix: Neuro-Symbolic AI & the AI Energy Crisis | AI / energy efficiency |
| 2026-05-21 | competitor-launch-radar | competitive intel |
| 2026-05-21 | last30 — bitcoin (30d) | crypto |
