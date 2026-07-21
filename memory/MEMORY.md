# Long-term Memory
*Last consolidated: 2026-07-21*

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
- **ISS-025 capture-step PR T+5 day-6** — SLIPPED T-0 firm 7-16 → T+5 today. Operator direct-author against `.github/workflows/aeon.yml:479-495` sole reliable path. cost-report late-success 7-20 19:08Z clears d7 acute-failure branch; sandbox-truncation family day-29 still durable across defi-overview/token-pick/search-skill.
- **Self-improve queue EMPTY of CONFLICTING** — PR #162 MERGED 7-20 14:16Z, PR #163 MERGED 7-20 17:11Z, PR #164 MERGED 7-20 21:50Z = triple-queue clears in single day. Only PR #165 (docs skill-graph) 2d old under stall gate. **Rule-5 primitive n=4 downgrades to n=2 partial-conflict class** after 3/4 auto-committed-drift PRs land clean.
- **12:00 UTC batch DARK day-24** — 8-skill 6-28 cluster still frozen. Per-skill blockage n=25 confirmed via clean same-slot fires (token-alert 12:00Z + btc-levels 12:15Z + security-digest 14:00Z fire clean while 8-skill cluster stays frozen = ISS-027 signature).
- **Operator on-chain config day-45** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Blocked.

## Recently Cleared
- **Triple self-improve PR queue CLEARS in single day 7-20** — #162 daily-routine (14:16Z) + #163 skill-security-scan (17:11Z) + #164 investment-advisor (21:50Z) all MERGED. First 3-PR same-day sweep in fleet history. Weekly-review action #4 SHIPPED via #164 investigation landing.
- **cost-report late-success 7-20 19:08Z** — 3rd-consec-Mon-weekly-miss test lands NEGATIVE at n=2 not n=3 (missed 7-6/7-13, succeeded 7-20 via late-dispatch at 18:45Z ~12h post-scheduled). Fleet CRITICAL flag lifts pending next skill-health tick formal read.
- **BTC $65,900 reclaim FIRES 7-21 09:29Z** — first time spot ≥ $65,900 in current regime, reclaim65900Alerted set true (re-arm sub-$60,500 only). Spot $66,241 → $66,563 through the day, 2-week high.
- **CLAUDE.md rule-5 codification SHIPPED via skill exit-gate 7-19 18:32Z** — `improvement-PR-queue-locks-self-improve 2-consec` codified. Self-improve exits when 3+ open PRs. Rule-5 evidence downgrades post-3/4 clean-merge sweep.
- **Weekly-review action #4** (Investment Advisor cancellation) SHIPPED-ON-TARGET via self-improve PR #164 MERGED same day.

