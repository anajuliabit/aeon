# Long-term Memory
*Last consolidated: 2026-07-01*

## Current Goals
- **Sandbox-truncation systemic** — ISS-019/020/021/024/025 cluster still bleeds a 19-skill chronic tail (`output_tokens=0`). Durable `aeon.yml` capture-step fix unshipped **day 8** since action-converter's 4.6/5-quality PR flag (6-24 18:14Z). Hard surface deadline: weekly-review **2026-07-04** (3d out).
- **PR #150 fix(aeon.yml) `usepod_model` → `model:`** — opened 6-29 18:17Z by anajuliabit, 5-line diff, ~$107/wk / $456/mo cost savings for on-chain-monitor / token-pick / token-movers. **~44h stall as of 7-01 14:13Z** — crossed 24h threshold on 6-30 evening, no merge action yet.
- **PR #149 docs(skill-graph)** — opened 6-28 17:15Z, **~69h stall day 3**. Operator-merge gated.
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16 (**day 16**). Operator top-up pending. WebSearch fallback covers daily-routine/tweet-roundup/narrative-tracker; prefetched XAI paths still serve list-digest/agent-buzz/token-pick. *[BLOCKED]*
- **Operator on-chain config** — defi-monitor NO_CONFIG day 24; `memory/on-chain-watches.yml` needs `type: pool` / `type: position` entries. `ALCHEMY_API_KEY len=0`, `ETHERSCAN_API_KEY null`. *[BLOCKED — partial]*
- **BTC breakdown day 6 CONFIRMED** — 6-30 close $58,551 = 6th consecutive sub-$60,500; 00:19Z alert fired. Tape pinned $58.2k–$59.8k through 7-01 12:18Z. First sub-$60k print since 2024, 50% below Oct-2025 $126k ATH. Tonight's UTC close decides 7th-red or reclaim ($63.5k / $65.9k).

## Fleet Health
- **skill-health 6-30 18:08Z snapshot:** 9 healthy · 23 degraded · 8 warning · 0 critical · 2 no_data (operator-scorecard, fork-skill-gap). Hash 1ff18e84; daily-cadence notify fired despite classification byte-identical to 6-29. 15 open issues, 0 filed/resolved. See [[fleet]] for chronic tail.
- **Open issues: 15** — 4 critical sandbox cluster (ISS-019/020/021/025) + 1 sandbox-limitation (ISS-018) + 7 high + 3 medium incl ISS-026 (heartbeat false-fail timing, action queued).
- **fork-skill-digest STUCK ~68h+** carry — dispatched 2026-06-28T18:38Z, never resolved. Crossed 48h dedup window; next Sunday 7-05 weekly tick will attempt fresh dispatch.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PR history, blockers, skill-health, 7-01 entry (PR #150 44h stall, PR #149 day-3 stall, BTC breakdown day-6, WELL vol-spike resolved bearish).
- [Crypto research](topics/crypto.md) — Narrative evolution, token picks (VELVET, SLX day-4 -3.6% unwinding, AAVE, APE invalidated, SEI stopped-out), Morpho curator-risk, watchlist alerts, 7-01 BTC breakdown day-6 + WELL supply-hitting-bid confirmed.
- [Market context](topics/market-context.md) — 7-01 snapshot: BTC $58.4k pinned day-6, breadth 32/100 (deteriorated from 45/100 yest), Anthropic ship day cluster (Sonnet 5 / Mythos export lift / stego-marking).
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage tracker since 6-16 (**day 16**); PR #148 merged 6-29.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 21:00Z.

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | $0.00330605 -1.75% 7-01 (2nd consecutive red; 6-30 vol spike 3.83× decayed to 2.30× on red close = **supply-hitting-bid confirmed**, not accumulation) |
| MAMO    | mamo               | 15%           | $0.00797508 +3.82% 7-01 (snaps 2-day red streak; 1st green since 6-28, vol 1.08× baseline = participation-shallow bounce) |
| REPPO   | reppo              | 15%           | $0.02077600 +0.03% 7-01 (wobbles $0.021 line 2nd day; vol 1.14× baseline drought persists sub-$150K rail) |
| GITLAWB | gitlawb            | 15%           | $0.00004494 -7.51% 7-01 (worst 1d of window, $0.00005 handle rejected day-2, fresh 2026-window low; vol 1.02× baseline = orderly fade) |

## Recurring patterns (durable)
- **Meta-bear "crypto needs new narrative" day 6** — broke 24h half-life days 3–6. Structural: BTC ETF outflow streak, F&G 18 day-5, breadth 45→32/100 (7-01 deteriorated), quarter-end de-grossing carried into July-open. STRUCTURAL longs persist (7-day streak): AI agent infra, stablecoins, RWA via CEX rails, prediction markets.
- **Brandjacking is the new default supply-chain vector** — 6-30 security-digest: 4th consecutive day 0 reviewed-critical, 100% malware-driven. Attackers now riding agent-infra narrative (ai-sdk-ollama, autotel-* 18-pkg cluster, LiveKit Agents, Confluent Kafka JS on 7-01 = 1st enterprise-data-infra target of wave). 100% of 154 malware advisories npm; pip/crates/go zero.
- **search-skill SEARCH_SKILL_NO_GAP day 8** — fleet capability-complete on external-skill axis. Failures are infra (ISS-025 capture step), not gaps. Stop noise-filing new gap reports unless cron-state failure mode changes.
- **operator-scorecard Mon 10:30Z slot perpetually MISSED** — scheduler-side never-run gap, flagged every Monday hb. Not skill-side. Carry indefinitely until scheduler patch.
- **Fake-star pattern** — drop with confidence when: >100k stars + 1:6 (or worse) fork ratio + wrong-language tag (Shell for AI project) + unknown maintainer provenance. Anchors: agency-agents (6-30 + 7-01), OmniRoute (7-01, TypeScript + rapid semver v3.8.42/139d + brand-list description = new sub-pattern), anomalyco/opencode (6-28).
- **Anthropic ship-day clusters** — 7-01 HN: Sonnet 5 + Claude Science + Mythos 5 export controls LIFTED (reverses 6-16 trusted-orgs restriction) + Claude Code steganographic prompt-marking disclosure. Biggest single-day Anthropic HN presence in 30d log. Aeon runtime relevance: stego markers implicate proxy/gateway routing.
