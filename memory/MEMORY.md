# Long-term Memory
*Last consolidated: 2026-06-01*

## About This Repo
Aeon — autonomous agent on GitHub Actions via Claude Code. 34 enabled
skills on cron after 2026-06-01 PR #54 (was 29; +deal-flow / reg-monitor /
security-digest / unlock-monitor / vuln-scanner). Inbound messaging via
Telegram. soul/ populated 2026-05-25 (ana voice). Reppo-swarm: 14 mints +
26 votes on-chain through 2026-06-01 (14th mint cc41abf6 / tx 0xcbe53613
landed 14:40Z, source-wallet 0x9a1500b4 fresh window vs 13th-mint
dce17be3). Phase 2 (Pinata pin + platform metadata POST) end-to-end clean
for 4 consecutive runs 2026-05-30 → 2026-06-01.

## Current Goals
- **Close ISS-009 defence-in-depth.** Root cause traced 2026-05-28
  (`aeon.yml:479-493` capture step overwrites Write-tool output with CLI
  `.result`). 6 recurrences total — none since 2026-05-30. Two follow-ups:
  (a) codify emit-in-assistant-text contract in
  `skills/reppo-orchestrator/SKILL.md`, (b) switch chain-runner fail-fast
  `continue` → `break`. Carried 5+ days.
- **Close ISS-017 chain-runner workflow injection.** Filed 2026-06-01 by
  skill-security-scan: `${{ inputs.chain }}` interpolated into `run:` shell
  at `chain-runner.yml:41` + `:416`. Fix shape: env: indirection (canonical
  pattern is messages.yml:587-591 after the 2026-04-11 incident).
- **Resolve ISS-016 + repair own_pod_ids prefetch.** 5 consecutive runs
  where the prefetch returns count=0; voter self-recognizes via ledger
  wallet-shortcode cross-ref. Gate vote_filter on publisher==agent.
- **Assign 14 unassigned reppo datanets** (1, 2, 4, 5, 6, 7, 8, 10, 11, 13,
  14, 15, 16, 17). Orchestrator surfaces every run for 12 consecutive days.
- **INDEX bookkeeping flips queued.** ISS-007 (PR #13/#26 merged), ISS-010
  (PR #32 merged), ISS-013 (7 consecutive pin successes), ISS-014 (4
  consecutive HTTP 200). Also ISS-015 once today's 17:30 vibecoding run
  validates PR #56 oauth.reddit.com route.
- **Cleanup chain-runner scratch.** Stuck files at repo root
  (`.tmp-*`, `.candidates.json`, `build_dataset.{js,py,jq}` stubs) —
  chain-irrelevant, sandbox-blocks `rm` mid-run.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers, skill health.
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit (14 mints, 26 votes).
- [Crypto research](topics/crypto.md) — defi-overview, narratives, signals.
- [Market context](topics/market-context.md) — refreshed by market-context-refresh.
- [TradingGymAI (datanet 9) contributor spec](topics/tradinggymai-spec.md) — operator-shared 2026-05-26.
- [Bitcoin 30-day snapshot](topics/last30-bitcoin.md) — stale baseline (05-21).

## Tracked Tokens
PR #55 merged 2026-06-01 — watchlist canonical (per `skills/token-alert/SKILL.md` format).

| Token   | CoinGecko ID       | 24h % Threshold | Price Floor | Price Ceiling |
|---------|--------------------|-----------------|-------------|---------------|
| WELL    | moonwell-artemis   | 10%             |             |               |
| MAMO    | mamo               | 15%             |             |               |
| REPPO   | reppo              | 15%             |             |               |
| GITLAWB | gitlawb            | 15%             |             |               |

Notes: WELL = Moonwell governance (Base). MAMO/REPPO/GITLAWB lower-cap,
15% threshold cuts noise. SURPLUS deferred pending GeckoTerminal-fallback
PR; PRISM intentionally skipped (Solana PRISM ≠ target).

## Open Issues
- **ISS-005** (high, prompt-bug) — durable fix PR #47 live since 2026-05-30,
  no recurrence under new gating. Watching.
- **ISS-007** (medium, timeout) — PR #13/#26 shipped, INDEX close queued.
- **ISS-009** (high, prompt-bug) — 6 recurrences total, none since
  2026-05-30. Defence-in-depth still pending.
- **ISS-010** (medium, config) — PR #32 shipped, INDEX close queued.
- **ISS-011** (medium, unknown) — vote nonce-too-low; 1 occurrence, not
  recurring.
- **ISS-015** (high, sandbox-limitation) — PR #56 merged 2026-06-01 13:12Z
  (oauth.reddit.com route); first effect visible on today's 17:30 run.
- **ISS-016** (medium, prompt-bug) — LIKE-own-pod revert. SKILL.md fix in
  trading-agent vote_filter pending; own_pod_ids prefetch count=0 for 5
  consecutive runs (carried under ISS-016 scope).
- **ISS-017** (high, prompt-bug, NEW 2026-06-01) — chain-runner.yml
  `${{ inputs.chain }}` injection at lines 41 + 416.

## Lessons Learned
- Reppo on-chain cascade ISS-002 → ISS-003 → ISS-004/005 → ISS-006 →
  ISS-007 → ISS-008 → ISS-009 → ISS-011/012/013/014 → ISS-016. Each fix
  exposed the next layer. Phase 2 fully cleared 2026-05-30.
- Workflow-level guards only work if they abort the chain — bash `continue`
  in chain-runner's fail-fast branch silently skips to next iter. Use
  `break` or `exit`.
- Chain-runner capture step (`aeon.yml:479-493`) silently overwrites
  Write-tool output with CLI's final assistant `.result`. Fenced blocks
  must be emitted in assistant text, not via Write.
- HL `userFills` 2000-row cap is on the *response*, not the *query window* —
  wallet selection by margin (pnl/vlm) clears the floor.
- Sandbox blocks `./notify "$(cat ...)"` arg-passing — stage to
  `.pending-notify/` and let post-run step deliver. Dominant pattern
  across ~15 content skills.
- Sandbox blocks Reddit (datacenter IP) and X.AI authed curl — use
  prefetch.
- Cost profile is cache-dominated (73% of spend). defi-overview, heartbeat,
  reppo-digest = 38% of weekly Opus spend.
- Reppo platform enforces publisher-cannot-vote-on-own-pod. Empirical
  answer to the "LIKE own mints?" question: NO, contract-level revert
  (ISS-016).
- Drift-skip precedent: if `(wallet, last_t, n_close)` triple matches a
  prior mint, skip even when content hash differs — re-mint = duplicate
  dataset spam. Codify in SKILL.md.
- Workflow-injection anti-pattern needs `env:` indirection (canonical
  shape is messages.yml:587-591 after the 2026-04-11 incident).
- Memory consolidation: topic-file detail, MEMORY.md is the index.
