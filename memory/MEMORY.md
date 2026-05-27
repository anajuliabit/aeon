# Long-term Memory
*Last consolidated: 2026-05-27*

## About This Repo
Aeon — autonomous agent running on GitHub Actions via Claude Code. ~21 skills
enabled on cron; inbound messaging via Telegram (live). Fleet exited bootstrap
2026-05-21. soul/ populated 2026-05-25 (ana voice). Reppo-swarm chain first
on-chain output (mint + vote) landed 2026-05-26 after 5 days of stacked blockers.

## Current Goals
- Land PR #30 (rewrite reppo-trading-agent to construct pods from HL public
  data — Hyperliquid leaderboard fills + IPFS pin + platform POST). Every
  reppo-swarm run open keeps minting off-rubric strategy text after PR #28
  rewrote the rubric.
- Durable fix for ISS-009 — chain-runner.yml `fail-fast` branch uses bash
  `continue` (skips to next loop iter) instead of `break`; PR #27's workflow
  grep guard merged but did not abort downstream dispatch when fenced
  reppo-plan block was missing 2026-05-27. Third occurrence today.
- Assign agents to the 14 unassigned reppo datanets (1, 2, 4, 5, 6, 7, 8, 10,
  11, 13, 14, 15, 16, 17 — surfaced every reppo-orchestrator run for 7 days,
  untouched).
- Durable ISS-005 fix — move validityEpoch ≤ current-1 filter into
  `scripts/prefetch-reppo.sh` so vote_cap=3 isn't bottlenecked at 2 epoch-97
  pods. Agent-side workaround live since 2026-05-24.

## Completed Goals
- Unblock reppo-swarm on-chain output — completed 2026-05-26. First mint
  (ETH Supertrend, tx 0x77f1…) + first vote (DISLIKE pod 373, tx 0x937d…)
  ever on-chain. 21st run (05-26 evening) shipped 3 on-chain (1 mint + 2
  votes, 0 failures — most productive run since chain launch).
  ISS-004 (PR #10/#19/#20), ISS-006 (PR #11/#23), ISS-008 (PR #21) all resolved.
- Populate `soul/` — completed 2026-05-25 (PR #12: SOUL.md 74L + STYLE.md 96L).
- Align tradinggymai rubric with operator-shared contributor spec —
  completed 2026-05-26 (PR #28). Spec preserved at [[tradinggymai-spec]].

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, recurring blockers, skill health.
- [Crypto research](topics/crypto.md) — defi-overview, narratives, token signals.
- [Bitcoin 30-day snapshot](topics/last30-bitcoin.md) — last30 baseline (stale, 05-21).
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit trail.
- [TradingGymAI (datanet 9) contributor spec](topics/tradinggymai-spec.md) — operator-shared 2026-05-26.

## Open Issues
- ISS-005 (high, prompt-bug) — vote pods fail POD_NOT_VALID_FOR_EPOCH; agent-side
  workaround live (filter validityEpoch ≤ current-1); durable prefetch + agent-prompt
  fix still pending. With epoch-97 alone yielding only 2 pods, vote_cap=3 is
  bottlenecked.
- ISS-007 (medium, timeout) — Base RPC `INTERNAL_ERROR`; PR #13 retry merged,
  PR #26 widened budget. INDEX.md still shows open — action-converter has
  bookkeeping queued.
- ISS-009 (high, prompt-bug) — reppo-orchestrator drops fenced reppo-plan
  block; 3rd occurrence 2026-05-27. PR #24 prompt-tightening + PR #27 workflow
  grep guard both insufficient (chain-runner `continue` does not abort chain
  in fail-fast branch). Escalation: `continue` → `break`.

## Open PRs
- #30 — rewrite reppo-trading-agent to construct pods from HL public data
  (opened 2026-05-26 22:50Z; <24h old).

## Lessons Learned
- Reppo on-chain blockers cascade: ISS-002 → ISS-003 → ISS-004/005 → ISS-006 →
  ISS-007 → ISS-008 → ISS-009. Took 6 days to fully unblock. Each fix exposed
  the next — assume more surface as real writes scale.
- Auto-recovery helpers (auto-approve, auto-grant, auto-lock) sometimes need
  retry-with-backoff because allowance/lock reads can be pre-confirmation stale
  (PR #20, PR #26 widened budgets after first-pass failures).
- Workflow-level guards (PR #27) only work if they actually abort the chain —
  bash `continue` in chain-runner's fail-fast branch silently skips to the
  next iteration. Use `break` or `exit` to abort downstream dispatch.
- Sandbox blocks Reddit (datacenter IP) and X.AI authed curl — use the prefetch pattern.
- `./notify "$(cat ...)"` arg-passing intermittently fails in sandbox — stage to
  `.pending-notify/` and let the post-run step pick it up (defi-overview pattern).
- Orchestrator skills that pass fenced blocks to downstream chain steps must
  treat the block as non-negotiable AND have the downstream step abort on
  missing block. Prompt-level reinforcement alone proved insufficient (ISS-009).
- Reppo ledger rows are for on-chain-confirmed actions only — a queued intent is not a mint.
- Cost profile is cache-dominated (73% of spend is cache read+write). The
  standard "model-downgrade" filter misses Sonnet-rotation savings for
  high-cache skills (defi-overview, heartbeat, reppo-digest = 38% of weekly
  Opus spend). Operator-call territory, not auto-fix.
- skill-evals's evals.json carries wrong `output_pattern` entries for skills that
  write to `memory/logs/` (token-alert, skill-health) or have no skills/ directory
  (hn-digest, polymarket) — action queue from 2026-05-24, still unworked.

## Recent Articles
| Date | Title | Topic |
|------|-------|-------|
| 2026-05-27 | skill-freshness audit | meta / fleet health |
| 2026-05-26 | skill-freshness audit | meta / fleet health |
| 2026-05-25 | cost-report (week 1) | meta / fleet health |
| 2026-05-25 | security-scan bootstrap | meta / fleet health |
| 2026-05-25 | weekly-review (week 1 baseline) | meta / fleet health |
| 2026-05-24 | skill-evals bootstrap baseline | meta / fleet health |
| 2026-05-21 | The 100x Fix: Neuro-Symbolic AI & the AI Energy Crisis | AI / energy efficiency |
| 2026-05-21 | competitor-launch-radar | competitive intel |
| 2026-05-21 | last30 — bitcoin (30d) | crypto |
