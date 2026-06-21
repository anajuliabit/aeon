# Long-term Memory
*Last consolidated: 2026-06-21*

## Current Goals
- **Sandbox-truncation systemic** — ISS-019/020/021 (defi-overview, token-pick, search-skill) extended 6-21 by ISS-022/023/024 (monitor-polymarket, token-alert, skill-health). 8 critical + 19 degraded share `output_tokens=0` signature. Root-cause + durable fix needed; rate-limit alone doesn't explain cluster timestamps 12:14-14:17Z.
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16. As of 6-21 daily-routine uses WebSearch fallback successfully (no 400). Caches still warm for agent-buzz; quota top-up still pending operator.
- **Operator action: on-chain config completion** — `memory/on-chain-watches.yml` now seeded with 5 Base wallets (good), but: (a) defi-monitor needs `type: pool` / `type: position` entries with ABIs, not wallets; (b) Etherscan v2 free tier blocks Base — need `ALCHEMY_API_KEY` or `ETHERSCAN_API_KEY` to lift `ON_CHAIN_DEGRADED`.
- **Stuck skills** — `deal-flow` (13d, since 6-08), `fork-cohort` (7d, 2nd Sun fail), `token-alert` NEW mid-dispatch hang (6-21 13:45Z, 96 min), `chain:investment-advisor` failed 6-08 (off table).
- **skill-freshness FRESHNESS_WARN** — operator-scorecard depends on stale articles/skill-analytics-*.md (264h/11d old, weekly 192h threshold). Next refresh due tonight 18:30 UTC.
- **BTC hard levels** — Both reclaim 63,500 (6-11) and 65,900 (6-15) triggered. Daily close < $60,500 still arms downtrend continuation alert.

## Fleet Health Overview
- **Skill-health classification (6-21 18:55Z): 9 critical · 19 degraded · 3 warning · 2 no-data · 9 healthy.** Major regression from "41 healthy / 0 degraded" stable baseline (6-12 → 6-19) — driven by sandbox-truncation systemic + accumulating cron-state denominators.
- **Heartbeat 6-21 15:22Z: 🔴 DEGRADED.** Chronic-failure tail expanded from 11 to **24 skills** with success_rate < 0.5. Worst: reg-monitor 7%, vuln-scanner 7%, skill-analytics 9%, security-digest 16%, list-digest 22%.
- **Open issues: 13** (3 critical sandbox + 7 high + 3 medium).
- **PR backlog: 0 open** (#112 / #122 / #127 all merged or closed since 6-19 — clean delta).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PR history, blockers, skill-health patterns through 6-21 inc. sandbox-truncation systemic.
- [Crypto research](topics/crypto.md) — Narrative evolution, token picks (AERO + SOL added 6-21), tracked-token alert history through 6-21.
- [Market context](topics/market-context.md) — 6-21 18:47Z snapshot: risk-on recovery (BTC $63,986 +0.91%, breadth 14/20 recovered from 7/20).
- [Capital‑2× program](topics/capital-2x-program.md) — North-star spec.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage tracker since 6-16.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 46 clusters tracked, ~250 chains indexed (both stable).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | Stable, -2.88% 6-19 |
| MAMO    | mamo               | 15%           | Stable, -0.35% 6-19 |
| REPPO   | reppo              | 15%           | Both-direction trips: +18.93% (6-14), -15.78% (6-16); -8.52% 6-19 consolidation |
| GITLAWB | gitlawb            | 15%           | Downtrend extending; -10.61% 6-19, -13.48% near-miss 6-17 |

## Recent Patterns & Issues
- **Sandbox-truncation cluster (6-21 12:14-14:17Z):** systemic `output_tokens=0` across 8 critical skills extending ISS-019/020/021 pattern. ISS-022 (monitor-polymarket), ISS-023 (token-alert mid-dispatch hang), ISS-024 (skill-health 26 consecutive failures, 0.26 sr).
- **PR backlog cleared.** 0 open PRs as of 6-21 15:22Z heartbeat (vs 2 stalled on 6-19).
- **Market regime 6-21:** risk-on recovery — BTC $63,986 +0.91%, breadth 14/20 green (recovered from 7/20 on 6-20). F&G 23 flat. BoJ 6-25 + Iran oil are next catalysts.
- **Recent token picks:** AERO (6-21) $0.5406 HIGH 7/10 Base DEX; SOL (6-21 re-fire) $73.47 HIGH 7/10; HYPE (6-20) $71.06.
- **Narrative tracker 6-21:** 15 actionable (consolidated from 27 on 6-15). 2 FRONT-RUN (AI Agents × RWA, Onchain AI Agents × Compute), 6 RIDE, 5 WATCH, 1 FADE, 1 IGNORE.
- **AIXBT Pulse 6-21:** 5 NEW (MEV exploit, RWA sector growth, Hyperliquid OI, Fed explicit hold, waterway geopolitics).
- **Daily-routine 6-21 OK:** Token-movers (LAB +26.9%, JUP +12.4%, AERO +10.0%), paper-pick ContextRL (arXiv 2606.17053), tweet-roundup via WebSearch.
- **defi-overview 6-21:** Mixed — TVL $58.3T flat, DEX vol $4.7B (-7.6% 1d, +26.6% 7d). yields=fail.
- **defi-monitor recovered:** running cleanly with empty pool/position watches (5 wallet watches handled by on-chain-monitor instead).
