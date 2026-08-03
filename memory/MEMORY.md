# Long-term Memory
*Last consolidated: 2026-08-03*

## Current Goals
- **P0 ISS-029 fleet-wide usepod.ai 402 Payment Required 8-03** — every scheduled skill dispatched today (11:49Z + 18:27Z batches, ~18 skills) failed against `api.usepod.ai/v1/messages` with `Payment required. Retry the same request with an X-PAYMENT or PAYMENT-SIGNATURE header.` Only 8-03 success: btc-levels 04:50Z (pre-outage). 20:14Z batch dispatched, in_progress at reflect time. Operator-gated (payment top-up or proxy rotation). See [[iss-029]] / ISS-029.md.
- **ISS-028 kill-test workaround-chain n=20+ durable 12-UTC-day span 7-22 → 8-02** — 8-02 evening thought-review 21:35Z blocked heredoc-append (17th+ call-site NEGATIVE); no fresh 8-03 probes (fleet outage). PR #167 fix-scope-narrowness hypothesis still firm across 4-consec-UTC-day negative kill-test. Weekly-review 8-03 T-0 reopens root-cause investigation ask when fleet recovers.
- **12:00 UTC batch DARK day-37** — 8-skill cluster frozen since 2026-06-28 21:00Z. ISS-027 signature durable through 8-02 12:00Z clean same-slot token-alert (40th consec CG clean day).
- **ISS-025 hand-off T+5 day-20 SLIPPED** — cost-report weakest chronic-failure sr=0.11 (7/64) durable. Weekly-review 8-03 T-0 action #1 at Sunday-batch window.
- **PR queue at 3 through 8-03 morning** — **#165 d15 CONFLICTING** (7-19 17:38Z docs skill-graph, CLAUDE.md ~7d-past-touch escalation window OPEN since 8-02); **#171 ~60h** (7-31 18:07Z fix github-trending 12-17 cap, ci-skills-json FAILURE 3-consec-day); **#172 ~44h** (8-01 18:42Z fix daily-routine XAI-prefetch, ci-skills-json FAILURE 3-consec-day). Weekly-batch merge window opens today but blocked on operator + ISS-029 recovery.
- **ci-skills-json FAILURE 3-consec-day formal-pattern** — root cause identified 8-02 action-converter via `gh run view 30713133283 --log-failed`: `./generate-skills-json` not run by self-improve; both PRs fail same check. Fix path: add regen step to self-improve.md OR CI auto-regen bot. ISS-029 candidate downstream of formal-pattern promotion — awaits weekly-review 8-03 root-cause escalation.
- **Operator on-chain config day-58** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Operator-gated.
- **priorities.md 60d stale** — last reviewed 2026-06-04. Vault inbox 43d cold streak (last real capture 2026-06-21T08:32Z). Escalation candidate for weekly-review 8-03 refresh-ask.

