# Long-term Memory
*Last consolidated: 2026-06-26*

## Current Goals
- **Sandbox-truncation systemic** — ISS-019/020/021/024/025 cluster (defi-overview, token-pick, search-skill, skill-health, cost-report). 20–22 chronic-tail skills sr<0.5 share `output_tokens=0` signature. Durable fix at workflow `aeon.yml` capture step still pending: action-converter flagged a 4.6/5-quality PR on 6-24 18:14Z, not opened yet (day 4 unshipped, surfaced in morning-brief 6-25 + 6-26).
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16 (day 11). WebSearch fallback covers daily-routine, tweet-roundup, narrative-tracker; XAI primary still works via prefetched paths (list-digest 6-26 cache hit, narrative-tracker 6-26 cache hit, agent-buzz 6-25 cache hit). Operator top-up pending. *[BLOCKED]*
- **Operator on-chain config** — `memory/on-chain-watches.yml` seeded with 5 Base wallets. defi-monitor still NO_CONFIG day 19 (needs `type: pool` / `type: position` entries). on-chain-monitor green via Blockscout keyless but `ALCHEMY_API_KEY len=0` + `ETHERSCAN_API_KEY null`. *[BLOCKED — partial]*
- **BTC breakdown CONFIRMED 6-26 05:02Z** — first qualifying close $59,712 < $60,500 fired the breakdown alert; reclaim flags re-armed (need close back > $60,500 to disarm; > $63,500 / $65,900 for reclaim trips). 6-26 13:22Z spot tapped 21-month low $58,115, retesting $59–60.5k range; F&G 13 Extreme Fear 3rd consecutive day; $1.48B liquidation cascade + $10B options expiry today.

## Recently Cleared
- **AAVE 6-24 HIGH 8/10 pick worked** — $76.09 → $86.33 by 6-26 morning (+13.4%) on Kraken-stake-$385M-rumor live bid; [TRENDING+UP] day-3. Confirms Aave V3 fees day-3 reversal -0.1% → +21% → +36% 7d through 6-26.
- **SEI 6-25 HIGH 9/10 pick stopped out day 1** — entry $0.0584 → $0.0542 intraday 6-26 (-7.2%, hit invalidation). Giga 200K-TPS / EVM-migration / ETF / Xiaomi-wallet catalyst stack didn't survive the risk-off tape.
- **PR #138 merged 6-24 21:37Z** — goal-tracker header drift fix. Queue empty until PR #147 (advisor hard-risk-layer #140 impl) opened 6-26 12:44Z by operator — first of 7-issue advisor sprint (#139–#145 filed 6-25).
- **token-alert 7 clean CG days through 6-28** (ISS-023 closed 6-22) — no rail-break across WELL/MAMO/REPPO/GITLAWB; 6-28 watchlist green for first time since 6-22 (median +1.51%), GITLAWB ends 7-day red streak (+5.38%, first elevated-vol upside print 1.27× day-prior).
- **on-chain-monitor 6-26 quiet 24h** — zero raw events post-6-25 address-poisoning escalation (3 fake-W1 baits planted under W2/W4 by `0xC3236716…`, attacker iterated within 48h). Dust did not repeat; legitimate W1↔Morpho/W2/W4 activity also paused. `known-addresses.yml` seeded 6-25 (5 op wallets + Morpho GA1 + phishing infra).

## Fleet Health Overview
- **Skill-health 6-25 18:18Z snapshot:** 9 healthy · 27 degraded · 5 warning · 0 critical · 3 no_data (autoresearch, operator-scorecard, fork-skill-gap). Hash identical to 6-24 18:14Z — no movement in 24h. Sandbox-truncation `output_tokens=0` cluster carries; cost-report cf=0 holds since 6-24 03:48Z recovery (sr 10% structural).
- **Heartbeat 6-26 09:19Z + 14:05Z: 🔴 DEGRADED** — fleet cf=0 across all 42 dispatched; chronic-failure tail 20 skills sr<0.5 (defi-monitor flipped to exactly 50%, leaves cluster). Worst: vuln-scanner 7% / reg-monitor 10% / cost-report 10% / skill-analytics 11% / security-digest 20% / list-digest 29% / search-skill 29% / narrative-tracker 30% / skill-health 31%.
- **Open issues: 14** (4 critical sandbox cluster ISS-019/020/021/025 + 7 high + 3 medium). 13 resolved historically.
- **PR backlog: 1 open** — PR #147 advisor risk-layer opened 6-26 12:44Z, within 24h stall threshold.
- **chain:investment-advisor** failed 6-08, off status table per spec (long-standing).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PR history, blockers, skill-health patterns.
- [Crypto research](topics/crypto.md) — Narrative evolution, token picks (APE 6-26 HIGH 9/10 fresh, AAVE 6-24 +13.4% day-3 holding, SEI 6-25 stopped out day 1), Morpho curator-risk + operator leverage-freeze guidance, watchlist alerts.
- [Market context](topics/market-context.md) — 6-26 snapshot: risk-off deepening (conviction high), BTC $59,081 / 21-month low $58,115, PCE 4.1% 3-yr high killed rate-cut pricing, F&G 13 Extreme Fear; breadth 4/20 24h.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage tracker since 6-16 (day 11).
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-26 09:00Z (somnia added). Key: $270B stablecoin float + lower yields = rotation fuel stacked, BTC ETF $696M outflow + Micron +15% = AI conviction bifurcating by asset class.

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | $0.00340074 +1.10% 6-28 (2nd consecutive green, vol $72K = 0.05× mean — weakest vol print of 2026 watchlist run) |
| MAMO    | mamo               | 15%           | $0.00788301 +0.96% 6-28 (2nd consecutive green after 6-day low extension; holds above $0.00785, vol 0.87× mean) |
| REPPO   | reppo              | 15%           | $0.02106098 +1.92% 6-28 (3rd consecutive green, reclaims $0.02 with bid thinning vol 0.29×; net +22.7% from 6-19 base) |
| GITLAWB | gitlawb            | 15%           | $0.00005011 +5.38% 6-28 (1st green after 7-day red streak; reclaims $0.00005; first elevated-vol upside print 1.27× day-prior) |

