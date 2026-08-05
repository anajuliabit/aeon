# Long-term Memory
*Last consolidated: 2026-08-04*

## Current Goals
- **ISS-029 EFFECTIVELY RECOVERED 8-04** — usepod.ai 402 payment gate lifted between 8-03 18:27Z (last fresh 402) and 20:14Z (first clean dispatch). 20-of-20 post-20:14Z fires clean through 8-04 16:33Z. Kept OPEN pending operator confirmation of usepod billing status; no fresh 402 errors observed. See [[iss-029]].
- **P0 ISS-030 cost-report SDK opt-in mismatch NEW 8-04** — sole ISS-029 survivor. Distinct signature `terminal_reason: api_error / fast_mode_disabled_reason: sdk_opt_in_required` (not usepod 402, not sandbox-truncation). consec=17 sr=0.09 (7/75), last success 2026-07-27T08:47Z (8d ago). Filed today. Weekly cost visibility blind. See [[iss-030]].
- **ISS-028 kill-test workaround-chain n=22+ durable 13-UTC-day span 7-22 → 8-04** — 8-04 heartbeat 14:45Z + github-trending 10:14Z + token-alert 12:17Z + security-digest 14:47Z all held clean via WebFetch + Write-tool + Edit-tool + `--paginate` + URL-encoded `%3E` pattern. PR #167 fix-scope-narrowness hypothesis firm across 5-consec-UTC-day. Weekly-review 8-10 T-6 reopens root-cause investigation ask.
- **12:00 UTC batch DARK day-38** — ISS-027 8-skill cluster frozen since 2026-06-28. Post-ISS-029 recovery did NOT thaw the 12:00Z cluster (separate cause). 8-04 12:00Z token-alert clean (**CG clean-day d41**) confirms slot itself works; ISS-027 is scheduler-side gap for the 8-skill cluster.
- **ISS-025 hand-off T+5 day-21 SLIPPED** — sandbox-truncation family durable. cost-report weakest chronic sr=0.09 but signature is now ISS-030 (not ISS-025). Weekly-review 8-10 T-6 milestone.
- **PR queue at 4 through 8-04 morning** — **#165 d16 CONFLICTING** (7-19 17:38Z docs skill-graph, CLAUDE.md ~7d-past-touch escalation window OPEN); **#171 ~4d** (7-31 18:07Z fix github-trending 12-17 cap, ci-skills-json FAILURE); **#172 ~3d** (8-01 18:42Z fix daily-routine XAI-prefetch, ci-skills-json FAILURE); **#173 fresh** (8-03 20:17Z `fix(claude): require skills.json regen when editing SKILL.md` — targets shared ci-skills-json root cause, if merged unblocks #171/#172 at 8-10 Sunday-batch).
- **ci-skills-json FAILURE root cause SOLVED 8-03 20:17Z** — PR #173 encodes self-improve `./generate-skills-json` regen requirement. If merged, unblocks #171/#172 at next Sunday-batch (8-10).
- **Operator on-chain config day-59** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Operator-gated.
- **priorities.md 61d stale** — last reviewed 2026-06-04. Vault inbox 44d cold streak (last real capture 2026-06-21T08:32Z). Weekly-review 8-10 refresh-ask.

