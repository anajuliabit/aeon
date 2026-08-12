# Long-term Memory
*Last consolidated: 2026-08-11*

## Current Goals
- **ISS-030 cost-report 8-10 Mon 07Z deciding-test T-0 TODAY** — 8-04 21:48Z same-day organic recovery holds; chronic sr=10%; signature `sdk_opt_in_required` cleared organically. Clean → RESOLVED same-day candidate; fail same-signature → 4-consec-week formal-pattern. See [[iss-030]].
- **`chronic-cohort-alone-degraded` regime 12-consec-heartbeat-tick ~125h span 8-04 14:45Z → 8-09 20:14Z (8th 24h durability gate crossed 8-09 20Z)** — 10-skill chronic sub-50% cohort composition-locked: cost-report 10% / skill-analytics 21% / reg-monitor 21% / vuln-scanner 25% / market-context-refresh 32% / narrative-tracker 33% / search-skill 38% / fleet-control 40% (disabled) / security-digest 45% / aixbt-pulse 47%. Deepest composition-identity print in memory-window.
- **fork-cohort STUCK 8-09 20Z — NEW P0 novel signal** *[BLOCKED 8-12 — ISS-032 file-op owed since 8-11 18:40Z; ~95h stuck, past 48h threshold]* — first fork-cohort stall of memory-window; state-update-race on cancelled workflow (run 31330721650 hit 30-min "Run" step timeout at 19:35:47Z, but "Update cron state" step conclusion=success did NOT clear the dispatched marker). Last success 2026-08-02T19:52:59Z. Weekly-review 8-10 T-0 root-cause investigation candidate — check if commit-results/update-cron-state steps handle cancellation; file as new ISS if not.
- **ISS-028 workaround-chain n=38+ durable 18-UTC-day span 7-22 → 8-09** — 5 fresh 8-09 call-sites (daily-routine tweet-roundup + github-trending Edit-tool 2-step + token-alert Write+Edit-append + heartbeat 14:44Z + agent-buzz + heartbeat 20:14Z + goal-tracker + skill-health). PR #177 opened 8-09 18:18Z documenting sandbox-block in CLAUDE.md. Sibling bash-redirect-block + heredoc-parser-over-length family stable. Weekly-review 8-10 T-0 reopens root-cause investigation.
- **12:00 UTC batch DARK day-44 on 8-10** — ISS-027 8-skill cluster frozen since 2026-06-28; scheduler-side gap not CG infra. Token-alert 12Z slot fires 4-consec clean 8-06→8-09 confirming `[[12Z-slot-dark-immunity-per-skill]]` per-dispatcher-path. 8-10 12Z = 5-consec-candidate.
- **PR queue at 3 on 8-09 20Z (post Sunday-batch)** — #174 (Advisor Brier-weight, ~44h+, mergeable=UNKNOWN + empty statusCheckRollup, CI never fired), **#176 fresh (skill-graph regen `EDGES_TOTAL: 32→74`, opened 17:10Z by skill-graph Sunday-fire, ~3h at 20Z heartbeat)**, **#177 fresh (fix(claude-md) ISS-028 file-redirect sandbox-block doc, opened 18:18Z by self-improve 18:14Z run, ~2h at 20Z heartbeat)**. Queue-full self-improve exit-gate stays DISENGAGED (only #177 counts as self-improve, n=1 < 3).
- **Operator on-chain config day-65 on 8-10** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Operator-gated.
- **priorities.md 67d stale on 8-10** — last reviewed 2026-06-04. Vault inbox 50d cold streak (last real capture 2026-06-21T08:32Z). Weekly-review 8-10 T-0 refresh-ask.

