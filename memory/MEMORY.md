# Long-term Memory
*Last consolidated: 2026-06-23*

## Current Goals
- **Sandbox-truncation systemic** — ISS-019/020/021 (defi-overview, token-pick, search-skill) extended 6-21 by ISS-022/023/024 (monitor-polymarket, token-alert, skill-health). 8 critical + 19 degraded share `output_tokens=0` signature. Root-cause + durable fix needed; rate-limit alone doesn't explain cluster timestamps 12:14-14:17Z.
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16. As of 6-21 daily-routine uses WebSearch fallback successfully (no 400). Caches still warm for agent-buzz; quota top-up still pending operator.
- **Operator action: on-chain config completion** — `memory/on-chain-watches.yml` now seeded with 5 Base wallets (good), but: (a) defi-monitor needs `type: pool` / `type: position` entries with ABIs, not wallets; (b) Etherscan v2 free tier blocks Base — need `ALCHEMY_API_KEY` or `ETHERSCAN_API_KEY` to lift `ON_CHAIN_DEGRADED`.
- **Stuck skills** — `deal-flow` (13d, since 6-08), `fork-cohort` (7d, 2nd Sun fail), `token-alert` NEW mid-dispatch hang (6-21 13:45Z, 96 min), `chain:investment-advisor` failed 6-08 (off table).
- **skill-freshness FRESHNESS_WARN** — operator-scorecard depends on stale articles/skill-analytics-*.md (264h/11d old, weekly 192h threshold). Next refresh due tonight 18:30 UTC.
- **BTC hard levels** — Both reclaim 63,500 (6-11) and 65,900 (6-15) triggered. Daily close < $60,500 still arms downtrend continuation alert.
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16, blocking 10+ XAI-dependent skills. Await next billing cycle or operator top-up. *[BLOCKED — operator top-up pending since 6-16; tweet-roundup/agent-buzz still routing to WebSearch fallback as of 6-21]*
- **Operator-gated monitors** — `on-chain-monitor` and `defi-monitor` await `memory/on-chain-watches.yml` seed (>14 days). *[BLOCKED — partial progress 6-21: 5 wallet entries seeded, but on-chain-monitor degraded (Etherscan free-tier blocks Base) and defi-monitor still NO_CONFIG (no pool/position entries)]*
- **Stuck skills** — `deal-flow` (13 days), `fork-cohort` (2nd consecutive Sunday failure), `security-digest` intermittently dispatched. *[ON TRACK — `deal-flow` ran clean 6-22 (8 deals, DEAL_FLOW_OK), `token-alert` recovered 6-22 12:39Z (ISS-023 closed), `fork-cohort` recovered 6-21 Sunday cycle. Chronic tail rolls up to sandbox-truncation goal]*
- **BTC hard levels** — Reclaim 63,500 (6-11) and 65,900 (6-15) both triggered; daily close < $60,500 downtrend alert armed. *[ON TRACK — `btc-levels` ran 13:09Z + 16:51Z 6-21; spot $64,021, no alerts fired]*
- **Sandbox-truncation systemic** — ISS-019/020/021 baseline extended 6-21 by ISS-022/023/024 (monitor-polymarket, token-alert, skill-health); cost-report joined cluster 6-22 (cf=3, output_tokens=0 signature). 28 degraded skills share signature per 6-21 skill-health snapshot. Durable fix needed; rate-limit alone doesn't explain.
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16. WebSearch fallback covers daily-routine, tweet-roundup, narrative-tracker (6-22 via prefetch cache). Operator top-up still pending. *[BLOCKED — 6 days]*
- **Operator on-chain config** — `memory/on-chain-watches.yml` seeded with 5 Base wallets. defi-monitor needs `type: pool` / `type: position` entries; on-chain-monitor needs `ALCHEMY_API_KEY` or `ETHERSCAN_API_KEY` (Etherscan v2 free tier blocks Base, Alchemy key empty). on-chain-monitor 6-22 ran OK via Blockscout keyless but 0 events on slow multisigs in 2400-block window. *[BLOCKED — partial]*
- **BTC hard levels** — Reclaim 63,500 (6-11) and 65,900 (6-15) triggered. Daily close < $60,500 still arms downtrend continuation alert. 6-22 spot range $63.9k–$64.9k, daily close $63,231.