## Recent Patterns & Issues
- **Today's 6-26 12:25Z token-pick APE HIGH 9/10 $0.151** — Yuga Labs ecosystem control 6-5, ApeMars staking 63% APY 6-19, Hyperliquid $1M whale 5x long; only sub-rank-200 large-cap green on red tape (+11.4% 24h / +19.3% 7d). Exit $0.185 / inv $0.131 / 14d. Market: SKIPPED (only 4 markets clear $50k vol post-football, no defensible ±10% fair value).
- **NEW STRUCTURAL META-BEAR 6-26: "Crypto needs new narrative"** (@KobeissiLetter + @AliMartinez) — H1 close BTC -32% / ETH -47% / MSTR -43% + 46-day Coinbase Premium negative + $2.92B ETF outflows 6w + USDT dominance +43% to 9.17%. **BREAKS the 24h-bear-half-life pattern** by being backed by structural data not narrative chop. Watch 6-27/28 for persistence. Stablecoins PROMOTED 4→5 ↑ Peak Bull (USDT dominance shift IS the reflexive output). 4 RIDE narratives still hold: AI agent infra, RWA, stablecoins, prediction markets — 4-day structural-longs streak.
- **defi-overview 6-26:** DEX vol +4.5%, Uniswap V4 ties V3 share ($706M ≈ $707M, V3 day-1 share leak). **Aave V3 fees +36% / TVL -4% 7d on $11.6B** (day-3 reversal -0.1→+21→+36, real lending demand) + Morpho Blue +62% fees day-3 carry from +89%. **Invesco USTB -16.66% day-2 unwind ($749M→$623M, cumulative -28%/-$223M 48h, RWA Eth/Sol/Plume)** = institutional Treasury-product liquidation matching BlackRock $257M-to-Coinbase pattern. **APXUSD broke peg to $0.71, APYUSD to $0.97** — small-cap yield-USD wrapper sector unwind day-3. Yesterday's 42.2% USDC-AERO incentive cooled to 39.3%, AERO -9.1% gave the bid back.
- **security-digest 6-26:** **2 net-new KEV adds** breaks 6-25's zero cadence — Cisco Unified CM SSRF CVE-2026-20230 (EPSS 0.512 PoC-live = 2nd ≥0.5 EPSS PATCH-TODAY of 2026) + PTC Windchill unauth-RCE CVE-2026-12569 (CISA due 6-28). **Go x/crypto/ssh 9-CVE coordinated drop 6-25** incl CVSS-10 CVE-2026-46595 re-opening the 2024 CVE-2024-45337 callback-skip surface (every Go SSH server with non-publickey callbacks exposed → ≥0.52.0). **leo-sdk supply chain expanded 5×** (3→15 packages, full leo-connector + rstreams-* + serverless-leo namespace = full-namespace burn requiring credential rotation).
- **Operator advisor Q&A 6-26 (Telegram):** clarified Morpho-Blue $11.2k MORPHO bag = passive HOLD pending DefiLlama 7d fee verification (<$50k weak / >$500k re-evaluate). cbBTC/USDC leverage-freeze = no new collateral / no margin until LLTV drops 0.86→<0.80; operator pushed back on collateral-add — response: F&G 12 + BTC pinned to $60,500 breakdown = doubling down on leveraged BTC, pay down USDC instead (same LTV drop, no new BTC exposure). Re-add at LTV<0.80 AND BTC reclaim >$63,500.
- **list-digest 6-26 quiet day** — top signal: DefiIgnas surfaced uni-v4 hooks + Spark lenders as LPs primitive (Spark = Sky/MakerDAO subDAO; uni-v4 production-rolling = lending-protocol depositors absorbing AMM throughput risk). NEW DeFi composability pattern worth tracking if it recurs.
- **search-skill 6-26 SEARCH_SKILL_NO_GAP day 3** — fleet capability-complete on external-skill axis at 192 installed skills (8 security/audit-shaped). Failures are infra (ISS-025 capture step), not gaps. Stop noise-filing new gap reports unless cron-state failure mode changes.
