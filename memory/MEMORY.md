# Long-term Memory
*Last consolidated: 2026-08-10*

## Current Goals
- **ISS-030 cost-report 8-10 Mon 07Z deciding-test T-0 TODAY** — 8-04 21:48Z same-day organic recovery holds; chronic sr=10%; signature `sdk_opt_in_required` cleared organically. Clean → RESOLVED same-day candidate; fail same-signature → 4-consec-week formal-pattern. See [[iss-030]].
- **`chronic-cohort-alone-degraded` regime 12-consec-heartbeat-tick ~125h span 8-04 14:45Z → 8-09 20:14Z (8th 24h durability gate crossed 8-09 20Z)** — 10-skill chronic sub-50% cohort composition-locked: cost-report 10% / skill-analytics 21% / reg-monitor 21% / vuln-scanner 25% / market-context-refresh 32% / narrative-tracker 33% / search-skill 38% / fleet-control 40% (disabled) / security-digest 45% / aixbt-pulse 47%. Deepest composition-identity print in memory-window.
- **fork-cohort STUCK 8-09 20Z — NEW P0 novel signal** — first fork-cohort stall of memory-window; state-update-race on cancelled workflow (run 31330721650 hit 30-min "Run" step timeout at 19:35:47Z, but "Update cron state" step conclusion=success did NOT clear the dispatched marker). Last success 2026-08-02T19:52:59Z. Weekly-review 8-10 T-0 root-cause investigation candidate — check if commit-results/update-cron-state steps handle cancellation; file as new ISS if not.
- **ISS-028 workaround-chain n=38+ durable 18-UTC-day span 7-22 → 8-09** — 5 fresh 8-09 call-sites (daily-routine tweet-roundup + github-trending Edit-tool 2-step + token-alert Write+Edit-append + heartbeat 14:44Z + agent-buzz + heartbeat 20:14Z + goal-tracker + skill-health). PR #177 opened 8-09 18:18Z documenting sandbox-block in CLAUDE.md. Sibling bash-redirect-block + heredoc-parser-over-length family stable. Weekly-review 8-10 T-0 reopens root-cause investigation.
- **12:00 UTC batch DARK day-44 on 8-10** — ISS-027 8-skill cluster frozen since 2026-06-28; scheduler-side gap not CG infra. Token-alert 12Z slot fires 4-consec clean 8-06→8-09 confirming `[[12Z-slot-dark-immunity-per-skill]]` per-dispatcher-path. 8-10 12Z = 5-consec-candidate.
- **PR queue at 3 on 8-09 20Z (post Sunday-batch)** — #174 (Advisor Brier-weight, ~44h+, mergeable=UNKNOWN + empty statusCheckRollup, CI never fired), **#176 fresh (skill-graph regen `EDGES_TOTAL: 32→74`, opened 17:10Z by skill-graph Sunday-fire, ~3h at 20Z heartbeat)**, **#177 fresh (fix(claude-md) ISS-028 file-redirect sandbox-block doc, opened 18:18Z by self-improve 18:14Z run, ~2h at 20Z heartbeat)**. Queue-full self-improve exit-gate stays DISENGAGED (only #177 counts as self-improve, n=1 < 3).
- **Operator on-chain config day-65 on 8-10** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Operator-gated.
- **priorities.md 67d stale on 8-10** — last reviewed 2026-06-04. Vault inbox 50d cold streak (last real capture 2026-06-21T08:32Z). Weekly-review 8-10 T-0 refresh-ask.
- **weekly-shiplog 8-10 09Z T-0** — 20d stale (last_success 2026-07-20T10:55Z) = 3× 7d-schedule miss; Mon 09Z tick today decides if scheduler auto-fires or requires manual seed.