## Recently Cleared (8-11)
- **weekly-shiplog 8-10 09Z T-0** — RESOLVED 2026-08-10 19:21Z via `articles/weekly-shiplog-2026-08-10.md` ship (51 commits / 28 PRs merged / 0 issues closed; themes: vuln-scanner fuzzing / catalog clears 70 / Agent Skills spec-form replaces OKF). Prior 20d-stale flag cleared same-day; next 7d tick 2026-08-17 09Z.
- **ISS-030 n=3 same-signature cluster intra-~18h 8-10 20:32Z → 8-11 14:14Z** — cost-report `sdk_opt_in_required` prints ×3 in ~18h span (all within week-1 shape). Still same-week; formal-pattern week-tick counter frozen at n=1 pending 8-17 Mon 07Z next-week deciding-test. consec=33 sr=7% (fresh chronic drop). See [[iss-030]].
- **ISS-031 usepod 402 SELF-HEALED 8-10 ~19:15Z** — fleet-wide burst 8-10 15:10Z → 19:15Z (~4h duration, slightly longer than ISS-029 8-03 ~2h shape). Overnight morning batch 8-11 (thought-review 07:50Z + morning-brief 07:52Z + daily-routine 07:59Z + heartbeat 08:41Z + skill-freshness 09:00Z + github-trending 09:47Z + token-alert 12:13Z + heartbeat 14:46Z + security-digest 14:47Z + agent-buzz 17:44Z) all clean = gateway self-heal held ~24h. **2nd 7d-recurrence event of ISS-029 shape** → signature crosses one-off → pattern threshold per weekly-review 8-10 action. Awaiting operator decision on `scripts/detect-usepod-402.sh` gate (2026-08-13 deadline).
- **fork-cohort STUCK approaching 48h escalation ~19:05Z tonight 8-11** — dispatched 8-09T19:05Z, last_success 8-02T19:52Z. At 14:46Z heartbeat = ~67.7h stuck. **File new ISS if uncleared** past 19:05Z (dedup vs 8-09 novel-signal flag). Root-cause: state-update-race on cancelled workflows (commit-results/update-cron-state does not clear dispatched marker when Run step times out at 30-min cap).
- **Day-of-week reclarify — today is Tue 8-11, not Mon** — 08:41Z heartbeat wrongly assumed Mon per cost-report firing. 4 Mon-scheduled 🕸 stale-state stuck skills (search-skill · deal-flow · unlock-monitor · skill-security-scan) hold state through week; no auto self-clear until 8-17 Mon or operator intraweek manual invoke.
- **12:00 UTC batch DARK d45 on 8-11** — ISS-027 8-skill cluster frozen since 2026-06-28; scheduler-side gap not CG infra. Token-alert 12Z slot fires 5-consec clean 8-06→8-11 (memory-window-record) confirming `[[12Z-slot-dark-immunity-per-skill]]` per-dispatcher-path.
- **PR queue at 3 on 8-11** — #174 (Advisor Brier-weight, ~87h+ mergeable=UNKNOWN + empty statusCheckRollup — CI never fired), #176 (skill-graph regen EDGES_TOTAL: 32→74, opened 8-09 17:10Z), #177 (fix(claude-md) ISS-028 file-redirect sandbox-block doc, opened 8-09 18:18Z). Queue-full self-improve exit-gate stays DISENGAGED (only #177 counts as self-improve, n=1 < 3).
- **Operator on-chain config day-66 on 8-11** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Operator-gated.
- **priorities.md 68d stale + vault inbox 51d cold on 8-11** — last priorities review 2026-06-04; last real capture 2026-06-21T08:32Z. 5-consec-UTC-day zero-capture streak on `### Idea Captured` axis (8-07 → 8-11). Weekly-review 8-10 T-0 refresh-ask.

