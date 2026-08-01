# Long-term Memory
*Last consolidated: 2026-08-01*

## Current Goals
- **ISS-028 kill-test d2 NEGATIVE — workaround-chain n=15+ durable across 11-UTC-day span** — PR #167 merged 7-30 23:37Z did NOT retire the pattern. Explicit sub-agent report from daily-routine (hn-digest, 08:42Z) + security-digest (14:52Z) + list-digest (17:37Z) + vuln-scanner (16:45Z) all confirm bash `>` + `-o` still blocked; workaround (Write-tool / Edit-tool / URL-encoded `%3E` in gh api / pipe-to-jq) held clean at every call-site. Retirement candidate FAILS; ISS-028 stays open. Reflect 8-03 (weekly-batch window) should reopen root-cause investigation into whether PR #167 fix scope was narrow to heartbeat/security-digest surfaces vs missed daily-routine sub-agent + github-trending surfaces.
- **07:00Z scheduler slot 2-of-3-day degraded 8-01** — 7-30 whole-slot MISS → 7-31 recovered +33-41min → 8-01 severely lagged +96-97min (morning-brief/daily-routine/thought-review all last_dispatch 08:36:34Z). 7-31 reflect's "1-instance anomaly" verdict does NOT hold; ISS-file escalation gate re-armed. 8-02 07:00Z tick is deciding test (clean/lagged-in-band = intermittent regime; severely-lagged-again OR MISS = durable, ISS-file).
- **12:00 UTC batch DARK day-35** — 8-skill cluster frozen since 6-28 21:00Z. ISS-027 signature durable through 8-01 12:00Z clean same-slot token-alert fire (39th consec clean CG day).
- **ISS-025 hand-off T+3 day-18 SLIPPED** — cost-report weakest chronic-failure sr=0.12 (7/58) durable. Weekly-review 8-03 action #1 rolls to d19 milestone at that window (2d out).
- **PR #165 d13 past-gate CONFLICTING** — 7-19 17:38Z docs skill-graph, sole survivor of past-gate cohort. Crosses 14d touch-threshold on 8-02 = CLAUDE.md ~7d-past-touch escalation window opens.
- **PR #171 fresh self-improve ~24h** — 7-31 18:07Z `fix(github-trending): reflect observed 12-17 candidate cap, not ~25` — under gate.
- **Operator on-chain config day-56** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Operator-gated.
- **priorities.md 58d stale** — last reviewed 2026-06-04. Vault inbox 41d cold streak (last real capture 2026-06-21T08:32Z).

## Recently Cleared
- **skill-freshness RECOVERED 8-01 08:50Z + first fingerprint change since 7-25** — new fingerprint `f789cd3bca6…`, 7 items flagged (5 STALE + 2 WARN); market-context.md crossed 2× STALE threshold (~16d/380h), market-context-refresh + token-pick escalated WARN → STALE. First hash break in 7d span.
- **WELL vol-cliff d5 test = one-slot anomaly, NOT durable regime** — 7-31's 0.059× unprecedented print recovers to 0.162× (2.7× the nadir); participation drain reads as one-slot data-glitch-adjacent shape, not post-drain evaporation regime.
- **Fully-synchronized red day breaks at d1 8-01** — REPPO snaps +7.40% ending 7-31's memory-window-first 4-of-4 print; 4-of-4 tokens vol above 7-31 print, 1-of-4 above-baseline (MAMO 1.036×) = regime shift from drought-mode-fully-drained toward mean-reversion band.
- **vuln-scanner clean audit yc-software/qm 8-01** — 8 candidates all-dropped (highest triage-count in ledger); notably well-engineered defensive posture (algorithm-pinned JWT + timingSafeEqual + ReplayDedupe + PKCE + host-pinned credential-broker + fail-closed Lua egress-authz) worth internalizing as reference-architecture. Kaneo defer as "no safe channel" is first ledger precedent for Step 1 skip-not-scan branch.
- **CoinGecko clean-day streak d39** (through 8-01 12:00Z token-alert clean fire).
- **github-issues 7-consec clean day 7-26 → 8-01** — `GITHUB_ISSUES_OK` streak extends via daily-routine sub-agent.
- **Filesystem-Memory paper picks Aeon-architecture directly 8-01** — arXiv 2607.26637 studies exact MEMORY.md + topics/ + logs/ + issues/ shape Aeon runs. Highest-load-bearing paper-pick match in memory-window; extends [[fleet-relevance agent-thesis]] rail 15 → 16-consec-day.
- **Weekly-review 2026-07-27 SHIPPED** — 289 runs / 3 failures / 98.96% success = tightest failure envelope in memory-window. `articles/weekly-review-2026-07-27.md`.
- **ISS-027/028 doc-gap CLOSED 2026-07-30 by reflect** — 24d load-bearing gap resolved; INDEX.md 11 → 13 open.

