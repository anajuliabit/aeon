# Long-term Memory
*Last consolidated: 2026-07-19*

## Current Goals
- **CLAUDE.md rule-5 codification T+2 SLIPPED** — self-improve 18:00Z 7-19 tests 2-consec exit-gate pattern ([[improvement-PR-queue-locks-self-improve]]). Rule-5 primitive n=4 = **auto-committed state drift** across any self-improve authored PR. Operator direct-author is sole reliable path.
- **ISS-025 capture-step PR T+3 day-4** — SLIPPED T-0 firm 7-16, T+1 7-17, T+2 7-18, now T+3. Operator direct-author against `.github/workflows/aeon.yml:479-495`. cost-report STUCK d6 ~137h is current manifest.
- **All 3 self-improve authored PRs CONFLICTING past stall gates** — PR #162 T+5 day-6 (~188h), PR #163 past 72h gate (~140h), PR #164 past 24h gate (~91h). Operator direct-author is sole reliable path per rule-5 extension.
- **cost-report STUCK d6 ~137h** — `last_status: dispatched` 2026-07-13T20:44Z, cf=5, sr=0.10, ~19d since last_success. ISS-025 signature. Operator PR unblocks.
- **12:00 UTC batch DARK day-22** — 9-skill cluster still frozen at 2026-06-28. Per-skill blockage confirmed 7-19 by token-alert 12:41Z + btc-levels 12:40Z clean fire at same slot (ISS-027 scheduler-side). **07:00Z morning-batch d3 DURABLE-RECOVER CONFIRMED 7-19** — daily-routine 07:14Z + morning-brief 07:00Z + thought-review 07:10Z all fired in tighter catch-up band than 7-18 (~14min vs ~25min = durable, not single-fire).
- **Operator on-chain config day-43** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Blocked.

## Recently Cleared
- **07:00Z morning-batch DURABLE-RECOVER CONFIRMED 7-19** — d3 fires ~14min late (tighter than d2's ~25min = durable, not single-fire catch-up). Resolves 7-18 open "d3 tests durable" question.
- **Weekly-review action #4** (Investment Advisor cancellation) SHIPPED-ON-TARGET via self-improve PR #164 authored 7-15 T-1 (PR CONFLICTING but investigation output landed).
- **BTC $63.5k arc softens then recovers** — 7-14 close $64,977 (reclaim); 7-15/16 confirm; 7-17/18 intraday $62,859-$64,292 slips but `reclaim63500Alerted=true` holds; 7-18 close $64,793; 7-19 spot $64,357-$64,737 through the day.

## Fleet Health
See [[fleet]] for full snapshot. Last skill-health hash b4d66e6c (7-18 18:14Z NOOP): 1 CRITICAL (cost-report) / 17 DEGRADED / 13 WARNING / 9 HEALTHY / 3 NO_DATA. 11 open issues (4 critical / 4 high / 3 medium). Sandbox-truncation family **day-27**. aixbt-pulse dead-slot **d22** (UTC-day rollover). weekly-shiplog + operator-scorecard chronic Mon miss.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, rule-5 extension.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns.
- [Market context](topics/market-context.md) — Baseline snapshot; refreshed each cycle.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).
- [XAI quota state](topics/xai-quota-exhausted.md) — Retired reference; cache-prefetch primary path.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 21:00Z (aixbt-pulse dead-slot d22 = state frozen).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. Anchors refreshed per 7-19 12:41Z print (0/12 checks fire → **2-consec zero-alerts day, watchlist in compression regime** as 4/4 signals fade to mechanical shapes: 2 thin-bid rebounds + 2 exhaustion-completes).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 7-19 +0.71%, vol **0.10× baseline** ($53K new window-low d2) = **distribution-flush extends d2 not exhaust-within-24h**; +0.66% log-to-log on falling participation = mechanical-rebound thesis fades |
| MAMO    | mamo               | 15%           | 7-19 -0.14%, vol 0.94× = **day-9 sustainable-shape holds** (4th-consec near-baseline 0.99/0.99/0.99/0.94, sub-1% drift = unmatched pause-at-mean signature) |
| REPPO   | reppo              | 15%           | 7-19 -0.27%, vol 0.78× = **fade-back-to-trend d5 completes with decelerating rate** (cascade -12.66% → -4.31% → -12.66% → -2.31% → -0.54% = mean-reversion exhausts) |
| GITLAWB | gitlawb            | 15%           | 7-19 +5.61%, vol 0.57× = **d6 thin-bid bounce-attempt breaks dead-flat pause** on falling participation, parallels WELL's mechanical-rebound; 6-day arc under-baseline (running mean 0.64×) |

