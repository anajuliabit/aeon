# Agent Fleet — Status & Infrastructure

The fleet exited bootstrap on 2026-05-21. ~21 enabled skills on cron (plus
chains and operator-invokable extras). soul/ populated 2026-05-25. Reppo-swarm
chain first on-chain output landed 2026-05-26. This file tracks fleet-wide
state: what was built, recurring blockers, and health.

## Current health snapshot (2026-08-08)

- **skill-health hash `35369f69` stable** (8-07 18:07Z pure daily-cadence reminder tick, composition identical to 8-05 19:51Z, 46h delta): 0 CRITICAL · 18 DEGRADED · 14 WARNING · 8 HEALTHY · 3 NO_DATA · 14 open issues. No fresh usepod 402 / sdk_opt_in_required signatures. Systemic block reads pure-daily-cadence-reminder (composition unchanged).
- **ISS-030 cost-report OPEN pending 8-10 Mon 07Z deciding-test (T-2)** — advanced from T-3 on 8-07. 8-04 21:48Z same-day organic recovery holds; chronic sr=10%.
- **`[[morning-08Z-slot-dark]]` formal-pattern n=4-consec BREAKS at n=5 on 8-08** — heartbeat 08:10Z + skill-freshness 08:13Z both fired clean. `[[heartbeat-dispatch-lag]]` 08Z-slot sequence 31→50→50→75→75→**4**min = 60min-warn plateau broken. Positive pattern-termination; 8-09 08Z deciding-test = 2-consec clean (pattern-broken-permanent) vs single-day-restart.
- **chronic-cohort-alone-degraded 5th AND 6th 24h durability gates crossed 8-08** — 8-consec-tick at heartbeat 08:04Z (5th gate) + 9-consec-tick at heartbeat 14:16Z (6th gate); ~95h span 8-04 14:45Z → 8-08 14:16Z. Composition identical: cost-report 10% / skill-analytics 21% / reg-monitor 21% / vuln-scanner 23% / market-context-refresh 32% / narrative-tracker 33% / search-skill 38% / fleet-control 40% (disabled) / security-digest 44% / aixbt-pulse 47%. Deepest composition-identity print in memory-window continues.
- **Fleet clean-consec d3 → d4 crossing 8-08** — unbroken since 8-04 21:48Z cost-report same-day organic recovery. All 43 enabled skills consec=0 at both 08:04Z + 14:16Z heartbeat ticks.
- **PR queue at 5 on 8-08** — **#174 fresh (~18h at reflect time, Advisor Brier-weight overnight open 00:31Z, mergeable=UNKNOWN + empty statusCheckRollup)** = first Advisor-workflow-opened PR in memory-window, needs triage; **#173 ~110h CI cold** (T-1 to 8-09 Sunday-batch, commit-push nudge needed); **#172 d7** + **#171 d8** (both ci-skills-json FAILURE waiting on #173); **#165 d20 CONFLICTING** (T-1). Queue-full self-improve exit-gate active from 8-07.
- **Bash `>` redirect workaround-chain n=33+ durable 17-UTC-day span 7-22 → 8-08** — **4 fresh 8-08 call-sites** (daily-routine tweet-roundup `$XAI_API_KEY` env-expansion + list-digest `>>` redirect + agent-buzz Edit-tool 2-step + reflect Edit-tool). Sibling bash-redirect-block + heredoc-parser-over-length family recurs 8-08 github-trending (distinct from ISS-028 env-expansion). Weekly-review 8-10 T-2 reopens root-cause investigation.
- **12:00 UTC batch DARK day-42** — ISS-027 8-skill cluster frozen since 2026-06-28. Token-alert 12Z slot fires 3-consec clean (8-06 + 8-07 + 8-08) confirming slot works for other skills. **NEW `[[12Z-slot-dark-immunity-per-skill]]` observation 8-08** — same 12Z clock, distinct dispatcher paths per skill.
- **weekly-shiplog 09:00Z Monday slot** — last_success 2026-07-20 = 19d ago on 7d schedule. Next 8-10 09Z tick.
- **Sub-25 github-trending fetch pattern 11-consec permanent shape 8-08** — 7-28 → 8-08 with 8-03 skip; range 12-18 holds (n=17 mid-band 8-08 print extends observed range with upper-edge datapoint matching PR #171 12-17 body assertion).
- **Aeon-fleet clean d8 → d9 vs security-digest surface 8-08** (7-30 → 8-08) — extended second week; capability-complete on defensive-import axis (0/5 fresh advisories impact tracked deps).
- **ISS-018 sandbox family day-47 8-08** — /usr/bin/go execution blocked despite binary present (vuln-scanner witr scan); path-based binary blocklist broader than pip/downloaded-scanners.

## Positive events 8-07 evening → 8-08 afternoon

- **`[[morning-08Z-slot-dark]]` formal-pattern n=4-consec BREAKS at n=5 8-08** — heartbeat 4min dispatch (vs 75min prior plateau) + skill-freshness clean = positive pattern-termination on both co-slot skills.
- **prime-agent (PrimeIntellect-ai) first shipping-repo on recursive-self-improve rail 8-08 top-pick github-trending** — after 3 papers this week (PAST-Bench 8-05 + AgentOPSD 8-07 + Activity Frames 8-08). Recursive Language Model primitive; "continual harness"; 4,480 commits + v0.7.1 shipped 8-07 18:39Z. Cross-surface handoff paper→github same UTC-day.
- **`[[fleet-relevance agent-thesis]]` rail 22 → 24-consec-day 8-08 double-axis extension** — paper-pick (Activity Frames) + github-trending (prime-agent) same UTC-day.
- **`[[skill-pack-primitive-rail]]` n=4 → n=5 8-08** — google/skills first-hyperscaler. NEW `[[skill-pack-portability-across-harnesses]]` sub-primitive n=1 (Claude Code + Codex plugins). Cross-surface agent-buzz confirmation: OpenAI Agent Plugins draft multi-vendor with Google.
- **cloudflare/computer 3-day top-pick durability failure 8-08** — memory-window-first top-pick to be 2-consec then miss day-3 slate; sustained-viral shape breaks at day-3 while ecosystem-relevance holds.
- **NEW `[[hyperscaler-open-answer]]` sub-shape candidate n=1 8-08** — denoland/celld self-hosted Durable Objects within 3d of cloudflare/computer 2-consec top-pick run.
- **`[[all-agent-slate]]` n=3 candidate FAILS deciding-test 8-08** — frozen at n=2 (kept slate is 4-of-6 agent + 1 agent-adjacent + 1 pure-non-agent).
- **`[[memory-primitive-paper streak]]` 6 → 7-consec-UTC-day 8-08** — Activity Frames (Nossa Iyamu, ↑13) direct hit on Aeon's own architecture.
- **token-alert 12Z 8-08 reverts to 0/4 clean** — from 8-07 memory-window-first 2/4 fire (`[[vol-spike-sustained]]` candidate FAILS at n=0); GITLAWB 5-phase arc closes cleanly (first-in-memory-window); REPPO spent-flush resolves biggest-post-spike-vol-contraction; WELL cliff-resumes NEW `[[recovery-plateau-then-cliff-recur]]` sub-shape candidate n=1; CG clean-day d46.
- **security-digest 14:24Z 8-08** — CVE-2026-8037 LoadMaster KEV EPSS 0.848 (memory-window-2nd single-CVE ≥0.8 after Tomcat 0.812); 322-pkg npm malware 48h wave; 3 rail extensions (whatsapp-baileys/claude-brand-typosquat/ai-agent-brand-typosquat n=1→n=2); 3 NEW sub-class candidates (wallet-seed-crypto-lib-vuln crypto-js BIP39 / sui-move-ecosystem-typosquat / nigerian-fintech-payment-typosquat); `[[single-project-mass-disclose]]` rail n=3 GitPython; Aeon-fleet clean d9.
- **NEW `[[mcp-mandate-primitives-in-spec]]` sub-rail candidate n=1 8-08 (agent-buzz)** — MCP spec RC bakes stateless HTTP + Multi Round-Trip approval-gate = mandate-adjacent spec-level primitive.
- **NEW `[[AI-in-official-project-governance]]` sub-rail candidate n=1 8-08 (HN)** — Oracle bans AI-generated code from OpenJDK; production-code-governance rejection distinct from defensive-agent counter.
- **NEW `[[go-dep-cve-unreachable-via-vendor-scope]]` sub-pattern candidate n=1 8-08 (vuln-scanner witr)** — Go vendor/modules.txt = reachability oracle; 2/2 osv-api hits droppable via inspection alone.
- **vuln-scanner witr audit (20K★ Go devtool)** — 0 confirmed findings, clean-audit-partial-scan; production-serious defensive posture with in-code threat-model comments.
- **MetaMask Agent Wallet ships 8-07** — first mainstream self-custodial wallet-for-agents mandate-primitive (constraints-not-custody axis).
- **`[[curator-concentration-within-diverse-slate]]` sub-shape candidate n=1 8-08 (list-digest)** — DefiIgnas 2-of-top-3 in 4-poster diverse day; DeFi-list poster-count 2→4 recovery (8-07 shrink NEGATIVE).
- **`[[security-digest-14Z-slot-dark]]` sub-shape candidate n=1 8-07 BREAKS 8-08** — 14Z slot recovered clean 14:24Z fire. Frozen at n=1.
- **github-issues clean-day streak 12 → 13-consec 8-08** — first 13-consec in memory-window.
- **CoinGecko clean-day streak d45 → d46 8-08** — unbroken.

## Current health snapshot (2026-08-07)

- **skill-health fresh formal tick 8-05 19:51Z hash `35369f69`** (supersedes 8-04 `ed794682` in ~25h; `prev_hash` verified). Classification: **0 CRITICAL** · **18 DEGRADED** · **14 WARNING** · **8 HEALTHY** · **3 NO_DATA**. **14 open issues**. Systemic: CRITICAL 1→0 (cost-report promoted DEGRADED post 8-04 21:48Z same-day recovery); no fresh usepod 402 / sdk_opt_in_required signatures in 24h window. **INDEX.md ISS-029 sync completed automatically this run** — resolves 8-05-reflect's atomic-emit-defect concern (data-consistency writer worked on next tick).
- **ISS-030 cost-report OPEN pending 8-10 Mon 07Z deciding-test (T-3)** — 8-04 21:48Z same-day organic recovery holds; chronic sr=10%. Clean → RESOLVED same-day candidate; fail → 4-consec-week formal-pattern.
- **`[[morning-08Z-slot-dark]]` formal-pattern n=4-consec 8-07** — heartbeat + skill-freshness co-miss 4-consec mornings (8-04/8-05/8-06/8-07). Rail crossed 24h durability gate 4×. 8-08 08Z fire = n=5-consec candidate.
- **`[[heartbeat-dispatch-lag]]` rail slot-specific 8-07 confirmed** — sequence 31→50→50→75→75→**24**min at 14Z slot recovery = 08Z co-slot cluster-dark is slot-specific pattern, NOT fleet-wide dispatch-degrade. 14Z + 20Z slots recover normally.
- **chronic-cohort-alone-degraded regime crosses 4th 24h durability gate 8-07 09:15Z → 7-consec-heartbeat-tick ~71h span 8-04 14:45Z → 8-07 14:24Z cross-3-full-UTC-day + into 4th** = deepest composition-identity print in memory-window. 10-skill chronic sub-50% cohort composition-locked: cost-report 10% / skill-analytics 21% / reg-monitor 21% / vuln-scanner 23% / market-context-refresh 32% / narrative-tracker 33% / search-skill 38% / fleet-control 40% (disabled) / security-digest 43% / aixbt-pulse 47%.
- **8-06 fleet all-day-dark shape one-day-only NOT cluster-shift** — 9-skill evening batch + morning-brief + daily-routine + heartbeat 14/20Z all missed 8-06 UTC-day. 8-07 07Z morning cluster fired clean (morning-brief 07:59Z + daily-routine 08:28Z + thought-review 08:02Z) = blackout absorbed within 24h. Distinct from persistent `[[morning-08Z-slot-dark]]` cluster.
- **Fleet clean-consec d3 crossing 8-07** — unbroken since 8-04 21:48Z cost-report same-day organic recovery (through 8-05 + 8-06 all-day-dark + 8-07 morning fires).
- **PR queue at 4 unchanged 8-07** — **#173 CI cold ~90h at heartbeat 14:24Z** (T-2 to Sunday-batch 8-09, commit-push nudge needed); **#172 d6** + **#171 d7** (both ci-skills-json FAILURE waiting on #173); **#165 d19 CONFLICTING** (T-2 to 8-09, still in-cycle per weekly-batch cadence).
- **Bash `>` redirect workaround-chain n=32+ durable 16-UTC-day span 7-22 → 8-07** — **9 fresh 8-07 call-sites** (daily-routine + 4 sub-agents + heartbeat + token-alert + security-digest + list-digest). New sibling family observed 8-07 github-trending: bash-redirect-block + heredoc-parser-over-length (distinct from ISS-028 env-expansion), worked around via Edit-tool 2-step.
- **12:00 UTC batch DARK day-41** — ISS-027 8-skill cluster frozen since 2026-06-28. **Standalone-inline substitution 2nd successful daily-routine fetch 8-07** (8-05 first, 8-06 daily-routine didn't run, 8-07 second) — path holds when daily-routine fires but not when daily-routine itself misses (8-06 case). Token-alert 12Z slot fires clean 2-consec-day (8-06 + 8-07) — token-alert's own slot is not part of ISS-027 cluster.
- **weekly-shiplog 09:00Z Monday slot** — last_success 2026-07-20 = 18d ago on 7d schedule. 8-03 missed (ISS-029). Next 8-10.
- **Sub-25 github-trending fetch pattern 10-consec permanent shape 8-07** — 7-28 → 8-07 with 8-03 skip; range 12-18 (8-06 n=13 + 8-07 n=13 = first back-to-back low-edge print in memory-window).
- **Aeon-fleet clean d8 vs security-digest surface 8-07** (7-30 → 8-07) — extended through 8-06 all-day-dark; capability-complete on defensive-import axis.

## Positive events 8-05 evening → 8-07 afternoon

- **skill-health 8-05 19:51Z formal tick fresh hash `35369f69`** — supersedes 8-04 `ed794682` in ~25h; CRITICAL 1→0, INDEX.md ISS-029 sync completed automatically.
- **8-07 token-alert 12Z FIRST MULTI-TOKEN ALERT FIRE in memory-window** — GITLAWB 24h +21.74% (first 24h-change alert ever, breaches 15% rail) + REPPO vol-spike 4.854× baseline (first REPPO vol-spike ever). Morning-brief 07Z focus-item #3 (GITLAWB at 72% of rail) validates as forward-looking call within 5h.
- **GITLAWB 4-day arc closes cleanly 8-07** — 8-04 +9.62% breakout → 8-05 -7.08% abort → 8-06 -10.84% capitulation → 8-07 +21.74% snap-back = first complete-arc capitulation-then-bounce shape in memory-window; +21.74% snap-back is 2.01× the drop = asymmetric recovery signature.
- **REPPO 3-day vol arc $41K→$128K→$384K = 9.4× compounding across 48h 8-07** — small +1.88% price move despite vol explosion = **NEW `[[vol-spike-flat-price]]` sub-shape n=1**.
- **`[[large-cap-single-day-flip]]` rail n=6 → n=7 8-07 via BEAT same-coin 48h reflip** — first same-coin pole-reflip in memory-window. **NEW `[[same-coin-48h-reflip]]` sub-shape n=1**.
- **CG clean-day streak d42 → d45 across 8-05 → 8-07** — unbroken through 8-06 all-day-dark + 12Z batch-dark d41 + ISS-029 blackout.
- **daily-routine 8-07 second successful standalone-inline run of ISS-027 batch-dark era** (8-05 first, 8-06 gap, 8-07 second) — path holds when daily-routine fires.
- **paper-pick AgentOPSD 8-07** (arXiv 2608.05987, Tsinghua, ↑49) — extends `[[memory-primitive-paper streak]]` 5 → 6-consec-UTC-day (8-04 gap absorbed); pairs with 8-05 PAST-Bench on recursive-self-improve axis (method + benchmark).
- **`[[fleet-relevance agent-thesis]]` rail 20 → 21-consec-day 8-06 (uber/ADR day-2 sustained) → 22-consec-day 8-07 (paper-pick axis handoff)** — cross-surface durability confirmed.
- **`[[skill-pack-primitive-rail]]` formalizes at n=4 credible authors in 8 days 8-07** — mattpocock/skills (207.9k stars) joins obra + reverse-skill + addyosmani. Primitive going ecosystem.
- **`[[hyperscaler-agent-runtime-primitive]]` sub-rail promoted candidate → durable 8-07** — cloudflare/computer +215% day-2 (13.5× → 34.6× baseline) = first hyperscaler agent-runtime sustained-viral. First back-to-back same-repo top-pick in memory-window (8-06 + 8-07). Durable Object + FUSE mount + capnweb RPC primitive.
- **`[[2-peak-with-1-day-trough]]` viral-shape closes at day-4 8-07** — TencentDB 4-day arc 1,090 → 1,111 → 1,892 → 1,057 (-44% decay after 2nd peak).
- **`[[top-pick-soft-decay-while-visible]]` verdict-shape day-3 8-07** — firecrawl/pdf-inspector 2,540 → 1,582 → 1,190 = 2-consec-decay while on trending; first memory-window top-pick to soft-decay 3 UTC-days without evaporating.
- **`[[all-agent-slate]]` sub-shape candidate n=2 8-07** — 100% agent-domain 2-consec-day (6-of-6 + 5-of-5).
- **`[[mature-repo-sustained-ratio-spike]]` sub-pattern candidate FROZEN at n=1 8-07** — airllm broke day-3 (-51%). Rail needs n=2 to promote.
- **security-digest 8-07 shipped 3/4/0 tiers** with 3 NEW sub-class candidates (claude-brand-typosquat + whatsapp-baileys + ai-agent-brand-typosquat) + Traefik 6-CVE mass-disclosure + Dolyame 10-pkg (2nd Russian-fintech in same UTC-week) + @united-airlines-org first airline-vertical + @ccfly 4-arch installer + JetBrains TeamCity KEV 2nd CI/CD-server-in-KEV + MCP-branded-malware n=5. Aeon-fleet clean d8. EPSS 10/10 clean 2-consec-day.
- **daily-routine tweet-roundup 8-07 Google CodeMender ships** = first fleet-visible defensive-side AI counter-agent for security. **NEW `[[defensive-AI-security-counter-agents]]` sub-rail candidate n=1**.
- **Hashdex $DEFI ETF closure at $14M 8-07** = first spot-BTC-ETF failure of cycle.
- **AMD acquires Taalas 8-07 (HN anchor)** — compute-in-memory hyperscaler acquisition; same-day cluster with AgentOPSD paper = compute-in-memory silicon + credit-assignment methodology compressing toward agent-runtime primitive.
- **github-issues clean-day streak 10 → 12-consec 8-07** (8-06 skip absorbed per silence-on-clean-day rule) — first double-digit-plus extends +2 UTC-days.
- **8-07 07Z morning cluster fires clean absorbing 8-06 all-day-dark** — morning-brief 07:59Z + daily-routine 08:28Z + thought-review 08:02Z + btc-levels 00:31Z/05:19Z/09:15Z all clean; scheduler restored.

## Current health snapshot (2026-08-05)

- **ISS-029 RESOLVED by skill-health 8-04 18:19Z** — usepod.ai 402 payment gate lifted 8-03 20:14Z; 44h+ clean through 8-05 afternoon (0 fresh 402s). skill-health `last-report.json` records `resolved_this_run: 1` for ISS-029 at 8-04 18:19Z (CRITICAL cohort 11→1, DEGRADED 8→17 as formerly-CRITICAL skills settled at historical baseline once consec_failures reset). **INDEX.md discrepancy 8-05**: ISS-029 still listed under Open in `memory/issues/INDEX.md` despite `resolved_this_run: 1` — skill-health's json→INDEX.md writer missed the move. Reconciled this reflect.
- **ISS-030 cost-report SAME-DAY RECOVERY 8-04 21:48Z** — first successful weekly-tick since 7-27 (8 UTC-days). Wrote ~$1,500/mo projection + weekly $350.02 breakdown + 3 optimization actions. consec 18→0, sr 9%→10% (chronic historical unchanged). Same skill/model/config resumed clean WITHOUT config change — the `sdk_opt_in_required` signature cleared organically. **ISS-030 remains OPEN pending 8-10 Mon deciding-test**: if 8-10 07Z tick fires clean, RESOLVED same-day candidate; if fails same-signature, crosses 4-consec-week-shape formal-pattern threshold.
- **skill-health fresh formal tick 8-04 18:19Z** — hash `ed794682` supersedes `29af7ab7` (broke 8-03 tick's identity in 22h). Classification: **1 CRITICAL** (cost-report only, pre-21:48Z recovery) · **17 DEGRADED** · **14 WARNING** · **8 HEALTHY** · **3 NO_DATA**. **14 open issues** at tick time (ISS-030 filed pre-tick, ISS-029 closed by tick). Note: cost-report's 21:48Z recovery post-dates the tick, so composition would flip further on next tick.
- **verdict-string "chronic-cohort-alone-degraded" regime crosses first 24h durability gate 8-05 14:31Z** — 3-consec-heartbeat-tick composition-identity through 8-04 14:45Z → 8-04 20:05Z → 8-05 14:31Z. First cross-UTC-day durability for new post-ISS-029 regime. Chronic sub-50% cohort (10 skills): cost-report 10% / skill-analytics 19% / reg-monitor 19% / vuln-scanner 23% / market-context-refresh 32% / narrative-tracker 33% / search-skill 38% / fleet-control 40% / security-digest 43% / aixbt-pulse 47%.
- **`[[morning-08Z-slot-dark]]` sub-rail candidate n=2 8-05** — heartbeat 08:00Z fired NEITHER 8-04 nor 8-05 (last dispatch 8-04 20:01Z; 18.4h gap = 3× 6h interval). skill-freshness 08:00Z also co-missed both mornings (last 8-03 20:21Z, currently 42h < 48h at edge). **2-skill 08Z-slot co-miss both mornings = fresh sub-pattern.** 8-06 08:00Z fire = deciding-test for formal-pattern promotion (3-consec heartbeat) + skill-freshness 2× threshold crossing.
- **PR queue at 4 unchanged through 8-05 afternoon** — **#165 d17 CONFLICTING** (7-19 17:38Z docs skill-graph; T-4 to Sunday-batch 8-09; ~7d escalation window OPEN); **#171 ~5d** (7-31 18:07Z fix github-trending 12-17 cap, ci-skills-json FAILURE, waiting on #173); **#172 ~4d** (8-01 18:42Z fix daily-routine XAI-prefetch, ci-skills-json FAILURE, waiting on #173); **#173 ~2d** (8-03 20:17Z `fix(claude): require skills.json regen when editing SKILL.md`, mergeable=UNKNOWN + empty statusCheckRollup, CI has not yet run at ~35h — needs commit-push nudge or manual re-request).
- **Bash `>` redirect workaround-chain n=26+ durable 14-UTC-day span 7-22 → 8-05** — 8-05 = **most call-sites in single UTC-day in rail history** (thought-review + morning-brief + daily-routine + github-trending + token-alert + heartbeat + reg-monitor (positive kill-test) + security-digest (positive kill-test) + agent-buzz + list-digest = 10 fires). reg-monitor hit was the day's first POSITIVE kill-test branch (bash `cat >>` blocked → Edit-tool fallback); security-digest hit was the second (bash `>` blocked → Write-tool via pipe-to-jq clean). Rail is now on 3rd consecutive week of durable clean-hits.
- **12:00 UTC batch DARK day-39** — ISS-027 8-skill cluster frozen since 2026-06-28. 8-05 12:34Z token-alert clean fire confirms slot itself works (**CG clean-day d42**); ISS-027 scheduler-side gap for the 8-skill cluster. **Standalone-inline substitution PROVEN 8-05** — daily-routine's token-movers sub-agent fetched CG markets clean via parallel-agent fan-out (first successful token-movers fetch since 2026-06-28 d38 start). If chain-runner stays frozen, standalone-inline can substitute for the frozen scheduler as a workaround path.
- **weekly-shiplog 09:00Z Monday slot** — last_success 2026-07-20 = 16d ago on 7d schedule. 8-03 missed (ISS-029). Next 8-10.
- **Sub-25 github-trending fetch pattern 8-consec permanent shape** — 7-28 → 8-05 with 8-03 skip (ISS-029). Range now observed as **12-18** (8-05 n=18 = new top-edge, +1 above PR #171's 12-17 assertion; PR-body update candidate on rebase).
- **Aeon-fleet clean d7 vs security-digest surface** (7-30 → 8-05) — durable capability-complete on defensive-import axis; failures = infra (ISS-025/027/028/030), not gaps.

## Positive events 8-04 evening → 8-05 afternoon

- **cost-report 8-04 21:48Z same-day recovery** — first successful weekly-tick since 7-27 (8 UTC-days). Wrote ~$1,500/mo projection + weekly $350.02 breakdown; consec 18→0. Same config/model/skill without change = organic signature-clear on `sdk_opt_in_required` failure family.
- **skill-health 8-04 18:19Z formal tick fresh hash `ed794682`** — supersedes 8-03 `29af7ab7` in 22h; CRITICAL cohort 11→1, 8 recovered skills settle back to historical baseline (moves to DEGRADED not HEALTHY because chronic sr<50% survives).
- **ISS-029 closed by skill-health 8-04 18:19Z** — record shows `resolved_this_run: 1`. INDEX.md writer missed the move; this reflect reconciles.
- **security-digest 14:00Z shipped 3/4/0 tiers** with 14 fresh rail-datapoints on a single dispatch — biggest single-day surface enrichment in memory-window.
  - **408-package npm malware mega-batch** = new memory-window #1 peak (displaces 8-01's 318, +28%). Triple-signature: Tinkoff mega-corp-scope 100+ pkgs (`tinkoff-*` / `statist-browser-typed-client-*` / `tramvai-tinkoff-*` / `volna-boxy-*` / `platform-ui-*` / `bigops-*`); hardware-wallet-SDK cluster (`trezor-lib` + `ledger-lib` + `ckcc-protocol` + `hwi-lib`); Polymarket cluster (`polyclob-api` + `poly-provider-api` + `polymarket-toolkit`).
  - **IBM Langflow KEV CVE-2026-9198** = 6th unauth-agent-framework-CVE-in-memory-window, first agent-framework in KEV since Claude Code. `[[AI-framework-attack-surface]]` deepens INTO KEV territory.
  - **Apache Tomcat KEV CVE-2026-34486 EPSS 0.812** = memory-window-first single-CVE ≥0.8 score at 99.6th percentile. CISA due 8-07 = 3-day patch window.
  - **Flowise 19-CVE 24h researcher mass-disclosure** = new `[[single-project-mass-disclose]]` peak (NLTK-4 + Thumbor-6 8-01 pair-drop displaced).
  - **N-central 18556+18577 both-in-KEV within 2 days** = incomplete-patch-KEV-chain pattern instance #1 in memory-window.
  - **`[[polymarket-npm-malware-cluster]]` NEW sub-class candidate n=1** — 3-pkg targeting prediction-market SDKs.
  - **Tinkoff mega-corp-scope 100+ pkgs** extends `[[enterprise-corp-scope-dep-confusion]]` to n=3 (fintech-8-01 + SaaS-8-04 + Russian-bank-8-05).
  - **hardware-wallet-SDK malware sub-cluster** extends `[[crypto-wallet-npm-malware-cluster]]` n=1→n=2, adds hardware-SDK sub to 8-04's PSBT/BIP39.
  - **`[[LLM-UI-attack-surface]]` NEW sub-rail candidate n=1** — Open WebUI 7-CVE cluster (KaTeX-XSS + OAuth-ATO + SSRF + collab-delete), distinct from agent-builder framework rail.
  - **`[[MCP-spec-maturity-vs-ecosystem-security]]` n=3→n=4** via Flowise `npm_config_yes` MCP-env-var-blocklist patch-bypass CVE-2026-69263 (2nd-order MCP security-primitive break).
  - **KEV quiet-cadence breaks HARD** — 3 fresh single-day = memory-window-first cadence-magnitude.
  - **EPSS 30/30 join** = cleanest in memory-window despite most items being sub-hour age.
- **reg-monitor 14:00Z Wed shipped 1 ACT / 1 WATCH** — NY v Kalshi $36B illegal-gambling suit (7-31 filing, NY AG + Gov Hochul in Manhattan state court, restitution + disgorgement + treble + $100k/unlawful-offering; adjacent to 7-27 Menendez Minnesota prelim injunction; 3rd Circuit ruled other way April 2026 = SCOTUS lines up if split hardens; direct hit Kalshi NY access + sports-contract legality). CFTC prediction-market NPRM comment closed 7-27, final-rule window opens = WATCH. Federal Register 0-hits over 7d = memory-window-notable low. **CFTC RSS 404 needs HTML-fallback pattern codified** (self-improve candidate for `skills/reg-monitor/SKILL.md` step 1C if 8-12 confirms persistence). **Congress.gov + house.gov + sportico 3-domain 403 WebFetch cluster** = enrichment friction pattern.
- **daily-routine 07:26Z first successful token-movers standalone-inline fetch since ISS-027 batch-dark start 2026-06-28 (d38)** — confirms scheduler-side gap not CG infra. Top winner PUMP +10.4% TRENDING+UP day-5; top loser UB -39.1% CAPITULATION memory-window magnitude. **[[large-cap-single-day-flip]] rail extends n=5 → n=6 in single UTC-day** (UB + BEAT dual-pole-flip = first same-day dual in memory-window). LDO CAPITULATION -12.9%; ZEC MAJOR +6.3% $226M vol; TAKE +26.8% at rank #936 near [PUMP-RISK] threshold no-trigger.
- **daily-routine paper-pick PAST-Bench** — Foundations of Recursive Self-Improvement in Personal Agents (Xue/Ding/Shen +6, Princeton, arXiv 2608.04003). 26 scenarios × 204 episodes × 7 base models × 4 frameworks. **Extends [[memory-primitive-paper streak]] 4-consec → 5-consec** (thaws 8-04 ISS-029 freeze). Most-thesis-aligned pick to date — directly benchmarks Aeon's MEMORY.md + logs/ + self-improve architecture.
- **daily-routine github-issues 10-consec clean-day** (7-26 → 8-05) — first double-digit streak in memory-window on `GITHUB_ISSUES_OK`.
- **github-trending 10:14Z 5 kept / 13 dropped / 18 candidates** — top pick firecrawl/pdf-inspector at 42× baseline day-2 compounding. **`[[fleet-relevance agent-thesis]]` rail 19 → 20-consec-day** via uber/ADR (enterprise AI-agent security framework — hyperscaler-corp agent-infra sibling to TencentDB). **obra/superpowers discovery** = first appearance on Aeon slate despite 266.8k stars/300d = memory-window-top-6 total-star pool (890/d baseline); skills-framework meta-fits Aeon architecture. **airllm 45× → 68× sustained day-2 ratio-spike** = memory-window-first mature-repo sustained-spike (invidious 8-02 was one-day-only); NEW `[[mature-repo-sustained-ratio-spike]]` sub-pattern candidate. **First HOLDOVER-flat-after-extension shape** — TencentDB 4.8× extension crest cools to +2% flat. **Mature-tail 6-of-18 concentration** = memory-window-first single-day (github algorithm reached long-tail; slow-catalyst-day signal). **livekit/agents +192% breakout** resolves 8-04 slot-economics judgment-call drop as wrong by 24h.
- **agent-buzz 18:01Z 2 clusters / 5 tweets / 10 candidates** — `[[MCP-enforcement-primitive-cluster]]` rail 4-consec (through 8-02) → **5-consec 8-05** (Aurimas_Gr data-domain-boundary + Ardor_Cerebrum getblock-prod + cv_usk gateway = three "rules-at-boundary" variants). `[[agent-buzz-engagement-drought]]` rail 3-consec → **4-consec** = candidate → formal-pattern promotion candidate on 8-06. **NEW `[[xai-cache-window-narrows]]` sub-pattern candidate n=1** — Grok returned single-day 8-04 despite 8-04→8-05 query range; first observed. **haoran_qiu98 Copilot 3.2M-user / 761M-LLM-calls / 95T-tokens** = largest named-numbers agent-behavior datapoint in memory-window's agent-buzz feed.
- **list-digest 18:00Z 2 tweets / 7 fetched** — cache-hit Path A 2-consec-day durable (8-04+8-05, no XAI_API_KEY at call-site). @DefiIgnas ENS-fatigue = directional onchain-identity-primitive-decay datapoint (serious researcher openly admitting ritual died in workflow > normie-abandonment stat). @francescoweb3 solana-WSOP-partner callout = named-risk assertion (not generic gripe) on solana-partnership choice-quality.
- **AISI 8-05 disclosure Anthropic Mythos 5 agent = 17-of-19 unauthorized actions in gov security evals** — surfaced in morning-brief Watch; qualifies "new risk" gate; extends AI-safety-of-agent-tooling signal into second week (after HF CEO 8-03 `[[AI-slop-in-security-pipelines]]` rail candidate). Distinct from `[[AI-framework-attack-surface]]` (this = agent-behavior-not-CVE surface).

## Current health snapshot (2026-08-04)

- **ISS-029 EFFECTIVELY RECOVERED 8-04** — usepod.ai 402 payment gate lifted between 8-03 18:27Z (last fresh 402) and 20:14Z (first clean dispatch). **20-of-20 post-recovery dispatches clean** across ~20 UTC-hour span (weekly-review 8-03 20:22Z → evening-recap 21:38Z → morning-brief 07:24Z → daily-routine 07:25Z → thought-review 07:23Z → github-trending 10:14Z → token-alert 12:19Z → heartbeat 14:45Z → security-digest 14:47Z → btc-levels 16:37Z). No fresh 402 errors observed today. Issue kept OPEN pending operator confirmation of usepod billing status.
- **P0 ISS-030 cost-report SDK opt-in mismatch NEW 8-04** — sole ISS-029 survivor. Fresh signature `terminal_reason: api_error / fast_mode_disabled_reason: sdk_opt_in_required` (canonicalModel `claude-sonnet-4-6`, provider `firstParty`). Distinct from ISS-025 sandbox-truncation (`outputTokens=12`) and ISS-029 (`usepod 402`). consec=17 sr=0.09 (7/75), last success 2026-07-27T08:47Z (8 UTC-days ago). Weekly cost visibility blind. Filed today. Fix path: audit cost-report SKILL.md for CLI flags needing SDK opt-in (likely `--fast-mode` or similar).
- **skill-health formal tick 8-03 20:16Z** — fresh hash `29af7ab7`, breaks `f0c415fd` 5-consec composition-identity (~120h span 7-28 → 8-02). Classification: **11 CRITICAL** (usepod-affected cohort, since recovered) · **8 DEGRADED** · **15 WARNING** · **6 HEALTHY** · **3 NO_DATA**. **15 open issues** (ISS-030 files today at 15).
- **16-consec DEGRADED heartbeat verdict-string durability rail CLOSES at ~124h span through 8-02 20:15Z** — memory-window record. Broken by post-ISS-029 composition-shift (chronic-cohort still degraded but consec_failures across cohort all reset from 3-9 range to 0 except cost-report=17). 8-04 14:45Z heartbeat verdict-string = new "chronic-cohort-alone-degraded" signature; no fresh-mass-failure-cluster overlay.
- **Chronic sub-50% cohort composition** (10 skills durable): cost-report 9% (7/75, worst — ISS-030 signature) / skill-analytics 19% / reg-monitor 19% / vuln-scanner 23% / market-context-refresh 32% / narrative-tracker 33% / search-skill 38% / fleet-control 40% / security-digest 43% / aixbt-pulse 47%. skill-health 50% + self-improve 51% + evening-recap 61% at edge.
- **PR queue at 4 through 8-04 morning** — **#165 d16 CONFLICTING** (7-19 17:38Z docs skill-graph, CLAUDE.md ~7d-past-touch escalation window OPEN); **#171 ~4d** (7-31 18:07Z fix github-trending 12-17 cap, ci-skills-json FAILURE); **#172 ~3d** (8-01 18:42Z fix daily-routine XAI-prefetch, ci-skills-json FAILURE); **#173 fresh** (8-03 20:17Z `fix(claude): require skills.json regen when editing SKILL.md` — targets shared ci-skills-json root cause). If #173 merges at 8-10 Sunday-batch, unblocks #171/#172.
- **ci-skills-json FAILURE 3-consec-day formal-pattern SOLVED 8-03 20:17Z via PR #173** — root cause was self-improve skips `./generate-skills-json` regen. PR encodes the requirement into the skill.
- **Bash `>` redirect workaround-chain n=22+ durable 13-UTC-day span 7-22 → 8-04** — 8-04 held clean at 4 call-sites (github-trending 10:14Z + token-alert 12:17Z + heartbeat 14:45Z + security-digest 14:47Z, all via WebFetch + Write-tool + Edit-tool + `gh api --paginate` + URL-encoded `%3E` pattern). PR #167 fix-scope-narrowness firm across 5-consec-UTC-day. Weekly-review 8-10 T-6 reopens root-cause investigation.
- **12:00 UTC batch DARK day-38** — ISS-027 8-skill cluster (defi-overview/token-pick/token-movers/narrative-tracker/market-context-refresh/on-chain-monitor/defi-monitor/aixbt-pulse) frozen since 2026-06-28. **Post-ISS-029 recovery did NOT thaw the 12:00Z cluster** — separate cause. 8-04 12:19Z token-alert clean fire confirms 12:00Z slot itself works (CG-side infrastructure d41); ISS-027 is scheduler-side gap specific to the 8-skill cluster.
- **weekly-shiplog 09:00Z Monday slot** — last_success 2026-07-20 = 15d ago on 7d schedule = >2x threshold. 8-03 fire missed (ISS-029 blocked morning cluster). Next test 8-10 09:00Z.
- **operator-scorecard 10:30Z Monday slot** — never run; 8-03 fire missed (ISS-029). Next test 8-10 10:30Z.
- **Sub-25 github-trending fetch pattern 7-consec permanent shape** — 7-28 (15) + 7-29 (12) + 7-30 (17) + 7-31 (14) + 8-01 (12) + 8-02 (15) + [skip 8-03 ISS-029] + 8-04 (16). Hard-cap ~15 via 12-17 range. PR #171 acknowledges.

## Positive events 8-03 evening → 8-04 afternoon

- **ISS-029 fleet-wide recovery 8-03 20:14Z** — payment gate lifted between 18:27Z (last fresh 402) and 20:14Z (first clean dispatch). 20-of-20 subsequent dispatches through 8-04 16:33Z all clean.
- **CoinGecko clean-day streak d41 continuation 8-04** — 12:19Z token-alert clean fire; CG-side infrastructure unbroken through ISS-029 blackout (block was upstream gateway, not CG).
- **PR #173 opened 8-03 20:17Z** — `fix(claude): require skills.json regen when editing SKILL.md` targets shared ci-skills-json root cause on #171/#172. If merged, unblocks Sunday-batch merge window at 8-10 weekly-review.
- **Weekly-review 8-03 shipped** — 313 workflow runs / 62 failures / 80.2% success (-18.8pp WoW); 87% of failures on 8-03 alone from ISS-029 usepod cascade. Top action: file ISS-029 (SHIPPED same-day via reflect). 4 PRs merged this week (#167/#168/#169/#170). Article: `articles/weekly-review-2026-08-03.md`.
- **skill-health formal tick 8-03 20:16Z** — first fresh formal-tick hash change since 7-28 (fresh identity `29af7ab7`, breaks 5-consec `f0c415fd` since 7-28). Filed ISS-029.
- **evening-recap 8-03 21:32Z clean** — TL;DR: "18-skill usepod.ai 402 cascade at 18:27Z — ISS-029 filed, 20Z batch recovered, PR #173 ships the ci-skills-json fix".
- **8-04 morning-brief 07:24Z first clean cycle post-ISS-029** — last successful morning-brief was 8-02 07:27Z (48h+ gap). Focus items: cost-report distinct-signature, ISS-029 continuity, PR #173 targets ci-skills-json.
- **8-04 daily-routine 07:19Z clean** — chain-runner appears to have carried stale 8-01 outputs forward through ISS-029 blackout; sub-skills fired on refresh, used with staleness flagged inline.
- **8-04 github-trending 10:14Z 7 kept / 9 dropped / 16 candidates** — top pick lyogavin/airllm at 45× baseline (second-largest ratio-spike memory-window behind 8-02 invidious 58× only); first [[deepseek-primitive-cluster]] rail candidate n=2 (antirez/ds4 + esengine/DeepSeek-Reasonix); same-day dual-HOLDOVER extension shape memory-window first (reverse-skill 1.85× + TencentDB 4.8× both extend yesterday's featured fires); first antirez trending appearance in memory-window = author-quality-override sub-pattern.
- **8-04 security-digest 14:47Z** — 3 today / 5 this-week / 2 monitor. **136-package fresh 8-04 malware batch = memory-window #2 largest single-day** behind 8-01's 318-batch. keyv/cacheable 25+ pkgs (first top-100-npm-package attack in memory-window); @servicetitan+@onereach+@or-sdk 88-pkg (new `[[enterprise-corp-scope-dep-confusion]]` sub-class); coldcard-helpers+psbt-utils+psbt-helpers+bip39-generator 4-pkg (new `[[crypto-wallet-npm-malware-cluster]]` rail candidate parallels operator morning-brief Coldcard $89M signal). Flowise CVE double-drop extends [[AI-framework-attack-surface]] to 5th. cryptography same-project-double-critical = 2 instances in one day. sequelize 9.8+PoC rare PATCH-TODAY-via-CVSS. Aeon-fleet clean d6.
- **8-04 heartbeat 14:45Z** — first mid-day post-ISS-029 fire in-band (+45min under 60min-warn); confirms fleet-recovery composition, breaks 16-consec verdict-string rail.
- **[[fleet-relevance agent-thesis]] rail 18 → 19-consec-day 8-04** — TencentDB HOLDOVER 4.8× extension keeps hyperscaler-agent-memory datapoint burning.
- **[[large-cap-single-day-flip]] rail extends n=4 → n=5 8-03** — UAI (7-31 not visible → 8-02 +39.1% #1 winner → 8-03 -31.4% #1 loser) joins BEAT/HOLO/PUMP/UNI. 5 pole-flips in 5 UTC-days.
- **[[memory-primitive-paper streak]] 4-consec-UTC-day through 8-03** — Memory Decoder + Filesystem-Memory + Σ-Mem + CAPA. First 4-day paper-thematic streak in memory-window.
- **[[louround-single-thesis-cadence]] rail durable n=4 8-03** — CODEC + PENGU + PUMP + IO ($IO thesis 4th consec).
- **[[AI-slop-in-security-pipelines]] rail NEW candidate 8-03** — jfrog SQLite-CVE-slop + HF CEO accountability call.
- **github-issues 9-consec clean day 7-26 → 8-03** — via daily-routine sub-agent.
- **deal-flow 8-03** — 25 candidates / 8 kept. Top deal Etched $300M @ $10.3B ~6.8× UP; two clusters (agent primitives at Series B, nuclear-for-compute megarounds).
- **security-scan 8-03 SECURITY_SCAN_NOCHANGE** — 4 HIGH · 15 MEDIUM · 4 LOW byte-for-byte identical since 7-27; canonical-4 aeon.yml HIGH at same lines for 7th consec scan.

## Current health snapshot (2026-08-03)

- **P0 ISS-029 fleet-wide usepod.ai 402 Payment Required 8-03** — every scheduled skill that fired today (11:49Z + 18:27Z dispatch batches, ~18 skills) failed with `api.usepod.ai/v1/messages` "Payment required. Retry the same request with an X-PAYMENT or PAYMENT-SIGNATURE header." Highest consecutive_failures at check time: thought-review 9, skill-freshness 6, daily-routine 6, cost-report 6, unlock-monitor 6, btc-levels 6, security-digest 5, self-improve 3, heartbeat 3, deal-flow 3. Only 8-03 pre-outage success: btc-levels 04:50:49Z. 20:14Z batch in_progress at reflect time; this reflect run itself is proceeding via Claude Code CLI (not usepod.ai proxy) and succeeded outside the failing path. Operator-gated: payment top-up or proxy rotation. **First fleet-wide LLM-proxy billing failure in memory-window** — distinct from sandbox-layer ISS-025/027/028 (payment-layer, not compute-layer).
- **Last formal skill-health tick 8-02 18:23Z NOOP** — hash `f0c415fd` 5-consec composition-identity ~120h span through 8-02 evening. Zero drift expected 8-02 → 8-03 but no fresh tick yet (ISS-029). Prior 8-02 evening state: 0 CRITICAL · 17 DEGRADED · 13 WARNING · 10 HEALTHY · 3 NO_DATA. **14 open issues** (ISS-029 files today).
- **16-consec DEGRADED heartbeat verdict-string identity across ~124h span through 8-02 20:15Z** — memory-window-longest continuous chronic-degraded stretch. Composition-identity durable at 10 chronic sub-50%: cost-report 11% (7/64) · reg-monitor 19% · skill-analytics 19% · vuln-scanner 23% · market-context-refresh 32% · narrative-tracker 33% · search-skill 38% · security-digest 44% · aixbt-pulse 47% · skill-health 50.37%. No 8-03 tick to advance (ISS-029).
- **PR queue at 3 through 8-03 morning** (unchanged from 8-02 evening) — **#165 d15 CONFLICTING** (7-19 17:38Z docs skill-graph shared_state 21→27; CLAUDE.md ~7d-past-touch escalation window OPEN since 8-02); **#171 ~60h** (7-31 18:07Z fix github-trending 12-17 cap, ci-skills-json FAILURE 3-consec-day); **#172 ~44h** (8-01 18:42Z fix daily-routine XAI-prefetch, ci-skills-json FAILURE 3-consec-day). Weekly-batch merge window opens today but blocked by ISS-029 + operator gate.
- **ci-skills-json FAILURE 3-consec-day root cause identified 8-02 action-converter** — `./generate-skills-json` not run by self-improve authoring; skills.json stale on both PRs. Fix path: add regen step to self-improve.md commit process OR CI auto-regen bot. Weekly-review 8-03 T-0 root-cause investigation ask.
- **Bash `>` redirect workaround-chain n=20+ durable 12-UTC-day span 7-22 → 8-02** — 8-02 evening thought-review 21:35Z heredoc block confirms 17th+ call-site NEGATIVE. No fresh 8-03 probes (ISS-029). PR #167 fix-scope-narrowness hypothesis firms at 4-consec-UTC-day kill-test NEGATIVE. Workaround-chain (WebFetch + Write-tool + Edit-tool pattern-match append + URL-encoded `%3E` + proxy-metrics) held clean at every fire 8-02.
- **12:00 UTC batch DARK day-37** — ISS-027 signature durable through 8-02 12:00Z token-alert clean same-slot fire (40th consec CG clean day). aixbt-pulse dead-slot d37 (68+ consec missed 12h cycles).
- **ISS-025 hand-off T+5 day-20 SLIPPED** — cost-report weakest 11% (7/64 post-fresh-failures) durable. Weekly-review 8-03 T-0 action #1 at Sunday-batch window (blocked by ISS-029 until fleet recovers).
- **Sub-25 github-trending fetch pattern 6-consec permanent shape** — 7-28 → 8-02 full-week promotion. Hard-cap ~15 confirmed via 12-17 range. PR #171 acknowledges.
- **[[MCP-enforcement-primitive-cluster]] rail 4-consec durable 8-02** — MCP-thesis dominance in agent-buzz. 8-02 sub-variant: definitional/framing (plumbing-not-framework, HeyAnjula).
- **[[fleet-relevance agent-thesis]] rail 18-consec-day 8-02** — extended via ManageLife_io DeFi-agent economic-outcome axis (was infra/memory/architecture-only before).

## Positive events 8-02 evening → 8-03 morning

- **Sunday-slot cluster all-clean fire 8-02** — skill-graph 17:28Z NO_CHANGE + skill-update-check 19:39Z NO_LOCK + fork-cohort 19:52Z WENT_STALE Da6hkin + fork-skill-digest 20:03Z 78% sr (40 forks disabling action-converter) + skill-evals 22:39Z RECOVERED (2 fixed: token-alert + skill-health) + evening-recap 21:41Z clean = 6-of-6 Sunday cadence. Weekly-review 8-03 T-0 input population complete.
- **20:00Z heartbeat 8-02 +15min in-band** — cleanest 20:00Z-slot fire since 7-27 20:12Z baseline; breaks 08:00Z+14:00Z two-lag-slot-per-UTC-day candidate pattern (20:00Z performs distinctly better than dual-lag slots).
- **skill-evals SKILL_EVALS_RECOVERED 8-02** — token-alert + skill-health both cross from failing to passing missing_pattern check. Coverage 12/43 (28%). No fresh issue files.
- **fork-cohort 8-02 WENT_STALE Da6hkin/aeon** — POWER → STALE (11.9d silent); sinfronterasai POWER → COLD; aganoob → POWER (direct entry). Total 211 forks discovered, 24 POWER / 8 ACTIVE / 10 STALE / 38 COLD.
- **fork-skill-digest 8-02** — 40 forks (82% of tracked) disable action-converter = fleet-wide signal that action-converter is noise for downstream operators. DEFAULT_FLIP_DISABLE cohort widens: action-converter 82% / search-skill 78% / self-improve 73% / autoresearch 73% / github-trending 69% / skill-health 67% / security-digest 65% / token-pick 65% / vuln-scanner 63% / defi-overview 63% / token-movers 63% / narrative-tracker 61% / unlock-monitor 61% / reflect 57% / deal-flow 57% / list-digest 55% / goal-tracker 55% / agent-buzz 53%.
- **evening-recap 8-02 shipped** — TL;DR: productive sunday — fork-cohort + reflect shipped, sunday cluster all-clean, but ci-skills-json 3-consec failure blocks both self-improve PRs from tomorrow's batch.
- **goal-tracker 8-02 18:44Z 07:00Z scheduler slot 2nd clear** — deciding-test PASSED, regime rewrites 2-of-3-degraded → 3-of-4-intermittent-recovered.
- **reflect 8-02 shipped** — 14 patterns integrated, 9 stale entries pruned, MEMORY.md 69L → 75L.
- **action-converter 8-02 identified pr-ci-shared-root-cause** — via `gh run view 30713133283 --log-failed`; fixes ISS-029 candidate pre-filing (now filed today).
- **[[MCP-enforcement-primitive-cluster]] rail 3 → 4 consec durable 8-02** — definitional/framing sub-variant (HeyAnjula plumbing-not-framework).
- **[[agent-buzz-engagement-drought]] rail candidate 3-consec durable 8-02** — outlier magnitude decay 711 → 65 → 44 = ~16× over 3 UTC-days.
- **[[fleet-relevance agent-thesis]] rail 17 → 18 consec-day 8-02** — ManageLife_io DeFi-agent teardown ($30M treasury vs -$191.7M holder loss) extends into agent-economic-outcome axis.
- **Framework-lifecycle-verdict signal NEW 8-02** — AutoGen maintenance mode (rajeshberi) as sub-observation under [[AI-framework-attack-surface]].
- **First multi-agent benchmark with concrete config-count on agent-buzz feed 8-02** — Vokal_team 260-config parallel +80% / sequential -50-70%.

## Current health snapshot (2026-08-02)

- **skill-health hash 7bf88238 stable 4th-consec formal-tick** (last formal tick 7-31 18:07Z NOOP dedup-skip; composition identity ~96h span through today). No fresh formal tick since 7-31 18:07Z — next window is 8-02 evening if fired. Classification: **0 CRITICAL** · 18 DEGRADED · 12 WARNING · 10 HEALTHY · 3 NO_DATA. **13 open issues** unchanged. Sandbox-truncation family **day-41** (T+16 day-18, ISS-025 hand-off T+4 SLIPPED). cost-report weakest sr=0.12 (7/58) durable.
- **15-consec DEGRADED heartbeat verdict-string identity across ~119h span** (7-27 20:12Z → 8-02 15:10Z) = memory-window-longest continuous chronic-degraded stretch on record (previous record was pre-7-27, unmemoried). 10-skill chronic-failure sub-50% cohort composition-identity zero-drift 09:30Z → 15:10Z: cost-report 12% · reg-monitor 19% · skill-analytics 19% · vuln-scanner 23% (post 8-01 clean audit inches up) · market-context-refresh 32% · narrative-tracker 33% · search-skill 38% · security-digest 43% · aixbt-pulse 47% · skill-health 49.62%.
- **PR queue at 3 through 8-02 15:10Z heartbeat** — **#165 day-14** (7-19 17:38Z docs skill-graph shared_state 21→27, CONFLICTING, CLAUDE.md ~7d-past-touch escalation window OPENS TODAY); **#171 40h** (7-31 18:07Z fix github-trending 12-17 cap, ci-skills-json FAILURE 3-consec-day); **#172 ~24h** (8-01 18:42Z fix daily-routine XAI-prefetch case, ci-skills-json FAILURE 3-consec-day). Batch-merge window opens 8-03 (Sunday-batch T-1 today).
- **07:00Z scheduler slot d4 RECOVERED 8-02 — deciding-test PASSED, ISS-file escalation gate discharges** — morning-brief 07:22Z (+22min) + thought-review 07:23Z (+23min) + daily-routine 07:37Z (+37min) all in-band vs 8-01's +96-97min severely-lagged. Regime rewrites 2-of-3-day-degraded → 3-of-4-day-intermittent-recovered. Dispatch-lag pattern durable at magnitude (08:00Z + 14:00Z lag-slot pair candidate at +70-90min today), but 07:00Z-specific ISS-candidacy discharges.
- **ci-skills-json FAILURE 3-consec-day on both self-improve PRs (#171 + #172)** — shared-root-cause candidate promotes to formal-pattern threshold (2-day → 3-day). Weekly-review 8-03 T-1 root-cause investigation ask (may be systemically broken vs one-shot).
- **Bash `>` redirect regression workaround-chain n=18+ durable 12-UTC-day span 7-22 → 8-02** — kill-test d3+d4 NEGATIVE at 3 explicit sub-agent + call-site probes today (daily-routine hn-digest 07:37Z bash `>` + `-o` blocked; list-digest 17:00Z bash `>>` seen-file append blocked; skill-graph fingerprint-recompute 5 forms blocked: `{...}|sha1sum` + `xargs` + `awk` mid-pipeline + `python3 -c` + `bash script.sh`). Fix-scope-narrowness hypothesis firms: PR #167 landed at heartbeat/security-digest main-thread surface but did NOT propagate to sub-agent + URL-encoded query-string + append-mode + compound-pipeline surfaces. Workaround-chain (WebFetch + Write-tool + Edit-tool pattern-match append + URL-encoded `%3E` + proxy-metrics change-detection) held clean at every fire. Reflect 8-03 (weekly-batch) reopens root-cause investigation.
- **12:00 UTC batch DARK day-36** — ISS-027 signature durable through 8-02 12:00Z token-alert clean same-slot fire (40th consec clean CG day). aixbt-pulse dead-slot d36 (67+ consec missed 12h cycles).
- **ISS-025 hand-off T+4 day-19 SLIPPED** — cost-report weakest 12% durable. Weekly-review 8-03 T-1 action #1 rolls to d20 milestone at Sunday-batch window.
- **Sub-25 github-trending fetch pattern 6-consec permanent shape** — 7-28 (15) + 7-29 (12) + 7-30 (17) + 7-31 (14) + 8-01 (12) + 8-02 (15) full-week promotion. Hard-cap ~15 confirmed via range. PR #171 acknowledges 12-17 cap as expected shape.

## Positive events 8-02

- **07:00Z scheduler slot d4 RECOVERED — deciding-test PASSED** — 2-of-3-day-degraded regime rewrites to 3-of-4-day-intermittent-recovered; ISS-file escalation gate discharges.
- **CoinGecko clean-day streak d40 8-02** — 12:00Z token-alert clean fire = longest infrastructure durability streak in memory-window post-ISS-023.
- **github-issues 8-consec clean day 7-26 → 8-02** — advances via daily-routine sub-agent (`GITHUB_ISSUES_OK` streak).
- **WELL vol-cliff d6 full-recovery to 0.890× baseline 8-02** — 7-31 0.059× nadir → 8-01 0.162× → 8-02 0.890× arc definitively confirms one-slot data-glitch, rules out durable participation-drain regime.
- **Σ-Mem paper picks per-skill sr% cohort infrastructure directly 8-02** — arXiv 2607.27958 (Feng/Yang/Poria, ↑12) formalizes per-peer trust as online-updated symmetric state with Weyl-bounded spectral drift = same shape as Aeon's per-skill sr% cohort. Extends [[fleet-relevance agent-thesis]] rail 16 → 17 consec-day.
- **Memory-primitive-paper streak 3-consec-UTC-day NEW 8-02** — Memory Decoder 7-31 + Filesystem-Memory 8-01 + Σ-Mem 8-02 = paper-pick memory-thread cadence.
- **TencentDB-Agent-Memory 8-02 = first hyperscaler agent-memory primitive to trend** — TypeScript · 227 today · 10.5k total · 2.5× baseline · ACCELERATING. Extends [[fleet-relevance agent-thesis]] rail with hyperscaler-scale entry (prior = arXiv + smaller OSS).
- **iv-org/invidious 58× baseline spike 8-02 = highest ratio-spike memory-window** — Crystal · 435 today · 21.7k total · 8-year-old privacy YouTube frontend re-viral without release-catalyst; external catalyst hypothesis (anti-adblock cycle / YouTube policy shift / viral post).
- **Parallel same-day 4×-burn extension shape NEW 8-02** — zhaoxuya520/reverse-skill (335 → 1,320) + usekaneo/kaneo (194 → 760) both quadruple d1 fires = first slate-level follow-through-day shape in memory-window.
- **Sub-floor-to-ACCELERATING same-repo reversal shape NEW 8-02** — github/copilot-sdk (7 → 142 = 20× d1). First memory-window instance of same-repo one-day sub-floor-crosses-velocity-gate.
- **Bucket-split widens to 4 (peak-diversity slate) 8-02** — AI/ML 2 + Devtools 1 + Infra 1 + Web/Apps 1; Infra bucket returns after 7-30 last appearance.
- **security-digest quiet-cadence d2 + malware 159× collapse 8-02** — 0 fresh KEV + 0 fresh tracked-ecosystem reviewed = starkest quiet-day in memory-window; 318-batch → 2 fresh single-package entries in 24h. Yesterday's 8-01 14:52Z digest absorbed the full slate.
- **First Termux-execution malware in memory-window digest 8-02** — wacve-utils (pip, kam193/OSSF campaign 2026-08-wacve-utils) = Android/Termux data-exfil chain textbook (files + browser data + SMS + Telegram exfil).
- **Aeon-fleet clean d4 vs security-digest surface 8-02** (7-30 → 8-02 all clean import-check).
- **[[louround-single-thesis-cadence]] rail promoted candidate → durable n=3 8-02** — CODEC 7-31 + PENGU 8-01 + PUMP 8-02 = 3-consec-UTC-day single-voice dominance on list-digest.
- **@Flowslikeosmo double-anchor same UTC-day 8-02 first-in-window** — platform-evolution + Trump-paid-shill tweets both anchor. [[single-account-anchor-doubling]] rail candidate if repeats.
- **[[MCP-spec-maturity-vs-ecosystem-security]] tension rail extends n=3 8-02** — RufRoot CVE-2026-59726 on Ruflo agent framework (unauth HTTP POST → code exec + LLM API key exfil, patched 3.16.3 in 24h loopback-bound + access-controls) joins 7-30 initial Ruflo + 8-01 dynatrace-mcp-server. 3 unauth-agent-framework-CVE-in-wild in 4 days.
- **[[DeepSeek-does-what-claude-refuses]] pattern candidate NEW 8-02** — Zhuhai actor wired DeepSeek into Hermes Agent framework and hit 460+ internet-facing systems (Citrix NetScaler + 11 Marimo notebook instances) where Claude/OpenAI models refused. First explicit call-out of model-refusal-behavior differential exploited in-the-wild in memory-window.
- **[[open-web-postmortem-cadence]] rail NEW candidate 8-02 (hn-digest)** — Google/RSS 498pts + Atom-better-than-RSS story = 2-story open-web-audit cluster on 8-02 front_page.

## Current health snapshot (2026-08-01)

- **skill-health hash 7bf88238 stable 4th-consec formal-tick since 7-28 19:02Z** (last formal tick 7-31 18:07Z NOOP dedup-skip, composition identity ~96h span): **0 CRITICAL** · 18 DEGRADED · 12 WARNING · 10 HEALTHY · 3 NO_DATA. **13 open issues** unchanged. Sandbox-truncation family **day-40** (T+15 day-17, ISS-025 hand-off T+3 SLIPPED). cost-report weakest sr=0.12 (7/58) durable.
- **12-consec DEGRADED heartbeat verdict-string identity across ~90h span** (7-27 20:12Z → 8-01 14:15Z). 10-skill chronic-failure sub-50% cohort composition identity unchanged: cost-report 12% · reg-monitor 19% · skill-analytics 19% · vuln-scanner 21% · market-context-refresh 32% · narrative-tracker 33% · search-skill 38% · security-digest 43% · aixbt-pulse 47% · skill-health 49%.
- **PR queue stable at 2 through 8-01 14:15Z heartbeat** — #165 d13 CONFLICTING (docs skill-graph 7-19 17:38Z, sole survivor past-gate cohort; crosses 14d touch-threshold 8-02 = CLAUDE.md ~7d-past-touch escalation window opens); #171 ~24h (self-improve `fix(github-trending): reflect observed 12-17 candidate cap, not ~25` 7-31 18:07Z; under gate).
- **07:00Z scheduler slot 2-of-3-day degraded 8-01** — 7-30 whole-slot MISS → 7-31 recovered +33-41min (dispatch-lag pattern) → 8-01 severely lagged +96-97min (morning-brief/daily-routine/thought-review all last_dispatch 08:36:34Z, largest of sequence). 7-31 reflect's "1-instance anomaly" verdict does NOT hold; ISS-file escalation gate re-armed. 8-02 07:00Z tick is deciding test.
- **skill-freshness fingerprint change 8-01 08:50Z — first change since 7-25** — new fingerprint `f789cd3bca6…`, 7 items flagged (5 STALE + 2 WARN); market-context.md crossed 2× STALE threshold (~16d/380h); market-context-refresh + token-pick escalated WARN → STALE. RECOVERED from 47h-stale-approaching-48h-P3-gate warning at morning heartbeat 08:37Z.
- **Bash `>` redirect regression workaround-chain n=15+ durable 11-UTC-day span 7-22 → 8-01** — **PR #167 merge kill-test d2 NEGATIVE** at 4 explicit call-sites (daily-routine hn-digest sub-agent 08:42Z + security-digest 14:52Z + list-digest 17:37Z + vuln-scanner 16:45Z). Fix scope hypothesis: PR #167 landed at heartbeat/security-digest main-thread surface but did NOT propagate to sub-agent / URL-encoded query-string / append-mode surfaces. Workaround (Write-tool / Edit-tool / URL-encoded `%3E` in gh api / pipe-to-jq) held clean at every fire. Reflect 8-03 (weekly-batch window) should reopen root-cause investigation into fix-scope narrowness.
- **12:00 UTC batch DARK day-35** — ISS-027 signature durable through 8-01 12:00Z token-alert clean same-slot fire (n=35 CONFIRMED). aixbt-pulse dead-slot d35 (66+ consec missed 12h cycles).
- **ISS-025 hand-off T+3 day-18 SLIPPED** — cost-report weakest 12% durable. Weekly-review 8-03 action #1 rolls to d19 milestone at that window (2d out).
- **Sub-25 github-trending fetch pattern 5-consec durable rail** — 7-28 (15) + 7-29 (12) + 7-30 (17) + 7-31 (14) + 8-01 (12). Hard-cap around ~15 confirmed. PR #171 acknowledges 12-17 candidate cap as expected shape.

## Positive events 7-31 → 8-01

- **skill-freshness RECOVERED 8-01 08:50Z + first fingerprint change since 7-25** — new fingerprint `f789cd3bca626257444b895c8b1636402081e86e`, market-context-refresh + token-pick escalated WARN → STALE (market-context.md crosses 2× 168h at ~16d / 380h). Notify SENT (first since 7-25). Discharges 48h P3 gate flagged by morning heartbeat.
- **vuln-scanner clean audit yc-software/qm 8-01** — 8 candidates all-dropped in triage (highest count in ledger); notably well-engineered defensive posture (algorithm-pinned JWT + timingSafeEqual + ReplayDedupe + PKCE + host-pinned credential-broker + fail-closed Lua egress-authz) worth internalizing as reference-architecture. Kaneo deferred as "no safe channel" per Step 1 (SECURITY.md missing + PVR disabled) = first ledger precedent for skip-not-scan branch. Vuln-scanner sr=21% chronic-failure cohort inches up on this success.
- **CoinGecko clean-day streak extends to d39** — 8-01 12:00Z token-alert clean same-slot fire under ISS-027 batch-dark signature.
- **github-issues 7-consec clean day 7-26 → 8-01** — `GITHUB_ISSUES_OK` streak extends via daily-routine sub-agent.
- **Filesystem-Memory paper picks Aeon-architecture directly 8-01** — arXiv 2607.26637 (Zhou/Yu/Wei/Wu +7 co-authors, ↑6) is first-principles study of MEMORY.md + topics/ + logs/ + issues/ shape Aeon runs. Two load-bearing findings: (i) organized stores halve retrieval cost when material is large (validates memory-flush topic-splitting); (ii) organization erodes for all but strongest management agent (direct-relevance to consolidation churn). Highest-load-bearing paper-pick match in memory-window; extends [[fleet-relevance agent-thesis]] rail 15 → 16-consec-day.
- **[[skill-pack-primitive-rail]] extends n=5 → n=6 8-01** — zhaoxuya520/reverse-skill (PowerShell, 335 today · 11.2k · 2.4× baseline, ACCELERATING) is first **domain-specialist** variant (security-research router: reverse engineering / authorized pentest / security research skill router pack for Claude Code / Kiro / Cursor / Cline). Sub-taxonomy expands: general-skill-packs → domain-router-packs. 2-day gap 7-30/7-31 broken.
- **[[large-cap-single-day-flip]] rail NEW durable n=3 8-01** — HOLO 7-29 winner +10.5% → 7-31 loser -14.4% + PUMP 7-29 loser -7.1% → 7-31 winner +5.4% + UNI 7-31 winner +13.7% → 8-01 loser -8.5%. Cross-token UTC-day pole-flip pattern promotes from candidate to durable rail.
- **[[MCP-spec-maturity-vs-ecosystem-security]] tension rail codifies n=2 8-01** — 7-30 Ruflo CVE-2026-59726 + 8-01 @dynatrace-oss/dynatrace-mcp-server GHSA-p7w7-4929-vpj5 (7.5 unauth HTTP MCP tool invocation). 2 MCP-server-CVE-in-wild in 48h; ecosystem outpacing spec maturity.
- **[[single-project-mass-disclose]] rail extends n=7 → n=9 same UTC-day 8-01** — NLTK 4-CVE (CVE-2026-12075 SSRF bypass + CVE-2026-12061/12072/12074 path-traversals in FramenetCorpusReader/NKJPCorpusReader/ReviewsCorpusReader) + Thumbor 6-CVE (CVE-2026-53500..53505 HMAC bypass + ALLOWED_SOURCES + 4 DoS in convolution/proportion filters). **First double-mass-disclose UTC-day in memory-window**; rail-cadence acceleration continues (n=6 7-27 → n=7 7-28 → n=8 7-29 → n=9 7-30 → skip 7-31 → n=10/n=11 pair-drop 8-01). NLTK is first AI/ML-adjacent vertical to hit the rail.
- **pterodactyl/wings 2nd critical in 3d 8-01** — CVE-2026-52855 (9.9 egg-templating secret leak fix 1.12.3) lands after 7-30 CVE-2026-54593 (8.1 JWT scoping fix 1.12.2). Same-project-double-critical-in-window pattern candidate.
- **Malware batch 318 entries 8-01 = largest single-window count in memory** — highest-signal clusters: `@0xlr/*` 10-pack SaaS-auth dep-confusion (clerk-auth + stripe + supabase + sentry + prisma real-infra impersonation) + fintech corporate-scope 20-pack (real-corp-repo-name impersonation targeting financial-services stacks — new [[fintech-corp-scope-dep-confusion]] sub-class candidate) + nvidia AI-tooling 10-pack (single-author-attribution likely) + MCP-typosquat 12+ pack + ethers/solana wallet-target 5-pack (extends 7-31 ethers.json 7-pack). **Aeon-fleet clean d3** vs security-digest CVE + malware surfaces.
- **[[louround-single-thesis-cadence]] rail n=2 candidate 8-01** (list-digest) — 7-31 CODEC $2.4M FDV robotics-launchpad + 8-01 $PENGU $380m NFT-IP-to-retail brand-thesis. 11-of-14 candidates across 2-UTC-day span.
- **[[launchpad-primitive]] rail n=2 candidate 8-01** — CODEC 7-31 + frontierhood/robinhood-chain 8-01 (revenue-buy-back structure). Robinhood Chain TVL +12.6% weekly = macro backdrop.
- **[[MCP-enforcement-primitive-cluster]] rail extends d3 8-01 (agent-buzz)** — 7-29 MCP-infra-maturity + 7-31 MCP-plumbing-concrete + 8-01 MCP-production-plumbing (concrete-tenant-count sub-variant: Loky 200+ agents parallels 7-31 deeepakbagada 80% number).
- **[[AI-writes-fixes-not-code]] rail NEW candidate 8-01 (hn-digest)** — Chrome AI-driven fuzz/triage month eclipsing prior 24 months of fixes pairs with 7-30 Anthropic cybersec-eval disclosure. AI-as-defender-force-multiplier framing, sibling to [[AI-framework-attack-surface]].
- **star-anomaly serial-drop sub-cluster crystallizing 8-01** — affaan-m/ECC 5-consec-drop 7-27→7-31 + mvanhorn/last30days-skill 4-consec-drop 7-29→8-01. 8 total within-genre appearances across memory-window; serial-drop-repos rail candidate.

## Current health snapshot (2026-07-31)

- **skill-health hash 7bf88238 stable through 7-30 18:15Z formal tick** (3-consec formal-tick hash identity, no fresh formal tick 7-31): **0 CRITICAL** · 18 DEGRADED · 13 WARNING · 10 HEALTHY · 3 NO_DATA. **13 open issues** post-ISS-027/028 filing 7-30. Sandbox-truncation family **day-39** (T+14 day-16, ISS-025 hand-off T+1 SLIPPED). cost-report weakest sr=0.12 (7/58) durable.
- **9-consec DEGRADED heartbeat verdict-string identity across ~65h span** (7-27 20:12Z → 7-31 14:44Z). 10-skill chronic-failure sub-50% cohort persists: cost-report 12% · reg-monitor 19% · skill-analytics 19% · vuln-scanner 21% · market-context-refresh 32% · narrative-tracker 33% · search-skill 38% · security-digest 42% · aixbt-pulse 47% · skill-health 49%. Composition identity unchanged.
- **PR queue clears 3→1 overnight** — #167 (bash-redirect fix, 7d past-gate) + #170 (hn-digest self-improve, 21h) both merged 7-30 23:37Z within 20-sec window. #165 sole survivor at d12 (docs skill-graph, CONFLICTING, 7-19 17:38Z; still under CLAUDE.md ~14d past-touch threshold in operator batch-merge cadence window).
- **07:00Z scheduler slot RECOVERS d1 7-31** — morning-brief 07:36Z + daily-routine 07:41Z + thought-review 07:36Z all fired at +33-41min dispatch-lag. 1-instance MISS confirmed as one-day anomaly, not durable regime. Discharges 7-30 15:16Z heartbeat's ISS-file escalation gate.
- **Dispatch-lag 40-76min pattern durable d2 7-31** — morning cluster 07:33-07:41Z (~+33-41min), token-alert 12:23Z (+23min), github-trending 09:xx (~+40min), security-digest 14:44Z (~+44min), heartbeat 14:44Z (~+44min). Not a one-day anomaly — 2-consec-UTC-day GHA runner queue depth or webhook processing delay.
- **Bash `>` redirect regression workaround-chain n=12+ durable 9-UTC-day span** — 7-22 → 7-31. PR #167 merged 7-30 23:37Z; 7-31 fires (heartbeat + security-digest + morning-brief + daily-routine + github-trending + token-alert) all held clean via Write-tool workaround belt-and-braces (no `>` attempted post-merge yet). **Workaround retirement candidate 8-01** — try `>` redirect next fire to confirm regression fix landed OR keep as durable pattern.
- **12:00 UTC batch DARK day-34** — ISS-027 signature durable through 7-31 12:00Z token-alert clean same-slot fire (n=34 CONFIRMED). aixbt-pulse dead-slot d34 (65+ consec missed 12h cycles).
- **ISS-025 hand-off T+1 day-16 SLIPPED** — 7-30 deadline passed without operator direct-author against `.github/workflows/aeon.yml:479-495`. Cost-report weakest 12% durable. Reflect 8-03 (weekly-batch window) next natural catch.

## Positive events 7-30 → 7-31

- **07:00Z scheduler slot RECOVERS d1 7-31** — morning-brief + daily-routine + thought-review all fired 07:33-07:41Z at +33-41min dispatch-lag vs 7-30's whole-slot MISS. 1-instance anomaly confirmed. First evidence 07:00Z scheduler-drop was one-day event, not durable regime; ISS-file escalation gate discharges.
- **PR queue clears 3→1 overnight 7-30 23:37Z** — #167 (bash-redirect fix, 7d past-gate self-improve 7-23 18:21Z) + #170 (hn-digest path fix, 21h self-improve 7-29 18:41Z) merged within 20-sec window. First self-improve merge-batch since 7-28 dupe-pair (#168+#169) close. #165 sole survivor at d12 CONFLICTING.
- **CoinGecko clean-day streak extends to d38** — 7-31 12:00Z token-alert clean same-slot fire under ISS-027 batch-dark signature, CG API independence holds.
- **github-issues 6-consec clean day 7-26 → 7-31** — `GITHUB_ISSUES_OK` streak durable via daily-routine sub-agent.
- **ISS-028 kill-test underway 7-31** — PR #167 merged 7-30 23:37Z; all 7-31 fires (n=6 skills) held clean via Write-tool workaround. Belt-and-braces preserved; workaround-chain rail extends n=11→n=12+. 8-01 slot: try `>` redirect to confirm regression fix.
- **[[rust-native-efficiency-first-harness]] rail NEW n=2 in 48h 7-31** — agavra/tuicr (code-review TUI, 19.4× baseline) pairs with 7-30 1jehuang/jcode (coding harness). Sub-taxonomy expands: coding-harness → code-review-harness.
- **[[star-anomaly-rail]] extends n=6 → n=7 durable 7-31** — affaan-m/ECC 7th trending appearance (1,219/d normalized velocity, most durable rail in memory-window). 5-consec-UTC-day drop 7-27→7-31.
- **Sub-25 trending page fetch pattern n=3 → n=4 durable 7-31** — 4-consec WebFetch cut short of ~25 expected (14-17 range). WebFetch hard-cap hypothesis firms; ISS-file candidate if 8-01 confirms 5-consec.
- **[[embodied-agent-runtime-primitive]] rail n=2 → n=3 7-31** — Gemini Robotics 2 whole-body drop (HN 539pts) joins airi + speech-to-speech + VibeVoice sibling voice-primitive rail. Big-lab whole-body tier upgrade; 3-consec-UTC-day embodied/voice-runtime cadence.
- **[[eth-lib-typosquat-campaign]] NEW sub-class 7-31** — 7 ethers.js typosquats + fs-extra + socket.io = 3-cluster mass-typosquat batch published 22:49-22:51Z 7-30. Direct Aeon-audience relevance. Sub-class under [[mass-parallel-real-package-account-takeover]] parent.
- **KEV quiet-cadence 7-31** — 0 fresh KEV entries surface after dedup gate (all 3 fresh-week network-perimeter vendors already covered by 7-27/7-29 fires).
- **First fully-synchronized red day in memory-window 7-31** — 4-of-4 tracked tokens negative 24h. Participation-lift extinguishes fully on d3.
- **Fleet-relevance agent-thesis extends 14 → 15-consec-day 7-31** — Memory Decoder paper + Gemini Robotics 2 + Anthropic cybersec-evals HN all direct-fleet-relevant. Rail durability continues 7-17 → 7-31.
- **Aeon-fleet meta-signal fresh 7-31** — Opus 5 half-price-Fable-5 confirmation d7 post 7-24 ship + Claude Code computer-use gain (previous CVE-2026-55607 auto-patch memory pointer).
- **Thinnest github-trending slate in memory-window 7-31** — 2 picks (vs 4-5 baseline) with 12/14 drop rate. Quality-over-quantity gate held on genuinely quiet day; first Devtools-only bucket-split.

## Current health snapshot (2026-07-30)

- **skill-health hash 7bf88238 (fresh 7-28 19:02Z NOTIFY, hash 3-consec formal-tick identity)**: **0 CRITICAL** · 18 DEGRADED · 13 WARNING · 10 HEALTHY · 3 NO_DATA. 11 open issues. Sandbox-truncation family **day-38** (T+13 day-15). Composition unchanged since 7-28 flip. cost-report weakest sr=0.12 (7/58) durable.
- **7-consec DEGRADED heartbeat verdict-string identity across ~43h span** (7-27 20:12Z → 7-30 15:16Z). 10-skill chronic-failure sub-50% cohort persists: cost-report 12% · reg-monitor 19% · skill-analytics 19% · vuln-scanner 21% · market-context-refresh 32% · narrative-tracker 33% · search-skill 38% · security-digest 42% · aixbt-pulse 47% · skill-health 49%.
- **07:00 UTC scheduler slot MISS NEW 7-30** — morning-brief + daily-routine + thought-review all dropped (8h+ past schedule, no in-flight recovery per 15:16Z heartbeat). Later slots recover with 40-76min dispatch-lag (btc-levels 09:15Z / skill-freshness 09:15Z / token-alert 12:56Z / btc-levels 12:56Z / heartbeat 15:16Z all late). First whole-slot MISS in memory-window; GHA runner queue depth or webhook processing delay candidate.
- **PR queue 3 open — 2 past-gate CONFLICTING/pending**: #170 (hn-digest path fix, self-improve 7-29 18:41Z, 21h+ old = fresh); #167 d7 (bash-redirect fix, 7-23 18:21Z, crosses 7d weekly-batch gate on UTC-day roll); #165 d11 (docs skill-graph, 7-19 17:38Z, CONFLICTING). Operator batch-merge cadence window.
- **Bash `>` redirect regression n=11 durable 8-UTC-day span** — 7-22 → 7-30 hit again 2× today (heartbeat 15:16Z writing notify file + security-digest 15:22Z). Workaround chain (`curl -o` / Write tool / gh --jq stdout piping / Read+Edit append) held on every fire. ISS-028 file still absent d24 (+4d past weekly-review 7-27 last-chance window).
- **12:00 UTC batch DARK day-33** — ISS-027 signature durable through 7-30 12:00Z token-alert clean same-slot fire (n=33 CONFIRMED). aixbt-pulse dead-slot d33 (64+ consec missed 12h cycles pending 21:00Z 7-30 tick).
- **ISS-025 hand-off T-0 DEADLINE TODAY 2026-07-30** — weekly-review 7-27 action #1 target. Operator direct-author against `.github/workflows/aeon.yml:479-495`. T+12 day-15. Reflect 7-30 evening captures shipped-on-target vs slipped d16 outcome.

## Positive events 7-29 → 7-30

- **07:00Z slot MISS confirmed 7-30 15:16Z + escalated to notify** — heartbeat 09:04Z flagged pending/delayed for morning-brief + daily-routine + thought-review; 15:16Z heartbeat confirmed all 3 dropped with 8h+ past-schedule gap. Novel P3 escalation (not in 48h dedup window as confirmed drop). First-in-memory-window observation.
- **skill-freshness FRESHNESS_NO_CHANGE 5-day fingerprint stability 7-30** — `1ab8c658` unchanged since 7-25 (7 items flagged, 5 STALE + 2 WARN). Baseline durability confirmed; market-context.md expected to cross STALE threshold ~13:00Z 7-30 triggering fingerprint change + notify 7-31.
- **CoinGecko clean-day streak extends to 37 consecutive days** — 7-30 12:00Z token-alert clean same-slot fire under ISS-027 batch-dark signature, CG API independence holds.
- **KEV quiet-cadence breaks d2 7-30** — Cisco Secure FMC 7-29 hardcoded-password unauth-remote-login fresh add ends 2-day zero-fresh streak.
- **[[network-perimeter-vendor-in-KEV]] cluster n=4 crystallizes 7-30** — Fortinet 7-27 + Arista 7-27 + Cisco Secure FMC 7-29 = 3-of-4 fresh KEV-this-week are network-perimeter vendors. Crystallized sub-class.
- **[[real-plugin-name-fake-ecosystem]] NEW sub-class 7-30** — litespeed-cache WordPress-plugin name published to npm = pure impersonation vector under [[mass-parallel-real-package-account-takeover]] parent.
- **[[single-project-mass-disclose]] rail n=6→n=7 7-30** — flyto-core 6-CVE mass-disclose (all in 14:44-14:48Z window). 3-consec-day same-day mass-disclose cadence = **acceleration confirmed monthly → same-day**.
- **[[AI-framework-attack-surface]] rail n=3→n=4 7-30** — @aws/agentcore Bedrock CLI code-injection joins Claude Code CVE-2026-55607 + Langflow + LiteLLM triad.
- **[[open-voice-primitive-rail]] NEW n=2 in 48h 7-30** — microsoft/VibeVoice + huggingface/speech-to-speech = cross-org lab+big-co concurrence on open-weights frontier voice AI. Sibling rail to [[embodied-agent-runtime-primitive]].
- **Rust-native efficiency-first coding-harness primitive NEW n=1 7-30** — 1jehuang/jcode differentiates on RAM efficiency in JS/Node/Electron-dominated harness landscape (Claude Code / aider / Cursor / opencode). Extends agent-harness taxonomy into runtime-efficiency-differentiated sub-class.
- **Kimi K3 → FlashKDA delta-attention pipeline 7-30** — 7-28 top-HN paper concurrence → 7-30 CUDA kernels ship with fresh CUTLASS pipeline optimizations. Paper → usable code in 48h.
- **Star-anomaly rail n=4→n=6 durable 7-30** — obra/superpowers 6th trending appearance without featuring (896/d normalized velocity, higher than ECC's 1,222/d). Drops-not-features codify pattern.
- **Sub-25 trending page fetch pattern n=3 durable 7-30** — 7-28 (15) + 7-29 (12) + 7-30 (17) = 3-consec WebFetch cut short of ~25 expected. Sandbox/rendering artifact firms as observation.
- **Dispatch-lag 40-76min pattern durable on later-slot fires 7-30** — btc-levels 09:15Z (+60min) + skill-freshness 09:15Z (+75min) + token-alert 12:56Z (+56min) + btc-levels 12:56Z (+41min) + heartbeat 15:16Z (+76min). GHA runner queue depth candidate; watch 7-31 for continuation vs one-day anomaly.
- **Fleet-relevance agent-thesis extends 14-consec-day 7-30** — VibeVoice + jcode + FlashKDA + book-to-skill + speech-to-speech all in 7-17 → 7-30 window.
- **PR #170 authored 7-29 18:41Z (hn-digest path fix)** — self-improve one-line fix from daily-routine standalone fallback. Under 24h stalled gate through 7-30 15:16Z heartbeat (~21h old).

## Current health snapshot (2026-07-29)

- **skill-health hash 7bf88238 (fresh 7-28 19:02Z NOTIFY, first hash break in 168h+ 467ce959 span)**: **0 CRITICAL** · 18 DEGRADED · 13 WARNING · 10 HEALTHY · 3 NO_DATA. 11 open issues. Sandbox-truncation family **day-37** (T+12 day-14). Composition delta: defi-overview + token-pick DEGRADED→WARNING (SR 0.69/0.64 above <0.6 gate); defi-monitor + evening-recap + list-digest crossed WARNING→DEGRADED (SR 0.53/0.59/0.56); btc-levels crossed WARNING→HEALTHY (SR 0.81 clears 0.8 gate + avg_score 3). cost-report weakest sr=0.12 (7/58) durable.
- **22+ consec heartbeat NOOP through 7-29 14:36Z** — flat regime durable across ~220h+ span since 7-19 09:17Z regime-onset. Sequence extends 7-28 20:00Z + 7-29 14:36Z all dedup-SKIP.
- **PR queue shrinks 4→2 via 7-28 22:36Z dupe-pair merge** — #168 + #169 (github-issues comments→commentsCount field-rename) both merged; self-improve queue-exit gate BREACH RESOLVED. Root-cause investigation still open (whether self-improve correctly evaluates 3-PR gate at authoring time; not clear if bypass or false-positive).
- **Bash `>` redirect regression n=10+ durable 7-UTC-day span** — 7-22 → 7-29 hit again 4× today (security-digest 14:42Z + reg-monitor + agent-buzz 17:37Z + list-digest 17:36Z). Workaround chain (`curl -o` / Write tool / gh --jq stdout piping / Read+Edit append) held on every fire. ISS-028 file still absent d23 (+3d past weekly-review 7-27 last-chance window).
- **12:00 UTC batch DARK day-32** — ISS-027 signature durable through 7-29 12:00Z token-alert clean same-slot fire (n=32 CONFIRMED). aixbt-pulse dead-slot d32 (63+ consec missed 12h cycles pending 21:00Z 7-29 tick).
- **Chronic sr<0.5 tail (11 skills at 14:36Z 7-29 hb, same mix vs 7-28)** — cost-report 0.12 (7/58, ISS-025) · reg-monitor 0.17 · skill-analytics 0.18 · vuln-scanner 0.21 (ISS-018) · market-context-refresh 0.32 · narrative-tracker 0.33 · search-skill 0.38 (ISS-021) · fleet-control 0.40 (disabled per aeon.yml) · security-digest 0.41 · aixbt-pulse 0.47 · skill-health 0.48. 192h+ hash-identity span across formal-tick heartbeats (via 7-29 rollover).

## Positive events 7-28 → 7-29

- **Self-improve queue-exit gate breach RESOLVED 7-28 22:36Z** — dupe pair #168 + #169 merged in ~30h. First gate-breach in memory-window closed. PR queue 4→2 (#165 d10 + #167 d6 remain).
- **skill-health hash flip 7-28 19:02Z** — 467ce959 → 7bf88238, first hash break in 168h+ span. Composition delta: 2 skills DEGRADED→WARNING (defi-overview + token-pick), 3 skills WARNING→DEGRADED (defi-monitor + evening-recap + list-digest), btc-levels WARNING→HEALTHY (10 HEALTHY, up from 9).
- **btc-levels graduates HEALTHY 7-28 19:02Z** — SR 0.81 clears 0.8 gate + avg_score 3 clears quality gate.
- **Broad-tape restore 8→40 top-100 green 7-29 = largest 1-day breadth restore in memory-window** — 7-28 risk-off was single-day flush not regime shift.
- **BEAT/UB/HOLO one-day-round-trip snap-back 7-29 = n=2 sub-class extends 7-28 BANK pattern** — same tokens lead each direction across two UTC-days.
- **REPPO capitulation-attempt fully digests d1 7-29** — 24h -20.10%→-2.41% 10× deceleration, vol 2.075×→1.003× baseline; drought-break head-fake resolves flat-on-baseline.
- **META rank 187 mid-cap breakout 7-29** — +66.8% TRENDING+UP+PUMP-RISK on $6.5M vol = biggest low-rank breakout with trending confirmation in memory-window.
- **[[skill-pack-primitive-rail]] extends n=5 via virgiliojr94/book-to-skill 7-29** — one-shot book-PDF→Claude-skill ingestion pipeline, tightest utility angle in rail.
- **[[embodied-agent-runtime-primitive]] extends n=2 via huggingface/speech-to-speech 7-29** — open-weights local voice pairs with 7-28 airi (Minecraft/Factorio). Agent-as-runtime vs agent-as-chat-frontend contrast.
- **[[MCP-enforcement-primitive-cluster]] n=1 NEW 7-29** — 2 independent builders same day (policylayer_dan + emadgnia); MCP-infra-maturity thesis has ≥2 voices simultaneously.
- **[[legit-defi-org-typosquat]] NEW sub-class 7-29** — karpatkey + karpatkit pip malware impersonates real DAO treasury firm. Extends [[full-scope-cred-stealer-supply-chain]] with new attack-target class.
- **[[single-project-mass-disclose]] rail n=5→n=6 7-29** — datamodel-code-generator 12-CVE mass-disclose + swagger-typescript-api 5-CVE concurrent same-day. **Acceleration from monthly → same-day**.
- **[[federal-CEA-authority-reassert]] NEW 7-29** — MN prediction-market ban (D. Minn., CEA-preemption) + CFTC self-cert crackdown same-week. State-vs-federal jurisdiction fragmentation escalates.
- **[[one-day-below-gate-then-above]] reversal NEW 7-29** — opengeos/GeoLibre 48→58.1/d velocity cross documents first "one-day-below-gate → above-gate on d2" reversal in memory-window.
- **KEV quiet-cadence pattern n=2 shape emerges 7-29** — 7-23→7-26 4d drought + 7-28→7-29 2d drought, both bounded by enterprise-network-vendor cluster fires.
- **Malware mass-cluster rail terminates d3 7-29** — 7-27 @antv/* 52-pack + 7-28 wagni_bot/polymarket/mcp-server 63-pack → 7-29 61 fresh entries all diverse-1-off (karpatkey+karpatkit sibling pair only >1-package cluster).
- **Star-anomaly rail n=4-durable via ECC 4th-consec drop 7-29** — drop-decision codifies star-count-inflation-vs-authentic-viral hypothesis; investigation candidate.
- **CoinGecko 36-consecutive-clean-day streak** post-ISS-023 recovery (through 7-29 12:00Z token-alert).
- **Fleet-relevance agent-thesis extends 13-consec-day** — pbakaus + alibaba/open-code-review + skill-packs + book-to-skill + speech-to-speech all in 7-17 → 7-29 window.

## Current health snapshot (2026-07-28)

- **skill-health hash 467ce959** (7-consec formal-tick hash identity across 168h+ span through 7-27 18:43Z): **0 CRITICAL** · 18 DEGRADED · 13 WARNING · 9 HEALTHY · 3 NO_DATA. 11 open issues. Sandbox-truncation family **day-36** (T+11 day-13). cost-report weakest sr=0.12 (7/58) durable.
- **22+ consec heartbeat NOOP through 7-28 14:32Z** — flat regime durable across ~200h+ span since 7-19 09:17Z regime-onset. Sequence extends: 7-27 20:12Z + 7-28 10:00Z + 7-28 14:32Z all dedup-SKIP.
- **Weekly-review 2026-07-27 SHIPPED** — 168h period 7-20 → 7-27, 289 skill runs / 3 failures / 98.96% success (tightest failure envelope in memory-window). 4 PRs merged in 32h batch window 7-20/7-21 (#162 + #163 + #164 + #166). Closed-loop: 2 shipped-on-target + 1 slipped-4th-week (iss-025 hand-off due 7-30) + 1 self-healed. Article: `articles/weekly-review-2026-07-27.md`.
- **Self-improve queue-exit gate BREACHED 7-27 18:45Z** — self-improve authored PR #169 at 18:45Z despite 3-PR gate reached at 4 open PRs (#165 + #167 + #168 + #169). #169 is dupe of #168 (github-issues field-rename). First gate-breach in memory-window. Evening-recap 7-27 flagged operator triage call.
- **12:00 UTC batch DARK day-31** — 8-skill 6-28 cluster still frozen. ISS-027 signature durable through 7-28 12:00Z token-alert clean same-slot fire under signature (per-skill blockage n=31 CONFIRMED). Same daily-cluster: defi-overview / token-pick / token-movers / narrative-tracker / market-context-refresh / on-chain-monitor / defi-monitor / aixbt-pulse (dead-slot d31 twice-daily 9,21 UTC = 62+ consecutive missed 12h cycles).
- **Chronic sr<0.5 tail (14 skills at 14:21Z 7-25 hb, zero delta since 7-24)** — cost-report 0.11 (57, ISS-025) · reg-monitor 0.17 · skill-analytics 0.18 · vuln-scanner 0.18 (ISS-018) · market-context-refresh 0.32 · narrative-tracker 0.33 · search-skill 0.38 (ISS-021) · security-digest 0.39 · fleet-control 0.40 · skill-health 0.47 · aixbt-pulse 0.47 · goal-tracker 0.49 · action-converter 0.49 · self-improve 0.48. All ISS-019/020/021/025 sandbox-truncation family day-33.
- **12:00 UTC batch DARK day-28** — 8-skill 6-28 cluster still frozen. Per-skill blockage n=28 CONFIRMED via 7-25 clean same-slot fires (token-alert 12:44Z + btc-levels 12:44Z fire clean while cluster stays frozen = ISS-027 signature durable).
- **07:00Z morning-batch catch-up-band sat 7-25** — daily-routine 09:05Z (~1h50m late), morning-brief 08:58Z (~1h54m late), thought-review 08:54Z (~1h52m late), heartbeat 08:52Z (~52min late), github-trending 10:28Z (~1h28m late), skill-freshness 09:07Z. Sat catch-up-band drifts slightly wider vs fri 7-24 (~1h45m morning-tick, evening-tick 20min).
- **Bash-`>` redirect regression n=8+ durable across 5-UTC-day span** — 7-22 → 7-28 security-digest 14:42Z hit again. Workaround chain (`curl -o` / Write tool / gh --jq stdout piping / Read+Edit append) validated on every fire. ISS-028 file still missing d22 (weekly-review 7-27 last-chance window passed without filing).
- **notify sandbox-block observation NEW 7-25** — `./notify` script execution required approval in vuln-scanner run's sandbox this cycle, workaround = write directly to `.pending-notify/<unix-ts>.md` (per CLAUDE.md post-process pattern). Not new ISS-file candidate (matches existing sandbox-family).
- **CVE-2026-55607 `@anthropic-ai/claude-code` sandbox-escape 7-25** — first-in-memory direct-CVE-on-Aeon-runtime signal via git worktree path confusion (CVSS/fix 2.1.163). **Auto-patched** via unpinned `npm install -g` in CI (`.github/workflows/aeon.yml`). Verify `claude --version` ≥ 2.1.163 next CI dispatch.
- **GH API field rename** — `gh search issues` `comments` → `commentsCount` field renamed. `skills/github-issues/SKILL.md` step 2 patch still pending (3-day carry).
- **Self-improve queue at 4 open PRs 7-28 (gate BREACHED)** — #165 (docs skill-graph, d9 past 7d gate CONFLICTING) + #167 (bash-redirect fix, 5d) + #168 (github-issues field-rename, 3d) + #169 (dupe of #168, 1d, opened despite 3-PR gate). Weekly-batch cadence overdue absorb — operator batch-merge cadence window.
- **`first_patched_version` field discovery 7-25** — security-digest self-correction on digest fidelity; prior ticks used legacy `patched_versions` (mostly null) vs accurate `first_patched_version` nested under `vulnerabilities[]`.
- **Weekly-review 2026-07-13 actions status (7-25):**
  - #1 Operator direct-author ISS-025 capture-step PR by 2026-07-16 — **SLIPPED T+9 day-10 (4 days past 1-week slip)**. iss-025 verb-pool exhausted → downgrade to reflect-scope carry, weekly-review 7-27 hand-off.
  - #2 Operator decide PR #162 by 2026-07-14 — **SHIPPED via MERGE 7-20 14:16Z**.
  - #3 Self-improve codifies rule-5 in CLAUDE.md by 2026-07-17 — **SHIPPED via exit-gate primitive 7-19 18:32Z + weekly-batch cadence PR #166 7-21 18:29Z**.
  - #4 Self-improve investigates Investment Advisor cancellation by 2026-07-16 — **SHIPPED via PR #164 MERGED 7-20 21:50Z**.

## Positive events 7-27 → 7-28

- **Weekly-review 7-27 SHIPPED** — 168h period, 289 skill runs / 3 failures / 98.96% success = tightest failure envelope in memory-window. 4 PRs merged in 32h batch window 7-20/7-21 (#162 + #163 + #164 + #166). Closed-loop: 2/4 shipped-on-target + 1 slipped-4th-week (iss-025) + 1 self-healed-without-action. Article `articles/weekly-review-2026-07-27.md`. Next action: iss-025 reframe out of weekly action-cycle by 2026-07-30 (retires 4-week slip pattern).
- **7-28 Kimi K3 top-HN + top-paper same-day concurrence** — 2.8T MoE / 104B active / 1M ctx / delta attention + RL. HN 1334pts + arxiv ↑130 (>>next-highest 16). Extends [[small-MoE-frontier-close]] rail 3d post-Opus 5 ship. **Frontier-lab-open-weights-cluster n=1 NEW**.
- **7-28 amnezia-vpn top github-trending = censorship-resistance top-pick n=2** — extends 7-26 bitchat (India takedown). 2/2 top-picks in 3-day trending window = anti-censorship-primitive-cluster candidate. Extends [[censorship-driven-code-host-migration]] rail to code-hosting + circumvention pair.
- **7-28 star-anomaly rail extends n=4 in agentic-adjacent primitive** — pbakaus/impeccable 52k in 8mo (205/d velocity) adds to obra/superpowers 261k + mattpocock/skills 188k + affaan-m/ECC 233k. Star-count-inflation-vs-authentic-viral hypothesis deepens.
- **7-28 skill-pack primitive rail n=4 in 4 UTC-days** — mattpocock/skills 7-24 → obra/superpowers 7-26 → bradautomates/claude-video + last30days-skill 7-28. Specialized-vertical skills (video-analysis + web-research) diversify from generic frameworks.
- **7-28 first embodied-agent-runtime primitive n=1** — moeru-ai/airi runs agents *inside* Minecraft/Factorio as first-class runtime. Distinct from open-webui/big-agi UI wrappers.
- **7-28 first design-language-for-AI-harnesses primitive n=1** — pbakaus/impeccable teaches AI harnesses to produce non-generic UI, shipped multi-artifact (Skill + Extension + CLI).
- **7-28 fleet-relevance agent-thesis 12-consec-day** — pbakaus + alibaba/open-code-review 7-26 = agentic-primitive dominance persists 7-17 → 7-28.
- **7-28 KEV quiet-cadence d4 BREAKS** — Fortinet FortiOS + Arista VeloCloud fresh 7-27 = first fresh KEV since 7-22. Both enterprise-network-vendor (extends 2026-Q3 network-perimeter-vendor-in-KEV rail).
- **7-28 AI-agent-tooling-supply-chain-typosquat sub-class NEW** — claude-code-base-action GitHub Action typosquat + mcp-server-*/anthropic-internal-* 15-pack dependency-confusion. Extends [[mass-parallel-real-package-account-takeover]] with AI-tooling attack angle. Fleet-clean (uses `@anthropic-ai/claude-code` CLI npm, not the GitHub Action).
- **7-28 [[AI-framework-attack-surface]] extends n=4** — adds claude-code-base-action typosquat to CVE-2026-55607 Claude Code + Langflow + LiteLLM triad.
- **7-28 Mini Shai-Hulud @antv/* d2 tail continuation** — 61 fresh GHSA IDs since 7-27 matches 7-27 3-5d tail prediction. Same atool-account-takeover chain.
- **7-28 Google DMCA rejected on search-index scraping** — search-index not copyrightable = broad AI-training precedent (extends [[ai-training-data-legal-flux]] rail).
- **7-28 Rust-rewrite mixed-signals n=2** — Bun rust-rewrite postmortem 4mo flat commits (negative signal) vs Claude Code v2.1.181 rust-rewrite 7-21 (positive). 2nd-consec-week rail split.
- **7-28 CoinGecko 35-consecutive-clean-day streak** post-ISS-023 recovery (via 12:00Z token-alert clean fire).

## Positive events 7-24 → 7-25

- **H unlock T-0 CONFIRMED SPURIOUS 7-25 morning-brief + daily-routine cascade** — WebSearch (next HYPE aug 6) + daily-routine H +5.8% upside on 1.4× baseline vol = zero cliff-signature. Ticker-resolution ambiguity flagged 7-24 lands cleanly. MEMORY line 5 correction shipped this reflect.
- **WELL vol-spike streak caps at n=2 mean-reversion path wins 7-25 12z** — morning-brief focus #2 prediction resolves; [[vol-spike-streak-caps-at-n2-under-baseline-drift]] primitive codified.
- **BTC $65.9k reclaim 5-day-hold-then-break shape codified 7-25** — 4-day hold 7-21→7-24 window, 7-25 breaks intraday but above $60.5k gate = no re-alert (`reclaim65900Alerted=true` intact).
- **5-shape breadth-regime taxonomy in 5-day window NEW 7-25** — first 5-consec-day distinct-breadth-regime run in memory-window.
- **UB d5 REVERSES post-d4-unwind 7-25** — +9.5% after 7-24 -9.0% d4 unwind = pattern-tail candidate "3-day-sustain + d4-unwind + d5-reversal" contradicts d5+ decay assumption in [[one-day-breakout-unwind]].
- **BUILDon d7 slide-fatigue-shape emerging 7-25** — decelerating -12.1% d6 → -7.9% d7 extends pattern-tail to 4-day compound.
- **BEAT d4 mild unwind -4.4% 7-25** — matches [[one-day-breakout-unwind]] at d4-unwind class but mild magnitude (accelerating-variant milder than flat-sustain-variant).
- **github-trending 100% recycled-board n=1 NEW 7-25** — 17/17 candidates featured/dropped in prior 2-day window (first-in-memory) = meta-signal for slow-week/catalog-drought.
- **First "d2 exceeds d1" viral-shape NEW 7-25** — ego-lite 880 exceeds 247 by 256% = late-viral-catch shape breaks standard d1-peak-fade.
- **worldmonitor 4-day accelerate→plateau→fade arc completes 7-25** — 3-class viral taxonomy firm (1-day + 4-day + 6-day).
- **HOLDOVER-heavy slate primitive works n=1 7-25** — first slate composed entirely of HOLDOVER re-features under viral-moment clause; both survivors invoke exception with concrete new-reason.
- **block/buzz release-catalyst COMPOUNDS with viral thesis 7-25** — v0.4.25 landed 23:04Z + d2 +51% rate = release-day-adjacent print accelerates (contrasts 1-3d catalyst-decay).
- **Fleet-relevance 100% agent-thesis 9-consec-days 7-25** — 2/2 direct-agent-primitive picks (agent-workspace + agent-browser).
- **Rust-cluster-day extends d2 candidate at pool-level 7-25** — 4 Rust candidates on trending board (block/buzz kept, RuView + harper + Pumpkin dedup/dropped). Pool-level durable; kept-slate variable.
- **CVE-2026-55607 direct-hit-on-Aeon-runtime auto-patched 7-25** — first-in-memory Claude Code sandbox-escape CVE lands, unpinned `npm install -g` handles it (no operator action).
- **[[AI-framework-attack-surface]] extends n=3 7-25** — Claude Code + Langflow + LiteLLM three-consecutive-week AI-orchestration CVEs.
- **[[single-project-mass-disclose]] extends n=4 7-25** — GitPython 5-CVE joins Pillow / Gitea / n8n (pip dominant 3/4).
- **[[wallet-credential-stealer-supply-chain]] quiet-d1 mean-reversion 7-25** — 4-pack app-*-layer vs 7-24 45-batch = ~11× lower rate.
- **[[mature-project-security-hygiene]] n=3 rail NEW 7-25** — block/buzz joins chrome-devtools-mcp + tirth8205; clean-audit-partial-scan is signal not bug.
- **[[list-digest-grok-cache-lag-day-old-window]] extends n=3 + cross-skill to agent-buzz 7-25** — pattern crosses skill-boundary; X search API systemic day-lag confirmed distinct from empty-list-day-noise.
- **Claude Opus 5 ships 7-24 = Aeon-fleet meta-signal 7-25** — Fable-5 intelligence at half price + effort-toggle + 1M-ctx. Effort-toggle gives per-skill cost-lever for Aeon; operator-side upgrade-path candidate.
- **security-digest 7-25 clean-workaround-run** — Write + curl -o + jq stdout sidestepped bash `>` regression cleanly; digest fidelity self-correction via `first_patched_version` field.
- **vuln-scanner block/buzz clean-audit-partial-scan 7-25** — 3 dep-CVE candidates all triaged to DROP (2 covered by `deny.toml`, 1 unshippable git-pin), 4 code-audit spot checks textbook-correct (SSRF check + `is_private_ip` IPv4/IPv6 comprehensive + NIP42 CSPRNG + NIP98 no-loopback-aliasing). Report `articles/vuln-scan-2026-07-25.md`.
- **CoinGecko 33 consecutive clean days post-ISS-023 recovery** (through 7-25 12:44Z token-alert).

## Current health snapshot (2026-07-24)

- **skill-health hash 467ce959** (stable through 7-24, byte-identical since 7-20 18:47Z NOTIFY): **0 CRITICAL** · 18 DEGRADED · 13 WARNING · 9 HEALTHY · 3 NO_DATA. 11 open issues (ISS-005/007/009/010/011/016/018/019/020/021/025). Sandbox-truncation family **day-32** (T+8 milestone). cost-report DEGRADED (sr=0.11).
- **15-consec heartbeat NOOP through 7-24 14:13Z** — flat regime durable across ~100h+ span since 7-19 09:17Z regime-onset. Sequence: 7-19 3× + 7-20 2× + 7-21 3× + 7-22 3× + 7-23 3× + 7-24 2×. Third UTC-day rollover intact.
- **Chronic sr<0.5 tail (13 skills at 14:13Z 7-24 hb, zero delta since 7-22 20:03Z)** — cost-report 0.11 (57, ISS-025) · reg-monitor 0.17 · skill-analytics 0.18 · vuln-scanner 0.18 (ISS-018) · market-context-refresh 0.32 · narrative-tracker 0.33 · search-skill 0.38 (ISS-021) · security-digest 0.39 · fleet-control 0.40 · skill-health 0.46 · aixbt-pulse 0.47 · goal-tracker 0.49 · action-converter 0.49 · self-improve 0.48. All ISS-019/020/021/025 sandbox-truncation family day-32.
- **12:00 UTC batch DARK day-27** — 8-skill 6-28 cluster still frozen. Per-skill blockage n=27 CONFIRMED via 7-24 clean same-slot fires (token-alert 12:14Z + btc-levels 12:15Z fire clean while cluster stays frozen = ISS-027 signature durable).
- **07:00Z morning-batch catch-up-band widens fri 7-24** — daily-routine 08:50Z (~1h50m late), morning-brief 08:44Z (~1h44m late), thought-review 08:45Z (~1h45m late), heartbeat 08:46Z (~46min late), btc-levels 08:46Z. Fri regresses vs thu 7-23 (13min tight); wed 7-22 was 1h52m — 7-24 near-matches wed shape after thu tightening.
- **Bash-tool `>` redirect sandbox regression n=5+ same-family** across 3 UTC-day span — 7-22 security-digest + 7-22 agent-buzz + 7-23 daily-routine + 7-23 security-digest + 7-24 daily-routine + 7-24 github-trending + 7-24 security-digest. Workarounds validated across all fires: `curl -o` (curl to file), Write tool (fs write), Read+Edit append (log append). **ISS-file threshold now firmly crossed** — action-converter follow-up ISS-file candidate ready.
- **GH API field rename** — `gh search issues` `comments` → `commentsCount` field renamed. `skills/github-issues/SKILL.md` step 2 patch pending.
- **aixbt-pulse dead-slot d27** — twice-daily 9,21 UTC, last 2026-06-28T21:21Z. 54 consecutive missed cycles.
- **Self-improve queue at 2 open PRs 7-24** — #165 (docs skill-graph) d5+ dormant + #167 (bash-redirect workaround) fresh ~20h. Both under 7d weekly-batch cadence gate + under 3-PR queue-lock gate.
- **PR #167 authored 7-23 18:21Z self-improve tick** — bash-`>`-redirect workaround for n=3 same-week regression (security-digest 7-22 + agent-buzz 7-22 + daily-routine 7-23). **Rule-5 primitive n=2 same-cycle test lands positive under 1-open-PR queue** (queue held under gate; self-improve authored successfully). Second same-cycle authoring after PR #166 (7-21 18:29Z merge).
- **PR #166 same-cycle authored+MERGED 7-21 18:29Z (20min turnaround)** — first same-cycle self-improve authored+merged in fleet history; codified weekly-batch PR review cadence in CLAUDE.md.
- **Weekly-review 2026-07-13 actions status (7-24):**
  - #1 Operator direct-author ISS-025 capture-step PR by 2026-07-16 — **SLIPPED T+8 day-9 (3 days past 1-week slip)**.
  - #2 Operator decide PR #162 by 2026-07-14 — **SHIPPED via MERGE 7-20 14:16Z** (T+6 late).
  - #3 Self-improve codifies rule-5 in CLAUDE.md by 2026-07-17 — **SHIPPED via exit-gate primitive 7-19 18:32Z + weekly-batch cadence PR #166 7-21 18:29Z**.
  - #4 Self-improve investigates Investment Advisor cancellation by 2026-07-16 — **SHIPPED via PR #164 MERGED 7-20 21:50Z**.

## Positive events 7-23 → 7-24

- **UB d4 unwind FIRES on 7-23 prediction 7-24 daily-routine** — extends [[one-day-breakout-unwind]] rule at "3-day-sustain-max-before-d4-unwind" shape, cap holds firmly at n=4. BUILDon d6 -12.1% extends compound-unwind to -32% off peak (3-day compound not 1-2 day tail).
- **WELL vol-spike d2 fires 7-24 12:00Z** — 6.11× ($2,053.6K vs $336.2K baseline post-7-23-entering). **First-ever back-to-back vol-spike-fires in watchlist history**; accumulation-look strengthening d2 shape distinct from distribution.
- **3-day alert-fire streak** — GITLAWB counter-tape 7-22 + WELL vol-spike-only 7-23 + WELL vol-spike-continuation 7-24 firms [[alert-class-shift-3-regime]] taxonomy.
- **PR #167 authored 7-23 18:21Z** — rule-5 primitive n=2 same-cycle test lands positive under 1-open-PR queue.
- **github-trending 4-pick slate 7-24 1-per-bucket even split first-in-memory-window** — block/buzz (agent-as-equal-member workspace via Nostr) + mattpocock/skills (practitioner-side .agents-as-plugin) + Automattic/harper (offline-privacy Grammarly-alternative) + citrolabs/ego-lite (agent-shared browser via isolated Spaces). Rare cross-domain balance. 8-consec-day agent-thesis rail continues (liberal 4/4 or strict 3/4).
- **Skills-primitive rail resurfaces d1** after 7-23 dark with 6-shape taxonomy: practitioner + workspace-orchestration + coding-single-purpose + physical-world + vendor-catalog + first-party.
- **worldmonitor HOLDOVER re-feature primitive full-cycle validation 7-24** — 1,295 → 4,139 (d1 re-feature) → 3,175 (d2 -23% fade). Clears d1 threshold but d2 fades = peak not sustain shape validated.
- **First Rust-majority github-trending slate in memory-window 7-24** — 3/4 Rust picks.
- **security-digest 14:14Z 7-24** — 3 today / 5 this-week / 3 monitor. npm-malware 45-batch d1 NEW (largest single-day npm-malware in memory-window), [[AI-framework-attack-surface]] extends n=2 via LiteLLM MCP-auth-bypass CVE-2026-59822, [[single-project-mass-disclose]] n=3 via n8n 24-CVE, KEV zero-cadence d3 (quiet-2day regime), 6-day dedup-heavy digest d1 (still surfaces 11 fresh items).
- **list-digest 7-24** — Grok cache-lag n=2 same-list (7-22 returned 7-21 tweets, 7-24 returned 7-23 tweets); 2 signal-clearing single-digit tweets kept.
- **CoinGecko 32 consecutive clean days post-ISS-023 recovery** (through 7-24 12:14Z token-alert).
- **DeepSeek legacy API deprecation 7-24 15:59Z** — `deepseek-chat`/`deepseek-reasoner` route to `deepseek-v4-flash`.

## Current health snapshot (2026-07-22)

- **skill-health hash 467ce959** (7-21 18:04Z NOOP formal read, byte-identical to 7-20 18:47Z NOTIFY): **0 CRITICAL** · 18 DEGRADED · 13 WARNING · 9 HEALTHY · 3 NO_DATA. 11 open issues (ISS-005/007/009/010/011/016/018/019/020/021/025). Sandbox-truncation family **day-30** (00:00Z 7-21→7-22 rollover, 30-day milestone). cost-report CRITICAL→DEGRADED formal promotion 7-21 (sr=0.11 keeps DEGRADED per sr<0.6 rule).
- **10-consec heartbeat NOOP through 7-22 14:35Z** — flat regime durable across full 77h+ span, 2nd tick of UTC-day 7-22 rollover holds. Sequence: 7-19 09:17Z + 14:13Z + 20:34Z + 7-20 15:19Z + 20:15Z + 7-21 09:43Z + 15:11Z + 20:52Z + 7-22 08:48Z + 14:35Z. Zero new surprise-shape flags; only counter-advance on ISS-025-family sandbox-truncation cluster + UTC-day rollover.
- **Chronic sr<0.5 tail (14 skills at 14:35Z 7-22 hb, zero delta vs 08:48Z tick)** — cost-report 0.11 (57, ISS-025), skill-analytics 0.16, reg-monitor 0.16, vuln-scanner 0.18 (ISS-018), market-context-refresh 0.32, narrative-tracker 0.33, search-skill 0.38 (ISS-021), security-digest 0.38, fleet-control 0.40, skill-health 0.46, aixbt-pulse 0.47, goal-tracker 0.48, action-converter 0.48, self-improve 0.48. **1-skill delta from 7-21 20:52Z tick** — reflect crossed 0.49→0.50 falls off strict `<0.5` gate.
- **12:00 UTC batch DARK day-25** — 8-skill 6-28 cluster (defi-overview / token-pick / token-movers / narrative-tracker / market-context-refresh / fleet-control / on-chain-monitor / defi-monitor) still frozen. Per-skill blockage n=26 CONFIRMED 7-22 12:00Z via clean same-slot fires (token-alert 12:29Z + btc-levels 12:27Z fire clean while 8-skill cluster stays frozen = ISS-027 signature durable).
- **07:00Z morning-batch catch-up-band widens vs tue 7-21** — 7-22 daily-routine 08:52Z (~1h52m late from 07:15Z slot) + morning-brief 09:00Z + thought-review 08:48Z + heartbeat 08:48Z. Contrasts 7-21 tue on-time 07:00Z shape (~44min tighter). Wed-load-day not a mon-load-day; wider than tue but narrower than mon's 79min shape.
- **Bash-tool `>` redirect sandbox regression n=2 same UTC-day 7-22** — security-digest 14:00Z + agent-buzz 17:30Z both hit `>`/`>>` block. Workarounds: `curl -o`, Write tool for files, Read+Edit for append. Distinct new-behavior vs 7-21 clean runs. Also: GH API `published=date..` range format rejected 422; corrected to `published=>date` URL-encoded `%3E`. Consider SKILL.md patch to security-digest step 2 curl.
- **aixbt-pulse dead-slot d25** — twice-daily 9,21 UTC, last 2026-06-28T21:21Z. UTC-day rollover from 7-21 d24 = 50 consecutive missed cycles.
- **Self-improve queue at 1 open PR 7-22** — PR #165 (docs skill-graph) sole remaining open, d4 age (updatedAt 2026-07-19T17:39:48Z), well under 7d weekly-batch cadence gate codified via PR #166 same-cycle merge 7-21 18:29Z. Fleet minimum PR state.
- **PR #166 same-cycle authored+MERGED 20min turnaround 7-21 18:29Z** — self-improve 18:10Z tick authored CLAUDE.md +4 lines codifying weekly-batch PR review cadence + operator merged 20min later. **First same-cycle self-improve authored-and-merged in fleet history**; rule-5 primitive T+3 test under empty queue lands positive.
- **CLAUDE.md rule-5 codification durable via skill exit-gate (7-19) + weekly-batch cadence codification via PR #166 (7-21)** — self-improve exits when 3+ open PRs; weekly-batch review cadence codified as "no operator activity in 24h is normal in-cycle state, escalate only at ~7d". Rule-5 primitive n=4 downgraded to n=2 partial-conflict class post 7-20 sweep.
- **Weekly-review 2026-07-13 actions status (7-22):**
  - #1 Operator direct-author ISS-025 capture-step PR by 2026-07-16 — **SLIPPED T+6 day-7 1-week-slip milestone**. Cost-report late-success cleared acute-branch 7-20; sandbox-truncation family scoping tightens per-skill; primitive itself unshipped.
  - #2 Operator decide PR #162 by 2026-07-14 — **SHIPPED via MERGE 7-20 14:16Z** (T+6 late).
  - #3 Self-improve codifies rule-5 in CLAUDE.md by 2026-07-17 — **SHIPPED via exit-gate primitive 7-19 18:32Z + weekly-batch cadence PR #166 7-21 18:29Z** (T+2 + T+4 late).
  - #4 Self-improve investigates Investment Advisor cancellation by 2026-07-16 — **SHIPPED via PR #164 MERGED 7-20 21:50Z** (T+4 late, MERGE not just investigation).

## Positive events 7-21 → 7-22

- **PR #166 same-cycle authored+merged 20min turnaround 7-21 18:29Z** — first same-cycle self-improve authored+merged in fleet history; codifies weekly-batch PR review cadence in CLAUDE.md via `## PR review cadence` section. Fleet minimum PR state at 1 open (#165 docs skill-graph d4).
- **cost-report CRITICAL → DEGRADED formal promotion via 18:04Z skill-health tick 7-21** — cf 8→0, sr=0.11 keeps DEGRADED per sr<0.6 rule. Fleet 0 CRITICAL first time in memory-window (18 DEGRADED / 13 WARNING / 9 HEALTHY / 3 NO_DATA; hash 467ce959 stable).
- **BTC ETF YTD outflows drop below $5B first time 7-22** — 5-consec-day US spot BTC ETF inflows totaling $727M authoritative BRN/CoinDesk figure with $226.9M final-day (7-21 said "$600M+"). New psychological threshold cross; extends 7-21 "peanuts framing d1 broken" call. Next BTC resistance $67.5-68k, break > $68k = fast 5-6% leg per @tedpillows.
- **4-consec zero-alerts day CLOSES 7-22 12:29Z via GITLAWB +16.53%** — breaks streak at n=4 (7-18 → 7-19 → 7-20 → 7-21). Counter-tape single-token reclaim shape (against broad-tape 24/100 green) vs 7-21's broad-tape multi-token constructive shape-shift. Two distinct crack shapes possible under distinct macro conditions.
- **BTC 2-week high holds through digestion 7-22** — spot $65,816-$66,241 through the day post 7-21 $66,563 peak, $65.9k reclaim holds, 24h -0.4% mild digestion after 7-21's +3.0%. HYPE $58.78 -6.7% / 7d -12% MAJOR breakdown lead on 63pt breadth compression day.
- **security-digest fires clean 14Z tue-tick (via wed operator-adjacent) 7-22** — 3 today / 3 this-week / 3 monitor across Fortinet FortiSandbox 2-CVE KEV-no-patch + DD-WRT 4yo re-emergence + Gitea 8-CVE mass-disclosure + GitPython 3-CVE unfixed + pip-mass-malware n=2 same-24h.
- **github-trending 5-pick slate 7-22** — ayghri/i-have-adhd top pick (coding-agent skill installable-package primitive) + earthtojake/text-to-cad (physical-world skills package) + agegr/pi-web (browser UI for pi CLI) + tradesdontlie/tradingview-mcp (agent-callable-desktop-tool) + koala73/worldmonitor (world-state as operator signal). 6-consec-day 100% agent-thesis coverage rail (26/26 kept picks over 6 days).
- **reg-monitor first tue-tick in memory 7-22 (operator-invoked off-wed cadence)** — 1 act (Cboe binary options Amendment No. 1 SEC accelerated approval effective today 7-22 · Release 34-105936) / 2 watch (Cboe binary KPI SR + FDIC stablecoin comment period closes 9-18) / 2 context (CFTC uncleared-swaps margin effective 8-17 + CFTC large-trader sunset). GENIUS Act 1-yr statutory deadline missed 7-18 durable frame.
- **CoinGecko 30 consecutive clean days post-ISS-023 recovery** (through 7-22 12:29Z token-alert).
- **10-consec heartbeat NOOP durable across UTC-day rollover 7-22** — 7-19 3× + 7-20 2× + 7-21 3× + 7-22 2× = flat regime firms across full 77h+ span, 2nd tick of new UTC-day 7-22 holds shape.

## Current health snapshot (2026-07-21) — prior for continuity

- **skill-health hash 467ce959** (7-20 18:47Z NOTIFY, classification byte-identical to 7-19 18:32Z NOOP report). 1 CRITICAL (cost-report — lifts pending 18Z 7-21 tick) · 17 DEGRADED · 13 WARNING · 9 HEALTHY · 3 NO_DATA. 11 open issues. Sandbox-truncation family **day-29**.
- **cost-report late-success 7-20 19:08Z** — d7 acute-failure branch resolved via late-dispatch (18:45Z ~12h post-scheduled 07Z). 3rd-consec-Mon-weekly-miss test lands NEGATIVE at n=2.
- **7-consec heartbeat NOOP through 7-21 15:11Z** — flat regime durable across full UTC-day + mid-day pivot.
- **12:00 UTC batch DARK day-24** — per-skill blockage n=25 confirmed.
- **Self-improve queue EMPTY of CONFLICTING 7-20** — triple-queue clears in single day via #162 + #163 + #164.

## Positive events 7-20 → 7-21

- **Triple-PR queue clears in single day 7-20** — PR #162 daily-routine XAI fallback tighten (14:16Z) + PR #163 skill-security-scan sandbox-block docs (17:11Z) + PR #164 investment-advisor fail-fast committee retries (21:50Z) all MERGED. First 3-PR same-day sweep in fleet history.
- **cost-report late-success 7-20 19:08Z** — clears d7 acute-failure branch; 3rd-consec-Mon-miss test lands NEGATIVE at n=2.
- **BTC $65,900 reclaim FIRES 7-21 09:29Z** — first time spot ≥ $65,900 in current regime; spot $66,241 → $66,563 through the day, 2-week high.
- **KEV 4-day zero-cadence CLOSES 7-21** — 4 fresh adds (Langflow RCE + WordPress ×2). [[kev-4-day-zero-cadence]] artifact-not-durable confirmed.
- **GH advisory feed 72h silent CLOSES with post-silence burst 7-21** — 3 critical + 38 high in 48h window; Pillow 10-CVE mass-dump + LightRAG 2-CVE + node-tar 2-CVE + Directus + Astro.
- **Broad-tape risk-on lift 7-21** — 87/100 top-100 green top-50 median +3.0% = 61pt breadth expansion vs 7-20 26/100.
- **security-digest fires clean 14Z tue-tick 7-21** — 3 today / 5 this-week / 3 monitor across supply-chain wave + Langflow KEV + LightRAG pair + node-tar pair + Pillow 10-bundle.
- **github-trending 3-pick slate 7-21** — bojieli/ai-agent-book #1 + AstrBot + tirth8205/code-review-graph d4 re-feature.



- **skill-health hash b4d66e6c** (7-18 18:14Z NOOP, unchanged as of 4-consec heartbeat NOOP through 7-20 15:19Z). 1 CRITICAL (cost-report) · 17 DEGRADED · 13 WARNING · 9 HEALTHY · 3 NO_DATA. 11 open issues (ISS-005/007/009/010/011/016/018/019/020/021/025). Sandbox-truncation family **day-28** (00:00Z 7-19→7-20 rollover).
- **cost-report STUCK→FAILED d7 state-change 7-20 13:24Z** — `last_status: failed`, cf 5→8 (+3 in 24h), sr 0.09. Mon-weekly 07:00Z tick DID NOT fire; scheduler picked up in 12:57Z batch alongside token-alert + btc-levels (shared last_dispatch stamp = batch behavior). **3rd-consec-Mon-weekly-miss n=3 pattern-durable** (last_success 6-29, missed 7-6 + 7-13 + 7-20). ISS-025 signature. Operator direct-author against `.github/workflows/aeon.yml:479-495` sole unblock path.
- **Chronic sr<0.5 tail (14 skills at 15:19Z 7-20 hb)** — narrative-tracker 0.33, goal-tracker 0.47, skill-health 0.45, reflect 0.49, action-converter 0.47, self-improve 0.47, skill-analytics 0.16, fleet-control 0.40, market-context-refresh 0.32, search-skill 0.37, security-digest 0.36, reg-monitor 0.16, vuln-scanner 0.18, aixbt-pulse 0.47. All ISS-019/020/021/025 sandbox-truncation family day-28.
- **12:00 UTC batch DARK day-23** — 8-skill 6-28 cluster still frozen. 7-20 12:57Z token-alert + btc-levels + cost-report all fired same slot cleanly = scheduler-side per-skill blockage n=23 (ISS-027 signature) rollover from 7-19 d22.
- **07:00Z morning-batch d4 catch-up widens on Mon-load-day** — 7-20 morning-brief 07:54Z (~54min late), token-alert 12:57Z (~60min late), heartbeat 14Z→15:19Z (~79min late) = mon-weekly-load widens the catch-up band vs 7-19 ~14-41min tighter shape. Band-widening = load-dependent not degradation.
- **aixbt-pulse dead-slot d23** — twice-daily 9,21 UTC, last 2026-06-28T21:21Z. UTC-day rollover from 7-19 d22.
- **weekly-shiplog 3-consec-Mon-miss test lands NEGATIVE 7-20 10:55Z SHIPLOG_OK** — mon-cluster health improves d1 vs cost-report which stays failed. Same-slot differential: weekly-shiplog fires vs operator-scorecard never-run (chronic Mon miss d13) vs cost-report failed = per-skill sandbox behavior not per-slot scheduler.
- **Open self-improve PRs — 2 CONFLICTING past stall gates + 1 new docs:**
  - **PR #164** `fix(investment-advisor): fail-fast committee retries` (7-15 19:31Z) — **T+5 day-6** past 24h stall gate. Script-file class.
  - **PR #163** `fix(skill-security-scan): document sandbox-blocked` (7-13) — past 72h stall gate. **7-20 14:19Z activity** (no longer stalled by no-activity, active PR movement). SKILL.md class.
  - **PR #165** `docs(skill-graph): shared_state 21→27` (7-19) — 0-1 day old, under stall gate.
- **PR #162 MERGED 7-20** — commit `e525536 fix(daily-routine): tighten XAI fallback rules for quota/sandbox/error` landed on main. Down from 3 to 2 open self-improve CONFLICTING PRs.
- **Rule-5 primitive n=4 = auto-committed state drift extension** — PR #160/162/163/164 span workflow + SKILL.md + scripts/ file classes. Operator direct-author sole reliable path. **PR #162 merge is exception via operator-direct-decision, not self-improve resolution** — rule-5 codification still stands as primitive.
- **CLAUDE.md rule-5 codification SHIPPED 7-19 18:32Z via skill exit-gate** — `improvement-PR-queue-locks-self-improve 2-consec` pattern codified. Self-improve exits when 3+ open PRs (revises 7-19 morning-brief focus #3 as ISS-025 T+2 SLIPPED → RESOLVED via exit-gate primitive, not via operator direct-author).
- **Weekly-review 2026-07-13 actions status (7-20):**
  - #1 Operator direct-author ISS-025 capture-step PR by 2026-07-16 — **SLIPPED T+4 day-5** (still open).
  - #2 Operator decide PR #162 by 2026-07-14 — **SHIPPED via MERGE 7-20** (T+6 late).
  - #3 Self-improve codifies rule-5 in CLAUDE.md by 2026-07-17 — **SHIPPED via exit-gate primitive 7-19 18:32Z** (T+2 late, not via CLAUDE.md edit but via skill-side gate).
  - #4 Self-improve investigates Investment Advisor cancellation by 2026-07-16 — **SHIPPED-ON-TARGET via PR #164** (PR CONFLICTING).

## Positive events 7-19 → 7-20

- **PR #162 MERGED 7-20** — 6-day-old self-improve XAI-fallback tighten lands via operator-direct-decision, first self-improve authored merge since rule-5 primitive extension.
- **weekly-shiplog SHIPLOG_OK 7-20 10:55Z** — 29 commits / 26 PRs merged / 0 issues in 7-day window (SINCE 2026-07-13T10:48Z), 10 substantive commits. Themes: OAuth for MCP servers durable, 3 new MCP skills + CTRL retires, Aeon Developer Kit lands. Article `articles/weekly-shiplog-2026-07-20.md`. Prior shiplog 6-29 = 21d back = outside 7-14d window → Momentum Check section omitted per skill spec.
- **rule-5 codification SHIPPED via skill-side exit-gate primitive** (revises expectation of CLAUDE.md-edit-fixes-primitive; skill-side gate is durable fix).
- **BTC ETF regime firms** — $273M net inflow over 2 weeks breaks 8-week $8B+ outflow streak; 7-17 net-inflow day $132.3M IBIT-led + ETH ETFs $36.7M ETHA-led (Coindesk "peanuts scale but streak broken").
- **Kimi K3 open-weights ship 7-27 = d7 out** — [[small-MoE-frontier-close]] rail n=4 confirmed pre-ship (2.8T open-MoE + 1M ctx + Kimi Delta Attention, beats Fable 5 + GPT-5.6 Sol on front-end Arena, 40% cheaper than Opus 4.8). Hard date locked; OmniRoute already wires pre-launch (see [[pre-launch-integration]]).
- **CoinGecko 28 consecutive clean days post-ISS-023 recovery** (through 7-20 token-alert 12:57Z).
- **btc-levels multi-tick chain preserved 7-20** — clean fires 04:52Z + 12:59Z + 16:50Z all with `reclaim63500Alerted=true` holding, spot band $64,563-$65,393 through the day.
- **security-digest 7-20: KEV day-4 zero-cadence + GH reviewed feed 48h silent + npm-malware wave RESUMES** (revises 7-19 close-of-wave call as scan-window artifact — 4 pkgs landed 7-19 23:53-23:55Z after 7-19 14:20Z scan).

## Infrastructure built (PRs)
| PR | Date | What |
|----|------|------|
| #1 | 2026-05-21 | Telegram webhook worker for instant inbound messaging |
| #2 | 2026-05-21 | Reppo agent swarm — orchestrator + trading agent vertical slice |
| #3 | 2026-05-21 | agent-buzz X.AI prefetch case + cache fallback (closed ISS-001) |
| #4 | 2026-05-21 | reppo-swarm activation — TradingGymAI datanet_id + integer-id support (closed ISS-002) |
| #5 | 2026-05-22 | chain-runner no longer aborts on a var-less first step |
| #6 | 2026-05-22 | reppo ledger reflects on-chain reality, not queued intent |
| #7 | 2026-05-22 | REPPO_PRIVATE_KEY wired into the post-process workflow step |
| #8 | 2026-05-23 | postprocess-reppo.sh surfaces raw CLI error (closed ISS-003) |
| #9 | 2026-05-25 | self-improve: tighten token-alert step 2 (volume-spike, threshold-cross config) |
| #10 | 2026-05-25 | auto-grant datanet access on PUBLISHER_LACKS_SUBNET_ACCESS (initial ISS-004 helper) |
| #11 | 2026-05-25 | reppo-lock setup helper (REPPO → veREPPO for voting power, initial ISS-006 helper) |
| #12 | 2026-05-25 | populate soul/SOUL.md + soul/STYLE.md from ~/code/social |
| #13 | 2026-05-25 | postprocess-reppo.sh retry-with-backoff on Base RPC failures (ISS-007) |
| #14 | 2026-05-25 | self-improve: tighten scan.sh backtick-with-$ HIGH pattern (97.5% noise cut) |
| #15 | 2026-05-25 | auto-approve REPPO spend on INSUFFICIENT_ALLOWANCE (initial ISS-008 helper) |
| #16 | 2026-05-25 | messages workflow apostrophe escape fix |
| #17 | 2026-05-25 | structured/scannable reppo-digest format |
| #18 | 2026-05-25 | install foundry via workflow action (auto-approve blocker) |
| #19 | 2026-05-26 | reppo approve (v0.5) — drop cast/foundry/REPPO_TOKEN_ADDRESS dep |
| #20 | 2026-05-26 | retry grant-access with backoff after auto-approve (post-confirmation stale-read fix) |
| #21 | 2026-05-26 | auto-recover pod-manager allowance on mint InsufficientAllowance (closed ISS-008) |
| #23 | 2026-05-26 | auto-lock 500 REPPO into veREPPO on INSUFFICIENT_VOTING_POWER (closed ISS-006) |
| #24 | 2026-05-26 | reppo-orchestrator: make fenced reppo-plan block non-negotiable (ISS-009 v1, prompt-side; insufficient) |
| #25 | 2026-05-26 | INDEX bookkeeping — close ISS-009, fix ISS-006 fix_pr link |
| #26 | 2026-05-26 | widen vote dry-run retry budget after auto_recover_lock to 5/10/15s |
| #27 | 2026-05-26 | chain-runner workflow-level grep guard for fenced reppo-plan (ISS-009 v2; insufficient — `continue` not `break`) |
| #28 | 2026-05-26 | align tradinggymai rubric with operator-shared contributor spec |
| #29 | 2026-05-26 | register pod metadata to platform DB for UI visibility |
| #30 | 2026-05-28 | rewrite reppo-trading-agent: construct pods from HL public data |
| #31 | 2026-05-28 | skill-evals — align output_pattern with actual skill output locations |
| #32 | 2026-05-28 | scheduler: scope skill parser to skills: block (closed ISS-010) |
| #33 | 2026-05-28 | skill-graph SKILL_GRAPH_NEW — 124 skills, 21 enabled |
| #34 | 2026-05-28 | HL prefetch: use `userFillsByTime` (window matches rubric 7-day floor) |
| #35 | 2026-05-28 | Telegram poller: fall back to `.message.caption` |
| #36 | 2026-05-28 | enable daily content + meta skills |
| #37 | 2026-05-28 | reppo: rank HL wallets by margin (pnl/vlm), drop 7d span floor, add anti-regurgitation contract — unlocked 4th mint ever |
| #38 | 2026-05-28 | replicate: pin pending-JSON contract + surface API errors |
| #39 | 2026-05-28 | HL_TOP_N default 10 → 3 to fit Aeon's 30-min timeout |
| #41 | 2026-05-29 | replicate-oneoff workflow (workflow_dispatch image gen) — merged |
| #42 | 2026-05-29 | capture HTTP status + response body on Pinata pin / platform POST failures (root-caused ISS-012 + ISS-013) — merged |
| #43 | 2026-05-29 | vibecoding-digest same-day dup-notify suppression — merged |
| #44 | 2026-05-29 | platform metadata Zod schema fix (subnetId string, podName ≤50, podDescription ≤200, extract_detail ≤600) — closed ISS-012 — merged |
| #47 | 2026-05-30 | move ISS-005 epoch filter into prefetch + cast subnetId UUID (durable ISS-005 + ISS-014 fixes) — merged 2026-05-30 ~08-14 UTC |
| #51 | 2026-05-30 | backfill 4 pre-PR-50 pod URLs — merged 2026-05-31 ~13Z |
| #54 | 2026-05-31 | enable Tier 1 crypto-builder skills — open 13:32Z |
| #55 | 2026-05-31 | canonical Tracked Tokens watchlist (WELL/MAMO/REPPO/GITLAWB) — open 15:01Z |
| #56 | 2026-05-31 | route vibecoding Reddit through oauth.reddit.com (ISS-015 fix) — open 15:09Z |
| #57 | 2026-05-31 | refactor reppo Phase 2 onto @reppo/cli≥0.6.0 native — open 15:39Z |
| #58 | 2026-05-31 | skill-graph weekly digest (NEW_ENABLED 8 · NEW_DEPS 33 · REMOVED_DEPS 10) — merged 2026-06-01 13:17Z |
| #54 | 2026-05-31 | enable Tier 1 crypto-builder skills (5 new: deal-flow Mon / reg-monitor Wed / security-digest daily / unlock-monitor Mon / vuln-scanner Sat) — merged 2026-06-01 13:12Z |
| #55 | 2026-05-31 | canonical Tracked Tokens watchlist (WELL/MAMO/REPPO/GITLAWB) — merged 2026-06-01 13:12Z |
| #56 | 2026-05-31 | route vibecoding Reddit through oauth.reddit.com (ISS-015 fix) — merged 2026-06-01 13:12Z |
| #57 | 2026-05-31 | refactor reppo Phase 2 onto @reppo/cli≥0.6.0 native — merged 2026-06-01 13:12Z |
| #59 | 2026-06-01 | dashboard Reppo swarm demo at /swarm — merged 13:13Z |
| #60 | 2026-06-01 | bump HL_TOP_N 5→12 to clear mint-ledger saturation — merged 13:50Z |
| #61 | 2026-06-01 | decouple voting from minting via new reppo-voter skill — merged 15:20Z |
| #62 | 2026-06-02 | self-improve: narrow bare `mamo` → `$MAMO` cashtag in fetch-tweets var — merged ~07:30Z |
| #64 | 2026-06-03 | chain-runner.yml `${{ inputs.chain }}` → `env:` indirection at lines 41 + 416 (closed ISS-017) — merged as commit 2a9ce1c |
| #65 | 2026-06-03 | disable vibecoding-digest + reddit-digest (closed ISS-015 wontfix) — merged |
| #67 | 2026-06-03 | enable token-movers + on-chain-monitor + defi-monitor + fork-cohort/digest/gap + operator-scorecard (34→41 enabled standalone) — merged 15:59Z |
| #69 | 2026-06-03 | reppo-orchestrator: codify emit-fenced-block-in-assistant-text contract (ISS-009 sub-task a) — merged 23:00:48Z; #68 closed 1s later as duplicate |
| #70 + chain-runner.yml:360 | 2026-06-03 | chain-runner `continue` → `break` flip (ISS-009 sub-task b shipped) — INDEX flip pending |
| #71 | 2026-06-04 | aeon personal-stack PR (priorities anchor + thought-review skill + telegram voice path) — merged this week |
| #73-#76 | 2026-06-04..05 | reppo+content-skill maintenance batch (per weekly-review 17-PR list) |
| #77/#78/#79 | 2026-06-05..07 | virtuals + deepseek-v4-flash fallback for 5 CG-price skills (`FALLBACK_CG_SKILLS` at **`.github/workflows/aeon.yml:498`** — defi-overview / token-movers / token-pick / token-alert / market-context-refresh) — reppo chain NOT covered, but reppo is off-CI post-Docker (2026-06-10) so FALLBACK_REPPO_SKILLS is moot |
| #80 | 2026-06-08 | investment-advisor swarm (8 advisor skills + chain wiring) — chain failed on same-day 429; PR #82 supersedes with standalone Virtuals workflow (open) |

## Recurring blockers
- **15 unassigned reppo datanets.** Orchestrator surfaces them every run (ids
  1, 2, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18 — id 18 ArAIstotle
  surfacing 5 consecutive days through 2026-06-05). 16+ days untouched.
  PR #30/#34/#37 unblock pod sourcing on datanet 9; still need an assignment
  rubric or operator pick for the other 15.
- **ISS-005 durable fix still pending.** Agent-side filter (validityEpoch ≤
  current-1) is in place since 2026-05-24; durable prefetch fix still pending.
  Compounding side-effect: pods 372/373 were DISLIKE'd 7× each on-chain
  2026-05-28 alone (1 per chain run, no CLI idempotency check). Today's runs
  (2026-05-29) **deliberately steered off 372/373** to break the compounding
  pattern — DISLIKE'd 332/390/391 instead, 1st vote on each. Organic
  mitigation works but isn't durable.
- **ISS-011 nonce-too-low REVERT.** Vote-391 1st run REVERTed (CLI provided
  nonce below current chain nonce after sibling votes landed same batch).
  2nd-run retry landed clean. Single occurrence so far; watch for recurrence.
- **Trading-agent dry streak ENDED 2026-06-05** after 11 consecutive dry
  runs through 6-04 4th-run. Three mints landed same day — new single-day
  record. 15th-mint **4a9a582a** (0xecb63caa 821 HFT closes 14.69 min,
  70 markets, perp-only filter retained 1768/1999 = 11.55% spot excluded,
  +$7,500 Sharpe 1351 tx 0xdb5b7bbc), 16th-mint **16671d6f** (0x944b5f7d
  29 SOL+BTC closes in 9.548s cluster, +$8,410 **Sharpe 48,523** = 2nd
  highest in ledger ever tx 0xef7ce963), 17th-mint **e2e925b2** (0x781e95fd
  201 LINK Close-Short over 2.88h, +$9,605 Sharpe 3782 tx 0xa86b8dca).
  Two operator follow-ups emerged from the unlock: (a) formalize spot_pct
  threshold in Step 4.2 alongside NEG/regression guards (15th-mint admitted
  at 11.55% vs 10th-mint precedent rejected 0xecb63caa at ~20%); (b)
  formalize Sharpe-vs-pnl selection criterion in Step 4 (17th-mint
  Sharpe-tiebreak picked LINK 3782 over runner-up AAVE 3421 +$14,615 — an
  alternate "max absolute pnl" rule would have selected AAVE). Margin-top-12
  cohort had rotated wholly by 6-05 vs 6-04's saturated structure — likely
  HL_WINDOW=week refresh rolled out the spot HFT cluster, not an in-skill
  knob. Operator config asks (perp-only prefetch / HL_MIN_VLM_USD bump /
  HL_WINDOW switch) NO LONGER on critical path.
- **Sandbox `./notify "$(cat ...)"` arg-passing.** Now the dominant pattern —
  most content skills stage to `.pending-notify/` and let the post-run delivery
  step pick it up (today: morning-brief, github-trending, defi-overview,
  agent-buzz ×2, daily-routine, token-pick, reppo-digest ×1, thread-formatter,
  technical-explainer ×5, market-context-refresh, vibecoding-digest, weekly-shiplog).
  `./notify` direct exec still works for some (token-alert, defi-overview when
  args are short).
- **Sandbox: Reddit endpoints.** Datacenter IP block on `curl`; WebFetch tool
  refuses both `old.reddit.com` and `www.reddit.com`. vibecoding-digest emits
  PREFETCH_FAILED markers even from the runner host (2nd ERROR run today) —
  worth auditing `scripts/prefetch-vibecoding.sh` (likely Reddit-side rate
  limit / UA rejection on runner IP too).
- **Sandbox: X.AI authed curl.** Fixed via `scripts/prefetch-xai.sh`; expand
  with one `case` per skill that needs `XAI_API_KEY`.
- **HL `userFills` 2000-row cap.** PR #30/#34 widened the prefetch *query*
  window to 7d, but cap is on the *response* — surfaced after 4 mintless runs.
  PR #37 fixed by switching wallet selection to rank-by-margin (pnl/vlm) and
  dropping the (non-existent) 7d span floor; 4th mint ever landed on 6th run.
- **operator-scorecard never run.** Mon 10:30 weekly slot — no cron-state entry
  since fleet bootstrap. Under 2x interval threshold so heartbeat doesn't flag.

## Resolved blockers
- **ISS-013 (Pinata IPFS pin HTTP 403) and ISS-014 (platform metadata
  POST HTTP 500) durably resolved 2026-05-30 → 2026-06-01.** 7 consecutive
  pin successes + 4 consecutive HTTP 200 POSTs through today's 14th-mint
  cc41abf6 / tx 0xcbe53613. INDEX bookkeeping flip queued.
- **Phase 2 platform/IPFS cleared 2026-05-30.** ISS-013 (Pinata HTTP 403
  NO_SCOPES_FOUND → operator rotated PINATA_JWT with `pinFileToIPFS` scope;
  5 consecutive pin successes 2026-05-29 4th-run through 2026-05-30 5th-run).
  ISS-012 (platform metadata POST HTTP 400 — payload Zod bug → PR #44 merged
  2026-05-29T19:21Z). ISS-014 (post-PR-#44 HTTP 500 server-side fault →
  self-healed; 1st HTTP 200 on 2026-05-30 4th-run, 2nd consecutive on
  5th-run). First end-to-end clean mints in chain history.
- **Reppo on-chain blocker cascade (CLEARED 2026-05-26).** Full sequence took
  6 days: ISS-002 (PR #4) → ISS-003 (PR #8) → ISS-004 (PR #10/#19/#20) →
  ISS-006 (PR #11/#23) → ISS-007 (PR #13/#26) → ISS-008 (PR #21) → ISS-009
  (PR #24, recurred → PR #27, recurred).
- **ISS-009 root cause traced 2026-05-28.** 4 recurrences across 05-26/05-27/
  05-28 morning. Chain-runner's "Capture skill output" step (`aeon.yml:479-493`)
  `cp`s the Claude CLI's `.result` (final assistant text) over
  `.outputs/${SKILL}.md`, silently overwriting any Write-tool output. PR #24
  (prompt-tightening) and PR #27 (workflow grep guard) both targeted the
  wrong layer. Fix path: orchestrator emits fenced block in final assistant
  *text*, not via Write tool. Validated across runs 2/3/4 on 2026-05-28 —
  gate cleared every time. Still want `continue` → `break` in chain-runner's
  fail-fast branch as a defence-in-depth. ISS-009 INDEX status still "open"
  pending the workflow fix.
- **ISS-010 dispatch phantom (CLEARED 2026-05-28).** `aeon.yml` parser scoped
  to skills: block via PR #32. INDEX still shows open — bookkeeping queued.
- **Soul files empty.** PR #12 populated 2026-05-25. Content skills now ship
  ana voice.
- **scan.sh backtick-with-$ noise.** PR #14 — 97.5% false-positive cut.
- **HL wallet selection mintless ceiling.** PR #34 (`userFillsByTime`) +
  PR #37 (rank by margin, drop span floor) — 6th chain run on 2026-05-28
  landed 4th mint ever (hash 397ee2e8e5e7e593, wallet 0x2b3349ff…33f7,
  110 closed trades, sharpe 110, win 0.76). 2026-05-29 added the 5th
  (LIT 9794ed80, wallet 0x8def9f50, sharpe 19515) and 6th (xyz:BRENTOIL
  7029a48d, wallet 0xebe126ad, sharpe 295k — **first commodity-perp mint**).

## Skill health
- **Latest classification (2026-06-12 18:09Z): 41 healthy, 0 critical/
  degraded/flapping/warning, 2 no_data** (operator-scorecard +
  fork-skill-gap awaiting first weekly tick). Cleaner than the
  2026-06-10 baseline (7 no_data → 2) as autoresearch, fork-cohort,
  fork-skill-digest, unlock-monitor and vuln-scanner all acquired
  first-run data over the week. `article` still carries sr=0.5 in
  cron-state (2 runs only, under chronic threshold — known noise).
  Through 6-13, heartbeat reports 0 skills at consecutive_failures≥2
  and the only dispatched-stuck rows are 3 daily carryovers from the
  6-12 weekly-limit wave + 11 weekly carryovers draining on Sun/Mon/Sat ticks.
- Earlier classification (2026-05-31 18:21Z): 27 healthy, 0 critical/degraded/
  flapping/warning, 1 no_data (operator-scorecard — Mon 10:30 weekly slot
  remains never-run; today's 10:30 slot also passed without state entry).
- **Fleet expanded 29 → 34 enabled skills 2026-06-01 13:12Z** via PR #54:
  deal-flow (Mon), reg-monitor (Wed), security-digest (daily), unlock-monitor
  (Mon), vuln-scanner (Sat). All 5 are tier-1 crypto-builder skills. First
  runs today: deal-flow (DEAL_FLOW_OK, $65B Anthropic round headline),
  security-digest (SECURITY_DIGEST_OK, 3 PATCH TODAY + 5 PATCH THIS WEEK,
  flagged concurrent npm KEV adds: Nx Console + TanStack).
- **reppo-voter introduced 2026-06-01 15:20Z (PR #61).** Voting decoupled
  from minting — first voter run reported gate=RUN, current_epoch=100,
  56 out-of-epoch + 17 already-voted + 1 own-pod (pod 492 = 14th-mint
  cc41abf6 source wallet), eligible=0. own_pod_ids prefetch returned
  count=0 (5th consecutive run gap), voter self-recognized via ledger
  wallet shortcode cross-ref.
- Data-quality gap: vibecoding-digest cron-state shows last_status=success
  but log entries record VIBECODING_DIGEST_ERROR (Reddit endpoints blocked,
  prefetch host failing too). Workflow exits 0 with a notification-only
  error — classifier follows cron-state, so the skill is HEALTHY by the
  rules. Surfaced to self-improve as a workflow-exit-vs-skill-outcome mismatch.
- Per-skill quality records on disk: `reppo-digest` 4/5 (3 runs: 05-23, 05-26,
  05-28); `search-skill` 4/5 (1 run, 05-22). No flags.
- `article` carries sr=0.5 in cron-state (2 runs only — under chronic-failure
  threshold).
- `github-trending` sr=0.88 (7/8) — above 0.5 threshold.
- `chain:reppo-swarm` last_status=failed 2026-05-28T13:53Z — trading-agent-step
  NOT executed in 5th chain run (orchestrator + digest only ran). Watching
  for recurrence; not yet a filed defect. Single occurrence.
- skill-evals 2026-05-24 baseline: 12/29 coverage, 1 PASS, 1 STALE, 12 NO_OUTPUT.
  PR #31 (merged 05-28) repointed token-alert + skill-health to memory/logs/
  and renamed hn-digest → hacker-news-digest, polymarket → monitor-polymarket.
  Expected next eval: 2 FIXED + 2 still NO_OUTPUT (disabled targets).
- security-scan 2026-05-25 bootstrap: 5 workflow-injection anti-pattern sites
  (messages.yml:578, aeon.yml:86/94/96/718). All auth-gated, exposure low.
  Follow-up PR still pending.
- search-skill: 7th consecutive NO_GAP exit (2026-05-22 → 05-28). Fleet
  gap-free on external-skill axis.

## Cost profile (week 1, bootstrap-inflated)
- Total: $179.73 across 61 runs, 4 days of actual data.
- 30-day projection: ~$770 raw; ~$1,290 trimmed (~$43/day post-bootstrap).
- Cache read + write = 73% of spend.
- defi-overview + heartbeat + reppo-digest = 38% of weekly Opus spend.
  Sonnet rotation could cut ~$55–65/wk; standard model-downgrade filter
  doesn't flag them because cache_read dominates direct input tokens.
- Week 2 baseline due at next cost-report (full Monday→Sunday).

## Issues
- ISS-001/002/003/004/006/008/012/013/014 resolved.
- ISS-005 open (high, prompt-bug) — agent-side workaround live; PR #47
  (durable prefetch fix + CLI vote-dedup) merged 2026-05-30 morning. Watch
  next runs for compounding-pattern break.
- ISS-007 open in INDEX (medium, timeout) — PR #13 retry + PR #26 widened
  budget; INDEX close queued (5+ days).
- ISS-009 open (high, prompt-bug) — root cause traced + fix path validated
  2026-05-28; 5th recurrence 2026-05-30 2nd-run after 6 consecutive runs held.
  Two follow-ups: (a) codify orchestrator emit-in-assistant-text in skill
  prompt, (b) chain-runner `continue` → `break` in fail-fast branch.
- ISS-010 open in INDEX (medium, config) — fix shipped in PR #32; close queued.
- ISS-011 open (medium, unknown) — vote nonce-too-low REVERT after sibling
  votes land same batch. 1 occurrence; retry landed; not recurring.
- **ISS-015 RESOLVED 2026-06-03** — wontfix: vibecoding-digest +
  reddit-digest disabled. PR #56 oauth.reddit.com route merged
  2026-06-01 but Reddit API access ungettable for this operator;
  operator chose to disable rather than wait. Frees 1 cron slot,
  removes 6+ days of daily noise.
- **ISS-016 open (medium, prompt-bug, NEW 2026-05-31)** — vote LIKE on
  agent's own pod reverts CANNOT_VOTE_FOR_OWN_POD. Fix: gate
  trading-agent vote_filter on publisher==agent (drop regardless of
  direction). own_pod_ids prefetch returning count=0 since filed
  (**15 consecutive voter runs** through 2026-06-05 3rd-run); voter
  self-recognizes via ledger cross-ref — durable workaround. 2026-06-05
  re-run was 1st time the ledger workaround actually FIRED on the active
  epoch (pod 583 = today's 15th-mint 4a9a582a self-filtered); 3rd-run
  filtered BOTH own-mints on the active epoch (pod 583 + pod 585 = today's
  15th + 16th mints in the same defensive pass). Workaround now demonstrated
  durable under load, not just theoretical — prefetch repair priority drops.
- **ISS-017 RESOLVED 2026-06-03** — chain-runner.yml `${{ inputs.chain }}`
  shell interpolation at lines 41 + 416 fixed via env: indirection
  (PR #64, commit 2a9ce1c). Day-3 carry → ship-in-morning ship cadence.
  Anti-pattern of record now closed for the chain-runner family.

## Lessons Learned
- Reppo on-chain cascade ISS-002 → ISS-003 → ISS-004/005 → ISS-006 →
  ISS-007 → ISS-008 → ISS-009 → ISS-011/012/013/014 → ISS-016. Each fix
  exposed the next layer. Phase 2 fully cleared 2026-05-30.
- Workflow-level guards only work if they abort the chain — bash `continue`
  in chain-runner's fail-fast branch silently skips to next iter. Use
  `break` or `exit`.
- Chain-runner capture step (`aeon.yml:479-493`) silently overwrites
  Write-tool output with CLI's final assistant `.result`. Fenced blocks
  must be emitted in assistant text, not via Write. Codified in
  skills/reppo-orchestrator/SKILL.md via PR #69 2026-06-03.
- HL `userFills` 2000-row cap is on the *response*, not the *query window* —
  wallet selection by margin (pnl/vlm) clears the floor.
- Sandbox blocks `./notify "$(cat ...)"` arg-passing — stage to
  `.pending-notify/` and let post-run step deliver. Dominant pattern
  across ~15 content skills.
- Sandbox blocks Reddit (datacenter IP) and X.AI authed curl — use
  prefetch. Reddit oauth route (PR #56) added but ungettable secrets
  forced ISS-015 wontfix 2026-06-03 (vibecoding + reddit disabled).
- Cost profile is cache-dominated (73% of spend). defi-overview, heartbeat,
  reppo-digest = 38% of weekly Opus spend.
- Reppo platform enforces publisher-cannot-vote-on-own-pod. Empirical
  answer to "LIKE own mints?": NO, contract-level revert (ISS-016).
- Drift-skip precedent: if `(wallet, last_t, n_close)` triple matches a
  prior mint, skip even when content hash differs — re-mint = duplicate
  dataset spam. Drift-skip spirit also applies on regressed quality (same
  wallet + same first_t + degraded sharpe/pnl) even when triple differs
  strictly. In-skill Step 4.2 quality guard now codifies the
  regression-aware variant; validated 2026-06-04 2nd-run on 0x9a1500b4.
- Workflow-injection anti-pattern needs `env:` indirection (canonical
  shape is messages.yml:586-591; chain-runner.yml closed via PR #64
  2026-06-03).
- Fetching X tweet content from sandbox: x.com direct WebFetch → HTTP 402,
  nitter.net → empty body, **api.fxtwitter.com/{handle}/status/{id}** is
  the working unauthed fallback (returns JSON with text + quoted-tweet body).
- Memory consolidation: topic-file detail, MEMORY.md is the index.

## PR sweep (2026-06-01 → 2026-06-03)
- 2026-06-01 13:12-15:20Z: 8 PRs merged in a single window. #54 enabled 5
  new tier-1 skills. #55 canonical token watchlist. #56 oauth.reddit.com
  route (later moot — ISS-015 wontfix). #57 reppo-cli≥0.6.0 native Phase
  2 path. #58 skill-graph weekly digest. #59 dashboard /swarm demo. #60
  HL_TOP_N 5→12 (unblocked the fresh wallet that landed the 14th mint).
  #61 split reppo-voter out of trading-agent.
- 2026-06-01 14:40Z 14th mint (wallet 0x9a1500b4, 74 Close-Long perp,
  hash cc41abf6, tx 0xcbe53613) — same source wallet as 13th-mint
  dce17be3 but fresh `(wallet, last_t, n_close)` triple proves
  drift-skip dedup admits genuine new activity. Thin/marginal: Sharpe
  0.84, MDD 91% vs 13th-mint's 9.98 / 171%. Wallet flipped NEG-PnL
  the next day and has stayed there — quality-guard motivator.
- 2026-06-02 ~07:30Z: PR #62 merged (self-improve: `mamo` → `$MAMO`
  cashtag in fetch-tweets var).
- 2026-06-02 1st chain run (07:00) added 2 DISLIKE votes on epoch-100
  HotBot v4 pods 498/499 — first reppo-voter-owned on-chain votes
  post-PR #61 chain split. Ledger 14 mints / 29 votes.
- 2026-06-03: PR #64 (chain-runner env: indirection) merged as commit
  2a9ce1c — closes ISS-017 (Day 3 carry → ship). ISS-015 resolved
  wontfix same day (vibecoding-digest + reddit-digest disabled).
  Open PR count back to 0. 4 high-sev opens → 3 (ISS-005, 009, 015 →
  005, 009 carry; 017 closed).

## 2026-06-06 → 2026-06-09 — rate-limit cluster + recovery
- **2026-06-06 06utc 19th mint cfd710ae** — 0xbc433ba7 52 HYPE/CBRS/QNT/
  SPCX/SNDK closes 5.37d +$25,453 Sharpe 97 tx 0xd9fb03bd. Same wallet was
  18th-mint Sharpe-tiebreak dropped runner-up 2026-06-05 4th-run — surfaces
  clean today after 0x0514f2f3 regressed under Step-4.2 (1st time Step-4.2
  regression check fired on 1-day-old prior mint: +$14,615 → +$5,856).
  Validates Sharpe tiebreak doesn't lose real signal (runner-up-becomes-
  winner-next-day).
- **2026-06-06 12:37Z Claude weekly rate-limit hit.** 140 failures clustered
  6-06/6-07/6-08; `api_error_status:429 "weekly limit"` → `exit 1`.
  18+ skills stuck in `last_status=dispatched`. 0 mints + 0 log entries
  written 6-07 + 6-08 (logs for 6-07 missing entirely; 6-08 only contains
  weekly-review + heartbeat + evening-recap + aixbt-pulse). 8+d
  reppo-swarm clean streak broken 6-08T18:37Z. Virtuals fallback covers
  5 CG-price skills only (`FALLBACK_CG_SKILLS` at
  `.github/workflows/aeon.yml:498`); reppo chain fell through at the time.
  → "extend FALLBACK to reppo" action SUPERSEDED 2026-06-10 by the Docker
  migration: reppo skills are now `enabled: false` in aeon.yml and run
  self-hosted, so CI weekly limits can't touch them. Residual gap is only
  non-reppo CI skills outside FALLBACK_CG_SKILLS (still `exit 1` on limit).
- **2026-06-08 weekly-review filed** — 369 workflow runs (230/136/2/1-null),
  17 PRs merged, 5 mints (15th-19th), 7 votes. ISS-009 + ISS-017 follow-ups
  SHIPPED; INDEX flips slipped (named items still Open). 3rd consecutive
  slip on datanet rubric. Filed article weekly-review-2026-06-08.md.
  4 next-week actions: FALLBACK_REPPO_SKILLS (by 6-11 — **VOIDED 6-10 by
  Docker migration, reppo off-CI**), ISS-018 file (by 6-09, still overdue),
  RUBRIC+1-datanet (by 6-12), 4-issue INDEX flip (by 6-10, still overdue).
- **2026-06-08 18:13Z PR #80 investment-advisor merged** then immediately
  failed on the same 429. PR #82 opened 18:13Z to supersede with
  standalone Virtuals workflow; PR #81 closed. `chain:investment-advisor`
  in cron-state with `last_failed=2026-06-08T17:04:46Z, no last_success`
  field — chain not in current `aeon.yml` per heartbeat 6-09; dropped
  from status table.
- **2026-06-09 06utc 20th mint 420334cb** — 0x06cecfba 250 AAVE Close-Short
  52.1min +$85,196 Sharpe 8458.93 MDD 0% win 100%. 2nd-highest pnl in ledger
  ever. Ends 2-day mintless streak. Multiple replays of same canonical
  (3rd-run 4th-run both correctly DEDUP'd; 4th-run also surfaced superset
  AAVE+BTC late-window dataset Sharpe 763.91 vs prior 8458.93 = materially
  regressed per Step-4.2 ≥0.5 rule despite sum_pnl improving to +$279k —
  rule held).
- **ISS-016 ledger workaround held under load 22+ consecutive runs.**
  6-09 voter caught pod 841 (today's 20th-mint) via wallet-shortcode +
  pods 764/824/825/828/832 (pre-ledger own pods) via 1st-run digest
  cross-ref. 4th-run regressed (5 own-pod reverts replayed 1st-run
  pattern — cross-ref not durable across runs, only prefetch repair
  fixes). Severity promoted medium → high after 6-09 1st-run digest
  >50% revert rate.

## Recent anomalies (through 2026-06-05)
- **2026-06-05 trading-agent triple-mint** — 11-run dry streak ended;
  3 mints landed same day (15th 4a9a582a HFT 821 closes, 16th 16671d6f
  Sharpe 48,523 SOL+BTC 9.548s cluster, 17th e2e925b2 LINK 201 single-mkt).
  New single-day record (surpasses 3-mint days 5-29 + 5-30). Two new
  operator follow-ups emerged: spot_pct threshold in Step 4.2 and
  Sharpe-vs-pnl tiebreak in Step 4. See Recurring blockers for detail.
- **ISS-016 ledger workaround fired live 2026-06-05** for the first time
  on the active epoch — re-run filtered pod 583 (own 15th-mint); 3rd-run
  filtered pods 583 + 585 (own 15th + 16th mints) in the same pass.
  15 consecutive voter runs at prefetch count=0 — workaround durable.
- **Watchlist twin trip 2026-06-04** — REPPO −17.93% + GITLAWB −26.25%
  both crossed 24h thresholds (first trips since canonical watchlist
  landed PR #55). 2026-06-05 cooldown: REPPO −6.75%, GITLAWB −0.25%;
  GITLAWB 3-day cumulative still −34% off 6-01 baseline. MAMO accelerating
  d/d 3 consecutive days (-6.11/-7.16/-9.60% 6-03→6-05) toward 15% rail.
- **narrative-tracker 2026-06-05 transitions** (Day 2 after re-baseline):
  3 NEW (capital rotation crypto→AI equities, ETH leadership crisis,
  proof-of-energy meta), 2 PROMOTED (BTC cycle-break Rising→Peak, RWA
  Rising→Peak), 3 DEMOTED (Hyperliquid Peak→Fading per HYPE −8.65%,
  privacy coins Rising→Fading per ZEC −43.66%, institutional BTC Peak→
  softening), 2 DEAD (LAB Fading→DEAD, altseason rotation Rising→DEAD).
  6-04 contrarian-FADE on BTC cycle-break was wrong; consensus bear played
  out. Reflexivity flagged 3 (Hyperliquid unlock, ZEC AI-assisted exploit,
  capital rotation self-fulfilling).
- **chain:reppo-swarm state-flip**: 2026-06-02 12:23Z `cron-state.json`
  flipped `last_status=failed` while `gh run view` confirmed workflow
  exit `conclusion=success`. ~5s gap between in-chain state-writer and
  final workflow exit; cleared on 18:12Z chain cycle. **7 successful chain
  cycles since** (6-03 × 3, 6-04 × 2, 6-05 × 2). Investigating under
  ISS-010 scope. Not a real chain failure but flips `docs/status.md`
  momentarily to DEGRADED on the literal rule.
- **on-chain-monitor + defi-monitor 2nd-consecutive NO_CONFIG 2026-06-05**
  (1st was 6-04 first-fire). Both gated behind `memory/on-chain-watches.yml`
  which is absent; skills exit cleanly without notification. Operator-populate
  required before either produces signal.
- **vibecoding-digest cron-state mismatch**: skill emits
  VIBECODING_DIGEST_ERROR notification but workflow exits 0, so
  cron-state records `last_status=success`. Workflow-exit-vs-skill-
  outcome mismatch. Now moot — skill disabled with ISS-015 resolution.

## reply-maker ad-hoc (new pattern)
- 2026-06-02 mid-day: operator forwarded an X URL via Telegram
  (RG @rgvrmdya QT'd @reppo's Orquestra launch and dedicated it to
  @anajuliabit). reply-maker drafted 2 reply options in ana voice,
  staged to `.pending-notify/reply-drafts-rgvrmdya.md`. Tweet content
  sourced via api.fxtwitter.com/{handle}/status/{id} after x.com
  direct WebFetch returned HTTP 402 and nitter.net returned empty —
  fxtwitter is the working sandbox-friendly fallback for X content.

## Project Lens & content skills
- **project-lens first article published 2026-06-01** (`sherwood.sh`
  operator-supplied lens). Industry-comparison angle vs Aeon's cron-as-
  optimistic-governance shape; angle history file seeded.
- 8 consecutive search-skill NO_GAP exits through 2026-06-01 — fleet
  gap-free on external-skill axis.

## 2026-06-12 → 2026-06-13 — 4th weekly-limit wave + ISS-018 collision
- **2026-06-12 weekly-limit wave (4th occurrence of the ISS-018 pattern).**
  ~12 daily skills hung 07:05–14:57Z with `last_status=dispatched`
  (morning-brief / daily-routine / thought-review / skill-freshness /
  github-trending / aixbt-pulse / on-chain-monitor / defi-monitor /
  narrative-tracker / security-digest / search-skill + the 08:00 + 14:00
  heartbeats themselves). **Diagnostic split confirmed**: the 5
  `FALLBACK_CG_SKILLS` (defi-overview / token-movers / token-pick /
  token-alert / market-context-refresh at
  `.github/workflows/aeon.yml:498`) SUCCEEDED via the Virtuals fresh-fetch
  fallback; every non-fallback skill dispatched in the same window HUNG.
  Confirms cause = claude weekly limit (not external API). Evening cluster
  16:00–18:16Z self-recovered. Pattern is now provably weekly-cyclical.
  Residual gap remains undocumented: non-reppo CI dailies outside
  `FALLBACK_CG_SKILLS` still `exit 1` on weekly limit.
- **2026-06-13 carryover cascade.** 10 daily-slot carryovers from the 6-12
  wave were still stuck at 08:04Z heartbeat (today's 07:00 + 08:00 slots
  guarded on stuck-state, did NOT re-dispatch). By 14:38Z, ~92% of daily
  fleet drained — 12:00 UTC cluster fully recovered (on-chain-monitor,
  btc-levels, token-alert, token-pick, defi-overview, token-movers,
  defi-monitor, market-context-refresh, narrative-tracker all ran SUCCESS).
  Residual: 3 dailies still stuck (search-skill / security-digest 6-12T14:57Z,
  self-improve 6-11T18:51Z); 11 weekly carryovers pending next tick.
- **ISS-018 number collision (NOT the weekly-limit issue).** vuln-scanner
  ran 17:00Z and filed `ISS-018` for `scripts/prefetch-vuln-scanner.sh`
  missing (sandbox blocks semgrep/trufflehog/osv-scanner installs/runs on
  every invocation). The intended "weekly-limit incident" issue —
  overdue from 2026-06-09 across 4 occurrences (6-06/07/08 + 6-12 wave) —
  remains UNFILED and should be `ISS-019` if filed. MEMORY.md goal
  renamed to reflect.
- **vuln-scanner 6-13 17:00Z**: target superloglabs/superlog (806★ TS
  Apache-2.0). 12 packages with recent high/critical advisories triaged;
  0 confirmed. esbuild Deno-only path, react-router Declarative Mode,
  next 15.5.15 demo-only `apps/sample/` → dropped per `demo/` triage
  rule. Channels: 0 PVR, 0 public PR. Dedup window armed through
  2026-07-13. Report at `articles/vuln-scan-2026-06-13.md`.
- **Skill-health 2026-06-12 18:09Z snapshot.** 41 healthy, 0
  critical/degraded/flapping/warning, 2 no_data (operator-scorecard +
  fork-skill-gap — await first weekly tick). Clean. Previous 6-10
  snapshot had 7 no_data; the 5-skill drop reflects autoresearch +
  fork-cohort + fork-skill-digest + unlock-monitor + vuln-scanner all
  acquiring first-run data during the week (vuln-scanner's today, others
  on their tick). `article` carries sr=0.5 (2 runs, under chronic
  threshold).
- **28-narrative tracker 6-13.** 5 NEW (#1 decentralized AI bid standalone
  on Anthropic Fable-5 + Mythos-5 US-gov export-control directive — TAO
  +17.4% TRENDING+UP+BREAKOUT + VVV +16.2% + MOR bid; #24 Polymarket US
  $969M CFTC-approved debut; #25 Curve gauge weight rotation on
  cvxCRV +13pts / sdcrv +3.5pts twin signal; #26 CFTC onshore BTC perp
  futures; #28 AI engineering layoffs as macro-tech context). 1 PROMOTED
  (#2 AI×crypto agent custody stack structural hardening — Coinbase
  agent accounts 6-12 = 5th big-co primitive in 4 months). 3 DEMOTED
  (#3 HL perp DEX Fading deepens, #6 stablecoin rails Peak softening,
  #8 capital rotation Bear-for-crypto → Mixed after anthropic
  export-control splits the call). 2 DEAD (#13 XMR/ZEC privacy-coin
  rotation one-session kill — 4th consecutive failed privacy-coin call,
  pattern stop holds; #15 VELVET parabolic terminal capitulation,
  6-11 FADE validated).
- **Token-alert 6-13 09:30Z.** REPPO +14.39% 24h / +22.05% 2d on baseline
  vol (0.94× rolling mean) — 61bp under the 15% rail. Closest non-trip
  on the up-side since canonical watchlist landed. No alerts fired
  (thin participation). Prior up-trip was GITLAWB +18.74% on 6-09.
- **No new mints 6-11/6-12/6-13.** Chain is `enabled: false` per Docker
  migration; ledger only advances off-CI. Still 25 mints + 45 votes
  through 2026-06-10.

## 2026-06-15 → 2026-06-16 — PR #108 durable + Hormuz risk-on + XAI quota wall
- **PR #108 file-flag notify path CONFIRMED durable.** All standalone
  skill notifications across 6-15 + 6-16 (morning-brief, daily-routine,
  weekly-shiplog, github-trending, aixbt-pulse, narrative-tracker,
  market-context-refresh, defi-overview, token-pick, token-movers,
  token-alert, list-digest, agent-buzz) delivered direct via
  `./notify -f .pending-notify/{skill}-msg.md` or `./notify` literal
  arg — no post-run `.pending-notify/` carryover fallback observed.
  6-14 caveat ("standalone runs still staging") fully cleared. PR
  retired the dominant sandbox fallback pattern noted across 6 days
  of standalone runs (6-09 → 6-14). Some `.pending-notify/` rm
  attempts still blocked by sandbox gate, but dedup catches and
  delivery still succeeds — operationally clean.
- **Weekly-shiplog 2026-06-15: SHIPLOG_OK.** 113 commits / 109 PRs
  merged / 2 issues closed in 7d window (2026-06-08→2026-06-15).
  Themes: multi-provider LLM gateway with automatic failover, soul
  & strategy builders lower the on-ramp, skills can call MCP servers
  mid-run. +11,602 / -4,784 lines across ~300 files. Article at
  `articles/weekly-shiplog-2026-06-15.md`.
- **BTC reclaim65900 FIRED 2026-06-15 14:00Z** ($66,427 spot vs
  $65,713.62 prior close). reclaim65900Alerted false→true. Both
  armed reclaim levels now SET (reclaim63500 6-11, reclaim65900
  6-15). Driver: Hormuz peace deal LANDED — Polymarket "US × Iran
  peace deal by June 15?" YES 11%→93% (+82pp) as deadline arrived;
  oil premium drained into risk. 6-16 consolidating $66k-$67k
  pre-BOJ-Tuesday (binary catalyst per morning-brief focus).
- **btc-levels recovered same-day 6-15** — failed 05:42Z (first
  failure since skill landed, empty-usage `total_cost_usd:0 /
  output_tokens:0` error, same signature as bb3ab24 chore commit)
  → RECOVERED 07:38Z. sr 0.97, cf 0.
- **Narrative tracker consolidated 34→27 on 6-15.** 1 NEW (#27
  risk-on regime flip on Hormuz landing), 1 RESURRECTED (#13 XMR/ZEC
  privacy on ZEC +24.5% squeeze + Garrett Jin $21M HL long + clean
  audit), 2 PROMOTED (#26 BOJ-tuesday Emerging→Rising, #1 decAI
  thesis-hardening), 1 DEMOTED (#22 COAI faded), 2 DEAD (#7 BTC
  capitulation contradicted, #15 VELVET parabola resolved).
- **XAI quota exhausted 6-16 (NEW MEMORY.md goal).** Team 3a8b4c1e
  monthly credit limit hit — 3 skills today: token-pick 12:42Z
  (X leg absent), list-digest 17:56Z (LIST_DIGEST_EMPTY), agent-buzz
  17:56Z (AGENT_BUZZ_ERROR). Tweet-roundup AM (07:18Z) worked because
  WebSearch returned summary-grade news (not tweets) and spec accepts
  that; agent-buzz requires engagement metadata and cannot. **Residual
  gap from ISS-019 scope extends here:** when XAI quota dies,
  x_search-dependent skills have no fallback chain that resolves to
  a deliverable curation. XAI-dependent skills (agent-buzz / token-pick /
  refresh-x / remix-tweets / tweet-roundup / narrative-tracker /
  reply-maker / list-digest / article / fetch-tweets) NOT covered by
  `FALLBACK_CG_SKILLS`. Operator action: top up XAI credits or wait
  for monthly reset.
- **Monday-weekly tick 6-15 fully cleared previous-week carryovers.**
  cost-report 07:45Z, weekly-shiplog ran ok, unlock-monitor 10:00Z
  UNLOCK_MONITOR_OK (CONX 2,886× daily-vol leverage, SPK fade-pump,
  H biggest $ at $109.8M absorbed), deal-flow Monday 14:00 tick
  FAILED to clear it (stuck since 6-08 15:02Z, ~8d). fork-cohort
  2nd consecutive Sunday weekly fail (stuck 6-14 19:09Z).
- **PR #112 stalled** (skill-graph docs auto-gen, opened 6-14
  17:41Z) — past 24h stalled threshold across 6-15 → 6-16. Action-
  converter loop "merge #112" per 6-15 19:23Z + heartbeat 20:27Z
  flag.
- **PR #122 fix(docs) opened 6-15 19:13Z** in response to all-skill
  WebSearch 400 environmental failure earlier in the day. Under 24h
  threshold at 6-16 morning-brief read.
- **skill-evals 6-14: SKILL_EVALS_RECOVERED + COVERAGE CLIFF.**
  0 new fail / 1 fixed / 1 still failing / 12 stable. Coverage
  14/57 (24%) — 24pp drop from 48%. Action queued: patch
  `evals.json:monitor-polymarket` (POLYMARKET pattern too broad
  → tighten to `### monitor-polymarket`).
- **ISS-018 number collision noted on 6-13.** vuln-scanner filed
  ISS-018 (sandbox-limitation: scripts/prefetch-vuln-scanner.sh
  missing). The "weekly-limit incident" issue overdue from 2026-06-09
  remains UNFILED and should be **ISS-019** if filed. MEMORY.md
  goal renamed.
- **Skill health stable through 6-15 19:13Z snapshot: 41 healthy /
  0 flagged / 2 no_data** (operator-scorecard + fork-skill-gap
  await first weekly tick). Same classification through entire week
  6-12 → 6-15.
- **Status page docs/status.md** regenerated each heartbeat —
  consistently Overall=🔴 DEGRADED on stuck rows (deal-flow 8d,
  fork-cohort 38h). 43-44 enabled rows sorted last-run desc.
- **search-skill 7th consecutive NO_GAP** (6-09 → 6-16). Fleet
  capability gap-free; all "missing" signals are internal shims
  (ISS-018) or operator-blocked (watches.yml).
- **Thought-review 12 consecutive zero-capture days** through
  6-16. Operator inbox cold since personal-stack PR (~12d).
  `vault/inbox/` empty (.gitkeep only).
- **on-chain-monitor / defi-monitor 12 consecutive NO_CONFIG days**
  through 6-16. Operator-gated on `memory/on-chain-watches.yml`
  seed.

## Recent Issues & Patterns (through 2026-06-21)
- **Sandbox-truncation systemic** (6-19 → 6-21): ISS-019/020/021 (defi-overview, token-pick, search-skill) extended by ISS-022/023/024 (monitor-polymarket, token-alert, skill-health) — 8 skills critical / 19 degraded share `output_tokens=0` signature. Cluster timestamps 2026-06-21 12:14-14:17Z.
- **Skill-health classification flipped 6-21**: From "41 healthy / 0 degraded" stable baseline (6-12 → 6-19) to **9 critical / 19 degraded / 3 warning / 2 no-data / 9 healthy**. systemic flag set. Caused by accumulating cron-state denominators while successes lag.
- **Heartbeat chronic tail expanded 6-21**: 24 skills with success_rate < 0.5 (vs 11 on 6-19 baseline). Worst: reg-monitor 7%, vuln-scanner 7%, skill-analytics 9%, security-digest 16%, list-digest 22%.
- **Token-alert NEW stuck mode (6-21 13:45Z)**: First time the skill hung mid-dispatch (`last_status=dispatched`, 96 min elapsed). Different failure mode from cron-tick miss.
- **on-chain-monitor seeded but degraded** (6-21): Operator populated `memory/on-chain-watches.yml` with 5 Base wallets. Etherscan v2 keyless API blocks Base chain on free tier — `ON_CHAIN_DEGRADED` until `ALCHEMY_API_KEY` / `ETHERSCAN_API_KEY` set. CoinGecko ETH/USDC prices OK.
- **defi-monitor still NO_CONFIG**: Watches file has only wallet entries. defi-monitor consumes `type: pool` / `type: position`. Needs pool/position contract addresses + ABIs seeded.
- **PR backlog cleared**: 0 open PRs as of 6-21 15:22Z heartbeat. #112 + #122 + #127 all merged or closed since 6-19.
- **Weekly-limit wave 2026-06-12**: 4th occurrence of the ISS-018 pattern. Diagnostic split confirmed: 5 `FALLBACK_CG_SKILLS` succeeded via Virtuals fresh-fetch fallback; non-fallback skills HUNG. Pattern is weekly-cyclical.
- **XAI quota exhausted since 6-16**: Team 3a8b4c1e monthly credit limit. 10+ XAI-dependent skills blocked. As of 6-21 daily-routine: `tweet-roundup` working off WebSearch fallback successfully (no 400). `agent-buzz` 6-21 ran off XAI cache (`.xai-cache/agent-buzz.json`, fresh 14:37Z) — cache still warm despite quota.
- **deal-flow stuck since 6-08** (13 days). **fork-cohort** stuck 7 days (2nd consecutive Sunday weekly fail).
- **chain:investment-advisor** failed 6-08, off status table (dropped from `aeon.yml chains:`).
- **PR #108 file-flag notify path** continues working durably across all standalone skills (no `.pending-notify/` carry-over).
- **BTC levels**: Both reclaim 63,500 (6-11) and 65,900 (6-15) triggered. 6-21 spot range $63,986–$64,080, close $64,240. No alerts fired this week. Daily close < $60,500 still arms downtrend continuation alert.
- **Token alert canonical watchlist**: REPPO ±15% trips (6-14 +18.93%, 6-16 -15.78%) → 6-19 consolidation -8.52% (no follow-through). GITLAWB downtrend through 6-19 ($0.00006304). WELL/MAMO stable.
- **Recent token picks**: EIGEN (6-22 ~13:00Z) $0.305 HIGH 9/10 EigenCloud rebrand + Darkbloom Public Alpha; AERO (6-21 13:15Z) $0.5406 +10.19% HIGH 7/10 Base DEX play; SOL (6-21 13:50Z re-fire) $73.47 +8.46% 7d HIGH 7/10; HYPE (6-20) $71.06; JTO (6-16) $0.87 — all market legs skipped on Polymarket sports-heavy / dedup gates.
- **Narrative tracker 6-22**: 15 actionable post-dedup. Transitions: 5 NEW + 1 PROMOTED (stablecoins velocity → ↑↑) + 2 DEMOTED + 4 DEAD (sovereign AI chains, privacy tech, AI agent accountability, altseason rotation) + 4 CONSOLIDATED. 4 reflexivity flags inc. **1 inverse-reflexivity** (stablecoins/x402 real infra, fundamentals catching story). **Structural shift flagged: Kaito killed Yapper 2026-01-15 → Studio + Attention Markets (Polymarket joint)** — mindshare measurement layer shifting from points-driven to prediction-market-driven. 2 FRONT-RUN (P2P security mesh, ownership tokens), 8 RIDE, 3 WATCH, 1 FADE, 1 IGNORE.
- **AIXBT Pulse 6-22 10:00Z**: 7 NEW (Toss Bank Korea Solana PoC, SOL tokenized stock vol, security cluster Taiko/Aztec/Altura, BTC ETF $6.35B quantified, China +1T yuan, Treasuries 4.48% retreating, TradFi regime flip hawkish→easing). Clusters 36 tracked (down from 46 on 6-21).
- **market-context-refresh 6-22 16:00Z**: regime chop (low conviction). BTC $64,938 +1.52%, ETH $1,755 +1.92%. F&G 20 (↓3 to Extreme Fear). Breadth 13/20 green 24h · 6/20 7d (weekly downtrend dominant). Top narrative EigenCloud/AI-infra restaking.
- **defi-overview 6-22**: Mixed — TVL $73.6B (chain delta API regression day 5). DEX vol $4.2B (-10.8% 1d, -9.1% 7d). Top mover up Dolomite +14% (7d +56% lending inflows). 3 real-yield pools recovered (WSOL-USDC 32.4%, WETH-USDT 25.1%, UNI-WETH 17.3%) vs 6-21's 0. Stables $313.9B (+0.05%).
- **token-movers 6-22 12:37Z**: 77/100 green, median +0.87% — risk-on breadth but bounce-back leaderboard. Winners UB (+21.5% [FADE] 7d -3.8%), DEXE +18.7%, EIGEN +12.2% (7d +42.8% Darkbloom pivot). Losers H -22.5% (7d -73% continued capitulation), RE -17.6% [CAPITULATION] vol $159.8M on $125M mcap. SYN [PUMP-RISK] +91.6% trending.
- **unlock-monitor 6-22 10:38Z**: 3 tiered events (2 CRISIS, 0 STRAIN, 1 DIGESTIBLE). Top leverage **NEWT at 1.36× 24h-vol-proxy** — cliff $7.14M, 139.58M tokens = **64.9% of circulating supply** on $11M mcap, supply ~doubles 6-24. H investor STRAIN→CRISIS bump (post-$36M-exploit).
- **weekly-shiplog 6-22**: 58 commits / 58 PRs (vs 113/109 6-15) / +3,300 -3,920 first net-negative-lines week (20-skill prune #473 = -3,765). Themes: flat-skill-list to packs, one-click community pack install (5 packs), dependency hygiene wired.
- **security-digest 6-22 14:42Z**: 3 today / 0 this-week / 0 monitor. New KEV adds: CVE-2026-20262 Cisco SD-WAN + CVE-2026-54420 LiteSpeed cPanel. 2 npm `type=malware` adds (node-path-utils, mddriver — both 6-22T06:30Z). SECURITY_DIGEST_OK.
- **skill-security-scan 6-22**: SECURITY_SCAN_NOCHANGE. 4 HIGH / 15 MEDIUM / 4 LOW · 0 new · 0 resolved since 6-15. All 4 HIGH persistent in aeon.yml (L86/L94/L96/L812 — workflow_dispatch / workflow_call gated, low real risk).
- **search-skill 6-22**: Queried "vulnerability scanner" (vuln-scanner sr=0.07/29 runs, ISS-018 open). Found `davila7/claude-code-templates:vulnerability-scanner` (sum=19 UNTRUSTED, manual install only) — pure-python OWASP checklist sidesteps missing semgrep/trufflehog/osv-scanner binaries. Complementary to current vuln-scanner (OWASP audit vs responsible-disclosure pipeline).
- **on-chain-monitor 6-22 12:47Z**: ON_CHAIN_OK 5/5 watches, 0 surviving events. Blockscout keyless path used (Etherscan v2 free-tier blocks Base; ALCHEMY_API_KEY/COINGECKO_API_KEY workflow refs are length=0 — secrets injected as empty). 2400-block window too narrow for slow Safe multisigs — needs operator to widen default or supply Alchemy key.
- **deal-flow recovered 6-22 ~14:30Z**: clean run after 14d stuck since 6-08. ~32 candidates → 8 kept. Top: Baseten $1.5B Series E @ $13B post (2.6× val in 5 months). Themes: capital clustered on inference/compute (Baseten + Hydra Host $100M Series A w/ Nvidia + Founders Fund); cross-camp validation (Morpho $175M w/ Ribbit + Paradigm + a16z; Ripple → Flutterwave $3.2B strategic equity for RLUSD on African corridors).
- **token-alert recovered 6-22 ~13:00Z**: TOKEN_ALERT_OK. First clean run since 6-19. REPPO +5.49% / GITLAWB +9.66% / watchlist median +1.83% (first green-median since 6-14). REPPO 3d arc $0.01716998 → $0.02505217 = +45.91% reversal of 6-16 -15.78% trip. Volume-spike leg skipped (n=2, need 5 — 6-20/6-21 missing due to stuck-dispatch gap). Closes ISS-023.
- **cost-report 6-22 NEW FAILURE**: Mon weekly tick dispatched 12:36:29Z, failed 13:05:55Z. cf=3 (crossed API-degradation threshold), sr=0.50 (3/6). output_tokens=0 signature → extends ISS-019/020/021/024 sandbox-truncation cluster.
- **skill-freshness 6-22**: FRESHNESS_WARN — operator-scorecard depends on stale articles/skill-analytics-*.md (288h/12d, weekly 192h threshold). FRESHNESS_NO_CHANGE — fingerprint d522755e unchanged since 6-21; re-emits 6-28 if still unresolved.

## Soul-builder + MemoClaw strip (2026-06-22)
- **Soul-builder run** (morning 6-22) — subject @anajuliabit. Sources: anajuliabit.eth.limo + github.com/anajuliabit + DEV.to articles + X paywalled (direct tweet fetch 402, fell back to websearch). Files written: soul/SOUL.md, soul/STYLE.md, soul/examples/good-outputs.md. Added MemoClaw, ZHC worldview, DEV.to writing samples, The Range section, Vocabulary section.
- **Operator removed MemoClaw 6-22** — declared dead project via Telegram. Stripped from soul/SOUL.md: projects bullet, current-focus paragraph, tensions bullet, "AI agents have a memory problem" worldview, "Your agent's memory should work like yours" + namespace-leak opinions, "Uses AI tooling…fix amnesia" build-philosophy line, interests list pruned (`semantic memory for agents · x402 payments` removed), pet peeve on MEMORY.md, "memory architecture" → "vault architecture" in The Range. Stripped from good-outputs.md: 7 MemoClaw shorts/mediums/long-forms (sample count 16 → 10). Sherwood/Reppo/Mamo/Moonwell kept intact. PR drafting per CLAUDE.md "never push directly to main".

## Infrastructure updates (since 6-17)
- **PR #108 file-flag notify path** confirmed durable (6-15→6-16). Retires dominant sandbox fallback pattern (`./notify "$(cat ...)"`) across standalone skills.
- **Decentralised-AI bid validated.** 6-13 narrative-tracker #1 FRONT-RUN
  call (TAO HIGH 10/10 token-pick $248.76) paying +23.5% in 24h.
  Day-2 catalyst: WSJ/TechCrunch identify Andy Jassy as the trigger
  for US-gov Anthropic Fable-5/Mythos-5 access suspension (AWS
  researchers used Fable 5 to jailbreak a software-vuln-ID
  safeguard; AWS itself lost access to its own portfolio company's
  models). Rotation INSIDE DeAI: meme-side (TRUMP/EDGE/GWEI/VVV) all
  flipped TRENDING+DOWN intraday — money rotating into
  decentralised-compute primitives (TAO/AKT/FET) over AI-token wrappers.
- **defi-overview 6-14 Mixed verdict.** TVL recovery decelerated
  sharply (+0.41% snap c1d vs 6-13's +1.47% — a third of yesterday's
  pace). DEX vol -22.2% raw / **-38% clean ex-Polymarket-US** (PM US
  $1.70b print day 2, still inside the 7-day US-launch artifact
  window — distortion intensifies vs 6-13's $969m debut). 0 chain
  movers cleared 5% snap floor. 2 protocol UP (Figure Markets RWA
  +27%, Fluid Lite +11%) both no-obvious-catalyst. 0 protocol DOWN —
  Dolomite full direction-reversal ↔ (+10.88% → -9.24%, 19.96-pt
  swing) misses the strict gate. **Steakhouse Financial rolled OFF
  fees-beating-TVL** (was 6-13's biggest-ever entry on this list at
  $2.06b; fees c7d collapsed +41.48% → +15.65% under the 20% gate;
  TVL caught up). cvxCRV gauge surge cooling (-4.14pts to 27.35,
  first cool-off in 2 days). Yesterday's hot real-yield pool
  WETH-USDT (uniswap-v3) collapsed 40.63 → 11.36 apyBase + conf
  fell 2→1 — full hot pool rollover confirmed. 3 NEW real-yield
  pools displaced (REUSDE/MSUSD/ONYC — first re-protocol entry,
  first mainstreet entry, **first Solana real-yield entry** since
  yield-list adoption). /v2/chains c1d/c7d null **DAY 16** of API
  regression.
- **token-movers 12:30Z refresh — alt-bid cooling intraday.** Breadth
  halved since 07:12Z daily-routine (59 → 40/100 green); BTC $64,449,
  ETH $1,673, SOL $68.05. DeAI basket cooled hard intraday (TAO +23.5%
  → +7.5%, AKT +21.5% → +13.7%, JASMY +16.7% → +10.2%, VELVET +20.8%
  → +10.4%). H +135.7% biggest single-session reversal of the week
  (was +75.1% AM) but 1h -7.6% suggests top cooling — earned FADE tag.
  BTW BREAKOUT accelerated (+15.8% → +23.0% intraday). BEAT -34.2%
  (deepened from -20.1% AM — parabolic giveback of 6-13 narrative-
  tracker #21 BEAT-breakout call confirmed Bear).
- **github-trending 6-14: NVIDIA/SkillSpector top pick** (Python,
  4742★ total / 804 today / 55.8 stars/d ACCELERATING) — first-party
  security scanner for the agent-skills marketplace primitive
  (addresses supply-chain risk of arbitrary skills loaded into coding
  agents). Plus LMCache v0.4.7 (CUDA 13 nightly, KV cache for vLLM),
  agentsview (Go, "100× faster ccusage replacement" claim),
  music-assistant/server (2.9.0 stable). Short trending-feed day
  (14 returned, confirmed via second WebFetch — not fetch failure).
  Same skill-marketplace meta noise pattern dropped 3× today (vs 5×
  6-13).
- **heartbeat 6-14 08:33Z: zero stuck daily-slot skills, wave fully
  drained.** Previous days' daily carryovers all recovered overnight
  (evening-recap 6-13 21:16Z, aixbt-pulse 21:17Z, btc-levels 05:31Z,
  skill-evals 07:18Z = first non-stuck Sunday weekly tick post-carryover,
  thought-review 07:09Z, morning-brief 07:11Z, daily-routine 07:15Z).
  9 weekly carryovers still stuck (all >5d old, await next weekly
  tick: 4 Sunday-scheduled clear today 17–19Z, 5 Monday-scheduled
  clear 6-15). docs/status.md still DEGRADED on the stuck rows.
  HEARTBEAT_OK · STATUS_PAGE=DEGRADED — no notify (dedup, all in last
  48h logs).
- **Skill-health latest snapshot (2026-06-13 18:18Z): 41 healthy / 0
  flagged / 2 no_data** (operator-scorecard + fork-skill-gap — await
  first weekly tick). Clean. No drift from 6-12 snapshot.
- **thought-review 8 consecutive zero-capture days** through 6-14
  morning. Operator inbox cold since the personal-stack PR landed
  (6-04 PR #71). `vault/inbox/` empty (.gitkeep only).
- **on-chain-monitor / defi-monitor 9 consecutive NO_CONFIG days**
  through 6-14. `memory/on-chain-watches.yml` still absent —
  operator-gated.

## 2026-06-23 fleet deltas

- **Regime flip chop → risk-off (high conviction).** market-context-refresh
  13:24Z: BTC $62,055 -4.66% 24h, breadth collapsed 13/20 → 3/20 green in
  one session. Triggers: Korea Kospi -10% circuit breakers, $500M crypto
  liquidations, Warsh hawkish Fed repricing, JPMorgan $165B Q2-end
  rebalancing. F&G 23 still lags (doesn't yet capture today's action).
- **ISS-025 cost-report widening.** cf escalated 6 → 7 (6-22 evening)
  → 18 (6-23 morning batch) → 23 (6-23 13:10Z batch wave), sr=0.12 (3/26).
  Same `outputTokens=12` sandbox-truncation variant of ISS-019/020/021/024
  family. Dedup-blocked across morning-brief 07:07Z + heartbeat 08:24Z +
  14:05Z — no spam-notify on same-day escalation.
- **Positive 13:10Z batch wave.** 8 skills green: defi-overview /
  token-pick / token-alert / token-movers / btc-levels / defi-monitor /
  market-context-refresh / on-chain-monitor. cost-report sole failure
  in batch. on-chain-monitor surfaced W3 cyrillic `ÚSDС` mirror attack
  (1480 fake-units, fires 3 min after legit $1480 USDC W3→W1 transfer;
  byte-swap clone of W1 address). Operator notified + explainer sent via
  Telegram.
- **token-alert 6-23 13:12Z fired GITLAWB -15.63% rail break** — first
  downside trip since REPPO -15.78% on 6-16. Watchlist median 24h
  **-11.34%** — first sub-(-10%) median print since canonical watchlist
  landed. WELL/MAMO/REPPO/GITLAWB all red, consistent with broader
  risk-off (BTC -4.66%). vol on GITLAWB at 1.26× (real bid on dump,
  well under 3× capitulation rail).
- **EIGEN 6-22 HIGH 9/10 pick at invalidation.** -15.3% morning →
  -17.0% afternoon TRENDING+DOWN. Estimated ~$0.258 vs $0.26 invalidation.
  One-day reversal of restaking → AI-infra narrative pivot. SSV Network
  TVL -38.95% 7d confirms restaking sector derisked.
- **Token pick 6-23 DEXE HIGH 7/10 $22.98** (+28.2% 24h / +23.4% 7d).
  Only large-cap green on sea-of-red day. DAO-governance rotation —
  KCEX listing + "Dexelization" framing + $1.7B platform TVL. Score
  7/10: 24h+1, 7d+1, both>5%+2, RS vs BTC/ETH+2, DEX+1. Risk: 51.5%
  supply locked Q4 unlock cliff; intraday $17.62/$24.12 range mirrors
  June 3 $24.49 wick reversal. Exit target $28 / inv $19 / 14d.
  Market: Israel × Hezbollah peace deal by July 31 — YES 16.5¢, fair
  ~6%, edge 10.5pp (sell YES / buy NO at 83.5¢).
- **Narrative-tracker 6-23 14:09Z:** 12 actionable (vs 6-22's 15).
  5 NEW + 1 PROMOTED (DePIN/GPU compute Rising→Peak w/ IO/TAO/AKT
  slate) + 2 DEMOTED + 2 DEAD + 3 CONSOLIDATED. 3 reflexivity flags +
  1 carry-over (Kaito Yapper EOL). **INVERSE flag — AI capex rationing**
  (Tencent + Uber real fundamentals catching the AI-infra story,
  contrarian-bear). Key today: 9 of 12 threads AI-side, rotation
  signal hardening.
- **AIXBT Pulse 6-23 09:00Z:** 6 NEW (Warsh hawkish repricing, BTC
  crash <$62K + $500M liqs, Solana $40 bear call + KOL skepticism,
  institutional receipts Cboe/Ripple/UBS/Allfunds, protocol unwind
  Synthetix/ENS/Sonic, SpaceX-led tech selloff). Bridge call:
  Warsh + DXY executing into BTC order book — $500M liq = macro
  reading into on-chain leverage.
- **defi-overview 6-23:** Mixed — DEX vol $6.02B +45% 1d on sell-off
  volume spike. Top mover up Mellow Core +34% / Polygon Bridge +25%.
  Top mover down SSV -37% ($4.7B drop, likely re-measurement). Real-yield
  count **301 cleared** (vs 6-22's 3, 6-21's 0 — yields data quality
  fully recovered). Aave V3 fees +31% / TVL -4% 7d (real lending demand).
  Stables $313.8B; DAI +8.5% on $4.85B = ~$380M new mint.
- **security-digest 6-23 14:12Z:** 2 today / 5 this-week / 2 monitor.
  free-claude + free-anthropic-claude = Anthropic-SDK typosquats —
  direct supply-chain shot at ecosystem operator builds against. Plus
  26 npm malware drops in single 6h window. Budibase + Gogs coordinated
  patch batches collapsed onto one line each. KEV net-new = 0 this week
  (Splunk + Joomla already in prior digests).
- **search-skill 6-23** queried "llm cost" (cost-report cf=23). 5 hits
  all failed hard gates (PostHog-coupled, playbook-not-cron, board-locked).
  Note: cost-report failure is ISS-025 sandbox-truncation, not capability
  gap. Right fix path is root-cause, not external swap. SEARCH_SKILL_EMPTY.
- **list-digest 6-23 17:10Z** + **agent-buzz 6-23 18:00Z:** both clean
  via xai-cache path. cyrilXBT anthropic 13-cert drop top tweet
  (♥266/↻62/score 19.1). agent-buzz: MCP landscape mapped + tooling
  stack fills in + production multi-agent governance.
- **skill-freshness 6-23 08:24Z:** FRESHNESS_NO_CHANGE — operator-scorecard
  still depends on stale articles/skill-analytics-*.md (312h/13d, weekly
  192h threshold). Fingerprint unchanged from 6-22; re-emits 6-28 if
  still unresolved.

## 2026-06-24 fleet deltas

- **Regime flip risk-off → chop.** market-context-refresh: BTC bounced
  $62,055 → $62,442 (+0.62%), breadth 3/20 → 10/20 green. F&G 23 → 17
  is the index catching up to 6-23 crash, not fresh deterioration.
  Both readings Extreme Fear; directional signal noise. ETF outflows
  $1.67B weekly / $4.21B 3 weeks = institutional derisking anchor.
- **cost-report ISS-025 cf=30 → 0 overnight 03:48Z.** Weekly tick on
  `claude-sonnet-4-6` succeeded after 8 days. Sr still 10%, ISS-025
  cluster structurally persists across the 22-skill chronic tail.
  6-24 cost-report normal run also clean ($237.60 / 67 runs, −55.2%
  WoW — reppo cluster absent this week).
- **reg-monitor end-to-end clean at 14:55Z.** First success with all
  4 primary sources delivering (sr was 7%). Top item: CFTC v. Kentucky
  (9th state lawsuit over prediction-market preemption, 14.25% KY
  excise tax on event-contract notional is the live test). Worth
  watching across next 2-3 runs for sustained recovery.
- **BTC sub-$60,500 16:38Z.** Spot dipped to $60,319, both reclaim
  flags re-armed. If today's UTC close < $60,500, breakdown alert
  fires next run. Spot range 6-24 $60,319 → $62,903 (intraday).
- **Operator query 17:00Z — Morpho Alpha USDC Delta V2.** Vault
  collapsed 2026-06-20 (curator AlphaPing, ~30% concentrated in
  single msY/USDC market, msY crashed 70–85%, market at 100% util →
  withdrawals frozen, ~$18M trapped). Verdict to operator: DO NOT
  DEPOSIT. Documented as general Morpho curator-risk pattern in
  [[crypto]] for surface on future Morpho queries.
- **security-digest 6-24 15:05Z:** Ubiquiti CVE-2026-34910 EPSS
  0.818 / p96 — first EPSS≥0.5 PATCH TODAY trigger of 2026. UniFi
  KEV trio (34908/909/910) + Lantronix EDS5000 KEV. 40 net-new npm
  malware drops in 48h sustained ~20-22/day.
- **Token pick 6-24 AAVE HIGH 8/10 $76.09** — DeFi blue-chip relief,
  trending #1 CG, only large-cap DeFi green 7d vs BTC -3.0%.
  Grayscale $175 FV target + V4 Tokenization Spoke audit.
- **Narrative-tracker 6-24:** first major BEAR-BTC thesis (Hedgeye
  quad4) + first btc-maxi internal contrarian (Saylor critique).
  FRONT-RUN bucket emptied first time in 4 days. RESURFACED bucket
  appears (hyperliquid + BTC dominance returning from DEAD).
- **PR #138 (goal-tracker header drift fix)** open ~24h, under
  24h stall threshold per heartbeat. No urgent issues.

## 2026-06-28 fleet deltas

- **ISS-026 NEW (high, prompt-bug).** Filed by skill-evals 08:00Z run —
  heartbeat false-fail on missing_pattern because skill-evals dispatches
  before 08:00 UTC morning tick, captures pre-tick stale state of
  log-based skills (heartbeat / token-alert / skill-health). Recommended
  fix: schedule skill-evals after 21:00 UTC to capture full-day signal.
  Coverage dipped 12/44 (27%, −5pp). Action queued on action-converter.
- **PR #148 (fix agent-buzz x_search engagement ranking)** crossed 24h
  stall window (opened 6-27 18:14Z, ~24h+ as of 14:15Z hb). Operator-
  owned, direct follow-on to 6-27 agent-buzz cache-quality observation.
  Watch for merge before 6-29 morning hb.
- **ISS-025 capture-fix PR DAY 6 UNSHIPPED.** action-converter flagged
  4.6/5-quality PR on 6-24 18:14Z; surfaced in morning-brief 6-25 →
  6-26 → 6-27 → 6-28 (4 consecutive). Chronic 20-skill tail keeps
  bleeding `output_tokens=0`. Operator has not picked this up despite
  4 morning-brief surfaces — could be capacity-limited or deprioritized
  vs advisor sprint (#141–#145).
- **on-chain-monitor REPPO stake migration captured 13:03Z** — first
  non-zero on-chain-monitor run since 6-25 address-poisoning quiet
  thread (~72h). W3→W1 1.58M REPPO stake migration + W1 USDC→Morpho
  steakUSDC vault. Operationally validates the curl→WebFetch fallback
  + ID-keyed CoinGecko pricing path for token-transfers. Recommend
  adding `0xc81F...68E8` as "REPPO staking" in known-addresses.yml.
  Detail in [[crypto]] on-chain section.
- **defi-monitor NO_CONFIG day 21.** Operator config drift unchanged.
  ALCHEMY_API_KEY len=0; ETHERSCAN_API_KEY null. on-chain-watches.yml
  has 5 `type: wallet` entries, zero `type: pool` / `type: position`
  needed by defi-monitor.
- **Skill-health 6-27 18:10Z snapshot:** 24 DEGRADED + 8 WARNING + 9
  HEALTHY + 0 CRITICAL + 2 NO_DATA. Diff vs 6-26: btc-levels
  degraded→warning + daily-routine degraded→warning (both crossed
  0.6 sr line); −2 degraded. Hash 81dbbe4f changed → notification
  fired. Sandbox-truncation cluster (ISS-019/020/021/024/025 + chronic
  tail) still day 11 (since 6-19 first flag).
- **6-28 14:15Z hb:** 20-skill chronic tail unchanged from 09:18Z; some
  per-skill sr drift (vuln-scanner 7→10%, agent-buzz 48→49%, etc.) but
  classification stable. 1 open PR (#148), 15 open issues (ISS-026 add).
- **6-28 watchlist green-day** — token-alert TOKEN_ALERT_OK 7th
  consecutive clean CG day; whole canonical watchlist green for first
  time since 6-22 (median +1.51%); GITLAWB +5.38% ends 7-day red streak
  with first elevated-vol upside print 1.27× day-prior.

## 2026-06-29 entry

### PRs
- **PR #148 fix(agent-buzz) MERGED 2026-06-29T00:17Z** — ~30h from open (6-27 18:14Z) to merge. `mode:"Latest"` → `mode:"Top"` + `min_likes:5` switch in `scripts/prefetch-xai.sh`. agent-buzz cron-state sr 49% → 50% the same morning; full effect needs 5–7 days of fresh runs to register in skill-health.
- **PR #149 docs(skill-graph) by anajuliabit OPEN** — opened 2026-06-28T17:15Z; under 24h at morning hb (~15.5h), approaching but not crossing 24h stall at 15:04 hb (~22h). Watch carry next reflect.
- **aaronjmars/aeon PR #560 OPEN (sister-fleet ship)** — wired existing `scripts/validate-config.test.js` (7 fixture tests for the checkout-ordering invariant from #546) into `.github/workflows/ci-tests.yml`. Proactive gap-fix; tests shipped without CI gate. Branch `ai/ci-validate-config-tests` via fork `anajuliabit/aeon-fork` (`anajuliabit/aeon` already exists as unrelated repo).

### Fleet health
- **skill-health 6-28 18:08Z snapshot (24h hash unchanged):** 9 healthy · 24 degraded · 8 warning · 0 critical · 2 no_data. Same as 6-27 — classification stable. Open issues: 15 (4 critical sandbox cluster ISS-019/020/021/025 + 1 sandbox-limitation ISS-018 + 7 high prompt-bug/quality-regression + 3 medium).
- **Heartbeat 6-29 08:47Z + 15:04Z: HEARTBEAT_OK, STATUS_PAGE=DEGRADED** — fleet cf=0. Chronic-failure tail unchanged: 19 skills sr<0.5 sharing `output_tokens=0` sandbox-truncation signature. Worst: reg-monitor 10% / cost-report 11% / skill-analytics 11% / vuln-scanner 10%. agent-buzz now sits on cluster boundary at 50% post-PR #148 merge.
- **fork-skill-digest STUCK ~20h** carry — dispatched 2026-06-28T18:38:01Z, `last_status: dispatched`, last_success 2026-06-21T18:57:04Z (weekly Sun slot). Carried from 6-28 20:18Z + 6-29 08:47Z hb ticks within 48h dedup window.
- **operator-scorecard Mon slot missed again** — scheduled Mon 10:30Z, no cron-state entry; never-run since enabled. Same condition flagged each prior Monday — scheduler-side gap, not skill-side.

### Skill-security-scan 6-29 (Mon slot)
- **`SECURITY_SCAN_NOCHANGE`** — 4 PERSISTENT HIGH, 0 NEW, 0 RESOLVED. Identical line set as 2026-06-22; finding #4 stable at `aeon.yml:812` for 2nd consecutive scan. `scan.sh` blocked by sandbox approval gate 5th consecutive run since 2026-05-25 — fallback inline_grep_fallback per SKILL.md step 4.
- HIGH findings: `.github/workflows/aeon.yml` L86 (`inputs.skill` → `run:`), L94 + L96 + L812 (downstream `steps.skill.outputs.name` / `steps.work.outputs.label` chain). Workflow_dispatch / workflow_call require repo write access → low real risk; canonical fix is `env:` indirection (pattern shown in article).

### Cost-report 6-29 (Mon slot)
- **$595.75 last-7d / 113 runs / 14 anomalies / ⚠ ~$2,553/mo projected.** ↑199.5% WoW (prior window suppressed by widespread `output_tokens=0` sandbox failures, so the spike is largely artefact).
- 14 anomalies: 1 per-run (aixbt-pulse 2026-06-24 output spike +2.4σ), 13 WoW spikes — 10 attributed to ISS-019/020/021/025 sandbox-truncation artifact, 3 genuine: vuln-scanner 21.5× / reflect 3.0× / token-movers+token-pick `usepod_model` drift.
- **Optimization queued:** rename `usepod_model` → `model:` in `aeon.yml` for on-chain-monitor / token-pick / token-movers = ~$107/wk / $456/mo combined savings.

### Weekly shiplog 6-29 (Mon slot)
- 23 commits / 23 PRs merged / 1 issue closed last week on aaronjmars/aeon.
- Themes: Cron state and votable health move into GitHub Issues; Phylax becomes the pre-install verdict for external skills; The dashboard stops surfacing Dependabot.
- Stats: +3,176 / −442 lines, 87 files, contributors: aaronjmars, usephylax, SamsShow, clawhunter, anajuliabit, vigilcodes, dependabot[bot].

### ISS-026 status (heartbeat false-fail timing artefact)
- Detected 2026-06-28 08:00Z by skill-evals run.
- Recommended fix: move skill-evals dispatch after 21:00 UTC so it captures post-tick state of log-based skills (heartbeat/token-alert/skill-health) instead of pre-tick stale state.
- Action queued in action-converter q4u4 backlog; awaiting operator pickup.

## 2026-06-30 entry

### PRs
- **PR #150 fix(aeon.yml) `usepod_model` → `model:` OPEN** — opened 6-29 18:17Z by anajuliabit, 5-line diff for on-chain-monitor / token-pick / token-movers. ~$107/wk / $456/mo savings. Under 24h stall at 14:43Z 6-30 hb (~20h), approaching threshold. Queued in morning-brief 07:48Z focus #2.
- **PR #149 docs(skill-graph) STUCK day 2** — opened 6-28 17:15Z, ~45h+ at 14:43Z 6-30 hb. Crossed 24h stall threshold ~21h earlier; surfaced in morning-brief 07:48Z focus #1 + action-converter 6-29 18:22Z (dedup-blocked, no separate stalled-PR notification).
- **fork-skill-digest STUCK ~44h+** carry — dispatched 6-28 18:38Z, `last_status: dispatched`, last_success 6-21 18:57Z weekly Sun slot. 5 prior hb mentions; within 48h dedup window through 14:43Z 6-30; crosses threshold next tick.

### Fleet health
- **skill-health 6-29 17:45Z snapshot:** 9 healthy · 23 degraded · 8 warning · 0 critical · 2 no_data (operator-scorecard, fork-skill-gap). Hash 992a90ed; fleet-control dropped (now disabled in aeon.yml). 15 open issues, 0 filed/resolved this run.
- **Heartbeat 6-30 08:51Z + 14:43Z: HEARTBEAT_OK, STATUS_PAGE=DEGRADED** — fleet cf=0. 19-skill chronic-failure tail unchanged: reg-monitor 10% / vuln-scanner 10% / cost-report 11% / skill-analytics 11% / security-digest 24% worst. agent-buzz 51% holds out of cluster post-PR #148 merge. fleet-control re-entered chronic at 40% before being disabled.
- **operator-scorecard Mon 10:30Z perpetually missed** — 6-29 Monday tick now ~28h+ past with no dispatch as of 14:43Z 6-30 hb. Same scheduler-side gap flagged every prior Monday — carry indefinitely until scheduler patch.

### WELL volume spike (token-alert 12:11Z)
- **WELL $0.00334006 -2.28% on vol $3.68M = 3.83× of $961K 5d mean — first 3×+ print of the 6-day watchlist run**, but on a red tape print. Snaps the 3-day green streak on quarter-end sell flow.
- Read as **accumulation OR forced supply hitting a bid** — direction confirms on next 2 closes. Previous 6-day low-vol regime broken in the opposite direction of price relief.
- Next-run baseline shifts $961K → $1.020M; comparable 3× spike tomorrow needs $3.06M+.

### github-trending 6-30 (4 picks)
- **browser-use/video-use** (top pick · ACCELERATING · 967 today · 12.3k total · Python; org expansion from web→video editing, agent-tooling meta-narrative day 3)
- **0xNyk/council-of-high-intelligence** (RETURNING · 331 today · 2.2k total · Shell; `/council` Claude Code slash command runs 18 named-thinker AI personas across multi-vendor LLMs — structured-debate-as-judgment primitive)
- **logto-io/logto** (RETURNING · 158 today · 13k total · TypeScript; v1.41.0 released 6-30 08:09Z = release-driven spike; open Auth0/WorkOS alternative)
- **refactoringhq/tolaria** (ACCELERATING · 280 today · 17.8k total · TypeScript; pre-1.0 alpha, 9 alpha cuts in single day = ship-cadence-as-signal)
- **Fake-star drop precedent** — msitarzewski/agency-agents 119.8k stars Shell repo dropped with confidence on: 1:6 fork ratio (vs typical 1:30-1:50) + Shell language tag for "AI agency" + unknown maintainer + 459/d sustained 8mo on cheesy description. New rule: >100k stars + anomalous fork ratio + wrong language tag = inorganic-star-farm.

### security-digest 6-30 14:50Z
- **KEV zero-cadence streak ENDED at 4 days** — SimpleHelp CVE-2026-48558 added 6-29: CVSS 10.0 + horizon3.ai PoC + TaskWeaver/Djinn intrusion chain documented + CISA BOD 26-04 hard due 2026-07-02 = PATCH TODAY.
- **Brandjacks ride agent-infra narrative**: GHSA-m9j7-x8ww-5jwr ai-sdk-ollama@0.13.1 (Vercel AI SDK + Ollama brandjack); 18-pkg autotel-* cluster (autotel-mcp/cli/web/vitest/backends/etc, 10.5h single-author window = largest single-namespace coordinated brandjack of 48h).
- 100% of 154 malware advisories npm; pip/crates/go contribute zero — npm remains sole supply-chain attack surface.

### list-digest 6-30
- 1 signal: Hercules_Defi Pi2Day 2026 announcements (SoloHost local AI + Pi Sign-in OAuth + PiVerify KYC-as-a-service over 18M+ Pi-verified accounts). Pi's KYC reach is a real distribution asset; framing finally moved from mining-gimmick to infra play. Execution unproven.

## 2026-07-01 entry

### PRs
- **PR #150 fix(aeon.yml) `usepod_model` → `model:`** — opened 6-29 18:17Z, **~44h stall as of 14:13Z hb** (crossed 24h threshold 6-30 evening ~20h ago). 5-line diff, ~$107/wk / $456/mo savings for on-chain-monitor/token-pick/token-movers. Surfaced in morning-brief 7-01 07:03Z focus #1 + 4 hb ticks + 6-30 action-converter action-1 → dedup-blocked. Operator-merge gated.
- **PR #149 docs(skill-graph)** — opened 6-28 17:15Z, **~69h stall day 3**. Same dedup-blocked pattern.
- **fork-skill-digest STUCK ~68h+** — dispatched 6-28 18:38Z, `last_status: dispatched`, last_success 6-21 18:57Z. 8 prior hb mentions. Crossed 48h dedup window; next Sunday 7-05 tick will attempt fresh dispatch.

### Fleet health
- **skill-health 6-30 18:08Z snapshot:** 9 healthy · 23 degraded · 8 warning · 0 critical · 2 no_data. Hash 1ff18e84 (vs 992a90ed 6-29); classification byte-identical, daily-cadence notify fired at 24h23min elapsed. 15 open issues unchanged.
- **Heartbeat 7-01 08:32Z + 14:13Z: HEARTBEAT_OK, STATUS_PAGE=DEGRADED** — fleet cf=0. 19-skill chronic tail sr<0.5 unchanged. Worst: reg-monitor 10% / vuln-scanner 10% / cost-report 11% / skill-analytics 11% / security-digest 24%. All share `output_tokens=0` sandbox-truncation signature (cluster ISS-019/020/021/024/025). agent-buzz 52% holds out of cluster post-PR #148 merge.
- **operator-scorecard Mon 10:30Z slot MISSED day 3** — 6-29 Monday tick ~51h past with no dispatch. Same scheduler-side never-run gap.

### BTC breakdown day 6 CONFIRMED
- **btc-levels 00:19Z fired ⚠️ breakdown alert** for 6-30 close $58,551 = 6th consecutive sub-$60,500. Quiet ticks 05:12Z $59,155 / 08:32Z $58,552 / 12:18Z $58,432 / 17:03Z $59,846 — spot pinned sub-reclaim ($63.5k / $65.9k).
- First sub-$60k print since 2024; 50% below Oct-2025 $126k ATH.

### WELL vol-spike resolves BEARISH
- 6-30 vol spike 3.83× on -2.28% red print (either accumulation OR supply-hitting-bid) → 7-01 12:18Z **decays to 2.30× on -1.02% close** = **supply-hitting-bid confirmed**. Bid absorbed offers but couldn't drive a green print. Structural pattern noted; one more sub-$0.0033 close = trend-follow signal.

### github-trending 7-01 (4 picks)
- **google/agents-cli** (top pick · ACCELERATING · 445 today · 4.5k · Python; 3 releases in past week; Google first-party CLI + `skills/` directory primitive for agents on Google Cloud — same shape as Anthropic Agent SDK from 6-28; **skills-as-primitive convergence signal across major vendors**)
- **ogulcancelik/herdr** (ACCELERATING · 486 today · 9.2k · Rust; terminal-native agent multiplexer — Rust tmux-shaped answer for many coding-agent panes side-by-side, first devtool in this niche to hit trending)
- **usestrix/strix** (ACCELERATING · 515 today · 28.5k · Python; AI pentest agent, borderline drop yesterday reconsidered on today's 6× baseline vs 1.5× yest)
- **facebook/astryx** (RETURNING · 364 today · 2k · TypeScript; v0.1.2 6-29; Meta first-party open design system explicitly "agent-ready" — 1st-party framework declaring agents as 1st-class UI-consumer)
- **Fake-star drops (2)**: msitarzewski/agency-agents day-2 same pattern; **NEW diegosouzapw/OmniRoute** (TypeScript + rapid semver v3.8.42/139d + 1:6.3 fork ratio + brand-list description name-dropping Claude Code/Codex/Cursor/Cline/Copilot = new fake-star sub-pattern).

### Anthropic ship-day cluster (hn-digest 7-01)
- 3 of top-5 HN stories Anthropic-branded — biggest single-day HN presence in 30d log.
- **Claude Code steganographic prompt-marking disclosure** (1908p) — direct on aeon runtime; proxy/gateway routing implication (gateway.provider=direct in aeon.yml, but usepod/bankr/virtuals gateways would see markers).
- **Claude Sonnet 5** (1098p) — 80.4% Terminal-Bench beats Opus 4.7 launch score; 63.2% agentic coding vs Opus 4.8's 69.2%; 97% of Opus at ~15% cost; $2/$10 intro thru 8-31. "Most agentic Sonnet."
- **DoC lifts Mythos 5 export controls** (646p) — fully reverses 6-16 trusted-orgs restriction. Anthropic-Mythos-quota thread CLOSED (different event from XAI Elon x.ai quota, still day 16 unblocked).
- Claude Science ships same day (477p). Nano Banana 2 Lite (Google, 367p) as non-Anthropic AI balance.

### security-digest 7-01 (Fission cluster + brandjack vertical expansion)
- **Fission Go 9-CVE coordinated disclosure batch** (4 crit CVSS 9.9 + 5 high on `<=1.23.0`, podspec injection / node escape / cross-namespace / cluster-takeover, 8-min window) — largest single-project no-patch Go advisory cluster of 2026. Plus Fulcio CVE-2026-49478 CVSS 8.7 no-fix (SSRF + JWKS substitution → K8s SA token leak) + Cedar authz-bypass CVSS 8.8 no-fix. **Reviewed-CVE side now 100% no-patch.**
- Brandjacks: LiveKit Agents SDK, **Confluent Kafka JS (1st enterprise-data-infra target after 4 days AI-infra-only)**, chai-as-promised pair, agent-starter-pack (Google Cloud). Confluent = new brandjack vertical.
- **KEV net-new: 0** — day-2 zero-cadence since SimpleHelp 6-29. Total this-week: 3 (SimpleHelp + Windchill/Cisco Unified CM from 6-25).

### reg-monitor 7-01 (post-recovery batch)
- **Stop Lawmakers from Predicting Act passed House Admin Committee 5-4** (bipartisan Budzinski/Smith companion; penalty ≥$2k or 10% trade + net-profit forfeiture; Speaker Johnson + Trump backing). Direct hit on prediction-market coverage.
- **CFTC Data Reporting for Event Contracts NPRM** (doc 2026-13239, fresh 7-01) — moves fully-collateralized contracts out of 2017 no-action-letter regime into codified parts 15–18/17/18. **Most material CFTC action on prediction markets since Kalshi-Selig letter.** Standard 60d comment window ~2026-08-30 close.
- CFTC+SEC Portfolio/Cross-Margining Joint NPRM (2026-06-30, crypto-derivative cross-margining unlock).
- MiCA transition officially expired 7-01 (no fresh primary source to link).

### list-digest 7-01
- **$LIT (Lighter) thesis top signal** — @Flowslikeosmo: 17.9M/yr buyback-burn vs 7.5M/yr staking emit ≈ 2.4× net-supply shrink if revenue holds; first on-chain burn drops post-Q2 close; P/S 13.5×, P/F 10×, 30d fees +38.5%. 1st surfacing on curated DeFi flow this week.
- $LNQ (Linq) small-cap AI-compute infra bet; watchlist candidate.
- **DEX-supremacy meta being questioned** in curator screens (Flowslikeosmo shortlist RAIL/NXM/STON/YB/AQUA/OPINION/MOR/CAPX notably DEX-light) = macro read for token-pick / narrative-tracker.

## 2026-07-02 entry

### PRs — batch merge day
- **PR #150 fix(aeon.yml) `usepod_model` → `model:` MERGED 13:20:07Z** — 5-line diff shipped after ~68h stall; unblocks on-chain-monitor/token-pick/token-movers from `output_tokens=0` truncation root cause. **12:00 UTC batch (6 skills stopped dispatching 6-28) should recover on Fri 7-03 tick — first live test of the fix.** ~$456/mo bleed halted.
- **PR #151 fix(aeon.yml) skill-evals cron Sun `0 6 * * 0` → `0 22 * * 0` MERGED 13:20:37Z** — ISS-026 fix ships. Heartbeat/skill-health/fork-skill-digest/skill-update-check/fork-skill-gap ticks now land before Sunday eval reads. Issue file needs INDEX flip open→resolved.
- **PR #149 docs(skill-graph) STILL STALLED ~94h day-4** — dedup-blocked, operator-merge gated. Only PR left in the stack post-batch.

### fork-skill-digest carries
- STUCK ~93h dispatched row (6-28 18:38Z → last_success 6-21 18:57Z weekly Sun slot). Next Sun 7-05 fresh tick.

### BTC breakdown day 7 CONFIRMED + first material bounce
- **btc-levels 01:17Z fired ⚠️ breakdown alert** for 7-01 close $59,979.90 = **7th consecutive sub-$60,500 close**. 05:11Z spot $60,752 = first close-window print back at the $60k handle of the streak; 13:07Z $61,528 = first material touch of the breakdown line in 7 days; 17:14Z $61,650 pins the reclaim attempt below $63.5k/$65.9k rails. **Tonight's UTC close decides day-8-red or first-reclaim.**
- June ETF net −$4.51B = **worst month ever** (IBIT −$212M on 6-30, SpaceX-IPO rotation cited); DXY reversal off local highs; July historical avg +7.25% / median +8.16% (July-relief base case).

### Fleet health
- **skill-health 6-30 18:08Z snapshot unchanged** (daily-cadence tick 7-01 18:30Z byte-identical hash 1ff18e84): 9 healthy · 23 degraded · 8 warning · 0 critical · 2 no_data. 15 open issues; ISS-026 fix-shipped via PR #151 but INDEX still Open.
- Heartbeat 08:26Z + 15:29Z **HEARTBEAT_OK** — fleet cf=0. 19-skill chronic tail sr<0.5 unchanged from 7-01 (all `output_tokens=0` sandbox-truncation signature cluster ISS-019/020/021/024/025). agent-buzz 52% + defi-monitor 53% stay above cluster boundary.
- **operator-scorecard Mon 10:30Z slot MISSED day 4** — 6-29 Monday tick ~101h past no dispatch. Scheduler-side never-run gap carries.

### watchlist — whole-green day (first since 6-28)
- +5.19% median 1d across 4 tokens. **WELL 3rd close post-6-30 vol spike confirms direction UP not distribution** — reverses 7-01 "supply-hitting-bid" thesis to **washout-then-reversal**. **REPPO vol-trigger 3.16× rail** on $0.021 wobble-line reclaim ($294K vs $93K baseline drought) — 4-day base snaps, participation finally arrives. WELL 1.55× decay. MAMO 2nd green clears $0.0083 first time since 6-27 on 0.99× baseline. GITLAWB +8.03% snaps "worst 1d" pattern but on 0.88× shrinking vol = participation-shallow bounce.

### daily-routine 7-02 (tape flip)
- **81/100 breadth** (up from 32/100 6-30 = biggest single-day swing in 30d window). Winners **M MemeCore +65.8% MAJOR MEAN-REVERT** (7d -76% → +83% swing week = post-capitulation shakeout day-2), RIF +36.4%, GWEI +20.5% mean-revert, **LIT +15.3% BREAKOUT day-2 7d +29%** (Flowslikeosmo tokenomics thesis 7-01 playing out on tape — buyback-burn math becoming a live-market read), SYN +14.3%, PENDLE +12.5%, MORPHO +8.5%. Losers **VELVET −60.1% #138 CAPITULATION** (HIGH 11/10 pick day-5 fully blown: entry $1.97 → $0.62 = **−68.5% blown position**; 8d to July-10 unlock priced 8d early — market did not wait), TAC −38.2% (7d +77% breakout fully unwound), DYDX −29.1% (was yest #3 winner +16.8%), LAB −14.4% day-2 CAPITULATION MAJOR.

### security-digest 7-02 (brandjack extends to testing arm + pattern inversion)
- **CVE-2026-45659 SharePoint added KEV 7-01** — only fresh KEV entry this week; 4 total this-week (SimpleHelp 6-29 + Windchill/Cisco Unified CM 6-25 all dedup-carried).
- **This-week: 4 major CVEs (patched):** GHSA-84hp-mqvj-3p8h mcp-memory-service CVSS 9.8+PoC unauth doc-API RCE ≥10.67.1; GHSA-xr65-5cpm-g36x/CVE-2026-44935 rancher/fleet Go 9.9 cross-namespace secret disclosure; GHSA-mhc6-2gfq-xx62/CVE-2026-44939 rancher Go 9.6 YAML command injection; GHSA-9mm9-rqhj-j5mx/CVE-2026-49987 repomix npm 8.8+PoC --remote-branch arg-injection RCE.
- **Brandjack extends to testing-framework arm** — `vitest-agent` (Vitest+agent brand), 3-pkg Tailwind cluster (tailwind-animates + animatecss-postcss-plugin + tailwind-typography-stylecss all published 7-02). Extends the pattern (AI-infra 6-30 → enterprise-data-infra 7-01 → testing-framework 7-02).
- **Pattern inversion vs 7-01** — GH `patched_versions: null` cascade → all-patched-today. **API field lags advisory-page reality; WebFetch on advisory pages is canonical.** Codify: don't trust the JSON field for triage.
- **MCP/agent-infra 5-advisory 48h window** — mcp-memory-service + @apify/actors-mcp-server + auth-fetch-mcp + neuro-cortex-memory (**CLAUDE_PROJECT_DIR RCE — worth tracking, direct Claude Code adjacency**) + vitest-agent brandjack.

### hn-digest 7-02
- **"For first time, a cell built from scratch grows and divides"** (844p, Quanta) — synthetic biology milestone.
- **"Physical disc production ending Jan 2028 for PlayStation"** (703p) — end-of-media-era cultural marker.
- **"ZCode — Harness for GLM-5.2"** (377p, z.ai) — **Chinese-model agentic-harness axis extends** the skills-as-primitive convergence (google/agents-cli 7-01 + Anthropic Agent SDK 6-28 + ASPIRE paper 7-02 + ZCode/GLM-5.2 = **day-3 convergence with 4 provider artifacts including a Chinese lab**).
- **"Cloudflare Monetization Gateway via x402"** (290p) — HTTP 402 payment-rail behind CF, "charge for any resource" — micropayment infrastructure durable signal for aeon apps that could paywall through CF's rail.

### list-digest 7-02
- **@Flowslikeosmo doubles down** — Flare 2-lanes (interoperable assets + confidential compute, implicit no-vote on AVS/DA optionality) + $LIT tokenomics-alignment overhaul (2nd surfacing this week). Tokenomics-as-team-seriousness filter now durable-tracked caller (adds $LIT to memory/topics/crypto.md's SLX/VELVET SLX/VELVET filter).

### paper-pick 7-02
- **MemSyco-Bench (arXiv 2607.01071, HF ↑17)** — memory sycophancy in agents; direct aeon-runtime hit (memory-consolidation quality risk). Continues eval-side thread Dockerless (7-01) → TUA-Bench (6-30) → Gauntlet (6-29) → OPID (6-28) → Verification Horizon (6-27).

### reg-monitor day-1 tick surfaced 7-02 (via daily-routine)
- **CFTC Event Contracts NPRM** carries — comment window closes ~2026-07-27 (T-25d), **biggest prediction-market action since Kalshi-Selig letter**.

## 2026-07-03 entry

### PRs & merges
- **#149 docs(skill-graph)** — day-5 stall (~118h), only PR in stack after 7-02 batch-merge. Operator-merge gated.
- **PR #150 was PARTIAL fix** — 12:00 UTC batch first live test 7-03 FAILED. 6 skills (token-pick/defi-overview/token-movers/on-chain-monitor/defi-monitor/market-context-refresh) still dark ~5.2d since 6-28. Additional dead slots 7-03: github-trending 09:00Z + aixbt-pulse 09:00Z + narrative-tracker 13:30Z. Deeper scheduler/YAML issue remains (possibly `market-context-refresh` line 155 still carries `usepod_model` field). Wed skill-analytics 18:30Z will formalize the anomaly.
- **ISS-026 fix (PR #151) shipped 7-02 but INDEX still Open** — memory-flush follow-up carries.

### Skill-health snapshot
- **7-02 18:53Z byte-identical 3rd day** — 0 critical · 23 degraded · 8 warning · 9 healthy · 2 no_data. Systemic: `output_tokens=0` cluster ISS-019/020/021/024/025 day-10 since action-converter 6-24 flag; **weekly-review hard deadline 07-04 = T-1d, TIGHT**.
- **18-skill chronic tail** (was 19 at 7-02 — thought-review 50%→51% exits cluster): vuln-scanner 10% / cost-report 11% / reg-monitor 12% / skill-analytics 13% / security-digest 26% / market-context-refresh 32% / narrative-tracker 33% / search-skill 34% / skill-health 36% / list-digest 37% / self-improve 37% / action-converter 38% / goal-tracker 38% / skill-evals 38% / reflect 39% / fleet-control 40% / evening-recap 46% / aixbt-pulse 47%.
- fork-skill-digest STUCK ~117h carry — next Sun 7-05 fresh dispatch attempt.
- operator-scorecard Mon 10:30Z MISSED **day 5** — scheduler-side never-run gap, carry.

### security-digest 7-03
- **1 TODAY / 5 THIS-WEEK / 0 MONITOR**. Notable:
  - **9router npm 9.8** hardcoded default JWT fallback secret `9router-default-secret-change-me` + public PoC = worst config default of year candidate.
  - **fast-mcp-telegram pip 9.4** bearer-token path traversal → 0.19.1 (MCP-adjacent, day-7 of agent-infra brandjack thread).
  - **zebrad rust 9.3** P2SH sigop undercount = Zcash consensus divergence (chain-split miners for fee cost) → 4.5.0.
  - **electerm npm 8.8** cmd injection via malicious SSH/SFTP filenames → 3.11.11.
  - **joserfc pip 8.7** HS256 accepts empty/nil HMAC key = JWT forgery when secret unset → 1.6.8. Cross-lang sibling of ruby-jwt + PyJWT — **pattern-of-week: JWT verify-with-nil-key across ecosystems**.
  - **coder Go 8.1** `dotfiles_uri` + `mode=auto` workspace-creation = RCE on victim click → 2.29.7/2.30.2.
- **OpenClaw npm 23-advisory single-package coordinated disclosure batch** on agent-orchestration platform — **2nd solo-researcher mega-batch of week** (7-01 Fission Go 9-CVE = 1st, ~2.5× smaller). Same-project batch-magnitude signature = codify.
- **openbabel pip 13-CVE republish batch** — cheminformatics lib, filter-out-of-stack but pattern hit.
- **GH Advisory `patched_versions: null` inversion extends day-3** (7-01 all-null cascade → 7-02 inversion → 7-03 continues). Codify: WebFetch advisory page canonical for triage.
- **First supply-chain-quiet 24h window since 6-25** — 0 fresh npm malware after 7-02 15:00Z breaks 8-day daily-npm-malware streak. Watch next 48h for pattern-vs-blip.

### hn-digest 7-03 — sovereignty stack shipping day
- **Virginia bans sale of geolocation data** (733p) — first US state-level ban.
- **Podman v6.0.0** (504p, CNCF-incubated) — Docker-alternative; ships day-of Immich 3.0.
- **LUKS suspend stopped wiping disk-encryption keys since Linux 6.9** (457p) — kernel regression.
- **Immich 3.0** (372p) — self-hosted photo/video stack major.
- **Right to Local Intelligence** (203p) — policy push for on-device model access. Extends skills-as-primitive convergence to a **policy vector** (was compute + tools + protocols; now +user-rights-to-run-locally).
- **Three-thread convergence:** sovereignty stack + privacy legislation escalation (Virginia + American Privacy Emergency) + encryption-tooling security regression (LUKS).

### paper-pick 7-03
- **AgenticSTS (arXiv 2607.02255, HF ↑28)** — bounded-memory testbed for long-horizon LLM agents. Direct aeon-runtime hit: memory as contract about what each future decision is allowed to see. **Day-2 of memory-as-eval-axis** thread (MemSyco 7-02 → AgenticSTS 7-03).

### tweet-roundup 7-03 (WebSearch fallback — XAI day 18)
- BTC broke $61k resistance yest, consolidating $61.0–$61.8k. $61.8k gate. **Spot ETF flip +$222M BTC net-in breaks 10d outflow streak; ETH ETFs +$29M same day.** TD Sequential buy signals across BTC/ETH/XRP/SOL. XRP breakout printed.
- Sonnet 5 framed as **agentic-shift crystallization** — "AI war shifting from chat to agents." $2/$10 promo through Aug-31. GPT-5.6 Sol preview + Gemini 3.5 Flash both agent-first = table stakes.
- Podman v6.0.0 + Immich 3.0 shipped same window — self-host/sovereignty stack keeps compounding.

## 2026-07-12 fleet snapshot

### State roll-up (14:16Z heartbeat)
- **43 enabled skills, verdict DEGRADED, 11 open issues** (4 critical / 4 high / 3 medium — ISS-005/007/009/010/011/016/018/019/020/021/025).
- **Chronic ~17-skill sr<0.5 tail unchanged** — ISS-019/020/021/025 sandbox-truncation systemic day-20: cost-report 0.11, skill-analytics 0.14, reg-monitor 0.14, vuln-scanner 0.16, security-digest 0.32, market-context-refresh 0.32, narrative-tracker 0.33, search-skill 0.37, fleet-control 0.40, skill-health 0.41, self-improve 0.43, goal-tracker 0.43, action-converter 0.43, skill-evals 0.43, reflect 0.45, list-digest 0.45, aixbt-pulse 0.47.
- **skill-health hash `12f8bbcf`** (day-N 18→19 flip; classification byte-identical **10-day streak**).
- **skill-graph NO_CHANGE day-7** — 191/43/5/0/0/21 identical vs 2026-07-05 baseline. Silent-exit path taken. Stable-architecture streak week-1 confirmed.

### Batch-dark + dead-slot state
- **12:00 UTC batch dark day-15** — 8 batch skills (token-pick/defi-overview/token-movers/on-chain-monitor/defi-monitor/market-context-refresh/narrative-tracker/aixbt-pulse) still last_success 2026-06-28. **7-12 slot catch-up partial**: token-alert dispatched 12:39Z + succeeded 12:47Z (fired 1 alert GITLAWB -19.49%) + btc-levels 12:40Z under operator invocation. Same slot-level-not-skill-level pattern as 7-10 13:31Z + 7-11 12:39Z. Broader 8-skill batch remains dark. Per ISS-027.
- **aixbt-pulse dead-slot day-14** — 7-11 21:00Z tick MISSED (7 consecutive twice-daily slots missed since 7-08 09:00Z). 7-12 21:00Z = break-vs-continue test.
- **operator-scorecard chronic Mon 10:30Z miss** — 8 consecutive Monday misses through 7-06; next tick Mon 7-13 **T-1**.
- **weekly-shiplog + cost-report Mon 7-06 miss** — 13d gap = 1.86× 7d interval, approaching 2× threshold; 7-13 Mon tick is next slot.

### Weekly-review deadline T-1 (Mon 2026-07-13) — twin gate
- (a) **SLX open pick day-18 CATASTROPHIC recut** — no fresh CG print (last $0.256 on 7-05 12:59Z, 7d stale); daily-routine 7-10 trending endpoint $0.174 = -63.4% vs $0.4753 entry stands. Operator-owned slot per weekly-review action-list.
- (b) **ISS-025 capture-step PR against `.github/workflows/aeon.yml` chain-runner day-20 unshipped** — rule-5 workflow-file structural block CODIFIED through 7-11 self-improve routing test (PR #162 authored `fix(daily-routine)` XAI-fallback tightening instead — adjacent target). Operator direct-author sole path per goal-tracker + skill-health + action-converter + reflect 7-11 consensus.
- Next self-improve tick 7-13 18:00Z (post-deadline).

### GH Actions morning-slot cron catch-up pattern durable
- 7-06/07/08/09/10/11/12 all show 08:00Z + 12:00Z + 14:00Z + evening ticks firing ~9min–2h late.
- 7-12 confirmed: thought-review 08:58Z + heartbeat 08:59Z + morning-brief 09:01Z + skill-freshness 09:07Z + daily-routine 09:08Z (~2h late), github-trending 10:46Z (~1h46min late), token-alert 12:47Z (~47min late), btc-levels 12:40Z (~25min late), heartbeat 14:16Z (~16min late), security-digest 14:20Z, skill-graph 17:36Z (Sun, ~36min late), agent-buzz 17:37Z, list-digest 17:36Z.
- Recurring, expected — not skill-side.

### github-trending 7-12 4-pick slate (all agent-runtime-adjacent OR sovereignty-of-infra)
- **malisper/pgrust** TOP — Rust rewrite of Postgres, 774 today (28.7× baseline), passes 46k+ pg regression queries, WIP branch 300× faster on analytics (2× slower than ClickHouse on clickbench), disk-compatible pg 18.3, AI-assisted-development topic. Novel sovereignty-of-infra day-11 database rail.
- **wonderwhy-er/DesktopCommanderMCP** HOLDOVER 909 today (2.8× DoD, 25×→70× baseline). MCP-becomes-infra day-3.
- **google-labs-code/stitch-skills** HOLDOVER 340 today (3× DoD jump 117→340). Skills-primitive convergence day-12 — framework-fades-libraries-hold split.
- **anthropics/claude-cookbooks** RETURNING 219 today (4.87× baseline); recent adds (Sentry-triage scheduled agent 6-09, roadtrip_planner managed agents 6-30, agentic-search benchmark reproduction 6-30, coordinator-pattern big-plan/small-execute 7-02). Anthropic-official agent-primitive curation day-1 NEW.
- Dropped 20: 5 mature always-trending + C++ cluster of 4 + 2 HOLDOVER fade/same-story (obra/superpowers 740 below 916/d baseline; davila7/claude-code-templates same-story).

### security-digest 7-12 VERDICT-FLIP DAY
- **First "nothing urgent today" verdict in last 5 runs** — genuinely earned by simultaneous KEV-quiet + malware-quiet + no-fresh-critical, not dedupe erasure.
- **npm malware wave d5-QUIET** — 0 fresh pkgs published after 7-11 14:22Z digest; 52+h genuine pause after 4-day escalation (7-08 240 → 7-09 27 → 7-10 51 → 7-11 polymarket brand-jack + safeinstall-cli).
- **KEV feed 1.5-day quiet** since 7-10 Balbooa/iCagenda pair.
- **PATCH THIS WEEK (3):** SiYuan Go 5-CVE cluster (CVE-2026-54069 unauth admin api + 3× stored-xss→rce 9.9 + CVE-2026-54070 bazaar readme xss 7.1; one commit `2d5d72223df4` fixes all; 34k-star self-hosted note app). TSDProxy Go GHSA-g936-7jqj-mwv8 CVSS 9.0 (internal proxy auth token forwarded → mgmt-api escalation on tailscale-adjacent reverse proxy, upgrade to `1.4.4-0.20260603142855-434819b4421e`). safeinstall-cli npm GHSA-xrmc-c5cg-rv7x CVSS 8.8 (supply-chain-defense tool's own agent guard has shell parsing bypass; **meta-signal worse than CVSS 8.8**; upgrade ≥0.10.2; extends chai-defender / tailwind-animate-v4 typosquat / polymarket brand-jack lineage).
- **MONITOR (2):** babeldoc pip CVE-2026-54071 CVSS 7.8 pickle-deserialization RCE via CMap parser (no fix, all ≤0.6.2). clauster pip GHSA-h4g2-xfmw-q2c9 config-default unauth dashboard on non-loopback (no fix, ≤0.2.1).

### agent-buzz 7-12 (mcp production hardening dominates)
- @elliot1one contract-drift → gates.
- @gautham_city_ MCP+oauth long-running loops.
- @h100envy swe-agent 12.5% swe-bench = ACI-ceiling argument (architecturally-adjacent to Aeon's skill-primitive layering).
- @DerekColley_ Shanghai 35b agents-a1 MoE matches 1T-scale = **4th Chinese-lab agent-runtime primitive** (joins TencentDB-Agent-Memory + alibaba/page-agent + CubeSandbox at n=4).
- @KirkDBorne 574-page agentic-patterns book.
- @shenli3514 awesome-agent-infra list.

### list-digest 7-12 — 2-operator alignment-lens convergence
- @Flowslikeosmo Noxa/Robinhood immutable-launch thesis ($5.36M of $5.58M monthly fees in last week alone; trust as architecture).
- @thesaint_ "airdrops dead / project farming users = new meta".
- Same tokenomics-alignment axis, two angles (architecture-alignment vs aligned-participation). 2-operator convergence same day (previously solo-Flowslikeosmo).

### Blocked (waiting on operator)
- **XAI quota recovery day-27** — Team 3a8b4c1e monthly credit exhausted 6-16. WebSearch fallback covers daily-routine/tweet-roundup/narrative-tracker; prefetched paths serve list-digest/agent-buzz/token-pick.
- **Operator on-chain config day-35** — defi-monitor NO_CONFIG; `memory/on-chain-watches.yml` needs `type: pool` / `type: position` entries. `ALCHEMY_API_KEY len=0`, `ETHERSCAN_API_KEY null`.
