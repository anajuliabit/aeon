# Long-term Memory
*Last consolidated: 2026-07-02*

## Current Goals
- **Sandbox-truncation systemic** — ISS-019/020/021/024/025 cluster still bleeds a 19-skill chronic tail (`output_tokens=0`). Durable `aeon.yml` capture-step fix unshipped **day 8** since action-converter's 4.6/5-quality PR flag (6-24 18:14Z). Hard surface deadline: weekly-review **2026-07-04** (3d out).
- **PR #149 docs(skill-graph)** — opened 6-28 17:15Z, **~69h stall day 3**. Operator-merge gated.
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16 (**day 16**). Operator top-up pending. WebSearch fallback covers daily-routine/tweet-roundup/narrative-tracker; prefetched XAI paths still serve list-digest/agent-buzz/token-pick. *[BLOCKED]*
- **Operator on-chain config** — defi-monitor NO_CONFIG day 24; `memory/on-chain-watches.yml` needs `type: pool` / `type: position` entries. `ALCHEMY_API_KEY len=0`, `ETHERSCAN_API_KEY null`. *[BLOCKED — partial]*
- **BTC breakdown day 6 CONFIRMED** — 6-30 close $58,551 = 6th consecutive sub-$60,500; 00:19Z alert fired. Tape pinned $58.2k–$59.8k through 7-01 12:18Z. First sub-$60k print since 2024, 50% below Oct-2025 $126k ATH. Tonight's UTC close decides 7th-red or reclaim ($63.5k / $65.9k).
- **Sandbox-truncation systemic** — ISS-019/020/021/024/025 cluster still bleeds 19-skill chronic tail (`output_tokens=0`). Durable `aeon.yml` capture-step fix unshipped **day 9** since action-converter's 4.6/5-quality flag (6-24 18:14Z). Weekly-review hard deadline **2026-07-04 (T-2d)**.
- **PR #149 docs(skill-graph)** — opened 6-28 17:15Z, **~94h day-4 stall** as of 7-02 15:29Z. Last PR in the stack after 7-02 batch merge; operator-merge gated.
- **12:00 UTC batch first live test 7-03** — 6 skills (token-pick / defi-overview / token-movers / on-chain-monitor / defi-monitor / market-context-refresh) dark since 6-28; PR #150 merge (7-02 13:20Z) removed root cause. Watch Fri 7-03 12:00 tick.
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16 (**day 17**). Operator top-up pending. WebSearch fallback covers daily-routine/tweet-roundup/narrative-tracker; prefetched paths serve list-digest/agent-buzz/token-pick. *[BLOCKED]*
- **Operator on-chain config** — defi-monitor NO_CONFIG **day 25**; `memory/on-chain-watches.yml` needs `type: pool` / `type: position` entries. `ALCHEMY_API_KEY len=0`, `ETHERSCAN_API_KEY null`. *[BLOCKED — partial]*
- **BTC breakdown day-7 CONFIRMED → first material bounce** — 7-01 close $59,979.90 = 7th consecutive sub-$60,500; 01:17Z alert fired. 7-02 tape flip $60.7k → $61.6k intraday = first close-window print back above $60k of the streak; +3.0% intraday, breadth 32→81/100 = biggest single-day swing in 30d. **Tonight's UTC close decides day-8-red or first-reclaim.** No reclaim yet — $63.5k / $65.9k rails still gate.

## Recently Cleared
- **PR #150 fix(aeon.yml) `usepod_model` → `model:`** — completed 2026-07-02 (MERGED 13:20:07Z by operator, batch-merged alongside #151; ~$456/mo cost fix landed for on-chain-monitor/token-pick/token-movers).

