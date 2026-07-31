# Long-term Memory
*Last consolidated: 2026-07-31*

## Current Goals
- **ISS-025 capture-step PR hand-off T-0 DEADLINE TODAY 2026-07-30** — operator direct-author against `.github/workflows/aeon.yml:479-495`. Weekly-review 7-27 action #1 target; T+12 day-15. Cost-report weakest at 12% (7/58) durable. Reflect 7-30 evening captures shipped-on-target vs slipped d16 outcome.
- ~~07:00 UTC scheduler slot MISS NEW 7-30~~ — **RECOVERED 2026-07-31 by goal-tracker** (see [Recently Cleared](#recently-cleared)). 1-instance anomaly, ISS-file escalation gate discharged.
- **12:00 UTC batch DARK day-33** — 8-skill 6-28 cluster (defi-overview / token-pick / token-movers / narrative-tracker / market-context-refresh / fleet-control / on-chain-monitor / defi-monitor) frozen since 6-28 21:00Z. ISS-027 signature durable through 7-30 12:00Z clean same-slot token-alert fire.
- ~~ISS-027/028 doc-gap~~ — **CLOSED 2026-07-30 by reflect skill** (see [Recently Cleared](#recently-cleared)). ISS-027 (12:00 UTC batch DARK d33) + ISS-028 (bash `>` redirect n=11+ 8-UTC-day span) both filed to `memory/issues/`; INDEX.md updated. 11→13 open issues.
- **PR #165 d11 past-gate CONFLICTING** — created 7-19 17:38Z, weekly-review 7-27 absorbed 7d gate cross; still CONFLICTING through 7-30 heartbeat = 11d open. Operator batch-merge cadence window.
- ~~PR #167 d7 crosses weekly-batch gate 7-30~~ — **MERGED 2026-07-30 23:37:20Z** (see [Recently Cleared](#recently-cleared)). Past-gate cohort cleared to n=1 (#165 sole survivor).
- **Operator on-chain config day-54** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Operator-gated.
- **priorities.md 56d stale** — last reviewed 2026-06-04. Thought-review flagged in every daily notify. Operator-owned refresh candidate.

## Recently Cleared
- **PR #167 bash-redirect fix MERGED 2026-07-30 23:37:20Z** — 7d past-gate cohort clears to n=1. First live kill-test slot for the workaround chain (curl `-o` / Write / Edit / gh --jq) fires today; if 8-01 security-digest slot fires clean with a `>` redirect, the ISS-028 signature retires as durable pattern.
- **07:00 UTC scheduler slot MISS RECOVERED 2026-07-31 by goal-tracker** — morning-brief 07:33Z + daily-routine 07:41Z + thought-review 07:36Z all fired at +33-41min dispatch-lag on 7-31. Whole-slot MISS confirmed as 1-instance 7-30 anomaly, not durable regime. ISS-file escalation gate discharged per heartbeat 7-30 15:16Z follow-up (v).
- **ISS-027/028 doc-gap CLOSED 2026-07-30 by reflect skill** — 24d load-bearing gap closed. ISS-027.md (12:00 UTC batch DARK, 8-skill cluster frozen since 6-28 21:00Z, category=config, severity=high) + ISS-028.md (bash `>` redirect regression, workaround chain held on n=11+ fires across 8-UTC-day span 7-22→7-30, category=sandbox-limitation, severity=medium) both filed to `memory/issues/` with YAML frontmatter matching ISS-025 template; INDEX.md updated 11→13 open issues. Action-converter proposals from 7-24→7-29 (max-score 125 file-creates 4-consec runs) finally landed via reflect scope.
- **07:00Z slot MISS confirmed 7-30 15:16Z** — pending/delayed flag from 09:04Z heartbeat escalated to dropped-tick with notify SENT. Morning-brief + daily-routine + thought-review all 8h+ past schedule.
- **skill-freshness 09:15Z FRESHNESS_NO_CHANGE** — fingerprint `1ab8c658` stable 5d since 7-25 (7 items flagged: 5 STALE + 2 WARN). Watch: market-context.md crosses STALE threshold ~13:00Z 7-30, fingerprint change + notify expected 7-31.
- **CoinGecko clean-day streak extends to 37 consecutive days** — 7-30 12:00Z token-alert fires under ISS-027 batch-dark signature, CG API independence holds.
- **KEV quiet-cadence breaks d2 7-30** — Cisco Secure FMC 7-29 hardcoded-password unauth-remote fresh add ends 2-day zero-fresh streak.
- **Self-improve queue-exit gate breach RESOLVED 7-28 22:36Z** — dupe pair #168 + #169 both merged. Root-cause investigation (whether self-improve correctly evaluates gate at authoring time) still open per 7-28 reflect follow-up #3.
- **skill-health hash flip 467ce959 → 7bf88238 (7-28 19:02Z)** — first hash break in 168h+ span. btc-levels graduates HEALTHY (SR 0.81). 10 HEALTHY (up from 9).
- **ISS-025 capture-step PR hand-off T+1 day-16 SLIPPED** — 7-30 deadline passed without operator direct-author against `.github/workflows/aeon.yml:479-495`; cost-report weakest sr=0.12 (7/58) durable; weekly-review 7-27 action #1 milestone rolls forward. Reflect 8-03 (weekly-batch window) next natural catch.
- **ISS-028 workaround-chain retirement candidate NEW** — PR #167 (bash-redirect fix) merged 7-30 23:37Z; 7-31 fires (heartbeat 14:44Z + security-digest 14:44Z + morning-brief + daily-routine + github-trending + token-alert) all held clean via Write-tool workaround belt-and-braces (no `>` attempted). 8-01 slot: try `>` redirect to confirm regression fix landed OR keep as durable pattern; rail extends n=12+ across 9-UTC-day span 7-22→7-31.
- **12:00 UTC batch DARK day-34** — 8-skill 6-28 cluster (defi-overview / token-pick / token-movers / narrative-tracker / market-context-refresh / fleet-control / on-chain-monitor / defi-monitor) frozen since 6-28 21:00Z. ISS-027 signature durable through 7-31 12:00Z clean same-slot token-alert fire.
- **PR #165 d12 past-gate CONFLICTING sole survivor** — created 7-19 17:38Z; PR queue 3→1 overnight after #167 + #170 both merged 7-30 23:37Z within 20-sec window. 12d < CLAUDE.md ~14d weekly-review escalation threshold; expected shape in operator batch-merge cadence window.
- **Operator on-chain config day-55** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Operator-gated.
- **priorities.md 57d stale** — last reviewed 2026-06-04. Thought-review flagged daily; operator-owned refresh candidate. Vault inbox 40-day cold streak (last real capture 2026-06-21T08:32Z).

## Recently Cleared
- **07:00Z scheduler slot RECOVERS d1 7-31** — morning-brief 07:36Z + daily-routine 07:41Z + thought-review 07:36Z all fired at +33-41min dispatch-lag (within observed 40-76min pattern). Discharges 7-30 15:16Z heartbeat's ISS-file escalation gate. 1-instance MISS confirmed as one-day anomaly, not durable regime.
- **PR queue clears 3→1 overnight 7-30 23:37Z** — #167 (bash-redirect fix, 7d past-gate) + #170 (hn-digest self-improve, 21h) both merged within 20-sec window. First self-improve merge-batch since 7-28 dupe-pair (#168+#169) close. Sole survivor #165 d12 CONFLICTING (docs skill-graph).
- **CoinGecko clean-day streak extends to d38** — 7-31 12:00Z token-alert clean same-slot fire under ISS-027 batch-dark signature (CG API independent).
- **github-issues 6-consec clean day 7-26 → 7-31** — `GITHUB_ISSUES_OK` streak durable via daily-routine sub-agent.
- **ISS-027/028 doc-gap CLOSED 2026-07-30 by reflect** — 24d load-bearing gap resolved via file authoring; INDEX.md updated 11→13 open issues. Kept as pointer.
- **Weekly-review 2026-07-27 SHIPPED** — 289 runs / 3 failures / 98.96% success = tightest failure envelope in memory-window. Article `articles/weekly-review-2026-07-27.md`.

## Fleet Health
See [[fleet]] for full snapshot. skill-health hash **7bf88238** (3-consec formal-tick identity ~48h span; no formal tick yet since 7-30 18:15Z): 0 CRITICAL / 18 DEGRADED / 13 WARNING / 10 HEALTHY / 3 NO_DATA. **13 open issues** post-ISS-027/028 filing. **Heartbeat verdict-string 9-consec DEGRADED-tick identity across ~65h span** (7-27 20:12Z → 7-31 14:44Z). Sandbox-truncation family **day-39** (T+14 day-16). aixbt-pulse dead-slot **d34**. **Bash `>` redirect regression workaround-chain n=12+ durable 9-UTC-day span** (7-22 → 7-31, PR #167 kill-test in-progress). Dispatch-lag 40-76min pattern durable on later-slot fires (d2 confirmed 7-31 via 07:36Z morning cluster + 12:00Z token-alert 12:23Z + 14:00Z security-digest 14:44Z). **Chronic sr<0.5 cohort 10-skill sub-50% durable** (identical composition through 9-consec heartbeat ticks).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, weekly-batch cadence, positive events log.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns.
- [Market context](topics/market-context.md) — Baseline snapshot (stale from 7-16; refresh next fire; STALE threshold crossed 7-30).
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. 7-31 12:00Z snapshot: 0/4 alerts (all sub-threshold, 38th consec clean CG day). **First fully-synchronized red day in memory-window** — 4-of-4 tokens negative 24h. Participation-lift extinguishes fully on d3 (3-of-4 → 1-of-4 → 0-of-4 above-baseline across 7-29/7-30/7-31). Leader-of-ratio rolls MAMO 0.930× = **first time leader crosses sub-baseline** (4-consec-day monotone attenuation 2.075× → 2.009× → 1.386× → 0.930×, 4th different leader in 4 UTC-days).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 7-31 -0.50%, vol $86K = 0.059× baseline (**vol-cliff unprecedented in memory-window** — lowest baseline-ratio for any token any run, 94% single-slot collapse without price cascade, pure participation evaporation post-drain regime d4) |
| MAMO    | mamo               | 15%           | 7-31 -2.35%, vol $741K = 0.930× baseline (digestion d10 widening-red print; biggest red modulus of run on 2nd consec sub-baseline print = digestion-to-fade transition candidate) |
| REPPO   | reppo              | 15%           | 7-31 -5.73%, vol $79K = 0.620× baseline (capitulation-tail d3 re-engagement bid fails d1; vol halves to sub-baseline, drought-mode returns) |
| GITLAWB | gitlawb            | 15%           | 7-31 -7.13%, vol $202K = 0.777× baseline (green-print d1 fails to sustain, cliff-give-back resumes d8 at 7-28/7-29 magnitude; one-slot mean-reversion fully digested) |

## Recurring patterns (durable — brief pointers; details in topic files)
- **[[rust-native-efficiency-first-harness]] rail NEW n=2 in 48h 7-31** — agavra/tuicr (code-review TUI, 19.4× baseline) pairs with 7-30 1jehuang/jcode (coding harness). Sub-taxonomy: coding-harness → code-review-harness. Both Rust-native differentiating on runtime efficiency vs JS/Node/Electron pack (Claude Code / aider / Cursor / opencode).
- **[[star-anomaly-rail]] extends n=6 → n=7 durable 7-31** — affaan-m/ECC 7th trending appearance (1,219/d normalized velocity, most durable rail in memory-window). 5-consec-UTC-day drop 7-27→7-31 + obra/superpowers sibling.
- **Sub-25 trending page fetch pattern n=3 → n=4 durable 7-31** — 7-28 (15) + 7-29 (12) + 7-30 (17) + 7-31 (14) = 4-consec WebFetch cut short of ~25 expected. WebFetch hard-cap hypothesis firms; ISS-file candidate if 8-01 confirms 5-consec.
- **[[embodied-agent-runtime-primitive]] rail n=2 → n=3 7-31** — Gemini Robotics 2 whole-body drop (HN 539pts) pairs with 7-28 airi (Minecraft/Factorio) + 7-29 huggingface/speech-to-speech. Big-lab whole-body tier upgrade; sibling to [[open-voice-primitive-rail]] (VibeVoice).
- **[[eth-lib-typosquat-campaign]] NEW sub-class 7-31** — 7 ethers.js typosquats + fs-extra + socket.io = **3-cluster mass-typosquat batch** published 22:49-22:51Z 7-30. Direct Aeon-audience relevance (crypto-focused fleet). Sub-class under [[mass-parallel-real-package-account-takeover]] parent alongside [[legit-defi-org-typosquat]] (7-29) + [[real-plugin-name-fake-ecosystem]] (7-30) + [[AI-tooling-typosquat]] (7-28).
- **HOLO round-trip winner→loser in 48h 7-31** — 7-29 top-10 winner +10.5% → 7-31 top-10 loser -14.4%. Single-token full participation-lift-then-flush shape at token-instance-scale. Sibling to [[participation-lift-single-day-flush]] rail.
- **PUMP intra-week reversal 7-31** — 7-29 -7.1% loser → 7-31 +5.4% winner; second name with HOLO doing top-10 pole-flip in UTC-day roll = cross-token flip-day pattern candidate.
- **UNI +13.7% large-cap standout 7-31** — only top-40 mcap in winners list at DEX-token category leadership tier; rare non-microcap dominance vs today's UB (#108) / DCR (#145) / CARDS (#489) tail.
- **First fully-synchronized red day 7-31** — 4-of-4 tokens negative 24h (WELL/MAMO/REPPO/GITLAWB). Participation-lift extinguishes fully on d3.
- **WELL vol-cliff to 0.059× baseline 7-31** — 94% single-slot participation collapse without price cascade; lowest baseline-ratio for any token any run in memory-window. Pure participation-drain, distribution-adjacent structure evaporates.
- **Vol-intensity leader crosses sub-baseline for first time 7-31** — MAMO 0.930× tops rail vs prior day leaders' 1.386× / 2.009× / 2.075× (4-consec-day monotone ~30%/day attenuation, 4-consec different leaders).
- **[[open-voice-primitive-rail]] rail n=2** — microsoft/VibeVoice 7-30 + huggingface/speech-to-speech 7-29. Sibling to [[embodied-agent-runtime-primitive]].
- **[[network-perimeter-vendor-in-KEV]] cluster n=4 stable 7-31** — 3-of-4 fresh KEV-this-week are network-perimeter vendors (Fortinet 7-27 + Arista 7-27 + Cisco Secure FMC 7-29; SharePoint 7-22 only non-network). 0 fresh-week net-new post-dedup at 7-31 digest.
- **[[single-project-mass-disclose]] rail n=7 stable 7-31** — flyto-core 6-CVE 7-30 remains latest; 3-consec-day same-day mass-disclose cadence not extended on 7-31 (7-30 dedup absorbed slate).
- **[[AI-framework-attack-surface]] rail n=4** — @aws/agentcore Bedrock CLI 7-30 joins Claude Code CVE-2026-55607 + Langflow + LiteLLM triad.
- **Kimi K3 → FlashKDA delta-attention pipeline 7-30** — paper → usable CUDA kernels in 48h. Extends [[small-MoE-frontier-close]] rail.
- **[[skill-pack-primitive-rail]] n=5 stable** — mattpocock/skills → obra/superpowers → bradautomates/claude-video → mvanhorn/last30days-skill → virgiliojr94/book-to-skill. No new entry 7-30 or 7-31.
- **Chain-mode gap durable** — aeon.yml `chains: {}` inactive; daily-routine standalone fallback fires correctly each cycle.
- **[[fleet-relevance agent-thesis]] 15-consec-day 7-31** — Memory Decoder paper + Gemini Robotics 2 + Anthropic cybersec-evals HN all direct-fleet-relevant; agentic-primitive dominance 7-17 → 7-31.
- **Search-skill NO_GAP durability rail day-34 7-31** — fleet capability-complete on external-skill axis. Failures = infra (ISS-025/027/028), not gaps.
- Claude Opus 5 shipped 7-24 = Aeon-fleet meta-signal; effort-toggle per-request gives per-skill cost-lever. Claude Code computer-use gain 7-31 = fresh Aeon-relevance datapoint.
- CVE-2026-55607 Claude Code auto-patched 7-25 via unpinned `npm install -g` (fix 2.1.163).
- FTX $900M distribution 2026-07-31 = 5th round creditor payout, largest single supply event of quarter, 45 excluded jurisdictions (WebSearch confirmed via bloomberg/coindesk/kucoin aggregate).
