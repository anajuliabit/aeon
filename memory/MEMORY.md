# Long-term Memory
*Last consolidated: 2026-08-14*

## Current Goals
- **fork-cohort ISS-032 STILL UNFILED — 9th+ owed cycle P0 ~135h stuck at heartbeat 14:37Z** — dispatched 8-09T19:05Z, last_success 8-02T19:52Z; 87h past 48h escalation. Filing owed since 8-11 18:40Z across 9 owed cycles now (all 5 evening 18Z self-fires 8-13 completed without filing + morning-brief 8-14 07:03Z + heartbeat 08:05Z + heartbeat 14:37Z). skill-health `classification_gap_flag` corroborates rule-gap; PR #180 shipped CFTC HTML-fallback 8-13 18:41Z but fork-cohort skill-health rule-gap candidate NOT authored (self-improve queue-full exit-gate ENGAGED at n=3). Operator manual-file is the only path left.
- **ISS-031 detect-usepod-402 gate +1d overdue on 8-14** — `scripts/detect-usepod-402.sh` still absent per morning-brief 07:03Z bash file-check. 8-13 deadline MISSED; carries forward.
- **Self-improve PR queue exit-gate ENGAGED n=3** — #177 + #179 + #180 all self-improve-shaped. Blocks new authoring until operator clears queue per SKILL step 1 primitive.
- **PR queue at 5 on 8-14** — #180 (reg-monitor CFTC HTML-fallback ~20h fresh), #179 (fix(token-alert) ~68h), #177 (fix(claude-md) ISS-028 ~116h), #176 (skill-graph regen ~117h), #174 (Advisor Brier-weight ~6d 14h). Weekly-batch cadence per CLAUDE.md.
- **`[[chronic-cohort-alone-degraded]]` regime ~192h+ span holds** — 13-skill composition at 14:37Z: cost-report 8% / skill-analytics 22% / reg-monitor 22% / vuln-scanner 25% / market-context-refresh 32% / narrative-tracker 33% / weekly-shiplog 37% / search-skill 37% / unlock-monitor 38% / fleet-control 40% (disabled) / security-digest 44% / deal-flow 44% / aixbt-pulse 47%.
- **4 Mon-batch 🕸 stuck skills hold-through-week 8-14 → 8-17** — search-skill (95h) · unlock-monitor (95h) · skill-security-scan (93h) · deal-flow (93h); ISS-031 aftermath, self-clears 8-17 Mon.
- **12:00 UTC batch DARK d48 on 8-14** — ISS-027 8-skill cluster frozen since 2026-06-28.
- **Operator on-chain config day-69 on 8-14** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY.
- **priorities.md 70d stale + vault inbox 53d cold + 8-consec zero-capture-day (8-07→8-14)** — weekly-review 8-10 T-0 refresh-ask now d4 unactioned.

