# Long-term Memory
*Last consolidated: 2026-06-28*

## Current Goals
- **Sandbox-truncation systemic** — ISS-019/020/021/024/025 cluster (defi-overview, token-pick, search-skill, skill-health, cost-report). 20-skill chronic tail sr<0.5 share `output_tokens=0` signature. Durable fix at workflow `aeon.yml` capture step still pending: action-converter flagged a 4.6/5-quality PR on 6-24 18:14Z, **day 5 unshipped** (surfaced in morning-brief 6-25 → 6-26 → 6-27 → 6-28, 4 consecutive without operator pickup).
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16 (day 13). WebSearch fallback covers daily-routine, tweet-roundup, narrative-tracker; XAI primary still works via prefetched paths (list-digest/narrative-tracker/agent-buzz/token-pick all cache-hit through 6-28). PR #148 fix(agent-buzz) addresses cache-quality (Latest→Top + min_likes:5); ~24h+ open as of 6-28 hb. Operator top-up pending. *[BLOCKED]*
- **Operator on-chain config** — `memory/on-chain-watches.yml` seeded with 5 Base wallets. defi-monitor still NO_CONFIG day 21 (needs `type: pool` / `type: position` entries). on-chain-monitor green via Blockscout keyless + curl→WebFetch fallback proved durable today; `ALCHEMY_API_KEY len=0` + `ETHERSCAN_API_KEY null`. *[BLOCKED — partial]*
- **BTC breakdown CONFIRMED day 3** — 6-27 close $59,943 = 3rd consecutive qualifying sub-$60,500 close (alert fired 6-28 01:21Z). Spot range 6-28 $59,596–$60,289 (afternoon dip back below $60k). Reclaim flags re-armed (need close back > $60,500 to disarm; > $63,500 / $65,900 for reclaim trips). Quarter-end rebalancing June 30 adds structural sell pressure to already-bearish tape.

## Recently Cleared
- **VELVET 6-28 HIGH 11/10 fresh pick $1.72** — Trade.xyz pre-IPO synthetic + Aerodrome routing + 11/10 score (only sub-rank-100 BREAKOUT day-3 holds on broad bear tape). Exit $2.20 / inv $1.32 / 10d pre-July-10 unlock (15% early-backer + 20% team vesting cliff).
- **SLX 6-27 HIGH 9/10 pick day-1 +13.8% on entry** ($0.4753 → $0.541 morning → $0.522 afternoon = +9.8% midday). Solana institutional delta-neutral, Binance trading event + listings.
- **AAVE 6-24 HIGH 8/10 pick day-5 +17.8% from entry** (gave back from peak +25.9% day-4 on profit-taking, still profitable).
- **APE 6-26 HIGH 9/10 pick day-3 -7.3% on entry** — invalidation tail extends; ApeMars / Hyperliquid-whale stack didn't survive meta-bear tape. Reconsider $0.131 stop trigger.
- **on-chain REPPO stake migration captured 6-28** — first non-zero on-chain-monitor run since 6-25 quiet thread (~72h). W3→W1 1.58M REPPO stake migration (W3 withdrew from staking contract `0xc81F...68E8`, transferred to W1, W1 re-staked) + W1 6,595 USDC → Morpho Steakhouse Prime Instant vault (steakUSDC). On-thesis institutional yield-vault accumulation; Steakhouse one of the trusted curators per Morpho lessons.
- **Watchlist whole-green day 6-28** (1st since 6-22) — token-alert TOKEN_ALERT_OK 7th consecutive clean CG day; median +1.51%; GITLAWB +5.38% ends 7-day red streak with first elevated-vol upside print 1.27× day-prior.

## Fleet Health Overview
- **Skill-health 6-27 18:10Z snapshot:** 9 healthy · 24 degraded · 8 warning · 0 critical · 2 no_data (operator-scorecard, fork-skill-gap). Diff vs 6-26: btc-levels + daily-routine degraded→warning (both crossed 0.6 sr line); −2 degraded. Hash 81dbbe4f changed, 24h cadence → notification fired. Sandbox-truncation `output_tokens=0` cluster carries day 11 since 6-19 first flag.
- **Heartbeat 6-28 09:18Z + 14:15Z: 🔴 DEGRADED** — fleet cf=0 across all 42 dispatched; chronic-failure tail 20 skills sr<0.5 (vuln-scanner 10% / reg-monitor 10% / cost-report 10% worst). defi-monitor 53% stays outside cluster (NO_CONFIG OK-path lifts sr).
- **Open issues: 15** (ISS-026 NEW 6-28 — heartbeat false-fail timing artefact, recommend moving skill-evals after 21:00 UTC; 4 critical sandbox cluster ISS-019/020/021/025 + 7 high + 3 medium). 13 resolved historically.
- **PR backlog: 1 open** — PR #148 fix(agent-buzz) opened 6-27 18:14Z, crossed 24h stall window as of 6-28 14:15Z hb.
- **chain:investment-advisor** failed 6-08, off status table per spec (long-standing).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PR history, blockers, skill-health patterns, 6-28 deltas.
- [Crypto research](topics/crypto.md) — Narrative evolution, token picks (VELVET 6-28 HIGH 11/10 fresh, SLX 6-27 +9.8% day-1, AAVE 6-24 +17.8% day-5, APE 6-26 -7.3% day-3, SEI 6-25 stopped-out), Morpho curator-risk + operator leverage-freeze guidance, watchlist alerts, 6-28 meta-bear day-3 + on-chain REPPO stake migration.
- [Market context](topics/market-context.md) — 6-28 snapshot: risk-off, breadth collapsed 18→6/20 post-opex bounce erased, BTC pinned $60K 4th day, F&G 18 Extreme Fear day-4, quarter-end rebalancing 2 days out.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage tracker since 6-16 (day 13); PR #148 fix-in-flight for cache quality.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 09:00Z. Key 6-28: CZ proposes BTC fork + Satoshi-coin freeze (governance attack on BTC immutability) + USD1 hits $4.7B = #3 stablecoin + tokenized equities pivot to CEX-led (Binance/Backpack/OKX) + Sui Seal MPC ships (agent-custody primitive).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | $0.00340074 +1.10% 6-28 (2nd consecutive green, vol $72K = 0.05× mean — weakest vol print of 2026 watchlist run) |
| MAMO    | mamo               | 15%           | $0.00788301 +0.96% 6-28 (2nd consecutive green after 6-day low extension; holds above $0.00785, vol 0.87× mean) |
| REPPO   | reppo              | 15%           | $0.02106098 +1.92% 6-28 (3rd consecutive green, reclaims $0.02 with bid thinning vol 0.29×; net +22.7% from 6-19 base) |
| GITLAWB | gitlawb            | 15%           | $0.00005011 +5.38% 6-28 (1st green after 7-day red streak; reclaims $0.00005; first elevated-vol upside print 1.27× day-prior) |

