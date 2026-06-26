# Long-term Memory
*Last consolidated: 2026-06-25*

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
- **Sandbox-truncation systemic** — ISS-019/020/021/024/025 cluster (defi-overview, token-pick, search-skill, skill-health, cost-report). 22 chronic-tail skills sr<0.5 share `output_tokens=0` signature; cost-report ISS-025 is `outputTokens=12` variant. **Durable fix needed at workflow `aeon.yml` capture step or usepod response shape.** action-converter flagged a fix PR at 4.6/5 quality on 6-24 18:14Z; not yet opened.
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16 (day 10). WebSearch fallback covers daily-routine, tweet-roundup, narrative-tracker; XAI primary still works for prefetched paths (list-digest 6-25 cache hit, narrative-tracker 6-25 cache hit). Operator top-up pending. *[BLOCKED]*
- **Operator on-chain config** — `memory/on-chain-watches.yml` seeded with 5 Base wallets. defi-monitor still NO_CONFIG day 18 (needs `type: pool` / `type: position` entries). on-chain-monitor green via Blockscout keyless but `ALCHEMY_API_KEY len=0` + `ETHERSCAN_API_KEY null`. *[BLOCKED — partial]*
- **BTC hard levels** — Reclaim 63,500 (6-11) and 65,900 (6-15) both triggered. 6-24 daily close $60,909 above $60,500 threshold. **6-25 16:39Z spot dipped to $59,317 (sub-$60,500) → reclaim flags re-armed**. Today's UTC close is the binary signal: close <$60,500 fires breakdown alert next run.

## Recently Cleared
- **skill-freshness FRESHNESS_WARN cleared 6-25** — skill-analytics ran 6-24 Wednesday, resolving operator-scorecard stale-dep (`articles/skill-analytics-*.md` was 336h/14d old). 6-25 skill-freshness verdict: FRESHNESS_OK.
- **AAVE token-pick 6-24 HIGH 8/10 worked** — $76.09 entry → $81.99 by 6-25 morning (+7.7%), trending #1 carry day 2 in red tape. Skill required fresh catalyst to re-pick — passed today, picked SEI instead.
- **reg-monitor 6-24 14:55Z clean** — first end-to-end success with all 4 primary sources delivering (sr was 7%). Top item: CFTC v. Kentucky (9th-state preemption lawsuit). Worth watching for sustained recovery.
- **PR #138 merged 6-24 21:37Z** — goal-tracker header drift fix. Open-PR queue now empty.

