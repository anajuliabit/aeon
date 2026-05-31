# Long-term Memory
*Last consolidated: 2026-05-30*

## About This Repo
Aeon — autonomous agent on GitHub Actions via Claude Code. 29 enabled skills
on cron; inbound messaging via Telegram (live). Fleet exited bootstrap
2026-05-21. soul/ populated 2026-05-25 (ana voice). Reppo-swarm first on-chain
output 2026-05-26. 2026-05-30 was the heaviest mint day (3 mints: 10th-12th
ever) and the first day Phase 2 (Pinata pin + platform metadata POST) ran
end-to-end clean — runs 4 + 5 both posted HTTP 200 with no Phase 2 reverts.

## Current Goals
- **ISS-009 codification.** 5th recurrence today (2nd run drift after 6
  consecutive chain runs holding the emit-in-assistant-text path). Still
  TODO: codify contract in `skills/reppo-orchestrator/SKILL.md` AND switch
  chain-runner fail-fast `continue` → `break` as defence-in-depth. Carried
  4+ days.
- **Assign 14 unassigned reppo datanets** (1, 2, 4, 5, 6, 7, 8, 10, 11, 13,
  14, 15, 16, 17). 10th day surfaced. PR #30 blocker lifted 2026-05-28;
  staging gated on operator pick of rubric.
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
- Assign agents to the 14 unassigned reppo datanets (1, 2, 4, 5, 6, 7, 8, 10,
  11, 13, 14, 15, 16, 17 — 8th day surfaced).