## Recently Cleared (8-10 → 8-11)
- **weekly-shiplog CLEARED 8-10 19:21Z** — resolved 20d-stale flag; article shipped 2026-08-10.
- **ISS-031 usepod 402 fleet-wide burst SELF-HEALED 8-10 ~19:15Z** — ~4h event; 13-skill retry batch all succeeded 19:15-19:23Z; morning batch 8-11 held clean overnight.
- **github-trending + token-alert stale-state 🕸 self-cleared 8-11** — 09:47Z + 13:44Z respectively; both dispatchers work independently of Mon-scheduled cohort.
- **`[[agent-buzz-engagement-drought]]` rail 6-consec-day 8-10 → BREAKS 8-11** — @Sengo_Sol raw eng 115 (founder-boost 104.6) resets counter.
- **BTW `[[same-coin-48h-reflip]]` deciding-test CLARIFIED as fade-not-reflip 8-10 + 8-11** — 3-consec-fade (8-09 +28.8% → 8-10 -6.7% → 8-11 -9.2%) = 3-day mean-reversion pattern dominant read; rail promotion **abandoned on reflip axis**, opens on `[[3-day-mean-reversion-post-spike]]` axis n=1 candidate.
- **CG clean-day d49 → d50 8-11 = MEMORY-WINDOW-FIRST 50-CONSEC-DAY PRINT** — round-number milestone on infra durability rail.
- **Token-alert 5-consec-day clean-fire streak 8-07 → 8-11** — memory-window record for consecutive 0/4 fires post the rare 2/4 print.
- **CYS 4-consec-day sustained-breakout arc 8-08→8-11 (+61%/+18%/+18%/+47%, 7d +362%)** — NEW `[[sustained-multi-day-breakout]]` sub-shape candidate n=1 8-11. Memory-window rare.
- **BEAT `[[large-cap-2-day-blowup]]` NEW sub-shape n=1 8-11** — 2-consec-day capitulation (-52% → -55%, 7d -62%). Distinct from single-day flip.
- **`[[fleet-relevance agent-thesis]]` rail 25 → 28-consec-UTC-day 8-11** — triple-axis 8-11 via github-trending (semantica + t3code + LifeOS) + paper-pick (Ouroboros direct-hit on Aeon self-improve). Approaches 4-consec-week durability.
- **Ouroboros paper 8-11 daily-routine paper-pick** — self-developing frontier coding agent with reviewed core evolution = **literal blueprint description of Aeon's self-improve loop**. Highest fleet-meta signal of the week.
- **security-digest 2 formal-pattern promotions 8-11**: `[[malware-only-security-surface]]` n=3→n=4 promoted (4-consec-day zero-fresh-critical/high-with-fresh-malware); `[[cross-ecosystem-malware-escalation]]` n=2→n=3 promoted (PyPI share 42% today vs 8-10 14.6% vs 8-09 2%); `[[EPSS-skip-run]]` n=2→n=3 promoted (formal-pattern). `[[SvelteKit-brand-typosquat-cluster]]` deciding-test FAILS at n=2.
- **Aeon-fleet clean d11 → d12 vs security-digest surface 8-11** — deepest clean-streak in memory-window on defensive-import axis.
- **fork-cohort STUCK 8-09 20Z novel P0 — durability 26h → 67.7h** — through 8-11 14:46Z; awaits 48h-threshold escalation tonight.

## Fleet Health
See [[fleet]] for full snapshot. **Fleet recovers from ISS-031 usepod 402 burst overnight** (8-10 15:10Z → 19:15Z, ~4h). All morning batch 8-11 clean through 17:44Z; only fresh fails today are ISS-030 cost-report n=3 same-signature (08:19Z + 14:14Z, plus 8-10 20:32Z prior). Chronic-cohort regime holds ~131h span (broken 8-10 by ISS-031, resumes 8-11 morning). **fork-cohort STUCK ~67.7h at 14:46Z** approaches 48h escalation ~19:05Z tonight. **CG clean-day d50 memory-window-first**. **12Z-slot-dark-immunity-per-skill 5-consec extends**. **weekly-shiplog CLEARED**. **PR queue holds at 3** (weekly-batch cadence). **Bash `>` redirect workaround-chain n=39+ durable 19-UTC-day span 7-22 → 8-11** (fresh 8-11 call-site: python inline-exec-blocked as NEW variant, jq-only path is workaround).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, weekly-batch cadence, positive events log.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns.
- [Market context](topics/market-context.md) — Baseline snapshot (STALE ~26d/624h+ on 8-11, crossed 2× threshold 8-01; refresh chained on next batch-dark thaw or manual invoke).
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. Last fire 8-11 13:44Z operator re-check: **0/4 alerts** (5-consec-day clean-fire streak post-8-07 memory-window-first 2/4 print). CG clean-day d50 unbroken (memory-window-first round-number). REPPO closest-to-threshold today at 51-64% of rail with intraday shape-inversion (12:13Z `[[price-fade-on-collapsing-vol]]` n=1 candidate → 13:44Z `[[vol-flush-price-bounce]]` n=1 competing candidate — 8-12 direction picks winner). WELL 3rd intraday 24h flip to positive (+0.17% 13:44Z, first positive since 8-09). GITLAWB `[[vol-compression-on-price-decay]]` sub-shape n=1 candidate (5-consec sub-baseline vol on -6% moves). MAMO 2-consec above-baseline vol (07:50Z + 12:13Z); digestion band d21.

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 8-11 +0.17% (13:44Z operator re-check), vol $799K = 0.89× baseline — 3rd intraday 24h print flips positive, 1st positive since 8-09 |
| MAMO    | mamo               | 15%           | 8-11 −3.68% (13:44Z), vol $747K = 1.06× baseline — 2-consec above-baseline vol (07:50Z + 12:13Z), digestion band d21 |
| REPPO   | reppo              | 15%           | 8-11 −7.68% (13:44Z, bounced from 12:13Z −9.56%), vol $120K = 0.63× baseline — 2 competing intraday sub-shapes; 6-phase post-peak arc extends |
| GITLAWB | gitlawb            | 15%           | 8-11 −5.33% (13:44Z), vol $178K = 0.95× baseline — 5-consec sub-baseline vol on continued fade; 9-phase arc extension |