## Fleet Health
- **skill-health 6-30 18:08Z snapshot unchanged** (daily-cadence 7-01 18:30Z byte-identical hash 1ff18e84): 9 healthy · 23 degraded · 8 warning · 0 critical · 2 no_data. 15 open issues; **ISS-026 fix shipped via PR #151 merge 7-02 13:20Z — INDEX still Open, needs resolved-flip**.
- **PR #150 + #151 both MERGED 7-02 13:20Z** — batch operator merge; 2/3 stacked PRs resolved. Only #149 left. $456/mo bleed halted; ISS-026 heartbeat/skill-health/eval-tick timing fixed. See [[fleet]] 7-02 entry.
- **fork-skill-digest STUCK ~93h** carry — dispatched 2026-06-28T18:38Z, never resolved. Weekly Sun 7-05 fresh tick.
- **operator-scorecard Mon 10:30Z MISSED day 4** — scheduler-side never-run gap, carry indefinitely until scheduler patch.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers, skill-health, 7-02 entry (batch-merge day: #150/#151 both shipped, BTC day-7 → first bounce, whole-green watchlist, brandjack extends to testing arm, MCP/agent-infra 5-advisory 48h cluster).
- [Crypto research](topics/crypto.md) — Narratives, picks (VELVET FULLY BLOWN day-5 −68.5% closed, SLX day-5 watch, LIT breakout day-2 +15.3%, REPPO vol-trigger 3.16×, WELL washout-then-reversal), 7-02 tape flip.
- [Market context](topics/market-context.md) — 7-02 snapshot: BTC $60.3k–$61.6k intraday, breadth 81/100 flip, SOL leadership, HYPE divergence, PR #150/#151 merged, skills-as-primitive day-3 convergence.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage day 17; PR #148 merged 6-29.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 21:00Z.

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | $0.00356401 +5.84% 7-02 (3rd close post-6-30 vol spike; direction confirms UP = **washout-then-reversal**, reverses 7-01 supply-hitting-bid thesis; vol 1.55× baseline) |
| MAMO    | mamo               | 15%           | $0.00830984 +4.53% 7-02 (2nd consecutive green; clears $0.0083 first time since 6-27; vol 0.99× baseline = flat participation) |
| REPPO   | reppo              | 15%           | $0.02153733 +4.31% 7-02 (breaks $0.021 wobble line on **vol spike 3.16×** — 4-day drought base snaps, largest print since 6-22; TRIGGER FIRED) |
| GITLAWB | gitlawb            | 15%           | $0.00004802 +8.03% 7-02 (snaps "worst 1d" pattern, $0.00005 handle reclaim attempt; vol 0.88× = participation-shallow bounce) |

## Recurring patterns (durable)
- **Meta-bear "crypto needs new narrative" day 7 → first-bounce day** — persistent 6/20 through 7-01; 7-02 breadth flipped 32→81/100 (biggest 30d-window swing), BTC +3.0% intraday, watchlist +5.19% median. First contradiction of the run; regime pivot signal but no reclaim yet ($63.5k/$65.9k still gate). STRUCTURAL longs persist: AI agent infra, stablecoins, RWA via CEX rails, prediction markets.
- **Brandjacking is the new default supply-chain vector** — extends across verticals: AI-infra (6-30) → enterprise-data-infra (Confluent Kafka JS 7-01) → **testing-framework arm (vitest-agent + 3-pkg Tailwind cluster 7-02)**. 100% npm; pip/crates/go zero. 5 MCP/agent-infra advisories in 48h window 7-01→7-02 (incl neuro-cortex-memory RCE via `CLAUDE_PROJECT_DIR` = direct Claude Code adjacency).
- **Skills-as-primitive convergence** — 4 provider artifacts across vendors: Anthropic Agent SDK (6-28) + google/agents-cli (7-01) + ASPIRE robotics paper (7-02) + **z.ai ZCode/GLM-5.2 (HN 7-02)**. Cross-vendor incl Chinese lab = durable pattern, not a single-lab move.
- **Anthropic ship-day cluster** — 7-01 HN dominated (Sonnet 5 + Claude Science + Mythos 5 export lift + stego prompt-marking); 7-02 follow-through **Sonnet 5 dev-preference 82% inside Claude Code**, 92.4% SWE-bench (vs Opus 4.6 80.8%). Aeon runtime relevance: stego markers implicate proxy/gateway routing.
- **search-skill SEARCH_SKILL_NO_GAP day 9** — fleet capability-complete on external-skill axis. Failures are infra (ISS-025 capture step), not gaps. Stop noise-filing new gap reports unless cron-state failure mode changes.
- **operator-scorecard Mon 10:30Z perpetually MISSED** — scheduler-side never-run gap, flagged every Monday hb. Not skill-side. Carry indefinitely until scheduler patch.
- **Fake-star pattern** — drop with confidence when: >100k stars + 1:6 (or worse) fork ratio + wrong-language tag (Shell for AI project) OR rapid semver (v3.8.42/139d) + brand-list description. Anchors: agency-agents (6-30 + 7-01), OmniRoute (7-01 TypeScript sub-pattern), anomalyco/opencode (6-28).
- **GH Advisory `patched_versions: null` lags advisory-page reality** — 7-02 inversion vs 7-01 all-null cascade. Codify: WebFetch on advisory page is canonical for triage, not the JSON field.
- **Alpha-filter framework — tokenomics-alignment via @Flowslikeosmo** — day-2 doubling down on $LIT (7-02 +15.3% BREAKOUT playing out live). Same caller previously surfaced SLX/VELVET. Filter itself durable-tracked; 2nd application confirms shape.
