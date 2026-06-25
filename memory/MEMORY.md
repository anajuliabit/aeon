# Long-term Memory
*Last consolidated: 2026-06-24*

## Current Goals
- **Sandbox-truncation systemic** — ISS-019/020/021/024/025 cluster (defi-overview, token-pick, search-skill, skill-health, cost-report). 22 chronic-tail skills sr<0.5 share `output_tokens=0` signature; cost-report ISS-025 is `outputTokens=12` variant (cf=30→0 recovered overnight 6-24 03:48Z but sr still 10%, structural). **Durable fix needed at workflow `aeon.yml` capture step or usepod response shape; rate-limit alone doesn't explain.**
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16 (day 8). WebSearch fallback covers daily-routine, tweet-roundup, narrative-tracker; XAI primary still works for prefetched paths (list-digest 6-23/24 cache hit, agent-buzz 6-23 cache hit, narrative-tracker 6-23/24 cache hit). Operator top-up pending. *[BLOCKED]*
- **Operator on-chain config** — `memory/on-chain-watches.yml` seeded with 5 Base wallets (6 days). defi-monitor still NO_CONFIG day 17 (needs `type: pool` / `type: position` entries). on-chain-monitor green via Blockscout keyless but `ALCHEMY_API_KEY len=0` + `ETHERSCAN_API_KEY null` — 2400-block window too narrow for slow Safe multisigs. *[BLOCKED — partial]*
- **BTC hard levels** — Reclaim 63,500 (6-11) and 65,900 (6-15) both triggered. **6-24 16:38Z spot dipped to $60,319 (sub-$60,500) → both reclaim flags re-armed**. If today's UTC close < $60,500, breakdown alert will fire next run. Spot range 6-24 $60,319–$62,903.

## Recently Cleared
- **skill-freshness FRESHNESS_WARN cleared 6-25 ~06:00Z** — skill-analytics ran 6-24 Wednesday, resolving the operator-scorecard stale-dep that had persisted since 2026-06-21. skill-freshness 6-25 returned FRESHNESS_OK ("prior FRESHNESS_WARN cleared"). Fingerprint d522755e cycle complete; goal closed by goal-tracker 6-25.
- **cost-report cf=30→0 overnight 6-24 03:48Z** — weekly tick on `claude-sonnet-4-6` succeeded. Sr still 10%, ISS-025 cluster persists structurally. 6-24 cost-report normal weekly run also clean ($237.60 across 67 runs, −55.2% WoW — reppo cluster absent).
- **token-alert ISS-023 closed 6-22 12:39Z** — fired GITLAWB -15.63% rail-break 6-23 13:12Z (first downside trip in 4d), 6-24 12:09Z clean (3rd consecutive CG day post-recovery).
- **deal-flow recovered 6-22 14:30Z** — DEAL_FLOW_OK after 14d stuck (Baseten $1.5B Series E top).
- **fork-cohort recovered 6-21 19:33Z** — Sunday cycle ran clean.
- **MemoClaw soul-strip PR #137 merged 6-22 15:08Z** — soul/SOUL.md + good-outputs.md scrubbed (worldview, projects, 7 sample posts). Goal closed by goal-tracker 6-23.
- **EIGEN 6-22 pick stopped out 6-23 at invalidation $0.26** — 3rd consecutive day reversal through 6-24 (-6.7%). Restaking → AI-infra narrative effectively dead. SSV Network TVL -32.5% 1d / -38.95% 7d confirms restaking sector derisked.
- **reg-monitor 6-24 14:55Z clean** — first end-to-end success with all 4 primary sources delivering (sr was 7%). Top item: CFTC v. Kentucky (9th state lawsuit over prediction-market preemption). Worth watching for sustained recovery.

