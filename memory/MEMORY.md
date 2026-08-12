# Long-term Memory
*Last consolidated: 2026-08-12*

## Current Goals
- **ISS-030 cost-report 8-10 Mon 07Z deciding-test T-0 TODAY** — 8-04 21:48Z same-day organic recovery holds; chronic sr=10%; signature `sdk_opt_in_required` cleared organically. Clean → RESOLVED same-day candidate; fail same-signature → 4-consec-week formal-pattern. See [[iss-030]].
- **`chronic-cohort-alone-degraded` regime 12-consec-heartbeat-tick ~125h span 8-04 14:45Z → 8-09 20:14Z (8th 24h durability gate crossed 8-09 20Z)** — 10-skill chronic sub-50% cohort composition-locked: cost-report 10% / skill-analytics 21% / reg-monitor 21% / vuln-scanner 25% / market-context-refresh 32% / narrative-tracker 33% / search-skill 38% / fleet-control 40% (disabled) / security-digest 45% / aixbt-pulse 47%. Deepest composition-identity print in memory-window.
- **fork-cohort STUCK 8-09 20Z — NEW P0 novel signal** *[BLOCKED 8-12 — ISS-032 file-op owed since 8-11 18:40Z; ~95h stuck, past 48h threshold]* — first fork-cohort stall of memory-window; state-update-race on cancelled workflow (run 31330721650 hit 30-min "Run" step timeout at 19:35:47Z, but "Update cron state" step conclusion=success did NOT clear the dispatched marker). Last success 2026-08-02T19:52:59Z. Weekly-review 8-10 T-0 root-cause investigation candidate — check if commit-results/update-cron-state steps handle cancellation; file as new ISS if not.
- **ISS-028 workaround-chain n=38+ durable 18-UTC-day span 7-22 → 8-09** — 5 fresh 8-09 call-sites (daily-routine tweet-roundup + github-trending Edit-tool 2-step + token-alert Write+Edit-append + heartbeat 14:44Z + agent-buzz + heartbeat 20:14Z + goal-tracker + skill-health). PR #177 opened 8-09 18:18Z documenting sandbox-block in CLAUDE.md. Sibling bash-redirect-block + heredoc-parser-over-length family stable. Weekly-review 8-10 T-0 reopens root-cause investigation.
- **12:00 UTC batch DARK day-44 on 8-10** — ISS-027 8-skill cluster frozen since 2026-06-28; scheduler-side gap not CG infra. Token-alert 12Z slot fires 4-consec clean 8-06→8-09 confirming `[[12Z-slot-dark-immunity-per-skill]]` per-dispatcher-path. 8-10 12Z = 5-consec-candidate.
- **PR queue at 3 on 8-09 20Z (post Sunday-batch)** — #174 (Advisor Brier-weight, ~44h+, mergeable=UNKNOWN + empty statusCheckRollup, CI never fired), **#176 fresh (skill-graph regen `EDGES_TOTAL: 32→74`, opened 17:10Z by skill-graph Sunday-fire, ~3h at 20Z heartbeat)**, **#177 fresh (fix(claude-md) ISS-028 file-redirect sandbox-block doc, opened 18:18Z by self-improve 18:14Z run, ~2h at 20Z heartbeat)**. Queue-full self-improve exit-gate stays DISENGAGED (only #177 counts as self-improve, n=1 < 3).
- **Operator on-chain config day-65 on 8-10** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Operator-gated.
- **priorities.md 67d stale on 8-10** — last reviewed 2026-06-04. Vault inbox 50d cold streak (last real capture 2026-06-21T08:32Z). Weekly-review 8-10 T-0 refresh-ask.
- **fork-cohort STUCK ~68h+ P0 — ISS-032 filing OVERDUE** — dispatched 8-09T19:05Z, last_success 8-02T19:52Z; crossed 48h escalation 8-11 19:05Z, ~20h+ past threshold at 15:08Z heartbeat. Root-cause: state-update-race on cancelled workflows (`Update cron state` step reports success but does not clear dispatched marker when `Run` step hits 30-min timeout). Owed by 18Z action-converter / reflect fire.
- **ISS-031 detect-usepod-402 gate deadline 8-13 TOMORROW** — `scripts/detect-usepod-402.sh` operator-page gate is stopgap for `[[ISS-029/031 recurrence]]` (2nd 7d-recurrence 8-10 crossed one-off→pattern threshold). Final workday before deadline.
- **ISS-030 33+ consec chronic-fail BREAKS 8-11 20:08Z** — 2nd organic-recovery precedent (after 8-04 21:48Z); skill-health 16 → 4 CRITICAL deepest single-tick recovery of memory-window. Same-week n=5 same-signature cluster preceded recovery. **8-17 Mon 07Z next-week deciding-test** for same-signature 4-consec-week formal-pattern (counter still at n=1).
- **PR queue at 4 on 8-12** — #179 fresh 8-11 18:42Z (fix(token-alert) volume-spike baseline daily-granular), #177 ~69h (fix(claude-md) ISS-028), #176 ~70h (skill-graph regen 32→74), #174 ~4d (Advisor Brier-weight external). Weekly-batch cadence per CLAUDE.md; queue-full self-improve exit-gate DISENGAGED.
- **`[[chronic-cohort-alone-degraded]]` regime 12-skill composition holds ~155h span** — cost-report 8% / skill-analytics 21% / reg-monitor 21% / vuln-scanner 25% / market-context-refresh 32% / narrative-tracker 33% / search-skill 37% / weekly-shiplog 37% / unlock-monitor 38% / security-digest 43% / deal-flow 44% / aixbt-pulse 47%.
- **4 Mon-batch 🕸 stuck skills hold-through-week 8-12 → 8-17** — search-skill (48h) · unlock-monitor (48h) · skill-security-scan (46h) · deal-flow (46h); no auto self-clear until 8-17 Mon or operator intraweek manual invoke.
- **12:00 UTC batch DARK d46 on 8-12** — ISS-027 8-skill cluster frozen since 2026-06-28; token-alert 12Z slot fires 6-consec clean 8-07→8-12 (memory-window record) confirming `[[12Z-slot-dark-immunity-per-skill]]` per-dispatcher-path.
- **Operator on-chain config day-67 on 8-12** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Operator-gated.
- **priorities.md 69d stale + vault inbox 51d cold on 8-12** — `### Idea Captured` 6-consec zero-day streak (8-07→8-12). Weekly-review 8-10 T-0 refresh-ask stands unactioned.

