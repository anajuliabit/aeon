# Long-term Memory
*Last consolidated: 2026-07-30*

## Current Goals
- **ISS-025 capture-step PR hand-off T-0 DEADLINE TODAY 2026-07-30** — operator direct-author against `.github/workflows/aeon.yml:479-495`. Weekly-review 7-27 action #1 target; T+12 day-15. Cost-report weakest at 12% (7/58) durable. Reflect 7-30 evening captures shipped-on-target vs slipped d16 outcome.
- **07:00 UTC scheduler slot MISS NEW 7-30** — morning-brief + daily-routine + thought-review all dropped today (heartbeat 15:16Z confirmed 8h+ past schedule, no in-flight recovery). Later slots recover with 40-76min dispatch-lag. First whole-slot MISS in memory-window; ISS-file candidate if 7-31 07:00Z misses too.
- **12:00 UTC batch DARK day-33** — 8-skill 6-28 cluster (defi-overview / token-pick / token-movers / narrative-tracker / market-context-refresh / fleet-control / on-chain-monitor / defi-monitor) frozen since 6-28 21:00Z. ISS-027 signature durable through 7-30 12:00Z clean same-slot token-alert fire.
- ~~ISS-027/028 doc-gap~~ — **CLOSED 2026-07-30 by reflect skill** (see [Recently Cleared](#recently-cleared)). ISS-027 (12:00 UTC batch DARK d33) + ISS-028 (bash `>` redirect n=11+ 8-UTC-day span) both filed to `memory/issues/`; INDEX.md updated. 11→13 open issues.
- **PR #165 d11 past-gate CONFLICTING** — created 7-19 17:38Z, weekly-review 7-27 absorbed 7d gate cross; still CONFLICTING through 7-30 heartbeat = 11d open. Operator batch-merge cadence window.
- **PR #167 d7 crosses weekly-batch gate 7-30** — bash-redirect fix (7-23 18:21Z self-improve); joins #165 in past-gate cohort (n=2). PR queue 3 open (#170 21h + #167 7d + #165 11d).
- **Operator on-chain config day-54** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Operator-gated.
- **priorities.md 56d stale** — last reviewed 2026-06-04. Thought-review flagged in every daily notify. Operator-owned refresh candidate.

## Recently Cleared
- **ISS-027/028 doc-gap CLOSED 2026-07-30 by reflect skill** — 24d load-bearing gap closed. ISS-027.md (12:00 UTC batch DARK, 8-skill cluster frozen since 6-28 21:00Z, category=config, severity=high) + ISS-028.md (bash `>` redirect regression, workaround chain held on n=11+ fires across 8-UTC-day span 7-22→7-30, category=sandbox-limitation, severity=medium) both filed to `memory/issues/` with YAML frontmatter matching ISS-025 template; INDEX.md updated 11→13 open issues. Action-converter proposals from 7-24→7-29 (max-score 125 file-creates 4-consec runs) finally landed via reflect scope.
- **07:00Z slot MISS confirmed 7-30 15:16Z** — pending/delayed flag from 09:04Z heartbeat escalated to dropped-tick with notify SENT. Morning-brief + daily-routine + thought-review all 8h+ past schedule.
- **skill-freshness 09:15Z FRESHNESS_NO_CHANGE** — fingerprint `1ab8c658` stable 5d since 7-25 (7 items flagged: 5 STALE + 2 WARN). Watch: market-context.md crosses STALE threshold ~13:00Z 7-30, fingerprint change + notify expected 7-31.
- **CoinGecko clean-day streak extends to 37 consecutive days** — 7-30 12:00Z token-alert fires under ISS-027 batch-dark signature, CG API independence holds.
- **KEV quiet-cadence breaks d2 7-30** — Cisco Secure FMC 7-29 hardcoded-password unauth-remote fresh add ends 2-day zero-fresh streak.
- **Self-improve queue-exit gate breach RESOLVED 7-28 22:36Z** — dupe pair #168 + #169 both merged. Root-cause investigation (whether self-improve correctly evaluates gate at authoring time) still open per 7-28 reflect follow-up #3.
- **skill-health hash flip 467ce959 → 7bf88238 (7-28 19:02Z)** — first hash break in 168h+ span. btc-levels graduates HEALTHY (SR 0.81). 10 HEALTHY (up from 9).
- **Weekly-review 2026-07-27 SHIPPED** — 289 runs / 3 failures / 98.96% success = tightest failure envelope in memory-window. Article `articles/weekly-review-2026-07-27.md`.

## Fleet Health
See [[fleet]] for full snapshot. skill-health hash **7bf88238** (fresh 7-28 19:02Z NOTIFY): 0 CRITICAL / 18 DEGRADED / 13 WARNING / 10 HEALTHY / 3 NO_DATA. 11 open issues. **Heartbeat verdict-string 7-consec DEGRADED-tick identity across ~43h span** (7-27 20:12Z → 7-30 15:16Z). Sandbox-truncation family **day-38** (T+13 day-15). aixbt-pulse dead-slot **d33**. **Bash `>` redirect regression n=11 durable 8-UTC-day span** (7-22 → 7-30 heartbeat 15:16Z + security-digest 15:22Z + morning-brief + prior fires). **NEW: 07:00Z slot MISS + dispatch-lag 40-76min pattern durable on morning fires** — GHA runner queue depth or webhook processing delay candidate; watch 7-31 for continuation.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, weekly-batch cadence, positive events log.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns.
- [Market context](topics/market-context.md) — Baseline snapshot (stale from 7-16; refresh next fire; crosses STALE threshold ~13:00Z 7-30).
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. 7-30 12:00Z snapshot: 0/4 alerts (all sub-threshold, 37th consec clean CG day). 7-29's 3-of-4 above-baseline participation-lift-day reverses to 1-of-4 (only REPPO above baseline) = single-day flush not sustain. Leader-of-ratio rolls GITLAWB→REPPO (3rd different leader in 3 UTC-days), vol-intensity attenuates run-over-run (2.075× → 2.009× → 1.386×).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 7-30 -2.53%, vol $1.36M = 0.852× baseline (post-drain regime resumes drift-down d3; 2-consec above-baseline sequence breaks toward fresh drift-down) |
| MAMO    | mamo               | 15%           | 7-30 +1.20%, vol $768K = 0.951× baseline (digestion d9 first positive 24h print in sequence; 7-29 vol-lift fails to sustain) |
| REPPO   | reppo              | 15%           | 7-30 -4.70%, vol $156K = 1.386× baseline (capitulation-tail d2 re-engagement bid on lifting participation; give-back doubles the digestion-stall print) |
| GITLAWB | gitlawb            | 15%           | 7-30 +6.85%, vol $230K = 0.817× baseline (cliff-give-back d6 reverses to green d7 on halved participation; first green print of 6-day give-back sequence terminates rail) |

## Recurring patterns (durable — brief pointers; details in topic files)
- **[[open-voice-primitive-rail]] NEW n=2 in 48h 7-30** — microsoft/VibeVoice pairs with 7-29 huggingface/speech-to-speech = cross-org lab+big-co concurrence on open-weights frontier voice AI in 24h window. Sibling rail to [[embodied-agent-runtime-primitive]] (agent-as-voice-runtime vs agent-as-embodied-game-runtime).
- **[[network-perimeter-vendor-in-KEV]] cluster n=4 crystallizes 7-30** — Fortinet 7-27 + Arista 7-27 + Cisco Secure FMC 7-29 = 3-of-4 fresh KEV-this-week are network-perimeter vendors (SharePoint 7-22 only non-network). Crystallized sub-class.
- **[[real-plugin-name-fake-ecosystem]] NEW sub-class 7-30** — litespeed-cache WordPress-plugin name published to npm = pure impersonation vector under [[mass-parallel-real-package-account-takeover]] parent.
- **[[single-project-mass-disclose]] rail n=6→n=7 7-30** — flyto-core 6-CVE mass-disclose (all in 14:44-14:48Z window) = 3-consec-day same-day mass-disclose cadence. **Acceleration confirmed monthly → same-day**.
- **[[AI-framework-attack-surface]] rail n=3→n=4 7-30** — @aws/agentcore Bedrock CLI code-injection joins Claude Code CVE-2026-55607 + Langflow + LiteLLM triad.
- **Rust-native efficiency-first coding-harness primitive NEW n=1 7-30** — 1jehuang/jcode differentiates on RAM efficiency in JS/Node/Electron-dominated harness landscape (Claude Code / aider / Cursor / opencode). Extends agent-harness taxonomy into runtime-efficiency-differentiated sub-class.
- **Kimi K3 → FlashKDA delta-attention pipeline 7-30** — 7-28 top-HN paper concurrence → 7-30 CUDA kernels ship with fresh CUTLASS pipeline optimizations. Extends [[small-MoE-frontier-close]] rail (paper → usable code in 48h).
- **Star-anomaly rail n=4→n=6 durable 7-30** — obra/superpowers 6th trending appearance without featuring (896/d normalized velocity, higher than ECC's 1,222/d). Drops-not-features codify pattern; investigation candidate deepens.
- **[[skill-pack-primitive-rail]] n=5 in 6 UTC-days** — virgiliojr94/book-to-skill 7-29 tops the rail: mattpocock/skills → obra/superpowers → bradautomates/claude-video → mvanhorn/last30days-skill → virgiliojr94/book-to-skill. No new entry 7-30 (rail didn't extend).
- **[[embodied-agent-runtime-primitive]] rail n=2** — huggingface/speech-to-speech 7-29 pairs with 7-28 airi (Minecraft/Factorio). Now sibling to [[open-voice-primitive-rail]].
- **Sub-25 trending page fetch pattern n=3 durable 7-30** — 7-28 (15 candidates) + 7-29 (12) + 7-30 (17) = 3-consec WebFetch cut short of ~25 expected. Sandbox/rendering artifact firms as observation; filter kept ≥3 each time so fallback branch never triggered.
- **Participation-lift-day does not persist d2 7-30** — 7-29 3-of-4 above-baseline reverses to 1-of-4 today. Extends [[participation-lift-single-day-flush]] shape.
- **Vol-intensity attenuates run-over-run 7-30** — 7-28 REPPO 2.075× → 7-29 GITLAWB 2.009× → 7-30 REPPO 1.386× (3rd different leader in 3 UTC-days, 33% drop vs prior day's leader). Cross-token rail loses vol-intensity even as leader rotates.
- **[[federal-CEA-authority-reassert]] 7-29** — MN prediction-market ban enjoined (D. Minn.) + CFTC self-cert crackdown same-week; state-vs-federal jurisdiction fragmentation escalates. See [[crypto]].
- **[[legit-defi-org-typosquat]] sub-class 7-29** — karpatkey + karpatkit pip full-scope cred stealer. Under [[mass-parallel-real-package-account-takeover]] parent alongside 7-28 AI-tooling-typosquat sub-class.
- **[[training-curriculum-as-a-service]] primitive 7-29** — Qwen Skill Self-Play (DeFi Minty link, arxiv). Proposer/solver/controller loop refines own task pool; extends [[small-MoE-frontier-close]] rail.
- **[[MCP-enforcement-primitive-cluster]] n=1 7-29** — agent-buzz surfaces 2 independent MCP-infra-maturity builders same day.
- **[[low-rank-mid-cap-trending-breakout]] rail candidate 7-29** — META rank 187 +66.8% TRENDING+UP on $6.5M vol.
- **[[one-day-below-gate-then-above]] reversal 7-29** — opengeos/GeoLibre 48→58.1/d velocity cross first "just-below-gate → above-gate on d2" reversal in memory-window.
- **KEV quiet-cadence pattern n=2 shape 7-29** — 7-23→7-26 4d drought + 7-28→7-29 2d drought, both bounded by enterprise-network-vendor fires.
- **AEON trending +17.8% at rank 781 7-29** — project's own token in trending endpoint. Note-only, no action.
- **Chain-mode gap durable** — aeon.yml `chains: {}` inactive; daily-routine standalone fallback fires correctly each cycle per SKILL.md.
- **Fleet-relevance agent-thesis 14-consec-day 7-30** — VibeVoice + jcode + FlashKDA + book-to-skill + speech-to-speech = agentic-primitive dominance persists 7-17 → 7-30.
- **Search-skill NO_GAP durability rail day-33** — fleet capability-complete on external-skill axis. Failures = infra (ISS-025/027/028), not gaps.
- Claude Opus 5 shipped 7-24 = Aeon-fleet meta-signal; effort-toggle per-request gives per-skill cost-lever.
- FTX $900M distribution jul 31 T-1 = largest single supply event of quarter (unlock-monitor confirmed as headline, not vesting cliff).
- CVE-2026-55607 Claude Code auto-patched 7-25 via unpinned `npm install -g` (fix 2.1.163).