## Fleet Health
See [[fleet]] for full snapshot. Last skill-health hash 467ce959 (7-20 18:47Z NOTIFY, classification byte-identical to 7-19 18:32Z NOOP): 1 CRITICAL (cost-report — lifts pending 18Z 7-21 tick) / 17 DEGRADED / 13 WARNING / 9 HEALTHY / 3 NO_DATA. 11 open issues. **7-consec heartbeat NOOP** through 7-21 15:11Z = flat regime durable across full UTC-day + mid-day pivot. Sandbox-truncation family **day-29**. aixbt-pulse dead-slot **d24** (UTC-day rollover). 07:00Z morning-batch catch-up-band narrows on tue vs mon-load-day (7-21 daily-routine 07:15Z on-time vs 7-20 07:54Z ~54min late).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, rule-5 primitive downgrade.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns.
- [Market context](topics/market-context.md) — Baseline snapshot; refreshed each cycle.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).
- [XAI quota state](topics/xai-quota-exhausted.md) — Retired reference; cache-prefetch primary path.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 21:00Z (aixbt-pulse dead-slot d24 = state frozen).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. Anchors refreshed per 7-21 12:00Z print (0/12 checks fire → **4-consec zero-alerts day, watchlist compression regime d4 by alert-count** but **cracks by shape-count** on broad-tape risk-on lift — 3/4 tokens print constructive shape-shifts sub-threshold).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 7-21 +0.52%, vol **0.285× baseline** ($134K = 2.03× yesterday's $66K) = **distribution-drought softens d4** with faint bid re-entry on broad-tape lift; 8th-consec under-baseline print but first meaningful lift off floor |
| MAMO    | mamo               | 15%           | 7-21 +7.91% (l2l +7.92%), vol 1.118× ($1,006K) = **pause-at-mean FRACTURES d11** — 4.4pt jump breaks 10-day compression cleanly, first above-baseline vol print in 6 days confirms real bid not thin-bid drift, sub-15% by 7.1pt but breakout-attempt shape |
| REPPO   | reppo              | 15%           | 7-21 +4.83% (l2l +5.06%), vol 0.807× ($120K = 2.08× yesterday's $58K) = **exhaustion-drought BREAKS d7** — first positive 24h print since fade-cascade started 5 days ago, 6×-jump on real bid arrests post-exhaustion phase into re-accumulation attempt |
| GITLAWB | gitlawb            | 15%           | 7-21 -2.09% (l2l -2.09%), vol 0.810× ($199K = 0.82× yesterday's $243K) = **cliff-back-under d2 fade decelerates** — drift compresses 5× vs prior tick as distribution exhausts, 7-day roundtrip stays below starting price |

## Recurring patterns (durable)
- **Compression regime cracks by shape-count on broad-tape risk-on lift n=1 NEW 7-21** — 4-consec zero-alerts day extends by count, but 3/4 tokens print constructive sub-threshold shape-shifts (MAMO breaks 10-day pause with real bid, REPPO breaks 6-day drought with 6× 24h, WELL bid doubles off floor); only GITLAWB continues fade. Broad-tape catalyst = top-100 87/100 green top-50 median +3.0% (61pt breadth expansion vs 7-20 26/100). Tests 7-22 for n=2 extension across 2+ tokens.
- **One-day-breakout-unwind extends to n=6-7 with 4 exceptions 7-21** — BUILDon +12.1% d3 clean-continuation extends exception-set (BEAT/B + BUILDon d2 + BUILDon d3 + XEC-delayed = **4 exceptions vs n=6-7 confirmations**). Pattern-shape codifies as **"one-day-breakout-with-mixed-outcome"** — exception-set trajectory matches confirmation-set.
- **Thin-bid-rebound-then-fade-back-cliff n=1 tests d2 hold 7-21** — GITLAWB fade-decelerates 5× (drift compresses -10.59% → -2.09%) as distribution exhausts; d3 tomorrow tests cliff-under-hold vs drift-back-to-mean pattern tail.
- **BUILDon d3 clean-continuation forces pattern-shape codification** — 7d +125% after 7-19 +61.5% + 7-20 +24.4% + 7-21 +12.1% = 3-day sustain, biggest exception-set contributor to [[one-day-breakout-unwind]] softening.
- **NIGHT capitulation -26.4% 7-21 on 38% mcap-turnover $123M vol / $324M mcap** — 7d -33% = single-session capitulation candidate for [[LAB-reference-adjacent]] arc-watch.
- **LAB -95% zero-arc reference case** — 7d cumulative ~99.4%; sellers-exhaust heuristic 0/7. BONK dead-cat d5 +10.8% 7-21 continues LAB-reference-adjacent tail.
- **Rule-5 primitive n=4 downgrades to n=2 partial-conflict class 7-20** — 3/4 auto-committed-drift PRs (#162 + #163 + #164) land clean same day via operator batch-merge decision; only #164's CONFLICTING flag was durable prior. Skill-side exit-gate primitive (7-19 codification) remains fully-load-bearing.
- **Improvement-PR-queue-locks-self-improve 2-consec CODIFIED 7-19 18:32Z** — Self-improve gate written into SKILL.md as durable primitive. Tests unblocked-self-improve authoring quality on next fire (odd-day 7-21 18:00Z fires post-queue-clear).
- **Code-review-graph 4-day viral arc n=1 durable NEW 7-21** — tirth8205/code-review-graph on github-trending: 74 (7-18) → 355 (7-19) → 663 (7-20) → 1,833 (7-21) = **25× day-1 pace on d4 with re-feature under viral-moment clause**. First observed 4-day sustained-accelerating monotonic shape in skill history. Extends prior 1-day-visibility (release-catalyst) + 4-5-day-viral-tail (oscillating) shapes with new "sustained-accelerating monotonic" class. Watch d5 tomorrow for fade-vs-continue.
- **Book-as-code-primitive n=1 NEW 7-21** — bojieli/ai-agent-book (Chinese-language agent engineering book) trends #1 at 4,434 today = **109× baseline** (created 2025-09-09, 316d). Ships book text + compiled PDF + per-chapter accompanying code = distinct from awesome-list resource-collection noise pattern + distinct from tutorial/learn-X shape. Watch analog within 30d for pattern durability.
- **Chinese-language agent-primitive rail n=4-5 durable extends 7-21** — kimi-cli (7-19 → 7-21 3-day continuation) + airllm (7-19) + Qwen 3.8 (7-20 daily-routine) + ai-agent-book (7-21 #1) + AstrBot (7-21 37k mature returning). Watch 3rd distinct sub-category (dataset/benchmark/protocol) within 7d for rail-durable at frame-level.
- **Small-MoE-frontier-close cluster n=4 pre-ship demand overshoots infra 7-21** — Moonshot AI **PAUSES new Kimi subscriptions** — Kimi K3 demand near-capacity limits in 48h per @kimi_moonshot, 6 days before open-weights ship 7-27 = **new leg of rail (product-launch-before-weights pattern)**. Prior rail: Muse Spark 1.1 + Sonnet 5 near-Opus + Bonsai-27B + Kimi K3.
- **China-lab edge-inference cluster n=3 firms at macro-frame level 7-21** — HN top-of-day "China's open-weights AI strategy is winning" (1066pts werd.io) confirms cluster n=3 at macro-thesis frame not just repo-trend level. Full cluster: airllm + MoonshotAI/kimi-cli + Qwen 3.8 (2.4T MoE multimodal).
- **LLM-solves-open-math n=2 durable 7-21** — GPT-5.6 convex-opt (7-18, 30-yr gap) + Claude Fable 5 Jacobian counterexample (7-19, Alpöge public X thread, properness-challenge still-open). Both HN top-5. Watch n=3 within 7d.
- **Meta-aeon signal n=1 7-21** — Claude Code v2.1.181 = Bun's Rust port shipped 6-17 (Zig→Rust rewrite via dozens of parallel Claude Code sessions per Bun team writeup, 10% startup on Linux). Architecture-adjacent to Aeon's own fleet + skills + parallel sessions.
- **Agent-memory-as-first-class primitive n=2 7-21** — cognee + jcode same trending day = distinct product category from [[code-review-graph]] MCP-context-burn axis. Watch n=3 within 7d.
- **Competitive-positioning-vs-Claude-Code cluster n=2 7-21** — copilot-sdk 7-18 first-party-incumbent-scope + jcode "245× faster than claude code" 7-20 3rd-party competitive-scope within 3 days.
- **Pre-launch integration pattern n=1 7-21** — OmniRoute wires Kimi K3 7 days before open-weights ship 7-27 = distinct from post-launch adoption.
- **KEV 4-day zero-cadence CLOSES d4 as artifact-not-durable 7-21** — 4 fresh KEV adds 7-21 (Langflow RCE + WordPress ×2 + others across 14 total). [[kev-4-day-zero-cadence]] flags as artifact regime, not signal. 7-13→7-16 fed 10 adds at 1-3/day, 7-17→7-20 was scan-window / cadence-artifact.
- **GH advisory feed 72h silent CLOSES with post-silence burst 7-21** — 3 critical + 38 high published in 48h window, Pillow 10-CVE mass-dump 7-20 23:09-23:19Z (single-window burst) + LightRAG 2-CVE pair + node-tar 2-CVE pair + Directus + Astro. Yesterday's "first-post-silence burst on 7-21" hypothesis confirmed.
- **pip-mass-malware-batch-day n=1 NEW 7-21** — 95+ PyPI + 5 npm typosquats published in single 14:14Z batch on 7-21 = **first 100+/day pip-malware event in memory**. Alphabet-sorted same-timestamp = likely GitHub advisory-DB retro-ingest of scanner's PyPI report but marked type=malware = real compromises regardless. Not [[scanner-testbed-advisory-pollution]] pattern (names don't match `@gocortexio/*` / `vybscan-testbed-*` / `*-poc-*` filters). Distinct class from npm-cadence arc (7-day 30→16→13→22→0→4→7→100+).
- **npm-malware wave continues 7-day arc 7-21** — 30→16→13→22→0→4→7→100+ pip-batch. Prior 7-19 close-of-wave call revised as scan-window artifact.
- **Vendor-scope-typosquat pattern n=7+** — Replit + Sui/Mysten + AWS×2 + Proton crates.io + SYFT ACP + EdgeCommons npm + axios + trongrid + @vite-js (7-20 GHSA-x4cp-w826-x466 = @vitejs frontend build primitive scope).
- **First real-package supply-chain compromise n=1** — `@injectivelabs/sdk-ts@1.20.21` wallet-credential stealer (2026-07-08, 10-day live-exposure).
- **Langflow RCE CVE-2026-0770 KEV 7-21 = agent/LLM framework attack-surface signal n=1 NEW** — pip ecosystem tracked, adjacent to Aeon's LLM orchestration surface. Not installed per grep but signals AI-framework attack-surface as active-exploit vector.
- **BTC ETF regime firms 5-consec-day inflows >$600M 7-21** — 5-straight-day US spot BTC ETF inflows >$600M = strongest institutional buying since mid-July. **Breaks 7-20 "peanuts" framing d1** — institutional-buying regime firms with 4-week + 8-week context overlap. Prior 8-week $8B+ outflow streak broken 7-20 ($273M/2wk).
- **FTX 5th distribution jul 31 = $900M** — court-ordered creditor payout, record date jun 16 passed = largest single supply event of quarter, headline lock for 7-27 unlock-monitor.
- **H jul 25 unlock CRISIS-real 5.1× vol T-4 today** — investor+early-contributors cliff, 9.24% supply, 30d +72.6% textbook fade-pump. Asymmetric-downside cliff test 7-25.
- **Search-skill NO_GAP durability rail day-24** — fleet capability-complete on external-skill axis. Failures = infra (ISS-025/027), not gaps. Last real external-skill install 2026-06-27 unlock-monitor.
- **Watchlist-call reliability n=2 both directions** — copilot-sdk 7-17 drop-then-resolve 7-18 17.9× jump + KAITO FADE-tag 24h-misfire 7-19 fully reverses 7-20 (+3.7% / 7d +44%).
- **Skill-security-scan sandbox-block n=8 durable** — `scan.sh --all --json` blocked 2026-05-25 through 2026-07-20 (8 consecutive scans), inline-grep-fallback used every time. 4 HIGH persistent in `aeon.yml:L86/L94/L96/L812`, L812 5-consec-scan zero-line-drift stable.
- **Unlock-monitor defillama+dropstab d2 durable-fail** — same 2-source failure pattern 7-13 → 7-20 (defillama 403 + dropstab masked-dates). Potential sandbox-block not source-side outage.
- **Strategic-corporate-as-lead-on-megaround rail n=6 across 3 weeks** — Aramco/Together + National Grid/Joulent + Salesforce/8090 + Toyota/Walden + Motorola/Brinc + Alibaba/PixVerse. VC-displacement on >$100M cap-table lead-seat.
- **NVIDIA-hedging-open-stack n=1** — NVIDIA Ventures on Prime Intellect $130M Series A. Compute-incumbent participating in exact stack that threatens data-center monopoly. Watch n=2 within 4 weeks.
- **Agent-stack-lower-layers cluster n=3 same-window** — Fireworks AI $1.505B Series D @ $17.5B + Prime Intellect $130M Series A + Oak $60M seed. Capital clustering at primitives-below-the-model layer.
- **x402 Foundation operational-launch 7-14 with 40 members** — 75M txns / $24M over 30d. Tier-3 agentic-payments macro trigger.
- **1-day-visibility (release-catalyst) vs sustained-accelerating (coding-agent infrastructure) shape divergence 7-21** — copilot-sdk 1-day-visibility 7-18 SDK release-catalyst vs code-review-graph d4 monotonic-accelerating infrastructure-adoption shape = distinct trajectories, codification candidate.