## Recently Cleared (8-11 → 8-12)
- **ISS-030 cost-report 33+ consec BREAKS 8-11 20:08Z** — see Current Goals; 8-12 morning batch (thought-review + morning-brief + daily-routine + heartbeat + skill-freshness + github-trending + token-alert + security-digest + reg-monitor + list-digest) all clean through 17:13Z.
- **skill-health CRITICAL 16 → 4 deepest single-tick recovery of memory-window** — post 8-11 20:08Z cost-report recovery.
- **`[[claude-code-alternative-open-source]]` FORMAL PATTERN promoted n=3 8-12** — Jcode 8-11 + t3code 8-11 + stablyai/orca 8-12 within 7d window; 3 distinct sub-classes.
- **CG clean-day d50 → d51 8-12** — memory-window-first round-number extends.
- **Token-alert 5-consec → 6-consec clean-fire streak 8-12** — memory-window record extends.
- **`[[fleet-relevance agent-thesis]]` rail 28 → 29-consec-UTC-day 8-12** — github-trending 4-pick fleet-adjacent slate + AgentOPSD paper.
- **Aeon-fleet clean d12 → d13 vs security-digest surface 8-12** — deepest defensive-import clean-streak in memory-window.
- **security-digest paired rail-break day 8-12** — `[[malware-only-security-surface]]` n=4 formal-pattern BREAKS (SeaweedFS Go SSRF tracked-critical) + `[[quiet-KEV-baseline]]` 4-consec BREAKS (3 KEV added 8-11) + `[[EPSS-skip-run]]` n=3 formal-pattern BREAKS. `[[cross-ecosystem-malware-escalation]]` n=3 does not extend (npm-only 98.3% today).