## Recently Cleared
- **Sunday-slot cluster all-clean fire 8-02** — skill-graph 17:28Z NO_CHANGE + skill-update-check 19:39Z NO_LOCK + fork-cohort 19:52Z WENT_STALE Da6hkin + fork-skill-digest 20:03Z 78% sr (40 forks disabling action-converter) + skill-evals 22:39Z RECOVERED (2 fixed: token-alert + skill-health) + evening-recap 21:41Z clean = 6-of-6 Sunday cadence. Weekly-review 8-03 T-0 input population complete.
- **20:00Z heartbeat 8-02 +15min in-band** — cleanest 20:00Z-slot fire since 7-27 20:12Z baseline tick; breaks 08:00Z+14:00Z two-lag-slot pattern (20:00Z performs distinctly better).
- **16-consec heartbeat verdict-string identity across ~124h span** (7-27 20:12Z → 8-02 20:15Z) — memory-window-longest continuous chronic-degraded stretch. Composition-identity durable through 8-02 evening. No 8-03 tick yet due to ISS-029 outage.
- **CoinGecko clean-day streak d40 8-02** — 12:00Z token-alert clean fire = longest infrastructure durability streak in memory-window post-ISS-023.
- **github-issues 8-consec clean day 7-26 → 8-02** — via daily-routine sub-agent (`GITHUB_ISSUES_OK` streak).
- **[[MCP-enforcement-primitive-cluster]] rail extends d4 durable 8-02** — 7-29 MCP-infra + 7-31 MCP-plumbing + 8-01 MCP-production + 8-02 MCP-as-plumbing-vs-framework = 4-consec-UTC-day agent-buzz dominance. Rail crosses "durable" threshold.
- **[[fleet-relevance agent-thesis]] rail 17 → 18 consec-day 8-02** — ManageLife_io DeFi-agent teardown ($30M treasury vs -$191.7M holder loss) extends into agent-economic-outcome axis (was infra/memory/architecture-only before).
- **[[agent-buzz-engagement-drought]] rail candidate 3-consec durable 8-02** — outlier magnitude decay 711 → 65 → 44 = ~16× over 3 UTC-days on steady slate volume.
- **WELL vol-cliff d6 full-recovery to 0.890× baseline 8-02** — 7-31 0.059× nadir → 8-01 0.162× → 8-02 0.890× arc definitively confirms one-slot data-glitch, rules out durable participation-drain regime.
- **[[louround-single-thesis-cadence]] rail promoted candidate → durable n=3 8-02** — CODEC 7-31 + PENGU 8-01 + PUMP 8-02 = 3-consec-UTC-day single-voice dominance.
- **Σ-Mem paper picks per-skill sr% cohort infrastructure directly 8-02** — arXiv 2607.27958 formalizes per-peer trust as online-updated symmetric state = same shape as Aeon's per-skill sr% cohort. Extends [[fleet-relevance agent-thesis]].
- **Memory-primitive-paper streak 3-consec-UTC-day 8-02** — Memory Decoder 7-31 + Filesystem-Memory 8-01 + Σ-Mem 8-02.
- **TencentDB-Agent-Memory 8-02 = first hyperscaler agent-memory primitive to trend** — 227 today · 2.5× baseline · ACCELERATING.
- **Sub-25 github-trending fetch pattern 6-consec full-week 8-02** — 7-28 → 8-02 = permanent-shape promotion; hard-cap ~15 confirmed via 12-17 range.
- **iv-org/invidious 58× baseline 8-02** — highest ratio-spike memory-window.
- **07:00Z scheduler slot d4 RECOVERED 8-02** — 2nd clear via deciding-test PASSED (goal-tracker 18:44Z); regime rewrites 2-of-3-degraded → 3-of-4-intermittent-recovered.
- **security-digest quiet-cadence d2 + malware 159× collapse 8-02** — 0 fresh KEV + 0 fresh tracked-ecosystem = starkest quiet-day in memory-window post-318-batch peak.
- **First Termux-execution malware in memory-window digest 8-02** — wacve-utils (pip, kam193/OSSF).
- **Aeon-fleet clean d4 vs security-digest surface** (7-30 → 8-02).

## Fleet Health
See [[fleet]] for full snapshot. **P0 ISS-029 CRITICAL 8-03**: usepod.ai proxy 402 blocks all scheduled dispatches; last skill-health formal tick 8-02 18:23Z NOOP (hash `f0c415fd` 5-consec composition-identity ~120h span); zero drift 8-02 → 8-03 expected but no fresh tick yet. Prior 8-02 evening state: 0 CRITICAL / 17 DEGRADED / 13 WARNING / 10 HEALTHY / 3 NO_DATA · **13 open issues** (ISS-029 files at 14). **16-consec DEGRADED heartbeat verdict-string identity across ~124h span through 8-02 20:15Z** (memory-window record). Sandbox-truncation family **day-42** (T+17 day-19, ISS-025 T+5 SLIPPED). ISS-028 workaround-chain n=20+ durable 12-UTC-day span (7-22 → 8-02, thought-review 21:35Z 17th+ call-site NEGATIVE). ci-skills-json FAILURE 3-consec-day root-cause identified (self-improve skips `./generate-skills-json`).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, weekly-batch cadence, positive events log.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns.
- [Market context](topics/market-context.md) — Baseline snapshot (STALE ~18d/420h, crossed 2× threshold 8-01; refresh chained on next batch-dark thaw or manual invoke).
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. No 8-03 fresh prints (ISS-029 blocked 12:00Z slot). Last snapshot 8-02 12:00Z: 0/4 alerts (40th consec clean CG day), tape mixed-to-green vs 7-31's fully-red.

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 8-02 -0.58%, vol $896K = 0.890× baseline (**vol-cliff d6 full-recovery**, glitch-verdict confirmed) |
| MAMO    | mamo               | 15%           | 8-02 +1.67%, vol $750K = 0.941× baseline (**digestion band re-anchors d12** — distribution abort) |
| REPPO   | reppo              | 15%           | 8-02 +4.50%, vol $46K = 0.377× baseline (**price-without-participation widens d5** — fresh drought low) |
| GITLAWB | gitlawb            | 15%           | 8-02 -0.89%, vol $176K = 0.669× baseline (**base-building d10 2-consec noise-floor flatline**) |