## Recently Cleared
- **MemoClaw soul-strip PR landed 6-22 15:08Z** — PR #137 "soul: remove MemoClaw — dead project" merged. soul/SOUL.md + soul/examples/good-outputs.md scrubbed (projects, worldview, build-philosophy, vault-architecture rename, 7 sample shorts/mediums/long-forms). Goal closed by goal-tracker 6-23.
- **token-alert ISS-023 recovered 6-22 ~12:39Z** — clean run after 19h stuck-dispatch (6-21 13:45Z → 6-22 08:33Z heartbeat). REPPO +5.49% / GITLAWB +9.66% / watchlist median +1.83% (first green-median since 6-14).
- **deal-flow recovered 6-22 ~14:30Z** — clean DEAL_FLOW_OK after ~14d stuck since 6-08. 8 deals kept, Baseten $1.5B Series E top.
- **fork-cohort recovered 6-21 19:33Z** — Sunday cycle ran clean (100% sr on 1 run).
- **PR backlog cleared** — 0 open PRs as of 6-22 14:37Z (#112/#122/#127 merged or closed since 6-19).
- **Sandbox-truncation systemic** — ISS-019/020/021 (defi-overview/token-pick/search-skill) baseline → extended 6-21 by ISS-022/023/024 (monitor-polymarket/token-alert/skill-health) → cost-report joined cluster 6-22 as ISS-025 critical. ISS-025 cf escalated 6→7→18→23 across 6-22 evening + 6-23 morning/afternoon ticks (`outputTokens=12` variant of the family). 28+ degraded skills share `output_tokens=0` signature. **Durable fix needed at workflow `aeon.yml` capture step or usepod response shape; rate-limit alone doesn't explain.**
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16 (7 days BLOCKED). WebSearch fallback covering daily-routine, tweet-roundup, narrative-tracker (6-22 + 6-23 via prefetch cache). XAI primary still working for cached prefetch paths (list-digest 6-23 cache hit, agent-buzz 6-23 cache hit, narrative-tracker 6-23 cache hit). Operator top-up pending.
- **Operator on-chain config** — `memory/on-chain-watches.yml` seeded with 5 Base wallets (5 days now). defi-monitor still NO_CONFIG day 16 (needs `type: pool` / `type: position` entries). on-chain-monitor green via Blockscout keyless but `ALCHEMY_API_KEY len=0` + `ETHERSCAN_API_KEY null` + `COINGECKO_API_KEY len=0` — 2400-block window too narrow for slow Safe multisigs, needs operator to widen default or supply Alchemy key.
- **MemoClaw soul-strip PR pending** — operator declared MemoClaw dead 6-22; soul/SOUL.md + soul/examples/good-outputs.md edited to remove all MemoClaw references (worldview, projects, current-focus, pet-peeve, 7 sample shorts/mediums/long-forms). PR drafting per CLAUDE.md "never push directly to main".
- **BTC hard levels** — Reclaim 63,500 (6-11) and 65,900 (6-15) both triggered. Daily close < $60,500 still arms downtrend continuation alert. **6-23 BTC dropped to $62,038–$64,037 intraday on risk-off cascade (Kospi -10% circuit breakers, $500M crypto liqs, Warsh hawkish repricing)** — closer to but not yet through $60,500 trigger.

## Recently Cleared
- **6-22 recoveries that stuck:** `token-alert` clean 6-22 12:39Z + 6-23 13:12Z (ISS-023 closed, fired GITLAWB -15.63% rail-break first downside trip in 4d); `deal-flow` clean 6-22 14:30Z after 14d stuck (DEAL_FLOW_OK); `fork-cohort` Sunday cycle 6-21 19:33Z.
- **PR backlog cleared** — 0 open PRs as of 6-23 14:05Z (`gh pr list` empty for 4th consecutive check).
- **skill-freshness FRESHNESS_WARN** still hot — operator-scorecard depends on stale `articles/skill-analytics-*.md` (312h/13d old 6-23, weekly 192h threshold). Fingerprint d522755e unchanged since 6-21; re-emits 2026-06-28 if still unresolved.

## Fleet Health Overview
- **Skill-health last snapshot 6-22 19:08Z:** 9 healthy · 27 degraded · 4 warning · 1 critical (cost-report) · 2 no_data. Systemic flag: sandbox-truncation `output_tokens=0` cluster.
- **Heartbeat 6-23 14:05Z: 🔴 DEGRADED.** Chronic-failure tail of 22 skills sr<0.5 (worst: reg-monitor 7%, vuln-scanner 7%, skill-analytics 9%, security-digest 17%, list-digest 25%, narrative-tracker 26%). cost-report joins at 12% with cf=23.
- **Open issues: 14** (4 critical sandbox cluster — ISS-019/020/021/025 + 7 high + 3 medium). 13 resolved historically.
- **chain:investment-advisor** failed 6-08, off status table per spec (long-standing).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PR history, blockers, skill-health patterns through 6-23.
- [Crypto research](topics/crypto.md) — Narrative evolution, token picks (DEXE added 6-23), watchlist alerts through 6-23.
- [Market context](topics/market-context.md) — 6-23 snapshot: regime **risk-off (high conviction)**, BTC $62,055 -4.66%, F&G 23 (lagging), breadth 3/20 green 24h.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage tracker since 6-16.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~193 chains as of 6-23 09:00Z pulse.

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | $0.00358962 +2.38% 6-24 (small bounce on 0.06× vol — near-zero tape, no reclaim of 6-19 $0.00370 pivot) |
| MAMO    | mamo               | 15%           | $0.00797785 +0.65% 6-24 (holds sub-$0.008 after 6-23 -7.65% rinse, baseline vol 1.03×) |
| REPPO   | reppo              | 15%           | $0.02335656 +2.91% 6-24 (recovers ~⅓ of 6-23 -9.75% leg on 0.53× vol; still net +36.0% from 6-19 base) |
| GITLAWB | gitlawb            | 15%           | $0.00005658 -6.04% 6-24 (follow-through fresh local low day after 6-23 rail break; -34.3% from 6-15 top) |

## Recent Patterns & Issues
- **Token pick 6-23 DEXE HIGH 7/10 $22.98** — DAO-governance rotation, only large-cap green on risk-off day (BTC -6.6% / ETH -8.3% 7d). KCEX listing + "Dexelization" DAO-Studio framing + $1.7B platform TVL. mcap $1.08B (rank 65), vmc 0.09 just under gate. Score: 24h+1, 7d+1, both>5%+2, RS vs BTC/ETH+2, DEX+1 = 7/10. Risk: 51.5% supply locked (FDV/mcap 2.1×) Q4 unlock cliff; intraday wick mirrors June 3 $24.49 reversal. Exit: target $28 / inv $19 / 14d. Market: Israel×Hezbollah-peace-deal-by-July-31 at 16.5¢ YES (sell YES / buy NO at 83.5¢) — fair ~6%, edge 10.5pp.
- **EIGEN 6-22 pick at invalidation 6-23.** EIGEN -15.3% morning / -17.0% afternoon TRENDING+DOWN — reverses 6-22 HIGH 9/10 pick at $0.305, est ~$0.258 (at/near $0.26 invalidation). One-day reversal of restaking → AI-infra narrative pivot; SSV Network TVL -38.95% 7d confirms restaking sector derisked.
- **Narrative-tracker 6-23:** 12 actionable post-dedup (vs 6-22's 15). **5 NEW** (US pro-crypto policy "Bitcoin built in America" framing, AI-displaces-crypto attention meta, BTC+AI synergy, AI capex rationing contrarian-bear, Chinese AI > US contrarian) + **1 PROMOTED** (DePIN/GPU compute Rising→Peak with named slate IO/TAO/AKT) + **2 DEMOTED** (AI Agents × RWA Peak→Rising, Ownership tokens FRONT-RUN→WATCH) + **2 DEAD** (L1 vs AI wars, Meme 3.0) + **3 CONSOLIDATED**. 3 reflexivity flags + 1 carry-over: (1) AI-displaces-crypto meta = reflexive trade itself, (2) "Bitcoin built in America" pure framing, no bill text, (3) **INVERSE — AI capex rationing** (Tencent + Uber real fundamentals catching the AI-infra story), (4) Kaito Yapper EOL carry-over. 9 of 12 threads AI-side = rotation signal hardening.
- **AIXBT Pulse 6-23 09:00Z:** 6 NEW (Warsh hawkish repricing, BTC crash <$62K + $500M liqs, Solana $40 bear call + KOL skepticism, institutional receipt stack Cboe/Ripple/UBS/Allfunds, protocol unwind cluster Synthetix/ENS/Sonic, SpaceX-led tech selloff). Bridge call: Warsh + DXY executing into BTC order book — $500M liq is macro reading into on-chain leverage.
- **Market regime 6-23: risk-off (high conviction).** BTC $62,055 (-4.66% 24h, -6.54% 7d), ETH $1,649 (-6.48%), F&G 23 (lagging — doesn't yet capture today's action). Breadth collapsed 13/20 → 3/20 green in one session. Triggers: Korea Kospi -10% circuit breakers (Samsung/SK Hynix -10-12%), $500M crypto liqs, Warsh hawkish Fed repricing, JPMorgan $165B Q2-end equity rebalancing. Top narrative: RWA (Rain +10.6% sole top-20 outlier). Polymarket sports-only **day 3** (no crypto-macro).
- **defi-overview 6-23:** Mixed — DEX vol $6.02B (+45% 1d on sell-off volume spike, 7d still -17%), TVL $71.85B (chain delta API regression day 6, vs $73.6B 6-22 = -$1.75B nominal). Real-yield count 301 cleared (vs 6-22's 3, 6-21's 0 — yields data quality fully recovered). Top: WETH-USDT uniV3 ETH 37.6% apyBase. Aave V3 fees +31% / TVL -4% 7d (real lending demand). Stables $313.8B (+0.03%); DAI +8.5% on $4.85B = ~$380M new mint (real, crypto-backed peg expansion).
- **on-chain-monitor 6-23 13:25Z:** ON_CHAIN_OK — 5/5 watches, **8 surviving events ≥$1k** across W1/W2/W3. **PHISHING DETECTED W3:** Cyrillic `ÚSDС` (Ú+С lookalikes) 1480 fake-units → address that visual-clones W1 (first/last bytes match, middle byte-swap), **fires 3 min after legit W3→W1 $1480 USDC** — textbook mirroring attack. Plus 2x `EṬH` lookalike spam + Jetchua airdrop. Operator notified + explainer sent via Telegram.
- **unlock-monitor 6-22 still hot 6-24:** NEWT 139.58M tokens = **64.9% of circulating supply** on $11M mcap, supply ~doubles tomorrow. H unlock LIVE 6-23 (investor tranche post-$36M exploit, H -28.5% 24h confirms unlock selling).
- **Token-movers 6-23 afternoon capitulation deepened.** 13/100 green (vs 19/76 morning), median -4.79% (vs -2.1%). EIGEN -17.0% [TRENDING+DOWN] 2nd-day reversal. Trending list 13/15 red = capitulation not chase. AERO direction-flip TRENDING+UP morning → TRENDING+DOWN afternoon.
- **search-skill 6-23 "llm cost" query** returned 0 installs — all 5 catalog hits failed hard gates (PostHog-coupled / playbook-not-cron / board-locked). Note: cost-report failure is sandbox-truncation (ISS-025), not capability gap. Right fix path is root-cause, not external swap.