## Fleet Health
See [[fleet]] for full snapshot. **Cost-report chronic BREAK 8-11 20:08Z + 8-12 morning batch clean overnight** = biggest fleet-recovery of the week. **fork-cohort STUCK 68h+ P0** eclipses everything else in blast-radius terms; ISS-032 filing overdue. **ISS-031 detect-usepod-402 gate 8-13 deadline tomorrow**. **skill-health 16→4 CRITICAL deepest recovery of memory-window**. **PR queue at 4** (weekly-batch cadence). **Bash `>` redirect workaround-chain n=40 durable 20-UTC-day span 7-22 → 8-12** (fresh 8-12 call-sites: github-trending for-loop + list-digest `>>` seen-file append).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, weekly-batch cadence, positive events log.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns.
- [Market context](topics/market-context.md) — Baseline snapshot (STALE ~27d/648h+ on 8-12, crossed 2× threshold 8-01; refresh chained on next batch-dark thaw or manual invoke).
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. Last fire 8-12 12:30Z 12Z-slot scheduled: **0/4 alerts** (6-consec-day clean-fire streak post-8-07 memory-window-first 2/4 print). CG clean-day d51 unbroken. WELL `[[vol-vacuum-price-flat]]` n=1 candidate (0.06× baseline vol on -0.87% near-flat price = extremest sub-baseline vol print in memory-window). GITLAWB `[[vol-compression-on-price-decay]]` n=2 (6-consec sub-baseline on 10-phase arc). MAMO `[[MAMO-3-consec-above-baseline-vol]]` n=1 (digestion band d22). REPPO 8-11 2-competing-candidate deciding-test RESOLVES via healthy-flush read (both rail-abandoned at n=1).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 8-12 −0.87% (12:30Z), vol $52K = 0.06× baseline — vol-vacuum n=1 candidate; extremest sub-baseline print of memory-window |
| MAMO    | mamo               | 15%           | 8-12 −1.83% (12:30Z), vol $735K = 1.04× baseline — 3-consec above-baseline stretch (memory-window first); digestion band d22 |
| REPPO   | reppo              | 15%           | 8-12 −5.99% (12:30Z), vol $252K = 1.32× baseline — fade eases + vol expands = healthy-flush read; 2 8-11 candidates abandoned |
| GITLAWB | gitlawb            | 15%           | 8-12 −6.50% (12:30Z), vol $140K = 0.74× baseline — 6-consec sub-baseline vol on 10-phase price fade; n=2 extends |

