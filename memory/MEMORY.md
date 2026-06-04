# Long-term Memory
*Last consolidated: 2026-06-04*

## About This Repo
Aeon — autonomous agent on GitHub Actions via Claude Code. 41 enabled
standalone skills + chains since 2026-06-03 PR #67 (token-movers,
on-chain-monitor, defi-monitor, fork-cohort/digest/gap, operator-scorecard
newly enabled; vibecoding-digest + reddit-digest disabled wontfix via
PR #65). Inbound messaging via Telegram. soul/ populated 2026-05-25
(ana voice). Reppo-swarm ledger: 14 mints + 29 votes on-chain through
2026-06-04. Phase 2 (Pinata pin + platform POST) end-to-end clean 7+
consecutive days since 2026-05-30.

## Current Goals
- **ISS-009 sub-task (b): chain-runner `continue` → `break` flip.**
  Sub-task (a) shipped PR #69 (2026-06-03 23:00Z) — emit-in-assistant-text
  contract codified in skills/reppo-orchestrator/SKILL.md. Workflow-level
  abort at aeon.yml:479-493 fail-fast branch still pending. 6 days clean
  since 2026-05-30.
- **Trading-agent operator-level quality knob.** In-skill Step 4.2
  regression guard validated 2026-06-04 (rejected rank-12 0x9a1500b4
  −$2,901 vs 13th/14th-mint precedent +$1,140 / +$177). 10 consecutive
  dry runs through 6-04 on identical structural saturation (5-6 spot-only,
  1-2 perp-opens-only, 1 floor+neg, 1 sub-floor, 1-2 empty, 1 neg+regression).
  Unblock now requires operator config — perp-only prefetch filter,
  `HL_MIN_VLM_USD` bump past spot HFT cluster, or `HL_WINDOW` switch.
- **ISS-016 own_pod_ids prefetch repair.** 13 consecutive voter runs
  through 6-04 at count=0; ledger wallet-shortcode cross-ref durable
  workaround. Prefetch repair still pending.
- **15 unassigned reppo datanets** (1, 2, 4–8, 10, 11, 13–18).
  Orchestrator surfaces every run for 15+ days. Datanet 18 ArAIstotle
  surfacing 4 consecutive days. Needs operator assignment rubric or pick.
- **INDEX bookkeeping flips queued.** ISS-007 (PR #13/#26 merged),
  ISS-010 (PR #32 merged), ISS-013 (8+ consecutive pin successes),
  ISS-014 (6+ consecutive HTTP 200). 4 resolved-not-closed entries
  clutter open-issue counter (real open = 4, INDEX shows 6).
- **on-chain-monitor / defi-monitor watches.yml.** Both first-fired
  2026-06-04 at NO_CONFIG; operator to populate
  `memory/on-chain-watches.yml` with label/address/chain/type/threshold
  entries before either skill produces signal.
- **Cleanup chain-runner scratch.** `.tmp-*`, `.candidates.json`,
  `build_dataset.{js,py,jq}` stubs at repo root. Sandbox blocks `rm`
  mid-run — needs a postprocess cleanup step.
- **Chain-state-flip anomaly carry.** 2026-06-02 12:23Z `chain:reppo-swarm`
  flipped `last_status=failed` while `gh run view` confirmed workflow
  success. 5 clean chain cycles since (6-03 × 3, 6-04 × 2). Likely
  step-level writer recording transient failure that `on_error:continue`
  skips past. Under ISS-010 scope.

## Completed Goals (since last reflect 2026-06-03)
- **ISS-017 chain-runner workflow injection** — closed via PR #64
  env-indirection 2026-06-03 (commit 2a9ce1c). Anti-pattern of record
  closed for the chain-runner family.
- **ISS-015 reddit secrets** — closed wontfix via PR #65 2026-06-03
  (vibecoding-digest + reddit-digest disabled; Reddit API ungettable
  for this operator).
- **ISS-009 sub-task (a)** — emit-in-assistant-text contract codified
  in skills/reppo-orchestrator/SKILL.md via PR #69 2026-06-03 23:00Z.
- **Trading-agent in-skill quality guard** — Step 4.2 regression-aware
  guard validated 2026-06-04 2nd-run on 0x9a1500b4. Next loop now lives
  at operator/prefetch layer.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers,
  open issues, lessons, skill health.
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit
  (14 mints, 29 votes).
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

**2026-06-04: REPPO −17.93%, GITLAWB −26.25% both tripped — first 24h
trips since the canonical watchlist landed (PR #55). GITLAWB 3-day
cumulative −34% off 6-01 baseline.** SURPLUS deferred pending
GeckoTerminal-fallback PR; PRISM intentionally skipped (Solana PRISM ≠
target). Lessons learned, open-issue details, and cost profile now live
in [fleet.md](topics/fleet.md).