## Recurring patterns (durable — brief pointers; details in topic files)
- **[[large-cap-single-day-flip]] rail n=4 durable 8-02** — BEAT (7-31 winner +17.7% → 8-01 sustained → 8-02 loser -10.5%) joins HOLO/PUMP/UNI. 4 pole-flips in 4 UTC-days. BEAT 3-day arc = new sub-pattern.
- **[[fleet-relevance agent-thesis]] rail 18-consec-day 8-02** — Σ-Mem paper (per-skill sr% infrastructure) + TencentDB (hyperscaler agent-memory) + ManageLife_io DeFi-agent economic-outcome axis.
- **[[MCP-enforcement-primitive-cluster]] rail 4-consec durable 8-02** — MCP-thesis dominance in agent-buzz feed. Definitional/framing sub-variant 8-02 (plumbing-not-framework).
- **[[agent-buzz-engagement-drought]] rail candidate 3-consec durable 8-02** — outlier magnitude decay ~16× over 3 UTC-days.
- **Memory-primitive-paper streak 3-consec-UTC-day** — Memory Decoder 7-31 + Filesystem-Memory 8-01 + Σ-Mem 8-02.
- **[[MCP-spec-maturity-vs-ecosystem-security]] rail n=3 8-02** — RufRoot CVE-2026-59726 on Ruflo joins 7-30 initial Ruflo + 8-01 dynatrace-mcp-server. 3 unauth-agent-framework-CVE-in-wild in 4 days.
- **[[DeepSeek-does-what-claude-refuses]] pattern candidate n=1 8-02** — Zhuhai actor + Hermes + DeepSeek → 460+ systems attacked where Claude/OpenAI refused. First model-refusal-behavior-differential exploited in-the-wild in memory-window.
- **[[open-web-postmortem-cadence]] rail candidate n=1 8-02 (hn-digest)** — Google/RSS 498pts + Atom-better-than-RSS.
- **Sub-25 github-trending fetch pattern 6-consec permanent shape 8-02** — hard-cap ~15 via 12-17 range. PR #171 acknowledges.
- **Parallel same-day 4×-burn extension shape n=1 8-02** — reverse-skill (335 → 1,320) + kaneo (194 → 760) both quadruple d1 fires.
- **Sub-floor-to-ACCELERATING same-repo reversal n=1 8-02** — github/copilot-sdk (7 → 142 = 20× d1).
- **[[skill-pack-primitive-rail]] compounding-on-viral 8-02** — zhaoxuya520/reverse-skill 4× burn after 8-01 domain-router-pack promotion. Rail n=6 durable.
- **ci-skills-json FAILURE 3-consec-day formal-pattern 8-02** — both #171 + #172 fail same check; root cause = self-improve skips `./generate-skills-json` regen. Fix path: add regen to self-improve.md OR CI auto-regen.
- **[[mass-typosquat-campaign-cadence]] sub-signal candidate 8-02** — 318-batch → 2 fresh in 24h = 159× collapse.
- **[[louround-single-thesis-cadence]] rail durable n=3 8-02** — CODEC + PENGU + PUMP.
- **[[launchpad-primitive]] rail n=3 candidate 8-02** — CODEC + frontierhood + Virtuals/Robinhood.
- **[[single-project-mass-disclose]] rail n=9/11 stable** — NLTK 4-CVE + Thumbor 6-CVE 8-01 pair-drop peak.
- **[[star-anomaly-rail]] n=7 + serial-drop sub-cluster crystallizing** — affaan-m/ECC 5-consec + mvanhorn/last30days-skill 4-consec.
- **[[embodied-agent-runtime-primitive]] rail n=3 7-31** — Gemini Robotics 2 + airi + speech-to-speech.
- **[[eth-lib-typosquat-campaign]] sub-class 7-31** — 7 ethers.js + fs-extra + socket.io.
- **[[open-voice-primitive-rail]] n=2 7-30** — VibeVoice + speech-to-speech.
- **[[AI-framework-attack-surface]] rail n=4 7-30** — @aws/agentcore + Claude Code CVE-2026-55607 + Langflow + LiteLLM. Extended by AutoGen-in-maintenance-mode 8-02 (rajeshberi).
- **[[network-perimeter-vendor-in-KEV]] cluster n=4 stable 8-02** — Fortinet + Arista + Cisco Secure FMC (all dedup'd, 0 fresh KEV = quiet-cadence d2).
- **Search-skill NO_GAP durability rail day-37 8-03** — fleet capability-complete on external-skill axis. Failures = infra (ISS-025/027/028/029), not gaps.
- **Chain-mode gap durable** — aeon.yml `chains: {}` inactive; daily-routine standalone fallback fires correctly each cycle.
- Claude Opus 5 shipped 7-24 = Aeon-fleet meta-signal. Claude Code computer-use gain 7-31.
- FTX $900M distribution 2026-07-31 = 5th round creditor payout, largest single supply event of quarter.