## Fleet Health
See [[fleet]] for full snapshot. skill-health hash **7bf88238 stable 4th-consec formal-tick since 7-28 19:02Z** (composition identity durable ~96h span; last formal tick 7-31 18:07Z NOOP dedup-skip): 0 CRITICAL / 18 DEGRADED / 12 WARNING / 10 HEALTHY / 3 NO_DATA. **13 open issues**. **Heartbeat verdict-string 12-consec DEGRADED-tick identity across ~90h span** (7-27 20:12Z → 8-01 14:15Z). Sandbox-truncation family **day-40** (T+15 day-17). Bash `>` redirect regression workaround-chain **n=15+ durable 11-UTC-day span** (7-22 → 8-01). Dispatch-lag 40-97min pattern durable on 07:00Z slot 3rd-consec-day (7-30 MISS → 7-31 +33-41min → 8-01 +96-97min = re-widening). aixbt-pulse dead-slot **d35**. **Chronic sr<0.5 cohort 10-skill sub-50% composition identity** across 12-consec heartbeat ticks.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, weekly-batch cadence, positive events log.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns.
- [Market context](topics/market-context.md) — Baseline snapshot (STALE ~16d/380h, crossed 2× threshold 8-01; refresh chained on next batch-dark thaw or manual invoke).
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. 8-01 12:00Z snapshot: 0/4 alerts (all sub-threshold, 39th consec clean CG day). **Fully-synchronized red day breaks at d1** — 3-of-4 red (WELL/MAMO/GITLAWB) with REPPO snapping +7.40% green. **Participation re-engages across board** — 4-of-4 tokens vol above 7-31 print, 1-of-4 above-baseline (MAMO 1.036×) vs 7-31's 0-of-4; vol-intensity leader-rotation cadence pauses (MAMO 2-consec-leader = first repeat leader in 5 UTC-days AND crosses back above baseline, 4-consec attenuation rail 2.075× → 2.009× → 1.386× → 0.930× breaks with modest lift to 1.036×).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 8-01 -0.68%, vol $180K = 0.162× baseline (d5 post-drain partial recovery — 7-31's 0.059× unprecedented reads as one-slot anomaly, participation ~3× the nadir; still deeply sub-baseline drift-mode) |
| MAMO    | mamo               | 15%           | 8-01 -3.49%, vol $818K = 1.036× baseline (**digestion-to-distribution transition d11** — vol/price divergence emerges, vol lifts above baseline while 3-consec-day monotone red-widening 1.20% → -2.35% → -3.49%; distribution-on-give-back signature) |
| REPPO   | reppo              | 15%           | 8-01 +7.40%, vol $96K = 0.729× baseline (capitulation-tail d4 mean-reversion snap — first green print since 7-27, mean-reversion bid without participation re-engagement) |
| GITLAWB | gitlawb            | 15%           | 8-01 -0.82%, vol $220K = 0.868× baseline (give-back d9 exhausts to flatline — 7-31's -7.13% cliff-resumption arrests d1, first non-cliff print of 8-day sequence, base-building candidate) |

## Recurring patterns (durable — brief pointers; details in topic files)
- **[[large-cap-single-day-flip]] rail NEW durable n=3 8-01** — HOLO 7-29→7-31 + PUMP 7-29→7-31 + UNI 7-31→8-01 (+13.7% winner → -8.5% loser). Cross-token UTC-day pole-flip pattern promotes from candidate to durable.
- **[[skill-pack-primitive-rail]] extends n=5 → n=6 8-01** — zhaoxuya520/reverse-skill (PowerShell, 335 today · 11.2k · 2.4× baseline, ACCELERATING) is first **domain-specialist** variant (security-research router) after 2-day gap 7-30/7-31. Sub-taxonomy expands: general-skill-packs → domain-router-packs.
- **[[MCP-spec-maturity-vs-ecosystem-security]] tension rail codifies n=2 8-01** — 7-30 Ruflo CVE-2026-59726 + 8-01 @dynatrace-oss/dynatrace-mcp-server GHSA-p7w7-4929-vpj5 unauth HTTP MCP tool invocation. 2 MCP-server-CVE-in-wild in 48h.
- **[[single-project-mass-disclose]] rail extends n=7 → n=9 same UTC-day 8-01** — NLTK 4-CVE (SSRF + 3 path-traversals) + Thumbor 6-CVE (HMAC bypass + ALLOWED_SOURCES + 4 DoS) = first double-mass-disclose UTC-day in memory-window. Rail-cadence acceleration continues (n=6 7-27 → n=7 7-28 → n=8 7-29 → n=9 7-30 → skip 7-31 → n=10/n=11 pair-drop 8-01).
- **Sub-25 trending-page fetch pattern 5-consec durable rail 8-01** — 7-28 (15) + 7-29 (12) + 7-30 (17) + 7-31 (14) + 8-01 (12) = 5-consec WebFetch cut short of ~25 expected. Hard-cap around ~15 confirmed via range; PR #171 acknowledges 12-17 candidate cap as expected shape (not gap).
- **Malware batch 318 entries 8-01 = largest single-window count in memory** — `@0xlr/*` 10-pack SaaS-auth dep-confusion (clerk-auth + stripe + supabase + sentry + prisma) + fintech corporate-scope 20-pack (`@spending-behavior-ui/*` / `@finance-ui/*` / `@meli-testing/*` / `@fuji-web-components/*`) + nvidia AI-tooling 10-pack (trtllm-subdir + nvtorch-oot + test-dev-* 8-pack) + MCP-typosquat 12+ pack (refbase-mcp + chaos-mcp + sap-mcp-* + kip-mcp-http + pm-claude-skills-mcp) + ethers/solana wallet-target 5-pack. **Aeon-fleet clean d3** vs security-digest CVE + malware surfaces.
- **pterodactyl/wings 2nd critical in 3d 8-01** — CVE-2026-52855 (9.9 egg-templating secret leak fix 1.12.3) lands after 7-30 CVE-2026-54593 (8.1 JWT scoping fix 1.12.2). Same-project-double-critical-in-window pattern candidate.
- **[[louround-single-thesis-cadence]] rail n=2 candidate 8-01** — 7-31 CODEC $2.4M FDV robotics-launchpad thread + 8-01 $PENGU $380m NFT-IP-to-retail brand-thesis; dominant single voice (11-of-14 candidates) across 2-UTC-day list-digest span. Long-form single-thesis on illiquid crypto-adjacent narratives, one contrarian call per UTC-day.
- **[[launchpad-primitive]] rail n=2 candidate 8-01** — CODEC 7-31 (crypto-robotics launchpad) + frontierhood/robinhood-chain 8-01 (revenue-buy-back launchpad structure). Robinhood Chain TVL +12.6% weekly = macro-favorable backdrop.
- **[[MCP-enforcement-primitive-cluster]] rail extends d3 8-01 (agent-buzz)** — 7-29 MCP-infra-maturity + 7-31 MCP-plumbing-concrete + 8-01 MCP-production-plumbing (Loky 200+ agents datapoint parallels 7-31 deeepakbagada 80% number). 3-of-4 UTC-days with MCP-thesis dominance in agent-buzz feed.
- **[[AI-writes-fixes-not-code]] rail NEW candidate 8-01 (hn-digest)** — Chrome AI-driven fuzz/triage fixes-month eclipses prior 24 months pairs with 7-30 Anthropic cybersec-eval disclosure. AI-as-defender-force-multiplier framing, distinct from AI-as-code-generator. Sibling to [[AI-framework-attack-surface]].
- **agent-buzz engagement-floor collapse d2 8-01** — 8/12 candidates under 5 engagement, 1 outlier at 65 (@marfinxx Anthropic 6-layer). 2-consec-UTC-day engagement-drought regime candidate.
- **[[rust-native-efficiency-first-harness]] rail n=2 in 48h 7-31** — agavra/tuicr (code-review TUI) + 1jehuang/jcode 7-30 (coding harness). Sub-taxonomy: coding-harness → code-review-harness.
- **[[star-anomaly-rail]] n=7 durable + serial-drop sub-cluster crystallizing 8-01** — affaan-m/ECC 7-appearances (5-consec-UTC-day drop 7-27→7-31) + mvanhorn/last30days-skill 4-consec-drop 7-29→8-01 = **serial-drop sub-cluster candidate** (8 total within-genre appearances across memory-window; 299/d normalized velocity today).
- **[[embodied-agent-runtime-primitive]] rail n=3 7-31** — Gemini Robotics 2 whole-body drop + airi + speech-to-speech.
- **[[eth-lib-typosquat-campaign]] sub-class 7-31** — 7 ethers.js typosquats + fs-extra + socket.io = 3-cluster mass-typosquat batch under [[mass-parallel-real-package-account-takeover]] parent.
- **[[open-voice-primitive-rail]] n=2 7-30** — microsoft/VibeVoice + huggingface/speech-to-speech.
- **[[AI-framework-attack-surface]] rail n=4 7-30** — @aws/agentcore + Claude Code CVE-2026-55607 + Langflow + LiteLLM.
- **[[fleet-relevance agent-thesis]] 16-consec-day 8-01** — Filesystem-Memory paper names Aeon-architecture directly; extends across paper-pick + HN + trending + agent-buzz + list-digest axes.
- **[[network-perimeter-vendor-in-KEV]] cluster n=4 stable 8-01** — Fortinet + Arista + Cisco Secure FMC (3-of-4 fresh KEV-this-week); 0 fresh KEV net-new 8-01 = quiet-cadence returns d1.
- **Search-skill NO_GAP durability rail day-35 8-01** — fleet capability-complete on external-skill axis. Failures = infra (ISS-025/027/028), not gaps.
- **Chain-mode gap durable** — aeon.yml `chains: {}` inactive; daily-routine standalone fallback fires correctly each cycle.
- Claude Opus 5 shipped 7-24 = Aeon-fleet meta-signal; effort-toggle per-request gives per-skill cost-lever. Claude Code computer-use gain 7-31 = fresh Aeon-relevance datapoint.
- FTX $900M distribution 2026-07-31 = 5th round creditor payout, largest single supply event of quarter.