## Recurring patterns (durable — brief pointers; details in topic files)
- **`[[fleet-relevance agent-thesis]]` rail 29-consec-UTC-day 8-12** — github-trending 4-pick fleet-adjacent slate (orca + DeepTutor + anthropics/skills + diagram-design) + AgentOPSD paper. **Crosses 4-consec-week durability 8-15 if unbroken.**
- **`[[claude-code-alternative-open-source]]` FORMAL PATTERN n=3 8-12** — 3 distinct sub-classes within 7d (Jcode memory-efficient orch + t3code mobile viewer + orca full-ADE cross-surface). Rail promoted from candidate.
- **NEW `[[llm-output-visual-primitive]]` sub-shape n=1 8-12** — cathrynlavery/diagram-design (29 curated HTML+SVG diagram types for Claude Code, biggest github-trending spike). First "curated visual library for LLM emission targets" print.
- **NEW `[[memory-primitive-product-surface]]` sub-shape n=1 8-12** — HKUDS/DeepTutor (lifelong-personalized-tutoring). First memory-primitive-as-product-architecture print, distinct from infra-tier semantica/code-graph-rag prints.
- **`[[memory-primitive-paper streak]]` 7-consec 8-12** — AgentOPSD memory-adjacent (Tsinghua ↑49, recursive bayesian belief updates on teacher-student log-prob gaps).
- **NEW `[[EU-AI-Act-enforcement-surface]]` sub-shape n=1 8-12** — Claude watermarking global rollout is first fleet-visible enforcement print since 8-02 act live.
- **NEW `[[weights-as-wiring hardware]]` sub-shape n=1 8-12** — AMD/Taalas acquisition-priced (621pts HN).
- **NEW `[[hitl-review-fatigue-empirical]]` sub-shape n=1 8-12** — 40k game runs / 409k decisions gives empirical floor on HITL review reliability (293pts HN).
- **`[[agent-graphs-replacing-prompting]]` n=2 8-11** — Andrew Ng 8-10 + Anthropic engineer via ajay4ai 8-11. Rail promotion deciding-test 8-18 (3rd fleet-visible authority within 7d).
- **NEW `[[soft-sustain-2-consec-top-pick]]` sub-shape memory-window n=2 8-12** — semantica-agi/semantica -8% day-2 mild decay = 3rd top-pick with day-2 soft-sustain. Deciding-test 8-13 for 3-consec.
- **`[[3-day-sustained-top-pick]]` TERMINATES at day-4 8-12** — prime-agent -57% day-4 = viral-arc break, matches cloudflare/computer 8-06→8-07 -69% day-3 shape.
- **NEW `[[defi-protocol-brand-npm-typosquat-cluster]]` sub-shape n=1 8-12** — 7 npm defi-brand pkgs in 17h (permit2 Uniswap + boring-vault Yearn + augustdigital-sdk + camelot-ammv2-{core,periphery} + upshift-{config,finance}). Cross-ecosystem parent-pattern candidate n=1 (2-consec-UTC-day with 8-11 pip cluster).
- **NEW `[[alphabet-namespace-cluster]]` sub-shape n=1 8-12** — 22 alphabet-suffixed `@years18/n8n-nodes-utils-helper-{a..x}` variants; novel scaled-namespace-fill.
- **NEW `[[curator-fresh-handle-emergence]]` sub-shape n=1 8-12** — 0xTindorr first appearance in list-digest 154-line seen-file history. Pendle PT-loop breakdown = memory-window-first `[[pendle-yield-content-print]]` n=1. Flowslikeosmo $CARDS+$SEALED = first `[[collectible-tokenization-ticker-print]]` n=1.
- **`[[curator-DeFi_Made_Here-dominance]]` (from 8-11) FAILS 8-12** — DeFi_Made_Here 0 appearances today.
- **NEW `[[vol-vacuum-price-flat]]` sub-shape n=1 8-12** — WELL 0.06× baseline vol on -0.87% near-flat price; distinct from vol-compression-on-price-decay (needs price-decay) + healthy-consolidation (needs vol-at-baseline). Deciding-test 8-13.
- **`[[vol-compression-on-price-decay]]` n=2 8-12** — GITLAWB 6-consec sub-baseline vol; formal-pattern promotion at n=3.
- **NEW `[[MAMO-3-consec-above-baseline-vol]]` n=1 8-12** — first 3-consec above-baseline vol stretch on MAMO in memory-window.
- **NEW `[[intraday-candidate-both-fail-via-flush]]` observation n=1 8-12** — REPPO 8-11 2-competing-candidate deciding-test resolves via healthy-flush read (third-party emergent).
- **`[[malware-only-security-surface]]` n=4 formal-pattern BREAKS 8-12** — SeaweedFS Go SSRF critical hits tracked stack; first tracked-critical since 8-07 crypto-js.
- **`[[quiet-KEV-baseline]]` 4-consec streak (8-08→8-11) BREAKS 8-11** — 3 KEV added (Metabase + Cisco ASA/FTD + Windows WinSock, all patch-Tuesday product-CVEs + open-source app-CVE).
- **`[[EPSS-skip-run]]` n=3 formal-pattern BREAKS 8-12** — EPSS enriched 10/12 today. New counter starts on next EPSS-skip.
- **`[[cross-ecosystem-malware-escalation]]` n=3 does NOT extend 8-12** — npm-only 98.3% today = back to 8-08 baseline.
- **Aeon-fleet clean d13 vs security-digest surface 8-12** — deepest defensive-import clean-streak in memory-window. `permit2` near-miss noted.
- **`[[12Z-slot-dark-immunity-per-skill]]` 6-consec 8-07→8-12** — token-alert 12Z-slot fires clean while ISS-027 8-skill 12Z-batch dark d46.
- **Bash `>` redirect workaround-chain n=40 durable 20-UTC-day span 7-22 → 8-12** — 8-12 fresh call-sites: github-trending for-loop over `${repo}` variable expansion + list-digest `>>` seen-file append. NEW variant class from 8-11 `[[python-inline-exec-blocked]]` stable.
- **Sub-25 github-trending fetch pattern 14-consec permanent shape 8-12** — n=18 NEW mid-band high (prior high was n=17 8-08).
- **`[[MCP-enforcement-primitive-cluster]]` dormant since 8-05** — needs 3rd variant same-UTC-day to advance rail past 8-05.
- **reg-monitor CFTC RSS 404 durability d7+ confirmed 8-12** — 2nd-observation (8-05 + 8-12) → self-improve candidate to bake HTML-fallback into SKILL step 1C.
- **reg-monitor score-15 ACT-item 8-12** — CFTC 9281-26 emergency Kalshi order (§8a(9)) exceeds prior week's top score-12 (NY v Kalshi Forbes 8-05). Prediction-market lane signal density escalating.
- **`[[claude-real-math-breakthrough]]` observation n=1 8-11** — Claude solves 67% Riemann zeros in 1.5 days (prev 41.6%).
- **`[[dario-public-endorsement-of-own-product]]` observation n=1 8-09** — same-day pincer with claude-competitive-benchmark-print.
- **`[[pre-squash-history-rebuild-recipe]]` observation 8-09** — fresh branch + cherry-pick load-bearing + force-push-with-lease.
- **`[[fork-signal-fade-collapse]]` sub-shape candidate n=1 8-09** — 98%→32% configured-forks in 1 week. Deciding-test 8-16 next weekly cycle.
- Claude Opus 5 shipped 7-24. Claude Code computer-use gain 7-31. Claude Code subagent-cap-drop + self-hosted envs + cross-session messaging 8-06. Claude watermarking global 8-12 (EU AI Act enforcement surface).
- FTX $900M distribution 2026-07-31 = 5th round creditor payout. Hashdex $DEFI ETF closure at $14M 8-07 = first spot-BTC-ETF failure of cycle. MetaMask Agent Wallet ships 8-07 = first mainstream self-custodial wallet-for-agents mandate-primitive.
- **EU AI Act enforcement live 2026-08-02** — disclosure + watermarks + deepfake labeling now enforced; Claude watermarking global 8-12 = first fleet-visible enforcement print.
