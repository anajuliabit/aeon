# Long-term Memory
*Last consolidated: 2026-07-03*

## Current Goals
- **Sandbox-truncation systemic** — ISS-019/020/021/024/025 cluster still bleeds an 18-skill chronic tail (`output_tokens=0`). Durable `aeon.yml` capture-step fix unshipped **day 10** since action-converter 4.6/5-quality flag (6-24 18:14Z). Weekly-review hard deadline **2026-07-04 = T-1d, TIGHT**.
- **12:00 UTC batch first live test 7-03 → FAILED** — 6 skills (token-pick/defi-overview/token-movers/on-chain-monitor/defi-monitor/market-context-refresh) still dark ~5.2d since 6-28; **PR #150 `usepod_model`→`model:` was PARTIAL fix, deeper scheduler/YAML issue remains** (possibly `market-context-refresh` line 155 still carries `usepod_model`). Additional dead slots today: github-trending 09:00Z + aixbt-pulse 09:00Z + narrative-tracker 13:30Z (same batch-drop signature). Wednesday skill-analytics 18:30Z will formalize the anomaly.
- **PR #149 docs(skill-graph)** — opened 6-28 17:15Z, **~118h day-5 stall** as of 7-03 15:29Z. Only PR in stack; operator-merge gated.
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16 (**day 18**). Operator top-up pending. WebSearch fallback covers daily-routine/tweet-roundup/narrative-tracker; prefetched paths serve list-digest/agent-buzz/token-pick. *[BLOCKED]*
- **Operator on-chain config** — defi-monitor NO_CONFIG **day 26**; `memory/on-chain-watches.yml` needs `type: pool` / `type: position` entries. `ALCHEMY_API_KEY len=0`, `ETHERSCAN_API_KEY null`. *[BLOCKED — partial]*
- **BTC 7-day breakdown streak BROKEN → day-2 of reclaim** — 7-02 close $61,487 = **first daily close ≥ $60,500 in the 8-day window** (streak-break silent per skill spec: only $63.5k/$65.9k reclaim + <$60,500 breakdown fire alerts). 7-03 tape held $61.3k → $62.0k across 4 ticks; +$222M BTC ETF net-in breaks 10d outflow streak (ETH ETFs +$29M same day). $63.5k / $65.9k rails still gate for real reclaim.

## Fleet Health
- **skill-health 7-02 18:53Z snapshot byte-identical 3rd day** (0 critical · 23 degraded · 8 warning · 9 healthy · 2 no_data). 15 open issues; **ISS-026 fix shipped via PR #151 merge 7-02 13:20Z — INDEX still Open, needs resolved-flip**.
- **fork-skill-digest STUCK ~117h** carry — dispatched 2026-06-28T18:38Z, never resolved. Weekly Sun 7-05 fresh dispatch attempt.
- **operator-scorecard Mon 10:30Z MISSED day 5** — scheduler-side never-run gap, carry indefinitely until scheduler patch.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers, skill-health, 7-02 batch-merge entry.
- [Crypto research](topics/crypto.md) — Narratives, picks (VELVET −68.5% closed, SLX day-9 flat −1.5%, M MemeCore 3-day arc +130% closed, GITLAWB +27.38% breakout).
- [Market context](topics/market-context.md) — 7-03 bounce day-2: BTC $61.7k / breadth 83/100, ETH first-week-reclaim of $1,700, spot ETF flip +$222M, sovereignty-stack ship day.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage day 18; PR #148 merged 6-29.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 21:00Z.

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | $0.00361815 +1.16% 7-03 (day-4 green post 6-30 vol spike; 24h decel +5.84%→+1.16% = participation-fatigued follow-through; **vol 1.02× baseline = supply arc closed**, position on price-action-only now) |
| MAMO    | mamo               | 15%           | $0.00841540 +1.29% 7-03 (day-3 green — cleanest small-cap streak of watchlist, 3rd close in $0.0083–$0.0084 zone; vol 1.03× flat) |
| REPPO   | reppo              | 15%           | $0.02401810 +10.85% 7-03 (day-2 of vol-drought break — $0.021 wobble line broken decisively, near 15% rail but under-threshold; vol 1.72× = elevated but stepping down from 3.16× spike) |
| GITLAWB | gitlawb            | 15%           | $0.00006133 **+27.38% 7-03 — TRIGGER FIRED** (largest 1d gain of watchlist window; $0.00005→$0.00006 handle jump on 1.76× vol = participation-confirmed breakout, contrasts 7-02 +8.03% on 0.88× shallow) |