- INDEX bookkeeping — close ISS-007 (PR #13/#26 merged), close ISS-010
  (PR #32 merged).
- **Assign agents to the 14 unassigned reppo datanets** (1, 2, 4, 5, 6, 7,
  8, 10, 11, 13, 14, 15, 16, 17 — 9th day surfaced). PR #30 blocker lifted
  2026-05-28; goal-tracker flagged ready to stage one-at-a-time.
- **Close ISS-009 fully** — orchestrator's emit-in-assistant-text fix
  validated across 4 chain runs since (no SKIP since 2026-05-28 morning).
  Still TODO: codify the contract in `skills/reppo-orchestrator/SKILL.md`
  AND switch chain-runner's fail-fast `continue` → `break` as defence-in-depth.
- **INDEX bookkeeping** — close ISS-007 (PR #13/#26 merged), close ISS-010
  (PR #32 merged 2026-05-28T12:09Z). 5+ days queued.
- **ISS-015 mitigation.** vibecoding-digest Reddit blocked (3 consecutive
  days). Options: authed Reddit API (`REDDIT_CLIENT_ID/SECRET` →
  `oauth.reddit.com`), pushshift archive, or alternate source. Operator call.
- **Cleanup chain-runner scratch.** 4 stuck files at repo root from 4th-run
  trading-agent build steps (`.tmp-build-candidates.{py,js}`,
  `.tmp-build-dataset.js`, `.candidates.json`) — chain-irrelevant.

## Completed Goals
- **Phase 2 unblocked 2026-05-30.** ISS-012 (PR #44 Zod schema), ISS-013
  (PINATA_JWT rotation), ISS-014 (server self-healed) all resolved across
  4th + 5th chain runs — first end-to-end clean mints ever.
- **PR #30 — reppo-trading-agent rewrite (HL public data)** merged
  2026-05-28T12:05Z. Follow-ons #34 / #37 unlocked the 4th mint ever;
  5th-12th mints validated the path further.
- **Reppo on-chain blocker cascade cleared** — 2026-05-26 first mint + vote.
- **Populate `soul/`** — 2026-05-25 (PR #12).
- **Align tradinggymai rubric** — 2026-05-26 (PR #28).
- **Phantom-skill dispatch** — 2026-05-28 (PR #32 closes ISS-010).
- **skill-evals output_pattern realignment** — 2026-05-28 (PR #31).
- **Durable ISS-005 fix** — 2026-05-30 (PR #47 "vote dedup prefetch + platform
  subnetId = UUID" merged). Moved validityEpoch ≤ current-1 filter into
  `scripts/prefetch-reppo.sh` and added CLI idempotency on vote — pod-dedup
  durable, no more 7× DISLIKE compounding.
- **ISS-013 — PINATA_JWT rotation** — 2026-05-30. Secret rotated by operator;
  3 consecutive Phase 2 IPFS pin successes confirm fix (per 2026-05-30
  morning-brief). Phase 2 mints no longer blocked at dataset_uri.
- **ISS-012 — platform metadata POST HTTP 400** — 2026-05-30 (PR #44
  "satisfy platform Zod schema — subnetId string, podName cap 200,
  extract_detail 600" merged). 400 cleared; follow-on ISS-014 (HTTP 500) is
  a new layer and tracked separately. PR #42 (HTTP body capture) provided
  the diagnostic surface that enabled the Zod-schema diagnosis.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers, skill health.
- [Crypto research](topics/crypto.md) — defi-overview, narratives, signals.
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit trail (12 mints, 24 votes).
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
- **ISS-005** (high, prompt-bug) — vote POD_NOT_VALID_FOR_EPOCH; agent-side
  filter live, durable prefetch fix + CLI vote-dedup pending. PR #47 (vote
  dedup + subnetId UUID) was open this morning, merged before 14:00.
- **ISS-007** (medium, timeout) — PR #13/#26 shipped, INDEX close queued.
- **ISS-009** (high, prompt-bug) — 5 recurrences. Fix path validated 6+ runs
  before today's drift. Codify-in-SKILL + chain-runner `continue` → `break`
  remain.
- **ISS-010** (medium, config) — PR #32 shipped, INDEX close queued.
- **ISS-011** (medium, unknown) — vote nonce-too-low after sibling votes
  same batch. 1 occurrence; not recurring.
- **ISS-015** (high, sandbox-limitation, NEW 2026-05-30) — vibecoding can't
  reach Reddit (prefetch + WebFetch both dead, 3 consecutive days).

## Open PRs
- *(0 open as of 14:00 UTC — #47 merged this morning.)*

## Lessons Learned
- Reppo on-chain blockers cascade ISS-002 → ISS-003 → ISS-004/005 → ISS-006
  → ISS-007 → ISS-008 → ISS-009 → ISS-011/012/013/014. Each fix exposes the
  next layer. Phase 2 fully cleared 2026-05-30.
- Workflow-level guards only work if they actually abort the chain — bash
  `continue` in chain-runner's fail-fast branch silently skips to the next
  loop iter. Use `break` or `exit`.
- Chain-runner capture step (`aeon.yml:479-493`) silently overwrites Write-tool
  output with the CLI's final assistant `.result`. Fenced blocks must be
  emitted in assistant text, not via Write.
- HL `userFills` 2000-row cap is on the *response*, not the *query window* —
  wallet selection by margin (pnl/vlm) clears the floor.
- Sandbox blocks `./notify "$(cat ...)"` arg-passing — stage to
  `.pending-notify/` and let post-run step deliver (used by 12+ skills).
- Sandbox blocks Reddit (datacenter IP) and X.AI authed curl — use prefetch.
- Cost profile is cache-dominated (73% of spend). defi-overview, heartbeat,
  reppo-digest = 38% of weekly Opus spend; Sonnet rotation could cut ~$55-65/wk.
- Memory consolidation: topic-file detail, MEMORY.md is the index.
- Vote slot can be blocked by agent's own mint cadence — when current-epoch
  is owned entirely by your own prior mints, "AND is NOT one you just
  minted" reads as "0 vote targets". Worth a SKILL.md tighten on whether
  to LIKE-vote own mints or stay neutral.

## Recent Articles
| Date | Title | Topic |
|------|-------|-------|
| 2026-05-30 | code-health (weekly) | meta / fleet health |
| 2026-05-30 | skill-freshness audit | meta / fleet health |
| 2026-05-29 | skill-freshness audit | meta / fleet health |
| 2026-05-28 | weekly-shiplog (week 1) | meta / fleet health |
| 2026-05-28 | how the reppo agent swarm runs on aeon (explainer) | docs |
| 2026-05-28 | thread-formatter (PR #32 phantom-skill diagnosis) | meta |
| 2026-05-25 | cost-report (week 1) | meta / fleet health |
| 2026-05-25 | security-scan bootstrap | meta / fleet health |
| 2026-05-25 | weekly-review (week 1 baseline) | meta / fleet health |
| 2026-05-24 | skill-evals bootstrap baseline | meta / fleet health |
| 2026-05-21 | last30 — bitcoin (30d) — stale | crypto |