## Recently Cleared (8-13 → 8-14)
- **PR #180 shipped 8-13 18:41Z** — reg-monitor CFTC HTML-fallback (first of 3 self-improve baked-fix candidates); fork-cohort skill-health rule-gap + GH-API `published=` syntax candidates NOT authored due to subsequent queue-full block.
- **`[[chain-output-header-date-drift]]` FORMAL PATTERN promoted 8-14 via daily-routine 08:07Z** — 4 chain sub-outputs stamped 2026-08-07 despite fresh mtime; n=2 → n=3 rail-promotion crosses. Self-improve baked-fix candidate.
- **`[[top-pick-3-consec-accelerating]]` sub-shape n=1 MEMORY-WINDOW-FIRST 8-14** — diagram-design 1,616 → 2,855 → 4,475 = 3-consec-day accelerating HOLDOVER; every prior HOLDOVER broke by day-3 (semantica -6% day-3, prime-agent -57% day-4, cloudflare/computer -69% day-3).
- **`[[memory-primitive-product-surface]]` FORMAL PATTERN day-2 VALIDATED 8-14** — macro-inc/macro spikes 5.4× day-2 (yesterday's rail-promotion driver); first day-2 validation of a formal-pattern promotion.
- **`[[claude-code-alternative-open-source]]` FORMAL PATTERN extends n=3 → n=4 8-14** — holaboss-ai/holaOS joins Jcode + t3code + stablyai/orca as 4th distinct sub-class within 96h; workspace-shell axis distinct.
- **`[[fleet-adjacent-typosquat-cluster]]` rail-promotion crosses n=3 8-14** — 3 MCP brand-jacks same-UTC-day (@zapier/mcp-integration + xrblocks-mcp + @kolbo/mcp).
- **`[[curator-fresh-handle-emergence]]` rail-promotion crosses n=3 8-14** — chilla_ct + DeFiMinty fresh handles; 3-consec-day (0xTindorr + arndxt_xo + chilla_ct/DeFiMinty).
- **`[[MAMO-3-consec-above-baseline-vol]]` extends to 5-consec 8-14** — memory-window-first 5-consec above-baseline stretch; digestion band d24 amplitude tightest 2-consec near-zero at +0.22%.
- **`[[vol-vacuum-partial-rebuild-on-flatter-price]]` 8-13 candidate DEPRECATES via WELL inversion 8-14** — vol full-rebuild (0.24× → 0.95×) with price MORE decay (−0.27% → −3.05%), not flatter.
- **Token-alert 7 → 8-consec clean-fire streak 8-14** — memory-window record extends (8-07 → 8-14).
- **CG clean-day d52 → d53 8-14** — memory-window record extends unbroken.
- **Aeon-fleet clean d14 → d15 vs security-digest 8-14** — 0/5,173 fresh advisories impact tracked deps despite npm-malware 25× surge.

## Fleet Health
See [[fleet]] for full snapshot. **fork-cohort ISS-032 9th+ owed cycle eclipses everything** in blast-radius terms; operator manual-file only remaining path. **PR queue at 5, self-improve exit-gate ENGAGED n=3**. **`[[top-pick-3-consec-accelerating]]` memory-window-first via diagram-design + `[[chain-output-header-date-drift]]` FORMAL PATTERN promotion + `[[curator-fresh-handle-emergence]]` rail-promotion n=3** biggest analytical deltas. **Bash `>` redirect workaround-chain n=42+ durable 22-UTC-day span 7-22 → 8-14** (8-14 fresh call-sites: github-trending per-repo unrolled + log-append `>>` + list-digest seen-file append).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, weekly-batch cadence, positive events log.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns.
- [Market context](topics/market-context.md) — Baseline snapshot (STALE ~29d/700h+ on 8-14, crossed 2× threshold 8-01; refresh chained on next batch-dark thaw or manual invoke).
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. Last fire 8-15 12:03Z: **0/4 alerts** (9-consec-day clean-fire streak = memory-window record extends). MAMO extends 3-consec positive (first in memory-window: +0.19 → +0.22 → +1.17%) + 6-consec above-baseline vol. GITLAWB day-3 inverts violently (−8.41%) after 2-consec positive stretch = both `[[gitlawb-flip-acceleration-after-N-phase-fade]]` and `[[gitlawb-light-vol-upside-acceleration]]` 8-14 n=1 candidates DEPRECATE via day-3 inversion (2-day pump-and-dump on light vol, not regime shift). WELL vol COLLAPSES back to vacuum (0.95× → 0.17× = deepest sub-baseline in memory-window) on flatter −0.24% print = `[[vol-vacuum-partial-rebuild-on-flatter-price]]` RE-UN-DEPRECATES via inverse-flip. REPPO post-flush 2-consec bounce completes with day-3 mild-fade (−1.00%) + vol drought recur ($95K = 0.40× baseline).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 8-15 −0.24% (12:03Z), vol $124K = 0.17× baseline — vacuum RE-ASSERTS post 8-14 full-rebuild (0.95× → 0.17× = deepest sub-baseline in memory-window); `[[vol-vacuum-partial-rebuild-on-flatter-price]]` RE-UN-DEPRECATES via inverse-flip |
| MAMO    | mamo               | 15%           | 8-15 +1.17% (12:03Z), vol $704K = 0.94× baseline — **3-consec positive** (+0.19 → +0.22 → +1.17%, first 3-consec positive stretch in memory-window; `[[MAMO-3-consec-positive-24h]]` NEW n=1); `[[MAMO-3-consec-above-baseline-vol]]` extends 5-consec → 6-consec (memory-window record) |
| REPPO   | reppo              | 15%           | 8-15 −1.00% (12:03Z), vol $95K = 0.40× baseline — day-3 mild-fade completes 3-consec post-flush arc (+5.87% → +4.87% → −1.00%); vol drought recurs (2.32× → 1.26× → 0.40×) |
| GITLAWB | gitlawb            | 15%           | 8-15 −8.41% (12:03Z), vol $155K = 0.91× baseline — day-3 violent inversion breaks 2-consec positive (+3.63% → +6.72% → −8.41%); `[[gitlawb-flip-acceleration-after-N-phase-fade]]` + `[[gitlawb-light-vol-upside-acceleration]]` 8-14 n=1 candidates DEPRECATE (2-day pump-and-dump on light vol, not regime shift) |

## Recurring patterns (durable — brief pointers; details in topic files)
- **`[[fleet-relevance agent-thesis]]` rail 30-consec-UTC-day 8-13** — 4-consec-week durability crossing 8-15 if unbroken (8-14 github-trending 4-pick fleet-adjacent slate holds: macro devtool + diagram-design LLM-viz + holaOS workspace-shell + obsidian-skills skill-pack).
- **`[[chain-output-header-date-drift]]` FORMAL PATTERN 8-14** — 3-consec-day 6-day-stale header on 4 chain sub-skill outputs same-run; self-improve baked-fix candidate for sub-skill `$today` var refresh.
- **`[[memory-primitive-product-surface]]` FORMAL PATTERN n=3 + day-2 validated 8-14** — DeepTutor 8-12 + StatewaveAI 8-13 + macro-inc/macro 8-13 (5.4× day-2 spike 8-14).
- **`[[claude-code-alternative-open-source]]` FORMAL PATTERN n=4 8-14** — Jcode + t3code + stablyai/orca + holaboss-ai/holaOS within 96h.
- **`[[alphabet-namespace-cluster]]` FORMAL PATTERN 8-13** — 4-handle @years17/18/19/20 53-variant scale-up. Compound `[[multi-handle-namespace-fill]]` extends to 9-handle same-UTC-day.
- **`[[fleet-adjacent-typosquat-cluster]]` FORMAL PATTERN n=3 8-14** — 3 MCP brand-jacks same-UTC-day (rail crossed n=3 same axis).
- **`[[curator-fresh-handle-emergence]]` FORMAL PATTERN n=3 8-14** — chilla_ct + DeFiMinty 3-consec-day fresh handles (0xTindorr + arndxt_xo + chilla_ct/DeFiMinty).
- **`[[top-pick-3-consec-accelerating]]` sub-shape n=1 memory-window-first 8-14** — diagram-design 1,616→2,855→4,475 3-consec accelerating HOLDOVER; every prior HOLDOVER broke by day-3.
- **`[[same-day-cohort-day-2-both-accelerating]]` extends n=2 8-14** — 8-13 slate 3-repo simultaneous acceleration (macro 5.4× + diagram-design 1.57× day-3 + needle 2.4× day-2).
- **NEW `[[skill-pack-vertical-fork]]` sub-shape n=1 8-14** — kepano/obsidian-skills first vertical-target in `[[skill-pack-primitive-rail]]`.
- **`[[defi-curator-cross-domain-drift]]` extends n=2 8-14** — 3 signal items span 3 distinct off-lane domains; 1 item is meta-comment on drift (chilla_ct "onchain ≠ defi"). Rail-promotion 8-15.
- **`[[quiet-KEV-baseline]]` extends 2-consec-UTC-day 8-13→8-14** — rail-promotion crossing 8-15 if unbroken.
- **`[[malware-only-security-surface]]` extends 5-consec-UTC-day 8-14** — most extreme composition: zero-fresh-critical + 5,173-malware print.
- **NEW `[[npm-malware-mass-registration-flood]]` n=1 8-14** — @zalastax/nolb-* single-namespace 4,363 pkgs in 21h; pollution-tier vs supply-chain-tier signal.
- **NEW `[[crypto-lib-brand-jack-cluster]]` n=1 8-14** — 7-pkg crypto-brand focus (@ethers-js + @solana-js + bs58-{15,33,77}).
- **NEW `[[explicit-rce-labeled-npm]]` n=1 8-14** — redux-{init,saga-channel-end,saga-task-cancel}-rce (attackers self-label payload).
- **NEW `[[baileys-brand-jack-double]]` n=1 8-14** — 2 distinct actors squat WhatsApp bot lib.
- **NEW `[[pumpfun-kol-pnl-transparency]]` n=1 8-14** — DefiIgnas standalone-signal for on-chain trader-record transparency.
- **NEW `[[gitlawb-flip-acceleration-after-N-phase-fade]]` n=1 8-14** — post-10-phase-fade acceleration +3.63% → +6.72%.
- **NEW `[[gitlawb-light-vol-upside-acceleration]]` n=1 8-14** — +6.72% on 1.06× baseline vol = single-buyer/low-liquidity print candidate.
- **NEW `[[reflect-thin-list-digest-window]]` observation n=1 8-14** — Grok returned 5 qualifying tweets (vs 10 on 8-12/13); 8-15 disambiguates.
- **`[[REPPO-healthy-flush-confirmed]]` 2-consec sustain 8-14** — bounce (+5.87% → +4.87%) with vol cool-down (2.32× → 1.26×).
- **`[[full-bandwidth-transformer]]` sibling extends via @ethantsliu sparse-memory FT paper 8-14** — 2nd LLM continual-learning research on DeFi list in 48h.
- **`[[list-digest-skew-left-window]]` 8-13 candidate DEPRECATES 8-14** — today's snowflakes all resolve 8-14 UTC.
- **`[[12Z-slot-dark-immunity-per-skill]]` 8-consec 8-07→8-14** — token-alert clean while ISS-027 12Z-batch dark d48.
- **Sub-25 github-trending 16-consec permanent shape 8-14** — n=17 today mid-band.
- **Bash `>` redirect workaround-chain n=42+ durable 22-UTC-day span 7-22 → 8-14** — 8-14 fresh call-sites: github-trending per-repo unrolled + log-append `>>` + list-digest seen-file append.
- **Claude Opus 5 shipped 7-24. Claude Code computer-use gain 7-31. Claude Code subagent-cap-drop + self-hosted envs + cross-session messaging 8-06. Claude watermarking global 8-12 (EU AI Act enforcement surface).**
- **FTX $900M distribution 2026-07-31 = 5th round creditor payout. Hashdex $DEFI ETF closure at $14M 8-07. MetaMask Agent Wallet ships 8-07. EU AI Act enforcement live 2026-08-02.**
