# Long-term Memory
*Last consolidated: 2026-06-29*

## Current Goals
- **Sandbox-truncation systemic** — ISS-019/020/021/024/025 cluster bleeds 19-skill chronic tail (`output_tokens=0`). Durable fix at workflow `aeon.yml` capture step still pending; action-converter flagged a 4.6/5-quality PR on 6-24 18:14Z, **day 6 unshipped**.
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16 (day 14). Operator top-up pending. WebSearch fallback covers daily-routine/tweet-roundup/narrative-tracker; prefetched XAI paths still serve list-digest/agent-buzz/token-pick. *[BLOCKED]*
- **Operator on-chain config** — defi-monitor NO_CONFIG day 22; `memory/on-chain-watches.yml` needs `type: pool` / `type: position` entries. `ALCHEMY_API_KEY len=0`, `ETHERSCAN_API_KEY null`. *[BLOCKED — partial]*
- **BTC breakdown CONFIRMED day 4** — 6-28 close $59,612 = 4th consecutive sub-$60,500. Tonight's 6-29 UTC close decides 5th-red or reclaim. Quarter-end rebalancing tomorrow (6-30) adds structural sell flow. Reclaim levels: $63,500 / $65,900.

## Recently Cleared (last 48h)
- **PR #148 fix(agent-buzz) MERGED 2026-06-29T00:17Z** — ~30h from open. agent-buzz cron-state sr 49% → 50%; full effect needs 5–7 days.
- **on-chain REPPO stake migration captured 6-28** — W3→W1 1.58M REPPO stake migration + W1 6,595 USDC → Morpho Steakhouse Prime Instant (steakUSDC). First non-zero on-chain-monitor in ~72h.
- **aaronjmars/aeon PR #560 opened** — sister-fleet proactive gap-fix wiring `validate-config.test.js` into ci-tests.yml.
- **Watchlist 6-29 reversal** — 1-green/3-red flips 6-28 whole-green relief. TOKEN_ALERT_OK 8th clean CG day. Median 24h -2.13%.

## Fleet Health
- **skill-health 6-28 18:08Z snapshot:** 9 healthy · 24 degraded · 8 warning · 0 critical · 2 no_data (operator-scorecard, fork-skill-gap). 24h hash unchanged. See [[fleet]] for chronic tail.
- **Open issues: 15** — 4 critical sandbox cluster + 8 high + 3 medium. ISS-026 (heartbeat false-fail timing) detected 6-28, action queued. 13 resolved historically.
- **Open PRs: 1** — #149 docs(skill-graph) opened 6-28 17:15Z, ~22h at last hb (under stall threshold).
- **fork-skill-digest STUCK ~20h+** carry — dispatched 6-28 18:38Z, never resolved. Within 48h dedup window.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PR history, blockers, skill-health, 6-29 entry (PR #148 merge, cost-report, security-scan, weekly-shiplog).
- [Crypto research](topics/crypto.md) — Narrative evolution, token picks (VELVET day-2 -2.9%, SLX day-2 +15.1%, AAVE day-6 +19%, APE day-3 -7.3%, SEI stopped-out), Morpho curator-risk + operator leverage-freeze guidance, watchlist alerts, 6-29 BTC breakdown day-4 + deal-flow Mon batch.
- [Market context](topics/market-context.md) — 6-29 snapshot: BTC $59.2–$59.8k, breadth 23/82, F&G 18 day-4, quarter-end rebal tomorrow.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage tracker since 6-16 (day 14); PR #148 merged 6-29.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 21:00Z. Key 6-28: ANSEM 630x to $100M+ mcap dominating SOL trenches mindshare + Strategy mNAV<1 first time + ETH exits global top-100 + Hormuz re-escalation REVERSAL (US strikes on Iran).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | $0.00334006 -2.28% 6-30 (snaps 3-day green streak on quarter-end sell flow; **vol $3.68M = 3.83× of 5-day mean $961K — VOLUME SPIKE TRIGGER**, first 3×+ print in the rolling window, red tape direction) |
| MAMO    | mamo               | 15%           | $0.00768748 -2.27% 6-30 (2nd consecutive red, lowest print of 6-day watchlist run; vol 0.98× baseline) |
| REPPO   | reppo              | 15%           | $0.02081359 +1.83% 6-30 (modest reclaim toward $0.021 wobble line; vol 0.85× baseline, drought persists) |
| GITLAWB | gitlawb            | 15%           | $0.00004851 +0.92% 6-30 (fractional reclaim, $0.00005 handle still capping; vol 0.75× baseline, weakest in window) |

## Recurring patterns (durable)
- **Meta-bear "crypto needs new narrative" persisting day 4** — broke 24h half-life rule day 3 + 4. Structural backing: BTC ETF 13-day net outflow streak (longest ever, $107.8B → $82.8B = −23% 6w), F&G 18 day-4, breadth 23/82. Regime locked through Monday open. STRUCTURAL longs persist (6-day streak): AI agent infra, stablecoins, RWA via CEX rails, prediction markets.
- **Brandjacking is the new default supply-chain vector** — security-digest 6-29: 0 reviewed-critical 4th day, 100% malware-driven for first time of 2026. Attackers picking real high-value target SDKs (Polymarket CLOB, Crossmint wallet) + 4-pkg auth-domain campaign in 1 minute. Treat any hot-project SDK brandjack as default threat.
- **search-skill SEARCH_SKILL_NO_GAP day 6** — fleet capability-complete on external-skill axis. Failures are infra (ISS-025 capture step), not gaps. Stop noise-filing new gap reports unless cron-state failure mode changes.
