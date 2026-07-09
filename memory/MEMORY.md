# Long-term Memory
*Last consolidated: 2026-07-09*

## Current Goals
- **Sandbox-truncation systemic day 17** — ISS-019/020/021/025 cluster bleeds an 18-skill chronic tail (`output_tokens=0`). Chain-runner capture-step PR against `.github/workflows/aeon.yml` (per ISS-009 root-cause line) still un-authored. **Weekly-review 7-13 deadline T-4 days.** 7-07 self-improve routing test surfaced STRUCTURAL BLOCK: self-improve SKILL.md rule 5 forbids `.github/workflows/` edits, so `Authored by: self-improve × 3` slots cannot ship. Self-improve 7-09 18:00Z tick is the next routing-hypothesis test window (rule-relax vs operator direct-author).
- **12:00 UTC batch DARK day-12** — 7-09 12:00Z tick as of 14:17Z hb had not yet dispatched token-alert or btc-levels 12:15Z (2h past slot; prior 3 days caught up ~53min–1h late — 20:00Z hb will verify extension). 8 batch skills (token-pick/defi-overview/token-movers/on-chain-monitor/defi-monitor/market-context-refresh/narrative-tracker/aixbt-pulse) still last_dispatch 6-28 (12 days). Scheduler-side never-run, above per-skill config. **ISS-027 pattern codification filed 7-07.**
- **XAI quota recovery** — Team 3a8b4c1e monthly credit exhausted 6-16 (**day 24**). Operator top-up pending. WebSearch fallback covers daily-routine/tweet-roundup/narrative-tracker; prefetched paths serve list-digest/agent-buzz/token-pick. *[BLOCKED — waiting on operator team-credit top-up since 2026-06-16]*
- **Operator on-chain config day 32** — defi-monitor NO_CONFIG; `memory/on-chain-watches.yml` needs `type: pool` / `type: position` entries. `ALCHEMY_API_KEY len=0`, `ETHERSCAN_API_KEY null`. *[BLOCKED — waiting on operator config + API keys]*
- **BTC $63.5k reclaim arc BROKEN day-1** — 7-08 daily close $62,248 = **first close BELOW gate** after 2 closes ABOVE (7-06 $64,072 → 7-07 $63,351 → 7-08 $62,248). Reclaim arc snaps: close breakout day-1 → day-2 held → day-3 SOFTENS (spot below, close above) → **day-4 BROKEN (both below)**. 7-09 spot recovers modestly: $62,347 (01:16Z) → $62,402 (05:12Z) → $62,874 (08:57Z) → $62,676 (16:47Z) — all still below $63.5k gate but above $60.5k re-arm floor. `reclaim63500Alerted=true` holds. US-Iran strike headlines 7-08 late (Yahoo/CryptoNews) pulled BTC briefly to $61.9k -2.2%. Below-$60.5k re-arms breakdown alert; next reclaim gate remains $63.5k spot then $65.9k full.
- **SLX open pick DAY-15 CATASTROPHIC — recut STILL overdue** — HIGH 9/10 6-24 entry $0.4753 → last CG print 7-05 12:59Z $0.256 = -46% vs entry. 7-09 daily-routine trending endpoint prints SLX at **$0.174 = -63% vs entry** (fresh delta, token-alert scope doesn't cover SLX so no CG print 7-06/7-07/7-08/7-09). Position past every recut trigger; 6th consecutive daily-routine surface. Weekly-review action-list `Authored by: operator × 1` slot targets this — deadline 7-13 (T-4).

## Recently Cleared
- **PR #155 docs(skill-graph) MERGED 7-08 13:22Z** — supersede-candidate shipped (not closed as dup). +68 skills · 4→5 depends_on · 9→21 shared-state.
- **PR #160 fix(issues) close ISS-022 MERGED 7-08 13:31Z** — operator authored 7-07 18:38Z, INDEX flip landed ~19h later. Open issues 12 → 11.

## Fleet Health
- **skill-health 7-08 18:20Z**: 0 critical · 21 degraded · 11 warning · 8 healthy · 3 no_data (43 enabled). Hash `6f808f12` (day-N suffix flip; classification byte-identical **8-day streak**). **11 open issues** (ISS-005/007/009/010/011/016/018/019/020/021/025).
- **aixbt-pulse dead-slot day-11** — 7-08 09:00Z + 21:00Z + 7-09 09:00Z all MISSED. State file last_success 2026-06-28T21:21Z, ~283h stale = 11.8× twice-daily interval.
- **operator-scorecard chronic Mon 10:30Z miss** — 8 consecutive Monday misses through 7-06; scheduler-side never-run. Next tick Mon 7-13.
- **Morning-slot cron catch-up pattern durable** — 7-06/7-07/7-08/7-09 all show 08:00Z hb + 12:00Z batch firing ~53min–1h2min late; 7-09 14:00Z tick fired ~17min late (faster variance). Not skill-side; GH Actions cron catch-up gap. Recurring, expected.
- **Weekly-shiplog + cost-report Mon 7-06 ticks MISSED** — 10d gap = 1.43× 7d interval, still under 2× threshold, no flag. Same scheduler-gap category as operator-scorecard.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers, skill-health.
- [Crypto research](topics/crypto.md) — Narratives, picks (SLX day-15 CATASTROPHIC -63% via trending, VELVET closed at -68.5%, M MemeCore closed at +130%, GITLAWB CAPITULATION completed).
- [Market context](topics/market-context.md) — 7-09 BTC reclaim arc BROKEN (7-08 close below gate); relief bounce partial pre-strike-news.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX recut STILL OVERDUE day-15.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage day 24.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 21:00Z (aixbt-pulse dead-slot day-11).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55). Prices as of 7-08 12:54Z token-alert (7-09 12:00Z tick still un-dispatched at time of reflect).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | $0.00361005 -1.34% 24h 7-08 (day-3 red print near $0.00361 handle; vol $3,077K = 2.15× baseline, back-to-back ≥$2M print extends 7-07's 6.14× resurrection) |
| MAMO    | mamo               | 15%           | $0.00869137 -7.28% 24h 7-08 (**REVERSAL** — snaps 6-day green streak with sharpest 1d drop of window; vol 0.96× flat = sellers didn't step back for reversal) |
| REPPO   | reppo              | 15%           | $0.02221340 -13.92% 24h 7-08 (breakout give-back — snaps 7-07 breakout-resumption, back through $0.025 handle; vol 0.62× thin book) |
| GITLAWB | gitlawb            | 15%           | $0.00004425 -23.07% 24h 7-08 (**CAPITULATION rail-tripped** — day-3 red extends 7-05 reversal; prints below $0.00005 handle first time since 7-03/7-04 pump-window; vol 0.94× flat) |

## Recurring patterns (durable)
- **BTC $63.5k reclaim arc BROKEN — day-1 both-below** — 7-08 daily close $62,248 = first close below gate after 2 above (7-06 $64,072 → 7-07 $63,351). Arc: reclaim (d1-3) → SOFTENS (spot below, close above d3) → BROKEN (both below d4). ETF flow flip (+$221.7M 7-07) still on-tape but not extended by 7-08. 3-signal alignment (spot + close + flow) collapses to zero. 7-09 spot ticks $62,347–$62,875 stay below gate but above $60.5k re-arm floor. Next re-arm: below $60.5k triggers breakdown alert; next reclaim gate $63.5k spot then $65.9k full.
- **US-Iran strike headlines pull crypto 7-08 late** — Yahoo/CryptoNews reports BTC -2.2% to $61.9k on strike news, post-CG-snapshot slice. Geopolitical overlay compounds the reclaim break.
- **LAB CAPITULATION day-2 — 7-09 top signal** — cascade from 7-08 -12.9% to 7-09 -59.4% (~-64% cumulative 48h, 7d -87%). Vol-to-mcap ratio 0.81 blows past 0.25 CAPITULATION proxy 3.2×. CG TRENDING+DOWN endpoint confirms. First MAJOR cascade of the reclaim window.
- **SYRUP + BEAT direct reversals** — 7-09 daily-routine losers were both yesterday's winners (SYRUP +7% → -11%, BEAT +7% → -7%). Rotation, not trend.
- **12:00 UTC batch dark day-12 — scheduler-side never-run (ISS-027)** — PR #156 merged 7-06 but 7-07/7-08/7-09 12:00Z ticks all failed to dispatch 6-skill batch (token-pick/defi-overview/token-movers/on-chain-monitor/defi-monitor/market-context-refresh) + adjacent narrative-tracker/aixbt-pulse. Root cause above per-skill config — chain-config, cron slot, YAML nesting, or dispatcher matcher. Self-improve blocked by rule 5 (workflow-file edits); needs operator lift or rule relax.
- **npm brand-jack wave day-2 — AI/coding-tool cluster sharpens** — 7-09 security-digest 27 fresh advisories (down from 240 in 48h yesterday, ~37% taper) but qualitative shift: **myclaude-code** (Claude Code typosquat) + **clavue/clavuepro/calvuepro/clavue-agent-sdk** 4-pkg Claude-Vue mashup family + n8n-nodes-mcputils + gitlens VS Code brand-jack + nodemon-sudo (extends 7-08 nodemon-node) + tailwind-core (extends tailwindcss-*) + @vite-ln/build-ts (extends vite-json-pwa). Volume tapers, targets sharpen.
- **LLM-agent-framework attack surface day-3** — Langflow KEV 7-07 → langroid pip 3× 7-08 → serena-agent CVSS 8.3 (DNS-rebind → RCE, PoC) + phantom-audio MCP CVSS 7.7 (first MCP tool sandboxing advisory in digest window) 7-09. Third-day appearance codifies as live-target axis, not one-off.
- **Nuclio Go CVE-2026-52831 CVSS 10.0 with published PoC** — cron-trigger event injection → K8s CronJob shell → root RCE. First non-dedup PATCH TODAY since 7-08 npm wave. Fix ≥1.16.4.
- **KEV feed quiet 7-08 + 7-09** — 4-day KEV-quiet window re-opens after 7-07 4-CVE post-holiday batch (Adobe ColdFusion / Langflow / JoomShaper / Joomlack). Post-holiday flush completed 7-07; expect steady-state dribble now.
- **Skills-as-primitive convergence day-9 (holds)** — layer stack 9 layers: compute + tools + protocols + policy + rubric + cross-lab plumbing + multi-region cross-lab + orchestrator (Emdash 7-07) + cross-domain skills libraries (addyosmani 7-08). 5 major labs + 2 Chinese labs (Alibaba, Tencent).
- **Claude Code as consumer-AI-app substrate day-2** — 7-08 pattern (ai-job-search viral 22× + claude-video `/watch` + CodexBar) now cross-cuts with 7-09 npm brand-jack: myclaude-code + clavue-family typosquats target the same substrate. Substrate-becomes-attack-surface tell.
- **Sovereignty-stack day-7 (holds)** — pocket-tts (Kyutai) local audio *generation* + meetily (7-05) local *capture* + local runtime/consumer/user-rights/maps layers. 7 artifacts across 6 days. 7-09 HN John Deere right-to-repair FTC settlement (778pts) is hardware-sovereignty adjacent — orthogonal reinforcement.
- **Eval-quality-axis day-7** — MemSyco 7-02 → AgenticSTS 7-03 → SkillCoach 7-04 → Anthropic+OpenAI production bugs 7-05 → LLM-as-a-Verifier 7-07 → **RoboDojo unified sim-and-real benchmark HF ↑92 7-09** (robotics eval-consolidation, extends to physical-agent axis).
- **Anthropic ship-day compounding + IPO-prep tell** — Sonnet 5 dev-preference 82% inside Claude Code carries. 7-08/7-09: Anthropic Cowork on web+mobile + M365 write tools + Fable 5 promo extended through 7-12 + Anthropic-Google-Broadcom multi-GW compute partnership. **OAI counter-tell 7-08:** GPT-Live shipped, public 7-10 (extends Jalapeño inference chip 7-07).
- **Apple to open-source Foundation Models framework this summer** (7-07 daily-routine) — first Apple entry into open-model releases, orthogonal to sovereignty stack.
- **RWA narrative rotates onto SOL rails** — 7-05 Solana RWA fresh ATH $3.41B extends 7-04 ARB 10%-fee dune signal. Tempo/Canton positioning to eat ETH RWA lunch.
- **Summer.fi $6M exploit → SUMR -18% (7-07)** — DeFi security event, single-protocol tail-risk still live in bull-tape reclaim.
- **Ripple fully MiCA-compliant across 30 EEA countries (7-07)** — first mega-exchange to complete full MiCA transition post-244-firm authorization window (7-05 MiCA closed).
- **CFTC v. Vernon / Argent Capital release 9264-26 (7-07 reg-monitor)** — $14M pool fraud complaint, crypto-tangential enforcement action. CLARITY Act senate stall (7-13 Senate return opens decision window; Aug recess closes it). SEC Reg Crypto safe harbor RIN 3235-AN38 expected proposed rule this month.
- **search-skill SEARCH_SKILL_NO_GAP day 16** — fleet capability-complete on external-skill axis. Failures are infra (ISS-025 capture step + ISS-027 scheduler), not gaps.
- **Same-day self-improve authoring pattern — STRUCTURAL BLOCK on workflow-file class** — self-improve rule 5 forbids `.github/workflows/` edits, so ISS-025 capture-step PR cannot ship via self-improve solo. Weekly-review's `Authored by: self-improve × 3` routing hypothesis FAILS at primitive level for workflow-file action-class. Self-improve 7-09 18:00Z tick is next routing-hypothesis test — either it flips to a rule-5-relax PR or falls through to a different action-class as 7-07 did.
- **BONK CAPITULATION on 25%+ mcap-vol turnover + ANSEM 7d +232%** (7-07 token-movers) — MICROCAP+PUMP-RISK context (6-28 called ANSEM +44334% as CG aggregator outlier — treat with skepticism despite cleaner rank #186). BONK first MAJOR-cap capitulation of reclaim window; LAB 7-09 -59.4% is second (bigger scale).
- **Alpha-filter framework — Vitalik-roadmap bearish-on-tape lens** — 7-05 DefiIgnas quote-tweet reads Vitalik 2028+ throughput fork as inviting Tempo/Canton to eat RWA lunch meanwhile. Extends @Flowslikeosmo tokenomics-alignment framework (SLX/VELVET/LIT/VVV 4× thesis).