## Recurring patterns (durable)
- **One-day-breakout-unwind n=5** (MORPHO/EIGEN/NEX/TIBBIR/DRV) — breakout must hold d2. BEAT/B n=2 dead-cat-with-legs exception.
- **LAB -95% zero-arc reference case** — 7d cumulative ~99.4%; sellers-exhaust heuristic 0/7. **BONK CAPITULATION d3 extends 7-19** (7d -30% deepens -27% → -30%) — LAB-reference-adjacent watch.
- **GITLAWB whipsaw-continuation-pause-bounce 6-day arc under-baseline** — mechanical whipsaw → trend-fade → dead-flat pause → thin-bid bounce (7-19 d6). Rail-breach n=1 single-session isolate.
- **Rule-5 primitive extends past workflow-file class (n=4)** — conflict source = **auto-committed state drift**, not file-class-specific. Operator direct-author is sole reliable path for any self-improve output.
- **Improvement-PR-queue-locks-self-improve** — 7-17 18:00Z self-improve exit-gated on 3+ open PRs (first-ever codification-deadline skip). 7-19 18:00Z tests 2-consec pattern.
- **Skills-primitive rail intermittent-resurface CONFIRMED day-19 REVISES 7-18 gap** — 17-day continuous run 7-13→7-17 → 7-18 break → 7-19 ui-skills reappears d3 sustained = **library-shape survives beyond continuous cadence as intermittent resurface**.
- **Small-MoE-frontier-close cluster n=3 → n=4 pending 7-27** — Muse Spark 1.1 + Sonnet 5 near-Opus + Bonsai-27B. **Kimi K3 confirmed live 7-16 launch** (2.8T open MoE + 1M ctx + Kimi Delta Attention, beats Fable 5 + GPT-5.6 Sol on front-end Arena, 40% cheaper than Opus 4.8) — open weights ship 7-27 = n=4 confirm.
- **Vendor-scope-typosquat pattern n=6+** — Replit + Sui/Mysten + AWS×2 + Proton crates.io + SYFT ACP + EdgeCommons npm + axios pair + trongrid pip. Broadens across ecosystems.
- **First real-package supply-chain compromise n=1** — `@injectivelabs/sdk-ts@1.20.21` wallet-credential stealer (2026-07-08, **10-day live-exposure window**, hooks `PrivateKey.fromMnemonic`/`fromHex`). Top-40 crypto project.
- **First-party-incumbent-alt-to-Anthropic-scope n=1 + release-catalyst 1-day-visibility CONFIRMED 7-19** — github/copilot-sdk v1.0.7 Java+Rust parity 7-16 15:22Z drove 17.9× 24h jump 7-18, drops off trending d2 7-19 = release-catalyst caps 1-day (distinct from viral-moment 5-day terminal shape).
- **MCP-server hardening rail n=5 in 96h** — langbot pip + mcp-documentation-server npm + n8n-mcp npm + MCP Python SDK 3-CVE + Prompty pip/npm/rust/nuget.
- **Cross-ecosystem-single-repo cluster n=6 durable weekly rail** — SiYuan Go + DIRAC pip + nebula-mesh Go + dd-trace 6-lang polyglot + MCP Python SDK + Prompty.
- **High-EPSS regime n=2 pauses at 1-day flat 7-19** — 7-17 Fortinet CVE-2026-39808 EPSS 0.842 + 7-18 gitea CVE-2026-27771 0.407; 7-19 no ≥0.4 EPSS (vllm pair 0.003 each). n=2 stops flat, doesn't extend to n=3.
- **KEV day-3 zero-cadence NEW 7-19** — 7-17/7-18/7-19 zero KEV adds = **first 3-consec-zero KEV window in memory** (7-13→7-16 fed 10 adds at 1-3/day). Aligns with BOD 26-04 T-0 crossing 7-19 for Fortinet + SharePoint 58644.
- **npm-malware wave complete cool-off d6=0 7-19** — 7-18 d5=22 regime-reaccel signal resolves as anomaly; 5-day wave arc closes 30→16→13→22→0.
- **Cross-day-single-package-pair-pattern n=1 NEW 7-19** — meta-ads-mcp CVE-2026-54549 (SSRF 7-18) + CVE-2026-54547 (auth-bypass 7-17 late) same package ~24h gap, single fix bump 1.0.115. Distinct from same-day cluster (Prompty 2 CVEs).
- **MCP-symbol-flow-invisible-Unicode class n=1** — vuln-scanner PVR GHSA-chjm-935c-cx8p (tirth8205/code-review-graph): `_sanitize_name()` ASCII 0x00-0x1F strip leaves Tag chars U+E0000-U+E007F + BiDi overrides intact through 30 MCP tools. **First LLM-tool-integration finding via PVR** — expands taxonomy past dep-CVE + argv-injection.
- **Watchlist-call reliability n=2** — copilot-sdk 7-17 drop-then-resolve 7-18 17.9× jump (call-resolves). **KAITO FADE-tag 24h-misfire NEW 7-19** — 7-18 daily-routine FADE tag on KAITO -5.7% reverses 24h later +12.5% (7d +37%). Reliability signal cuts both directions.
- **Consumer-tool viral-tail day-5 convergence n=2** — hallmark 4-day monotonic + OpenCut oscillating both cap day-5 = **5-day terminal for consumer-tool category**.
- **China-lab edge-inference cross-signal cluster n=2 NEW 7-19** — airllm (chinese-llm topics) 7.8× baseline + MoonshotAI/kimi-cli 1.87× baseline same trending day. References [[small-MoE-frontier-close]] Kimi K3 7-27 watchlist.
- **Feed-forward-replaces-iterative-optimization n=1 NEW 7-19** — lingbot-map (arxiv 2604.14141) = first foundation-model primitive that kills a specific iterative-optimization workload (3D bundle adjustment). Track for SLAM/optical flow/neural rendering analogs.
- **MCP-server local-first $0/query positioning n=1 NEW 7-19** — wigolo positions vs Exa/Tavily/Firecrawl paid APIs. First MCP-native cost-elimination pattern (parallels context-window-burn axis from code-review-graph).
- **LG-monitor OEM-channel-abuse novel n=1 NEW 7-19** — HN #1 (1094 pts) LG monitors silently install software via Windows Update. First trust-breaker outside package-registry space, rails-adjacent to vendor-scope-typosquat on broader trust-boundary axis.
- **BTC ETF regime-shift signal 7-19** — US spot BTC ETFs snap 10-day outflow streak with $221.7M inflow (biggest daily haul in 2 months) + FHFA orders Fannie/Freddie count crypto as mortgage asset + Better+Coinbase issue first Fannie-backed crypto mortgage = institutional-onramp firms.
- **BUILDon +61.5% BREAKOUT 7-19** — 7d +41% clean-tag both axes; 7-17 -5.9% loser d2 shape reverses hard. Watch d2 hold vs one-day-breakout-unwind pattern n=5.
- **HKUDS-cluster n=4** — Vibe-Trading + DeepTutor 5-consecutive-day trending presence. Lab-momentum-as-signal confirmed.
- **search-skill SEARCH_SKILL_NO_GAP day 23** — fleet capability-complete on external-skill axis. Failures = infra (ISS-025/027), not gaps. 7-20 mon-weekly tick extends d22→d23 (all 4 gap-derivation sources dry, zero-cost step-1 exit; last real external-skill install 2026-06-27 unlock-monitor).
