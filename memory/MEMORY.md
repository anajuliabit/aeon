# Long-term Memory
*Last consolidated: 2026-06-30*

## Current Goals
- **Sandbox-truncation systemic** — ISS-019/020/021/024/025 cluster bleeds 19-skill chronic tail (`output_tokens=0`). Durable workflow `aeon.yml` capture-step fix still pending; action-converter flagged 4.6/5-quality PR on 6-24 18:14Z, **day 7 unshipped** (hard surface deadline weekly-review 2026-07-04).
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16 (**day 15**). Operator top-up pending. WebSearch fallback covers daily-routine/tweet-roundup/narrative-tracker; prefetched XAI paths still serve list-digest/agent-buzz/token-pick. *[BLOCKED]*
- **Operator on-chain config** — defi-monitor NO_CONFIG day 23; `memory/on-chain-watches.yml` needs `type: pool` / `type: position` entries. `ALCHEMY_API_KEY len=0`, `ETHERSCAN_API_KEY null`. *[BLOCKED — partial]*
- **BTC breakdown day 5 confirmed** — 6-29 close $60,160 = 5th consecutive sub-$60,500. Quarter-end TODAY 6-30 adds structural sell flow; tonight's UTC close decides 6th-red or reclaim. Reclaim levels: $63,500 / $65,900. Spot pinned $58.2k–$59.7k all day 6-30.

## Recently Cleared (last 48h)
- **WELL volume spike 3.83×** alerted 6-30 12:11Z — 7-01 close $0.00330605 = -1.02% (2nd red day), vol 2.30× (decaying). **Direction: supply-hitting-bid confirmed**, not accumulation — the "either/or" from 6-30 resolves bearish. One more sub-$0.0033 close = trend-follow signal.
- **github-trending 6-30 fake-star drop** — msitarzewski/agency-agents 119.8k stars / 1:6 fork ratio / Shell language for "AI agency" project = inorganic-star-farm. New precedent: drop with confidence on >100k Shell-language repos with anomalous fork ratios.
- **KEV zero-cadence streak ENDED at 4 days** — SimpleHelp CVE-2026-48558 added 6-29 (CVSS 10.0 + PoC + IOCs + CISA BOD 26-04 due 2026-07-02 = PATCH TODAY). Brandjacks now riding agent-infra narrative (ai-sdk-ollama, autotel-* 18-pkg cluster).
- **PR #150 fix(aeon.yml) opened 6-29 18:17Z** — rename `usepod_model` → `model:` for on-chain-monitor / token-pick / token-movers, ~$456/mo savings. 5-line diff by self-improve. Under 24h stall at 14:43Z 6-30 hb (~20h).

## Fleet Health
- **skill-health 6-29 17:45Z snapshot:** 9 healthy · 23 degraded · 8 warning · 0 critical · 2 no_data (operator-scorecard, fork-skill-gap). Hash 992a90ed; fleet-control dropped (disabled). 15 open issues, 0 filed/resolved this run. See [[fleet]] for chronic tail.
- **Open issues: 15** — 4 critical sandbox cluster (ISS-019/020/021/025) + 1 sandbox-limitation (ISS-018) + 7 high + 3 medium incl ISS-026 (heartbeat false-fail timing, action queued).
- **Open PRs: 2** — #149 docs(skill-graph) opened 6-28 17:15Z (**~45h+ stuck day 2**); #150 fix(aeon.yml) opened 6-29 18:17Z (under 24h stall but approaching).
- **fork-skill-digest STUCK ~44h+** carry — dispatched 2026-06-28T18:38Z, never resolved. Within 48h dedup window through 6-30 14:43Z hb; crosses threshold next tick.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PR history, blockers, skill-health, 6-30 entry (PR #150 fresh, WELL vol spike, github-trending fake-star precedent).
- [Crypto research](topics/crypto.md) — Narrative evolution, token picks (VELVET day-3 -12.8%, SLX day-3 +7.3%, AAVE day-7, APE day-4 invalidating, SEI stopped-out), Morpho curator-risk + operator leverage-freeze guidance, watchlist alerts, 6-30 BTC breakdown day-5 + WELL vol spike on red tape.
- [Market context](topics/market-context.md) — 6-30 snapshot: BTC $58.2–$59.7k pinned, breadth 45/100, F&G 18 day-5, quarter-end TODAY.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage tracker since 6-16 (**day 15**); PR #148 merged 6-29.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 21:00Z.

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | $0.00330605 -1.02% 7-01 (2nd consecutive red into July-open; 6-30 vol spike 3.83× decays to 2.30× today with a -1.02% close = **supply-hitting-bid confirmed**, not accumulation) |
| MAMO    | mamo               | 15%           | $0.00797508 +3.74% 7-01 (snaps 2-day red streak, reclaims $0.0079 — 1st green since 6-28; vol 1.08× baseline, participation-shallow bounce) |
| REPPO   | reppo              | 15%           | $0.02077600 -0.18% 7-01 (near-flat 2nd wobble on $0.021 line; vol 1.14× baseline, drought persists sub-$150K rail) |
| GITLAWB | gitlawb            | 15%           | $0.00004494 -7.36% 7-01 (worst 1d of watchlist run, $0.00005 handle rejected day-2, fresh 2026-window low; vol 1.02× baseline = orderly fade) |

## Recurring patterns (durable)
- **Meta-bear "crypto needs new narrative" persisting day 5** — broke 24h half-life day 3+4+5. Structural backing: BTC ETF outflow streak ($107.8B → $82.8B = −23% 6w, June worst month on record at $4-5B outflows incl IBIT $3.3B), F&G 18 day-5, breadth recovering 23/82 → 45/100 today. Quarter-end TODAY adds structural sell flow. STRUCTURAL longs persist (7-day streak): AI agent infra, stablecoins, RWA via CEX rails, prediction markets.
- **Brandjacking is the new default supply-chain vector** — security-digest 6-30: 0 reviewed-critical 4th day, 100% malware-driven. Attackers now ride agent-infra narrative (ai-sdk-ollama = Vercel AI SDK + Ollama brandjack; 18-pkg autotel-* OTel+MCP cluster in 10.5h window — largest single-namespace coordinated brandjack of 48h). 100% of 154 malware advisories npm; pip/crates/go contribute zero. Treat any hot-project SDK brandjack as default threat.
- **search-skill SEARCH_SKILL_NO_GAP day 7** — fleet capability-complete on external-skill axis. Failures are infra (ISS-025 capture step), not gaps. Stop noise-filing new gap reports unless cron-state failure mode changes.
- **operator-scorecard Mon 10:30Z slot perpetually MISSED** — scheduler-side never-run gap, flagged every Monday hb. Not skill-side. Carry indefinitely until scheduler patch.
- **Fake-star pattern** (new 6-30 precedent) — drop with confidence when: >100k stars + 1:6 (or worse) fork ratio + Shell language tag for non-shell project + unknown maintainer provenance. Anchored on msitarzewski/agency-agents drop, complements 6-28 anomalyco/opencode precedent.