## Recurring patterns (durable)
- **Bounce day-2 = whole-green watchlist + 83/100 breadth continuation** — 7-02 32→81/100 first-bounce, 7-03 83/100 = day-2 hold. Watchlist median 24h +6.07% (all 4 tokens green). BTC +$222M ETF net-in breaks 10d outflow streak; ETH first-week-reclaim of $1,700 (+6.1%); SOL leadership +3.7% continues. STRUCTURAL longs persist: AI agent infra, stablecoins, RWA via CEX rails, prediction markets. $63.5k/$65.9k rails still gate for real reclaim.
- **Brandjacking is the new default supply-chain vector** — extends across verticals: AI-infra (6-30) → enterprise-data-infra (Confluent Kafka JS 7-01) → testing-framework (vitest-agent + 3-pkg Tailwind 7-02). 100% npm; pip/crates/go zero. MCP/agent-infra brandjack thread **day-7** (fast-mcp-telegram + Grackle pair + neuro-cortex-memory RCE via `CLAUDE_PROJECT_DIR` = direct Claude Code adjacency).
- **Solo-researcher mega-batch pattern** — same-project coordinated disclosure batches shipping in single-day windows: 7-01 Fission Go 9-CVE = 1st, **7-03 OpenClaw npm 23-CVE = 2nd (~2.5× larger)**. Distinct from routine brandjacking (batch-magnitude signature, not one-off). 2 in 3 days = codify.
- **Skills-as-primitive convergence day-4** — 4 provider artifacts (Anthropic Agent SDK 6-28 + google/agents-cli 7-01 + ASPIRE robotics paper 7-02 + z.ai ZCode/GLM-5.2 HN 7-02) + **policy vector added 7-03**: Right-to-Local-Intelligence (HN 203p) alongside Podman v6.0.0 + Immich 3.0 = **sovereignty stack shipping day** (runtime + consumer + user-rights = 3 layers same slate). Compute + tools + protocols + policy = 4 layers now durable.
- **Memory as distinct eval axis** — MemSyco-Bench (7-02) → AgenticSTS (7-03) day-2 of paper-pick thread. Direct aeon-runtime hit: bounded-memory contract for what each future decision is allowed to see.
- **Anthropic ship-day compounding** — 7-01 HN dominated (Sonnet 5 + Claude Science + Mythos 5 export lift + stego prompt-marking); 7-02 Sonnet 5 dev-preference **82% inside Claude Code**, 92.4% SWE-bench (vs Opus 4.6 80.8%). Aeon runtime relevance: stego markers implicate proxy/gateway routing.
- **search-skill SEARCH_SKILL_NO_GAP day 10** — fleet capability-complete on external-skill axis. Failures are infra (ISS-025 capture step), not gaps. Stop noise-filing new gap reports unless cron-state failure mode changes.
- **operator-scorecard Mon 10:30Z perpetually MISSED** — scheduler-side never-run gap, flagged every Monday hb. Not skill-side. Carry indefinitely until scheduler patch.
- **Fake-star pattern** — drop with confidence when: >100k stars + 1:6 (or worse) fork ratio + wrong-language tag (Shell for AI project) OR rapid semver (v3.8.42/139d) + brand-list description.
- **GH Advisory `patched_versions: null` lags advisory-page reality** — 7-01 all-null cascade → 7-02 inversion → **7-03 day-3 continues inversion**. WebFetch on advisory page is canonical for triage, not the JSON field.
- **Alpha-filter framework — tokenomics-alignment via @Flowslikeosmo** — SLX/VELVET/LIT thesis-application shape confirmed by 2nd hit ($LIT +15.3% BREAKOUT 7-02, −5.5% 7-03 mean-revert, thesis 7d +25% intact).
- **Supply-chain-quiet 24h window signal** — 7-03 15:35Z = 0 fresh npm malware after 7-02 15:00Z breaks 8-day daily-npm-malware streak. Not yet durable (could be researcher-batch pause), watch next 48h for pattern-vs-blip.
