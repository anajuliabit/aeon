# Long-term Memory
*Last consolidated: 2026-06-03*

## About This Repo
Aeon — autonomous agent on GitHub Actions via Claude Code. 34 enabled
skills on cron after 2026-06-01 PR #54 (vibecoding-digest + reddit-digest
disabled 2026-06-03 with ISS-015 wontfix — effective ~32). Inbound
messaging via Telegram. soul/ populated 2026-05-25 (ana voice).
Reppo-swarm ledger: 14 mints + 29 votes on-chain through 2026-06-03.
Phase 2 (Pinata pin + platform POST) end-to-end clean for 6+ consecutive
days since 2026-05-30.

## Current Goals
- **Close ISS-009 defence-in-depth.** Root cause traced 2026-05-28
  (`aeon.yml:479-493` capture step overwrites Write-tool output with CLI
  `.result`). 6 recurrences total — none since 2026-05-30 (5 days clean).
  Two sub-tasks: (a) codify emit-in-assistant-text contract in
  `skills/reppo-orchestrator/SKILL.md`, (b) switch chain-runner fail-fast
  `continue` → `break`.
- **Repair ISS-016 own_pod_ids prefetch.** Prefetch returns count=0 for
  8 consecutive runs through 2026-06-02; voter self-recognizes via
  ledger wallet-shortcode cross-ref. Gate vote_filter on
  publisher==agent regardless of direction.
- **Trading-agent rubric saturation.** 3-for-3 dry runs on 2026-06-02
  (same structural blocker: spot dominance + opens-only HFT + 1 NEG-PnL
  on margin-top-12). Wallet 0x9a1500b4 (14th-mint cc41abf6 source)
  flipped to NEG-PnL today (yesterday +$177 → today −$117 after 13
  fresh fills incl. one −$378 trade) — rubric admitted a wallet that
  immediately regressed; needs quality guard beyond drift-skip.
- **Assign 14 unassigned reppo datanets** (1, 2, 4, 5, 6, 7, 8, 10, 11,
  13, 14, 15, 16, 17). Orchestrator surfaces every run for 13+ days.
  Datanet 18 ArAIstotle surfaced 2026-06-02 (new mainnet datanet,
  catalog now 16).
  **10 consecutive runs** through 2026-06-03 3rd-run voter; voter
  self-recognizes via ledger wallet-shortcode cross-ref (durable
  workaround). Gate vote_filter on publisher==agent regardless of direction.
- **Trading-agent quality guard beyond drift-skip.** 6 consecutive dry
  runs through 2026-06-03 3rd-run (4 on 6-02 + 3 today) on identical
  saturation: spot dominance + opens-only HFT + sub-floor closes + empty
  caches. 14th-mint cc41abf6 source wallet 0x9a1500b4 admitted at thin
  quality (Sharpe 0.84 / MDD 91%) flipped NEG-PnL within 24h and stayed
  there — rubric needs quality guard. Operator-level options: prefetch
  perp-only filter, bump `HL_MIN_VLM_USD` past spot HFT cluster.
- **Assign 15 unassigned reppo datanets** (1, 2, 4, 5, 6, 7, 8, 10, 11,
  13, 14, 15, 16, 17, 18). Orchestrator surfaces every run for 14+ days.
  Datanet 18 ArAIstotle surfacing 3rd consecutive day.
