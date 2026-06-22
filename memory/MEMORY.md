# Long-term Memory
*Last consolidated: 2026-06-22*

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
- **MemoClaw soul-strip PR pending** — Operator declared MemoClaw a dead project 6-22; soul/SOUL.md + soul/examples/good-outputs.md edited to remove all MemoClaw references (projects, current-focus, worldview, build-philosophy, pet-peeve, vault-architecture rename, 7 sample shorts/mediums/long-forms). PR drafting to land on main per CLAUDE.md "never push directly".
- **BTC hard levels** — Reclaim 63,500 (6-11) and 65,900 (6-15) triggered. Daily close < $60,500 still arms downtrend continuation alert. 6-22 spot range $63.9k–$64.9k, daily close $63,231.

## Recently Cleared
- **token-alert ISS-023 recovered 6-22 ~12:39Z** — clean run after 19h stuck-dispatch (6-21 13:45Z → 6-22 08:33Z heartbeat). REPPO +5.49% / GITLAWB +9.66% / watchlist median +1.83% (first green-median since 6-14).
- **deal-flow recovered 6-22 ~14:30Z** — clean DEAL_FLOW_OK after ~14d stuck since 6-08. 8 deals kept, Baseten $1.5B Series E top.
- **fork-cohort recovered 6-21 19:33Z** — Sunday cycle ran clean (100% sr on 1 run).
- **PR backlog cleared** — 0 open PRs as of 6-22 14:37Z (#112/#122/#127 merged or closed since 6-19).

## Fleet Health Overview
- **Skill-health 6-21 18:05Z: 9 healthy · 28 degraded · 3 warning · 0 critical · 2 no_data.** Major regression from 41-healthy baseline (6-12 → 6-19) driven by sandbox-truncation cluster. Notable: critical skills cleared after recent successes (e.g. token-alert recovery 6-22).
- **Heartbeat 6-22 14:37Z: 🔴 DEGRADED.** Chronic-failure tail: 22 skills sr<0.5. Worst: reg-monitor 7%, vuln-scanner 7%, skill-analytics 9%, security-digest 16%, list-digest 24%, narrative-tracker 25%. cost-report joins at 50% with new failure (extends ISS-019/020/021/024).
- **Open issues: 13** (3 critical sandbox + 7 high + 3 medium).
- **chain:investment-advisor** failed 6-08, off status table per spec.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PR history, blockers, skill-health patterns through 6-22.
- [Crypto research](topics/crypto.md) — Narrative evolution, token picks (EIGEN added 6-22), watchlist alerts through 6-22.
- [Market context](topics/market-context.md) — 6-22 16:00Z snapshot: regime chop (low conviction), BTC $64,938 +1.52%, F&G 20 (Extreme Fear, ↓3 from 23), breadth 13/20 green 24h · 6/20 7d.
- [Capital‑2× program](topics/capital-2x-program.md) — North-star spec.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage tracker since 6-16.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters tracked (down from 46 on 6-21), ~250 chains indexed.

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | $0.00376527 -1.84% 6-22, stable downtrend |
| MAMO    | mamo               | 15%           | $0.00855576 -1.34% 6-22, stable |
| REPPO   | reppo              | 15%           | $0.02505217 +5.49% 6-22 (+45.91%/3d reversal of 6-16 trip) |
| GITLAWB | gitlawb            | 15%           | $0.00007087 +9.66% 6-22 (first green since 6-12 downtrend) |

## Recent Patterns & Issues
- **Token pick 6-22 EIGEN HIGH 9/10 $0.305** — EigenCloud rebrand + Darkbloom Public Alpha (600M+ tokens on Apple silicon, 30-200% perf). 7d +42.93% outperforms BTC -1.47% / ETH +1.56% by ~44pp. Risk: 7-01 $8M unlock + uncapped supply + Q1 revenue collapse.
- **Narrative-tracker 6-22:** 15 actionable (transitions: 5 NEW + 1 PROMOTED + 2 DEMOTED + 4 DEAD + 4 CONSOLIDATED). 4 reflexivity flags including **1 inverse-reflexivity** (stablecoins/x402 — 480k agents / $50M cumulative / +265% weekly = real infrastructure, fundamentals catching story). **Structural shift:** Kaito killed Yapper leaderboard 2026-01-15; replaced w/ Studio + Attention Markets (Polymarket joint) — mindshare measurement layer shifted from points-driven to prediction-market-driven.
- **AIXBT Pulse 6-22 10:00Z:** 7 NEW (Toss Bank Solana PoC, SOL tokenized stock vol, security cluster Taiko/Aztec/Altura, BTC ETF $6.35B, China +1T yuan, Treasuries 4.48% retreating, TradFi flip hawkish→easing).
- **Market regime 6-22 16:00Z:** chop (low conviction) — BTC $64,938 +1.52%, F&G 20 (↓3 to Extreme Fear), breadth weekly 6/20 downtrend dominant. EigenCloud/AI-infra restaking top rising narrative.
- **defi-overview 6-22:** Mixed — TVL $73.6B (chain delta API regression day 5), DEX vol $4.2B (-10.8% 1d, -9.1% 7d). Top mover Dolomite +14% (7d +56% lending inflows). 3 real-yield pools recovered (WSOL-USDC 32.4%, WETH-USDT 25.1%, UNI-WETH 17.3%) vs 6-21's 0.
- **unlock-monitor 6-22:** NEWT crisis — 139.58M tokens = **64.9% of circulating supply** on $11M mcap, supply ~doubles 6-24. Plus H (post-$36M-exploit) + SAHARA tier events.
- **weekly-shiplog 6-22:** 58 commits / 58 PRs (down from 113/109 week prior); +3,300/−3,920 first net-negative-lines week (20-skill prune #473).
- **search-skill 6-22:** Found UNTRUSTED candidate `davila7/claude-code-templates:vulnerability-scanner` — pure-python OWASP checklist sidesteps semgrep/trufflehog/osv-scanner binary gap (ISS-018 sandbox block). Manual operator install required.
- **fetch-tweets 6-22:** Empty signal — Grok flagged "WOOD"/"mamo" as overbroad (matched soccer player Chris Wood, surnames, Portuguese betting). Recommend tightening to `$WOOD`/`$MAMO` or pairing w/ project context.
