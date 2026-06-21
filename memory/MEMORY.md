# Long-term Memory
*Last consolidated: 2026-06-21*

## Current Goals
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16, blocking 10+ XAI-dependent skills. Await next billing cycle or operator top-up.
- **Operator-gated monitors** — `on-chain-monitor` and `defi-monitor` await `memory/on-chain-watches.yml` seed (>14 days).
- **Stuck skills** — `deal-flow` (13 days), `fork-cohort` (2nd consecutive Sunday failure), `security-digest` intermittently dispatched.
- **PR backlog** — #112 skill-graph docs (~6 days), #122 self-improve fix (~3 days).
- **BTC hard levels** — Reclaim 63,500 (6-11) and 65,900 (6-15) both triggered; daily close < $60,500 downtrend alert armed.

## Fleet Health Overview
- **Enabled skills:** 41 healthy, 0 degraded/flapping, 2 no_data (`operator-scorecard`, `fork-skill-gap` awaiting first weekly tick).
- **Recent runs:** Most daily skills recovered from 6-12 weekly-limit wave. Critical sandbox failures filed (ISS-019/020/021).
- **System status:** 🔴 DEGRADED per heartbeat due to stuck skills (`deal-flow` 13d, `fork-cohort` 7d, `security-digest` 5h, `heartbeat` 4h).
- **Skill quality:** `defi-overview`, `token-pick`, `search-skill` show consecutive failure patterns (sandbox timeouts).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — Full PR history, blocker chronology, skill health patterns.
- [Crypto research](topics/crypto.md) — Narrative evolution, token picks, tracked-token alert history.
- [Market context](topics/market-context.md) — Daily regime updates, DeFi TVL/volume trends, prediction market signals.
- [Capital‑2× program](topics/capital-2x-program.md) — North-star specification and implementation tracking.

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | Stable, -2.88% 6-19 |
| MAMO    | mamo               | 15%           | Stable, -0.35% 6-19 |
| REPPO   | reppo              | 15%           | Both-direction trips: +18.93% (6-14), -15.78% (6-16) |
| GITLAWB | gitlawb            | 15%           | Near-miss -13.48% (6-17), -10.61% 6-19 |

## Recent Patterns & Issues
- **XAI quota exhaustion** (since 6-16): Affecting token-pick, agent-buzz, list-digest, refresh-x, remix-tweets, tweet-roundup, narrative-tracker, reply-maker, article, fetch-tweets.
- **Operator-gated monitors stuck**: `on-chain-monitor` & `defi-monitor` >14 days NO_CONFIG awaiting `memory/on-chain-watches.yml`.
- **Critical sandbox failures**: ISS-019 (defi-overview), ISS-020 (token-pick), ISS-021 (search-skill) — sandbox timeout/cost truncation.
- **Market regime**: Post-Hormuz peace deal cooling, BTC consolidating ~$64.5k. Both reclaim levels (63,500 on 6-11, 65,900 on 6-15) triggered.
- **Token alert activity**: REPPO ±15% trips (6-14 +18.93%, 6-16 -15.78%), GITLAWB -13.48% near-miss (6-17).
- **AIXBT Pulse**: 6-20 update showed 4 NEW items, 4 GONE items, bridge call on AI rotation + STRC depeg.
- **Recent token picks**: HYPE (6-20) $71.06 (+6.13% 24h, +22.07% 7d), JTO (6-16) $0.87 (+36.4% 24h).
- **Skill health snapshot** (6-19): 41 healthy, 0 degraded/flapping, 2 no_data (operator-scorecard, fork-skill-gap). Fleet status: 🔴 DEGRADED due to stuck skills.
