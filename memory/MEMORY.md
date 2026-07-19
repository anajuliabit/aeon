# Long-term Memory
*Last consolidated: 2026-07-18*

## Current Goals
- **CLAUDE.md rule-5 codification T+1 SLIPPED** — self-improve 18:00Z 7-17 exit-gated on 3+ open PRs (first-ever skip on codification deadline). Next fire 7-19 tests whether improvement-PR-queue-locks-self-improve dynamic is 2-consec pattern. Operator direct-author path still open. Rule-5 primitive n=4 = **auto-committed state drift** across any self-improve authored PR (workflow/SKILL.md/scripts alike).
- **ISS-025 capture-step PR T+2 day-3** — SLIPPED T-0 firm 7-16, T+1 7-17, now T+2. Operator direct-author against `.github/workflows/aeon.yml:479-495`. cost-report STUCK d5 ~113h is current manifest.
- **All 3 self-improve authored PRs CONFLICTING past stall gates** — PR #162 T+4 day-5 (~164h), PR #163 past 72h gate (~120h), PR #164 past 24h gate (~66h). Operator direct-author is sole reliable path per rule-5 extension.
- **cost-report STUCK d5 ~113h** — `last_status: dispatched` 2026-07-13T20:44Z, cf=5, sr=0.10, ~19d since last_success. ISS-025 signature. Operator PR unblocks.
- **12:00 UTC batch DARK day-21** — 9-skill cluster still frozen at 2026-06-28. per-skill blockage (token-alert + btc-levels fire cleanly at same slot); scheduler-side per ISS-027. **07:00Z morning-batch d2 BROKE 7-18** — daily-routine + morning-brief + thought-review + heartbeat all landed in catch-up band; **partial-slot recovery, not durable-recover** (single-fire).
- **Operator on-chain config day-42** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Blocked.

## Recently Cleared
- **07:00Z morning-batch dead-slot BROKE at d2** (7-18 07:20-07:31Z) — positive delta vs 20:03Z 7-17 hb prediction of d3 extension. Full morning-batch (daily-routine + morning-brief + thought-review + heartbeat + skill-freshness + github-trending) landed within catch-up band.
- **Weekly-review action #4** (Investment Advisor cancellation) SHIPPED-ON-TARGET via self-improve PR #164 authored 7-15 T-1 (PR now CONFLICTING but investigation output landed).
- **BTC $63.5k arc REOPENED then softens** — reclaim gate armed since 7-14 close $64,977; 7-15/16 confirm; 7-17/18 intraday $62,859-$64,292 slips but `reclaim63500Alerted=true` holds (re-arm sub-$60,500 only).

## Fleet Health
See [[fleet]] for full snapshot. Last skill-health hash 618ede5f (7-16 18:48Z NOOP): 1 CRITICAL (cost-report) / 17 DEGRADED / 13 WARNING / 9 HEALTHY / 3 NO_DATA. 11 open issues (4 critical / 4 high / 3 medium). Sandbox-truncation family **day-26**. aixbt-pulse dead-slot **d21**. weekly-shiplog + operator-scorecard chronic Mon miss.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, rule-5 extension.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns (breakout-unwind n=5 · LAB -95% zero-arc · PUMP 2-step-shape · GITLAWB whipsaw-continuation-pause 5-session closes · WELL distribution-with-return d1 thin-bid bounce · REPPO fade d4 decelerates · BTC arc reopens then softens).
- [Market context](topics/market-context.md) — Baseline snapshot; refreshed each cycle.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).
- [XAI quota state](topics/xai-quota-exhausted.md) — Retired reference; cache-prefetch primary path.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 21:00Z (aixbt-pulse dead-slot d21 = state frozen).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. Anchors refreshed per 7-19 12:41Z print (0/12 checks fire → **2-consec zero-alerts day**, watchlist enters compression regime as 4/4 signals fade to noise: 2 thin-bid mechanical-rebounds + 2 exhaustion-completes).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 7-19 +0.71%, vol **0.10× baseline** ($53K new window-low d2) = **distribution-flush extends d2 not exhaust-within-24h**; +0.66% log-to-log on falling participation = thin-bid softening, mechanical-rebound thesis fades |
| MAMO    | mamo               | 15%           | 7-19 -0.14%, vol 0.94× = **day-9 sustainable-shape holds** (4th-consec near-baseline print 0.99/0.99/0.99/0.94, sub-1% price drift = unmatched pause-at-mean signature) |
| REPPO   | reppo              | 15%           | 7-19 -0.27%, vol 0.78× = **fade-back-to-trend d5 completes with decelerating rate** (log-to-log cascade -12.66% → -4.31% → -12.66% → -2.31% → -0.54% = mean-reversion fully exhausts) |
| GITLAWB | gitlawb            | 15%           | 7-19 +5.61%, vol 0.57× = **d6 thin-bid bounce-attempt breaks dead-flat pause** but on falling participation = parallels WELL's mechanical-rebound signature; whipsaw-then-continuation-then-pause-then-bounce 6-day arc all under-baseline (running mean 0.64×) |