## Recently Cleared (8-09)
- **PR queue COLLAPSES 5 → 1 → 3 via operator Sunday-batch T-0 8-09** — #173 merged 11:15Z (squash `f866fd3770`); #172 rebuilt CI-clean 11:50Z; #165 rebuilt CI-clean 13:09Z. **NEW `[[pre-squash-history-rebuild-recipe]]` observation** — all 3 PRs had pre-squash history problem (main squashed to single commit `e6da7438`; PR heads carried pre-squash → merge-base empty); fix = fresh branch off main + cherry-pick load-bearing + force-push-with-lease. Late-day churn (#176 + #177 both fresh Sunday-scheduled) rebounds queue to 3.
- **`[[morning-08Z-slot-dark]]` PATTERN-BROKEN-PERMANENT VERDICT confirmed 8-09** — heartbeat 08:06Z (3min lag) + skill-freshness 08:17Z clean = 2-consec-clean at 08Z slot. `[[heartbeat-dispatch-lag]]` 08Z-slot sequence 31→50→50→75→75→4→3min = collapsed-and-held. Watchpoint retired from active-tracking.
- **chronic-cohort-alone-degraded 8th 24h durability gate crossed 8-09 20:14Z (12-consec-tick ~125h span)** — composition identity unchanged across 5 UTC-days.
- **Fleet clean-consec d4 → d5 crossing 8-09** — unbroken since 8-04 21:48Z. All 43 enabled skills consec=0 at 08:03Z + 14:44Z + 20:14Z heartbeat ticks.
- **Token-alert 4/4 shape-inflection print 8-09 (rare all-tokens event)** — WELL cliff-candidate FAILS (single-glitch confirmed via 4.892× snap-back vol); MAMO asymptotic-approach RESOLVES via baseline-crossing (9-consec sub-baseline breaks at n=9); REPPO spent-flush CONTINUES as drought (0.537× baseline); GITLAWB 5-phase → 6-phase arc via breakdown-resumption (-8.05% on 0.823× vol). CG clean-day d47.
- **BTW `[[same-coin-48h-reflip]]` n=3 candidate 8-09 via 6-day pole-inversion continuation** — 8-04 +9.62% → 8-09 +28.8%. Rail promotion deciding-test 8-10.
- **github-trending sub-25 rail 12-consec + n=12 NEW low-edge print 8-09** — first n=12 in memory-window. `PrimeIntellect-ai/prime-agent` day-2 top-pick +8% soft-sustain (NEW `[[soft-sustain-2-consec-top-pick]]` sub-shape n=1). `google/skills` day-2 +47% (`[[skill-pack-primitive-rail]]` day-2 accel n=2). Per-repo viral-arc caps at ~3 days.
- **cloudflare/computer 4-consec-day trending run ENDS 8-09** — first memory-window "top-pick 3-day-then-departure" arc closes.
- **`[[fleet-relevance agent-thesis]]` rail 24 → 25-consec-day 8-09** — double-axis via paper-pick (Agentic Economies ↑28, first sherwood-tier paper of memory-window) + github-trending (prime-agent + google/skills).
- **NEW security sub-classes 8-09**: `[[SvelteKit-brand-typosquat-cluster]]` n=1 (4-pkg 90-sec span); `[[statist-browser-typed-client cluster]]` n=1 (7-pkg same-second corp-scope); `[[cross-ecosystem-malware-escalation]]` n=1 (pip:riakcs first pip-ecosystem malicious in 322-pkg npm-wave).
- **`[[single-project-mass-disclose]]` rail n=3 → n=4 8-09** — CodeIgniter 3-GHSA joins GitPython + Traefik + Flowise.
- **Aeon-fleet clean d9 → d10 vs security-digest surface 8-09** — deepest clean-streak in memory-window on defensive-import axis. EPSS-skip 8-09 = 1st EPSS-skipped digest.
- **NEW `[[claude-competitive-benchmark-print]]` sub-shape candidate n=1 8-09 (agent-buzz)** — Qwen 3.8 Max at 58 Agentic Index vs Claude Fable 5 at 57, 5-8× cheaper. Fleet-meta-relevant.
- **NEW `[[dario-public-endorsement-of-own-product]]` observation n=1 8-09** — same-day pincer with claude-competitive-benchmark-print.
- **`[[xai-cache-window-narrows]]` n=3 datapoint via cache-side 8-09** — 15-min window 23:45-23:59Z 8-08. Rail promotion candidate 8-10.
- **`[[agent-buzz-engagement-drought]]` rail 5 → 6-consec-day 8-09** — top-survivor engagement 113 raw.
- **fork-skill-digest 8-09 19Z** — configured forks 32% (down from 49% last week — 18 prior-run signals FADED); 23 fork-only skills (16 prior + 7 new). Heaviest customizer Aluma/aeon (~39 overrides). bspacer shipped robinhood-mcp/aeon-doctor/seo-audit/you-web-search (not upstream). NEW `[[fork-signal-fade-collapse]]` sub-shape candidate n=1 (98%→32% configured-forks in 1 week).

