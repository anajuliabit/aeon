# Long-term Memory
*Last consolidated: 2026-07-20*

## Current Goals
- **ISS-025 capture-step PR T+4 day-5** — SLIPPED T-0 firm 7-16, T+1 7-17, T+2 7-18, T+3 7-19, now T+4. Operator direct-author against `.github/workflows/aeon.yml:479-495`. cost-report **STUCK→FAILED d7 state-change 7-20 13:24Z** (cf 5→8 in 24h) with 3rd-consec-Mon-weekly-miss n=3 durable-pattern (last_success 6-29, missed 7-6/7-13/7-20).
- **12:00 UTC batch DARK day-23** — 8-skill 6-28 cluster still frozen. 7-20 12:57Z per-skill blockage n=23 confirmed via clean same-slot fires (token-alert + btc-levels + cost-report all fired, ISS-027 signature).
- **Operator on-chain config day-44** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Blocked.

## Recently Cleared
- **2 self-improve PRs CONFLICTING past stall gates DONE 2026-07-20** — PR #163 fix(skill-security-scan) MERGED 17:11Z + PR #164 fix(investment-advisor) MERGED 21:50Z, resolving the residual queue after PR #162 landed 14:16Z. Full triple-PR self-improve queue cleared in a single day; PR #165 (docs skill-graph) is the sole remaining open PR and is docs-scope not self-improve. Rule-5 exit-gate primitive holds under full-sweep test.
- **PR #162 MERGED 7-20** — commit `e525536 fix(daily-routine): tighten XAI fallback rules for quota/sandbox/error` landed on main, first self-improve authored merge since rule-5 primitive extension. Reduces triple-PR queue → 2 CONFLICTING.
- **CLAUDE.md rule-5 codification SHIPPED via skill exit-gate 7-19 18:32Z** — `improvement-PR-queue-locks-self-improve 2-consec` codified. Self-improve exits when 3+ open PRs. Weekly-review action #3 ships via skill-side gate not CLAUDE.md-edit (T+2 late).
- **weekly-shiplog 3-consec-Mon-miss test lands NEGATIVE 7-20 10:55Z** — SHIPLOG_OK fires clean, mon-cluster health improves d1 vs cost-report failed. Same-slot differential = per-skill sandbox behavior not per-slot scheduler.
- **Weekly-review action #4** (Investment Advisor cancellation) SHIPPED-ON-TARGET via self-improve PR #164 (CONFLICTING but investigation landed).

## Fleet Health
See [[fleet]] for full snapshot. Last skill-health hash b4d66e6c (7-18 18:14Z NOOP, 4-consec heartbeat NOOP through 7-20 15:19Z = flat regime durable): 1 CRITICAL (cost-report cf=8 FAILED) / 17 DEGRADED / 13 WARNING / 9 HEALTHY / 3 NO_DATA. 11 open issues. Sandbox-truncation family **day-28**. aixbt-pulse dead-slot **d23** (UTC-day rollover). 07:00Z morning-batch d4 catch-up widens on Mon-load-day (~54-79min lateness vs 7-19 ~14-41min).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, rule-5 extension.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns.
- [Market context](topics/market-context.md) — Baseline snapshot; refreshed each cycle.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).
- [XAI quota state](topics/xai-quota-exhausted.md) — Retired reference; cache-prefetch primary path.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 21:00Z (aixbt-pulse dead-slot d23 = state frozen).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. Anchors refreshed per 7-20 12:57Z print (0/12 checks fire → **3-consec zero-alerts day, watchlist compression regime d3 durable** with 4/4 signals resolving to mechanical shapes: distribution-drought × 2 + pause-at-mean + thin-bid-fade-back-cliff).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 7-20 -0.15%, vol **0.14× baseline** ($66K lifts off d2 window-low but 7th-consec under-baseline) = **distribution-drought d3 extends**; mechanical-rebound thesis stays absent |
| MAMO    | mamo               | 15%           | 7-20 +0.97% (+1.22% log-to-log = first non-flat print in 5 days), vol 0.97× = **day-10 pause-at-mean holds**, 5th-consec near-baseline (0.99/0.99/0.99/0.94/0.97), band-lift breaks 4-day sub-1% streak, tests d11 fracture-or-revert |
| REPPO   | reppo              | 15%           | 7-20 -0.73%, vol **0.30× baseline** ($58K) = **exhaustion-drought d6**, vol cliff-drops from 0.78× to 0.30× in 24h as 5-day mean-reversion cascade terminates, new window-low |
| GITLAWB | gitlawb            | 15%           | 7-20 -10.59% (sub-15% miss by 4.4pt), vol 0.88× ($243K = 1.38× yesterday) = **thin-bid-rebound-then-fade-back-cliff n=1 confirms** — yesterday's +5.61% bounce reverses on rising volume within 24h, volume-confirmed distribution |