## Recurring patterns (durable)
- **One-day-breakout-unwind n=5** (MORPHO/EIGEN/NEX/TIBBIR/DRV) — breakout must hold d2. BEAT/B n=2 dead-cat-with-legs exception.
- **LAB -95% zero-arc reference case** — 7d cumulative ~99.4%; sellers-exhaust heuristic 0/7.
- **GITLAWB whipsaw-then-continuation-then-pause 5-session closes** — mechanical whipsaw → trend-fade → dead-flat pause; entire arc under-baseline (5-day mean 0.66×). Rail-breach n=1 single-session isolate.
- **Rule-5 primitive extends past workflow-file class (n=4)** — conflict source = **auto-committed state drift**, not file-class-specific. Operator direct-author is sole reliable path for any self-improve output.
- **Improvement-PR-queue-locks-self-improve NEW** — 7-17 18:00Z self-improve exit-gated on 3+ open PRs (first-ever codification-deadline skip). 7-19 fire tests 2-consec pattern.
- **Skills-primitive convergence rail day-18 as gap** — 17-day continuous run 7-13→7-17 (stitch-skills · hallmark · mattpocock/skills · ui-skills). First break 7-18. Tomorrow tests concludes-vs-intermittent.
- **Small-MoE-frontier-close cluster n=3** — Meta Muse Spark 1.1 + Sonnet 5 near-Opus + Bonsai-27B ~1.125 bits/weight fits-on-iPhone. 7-27 Kimi K3 open weights extends to n=4 if ships.
- **Vendor-scope-typosquat pattern n=6+** (7-18 CODIFIES, generalizes from Anthropic-scope n=2) — Replit + Sui/Mysten + AWS×2 + Proton crates.io **4 first-appearance scopes in single day** + SYFT ACP + EdgeCommons npm scope-families + axios pair + trongrid pip pair. Broadens across ecosystems, not slowing.
- **First real-package supply-chain compromise n=1 NEW** — `@injectivelabs/sdk-ts@1.20.21` wallet-credential stealer (published 2026-07-08, **10-day live-exposure window**, hooks `PrivateKey.fromMnemonic`/`fromHex`, base64 exfil as grpc-web POST). Top-40 crypto project = high blast-radius. First confirmed real-package compromise vs typosquats-only prior 4 weeks.
- **First-party-incumbent-alternative-to-Anthropic-scope n=1 NEW** — github/copilot-sdk v1.0.7 (7-16 15:22Z) Java+Rust parity = legitimate-incumbent-competition targeting `claude-*` namespace Claude Code holds. Distinct from adversarial typosquat rail.
- **MCP-server hardening rail n=5 in 96h** — langbot pip + mcp-documentation-server npm + n8n-mcp npm + MCP Python SDK 3-CVE cluster + Prompty pip/npm/rust/nuget. Durable weekly rail confirms.
- **Cross-ecosystem-single-repo cluster n=6 durable weekly rail** — 7-13 SiYuan Go 5-CVE + 7-14 DIRAC pip 4-CVE + 7-15 nebula-mesh Go 4-CVE + 7-16 dd-trace 6-lang polyglot + 7-17 MCP Python SDK 3-CVE + 7-18 Prompty pip/npm/rust/nuget. Parallel to MCP-hardening rail.
- **High-EPSS regime n=2 consec days** — 7-17 CVE-2026-39808 Fortinet FortiSandbox 0.842 pct 0.997 (first ≥0.5 in memory) + 7-18 CVE-2026-27771 gitea Go 0.407 pct 0.985 (2nd ≥0.4). Active-exploitation signal materially stronger than baseline holds day-2.
- **npm-malware wave regime-break at d5=22** — reverses 3-day fade 30→16→13→**22**; single-digit d5 prediction fails. d6 tests regime-break vs d5-anomaly.
- **MCP-symbol-flow-invisible-Unicode class n=1 NEW** (7-18) — vuln-scanner tirth8205/code-review-graph PVR GHSA-chjm-935c-cx8p: `_sanitize_name()` ASCII 0x00-0x1F strip leaves Tag chars U+E0000-U+E007F + BiDi overrides intact through 30 MCP tools into downstream LLMs. **First LLM-tool-integration finding via PVR** in Aeon vuln-scanner history — expands taxonomy past dep-CVE + argv-injection.
- **Watchlist-call-resolves n=1 NEW** — github-trending 7-17 drop of copilot-sdk ("watch for future fresh-release spike") resolves 7-18 at 17.9× jump. First cross-day self-resolving watchlist annotation. Suggests skill-side watch-notes are durable-actionable.
- **Consumer-tool viral-tail day-5 convergence n=2** — hallmark 4-day monotonic-compounding peaks day-4 (3,372) then fades day-5 (-56%); OpenCut oscillating-viral settles day-5 (-70%). **5-day terminal for consumer-tool category** (monotonic + oscillating both cap same).
- **HKUDS-cluster n=4 pattern firms soft→firm** (7-14 → 7-18) — Vibe-Trading + DeepTutor 5-consecutive-day trending presence. Lab-momentum-as-signal confirmed.
- **Old-CVE-fresh-KEV n=2** — 2008 Cisco IOS 12.4 + 2023 KNX Protocol. Long-tail EOL/legacy = active exploitation.
- **Agent-safety-guardrail rail n=3** — destructive_command_guard + Cursor DuneSlide 0day + pi-computer-use accessibility.
- **SharePoint EPSS 2-day plateau at 0.056/0.920** = percentile-cools-then-plateaus shape.
- **search-skill SEARCH_SKILL_NO_GAP day 22** — fleet capability-complete on external-skill axis. Failures = infra (ISS-025/027), not gaps.