## Fleet Health Overview
- **Skill-health 6-23 18:38Z snapshot:** 9 healthy · 27 degraded · 5 warning · 1 critical (cost-report) · 2 no_data (operator-scorecard, fork-skill-gap). Systemic flag: sandbox-truncation `output_tokens=0` cluster (26 degraded skills share signature).
- **Heartbeat 6-24 08:44Z + 14:57Z: 🔴 DEGRADED** but no fresh cf≥3 today. Chronic-failure tail of 22 skills sr<0.5 unchanged: reg-monitor 7% / vuln-scanner 7% / skill-analytics 9% / cost-report 10% / security-digest 18% / list-digest 26% / narrative-tracker 27% / market-context-refresh 28% / search-skill 28%, etc.
- **Open issues: 14** (4 critical sandbox cluster — ISS-019/020/021/025 + 7 high + 3 medium). 13 resolved historically.
- **PR backlog:** 1 open (PR #138 goal-tracker header drift fix, ~24h old, under 24h stall threshold).
- **chain:investment-advisor** failed 6-08, off status table per spec (long-standing).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PR history, blockers, skill-health patterns through 6-24.
- [Crypto research](topics/crypto.md) — Narrative evolution, token picks (AAVE added 6-24), Morpho curator-risk lessons, watchlist alerts.
- [Market context](topics/market-context.md) — 6-25 snapshot: regime **risk-off** (conviction high), BTC $61,147 −2.0%, F&G 12 (Extreme Fear deepening); breadth 4/20 (back to 6-23 crash-day lows); Seoul AI stocks −10% cascade new macro catalyst.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage tracker since 6-16.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~204 chains as of 6-24 21:00Z pulse. Key: BTC sub-$60K (Saylor liquidation fear), Micron earnings 4× AI memory (demand intact), prediction markets $40B+pUSD$500M, EU MiCA July 1.

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | $0.00337693 -5.95% 6-25 (gives back 6-24 bounce, fresh local low; vol 1.50× 5-day mean) |
| MAMO    | mamo               | 15%           | $0.00778230 -2.75% 6-25 (slow drip below 6-23 rinse low, sub-$0.008 holding pattern) |
| REPPO   | reppo              | 15%           | $0.02094174 -10.29% 6-25 (closest to 15% rail with 471bp slack; still net +21.97% from 6-19 base) |
| GITLAWB | gitlawb            | 15%           | $0.00005408 -4.41% 6-25 (5th consecutive red day, fresh local low; -37.2% from 6-15 top) |

## Recent Patterns & Issues
- **Token pick 6-24 AAVE HIGH 8/10 $76.09** — DeFi blue-chip relief: trending #1 CG, only large-cap DeFi green 7d vs BTC -3.0% / ETH -4.9%. Grayscale 6-20 $175 fair-value target + V4 Tokenization Spoke security audit advancing on-chain securities-finance rails. Exit: target $87 / inv $69 / 14d.
- **Morpho curator-risk lesson (operator query 6-24 17:00Z)** — Alpha USDC Delta V2 (curator AlphaPing) collapsed 2026-06-20: ~30% concentrated in single msY/USDC market; msY crashed 70–85%; market at 100% utilization → withdrawals frozen; ~$18M trapped. AlphaPing had discontinued collateral verification *before* collapse. **General principle: Morpho Blue protocol underwrites markets, curator underwrites concentration — single-market obscure-collateral + verification-lapsed curator = textbook failure.** Safer curators: Gauntlet, Steakhouse, MEV Capital. Safer no-curator alts: Aave V3 USDC, Sky USDS.
- **Narrative-tracker 6-24:** 12 actionable (vs 6-23's 12, 6-22's 15). **First major BEAR-BTC thesis** (Hedgeye quad4) + **first btc-maxi internal contrarian** (Saylor critique). FRONT-RUN bucket emptied first time in 4 days (P2P mesh died). RESURFACED bucket appears (hyperliquid + BTC dominance back from DEAD/folded). Pattern: macro headwinds + internal-camp contrarianism on top of AI-side dominance.
- **NEWT unlock cliff TODAY (6-24)** — 139.58M tokens = **64.9% of circulating supply** on $11M mcap, supply ~doubles. H unlock LIVE 6-23 (investor tranche post-$36M exploit, H -28.5% 24h confirmed unlock selling, -16% 6-24 follow-through).
- **AIXBT Pulse 6-24 09:00Z:** 7 NEW (EF 20% staff cuts + Eth Labs, JPY stablecoin + US CBDC ban + Solana $380M tokenized equities, BTC extreme-fear/flow framing, Cardano SecondFi $20M+ exploit, Solana gaming titles update, Micron MU -13%, US-Iran interim MoU operationalized). Bridge call: EF cuts + Eth Labs Ethereum-governance surface change; settlement migration to Solana already running; Micron = AI demand thesis hitting supply-chain reality.
- **Market regime 6-24: chop** (oversold relief, not risk-on). BTC $62,442 (+0.48% 24h, -3.60% 7d), F&G 17 (catching up to 6-23 crash, not fresh deterioration), breadth recovered 3/20 → 10/20 green (neutral). **BTC ETF outflows $1.67B weekly / $4.21B over 3 weeks** = institutional derisking macro anchor (10yr sticky ~4.45%, SpaceX IPO crowding allocation).
- **security-digest 6-24:** Ubiquiti CVE-2026-34910 **EPSS 0.818 / p96** (highest of 2026, first EPSS≥0.5 PATCH TODAY trigger this year) + UniFi KEV trio (34908/909/910) + Lantronix EDS5000 CVE-2025-67038 KEV + 40 net-new npm malware drops in 48h (sustained ~20-22/day velocity).
- **defi-overview 6-24:** xStocks TVL +19.6% today ($493M → $588M, RWA rotation signal). Aave V3 fees +31% / TVL -4% 7d (real lending demand). DAI dropped out of stable top-5, replaced by USD1/WLFI (structural shift toward Trump-affiliated issuer).
- **on-chain-monitor 6-25 13:05Z address-poisoning escalation:** same attacker contract `0xC3236716…` planted 3 fake-W1 baits under W2/W4/W4 (lookalike `0x98E57e6799…`) using a richer kit vs 6-23: zero-value REAL USDC + zero-value REAL CBBTC + cyrillic ÚSDС clone (value matched to the legit $1,115 USDC). 2 signer EOAs. Live wallet activity also resumed: $7,105 cbBTC W1→Morpho GeneralAdapter1, $6,641 cbBTC W2→W1, $1,115 USDC W4→W1. **Seeded `memory/known-addresses.yml`** (5 op wallets + Morpho + phishing infra) — future runs auto-label. Mitigation unchanged: hardware-screen verify, never copy from "recent" tx history.
- **search-skill 6-24 SEARCH_SKILL_NO_GAP** — no concrete capability word from any of (a) failing skills [all 22 chronic-tail at cf=0 today, all sandbox-truncation signature, infra not capability gap], (b) open issues, (c) MEMORY.md goals, (d) 7d log signals. Streak continues — fleet capability-complete on external-skill axis, failures are infra not gaps.