## Recurring patterns (durable)
- **One-day-breakout-unwind extends to n=6-7 with 3 exceptions 7-20** — TRAC -10% reverses 7-19's +14.7% (n=6), XEC -5.7% reverses 7-19's +4.1% d2 (n=7 delayed-variant); BUILDon +24.4% d2 clean-continuation on 7d +118% = 2nd exception besides BEAT/B dead-cat. Exception-set grows faster than confirmations = pattern softens toward "one-day-breakout-with-mixed-outcome".
- **Thin-bid-rebound-then-fade-back-cliff n=1 NEW 7-20** — GITLAWB +5.61% bounce d6 reverses -10.59% on rising volume within 24h = **inverted mirror of [[one-day-breakout-unwind]]** (single-day mechanical reversal but bounce→cliff-down not breakout→fade-down). Both are mechanical-reversal single-session shapes.
- **LAB -95% zero-arc reference case** — 7d cumulative ~99.4%; sellers-exhaust heuristic 0/7. **BONK CAPITULATION d4 7-20** dead-cat bounce +2.6% after 3-day capitulation, watch for LAB-reference-adjacent.
- **Rule-5 primitive n=4 = auto-committed state drift** across workflow + SKILL.md + scripts/ file classes. Operator direct-author sole reliable path for any self-improve authored PR. **Fix ships via skill-side exit-gate primitive not CLAUDE.md-edit** (7-19 18:32Z codification).
- **Improvement-PR-queue-locks-self-improve 2-consec CODIFIED 7-19 18:32Z** — 7-17 18:00Z first-ever codification-deadline skip → 7-19 18:00Z tests 2-consec → self-improve gate written into SKILL.md as durable primitive.
- **Small-MoE-frontier-close cluster n=4 CONFIRMED pre-ship 7-27** — Muse Spark 1.1 + Sonnet 5 near-Opus + Bonsai-27B + **Kimi K3** (2.8T open MoE + 1M ctx + Kimi Delta Attention, beats Fable 5 + GPT-5.6 Sol front-end Arena, 40% cheaper than Opus 4.8). Open-weights ship 7-27 = d7 out from 7-20.
- **China-lab edge-inference cluster n=3 firms 7-20** — airllm + MoonshotAI/kimi-cli + **Qwen 3.8** (2.4T MoE multimodal, "second only to Fable 5" own-benchmark, first Alibaba multimodal >1T params). Same-week trending-pipeline. Watch n=4 within 7d for rail-durable.
- **LLM-solves-open-math n=2 NEW durable 7-20** — GPT-5.6 convex-opt 7-18 (30-yr gap) + **Claude Fable 5 Jacobian counterexample** (Alpöge public X thread, under active technical challenge on properness). Both HN top-5. Watch n=3 within 7d.
- **Meta-aeon signal n=1 NEW 7-20** — Claude Code v2.1.181 = Bun's Rust port shipped 6-17 (Zig→Rust rewrite via dozens of parallel Claude Code sessions per Bun team writeup, 10% startup on Linux). Architecture-adjacent to Aeon's own fleet + skills + parallel sessions.
- **Agent-memory-as-first-class primitive n=2 NEW 7-20** — cognee (self-hosted knowledge-graph memory) + jcode (embedded semantic memory + cosine-retrieval) same trending day = distinct product category from prior [[code-review-graph]] MCP-context-burn axis. Watch n=3 within 7d.
- **Competitive-positioning-vs-Claude-Code cluster n=2 NEW 7-20** — copilot-sdk 7-18 first-party-incumbent-scope + jcode "245× faster than claude code" 7-20 3rd-party competitive-scope within 3 days.
- **Pre-launch integration pattern n=1 NEW 7-20** — OmniRoute wires Kimi K3 7 days before open-weights ship 7-27 = distinct from post-launch adoption.
- **Vendor-scope-typosquat pattern n=7+** — Replit + Sui/Mysten + AWS×2 + Proton crates.io + SYFT ACP + EdgeCommons npm + axios + trongrid + **@vite-js** (7-20 GHSA-x4cp-w826-x466 + GHSA-6x4h-wrvq-m68h = @vitejs frontend build primitive scope, highest-blast-radius add since Injective).
- **First real-package supply-chain compromise n=1** — `@injectivelabs/sdk-ts@1.20.21` wallet-credential stealer (2026-07-08, 10-day live-exposure).
- **MCP-server hardening rail n=5 in 96h** — langbot + mcp-documentation-server + n8n-mcp + MCP Python SDK 3-CVE + Prompty.
- **Cross-ecosystem-single-repo cluster n=6 durable weekly rail** — SiYuan + DIRAC + nebula-mesh + dd-trace + MCP Python SDK + Prompty.
- **KEV day-4 zero-cadence extends 7-20** — first 4-consec-zero-KEV window in memory (7-13→7-16 fed 10 adds at 1-3/day). Aligns post-BOD 26-04 T+1 crossing. **d5 tomorrow tests durable-vs-artifact regime**.
- **GH reviewed advisory feed 48h silent NEW 7-20** — 0 critical/high/medium published 7-18 15Z → 7-20 15Z (unprecedented in 4-week window). 7-17 was 12-high-burst. Tests 72h silent vs first-post-silence burst on 7-21.
- **npm-malware wave RESUMES 7-20 as 1-day pause not close-of-wave** — revises 7-19 d6=0 close-of-wave call as scan-window artifact (4 pkgs landed 23:53-23:55Z after 7-19 14:20Z scan). Arc extends 7-day: 30→16→13→22→0→4→7.
- **Scanner-testbed-advisory-pollution n=2 NEW 7-20** — 75 @gocortexio/npmgremlinbox-* + 2 vybscan-testbed-* = 77 testbed pkgs single day. **Filter rule: exclude `@gocortexio/*` + `vybscan-testbed-*` + `*-poc-*` from real-wave counts**.
- **MCP-symbol-flow-invisible-Unicode class n=1** — vuln-scanner PVR GHSA-chjm-935c-cx8p (tirth8205/code-review-graph): `_sanitize_name()` ASCII strip leaves Tag chars U+E0000-U+E007F + BiDi overrides intact through 30 MCP tools.
- **Skill-security-scan sandbox-block n=8 durable** — `scan.sh --all --json` blocked 2026-05-25 through 2026-07-20 (8 consecutive scans), inline-grep-fallback used every time. 4 HIGH persistent in `aeon.yml:L86/L94/L96/L812`, L812 5-consec-scan zero-line-drift stable.
- **Unlock-monitor defillama+dropstab d2 durable-fail** — same 2-source failure pattern 7-13 → 7-20 (defillama 403 + dropstab masked-dates). Potential sandbox-block not source-side outage.
- **Watchlist-call reliability n=2 both directions** — copilot-sdk 7-17 drop-then-resolve 7-18 17.9× jump (call-resolves) + **KAITO FADE-tag 24h-misfire 7-19 fully reverses 7-20** (+3.7% / 7d +44% = 7-18 FADE tag reverses hard, watchlist-call-fails signal firms d2).
- **BUILDon +61.5% BREAKOUT 7-19 → +24.4% d2 clean-hold 7-20** — 7d +118% = clean-continuation, first exception besides BEAT/B dead-cat.
- **Strategic-corporate-as-lead-on-megaround rail n=6 across 3 weeks 7-20** — Aramco/Together + National Grid/Joulent + Salesforce/8090 + Toyota/Walden + Motorola/Brinc + Alibaba/PixVerse. VC-displacement on >$100M cap-table lead-seat continues.
- **NVIDIA-hedging-open-stack n=1 NEW 7-20** — NVIDIA Ventures on Prime Intellect $130M Series A (decentralized training). Compute-incumbent participating in exact stack that threatens its data-center monopoly. Watch n=2 within 4 weeks.
- **Agent-stack-lower-layers cluster n=3 same-window NEW 7-20** — Fireworks AI $1.505B Series D @ $17.5B (inference, 4.375× UP vs $4B Series C Oct 2025) + Prime Intellect $130M Series A (training) + Oak $60M seed (agent-native IAM). Capital deliberately clustering at primitives-below-the-model layer.
- **x402 Foundation operational-launch 7-14 with 40 members** — Visa/Mastercard/AmEx/Stripe/Google/AWS/Shopify/Cloudflare/Coinbase/Ripple/Injective. 75M txns / $24M over 30d. Tier-3 agentic-payments macro trigger.
- **Exchange-token-absorption-metric-degenerates n=2 7-20** — GT 21.24× (7-20) + CONX 456× (7-13). Framework breaks on exchange-token low-off-CG-volume shape; file as watch-for-wick not real crisis.
- **BTC ETF regime firms 7-20** — $273M net inflow over 2 weeks breaks 8-week $8B+ outflow streak. 7-17 net-inflow day $132.3M IBIT-led + ETH ETFs $36.7M ETHA-led. Scale still "peanuts" per Coindesk but streak broken.
- **FTX 5th distribution jul 31 = $900M** — court-ordered creditor payout, record date jun 16 passed = largest single supply event of quarter, headline lock for 7-27 unlock-monitor.
- **H jul 25 unlock CRISIS-real 5.1× vol** — investor+early-contributors cliff, 9.24% supply, 30d +72.6% textbook fade-pump. Asymmetric-downside cliff test.
- **Search-skill NO_GAP durability rail day-23** — fleet capability-complete on external-skill axis. Failures = infra (ISS-025/027), not gaps. 7-20 mon-weekly tick extends d22→d23 (all 4 gap-derivation sources dry, zero-cost step-1 exit; last real external-skill install 2026-06-27 unlock-monitor).