- **INDEX bookkeeping flips queued.** ISS-007 (PR #13/#26 merged),
  ISS-010 (PR #32 merged), ISS-013 (8+ consecutive pin successes),
  ISS-014 (6+ consecutive HTTP 200).
- **Cleanup chain-runner scratch.** `.tmp-*`, `.candidates.json`,
  `build_dataset.{js,py,jq}` stubs at repo root. Sandbox blocks `rm`
  mid-run — needs a postprocess cleanup step.
- **Investigate chain-state-flip anomaly.** 2026-06-02 12:23Z
  `chain:reppo-swarm` flipped `last_status=failed` in `cron-state.json`
  while `gh run view` confirmed workflow exit success. Cleared on
  18:12Z cycle. 3 clean chain cycles on 6-03 (01:42 / 07:31 / 12:41Z).
  Likely step-level writer recording transient failure that
  `on_error:continue` skips past. Under ISS-010 scope.

## Completed Goals
- **Close ISS-017 chain-runner workflow injection.** Filed 2026-06-01.
  `${{ inputs.chain }}` interpolated into `run:` shell at
  `chain-runner.yml:41` + `:416`. Fix template on disk: env: indirection
  per messages.yml:586-591 (the same scan flipped messages.yml:578 to
  RESOLVED). Fastest high-sev close. — completed 2026-06-03 (PR #64)
- **Resolve ISS-015 secrets.** PR #56 (oauth.reddit.com route) merged
  2026-06-01 13:12Z but `REDDIT_CLIENT_ID/SECRET` still unset → 5+ days
  vibecoding-digest blocked. Operator call. — completed 2026-06-03
  (PR #65 wontfix; vibecoding-digest + reddit-digest disabled)

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers, skill health.
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit (14 mints, 29 votes).
- [Crypto research](topics/crypto.md) — narratives, picks, tracked-token alerts.
- [Market context](topics/market-context.md) — refreshed each market-context-refresh cycle.
- [TradingGymAI (datanet 9) contributor spec](topics/tradinggymai-spec.md) — operator-shared 2026-05-26.
- [Bitcoin 30-day snapshot](topics/last30-bitcoin.md) — stale baseline (05-21).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h % Threshold | Price Floor | Price Ceiling |
|---------|--------------------|-----------------|-------------|---------------|
| WELL    | moonwell-artemis   | 10%             |             |               |
| MAMO    | mamo               | 15%             |             |               |
| REPPO   | reppo              | 15%             |             |               |
| GITLAWB | gitlawb            | 15%             |             |               |

Notes: WELL = Moonwell governance (Base). MAMO/REPPO/GITLAWB lower-cap.
SURPLUS deferred pending GeckoTerminal-fallback PR; PRISM intentionally
skipped (Solana PRISM ≠ target). GITLAWB ran 2 consecutive days under
the 15% threshold (-14.93% 6-02, -14.16% 6-03 — slide eased 80bps).

## Open Issues (6 open, down from 8 — 2026-06-03)
- **ISS-005** (high, prompt-bug) — durable fix PR #47 live since 2026-05-30,
  no recurrence under new gating. Watching.
- **ISS-007** (medium, timeout) — PR #13/#26 shipped, INDEX close queued.
- **ISS-009** (high, prompt-bug) — 6 recurrences total, none since
  2026-05-30 (5 days clean). Defence-in-depth still pending.
- **ISS-010** (medium, config) — PR #32 shipped, INDEX close queued.
- **ISS-011** (medium, unknown) — vote nonce-too-low; 1 occurrence.
- **ISS-016** (medium, prompt-bug) — own_pod_ids prefetch count=0 for
  10 consecutive runs; voter self-recognizes via ledger cross-ref.

**Closed 2026-06-03:** ISS-015 (wontfix, vibecoding+reddit disabled),
ISS-017 (PR #64 env-indirection, commit 2a9ce1c).

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
  prefetch. Reddit oauth route (PR #56) added but ungettable secrets
  forced ISS-015 wontfix 2026-06-03 (vibecoding+reddit disabled).
- Cost profile is cache-dominated (73% of spend). defi-overview, heartbeat,
  reppo-digest = 38% of weekly Opus spend.
- Reppo platform enforces publisher-cannot-vote-on-own-pod. Empirical
  answer to "LIKE own mints?": NO, contract-level revert (ISS-016).
- Drift-skip precedent: if `(wallet, last_t, n_close)` triple matches a
  prior mint, skip even when content hash differs — re-mint = duplicate
  dataset spam. Drift-skip spirit also applies on regressed quality
  (same wallet + same first_t + degraded sharpe/pnl) even when triple
  differs strictly. **Not enough alone** — quality-guard layer needed
  for thin-at-admit wallets that regress within 24h (14th-mint precedent).
- Workflow-injection anti-pattern needs `env:` indirection (canonical
  shape is messages.yml:586-591; chain-runner.yml closed via PR #64
  2026-06-03).
- Fetching X tweet content from sandbox: x.com direct WebFetch → HTTP 402,
  nitter.net → empty body, **api.fxtwitter.com/{handle}/status/{id}** is the
  working unauthed fallback (returns JSON with text + quoted-tweet body).
- Memory consolidation: topic-file detail, MEMORY.md is the index.