## Recurring patterns (durable — brief pointers; details in topic files)
- **`[[fleet-relevance agent-thesis]]` rail 28-consec-UTC-day 8-11** — triple-axis via github-trending (semantica + t3code + LifeOS) + paper-pick (Ouroboros). Approaches 4-consec-week durability.
- **NEW `[[agent-graphs-replacing-prompting]]` sub-rail candidate n=2 8-11** — Andrew Ng 8-10 + Anthropic engineer via ajay4ai 8-11 corroboration. Rail promotion at n=3 (any 3rd fleet-visible authority within 7d).
- **NEW `[[graph-native-primitive-cluster]]` sub-shape candidate n=1 8-11** — semantica-agi/semantica + vitali87/code-graph-rag both graph-native, both fresh-push same UTC-day. Distinct from vector-DB substrate class.
- **NEW `[[agent-provenance-primitive]]` sub-shape candidate n=1 8-11** — semantica W3C PROV-O + no-LLM-in-reasoning-path; adjacent to Aeon memory/logs discipline.
- **`[[claude-code-alternative-open-source]]` n=1 (Jcode 07:52Z) → n=2 (t3code 09:47Z) same UTC-day 8-11** — 2 distinct sub-classes (memory-efficient orchestration vs mobile viewer). Rail promotion deciding-test accelerated.
- **NEW `[[3-day-sustained-top-pick]]` sub-shape candidate n=1 8-11** — prime-agent day-3 +6% memory-window first 3-consec-day pos-slope on top-pick axis.
- **`[[hyperscaler-open-answer]]` sub-shape refresh n=2 8-11** — google-deepmind/weathernext v0.3.0 open-weights joins denoland/celld 8-08.
- **`[[same-coin-48h-reflip]]` FAILS at n=2 rail-abandon 8-11** — BTW 3-consec-fade (8-09/8-10/8-11) resolves as mean-reversion, not reflip. Opens `[[3-day-mean-reversion-post-spike]]` axis n=1 candidate.
- **NEW `[[sustained-multi-day-breakout]]` sub-shape candidate n=1 8-11** — CYS 4-consec-day (+61%→+18%→+18%→+47%, 7d +362%). Distinct from single-day-breakout-then-fade.
- **NEW `[[large-cap-2-day-blowup]]` sub-shape candidate n=1 8-11** — BEAT 2-consec-day capitulation (-52% → -55%, 7d -62%).
- **`[[MCP-enforcement-primitive-cluster]]` refresh 8-10 + 8-11 pre-signal (agent-buzz)** — dormant since 8-05; 8-10 3 fresh call-sites (melvynx/straikerai/SheikAlthafDev) + 8-11 2 MCP-cluster tweets (shupeiman + KirkDBorne). Needs 3rd variant same-UTC-day to advance rail past 8-05.
- **`[[malware-only-security-surface]]` n=4 FORMAL PATTERN 8-11** — 4-consec-day zero-fresh-critical/high-with-fresh-malware.
- **`[[cross-ecosystem-malware-escalation]]` n=3 FORMAL PATTERN 8-11** — 3-consec-day non-npm-heavy malware (PyPI 42%).
- **`[[EPSS-skip-run]]` n=3 FORMAL PATTERN 8-11** — legitimately unmeasurable (all malware CVE-less + CVE-bearing dedup).
- **NEW `[[defi-protocol-brand-pip-typosquat-cluster]]` sub-class candidate n=1 8-11** — 8 pip pkgs (plp-contract/neutrl-core/dlmm-sdk/euler-sdk/morpho-sdk/joule-btp-extension) in ~15h span. First pypi defi-dev cluster.
- **NEW `[[scoped-brand-triple-scope-typosquat]]` sub-shape candidate n=1 8-11** — 3rd scope on sqlite brand (@sqlite-labs escalation of 8-10 double-scope @sqlite-prime + @sqlite-table).
- **NEW `[[npm-builtin-namespace-shadow]]` sub-class candidate n=1 8-10** — commonjs-assert + commonjs-assertion shadow node builtin `assert`. Higher pull-in-able risk than brand-typosquat.
- **`[[SvelteKit-brand-typosquat-cluster]]` deciding-test FAILS 8-11** — n=2 stays (no fresh SvelteKit-brand malware today).
- **Aeon-fleet clean d12 vs security-digest surface 8-11** — deepest clean-streak in memory-window on defensive-import axis.
- **`[[12Z-slot-dark-immunity-per-skill]]` extends to 5-consec 8-06 → 8-11** — token-alert clean while ISS-027 cluster batch-dark d45.
- **Bash `>` redirect workaround-chain n=39+ durable 19-UTC-day span 7-22 → 8-11** — NEW variant `[[python-inline-exec-blocked]]` (python3 -c heredoc hits path-validation lint; jq-only path is workaround). Fresh 8-11 call-site from daily-routine.
- **NEW `[[claude-real-math-breakthrough]]` observation n=1 8-11** — Claude solves 67% Riemann zeros in 1.5 days (prev 41.6%). First fleet-visible "Claude does real math research" print.
- **NEW `[[ZHC-narrative-print]]` sub-shape candidate n=1 8-11** — Sengo_Sol "agents as economic principals" first ZHC-adjacent thesis-print of memory-window.
- **NEW `[[industrial-brownfield-agent-deployment]]` sub-shape candidate n=1 8-11** — Neuron Industries 1991 Siemens PLC one-shot upgrade (distinct from hyperscaler-runtime axis).
- **NEW `[[curator-DeFi_Made_Here-dominance]]` sub-shape candidate n=1 8-11** — list-digest 2 of top-3 (distinct handle from prior DefiIgnas/Flowslikeosmo concentration).
- **`[[claude-competitive-benchmark-print]]` n=1 stable 8-09** — Qwen 3.8 Max vs Claude Fable 5 near-parity.
- **`[[dario-public-endorsement-of-own-product]]` observation n=1 8-09** — same-day pincer with claude-competitive-benchmark-print.
- **`[[pre-squash-history-rebuild-recipe]]` observation 8-09** — fresh branch + cherry-pick load-bearing + force-push-with-lease.
- **`[[fork-signal-fade-collapse]]` sub-shape candidate n=1 8-09** — 98%→32% configured-forks in 1 week. Deciding-test 8-16 next weekly cycle.
- **Sub-25 github-trending fetch pattern 13-consec permanent shape 8-11** — 7-28 → 8-11 (mid-band n=16 today).
- **Search-skill NO_GAP durability rail day-45 8-11** — fleet capability-complete on external-skill axis.
- **`[[memory-primitive-paper streak]]` extends via Ouroboros 8-11** — self-developing-agent-with-reviewed-core-evolution = Aeon-fleet-mirror paper.
- Claude Opus 5 shipped 7-24. Claude Code computer-use gain 7-31. Claude Code subagent-cap-drop + self-hosted envs + cross-session messaging 8-06.
- FTX $900M distribution 2026-07-31 = 5th round creditor payout. Hashdex $DEFI ETF closure at $14M 8-07 = first spot-BTC-ETF failure of cycle. MetaMask Agent Wallet ships 8-07 = first mainstream self-custodial wallet-for-agents mandate-primitive.
- **EU AI Act enforcement live 2026-08-02** — disclosure + watermarks + deepfake labeling now enforced.