## Recently Cleared
- **ISS-029 fleet-wide recovery 8-03 20:14Z → 8-04 16:33Z** — 20-of-20 post-recovery dispatches clean across ~20 UTC-hours. usepod 402 gate lifted; no fresh 402 errors observed today. Effectively resolved (kept OPEN pending operator confirmation).
- **16-consec heartbeat verdict-string durability rail CLOSES at ~124h span** — 7-27 20:12Z → 8-02 20:15Z memory-window record broken by post-ISS-029 composition-shift (chronic-cohort still degraded but consec_failures across cohort all reset from 3-9 range to 0 except cost-report=17). New "chronic-cohort-alone-degraded" verdict-string signature begins 8-04.
- **CoinGecko clean-day streak d41 8-04** — 12:19Z token-alert clean fire = longest infrastructure durability streak in memory-window post-ISS-023 continuation; CG-side infrastructure unbroken through ISS-029 blackout (block was upstream gateway).
- **github-issues 9-consec clean day 7-26 → 8-03** (via daily-routine sub-agent, `GITHUB_ISSUES_OK` streak).
- **136-package fresh 8-04 malware batch = memory-window #2 largest single-day** — behind 8-01's 318-batch only; qualitatively distinct signature (coordinated corp-scope + npm ecosystem-core compromise vs 8-01 mass-typosquat volume). keyv/cacheable 25+ pkgs = first top-100-npm-package attack in memory-window; @servicetitan+@onereach+@or-sdk 88-pkg = new `[[enterprise-corp-scope-dep-confusion]]` sub-class; coldcard-helpers+psbt-utils+psbt-helpers+bip39-generator 4-pkg = new `[[crypto-wallet-npm-malware-cluster]]` rail candidate parallels Coldcard $89M escalation.
- **Flowise agent-framework double-drop 8-04** — CVE-2026-69251 (RCE via TypeORM auth+PoC fix 3.1.3) + CVE-2026-69250 (unauth OAuth2 SSRF PoC fix 3.1.3) extends [[AI-framework-attack-surface]] rail to 5th unauth-agent-framework-CVE in memory-window (after Claude Code + Ruflo + Langflow + LiteLLM + dynatrace-mcp + AutoGen-maintenance).
- **cryptography same-project-double-critical 8-04** — CVE-2026-69247 Bleichenbacher PKCS#7 (fix 50.0.0) + CVE-2026-69249 path-building DoS (no-fix). Second same-project-double-critical of 8-04 (Flowise being #1). cryptography is transitive dep of paramiko/pyopenssl/many.
- **sequelize CVSS 9.8 public PoC 8-04** — CVE-2026-69240 Oracle SQL-injection fix 6.37.4. Rare PATCH-TODAY qualifier via CVSS-plus-PoC rule (most Patch-Today items are KEV or malware). Top-3 npm ORM after Prisma/TypeORM.
- **Aeon-fleet clean d6 vs security-digest surface** (7-30 → 8-04).
- **PR #173 opened 8-03 20:17Z** — `fix(claude): require skills.json regen when editing SKILL.md` targets shared ci-skills-json root cause on #171/#172. Sunday-batch T-6.
- **Weekly-review 8-03 shipped** — TL;DR: 313 workflow runs / 62 failures / 80.2% success -18.8pp WoW; 87% of failures on 8-03 alone from ISS-029 usepod cascade. Top action: file ISS-029 (SHIPPED same day via reflect). 4 PRs merged this week (#167/#168/#169/#170). Article: `articles/weekly-review-2026-08-03.md`.
- **skill-health formal tick 8-03 20:16Z** — first fresh formal-tick since 7-31; hash `29af7ab7` fresh identity (breaks `f0c415fd` 5-consec since 7-28). Classification: 11 CRITICAL (usepod-affected cohort) + 8 DEGRADED + 15 WARNING + 6 HEALTHY + 3 NO_DATA; **14 open issues** (ISS-029 filed). Systemic: ISS-029 usepod 402 blast.
- **[[MCP-enforcement-primitive-cluster]] rail extends d4 durable through 8-02** — 4-consec-UTC-day agent-buzz dominance; no 8-03 fresh datapoint (ISS-029 blocked agent-buzz).
- **[[fleet-relevance agent-thesis]] rail 18 → 19-consec-day 8-04** — TencentDB HOLDOVER 4.8× extension keeps hyperscaler-agent-memory datapoint burning.
- **[[memory-primitive-paper streak]] 4-consec-UTC-day 8-03** — Memory Decoder 7-31 + Filesystem-Memory 8-01 + Σ-Mem 8-02 + CAPA 8-03 (first 4-day paper-thematic streak in memory-window; ISS-029 blocked 8-04 paper-pick, streak counter frozen).
- **[[large-cap-single-day-flip]] rail extends n=4 → n=5 8-03** — UAI (8-02 +39.1% #1 winner → 8-03 -31.4% #1 loser) joins BEAT/HOLO/PUMP/UNI. 5 pole-flips in 5 UTC-days.
- **[[AI-slop-in-security-pipelines]] rail NEW candidate 8-03** — jfrog SQLite-CVE-slop piece + HF CEO accountability call = 2-story ai-safety-of-agent-tooling cluster on hn-digest + tweet-roundup. Distinct from [[AI-framework-attack-surface]] (tracks CVEs *IN* agent frameworks; this tracks CVE-slop *FROM* agents into other pipelines).
- **Same-day dual-HOLDOVER extension shape memory-window first 8-04** — reverse-skill (1,320 → 2,446 = 1.85×) + TencentDB (227 → 1,090 = 4.8×) both extend yesterday's featured fires on same slate.
- **First [[deepseek-primitive-cluster]] rail candidate n=2 8-04** — antirez/ds4 (local inference engine C) + esengine/DeepSeek-Reasonix (DeepSeek-native coding agent Go). Two DeepSeek-primitive picks in one slate = memory-window first.
- **First antirez github-trending appearance in memory-window 8-04** — Redis creator's zero-dep local-inference C engine for DeepSeek 4 hits slate. Author-quality-override activated; new keep-criterion sub-pattern.
- **airllm 45× spike 8-04 = second-largest ratio-spike memory-window** — behind 8-02 iv-org/invidious 58× only. Pattern: RETURNING mature-repos deliver biggest ratio-spikes when they hit fresh viral moments.
- **Sub-25 github-trending fetch pattern extends 6-consec → 7-consec (n=16 8-04, top-edge)** — PR #171 12-17 cap assertion still holds.
- **WELL vol-cliff regime rewrites 8-04** — 8-02 "one-slot data-glitch full-recovery" verdict has to give ground: 0.111× resumes cliff-shape after single-day recovery. 3-day arc (7-31 → 8-01 → 8-02) reads as partial mean-revert inside a durable participation-drain regime candidate, not a full glitch reversal.
- **GITLAWB 9-day base breaks up +9.62% 24h 8-04** — 7-24 → 8-01 give-back arc + 8-02 flatline resolves upward with participation lift 0.669× → 0.924×. First constructive candlestick since 7-23 breakout.
- **REPPO 3-consec green arc reverses inside 48h gap** — -8.23% log-to-log = 4th-largest single-print reversal in memory-window; participation re-engages on the give-back (drought regime candidate ending).
- **MAMO digestion band deepens to memory-window flatest print 8-04** — +0.08% 24h thinnest close-to-close of any print; distribution-abort holds firm.

## Fleet Health
See [[fleet]] for full snapshot. **ISS-029 EFFECTIVELY RECOVERED 8-04**: 20-of-20 post-20:14Z-8-03 dispatches clean through 8-04 16:33Z. **P0 ISS-030 NEW 8-04**: cost-report distinct-signature `sdk_opt_in_required`, consec=17 sr=0.09, only ISS-029 survivor. **skill-health formal tick 8-03 20:16Z**: fresh hash `29af7ab7` breaks `f0c415fd` 5-consec (~120h span 7-28 → 8-02); 11 CRITICAL (usepod cohort, since recovered) + 8 DEGRADED + 15 WARNING + 6 HEALTHY + 3 NO_DATA · **15 open issues** (ISS-030 files today at 15). **16-consec DEGRADED heartbeat verdict-string identity CLOSES** at ~124h span through 8-02 20:15Z (memory-window record); new "chronic-cohort-alone-degraded" signature begins 8-04. Sandbox-truncation family **day-43** (T+18 day-20, ISS-025 T+5 d21 SLIPPED — but note cost-report failure surface has shifted to ISS-030 signature). ISS-028 workaround-chain n=22+ durable 13-UTC-day span (7-22 → 8-04). ci-skills-json root cause SOLVED via PR #173.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, weekly-batch cadence, positive events log.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns.
- [Market context](topics/market-context.md) — Baseline snapshot (STALE ~19d/456h, crossed 2× threshold 8-01; refresh chained on next batch-dark thaw or manual invoke).
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. Last snapshot 8-05 12:34Z: 0/4 alerts (**CG clean-day d42** — longest infra durability streak in memory-window, unbroken through ISS-029 blackout). Tape mixed: WELL vol-recovery flips 8-04 drain-regime verdict, REPPO drought re-engages, GITLAWB breakout aborts <24h, MAMO digestion-band flatest 2-consec back-to-back.

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 8-05 +0.65%, vol $664K = 1.271× baseline (**vol-cliff regime rewrites again** — 8-04 drain-regime candidate flips back to intermittent-glitch; 7.12× rebound single-day resumes 8-02 "one-slot glitch" reading) |
| MAMO    | mamo               | 15%           | 8-05 +0.47%, vol $699K = 0.928× baseline (**digestion band d15 memory-window flatest 2-consec back-to-back** — 8-04 +0.08% + 8-05 +0.47%; distribution-abort deepens into 15-day flatline) |
| REPPO   | reppo              | 15%           | 8-05 -2.51%, vol $41K = 0.442× baseline (**drought re-engages after 1-day recovery** — 3-consec-green → 2-consec-red arc, book empties on continuation give-back, matches 8-02 trough shape) |
| GITLAWB | gitlawb            | 15%           | 8-05 -7.08%, vol $184K = 0.863× baseline (**breakout aborts one-day-only** — -7.26% log-to-log wipes yesterday's +9.62% within 24h, base-building resumes at deeper floor) |

## Recurring patterns (durable — brief pointers; details in topic files)
- **[[large-cap-single-day-flip]] rail n=5 durable 8-03** — UAI joins BEAT/HOLO/PUMP/UNI. 5 pole-flips in 5 UTC-days.
- **[[fleet-relevance agent-thesis]] rail 19-consec-day 8-04** — TencentDB HOLDOVER 4.8× extension.
- **[[MCP-enforcement-primitive-cluster]] rail 4-consec durable through 8-02** — MCP-thesis dominance in agent-buzz feed; 8-03 blocked (ISS-029), 8-04 tick pending.
- **[[memory-primitive-paper streak]] 4-consec-UTC-day 8-03** — Memory Decoder → Filesystem-Memory → Σ-Mem → CAPA; first 4-day paper-thematic streak. 8-04 blocked by ISS-029-morning-carry (stale-outputs), counter effectively frozen.
- **[[AI-framework-attack-surface]] rail extends 8-04** — Flowise double-drop CVE-2026-69251 + CVE-2026-69250 = 5th unauth-agent-framework-CVE in memory-window (Claude Code + Ruflo + Langflow + LiteLLM + dynatrace-mcp + AutoGen-maintenance + Flowise).
- **[[MCP-spec-maturity-vs-ecosystem-security]] rail n=3 stable 8-02** — RufRoot + Ruflo + dynatrace-mcp-server; 3 unauth-agent-framework-CVE-in-wild in 4 days.
- **[[enterprise-corp-scope-dep-confusion]] NEW sub-class 8-04** — @servicetitan 47 + @onereach 23 + @or-sdk 18 = 88-pkg SaaS corp-scope batch; sibling to `[[fintech-corp-scope-dep-confusion]]` 8-01. Largest single-day corp-scope batch in memory-window.
- **[[crypto-wallet-npm-malware-cluster]] NEW rail candidate n=1 8-04** — coldcard-helpers + psbt-utils + psbt-helpers + bip39-generator 4-pkg = coordinated crypto-seed/PSBT signing malware; parallels operator morning-brief Coldcard $89M escalation.
- **[[AI-slop-in-security-pipelines]] rail NEW candidate n=1 8-03** — jfrog SQLite-CVE-slop + HF CEO accountability call = 2-story ai-safety-of-agent-tooling cluster. Distinct from [[AI-framework-attack-surface]].
- **[[louround-single-thesis-cadence]] rail durable n=4 8-03** — CODEC + PENGU + PUMP + IO ($IO thesis 4th consec).
- **[[deepseek-primitive-cluster]] rail candidate n=2 8-04** — antirez/ds4 + esengine/DeepSeek-Reasonix. Two DeepSeek-primitive picks in one slate.
- **[[skill-pack-primitive-rail]] compounding-on-viral 8-04** — zhaoxuya520/reverse-skill 3-consec-day burn (335 → 1,320 → 2,446). Same-day dual-HOLDOVER extension shape (reverse-skill + TencentDB) = memory-window first.
- **[[agent-buzz-engagement-drought]] rail candidate 3-consec durable 8-02** — outlier magnitude decay ~16× over 3 UTC-days; 8-03 blocked, 8-04 pending.
- **[[network-perimeter-vendor-in-KEV]] cluster n=4 stable** — Fortinet + Arista + Cisco Secure FMC + N-central (8-03 fresh, adds `[[RMM-platform-in-KEV]]` sub-class candidate).
- **[[single-project-mass-disclose]] rail n=9/11 stable** — NLTK 4-CVE + Thumbor 6-CVE 8-01 pair-drop peak; Flowise 2-CVE + cryptography 2-CVE 8-04 = 2 same-project-double-critical instances in single day.
- **Sub-25 github-trending fetch pattern 7-consec permanent shape** — 7-28 → 8-04 (skip 8-03 ISS-029 blackout). Hard-cap ~15 via 12-17 range. PR #171 acknowledges.
- **Search-skill NO_GAP durability rail day-38 8-04** — fleet capability-complete on external-skill axis. Failures = infra (ISS-025/027/028/029/030), not gaps.
- **Chain-mode gap durable** — aeon.yml `chains: {}` inactive; daily-routine standalone fallback fires correctly each cycle.
- Claude Opus 5 shipped 7-24 = Aeon-fleet meta-signal. Claude Code computer-use gain 7-31.
- FTX $900M distribution 2026-07-31 = 5th round creditor payout, largest single supply event of quarter.
