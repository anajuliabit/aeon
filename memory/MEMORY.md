# Long-term Memory
*Last consolidated: 2026-06-05*

## About This Repo
Aeon — autonomous agent on GitHub Actions via Claude Code. 41 enabled
standalone skills + chains. Inbound messaging via Telegram. soul/
populated 2026-05-25 (ana voice). Reppo-swarm ledger: **17 mints + 32
votes** on-chain through 2026-06-05 (3-mint single-day record set 6-05).
Phase 2 (Pinata pin + platform POST) end-to-end clean **8+ consecutive
days** since 2026-05-30.

## Current Goals
- **ISS-009 sub-task (b): chain-runner `continue` → `break` flip.**
  Sub-task (a) shipped PR #69 2026-06-03 23:00Z. Workflow-level abort
  at `aeon.yml:479-493` fail-fast branch still pending. **8 days clean**
  since 2026-05-30. Codify before contributor reintroduces Write-tool
  overwrite anti-pattern.
- **Trading-agent: codify spot_pct threshold + Sharpe-vs-pnl tiebreak.**
  Two follow-ups surfaced from 2026-06-05's 3-mint day. (a) 15th-mint
  4a9a582a admitted 0xecb63caa at 11.55% spot via perp-only filter
  vs 10th-mint precedent which had rejected the same wallet at ~20%
  spot — formalize threshold in `skills/reppo-trading-agent/SKILL.md`
  Step 4.2. (b) 17th-mint e2e925b2 tiebreak picked LINK (Sharpe 3782,
  +$9,605) over runner-up AAVE (Sharpe 3421, +$14,615) under cap=1; an
  alternate "max absolute pnl" rule would have selected AAVE — formalize
  selection criterion in Step 4. Both are operator decisions.
- **ISS-016 own_pod_ids prefetch repair.** Prefetch count=0 for 15
  consecutive voter runs. Ledger wallet-shortcode workaround **fired live
  on the active epoch** for the first time 2026-06-05 (re-run filtered
  pod 583; 3rd-run filtered pods 583 + 585 in same pass). Workaround
  durability proven under load — prefetch repair priority drops.
- **15 unassigned reppo datanets** (1, 2, 4–8, 10, 11, 13–18).
  Orchestrator surfaces every run for 16+ days. Datanet 18 ArAIstotle
  surfacing 5 consecutive days. Needs operator assignment rubric or pick.
- **INDEX bookkeeping flips queued.** ISS-007 (PR #13/#26 merged),
  ISS-010 (PR #32 merged), ISS-013 (8+ consecutive pin successes),
  ISS-014 (8+ consecutive HTTP 200 incl. today's 3 mints). 4
  resolved-not-closed entries clutter open-issue counter (real open = 4,
  INDEX shows 6).
- **on-chain-monitor / defi-monitor watches.yml.** Both at NO_CONFIG
  2 consecutive days (6-04 + 6-05); operator to populate
  `memory/on-chain-watches.yml` with label/address/chain/type/threshold
  entries before either skill produces signal.
- **Cleanup chain-runner scratch.** `.tmp-*`, `.candidates.json`,
  `build_dataset.{js,py,jq}` stubs at repo root. Sandbox blocks `rm`
  mid-run — needs a postprocess cleanup step.
- **Chain-state-flip anomaly carry.** 2026-06-02 12:23Z `chain:reppo-swarm`
  flipped `last_status=failed` while `gh run view` confirmed workflow
  success. **7 clean chain cycles since** (6-03 × 3, 6-04 × 2, 6-05 × 2).
  Likely step-level writer recording transient failure that
  `on_error:continue` skips past. Under ISS-010 scope.

## Completed Goals (since last reflect 2026-06-04)
- **Trading-agent 11-run dry streak ENDED 2026-06-05.** Three mints in
  one day — 15th 4a9a582a (0xecb63caa 821 HFT closes 14.69 min, 70
  markets, +$7,500 Sharpe 1351 tx 0xdb5b7bbc), 16th 16671d6f (0x944b5f7d
  29 SOL+BTC 9.548s cluster, +$8,410 **Sharpe 48,523** = 2nd-highest
  ever tx 0xef7ce963), 17th e2e925b2 (0x781e95fd 201 LINK 2.88h, +$9,605
  Sharpe 3782 tx 0xa86b8dca). New single-day record (surpasses 3-mint
  days 5-29 and 5-30). Operator-knob blocker (perp-only prefetch /
  HL_MIN_VLM_USD / HL_WINDOW) no longer on critical path — margin-top-12
  cohort had rotated wholly vs 6-04's saturated shape.
- **ISS-016 ledger workaround proven durable on active epoch 2026-06-05.**
  Re-run defensively filtered pod 583 (own 15th-mint); 3rd-run filtered
  pods 583 + 585 (own 15th + 16th) in same pass.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers,
  open issues, lessons, skill health.
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit
  (17 mints, 32 votes).
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

**2026-06-05 watchlist state:** REPPO −6.75% (3rd consecutive red, fade
eases from prior day's −18.46% d/d), GITLAWB −0.25% (cooldown post
−26% trip, 3-day cumulative still −34% off 6-01), MAMO **−9.60% d/d 3rd
consecutive accelerating** (-6.11/-7.16/-9.60% 6-03→6-05, watch 15%
rail trip 6-06), WELL −6.67%. Detail + 6-04 twin-trip history in
[crypto.md](topics/crypto.md).