## Fleet Health
See [[fleet]] for full snapshot. **skill-health hash `71d8c76e` 8-09 18:17Z composition-unchanged reminder tick** (composition IDENTICAL to 8-08 18:05Z `91a4634d`): 0 CRITICAL · 17 DEGRADED · 15 WARNING · 8 HEALTHY · 3 NO_DATA · 14 open issues. **chronic-cohort-alone-degraded** regime 12-consec-heartbeat-tick ~125h span 8-04 14:45Z → 8-09 20:14Z (8th 24h durability gate crossed 8-09 20Z). **fork-cohort STUCK 8-09 20Z NOVEL P0** (first stall of memory-window; state-update-race on cancelled workflow). **Fleet clean-consec d5 crossing 8-09** all-day. ISS-028 workaround-chain **n=38+ 18-UTC-day span 7-22 → 8-09** (5+ fresh 8-09 call-sites). ISS-027 batch-dark d43 → d44 on 8-10. **`[[12Z-slot-dark-immunity-per-skill]]` extends to 4-consec** (token-alert clean while ISS-027 cluster dark). PR queue **5 → 1 → 3** via operator Sunday-batch T-0 (#173 merged, #172/#165 rebuilt clean) + Sunday-scheduled churn (#176 skill-graph regen + #177 self-improve ISS-028 doc). weekly-shiplog 20d stale 8-10 09Z T-0 today.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, weekly-batch cadence, positive events log.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns.
- [Market context](topics/market-context.md) — Baseline snapshot (STALE ~25d/600h, crossed 2× threshold 8-01; refresh chained on next batch-dark thaw or manual invoke).
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. Last snapshot 8-09 12:02Z: **0/4 alerts** (2-consec clean fire post-8-07 memory-window-first 2/4 multi-token fire). CG clean-day d47 unbroken. **Rare 4/4 shape-inflection print 8-09** — every token sees a shape-resolution or continuation-verdict: WELL cliff-candidate FAILS (single-glitch confirmed on 4.892× snap-back vol); MAMO asymptotic-approach RESOLVES via baseline-crossing (9-consec sub-baseline streak breaks at n=9); REPPO spent-flush CONTINUES as drought; GITLAWB 5-phase → 6-phase arc via breakdown-resumption.

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 8-09 -3.04%, vol $779K = 1.342× baseline (**cliff-candidate FAILS at n=1 — single-glitch confirmed**; 4.892× yesterday-vol snap-back = biggest single-day vol rebound of memory-window; 4-day arc $664K→$999K→$988K→$159K→$779K terminates via snap-back-to-above-baseline) |
| MAMO    | mamo               | 15%           | 8-09 +0.10%, vol $699K = 1.006× baseline (**asymptotic-approach RESOLVES via baseline-crossing**; 9-consec sub-baseline streak breaks at n=9 with 1st above-baseline print; digestion band d19 tightest print at |+0.10%|) |
| REPPO   | reppo              | 15%           | 8-09 -6.51%, vol $79K = 0.537× baseline (**spent-flush CONTINUES as drought**; 2nd-consec sub-baseline post-spike; 3-day arc: 4.854× → 0.709× → 0.537× = spike → flush → drought) |
| GITLAWB | gitlawb            | 15%           | 8-09 -8.05%, vol $171K = 0.823× baseline (**consolidation FAILS → breakdown-resumption**; 5-phase arc extends to 6-phase; closest-to-threshold print today at 54% of rail) |

## Recurring patterns (durable — brief pointers; details in topic files)
- **`[[same-coin-48h-reflip]]` n=3 candidate 8-09** — BTW 6-day pole-inversion. Rail promotion deciding-test 8-10.
- **`[[fleet-relevance agent-thesis]]` rail 25-consec-day 8-09** — double-axis paper + github-trending same UTC-day.
- **`[[MCP-enforcement-primitive-cluster]]` rail 5-consec-UTC-day 8-05** — three "rules-at-boundary" variants same-day. No 8-06→8-09 refresh.
- **`[[memory-primitive-paper streak]]` 7-consec-UTC-day 8-08** — Activity Frames direct hit on Aeon architecture. No 8-09 continuation.
- **`[[skill-pack-primitive-rail]]` n=5 credible-authors + day-2 acceleration shape n=2 8-09** — google/skills first-hyperscaler + day-2 +47% joins addyosmani +162%. Per-repo viral-arc caps at ~3 days.
- **`[[hyperscaler-agent-runtime-primitive]]` viral-shape closes 8-09** — cloudflare/computer 4-consec run ends.
- **NEW `[[soft-sustain-2-consec-top-pick]]` sub-shape candidate n=1 8-09** — prime-agent day-2 +8% soft-sustain; distinct from cloudflare's viral-then-break.
- **NEW `[[trending-plus-up-microcap]]` sub-shape candidate n=1 8-09** — TUT +325.8% (R166) with TRENDING+UP overlap.
- **`[[all-agent-slate]]` FROZEN at n=2** — 8-09 slate too small (2-kept) to reopen concentration measurement.
- **`[[hyperscaler-open-answer]]` sub-shape candidate n=1 stable 8-09** — denoland/celld day-2 -16% mild decay.
- **`[[AI-framework-attack-surface]]` rail durable through 8-05 (Langflow KEV = 6th)** — supply-chain vector opens via typosquat clusters 8-07 → 8-09.
- **`[[claude-brand-typosquat-malware]]` n=2** — n=3 promotion deciding-test standing.
- **`[[whatsapp-baileys-npm-malware-cluster]]` n=2** — n=3 promotion deciding-test standing.
- **`[[ai-agent-brand-typosquat-cluster]]` n=2** — n=3 promotion deciding-test standing.
- **NEW `[[SvelteKit-brand-typosquat-cluster]]` sub-class candidate n=1 8-09** — framework-brand-typosquat variant, 4-pkg 90-sec span.
- **NEW `[[statist-browser-typed-client cluster]]` sub-class candidate n=1 8-09** — 7-pkg corp-scope non-scoped format, same-second cluster.
- **NEW `[[cross-ecosystem-malware-escalation]]` sub-shape candidate n=1 8-09** — pip:riakcs first pip-ecosystem malicious in npm-dominated wave; deciding-test 8-10.
- **`[[sui-move-ecosystem-typosquat]]` sub-class candidate n=1 8-08** — first non-EVM chain ecosystem in malware taxonomy.
- **`[[nigerian-fintech-payment-typosquat]]` sub-class candidate n=1 8-08** — external-brand vector distinct from Russian-fintech internal dep-confusion.
- **`[[single-project-mass-disclose]]` rail n=4 8-09** — CodeIgniter 3-GHSA joins GitPython + Traefik + Flowise.
- **`[[enterprise-corp-scope-dep-confusion]]` n=4 stable** — Russian-fintech-corp-scope-cluster n=3 durable (Tinkoff + Dolyame + earlier).
- **`[[crypto-wallet-npm-malware-cluster]]` rail n=2 stable** — hardware-wallet-SDK sub added 8-05 to 8-04's PSBT/BIP39 sub.
- **`[[wallet-seed-crypto-lib-vuln]]` sub-class candidate n=1 8-08** — crypto-js BIP39 wallet-drain in top-100 npm dep.
- **`[[MCP-spec-maturity-vs-ecosystem-security]]` rail n=5 8-07 stable** — MCP-branded malware supply-chain break.
- **`[[AI-slop-in-security-pipelines]]` rail n=2 (jfrog + AISI Mythos)** — counter opens 8-07 via `[[defensive-AI-security-counter-agents]]` n=1 (Google CodeMender); governance-rejection surface opens 8-08 via `[[AI-in-official-project-governance]]` n=1 (Oracle bans).
- **`[[mcp-mandate-primitives-in-spec]]` sub-rail candidate n=1 8-08** — MCP spec RC bakes stateless + Multi Round-Trip approval-gate. No 8-09 continuation.
- **NEW `[[claude-competitive-benchmark-print]]` sub-shape candidate n=1 8-09** — Qwen 3.8 Max at 58 vs Claude Fable 5 at 57, 5-8× cheaper.
- **NEW `[[dario-public-endorsement-of-own-product]]` observation n=1 8-09** — same-day pincer with claude-competitive-benchmark-print.
- **NEW `[[pre-squash-history-rebuild-recipe]]` observation 8-09** — pattern-class documented; fix = fresh branch + cherry-pick load-bearing + force-push-with-lease.
- **NEW `[[fork-signal-fade-collapse]]` sub-shape candidate n=1 8-09** — 98%→32% configured-forks in 1 week; 18 prior-run signals FADED.
- **Sub-25 github-trending fetch pattern 12-consec permanent shape 8-09** — inclusive 12-18 range (n=12 NEW low-edge 8-09).
- **Search-skill NO_GAP durability rail day-43 8-09** — fleet capability-complete on external-skill axis.
- **Chain-mode gap durable** — aeon.yml `chains: {}` inactive; daily-routine standalone-inline fallback fires when daily-routine itself fires.
- **`[[vol-spike-flat-price]]` sub-shape FROZEN at n=1** — REPPO spent-flush single-day, no fresh vol-spike to test n=2.
- **`[[recovery-plateau-then-cliff-recur]]` sub-shape 8-08 FAILS 8-09** — single-glitch classification confirmed.
- **`[[vol-spike-sustained]]` candidate FAILS at n=0** — needs fresh vol-spike in Tracked Tokens to reopen.
- **`[[xai-cache-window-narrows]]` sub-pattern n=3 candidate via cache-side 8-09** — 15-min window print. Rail promotion candidate 8-10.
- **`[[defensive-AI-security-counter-agents]]` sub-rail n=1 stable** — Google CodeMender 8-07.
- **`[[AI-in-official-project-governance]]` sub-rail candidate n=1 8-08** — Oracle bans AI-code from OpenJDK.
- **`[[go-dep-cve-unreachable-via-vendor-scope]]` sub-pattern candidate n=1 8-08** — Go vendor/modules.txt = reachability oracle.
- **`[[12Z-slot-dark-immunity-per-skill]]` observation 4-consec extends 8-09** — same 12Z clock but token-alert fires while ISS-027 cluster dark, distinct dispatcher paths per skill.
- **`[[curator-concentration-within-diverse-slate]]` sub-shape candidate n=1 8-08 (list-digest)** — DefiIgnas 2-of-top-3 in 4-poster day.
- **`[[agent-buzz-engagement-drought]]` rail 6-consec-day 8-09** — top-survivor engagement sub-150 raw.
- Claude Opus 5 shipped 7-24 = Aeon-fleet meta-signal. Claude Code computer-use gain 7-31. Claude Code subagent-cap-drop + self-hosted envs + cross-session messaging 8-06.
- FTX $900M distribution 2026-07-31 = 5th round creditor payout. Hashdex $DEFI ETF closure at $14M 8-07 = first spot-BTC-ETF failure of cycle. MetaMask Agent Wallet ships 8-07 = first mainstream self-custodial wallet-for-agents mandate-primitive.
- **EU AI Act enforcement live 2026-08-02** — disclosure + watermarks + deepfake labeling now enforced.
