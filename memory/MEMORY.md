# Long-term Memory
*Last consolidated: 2026-05-31*

## About This Repo
Aeon — autonomous agent on GitHub Actions via Claude Code. 29 enabled skills
on cron; inbound messaging via Telegram (live). Fleet exited bootstrap
2026-05-21. soul/ populated 2026-05-25 (ana voice). Reppo-swarm first on-chain
output 2026-05-26. 13 mints + 26 votes on-chain through 2026-05-31. Phase 2
(Pinata pin + platform metadata POST) end-to-end clean for 3 consecutive runs
2026-05-30 → 2026-05-31 morning.

## Current Goals
- **Close ISS-009 defence-in-depth.** Root cause traced 2026-05-28
  (`aeon.yml:479-493` capture step overwrites Write-tool output with CLI
  `.result`). 6 recurrences total. Two follow-ups carry: (a) codify
  emit-in-assistant-text contract in `skills/reppo-orchestrator/SKILL.md`,
  (b) switch chain-runner fail-fast `continue` → `break`. Carried 4+ days.
- **Assign 14 unassigned reppo datanets** (1, 2, 4, 5, 6, 7, 8, 10, 11, 13,
  14, 15, 16, 17). Surfaced every orchestrator run for 11 consecutive days.
  PR #30 blocker lifted 2026-05-28; next step is staged 1-at-a-time pick.
- **Resolve ISS-016** (NEW 2026-05-31). Gate trading-agent vote_filter on
  publisher==agent so own-mint pods never selected regardless of direction.
- **Operator call ISS-015** — vibecoding-digest Reddit 4 days blocked.
  PR #56 proposes oauth.reddit.com route — needs `REDDIT_CLIENT_ID/SECRET`.
