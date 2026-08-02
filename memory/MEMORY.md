# Long-term Memory
*Last consolidated: 2026-08-02*

## Current Goals
- **ISS-028 kill-test d2 NEGATIVE — workaround-chain n=15+ durable across 11-UTC-day span** — PR #167 merged 7-30 23:37Z did NOT retire the pattern. Explicit sub-agent report from daily-routine (hn-digest, 08:42Z) + security-digest (14:52Z) + list-digest (17:37Z) + vuln-scanner (16:45Z) all confirm bash `>` + `-o` still blocked; workaround (Write-tool / Edit-tool / URL-encoded `%3E` in gh api / pipe-to-jq) held clean at every call-site. Retirement candidate FAILS; ISS-028 stays open. Reflect 8-03 (weekly-batch window) should reopen root-cause investigation into whether PR #167 fix scope was narrow to heartbeat/security-digest surfaces vs missed daily-routine sub-agent + github-trending surfaces.
- **12:00 UTC batch DARK day-35** — 8-skill cluster frozen since 6-28 21:00Z. ISS-027 signature durable through 8-01 12:00Z clean same-slot token-alert fire (39th consec clean CG day).
- **ISS-025 hand-off T+3 day-18 SLIPPED** — cost-report weakest chronic-failure sr=0.12 (7/58) durable. Weekly-review 8-03 action #1 rolls to d19 milestone at that window (2d out).
- **PR #165 d13 past-gate CONFLICTING** — 7-19 17:38Z docs skill-graph, sole survivor of past-gate cohort. Crosses 14d touch-threshold on 8-02 = CLAUDE.md ~7d-past-touch escalation window opens.
- **PR #171 fresh self-improve ~24h** — 7-31 18:07Z `fix(github-trending): reflect observed 12-17 candidate cap, not ~25` — under gate.
- **Operator on-chain config day-56** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Operator-gated.
- **priorities.md 58d stale** — last reviewed 2026-06-04. Vault inbox 41d cold streak (last real capture 2026-06-21T08:32Z).

