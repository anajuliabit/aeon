# Long-term Memory
*Last consolidated: 2026-07-05*

## Current Goals
- **Sandbox-truncation systemic day 12** — ISS-019/020/021/024/025 cluster bleeds an 18-skill chronic tail (`output_tokens=0`). Durable `aeon.yml` capture-step fix unshipped; self-set weekly-review Mon 7-06 deadline is **T-1**. Action-converter 7-04 ranked capture-step PR q5/u5 top action but PR not authored — tomorrow 19:00Z weekly-review formalizes miss unless self-improve authors today.
- **12:00 UTC batch — day-5 of failed live test post PR #150** — 6 skills (token-pick/defi-overview/token-movers/on-chain-monitor/defi-monitor/market-context-refresh) dark ~7.9d since 6-28. `usepod_model:` still on `aeon.yml` L155/162/171 (grep-confirmed 7-05 14:47Z hb).
- **PR #149 docs(skill-graph)** — opened 6-28 17:15Z, **~165h day-7 stall** at 7-05 14:47Z. Sunday + US Independence Day weekend → operator merge unlikely.
- **XAI quota recovery** — Team 3a8b4c1e monthly credit exhausted 6-16 (**day 20**). Operator top-up pending. WebSearch fallback covers daily-routine/tweet-roundup/narrative-tracker; prefetched paths serve list-digest/agent-buzz/token-pick. *[BLOCKED — waiting on operator team-credit top-up since 2026-06-16]*
- **Operator on-chain config day 28** — defi-monitor NO_CONFIG; `memory/on-chain-watches.yml` needs `type: pool` / `type: position` entries. `ALCHEMY_API_KEY len=0`, `ETHERSCAN_API_KEY null`. *[BLOCKED — waiting on operator config + API keys]*
- **BTC bounce day-5 above $60,500 breakdown line** — 7-05 ticks $63,001 (00:17Z) → $62,854 (04:35Z) → $62,568 (10:01Z) → $62,676 (12:56Z) → $62,647 (17:14Z); 7-04 close $63,094 = new high in reclaim window, ~$406 shy of $63.5k reclaim gate. Momentum tapering day-3 → day-5. $65.9k full-reclaim gate still much further.
- **SLX open pick DAY-11 CATASTROPHIC — recut overdue** — HIGH 9/10 6-24 entry $0.4753 → 7-05 $0.256 = **-46% vs entry** (intraday -29.6% capitulation, rank collapse #289 → #372, mcap $62M). CG simple-price verified. Position past every recut trigger; surfaced as top follow-up in 7-05 daily-routine.

## Recently Cleared
- **PR #154 fix(issues) close ISS-026** — completed 2026-07-06 (merged 15:35Z, day-3 stall closed; INDEX flip shipped).

## Fleet Health
- **skill-health snapshot byte-identical 6th consecutive day** (last run 7-04 18:47Z: 0 critical · 23 degraded · 8 warning · 9 healthy · 2 no_data). 15 open issues; ISS-026 pending PR #154 merge for INDEX resolved-flip.
- **fork-skill-digest STUCK ~168h** carry — dispatched 2026-06-28T18:38Z, never resolved. Weekly Sun 7-05 21:00Z fresh dispatch attempt (~4h out from 17:14Z log). 19th consecutive hb surface.
- **operator-scorecard Mon 10:30Z chronic MISSED** — scheduler-side never-run gap; day 6 by tomorrow, carry indefinitely until scheduler patch.
- **vuln-scanner Saturday 7-04 16:50Z fired** — VULN_SCAN_CLEAN on chrome-devtools-mcp v1.5.0; osv-api = durable single-surviving scanner leg per ISS-018 (3rd of 4 runs since 6-13 hit exact same tool-status matrix).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers, skill-health.
- [Crypto research](topics/crypto.md) — Narratives, picks (SLX day-11 CATASTROPHIC -46%, VELVET closed at -68.5%, M MemeCore closed at +130%, GITLAWB reversal day-1 after 2-day trigger streak).
- [Market context](topics/market-context.md) — 7-05 bounce day-5 tapers: BTC $62,647 (17:14Z) above $60,500 breakdown line, breadth 38/75 (~51%, tapered from 71%), median top-50 flat +0.02%, SOL -2.4% breaks 4-day leadership, HYPE -4.2% gives back yest breakout, ADA +9.9%/BCH +6.2% MAJOR winners rotate away from top-10.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX position recut OVERDUE.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage day 20.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 21:00Z.

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | $0.00370281 -1.31% 24h 7-05 (day-1 red print snaps 5-day green streak post 6-30 vol spike; vol $466K = 0.24× baseline but **7.4× intraday resurrection** from yest's collapse-floor) |
| MAMO    | mamo               | 15%           | $0.00928867 +6.32% 24h 7-05 (day-5 green — cleanest small-cap streak of watchlist, first close ≥ $0.009 in window; vol 1.29× = **first ≥1× print in 6 days, participation catches up** on strongest 1d) |
| REPPO   | reppo              | 15%           | $0.02392203 +1.09% 24h 7-05 (day-2 breather post 2-day breakout; flat print near $0.024 handle, vol 1.07× baseline flat) |
| GITLAWB | gitlawb            | 15%           | $0.00006231 **-17.25% 24h 7-05 — REVERSAL TRIGGER FIRED day-1** (snaps 2-day green trigger streak 7-03 +27.38% / 7-04 +23.21%; gives back ~half of 2-day gains, price drops below $0.00007 handle; vol 0.77× = **participation-abandoned** mean-revert) |

## Recurring patterns (durable)
- **Bounce day-5 tapers** — 38/75 top-100 green (~51% breadth, trajectory 83→71→51 day-3→5), median top-50 flat +0.02%. BTC $62.6k day-5 above $60,500; SOL -2.4% breaks 4-day leadership; HYPE -4.2% gives back yest breakout; ADA +9.9% + BCH +6.2% MAJOR winners = **rotation-away-from-top-10-majors**. LAB +81% (#22 MAJOR TRENDING+UP FADE — 7d -4.6% = relief bounce not sustained breakout). STRUCTURAL longs persist: AI agent infra, stablecoins, RWA via CEX rails, prediction markets. $63.5k/$65.9k rails still gate for real reclaim.
- **Skills-as-primitive convergence day-7 — multi-region cross-lab layer added** — 7-05 top pick **alibaba/page-agent** = first Chinese-lab entry (agent-in-page inverts chrome-devtools-mcp pattern). Layer stack now 7: compute + tools + protocols + policy + rubric-evolution + cross-lab plumbing + multi-region cross-lab. **6 major labs** (Anthropic + OpenAI + Google + Meta + Alibaba + Microsoft via 7-05 dotnet/skills first-party) across **2 regions** (US/China). MCP-momentum extends into game-engine (unity-mcp) after browser. Every layer/region has ≥1 shipping artifact within 7 days.
- **Sovereignty stack day-4** — 7-05 **meetily** (Rust local-audio-AI, never uploads audio) joins Podman v6.0.0 + Immich 3.0 + Right-to-Local-Intelligence (7-03) + jamesob local-LLM guide (7-04). 5 artifacts across 4 days spanning runtime + consumer + user-rights + operator-primer + local-audio layers.
- **Holiday-freeze cascade 7-05** — 3 discrete supply-side effects: (a) **GHAD HARD FREEZE ~65h day-3** — nothing published since 7-02T21:14Z, first zero-advisories-in-48h window in digest tracking history; expect Mon 7-06 resumption with backlog wave; (b) **HF paper-pick slate un-rotated day-3** (dateString stuck 7-03); (c) **CLARITY Act 7-04 signing MISSED day-2** (Senate recess until 7-13, deadline slips indefinitely).
- **Cross-lab same-day bug-report dual print 7-05** — Anthropic Claude Code **session/cache leakage between workspace instances** (HN 289p) + OpenAI Codex **reasoning-token clustering degradation** (HN 245p) same-day. Parallel eval-quality bug threads extends memory-as-eval-axis into **eval-quality-axis day-4** (MemSyco 7-02 → AgenticSTS 7-03 → SkillCoach 7-04 → Anthropic+OpenAI production bugs 7-05).
- **RWA narrative rotates onto SOL rails** — 7-05 **Solana RWA fresh ATH $3.41B** extends 7-04 ARB 10%-fee dune signal. Now 2 chains with concrete RWA/fee-accrual anchors within 48h. Tempo/Canton positioning to eat ETH RWA lunch (DefiIgnas Vitalik-roadmap read: 2028+ base-layer throughput fork = payoff too late).
- **9-day npm brandjack wave enters day-1 dormancy** — last malware advisory 7-03T16:06Z; wave paused for holiday-freeze. Watch Mon 7-06 GHAD un-freeze for wave resumption with any 7-03/7-04/7-05 discoveries. Prior thread (6-24 → 7-04) spanned AI-infra → enterprise-data-infra (Confluent Kafka JS) → testing-framework (vitest-agent + 3-pkg Tailwind). 100% npm; pip/crates/go zero.
- **npm-malware "quiet 24h" NOT durable — researcher-batch pauses look like drops** — 7-03 15:35Z log noted 8-day daily-npm-malware streak broken; between 15:35Z and 16:07Z on 7-03, **14 fresh npm advisories dropped in 3 same-minute clusters**. Hypothesis rejected within 32 minutes. Apply same skepticism to 7-05 dormancy read.
- **Solo-researcher mega-batch pattern** — same-project coordinated disclosure batches: 7-01 Fission Go 9-CVE → 7-03 OpenClaw npm 23-CVE (~2.5× larger). Distinct from routine brandjacking (batch-magnitude signature). Codified.
- **9router advisory cluster 3 CVEs** — CVE-2026-49352 hardcoded JWT + GHSA-g6g7 missing-authz/cmd-injection + CVE-2026-49353 no-fix Host-header bypass. Worst config default of year candidate; header-based access control not trustable.
- **dulwich pip RCE-via-clone with public PoC + no user interaction** — CVE-2026-52726 CVSS 7.5, git library writing `.git/hooks` on clone; any CI/dev-machine cloning untrusted repos affected. Fix 1.2.5 = **highest THIS-WEEK operational priority** (carry from 7-04; not re-surfaced under holiday-freeze but stands).
- **Anthropic ship-day compounding + IPO-prep tell** — 7-05 Anthropic ships **Claude Science** (research app w/ auditable artifacts + flexible compute) + **Claude Tag** (team collab) — post-Sonnet-5 product cadence continues. S-1 confidentially filed post $65B Series H → $965B > OpenAI carry; OpenAI IPO filing next weeks. Sonnet 5 dev-preference 82% inside Claude Code carries.
- **Alpha-filter framework extends — Vitalik-roadmap bearish-on-tape lens** — 7-05 DefiIgnas quote-tweet reads Vitalik 2028+ base-layer throughput fork as inviting Tempo/Canton to eat RWA lunch meanwhile. Adds ETH-tokenomics-timing critique to @Flowslikeosmo tokenomics-alignment framework (SLX/VELVET/LIT/VVV 4× thesis confirmed through 7-04).
- **search-skill SEARCH_SKILL_NO_GAP day 12** — fleet capability-complete on external-skill axis. Failures are infra (ISS-025 capture step), not gaps. Stop noise-filing new gap reports unless cron-state failure mode changes.
- **operator-scorecard Mon 10:30Z perpetually MISSED** — scheduler-side never-run gap, flagged every Monday hb. Not skill-side. Carry indefinitely until scheduler patch.
- **Fake-star pattern + dotfiles-shape complement** — 7-05 **mattpocock/skills** drop (Shell + 157k + "personal configuration" description) confirms dotfiles/config-dump filter as complementary tell to strict fake-star triad. Triad: >100k stars + 1:6 (or worse) fork ratio + wrong-language tag (Shell for AI project) OR rapid semver + brand-list description. Sustained-fake-trending on rolling day-count remains added tell (msitarzewski/agency-agents 4th-day drop 7-04).
- **GH Advisory `patched_versions: null` lags advisory-page reality day-4** — WebFetch on advisory page is canonical for triage, not the JSON field.
- **osv-api = durable single-surviving vuln-scanner leg per ISS-018** — 3rd of 4 vuln-scanner runs since 6-13 hit exact same tool-status matrix (semgrep=fail pip-install / trufflehog=fail tar-extract / osv-binary=fail exec / osv-api=ok). Sandbox-limitation durable. Prefetch step `scripts/prefetch-vuln-scanner.sh` could install binaries with full network access before Claude starts.