- **INDEX bookkeeping** — close ISS-007 (PR #13/#26 merged), close ISS-010
  (PR #32 merged), flip ISS-014 resolved (3 consecutive HTTP 200), flip
  ISS-013 resolved (6 consecutive pin successes). 5+ days queued.
- **Cleanup chain-runner scratch.** Stuck scratch files at repo root
  (`.tmp-*`, `.candidates.json`) — chain-irrelevant.

## Completed Goals
- **Phase 2 unblocked 2026-05-30.** ISS-012 (PR #44 Zod schema), ISS-013
  (PINATA_JWT rotation), ISS-014 (server self-healed) — first end-to-end
  clean mints; 6 consecutive pin successes through 2026-05-31.
- **PR #30 — reppo-trading-agent rewrite (HL public data)** merged
  2026-05-28T12:05Z. Follow-ons #34/#37 unlocked the 4th mint ever.
- **Reppo on-chain blocker cascade cleared** — 2026-05-26 first mint + vote.
- **Populate `soul/`** — 2026-05-25 (PR #12).
- **Durable ISS-005 fix** — PR #47 merged 2026-05-30 (vote-dedup prefetch +
  platform subnetId UUID). No 7× DISLIKE compounding since.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers, skill health.
- [Crypto research](topics/crypto.md) — defi-overview, narratives, signals.
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit trail (13 mints, 26 votes).
- [Market context](topics/market-context.md) — refreshed by market-context-refresh.
- [TradingGymAI (datanet 9) contributor spec](topics/tradinggymai-spec.md) — operator-shared 2026-05-26.
- [Bitcoin 30-day snapshot](topics/last30-bitcoin.md) — stale baseline (05-21).

## Tracked Tokens
Canonical watchlist for token-alert and other token-scoped skills. Format per `skills/token-alert/SKILL.md`.

| Token   | CoinGecko ID       | 24h % Threshold | Price Floor | Price Ceiling |
|---------|--------------------|-----------------|-------------|---------------|
| WELL    | moonwell-artemis   | 10%             |             |               |
| MAMO    | mamo               | 15%             |             |               |
| REPPO   | reppo              | 15%             |             |               |
| GITLAWB | gitlawb            | 15%             |             |               |

Notes:
- WELL = Moonwell governance token (Base).
- MAMO, REPPO, GITLAWB are lower-cap; default 24h thresholds bumped to 15% to cut noise from ordinary volatility.
- SURPLUS (Base `0xc52a…ba3`, "Surplus Intelligence") intentionally not listed yet — no CoinGecko ID; pending GeckoTerminal-fallback PR in token-alert.
- PRISM intentionally skipped — the only CoinGecko PRISM is Solana-based and not the one to track.

## Open Issues
- **ISS-005** (high, prompt-bug) — durable fix PR #47 merged 2026-05-30; no
  recurrence under new gating. Watching.
- **ISS-007** (medium, timeout) — PR #13/#26 shipped, INDEX close queued.
- **ISS-009** (high, prompt-bug) — 6 recurrences. Defence-in-depth still pending.
- **ISS-010** (medium, config) — PR #32 shipped, INDEX close queued.
- **ISS-011** (medium, unknown) — vote nonce-too-low; 1 occurrence, not recurring.
- **ISS-015** (high, sandbox-limitation) — vibecoding-digest Reddit blocked
  4 consecutive days. PR #56 (oauth.reddit.com route) open, needs secrets.
- **ISS-016** (medium, prompt-bug, NEW 2026-05-31) — vote LIKE on agent's own
  pod reverts CANNOT_VOTE_FOR_OWN_POD. SKILL.md fix in trading-agent vote_filter.

## Open PRs (5 as of 17:45 UTC)
- **#58** docs(skill-graph): NEW_ENABLED 8 · NEW_DEPS 33 (17:41Z, ~5min)
- **#57** refactor(reppo): @reppo/cli≥0.6.0 native Phase 2 (15:39Z, ~2h)
- **#56** fix(vibecoding): Reddit via oauth.reddit.com — ISS-015 (15:09Z, ~3h)
- **#55** chore(tokens): canonical watchlist WELL/MAMO/REPPO/GITLAWB (15:01Z, ~3h)
- **#54** chore(skills): enable Tier 1 crypto-builder skills (13:32Z, ~4h)

## Lessons Learned
- Reppo on-chain blockers cascade ISS-002 → ISS-003 → ISS-004/005 → ISS-006
  → ISS-007 → ISS-008 → ISS-009 → ISS-011/012/013/014 → ISS-016. Each fix
  exposes the next layer. Phase 2 fully cleared 2026-05-30.
- Workflow-level guards only work if they actually abort the chain — bash
  `continue` in chain-runner's fail-fast branch silently skips to the next
  loop iter. Use `break` or `exit`.
- Chain-runner capture step (`aeon.yml:479-493`) silently overwrites Write-tool
  output with CLI's final assistant `.result`. Fenced blocks must be emitted
  in assistant text, not via Write.
- HL `userFills` 2000-row cap is on the *response*, not the *query window* —
  wallet selection by margin (pnl/vlm) clears the floor.
- Sandbox blocks `./notify "$(cat ...)"` arg-passing — stage to
  `.pending-notify/` and let post-run step deliver. Dominant pattern across
  ~15 content skills.
- Sandbox blocks Reddit (datacenter IP) and X.AI authed curl — use prefetch.
- Cost profile is cache-dominated (73% of spend). defi-overview, heartbeat,
  reppo-digest = 38% of weekly Opus spend; Sonnet rotation could cut ~$55-65/wk.
- Memory consolidation: topic-file detail, MEMORY.md is the index.
- Reppo platform enforces publisher-cannot-vote-on-own-pod. Empirical answer
  to the "LIKE own mints?" question: NO, contract-level revert (ISS-016).
- Drift-skip precedent: if `(wallet, last_t, n_close)` triple matches a
  prior mint, skip even when content hash differs — re-mint = duplicate
  dataset spam. Codify in SKILL.md.
