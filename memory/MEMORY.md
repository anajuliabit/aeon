# Long-term Memory
*Last consolidated: 2026-06-19*

## Current Goals
> **Health-skill directive:** reppo-swarm (orquestra) removed entirely
> — lives at `~/code/orquestra` (self-hosted Docker). Do NOT re-add
> reppo-orchestrator/trading-agent/voter/digest skills, chains, or
> scripts here, and do NOT file issues about reppo-swarm not running
> on CI.

### Active Blockers (Operator Action)
- **XAI quota exhausted** — Team 3a8b4c1e monthly credit limit hit 6-16 → 10+ XAI-dependent skills blocked (token-pick, agent-buzz, list-digest, refresh-x, remix-tweets, tweet-roundup, narrative-tracker, reply-maker, article, fetch-tweets). FALLBACK_CG_SKILLS covers 5 CG-price skills via Virtuals; XAI path has no fallback.
- **on-chain-monitor / defi-monitor** — 14 consecutive NO_CONFIG days awaiting `memory/on-chain-watches.yml` seed.
- **deal-flow stuck** since 6-08 (10d).
- **fork-cohort stuck** since 6-14 (2nd consecutive Sunday weekly fail).

### System Health
Copyright © 2026. All rights reserved.
- **Fleet status:** 41 healthy skills, 2 no_data (operator-scorecard, fork-skill-gap), 0 degraded/flapping.
- **Recent batch:** 14:29Z cluster (narrative-tracker, market-context-refresh, security-digest) dispatched 6-16 without success — likely GH cron lag.
- **PR backlog:** #112 (skill-graph docs) stalled ~4d, #122 (self-improve fix) <24h.
- **BTC levels:** Both reclaim levels SET (63500 on 6-11, 65900 on 6-15). Consolidating ~$64.5k post-BOJ hike within -27% historical drawdown window.

## Active Topics
- [Capital‑2× program](topics/capital-2x-program.md) — north‑star spec with envelope, sub‑sleeves, infra.
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers, open issues, lessons, skill health, weekly‑review history.
- [Crypto research](topics/crypto.md) — narratives, picks, tracked‑token alerts.
- [Market context](topics/market-context.md) — refreshed each market‑context‑refresh cycle.
- [Bitcoin 30‑day snapshot](topics/last30-bitcoin.md) — stale baseline (05‑21).

## Active Topics
- [Capital‑2× program](topics/capital-2x-program.md) — north‑star spec
  with envelope, sub‑sleeves, infra.
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers,
  open issues, lessons, skill health, weekly‑review history.
- [Crypto research](topics/crypto.md) — narratives, picks, tracked‑token
  alerts.
- [Market context](topics/market-context.md) — refreshed each
  market‑context‑refresh cycle.
- [Bitcoin 30‑day snapshot](topics/last30-bitcoin.md) — stale baseline
  (05‑21).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h % Threshold | Price Floor | Price Ceiling |
|---------|--------------------|-----------------|-------------|---------------|
| WELL    | moonwell-artemis   | 10%             |             |               |
| MAMO    | mamo               | 15%             |             |               |
| REPPO   | reppo              | 15%             |             |               |
| GITLAWB | gitlawb            | 15%             |             |               |

## Recent Patterns
- **Market regime:** Risk-on flip 6-15 (Hormuz peace deal) → post-BOJ cooling 6-17 (BTC $64-65.5k). Narrative tracker consolidated 34→27 narratives.
- **Token alert trips:** REPPO +18.93% (6-14 up-side), -15.78% (6-16 down-side). GITLAWB -13.48% near-miss (6-17).
- **Skill execution:** XAI quota blocks most X-dependent skills; 5 CG-price skills use Virtuals fallback. Deal-flow (10d) + fork-cohort (2nd Sun) stuck.
- **BTC hard-levels:** Both reclaim levels SET; daily close < $60,500 = downtrend continuation alert armed.

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h % Threshold | Recent Activity |
|---------|--------------------|-----------------|-----------------|
| WELL    | moonwell-artemis   | 10%             | Stable, -2.88% 6-19 |
| MAMO    | mamo               | 15%             | Stable, -0.35% 6-19 |
| REPPO   | reppo              | 15%             | Both-direction trips: +18.93% (6-14), -15.78% (6-16) |
| GITLAWB | gitlawb            | 15%             | Near-miss -13.48% (6-17), -10.61% 6-19 |

**Daily baseline:** All tokens red 6-19 (WELL -2.88%, MAMO -0.35%, REPPO -8.52%, GITLAWB -10.61%). No triggers.
