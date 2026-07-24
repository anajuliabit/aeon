# Long-term Memory
*Last consolidated: 2026-07-24*

## Current Goals
- **ISS-025 capture-step PR T+8 day-9 (3 days past 1-week slip)** — SLIPPED T-0 7-16 through T+8 7-24. Operator direct-author against `.github/workflows/aeon.yml:479-495`. Action-converter 7-21 15:20Z proposed pivot to `dangerouslyDisableSandbox` per upstream sandbox iss #53012 (excludedCommands does not exempt from network enforcement; allowedDomains ignored). Cost-report acute-failure branch cleared 7-20 19:08Z; capture-step primitive itself unshipped.
- **12:00 UTC batch DARK day-27** — 8-skill 6-28 cluster (defi-overview / token-pick / token-movers / narrative-tracker / market-context-refresh / fleet-control / on-chain-monitor / defi-monitor) still frozen. Per-skill blockage n=27 CONFIRMED via clean same-slot fires (token-alert + btc-levels both fire while cluster stays frozen = ISS-027 signature durable).
- **Operator on-chain config day-48** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Blocked.
- **H unlock T-1 fri jul 25 tomorrow** — 5.1× vol on $15.86M / 9.24% supply / investor+early-contributors cliff / 30d +72.6% textbook fade-pump asymmetric-downside cliff, biggest signal-real of quarter per 7-20 unlock-monitor. **Watch flag**: 7-24 morning-brief WebSearch surfaced potential ticker ambiguity (H vs HYPE — HYPE has zero-VC-allocation, next unlock aug 6); verify next unlock-monitor 7-27.
- **priorities.md 50d stale — round-number threshold cross 7-24** — last reviewed 2026-06-04; "Reppo: orquestra working" + "Aeon: ship the personal-stack PR" lines read as live-work-slipped (personal-stack PR = ISS-025 tracker). Operator-owned refresh.

## Recently Cleared
- **WELL vol-spike d2 FIRES 7-24 12:00Z** — first-ever back-to-back vol-spike-fires in watchlist history at 6.11× ($2,053.6K vs $336.2K baseline post-7-23-entering). Participation compounds +53% off yesterday's print while price fade shallows -3.31% → -1.33% = **accumulation-look strengthening d2**, distinct from distribution-shape. Baseline-drift codified: single outlier-print (7-23's $1.345M) lifts 5-window baseline ~4× overnight, reshapes gate-sensitivity for 5+ days forward.
- **3-day alert-fire streak 7-22→7-24** — GITLAWB counter-tape 24h-change → WELL vol-spike-only first-instance → WELL vol-spike-continuation first-ever back-to-back = [[alert-class-shift-3-regime]] firms across 3-day arc.
- **UB d4 unwind FIRES on 7-23 prediction 7-24** — 7-21 +16.6% + 7-22 +12.8% + 7-23 +13.1% + 7-24 -9.0% = **[[one-day-breakout-unwind]] rule reasserts at "3-day-sustain-max-before-d4-unwind" shape**. Exception cap holds at n=4. BUILDon d6 -12.1% extends compound-unwind to -32% off peak = 3-day compound slide (not 1-2 day tail).
- **PR #167 authored 7-23 18:21Z** — self-improve bash-`>`-redirect workaround. Rule-5 primitive n=2 same-cycle test lands positive under 1-open-PR queue (queue now 2 PRs: #165 d5+ dormant + #167 fresh, still under 3-PR gate). PR #166 authored + MERGED same-cycle 7-21 18:29Z (20min turnaround, first same-cycle self-improve authored+merged in fleet history; codified weekly-batch PR review cadence in CLAUDE.md).
- **cost-report CRITICAL → DEGRADED 7-21** — cf 8→0 via 7-20 19:08Z late-success. **Fleet 0 CRITICAL first time in memory-window** (hash 467ce959 stable through 7-24).
- **BTC $65,900 reclaim FIRES 7-21 09:29Z, holds 4-day** — spot $63,886-$66,563 window through 7-24 (spot dipped $63,886 17:16Z; re-arm gate at $60,500 not breached).
- **4-consec zero-alerts day CLOSES 7-22 12:29Z** — GITLAWB +16.53% counter-tape single-token break of n=4 streak.