## Fleet Health Overview
- **Skill-health 6-24 18:14Z snapshot:** 9 healthy · 27 degraded · 5 warning · 0 critical · 3 no_data (autoresearch, operator-scorecard, fork-skill-gap). Cost-report recovered cf=28→0 at 6-24 03:48Z; sr still 10% (ISS-025 structural). Systemic flag: sandbox-truncation `output_tokens=0` cluster.
- **Heartbeat 6-25 08:43Z + 14:53Z: 🔴 DEGRADED** — no fresh cf≥3 today. Chronic-failure tail of 22 skills sr<0.5 unchanged: vuln-scanner 7% / reg-monitor 10% / cost-report 10% / skill-analytics 11% / security-digest 19% / list-digest 28% / search-skill 29% / market-context-refresh 30% / narrative-tracker 30% / skill-health 30%, etc. Fleet at cf=0 across the board today.
- **Open issues: 14** (4 critical sandbox cluster — ISS-019/020/021/025 + 7 high + 3 medium). 13 resolved historically.
- **PR backlog:** 0 open.
- **chain:investment-advisor** failed 6-08, off status table per spec (long-standing).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PR history, blockers, skill-health patterns.
- [Crypto research](topics/crypto.md) — Narrative evolution, token picks (SEI 6-25, AAVE 6-24 +7.7% worked), Morpho curator-risk lessons, watchlist alerts.
- [Market context](topics/market-context.md) — 6-25 snapshot: regime **risk-off** (conviction high), BTC $61,147 −2.0%, F&G 12 (Extreme Fear deepening); breadth 4/20 (back to 6-23 crash-day lows); Seoul AI stocks −10% cascade new macro catalyst.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage tracker since 6-16.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~193 chains as of 6-25 09:00Z pulse. Key: HYPE FDV>SOL + Solana DEX $883M, RLUSD Japan + credit union stablecoin pilots, MIM/MemeCore/STRC reflexivity failure cluster, $72K options max pain Friday (dealers short gamma, pinning price).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | $0.00337204 -3.44% 6-26 (pinned at fresh local low, no follow-through to 6-25's -5.95% leg; vol 0.34× 5-day mean) |
| MAMO    | mamo               | 15%           | $0.00755086 -3.15% 6-26 (drips below $0.0076, 6-day continuous low extension; vol 1.23× 5-day mean — highest absolute vol of window) |
| REPPO   | reppo              | 15%           | $0.01998087 -5.24% 6-26 (loses $0.02 handle to fresh leg low; still net +16.4% from 6-19 base) |
| GITLAWB | gitlawb            | 15%           | $0.0000487 -10.27% 6-26 (6th consecutive red day, fresh local low; closest to 15% rail at 473bp slack; -43.4% from 6-15 top) |

## Recent Patterns & Issues
- **Today's token-pick 6-25 SEI HIGH 9/10 $0.0584** — Live catalyst stack (Giga upgrade 200K-TPS target, EVM migration mid-June, Canary Staked SEI ETF SEIZ live, Xiaomi wallet preinstall) on strongest RS print in top 250: +8.83% on BTC -2.7%/ETH -2.8% red tape. Exit $0.069 / inv $0.054 / 14d. Market pick: "BTC dip to $57,500 in June" YES 26¢ MEDIUM (fair ~35%, 9pp edge); resolves 2026-07-01.
- **Morpho curator-risk lesson (operator query 6-24)** — Alpha USDC Delta V2 (curator AlphaPing) collapsed 6-20: ~30% concentrated in single msY/USDC market; msY crashed 70-85%; 100% utilization froze withdrawals; ~$18M trapped. AlphaPing had discontinued collateral verification *before* collapse. **General principle: Morpho Blue protocol underwrites markets, curator underwrites concentration — single-market obscure-collateral + verification-lapsed curator = textbook failure.** Safer curators: Gauntlet, Steakhouse, MEV Capital. Safer no-curator alts: Aave V3 USDC, Sky USDS.
- **Narrative-tracker pattern 6-25:** 24h annihilation of every bear/contrarian frame from 6-24 — CLARITY Act, Hedgeye macro-quad4, Saylor critique, BTC-dominance-cracking, privacy-coins/ZK all DEAD inside 24h. Pattern hardened: **24h half-life for reactive bear narratives, multi-day life for structural longs.** 4 NEW Rising rotation frames today (prediction markets, selective-liquidity slate, asset-specific fundamentals, value-accruing tokens). Two NEW reflexive named-slate publications (NOIRSINGULARIS TAO/WLD/HYPE/ONDO/PENDLE + ct_hoppy BNB/JUP/HYPE/AERO) — HYPE in BOTH = double-bid risk. 0 FRONT-RUN 2nd consecutive day.
- **defi-overview 6-25:** DEX vol +24% rebound ($7.74B, top-3 all up — opposite of 6-24 dispersion). NAVI Lending +53% TVL (Sui, $80M→$123M, new name). Mellow Core -22.77% full unwind of 6-23's +34% pop. USDC-AERO incentive yield **doubled in 24h** (25.2% → 42.2%, biggest single move tracked). crvUSD day-3 burn-down (-10.25% on $210M, ~$22M redemption). Aave V3 fees +21% / TVL -3% 7d (reversal flag — was -0.1% 6-24).
- **security-digest 6-25:** 48 net-new npm malware in 48h post-6-24 dedup. Two coordinated campaigns: 9× HubSpot-developer typosquat cluster (`@su-doughnym/*` + helper packages targeting hubspot.com integration plugins) + 3× LeoSDK family (leo-sdk/cron/logger). **Zero net-new KEV today** (first time this week — cadence pause after Monday's UniFi+Lantronix drop). OliveTin Go race CVE-2026-48708 only tracked-stack reviewed finding (CVSS 7.5).
- **on-chain-monitor 6-25 13:14Z address-poisoning escalation:** attacker contract `0xC3236716…` planted **3 fake-W1 baits** under W2/W4/W4 (lookalike `0x98E57e6799…`) — richer kit vs 6-23 single ÚSDС: zero-value REAL USDC + zero-value REAL CBBTC + cyrillic ÚSDС clone value-matched to legit $1,115 USDC. 2 signer EOAs. Live wallet activity also resumed: $7,105 cbBTC W1→Morpho, $6,641 W2→W1, $1,115 USDC W4→W1. **Seeded `memory/known-addresses.yml`** (5 op wallets + Morpho GeneralAdapter1 + phishing infra) — future runs auto-label. Mitigation: hardware-screen verify, never copy from "recent" tx history.
- **search-skill 6-25 SEARCH_SKILL_NO_GAP day 2** — no concrete capability word derivable from any of failing skills / open issues / MEMORY goals / 7d log signals. Streak continues — fleet capability-complete on external-skill axis, failures are infra not gaps.
