# Long-term Memory
*Last consolidated: 2026-07-07*

## Current Goals
- **Sandbox-truncation systemic day 12** — ISS-019/020/021/024/025 cluster bleeds an 18-skill chronic tail (`output_tokens=0`). Durable `aeon.yml` capture-step fix unshipped; self-set weekly-review Mon 7-06 deadline is **T-1**. Action-converter 7-04 ranked capture-step PR q5/u5 top action but PR not authored — tomorrow 19:00Z weekly-review formalizes miss unless self-improve authors today.
- **12:00 UTC batch — day-5 of failed live test post PR #150** — 6 skills (token-pick/defi-overview/token-movers/on-chain-monitor/defi-monitor/market-context-refresh) dark ~7.9d since 6-28. `usepod_model:` still on `aeon.yml` L155/162/171 (grep-confirmed 7-05 14:47Z hb).
- ~~**PR #149 docs(skill-graph)** — opened 6-28 17:15Z, **~165h day-7 stall** at 7-05 14:47Z. Sunday + US Independence Day weekend → operator merge unlikely.~~ *[MERGED 2026-07-06T21:26Z — see Recently Cleared]*
- **XAI quota recovery** — Team 3a8b4c1e monthly credit exhausted 6-16 (**day 20**). Operator top-up pending. WebSearch fallback covers daily-routine/tweet-roundup/narrative-tracker; prefetched paths serve list-digest/agent-buzz/token-pick. *[BLOCKED — waiting on operator team-credit top-up since 2026-06-16]*
- **Operator on-chain config day 28** — defi-monitor NO_CONFIG; `memory/on-chain-watches.yml` needs `type: pool` / `type: position` entries. `ALCHEMY_API_KEY len=0`, `ETHERSCAN_API_KEY null`. *[BLOCKED — waiting on operator config + API keys]*
- **BTC bounce day-5 above $60,500 breakdown line** — 7-05 ticks $63,001 (00:17Z) → $62,854 (04:35Z) → $62,568 (10:01Z) → $62,676 (12:56Z) → $62,647 (17:14Z); 7-04 close $63,094 = new high in reclaim window, ~$406 shy of $63.5k reclaim gate. Momentum tapering day-3 → day-5. $65.9k full-reclaim gate still much further.
- **SLX open pick DAY-11 CATASTROPHIC — recut overdue** — HIGH 9/10 6-24 entry $0.4753 → 7-05 $0.256 = **-46% vs entry** (intraday -29.6% capitulation, rank collapse #289 → #372, mcap $62M). CG simple-price verified. Position past every recut trigger; surfaced as top follow-up in 7-05 daily-routine.
- **Sandbox-truncation systemic day 13** — ISS-019/020/021/025 cluster bleeds an 18-skill chronic tail (`output_tokens=0`). Durable `aeon.yml` chain-runner capture-step (L479-493) PR still un-authored. **Weekly-review T-0 Mon 7-06 19:00Z** (~1h out from consolidation): action-converter 7-04 top-ranked action + 7-05 T-1 flag both slipped; weekly-review will formalize miss verdict unless self-improve authors PR in the next hour.
- ~~**PR #149 docs(skill-graph)** — opened 6-28 17:15Z, **~193h day-8 stall** at 7-06 14:47Z. **PR #155 (opened 7-05 17:28Z) is likely supersede-path** — same title/scope but +68 skills · 4→5 depends_on · 9→21 shared-state (vs #149's +68 · 9→36). Operator decision pending (which to merge/close). Post-holiday-weekend Monday reopens merge window.~~ *[MERGED 2026-07-06T21:26Z — PR #155 now dup-open, see Recently Cleared]*
- **XAI quota recovery** — Team 3a8b4c1e monthly credit exhausted 6-16 (**day 21**). Operator top-up pending. WebSearch fallback covers daily-routine/tweet-roundup/narrative-tracker; prefetched paths serve list-digest/agent-buzz/token-pick. *[BLOCKED]*
- **Operator on-chain config day 29** — defi-monitor NO_CONFIG; `memory/on-chain-watches.yml` needs `type: pool` / `type: position` entries. `ALCHEMY_API_KEY len=0`, `ETHERSCAN_API_KEY null`. *[BLOCKED — partial]*
- **BTC $63.5k RECLAIM CONFIRMED day-1 (7-06 01:29Z btc-levels alert)** — spot $63,595 / daily close $63,546 (7-05) = first reclaim print, `reclaim63500Alerted=true` set in state file. 7-06 ticks $63,595 (01:29Z) → $63,801 (17:23Z) hold above gate. Bounce day-6 with reclaim resolved. Next gate: **$65,900 full-reclaim**.
- **SLX open pick DAY-12 CATASTROPHIC — recut STILL overdue** — HIGH 9/10 6-24 entry $0.4753 → 7-05 $0.256 = **-46% vs entry** (intraday -29.6% capitulation, rank #372, mcap $62M). No fresh CG print today (token-alert not yet run 7-06). Position past every recut trigger; surfaced daily-routine 7-05 top follow-up, unchanged 7-06.

## Recently Cleared
- **PR #149 docs(skill-graph)** — completed 2026-07-06 (merged 21:26Z, day-8 stall closed after ~197h open; NEW_SKILLS +68, SHARED_STATE 9→36). Follow-up: PR #155 supersede opened 07-05 17:29Z is now DUP OPEN — operator close-decision pending.
- **PR #154 fix(issues) close ISS-026** — completed 2026-07-06 (merged 15:35Z, day-3 stall closed; INDEX flip shipped).
- **Sandbox-truncation systemic day 14** — ISS-019/020/021/025 cluster bleeds an 18-skill chronic tail (`output_tokens=0`). Chain-runner capture-step PR against `aeon.yml:479-493` (per ISS-009 root-cause line) still un-authored; weekly-review 7-06 19:20Z formalized MISS on the self-set Mon 7-06 deadline and restructured next-7d actions with `Authored by:` routing slots (self-improve × 3, operator × 1). **New deadline: 2026-07-13**.
- **12:00 UTC batch DARK day-10 — PR #156 DID NOT UNBLOCK** — 7-07 12:00Z tick was first live test post-merge and **batch 6 (token-pick/defi-overview/token-movers/on-chain-monitor/defi-monitor/market-context-refresh) did NOT dispatch**. Only token-alert + btc-levels fired at 13:54Z catch-up. PR #156 removed `usepod_model:` drift at aeon.yml L155/162/171 (real fix, ships cost delta) but the batch-dispatch failure is deeper — chain-config or 12:00Z cron slot itself. **Next action: aeon.yml audit at batch-dispatch layer, not per-skill model config.**
- **PR #155 docs(skill-graph)** — opened 7-05 17:28Z, ~73h day-3 stall; PR #149 predecessor merged 7-06 21:26Z resolved the supersede-decision by shipping the older PR. PR #155 now redundant-or-orphan — needs close or diff-audit to determine if it carries additional edits.
- **XAI quota recovery** — Team 3a8b4c1e monthly credit exhausted 6-16 (**day 22**). Operator top-up pending. WebSearch fallback covers daily-routine/tweet-roundup/narrative-tracker; prefetched paths serve list-digest/agent-buzz/token-pick. *[BLOCKED — waiting on operator team-credit top-up since 2026-06-16]*
- **Operator on-chain config day 30** — defi-monitor NO_CONFIG; `memory/on-chain-watches.yml` needs `type: pool` / `type: position` entries. `ALCHEMY_API_KEY len=0`, `ETHERSCAN_API_KEY null`. *[BLOCKED — waiting on operator config + API keys]*
- **BTC $63.5k RECLAIM day-2 HOLDING** — 7-07 ticks $63,946 (01:22Z) → $63,007 (05:33Z) → $63,011 (08:53Z) → $63,116 (13:55Z) → $63,958 (16:31Z); 7-06 daily close $64,072 = first daily close above $63.5k gate (post-reclaim high). `reclaim63500Alerted=true` set 7-06 01:29Z; no re-arm (spot > $60,500 floor). Bounce day-7 with reclaim confirmed on-tape. Next gate: **$65,900 full-reclaim**.
- **SLX open pick DAY-13 CATASTROPHIC — recut STILL overdue** — HIGH 9/10 6-24 entry $0.4753 → last CG print 7-05 12:59Z $0.256 = **-46% vs entry** (intraday -29.6% capitulation, rank #372, mcap $62M). No fresh CG print 7-06/7-07 (token-alert scope doesn't cover SLX). Position past every recut trigger; daily-routine 7-05/7-06/7-07 top follow-up, unchanged 3 consecutive days.

## Recently Cleared
- **PR #149 docs(skill-graph)** — MERGED 2026-07-06 21:26Z (~197h day-8 stall ended, post-holiday-weekend Monday evening).
- **fork-skill-digest UN-STUCK** — 168h+ stuck resolved 7-05 21:06Z retry after 20:18Z fail. cf=0, sr=75%. 19 consecutive hb surfaces cleared.

## Fleet Health
- **PR #156 SHIPPED cost fix but NOT batch-dispatch fix** — merged 7-06 15:45Z. Cost delta stands (~$46/wk → ~$2.50/wk on narrative-tracker via Haiku). Batch-6 unblock did NOT ship — 7-07 12:00Z live test failed with 0/6 dispatched. Root cause is beyond `usepod_model:` drift.
- **skill-health 7-06 19:16Z**: 0 critical · 21 degraded · 11 warning · 8 healthy · 3 no_data (43 enabled). Hash 190b6b8d (unchanged from 7-05; byte-identical 6-day streak). 12 open issues (down from 15 pre-7-05 skill-evals bulk close of ISS-023/024/026).
- **aixbt-pulse dead-slot day-9 CONFIRMED** — 7-07 09:00Z tick MISSED (state file last_success 6-28T21:21Z, ~236h = 9.8× twice-daily 09/21 interval).
- **operator-scorecard chronic Mon 10:30Z miss** — 7 consecutive Monday misses through 7-06; scheduler-side never-run gap. Next tick Mon 7-13.
- **Morning-slot cron catch-up pattern durable** — 7-06 and 7-07 both show 00:15/04:15 btc-levels dispatched ~1h late, 08:00Z hb ~53min late but eventually lands. Not skill-side; GH Actions cron catch-up gap. Recurring, expected.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers, skill-health.
- [Crypto research](topics/crypto.md) — Narratives, picks (SLX day-13 CATASTROPHIC -46%, VELVET closed at -68.5%, M MemeCore closed at +130%, GITLAWB reversal day-3).
- [Market context](topics/market-context.md) — 7-07 BTC reclaim day-2 holding; 7-06 daily close $64,072 = first close above gate.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX recut STILL OVERDUE day-13.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage day 22.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 21:00Z (aixbt-pulse dead-slot day-9).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55). Prices as of 7-07 14:00Z token-alert.

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | $0.00364437 +1.60% 24h 7-07 (24h green inside 2d red vs 7-05; vol $2,862K = 2.16× baseline, **6.14× intraday resurrection** — first ≥$2M print since 7-02) |
| MAMO    | mamo               | 15%           | $0.00932410 +1.82% 24h 7-07 (day-6 green — cleanest small-cap streak of watchlist, first sustained close ≥ $0.009; vol 0.90× baseline exhale) |
| REPPO   | reppo              | 15%           | $0.02558824 +4.87% 24h 7-07 (breakout resumes, day-1 fresh push above $0.025 handle post 2-day breather; vol 1.05× flat) |
| GITLAWB | gitlawb            | 15%           | $0.00005721 -2.91% 24h 7-07 (day-2 reversal give-back extends at slower pace; vol 1.45× = participation-selling extends) |

## Recurring patterns (durable)
- **BTC $63.5k RECLAIM day-2 HOLDING** — 7-06 daily close $64,072 = first close above gate. Reclaim arc breadth 32→81→83→71→51 → hold-above-gate → daily close breakout → +$221.7M ETF inflow snap-of-10d-outflow-streak (7-07) = 3-signal alignment (spot + close + flow). Next gate $65.9k; below-$60.5k re-arms breakdown alert.
- **12:00 UTC batch fix NOT sufficient — deeper root cause** — PR #156 removed L155/162/171 `usepod_model:` drift but 7-07 12:00Z tick still didn't dispatch batch 6. Root cause lives above per-skill config: chain-config, cron slot, YAML nesting, or dispatcher matcher. Next self-improve run should grep `12:00`/`0 12`/`schedule:` in aeon.yml and audit the batch-tick path.
- **Skills-as-primitive convergence day-8 — multi-region cross-lab holds** — 7-05 alibaba/page-agent (Chinese-lab first entry). 6 major labs (Anthropic + OpenAI + Google + Meta + Alibaba + Microsoft via dotnet/skills first-party) across 2 regions (US/China). 7-07 tweet-roundup: **Emdash agentic-dev-env orchestrates Claude Code + Gemini + Codex in parallel** — extends orchestrator-layer for cross-lab agents. MCP-momentum extends into game-engine (unity-mcp) after browser.
- **Sovereignty stack day-6** — meetily (Rust local-audio-AI) 7-05 + **CoMaps FOSS offline maps HN 527pts 7-07** = 6 artifacts across 5 days spanning runtime + consumer + user-rights + operator-primer + local-audio + local-maps layers. GLM 5.2 (HN 387pts 7-07, open-weights closing on frontier while inference cost drops) extends local-LLM sovereignty thread.
- **Eval-quality-axis day-6** — MemSyco 7-02 → AgenticSTS 7-03 → SkillCoach 7-04 → Anthropic+OpenAI production bugs 7-05 → **LLM-as-a-Verifier arXiv 2607.05391 HF ↑5 7-07** (Kwok/Li/Atreya — verification-as-scaling-axis via expected value over scoring-token logits, not discrete judge scores). Direct hit on aeon-runtime's own verifier-tool use.
- **Anthropic global-workspace paper HN 360pts 7-07** — info-geometric attribution across transformer layers. HN take mixed (promotional framing, real underlying paper). Adds interpretability angle to Anthropic ship-day compounding.
- **Anthropic ship-day compounding + IPO-prep tell** — 7-05 Claude Science + Claude Tag. S-1 confidentially filed $965B > OpenAI. **7-07 OAI counter-tell: custom Jalapeño inference chip announced**. Sonnet 5 dev-preference 82% inside Claude Code carries.
- **Apple to open-source Foundation Models framework this summer** (7-07 daily-routine tweet-roundup) — first Apple entry into open-model releases, orthogonal to sovereignty stack (BYO-model for consumer OS). New signal.
- **Holiday-freeze cascade RESOLVED post-Mon 7-06** — Monday US business hours reopened publishing pipelines. GHAD un-freeze wave expected; watch backlog (7-03/7-04/7-05/7-06-am + npm brandjack resumption). CLARITY Act 7-04 signing MISSED slipped to Senate return 7-13+.
- **RWA narrative rotates onto SOL rails** — 7-05 Solana RWA fresh ATH $3.41B extends 7-04 ARB 10%-fee dune signal. 2 chains with concrete RWA/fee-accrual anchors within 48h. Tempo/Canton positioning to eat ETH RWA lunch.
- **Summer.fi $6M exploit → SUMR -18%** (7-07) — DeFi security event: single-protocol tail-risk still live in bull-tape reclaim. Watch for wave-adjacency (protocol-of-protocols cascade absent so far).
- **Ripple fully MiCA-compliant across 30 EEA countries** (7-07) — first mega-exchange to complete full MiCA transition post-244-firm authorization window (7-05 MiCA closed). Institutional-rails narrative day-1 momentum.
- **Alpha-filter framework — Vitalik-roadmap bearish-on-tape lens** — 7-05 DefiIgnas quote-tweet reads Vitalik 2028+ throughput fork as inviting Tempo/Canton to eat RWA lunch meanwhile. Extends @Flowslikeosmo tokenomics-alignment framework (SLX/VELVET/LIT/VVV 4× thesis).
- **search-skill SEARCH_SKILL_NO_GAP day 14** — fleet capability-complete on external-skill axis. Failures are infra (ISS-025 capture step), not gaps.
- **Same-day self-improve authoring pattern** — 7-05 self-improve authored PR #156 targeting L155/162/171 called out in 12+ log entries since 6-24; merged 7-06. Chain: action-converter → self-improve → PR-merge closes when call-out is precise (specific file paths + line numbers). **But PR #156 was insufficient** — same chain now needs to author against `aeon.yml:479-493` (deeper capture step) which weekly-review 7-06 19:20Z routed to self-improve × 3 in next-7-day action list. **Test-run of routing hypothesis is live this week.**
- **Fake-star pattern + dotfiles-shape complement** — 7-05 mattpocock/skills drop (Shell + 157k + "personal configuration") confirms dotfiles/config-dump filter as complementary tell to strict fake-star triad.
- **BONK CAPITULATION on 25%+ mcap-vol turnover + ANSEM 7d +232%** (7-07 token-movers) — MICROCAP+PUMP-RISK context (memory: 6-28 called ANSEM +44334% as CG aggregator outlier — treat with skepticism despite today's cleaner rank #186). BONK first MAJOR-cap capitulation of reclaim window.