## Fleet Health
See [[fleet]] for full snapshot. skill-health hash 467ce959 (7-20 18:47Z NOTIFY, stable through 7-24): 0 CRITICAL / 18 DEGRADED / 13 WARNING / 9 HEALTHY / 3 NO_DATA. 11 open issues. **15-consec heartbeat NOOP** through 7-24 14:13Z (~100h+ span since 7-19 09:17Z regime-onset). Sandbox-truncation family **day-32** (T+8 milestone). aixbt-pulse dead-slot **d27** (frozen 6-28 21:00Z; 12h cadence miss = 54 consec cycles). **Bash-tool `>` redirect regression n=5+ durable across 3 UTC-day span** (7-22 security-digest + 7-22 agent-buzz + 7-23 daily-routine + 7-23 security-digest + 7-24 daily-routine + 7-24 github-trending + 7-24 security-digest = **ISS-file threshold now firmly crossed**). Workaround chain: `curl -o` / Write tool / Read+Edit append validated across all fires. **GH API field rename** — `comments` → `commentsCount` in github-issues SKILL.md step 2 (pending patch).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, weekly-batch cadence.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns.
- [Market context](topics/market-context.md) — Baseline snapshot; refreshed each cycle.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).
- [XAI quota state](topics/xai-quota-exhausted.md) — Retired reference; cache-prefetch primary path.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 21:00Z (aixbt-pulse dead-slot d27 = state frozen).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. Anchors refreshed per 7-24 12:00Z print (1/12 checks fire → **WELL vol-spike d2, first-ever back-to-back**).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 7-24 -1.33%, vol $2.054M = **6.11× baseline d2 vol-spike-continuation FIRES** (participation compounds +53% off 7-23's $1.345M print, price fade shallows -3.31% → -1.33% = accumulation-look strengthening d2; first-ever back-to-back vol-spike-fires in watchlist history). 7-25 d3 = mean-reversion vs unprecedented n=3 streak test |
| MAMO    | mamo               | 15%           | 7-24 -0.42%, vol $825K = 0.88× baseline = **1st sub-baseline print after 3-consec near-baseline** post-fracture, price hold tightens (24h fade shallows -2.46% → -0.42% = tightest hold in 4-day sequence, orderly consolidation d3) |
| REPPO   | reppo              | 15%           | 7-24 -4.54%, vol $80K = 0.84× baseline = **10th-consec under-baseline print** with slight participation lift off 7-23 window-low, drought extends d10 with continued price fade |
| GITLAWB | gitlawb            | 15%           | 7-24 -7.06%, vol $339K = 1.69× baseline = **first above-baseline print since watchlist add** breaks 10-consec under-baseline streak; above-baseline vol on price-fade continuation = **distribution-shape on cliff-reclaim give-back d2**; d3 tests fade-vs-floor |

## Recurring patterns (durable — brief pointers; details in topic files)
- **Breadth-regime 4-shape taxonomy in 4-day window 7-24** — broad-risk-on 87/100 +3.0% (7-21) → counter-tape compression 24/100 -0.35% (7-22) → neutral-rebound 45/100 +0.1% (7-23) → tilted-red-compression 20/100 -0.7% (7-24). 25pt breadth compression 7-23→7-24 = **second one-day-cross-hemisphere-breadth-swing in 3 days** (both compression direction, different magnitudes). Details in [[crypto]].
- **[[one-day-breakout-unwind]] rule reasserts "3-day-sustain-max-before-d4-unwind" 7-24** — UB d4 fires on 7-23 prediction; BUILDon d6 extends compound-unwind to -32% off peak. Exception cap holds at n=4.
- **BEAT 3-day sustained-accelerating shape NEW 7-24** — 7-22 +17.6% + 7-23 +3.9% + 7-24 +28.3% (d2→d3 accelerates 7.3×) = distinct from BUILDon flat-sustain (which decelerated pre-unwind). Pattern-class candidate: "accelerating-3-day-sustain-then-?" — watch d4 tomorrow.
- **[[alert-class-shift-3-regime]] firms 7-24** — 3-day alert-fire streak validates 3-regime taxonomy: zero-alert compression (7-18→7-21) · counter-tape 24h-change (7-22 GITLAWB) · vol-spike-only (7-23 WELL) · vol-spike-continuation (7-24 WELL first-ever back-to-back). Baseline-drift primitive codified.
- **Skills-primitive rail 6-shape taxonomy 7-24** — practitioner (mattpocock/skills) + workspace-orchestration (block/buzz) + coding-single-purpose (ayghri) + physical-world (earthtojake) + vendor-catalog (ComposioHQ dropped) + first-party (copilot-sdk). Skills-primitive rail resurfaces d1 after 7-23 dark.
- **Agent-as-equal-member workspace primitive NEW 7-24** — block/buzz first workspace where agents are cryptographically-signed equal members via Nostr, not humans-with-bots. Extends [[agent-as-economic-actor]] into team-coordination layer.
- **Agent-shared browser primitive NEW 7-24** — citrolabs/ego-lite first browser purpose-built for parallel human+agent workflows via isolated Spaces sharing Chrome auth. Extends [[agent-callable-desktop-tool]] rail into browser-native.
- **worldmonitor viral-moment re-feature primitive tail-behavior validates 7-24** — 1,295 (7-22) → 4,139 (7-23 HOLDOVER re-feature) → 3,175 (7-24 -23% fade). Clears d1 re-feature threshold but d2 fades = **peak not sustain**. First full validation of HOLDOVER re-feature primitive both entry (7-23) and exit (7-24) sides.
- **code-review-graph 6-day plateau-then-fade shape COMPLETES 7-23** — 74→355→663→1,833→1,925→882 = accelerating-4-day + flat-hold-1-day + fade-onset-1-day. 3-class viral taxonomy firms: (a) 1-day-visibility · (b) 4-5-day oscillating-tail · (c) 6-day accelerating-plateau-fade.
- **npm-malware 45-batch d1 NEW 7-24** — largest single-day npm-malware batch in memory-window (prior 7-21 96-batch pip). fs-extra-core (~30M weekly-DL fs-extra typosquat highest-blast-radius) + vue-demi-fix + fastify-bundler + bcryptjs scope-squat pair + Solana bs58 typosquat + Adobe AEM/IO Commerce + ethers-* trio = [[wallet-credential-stealer-supply-chain]] rail extends n=4 → n=~10+ within 24h. Pattern regime **not slowing**.
- **[[AI-framework-attack-surface]] extends 7-24** — CVE-2026-59822 LiteLLM MCP-auth-bypass n=2 pip-tracked following Langflow RCE KEV (CVE-2026-0770 added 7-21) = two consecutive-week AI-framework CVEs in pip, attack-surface expansion beyond one-lab isolated event. LiteLLM not-installed via grep verification pending.
- **[[single-project-mass-disclose]] extends n=3 7-24** — n8n workflow-automation 24 CVEs in ~2h window 7-22. Feed-shape distortion durable across 3 project types (image-lib Pillow / git-forge Gitea / workflow-automation n8n) in 5-day span.
- **KEV cadence 3-regime NEW 7-24** — 4-day zero (7-17→7-20 artifact-not-durable) + burst (7-21/7-22) + **quiet-2day** (7-23/7-24). Watch 7-25.
- **[[list-digest-grok-cache-lag-day-old-window]] extends n=2 same-list 7-24** — 7-22 17:44Z returned only 7-21 tweets, 7-24 returned only 7-23 tweets. Cache-lag rail firms distinct from empty-list-day noise. 7-25 tests n=3 durability.
- **First Rust-majority slate in github-trending memory-window 7-24** — 3/4 Rust (block/buzz + Automattic/harper + Pumpkin drop); JavaScript ego-lite sole non-Rust survivor. Watch d2 for continuation or Rust-cluster-day artifact.
- **Grammarly-alternative n=1 NEW 7-24** — Automattic/harper first offline+privacy-first grammar tool to trend; editor-native LSP, no cloud round-trip.
- **Kimi K3 shipped 7-16 CORRECTION 7-24** — WebSearch confirms Moonshot Kimi K3 already-shipped 7-16 (2.8T MoE 1M-ctx native vision). Prior MEMORY "Kimi K3 open-weights ship 7-27 T-5" was calendar-drift; **DeepSeek V4 stable 7-24** stands as sole major 3-day-window event. [[small-MoE-frontier-close]] rail hit earlier than planned.
- **DeepSeek legacy API deprecation 7-24 15:59Z** — `deepseek-chat` + `deepseek-reasoner` legacy endpoints route to `deepseek-v4-flash` today. No direct Aeon impact.
- **[[LLM-solves-open-math]] arc extended to n=3-lab 5-day 7-23** — Fable Alpöge Jacobian 7-19 → Tao Jacobian digest 7-21 → OpenAI unreleased sandbox-incident 7-22 → Tao ChatGPT convo 7-23 (793pts d5). Containment-failure dimension via authoritative-writer-endorsement (Simon Willison "science fiction that happened").
- **Vendor-scope-typosquat pattern n=7+** — Replit + Sui/Mysten + AWS×2 + Proton crates.io + SYFT ACP + EdgeCommons npm + axios + trongrid + @vite-js (@vitejs frontend build primitive scope).
- **First real-package supply-chain compromise n=1** — `@injectivelabs/sdk-ts@1.20.21` wallet-credential stealer (2026-07-08, 10-day live-exposure).
- **Strategic-corporate-as-lead-on-megaround rail n=6 across 3 weeks** — Aramco/Together + National Grid/Joulent + Salesforce/8090 + Toyota/Walden + Motorola/Brinc + Alibaba/PixVerse. VC-displacement on >$100M cap-table lead-seat.
- **FTX 5th distribution jul 31 = $900M** — court-ordered creditor payout, largest single supply event of quarter; headline lock for 7-27 unlock-monitor.
- **Search-skill NO_GAP durability rail day-27** — fleet capability-complete on external-skill axis. Failures = infra (ISS-025/027), not gaps. Last real external-skill install 2026-06-27 unlock-monitor.
- **Meta-aeon signal 7-21** — Claude Code v2.1.181 = Bun's Rust port shipped 6-17 (Zig→Rust rewrite via dozens of parallel Claude Code sessions). Architecture-adjacent to Aeon's fleet + skills + parallel sessions.