## Recent Patterns & Issues
- **Meta-bear "crypto needs new narrative" PERSISTED day 3 (6-28)** — broke 24h half-life rule for 2nd consecutive day, structurally backed: Bitcoin ETF 13-day net outflow streak (longest ever, total $107.8B → $82.8B = −23% 6w), F&G 18 day-4 Extreme Fear, breadth 18→6/20 post-opex bounce erased in one session. 0 FRONT-RUN 5 consecutive days. Regime locked; quarter-end rebalancing 6-30 likely adds Monday-open sell pressure. STRUCTURAL longs persisting 6-day streak: AI agent infra (Sui Seal MPC shipped 6-28 = custody primitive answer to mandate-vs-custody bear; Ondo+Virtuals+Treasures 430 tokenized stocks to 40k+ agents 6-27 = first RWA×agent product), stablecoins (USDT 9.17% dom + USD1 $4.7B = #3), RWA pivoting CEX-led (Binance/Backpack/OKX), prediction markets ($14.4B weekly Kalshi+Polymarket).
- **defi-overview 6-28: xStocks -59% 1d** ($579M → $235M) extends 3-day institutional Treasury/equity-wrapper unwind (Invesco USTB -28% 48h cumulative, Ethena USDtb -21% 6-27 = sector-wide redemption pressure). **Hyperliquid Perps fees -66% 1d reverses 6-27 HLP bid** (1-day reversal — HLP positioning transient). **Aave V3 fees day-4 fully unwound** (4-day arc: -0.1 → +21 → +36 → -35 → flat; lending spike was a 2-day burst, not regime).
- **security-digest 6-28: 0 net-new KEV adds 3rd consecutive day** (6-26/27/28 zero). 4 this-week items (Remark42 XSS / gonic Go playlist 3-CVE / mcp-memory-service OAuth scope / backpropagate auth-flag), 1 monitor (nebula-mesh CA-scoping bypass, no fix). EPSS top: Cisco CVE-2026-20230 slipped 0.512→0.417 (no longer clears 0.5 PATCH TODAY); Ubiquiti CVE-2026-34910 carry 0.786.
- **list-digest 6-28 quiet alpha day** — top reads: STRC solvency wobble (Strategy preferred-stock yield wrapper "flywheel stopped"; BTC-selling risk on $MSTR if discount holds; adjacent to btc-levels breakdown context); ETHFI re-rate (Flowslikeosmo flips dead-LRT consensus into 3-product financial-services stack); Prediction-markets $14.4B weekly Kalshi+Polymarket combined = RIDE narrative now cash-flow measurable not thesis.
- **agent-buzz 6-28 quiet builder day** — 6/10 kept across 3 clusters: MCP-as-inter-agent-standard (3 tweets, Google L3 spec endorsement + architectural authority-gap critique + security handbook); Agent runtime experiments (2 — meta-cognitive drift-calibration + DOM-affordance-vs-pixel control); General Intuition $320M gameplay-clip world-model raise (training-data bets).
- **paper-pick 6-28 OPID (On-Policy Skill Distillation for Agentic RL)** — directly load-bearing for operator's advisor sprint (#141 forced fine-grained probabilities + brier calibration, #142 net-of-cost paper grading, #145 momentum-chasing guardrail). Agent-self-trajectory distillation primitive.
- **github-trending 6-28 top pick: topoteretes/cognee** (RETURNING, 780 today / 24.3k total, persistent knowledge-graph memory for agents; v1.2.2 release 2026-06-26 drove the spike) — agent-infra primitive directly on-thesis with RIDE-narrative agent-infra cluster.
- **search-skill 6-28 SEARCH_SKILL_NO_GAP day 5** — fleet capability-complete on external-skill axis. Failures are infra (ISS-025 capture step), not gaps. Stop noise-filing new gap reports unless cron-state failure mode changes.
- **ISS-026 NEW (skill-evals 6-28 08:00Z)** — heartbeat false-fail missing_pattern because skill-evals dispatches BEFORE 08:00 UTC morning tick, capturing pre-tick stale state of log-based skills. Recommended fix: move skill-evals after 21:00 UTC. Action queued.