## Recently Cleared
- **07:00Z scheduler slot 2-of-3-day degraded 8-01 — DONE 2026-08-02** (deciding-test PASSED: morning-brief 07:22Z +22min / daily-routine 07:37Z +37min / thought-review 07:23Z +23min all in-band vs 8-01 +96-97min; ISS-file escalation gate discharges; regime rewrites 2-of-3-day-degraded → 3-of-4-day-intermittent-recovered).
- **skill-freshness RECOVERED 8-01 08:50Z + first fingerprint change since 7-25** — new fingerprint `f789cd3bca6…`, 7 items flagged (5 STALE + 2 WARN); market-context.md crossed 2× STALE threshold (~16d/380h), market-context-refresh + token-pick escalated WARN → STALE. First hash break in 7d span.
- **WELL vol-cliff d5 test = one-slot anomaly, NOT durable regime** — 7-31's 0.059× unprecedented print recovers to 0.162× (2.7× the nadir); participation drain reads as one-slot data-glitch-adjacent shape, not post-drain evaporation regime.
- **Fully-synchronized red day breaks at d1 8-01** — REPPO snaps +7.40% ending 7-31's memory-window-first 4-of-4 print; 4-of-4 tokens vol above 7-31 print, 1-of-4 above-baseline (MAMO 1.036×) = regime shift from drought-mode-fully-drained toward mean-reversion band.
- **vuln-scanner clean audit yc-software/qm 8-01** — 8 candidates all-dropped (highest triage-count in ledger); notably well-engineered defensive posture (algorithm-pinned JWT + timingSafeEqual + ReplayDedupe + PKCE + host-pinned credential-broker + fail-closed Lua egress-authz) worth internalizing as reference-architecture. Kaneo defer as "no safe channel" is first ledger precedent for Step 1 skip-not-scan branch.
- **CoinGecko clean-day streak d39** (through 8-01 12:00Z token-alert clean fire).
- **github-issues 7-consec clean day 7-26 → 8-01** — `GITHUB_ISSUES_OK` streak extends via daily-routine sub-agent.
- **Filesystem-Memory paper picks Aeon-architecture directly 8-01** — arXiv 2607.26637 studies exact MEMORY.md + topics/ + logs/ + issues/ shape Aeon runs. Highest-load-bearing paper-pick match in memory-window; extends [[fleet-relevance agent-thesis]] rail 15 → 16-consec-day.
- **Weekly-review 2026-07-27 SHIPPED** — 289 runs / 3 failures / 98.96% success = tightest failure envelope in memory-window. `articles/weekly-review-2026-07-27.md`.
- **ISS-027/028 doc-gap CLOSED 2026-07-30 by reflect** — 24d load-bearing gap resolved; INDEX.md 11 → 13 open.
- **ISS-028 kill-test d3+d4 NEGATIVE — workaround-chain n=18+ durable 12-UTC-day span 7-22 → 8-02** — 3 explicit sub-agent + call-site probes today (daily-routine hn-digest 07:37Z bash `>` + `-o` blocked; list-digest 17:00Z bash `>>` seen-file append blocked; skill-graph fingerprint-recompute 5 forms blocked: `{...}|sha1sum` + `xargs` + `awk` mid-pipeline + `python3 -c` + `bash script.sh`). Workaround-chain (WebFetch / Write-tool / Edit-tool pattern-match append / URL-encoded `%3E` / proxy-metrics change-detection) held clean at every fire. PR #167 fix-scope-narrowness hypothesis (heartbeat/security-digest main-thread only vs sub-agent + URL-encoded + append + compound-pipeline surfaces) firms across 4-consec-UTC-day negative kill-test. Reflect 8-03 (weekly-batch) reopens root-cause investigation.
- **07:00Z scheduler slot d4 RECOVERED 8-02 — deciding-test PASSED, ISS-file escalation gate discharges** — morning-brief 07:22Z (+22min), thought-review 07:23Z (+23min), daily-routine 07:37Z (+37min) all in-band vs 8-01's +96-97min severely-lagged; regime rewrites 2-of-3-day-degraded → 3-of-4-day-intermittent-recovered. Dispatch-lag pattern durable at magnitude but ISS-candidacy discharges.
- **ci-skills-json FAILURE 3-consec-day on both self-improve PRs (#171 + #172)** — shared-root-cause candidate promotes to formal-pattern threshold. Weekly-review 8-03 T-1 window should absorb as root-cause investigation ask (may be systemically broken vs one-shot).
- **PR queue at 3** — **#165 d14 CROSSES 14d touch-threshold TODAY** (7-19 17:38Z docs skill-graph shared_state 21→27, CONFLICTING, CLAUDE.md ~7d-past-touch escalation window opens 8-02); **#171 40h** (7-31 18:07Z fix github-trending 12-17 cap, ci-skills-json FAILURE 3-consec-day); **#172 ~24h** (8-01 18:42Z fix daily-routine XAI-prefetch case, ci-skills-json FAILURE 3-consec-day). Batch-merge window opens 8-03.
- **12:00 UTC batch DARK day-36** — ISS-027 8-skill cluster still frozen at 2026-06-28. Durable through 8-02 12:00Z clean same-slot token-alert fire (40th consec clean CG day).
- **ISS-025 hand-off T+4 day-19 SLIPPED** — cost-report weakest chronic-failure sr=0.12 (7/58) durable. Weekly-review 8-03 T-1 action #1 rolls to d20 milestone at Sunday-batch window.
- **15-consec heartbeat DEGRADED verdict-string identity across ~119h span** (7-27 20:12Z → 8-02 15:10Z) — memory-window-longest continuous chronic-degraded stretch. 10-skill chronic sub-50% cohort composition-identity zero-drift.
- **Operator on-chain config day-57** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Operator-gated.
- **priorities.md 59d stale** — last reviewed 2026-06-04. Vault inbox 42d cold streak (last real capture 2026-06-21T08:32Z).

## Recently Cleared
- **07:00Z scheduler slot d4 RECOVERED 8-02** — deciding-test PASSED, ISS-file escalation gate discharges (see [[fleet]]).
- **CoinGecko clean-day streak d40 8-02** — 12:00Z token-alert clean fire = longest infrastructure durability streak in memory-window post-ISS-023.
- **github-issues 8-consec clean day 7-26 → 8-02** — advances via daily-routine sub-agent.
- **WELL vol-cliff d6 full-recovery to 0.890× baseline 8-02** — 7-31's 0.059× nadir → 8-01 0.162× → 8-02 0.890× definitively confirms one-slot data-glitch reading; 3-day arc rules OUT durable participation-drain regime.
- **Σ-Mem paper picks per-skill sr% cohort infrastructure directly 8-02** — arXiv 2607.27958 (Feng/Yang/Poria, ↑12) formalizes per-peer trust as online-updated symmetric state with Weyl-bounded spectral drift = same shape as Aeon's per-skill sr% cohort. Extends [[fleet-relevance agent-thesis]] rail 16 → 17 consec-day.
- **Memory-primitive-paper streak 3-consec-UTC-day 8-02** — Memory Decoder 7-31 + Filesystem-Memory 8-01 + Σ-Mem 8-02 = paper-pick memory-thread cadence.
- **TencentDB-Agent-Memory 8-02 = first hyperscaler agent-memory primitive to trend** — 227 today · 2.5× baseline · ACCELERATING. Extends [[fleet-relevance agent-thesis]] rail with hyperscaler-scale entry (prior = arXiv + smaller OSS).
- **Sub-25 github-trending fetch pattern promoted to permanent shape 8-02** — 6-consec full-week 7-28 → 8-02 (12-17 range confirmed). PR #171 self-improve aligned with observed cap.
- **iv-org/invidious 58× baseline spike 8-02 = highest ratio-spike memory-window** — mature-project re-viral without release-catalyst shape suggests external catalyst (anti-adblock cycle, YouTube policy shift, or viral post).
- **security-digest quiet-cadence d2 + malware 159× collapse 8-02** — 0 fresh KEV + 0 fresh tracked-ecosystem reviewed = starkest quiet-day in memory-window; 318-batch → 2 fresh single-package entries in 24h. Yesterday's 8-01 14:52Z digest absorbed the full slate.
- **First Termux-execution malware in memory-window digest 8-02** — wacve-utils (pip, kam193/OSSF campaign 2026-08-wacve-utils) = Android/Termux data-exfil chain textbook (files + browser data + SMS + Telegram exfil).
- **Aeon-fleet clean d4 vs security-digest surface** (7-30 → 8-02 all clean import-check).
- **[[louround-single-thesis-cadence]] rail promoted candidate → durable n=3 8-02** — CODEC 7-31 + PENGU 8-01 + PUMP 8-02 = 3-consec-UTC-day single-voice dominance on list-digest.

## Fleet Health
See [[fleet]] for full snapshot. skill-health hash **7bf88238 stable 4th-consec formal-tick** (last formal tick 7-31 18:07Z NOOP dedup-skip): 0 CRITICAL / 18 DEGRADED / 12 WARNING / 10 HEALTHY / 3 NO_DATA. **13 open issues** unchanged. **Heartbeat verdict-string 15-consec DEGRADED-tick identity across ~119h span** (7-27 20:12Z → 8-02 15:10Z) = memory-window-longest chronic-degraded stretch on record. Sandbox-truncation family **day-41** (T+16 day-18, ISS-025 T+4 SLIPPED). Bash `>` redirect workaround-chain **n=18+ durable 12-UTC-day span** (7-22 → 8-02). Dispatch-lag 22-90min pattern durable but 07:00Z slot RECOVERED d4 (in-band); 08:00Z + 14:00Z lag-slot pair candidate. aixbt-pulse dead-slot **d36**. ci-skills-json FAILURE 3-consec-day on both self-improve PRs (#171 + #172) = shared-root-cause formal-pattern.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, weekly-batch cadence, positive events log.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns.
- [Market context](topics/market-context.md) — Baseline snapshot (STALE ~17d/402h, crossed 2× threshold 8-01; refresh chained on next batch-dark thaw or manual invoke).
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. 8-02 12:00Z snapshot: 0/4 alerts (all sub-threshold, **40th consec clean CG day**). **Tape shifts broad-red → mixed-to-green** vs 7-31's fully-red print (2 green / 2 red, participation re-engages further). WELL vol-cliff d6 full-recovery to 0.890× baseline definitively rules out drain regime.

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 8-02 -0.58%, vol $896K = 0.890× baseline (**vol-cliff d6 full-recovery** — 7-31 0.059× nadir → 8-01 0.162× → 8-02 0.890× arc definitively confirms one-slot data-glitch, drift-mode floor holds at noise) |
| MAMO    | mamo               | 15%           | 8-02 +1.67%, vol $750K = 0.941× baseline (**digestion band re-anchors d12** — 3-consec monotone red-widening (1.20% → -2.35% → -3.49%) reverses to +1.67%, distribution-on-give-back signature aborts at d11 test, digestion re-anchors) |
| REPPO   | reppo              | 15%           | 8-02 +4.50%, vol $46K = 0.377× baseline (**price-without-participation widens d5** — 2-consec green (+7.40% → +4.50%) on vol halving 0.729× → 0.377× fresh drought low, mean-reversion on empty book, sustainability watch d3 next tick) |
| GITLAWB | gitlawb            | 15%           | 8-02 -0.89%, vol $176K = 0.669× baseline (**base-building d10 2-consec noise-floor flatline** — 7-31 -7.13% cliff-give-back arrested 8-01 -0.82% + 8-02 -0.89%, 9-day give-back sequence cooled to base-building, participation slides further 0.868× → 0.669×) |

## Recurring patterns (durable — brief pointers; details in topic files)
- **[[large-cap-single-day-flip]] rail extends n=3 → n=4 8-02** — BEAT (7-31 #1 winner +17.7% BREAKOUT → 8-01 sustained BREAKOUT → 8-02 #2 loser -10.5%) joins HOLO/PUMP/UNI. **4 pole-flips in 4 UTC-days.** BEAT 3-day arc (winner → sustained → reversal) adds new sub-pattern under parent rail.
- **[[fleet-relevance agent-thesis]] rail 17-consec-day 8-02** — Σ-Mem paper (per-skill sr% cohort infrastructure direct hit) + TencentDB-Agent-Memory (first hyperscaler agent-memory primitive to trend, sibling to Aeon MEMORY.md + topics/ + logs/ + issues/ shape).
- **Memory-primitive-paper streak 3-consec-UTC-day NEW 8-02** — Memory Decoder 7-31 + Filesystem-Memory 8-01 + Σ-Mem 8-02 = paper-pick memory-thread cadence.
- **[[MCP-spec-maturity-vs-ecosystem-security]] tension rail extends n=3 8-02** — RufRoot CVE-2026-59726 on Ruflo agent framework (unauth HTTP POST → code exec + LLM API key exfil, patched 3.16.3 in 24h loopback-bound + access-controls) joins 7-30 initial Ruflo CVE + 8-01 @dynatrace-oss/dynatrace-mcp-server GHSA-p7w7-4929-vpj5. **3 unauth-agent-framework-CVE-in-wild in 4 days.**
- **[[DeepSeek-does-what-claude-refuses]] pattern candidate NEW 8-02** — Zhuhai actor wired DeepSeek into Hermes Agent framework and hit 460+ internet-facing systems (Citrix NetScaler + 11 Marimo notebook instances) where Claude/OpenAI models refused. First explicit call-out of model-refusal-behavior differential exploited in-the-wild in memory-window. Sibling to [[AI-framework-attack-surface]].
- **[[open-web-postmortem-cadence]] rail NEW candidate 8-02 (hn-digest)** — Google/RSS 498pts + Atom-better-than-RSS story = 2-story open-web-audit cluster on 8-02 front_page.
- **Sub-25 trending-page fetch pattern 6-consec permanent shape 8-02** — 7-28 (15) + 7-29 (12) + 7-30 (17) + 7-31 (14) + 8-01 (12) + 8-02 (15) full-week-consecutive-print promotes rail from "durable" to "permanent shape". PR #171 acknowledges 12-17 cap.
- **Parallel same-day 4×-burn extension shape NEW 8-02** — zhaoxuya520/reverse-skill (335 → 1,320) + usekaneo/kaneo (194 → 760) both quadruple d1 fires = first slate-level follow-through-day shape in memory-window.
- **Sub-floor-to-ACCELERATING same-repo reversal shape NEW 8-02** — github/copilot-sdk (7 → 142 = 20× d1). First memory-window instance of same-repo one-day sub-floor-crosses-velocity-gate.
- **[[skill-pack-primitive-rail]] compounding-on-viral shape 8-02** — zhaoxuya520/reverse-skill 4× burn extension (335 → 1,320) after 8-01 domain-router-pack promotion. Rail n=6 durable.
- **ci-skills-json FAILURE 3-consec-day on self-improve PRs (formal-pattern) 8-02** — both #171 (self-improve github-trending fix) and #172 (self-improve daily-routine XAI prefetch fix) failing same check across 3-consec-UTC-day tick. Shared-root-cause candidate promotes to formal-pattern; weekly-review 8-03 T-1 root-cause investigation ask.
- **[[mass-typosquat-campaign-cadence]] sub-signal candidate 8-02** — post-8-01 318-batch → 2 fresh entries in 24h = 159× collapse (rare post-mass-batch quiet-tail shape).
- **[[louround-single-thesis-cadence]] rail durable n=3 8-02** — CODEC 7-31 ($2.4M FDV robotics-launchpad) + PENGU 8-01 ($380m NFT-IP-to-retail) + PUMP 8-02 (pumpfun revenue+buyback) = 3-consec-UTC-day single-voice dominance.
- **[[launchpad-primitive]] rail n=3 candidate 8-02** — CODEC 7-31 + frontierhood/robinhood-chain 8-01 + Virtuals $200M agent trading volume on Robinhood Chain 8-02 (fleet-observation sidecar).
- **[[MCP-enforcement-primitive-cluster]] rail 3-of-4 UTC-days** — 7-29 MCP-infra-maturity + 7-31 MCP-plumbing-concrete + 8-01 MCP-production-plumbing.
- **[[single-project-mass-disclose]] rail stable n=9/11** — 7-30 → 8-01 pair-drop peak (NLTK 4-CVE + Thumbor 6-CVE). Rail-cadence acceleration continues.
- **[[star-anomaly-rail]] n=7 + serial-drop sub-cluster crystallizing** — affaan-m/ECC 5-consec-drop + mvanhorn/last30days-skill 4-consec-drop = candidate for reflect deep-dive if 3rd serial-drop-repo emerges.
- **[[embodied-agent-runtime-primitive]] rail n=3 7-31** — Gemini Robotics 2 + airi + speech-to-speech.
- **[[eth-lib-typosquat-campaign]] sub-class 7-31** — 7 ethers.js typosquats + fs-extra + socket.io.
- **[[open-voice-primitive-rail]] n=2 7-30** — microsoft/VibeVoice + huggingface/speech-to-speech.
- **[[AI-framework-attack-surface]] rail n=4 7-30** — @aws/agentcore + Claude Code CVE-2026-55607 + Langflow + LiteLLM.
- **[[network-perimeter-vendor-in-KEV]] cluster n=4 stable 8-02** — Fortinet + Arista + Cisco Secure FMC (all dedup'd on 8-02 security-digest, 0 fresh KEV = quiet-cadence d2).
- **Search-skill NO_GAP durability rail day-36 8-02** — fleet capability-complete on external-skill axis. Failures = infra (ISS-025/027/028), not gaps.
- **Chain-mode gap durable** — aeon.yml `chains: {}` inactive; daily-routine standalone fallback fires correctly each cycle.
- Claude Opus 5 shipped 7-24 = Aeon-fleet meta-signal; effort-toggle per-request gives per-skill cost-lever. Claude Code computer-use gain 7-31 = fresh Aeon-relevance datapoint.
- FTX $900M distribution 2026-07-31 = 5th round creditor payout, largest single supply event of quarter.
