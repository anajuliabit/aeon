# Long-term Memory
*Last consolidated: 2026-07-04*

## Current Goals
- **Sandbox-truncation systemic** — ISS-019/020/021/024/025 cluster still bleeds an 18-skill chronic tail (`output_tokens=0`). Durable `aeon.yml` capture-step fix unshipped **day 11**; morning-brief 07:00Z surfaced today (7-04) as **T-0 self-set weekly-review hard deadline** — no PR shipped, weekly-review Mon 07-06 will formalize the miss unless self-improve tick 07-04/05 authors it.
- **12:00 UTC batch — day-3 of failed live test post PR #150** — 6 skills (token-pick/defi-overview/token-movers/on-chain-monitor/defi-monitor/market-context-refresh) dark ~6.1d since 6-28. PR #150 `usepod_model`→`model:` was PARTIAL fix; morning grep 7-04 07:00Z confirms **aeon.yml L155/162/171 still carry `usepod_model:`**. Additional dead slot day-1: aixbt-pulse 09:00Z (2× interval threshold cross); github-trending 09:00Z + skill-freshness 08:00Z recovered late-fired.
- **PR #149 docs(skill-graph)** — opened 6-28 17:15Z, **~141h day-6 stall** as of 7-04 14:16Z. US Independence Day operator-merge probability low; PRs likely stay pending through 7-05.
- **PR #154 fix(issues) close ISS-026** — opened 7-03 18:20Z by self-improve, ~20h day-1 open. Under 24h stall threshold; INDEX flip pending merge.
- **XAI quota recovery** — Team 3a8b4c1e monthly credit limit exhausted 6-16 (**day 19**). Operator top-up pending. WebSearch fallback covers daily-routine/tweet-roundup/narrative-tracker; prefetched paths serve list-digest/agent-buzz/token-pick. *[BLOCKED]*
- **Operator on-chain config** — defi-monitor NO_CONFIG **day 27**; `memory/on-chain-watches.yml` needs `type: pool` / `type: position` entries. `ALCHEMY_API_KEY len=0`, `ETHERSCAN_API_KEY null`. *[BLOCKED — partial]*
- **BTC 7-day breakdown streak BROKEN → day-4 of reclaim** — 7-02 close $61,487 = first daily close ≥ $60,500 in the 8-day window. 7-03 close $62,537, 7-04 spot $62,558 (12:40Z) held day-4. $63.5k reclaim rail ~$942 away, $65.9k full-reclaim gate still much further; breakdown/reclaim signals silent per skill spec.
- **SLX open pick CRITICAL — thesis broken day-10** — HIGH 9/10 6-24 entry $0.4753 → 7-04 $0.363 = **-23.6% vs entry** (spot verified via CG simple-price call, -22.8% 24h). Position needs recut decision (capital-2x-program tracked, moonshot sub-sleeve ≤0.25% MEDIUM cap).

## Fleet Health
- **skill-health 7-02 18:53Z snapshot byte-identical 5th consecutive day** (0 critical · 23 degraded · 8 warning · 9 healthy · 2 no_data). 15 open issues; ISS-026 pending PR #154 merge for INDEX resolved-flip.
- **fork-skill-digest STUCK ~140h** carry — dispatched 2026-06-28T18:38Z, never resolved. Weekly Sun 7-05 fresh dispatch attempt (~28h out).
- **operator-scorecard Mon 10:30Z MISSED day 5** — scheduler-side never-run gap, carry indefinitely until scheduler patch.
- **vuln-scanner Saturday slot fired 16:50Z** — first live-test post-6-27, breaks 7d dispatch silence. VULN_SCAN_CLEAN (chrome-devtools-mcp partial-scan). osv-api = durable single-surviving scanner leg per ISS-018 (3rd of 4 runs since 6-13 hit exact same tool-status matrix).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers, skill-health.
- [Crypto research](topics/crypto.md) — Narratives, picks (SLX day-10 THESIS BROKEN -23.6%, VELVET day-3 dead-cat +36%, M MemeCore closed at +130%, GITLAWB day-2 trigger fired +23.21%).
- [Market context](topics/market-context.md) — 7-04 bounce day-4: BTC $62,558 12:40Z above $60,500 breakdown line, breadth 63/89 (~71%) top-100 green, ETH $1,754 extends first-week-reclaim past $1,750, SOL 7d +14.4% leadership continues, HYPE +6.6% breakout.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX position recut pending.
- [XAI quota state](topics/xai-quota-exhausted.md) — Outage day 19.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 21:00Z.

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | $0.00375649 +1.51% 24h 7-04 (day-5 green post 6-30 vol spike; **vol collapse to 0.03× baseline on green tape = liquidity-vacuum phase**, paper-participation lift, supply arc fully closed) |
| MAMO    | mamo               | 15%           | $0.00873464 +3.77% 24h 7-04 (day-4 green — cleanest small-cap streak of watchlist, first close ≥ $0.0087 in window; vol 0.99× flat baseline parity) |
| REPPO   | reppo              | 15%           | $0.02365287 -0.45% 24h 7-04 (day-1 breather post 2-day breakout; first red print after 7-03 +10.85%, vol fades $222K → $91K = 0.56× baseline = participation exhale) |
| GITLAWB | gitlawb            | 15%           | $0.00007443 **+23.21% 24h 7-04 — TRIGGER FIRED day-2** (2nd consecutive fire post 7-03 +27.38%; extends past $0.00007 handle, vol steps 1.76× → 2.27× = participation catching up to price, largest vol print of window) |

## Recurring patterns (durable)
- **Bounce day-4 holds** — 63/89 top-100 green (~71% breadth, tapered from 83/100 7-03 day-2), median top-50 +1.28% (was +2.12%). BTC day-4 above $60,500 breakdown line; ETH extends $1,700 reclaim to $1,754; SOL 7d +14.4% leadership continues; HYPE +6.6% breakout. STRUCTURAL longs persist: AI agent infra, stablecoins, RWA via CEX rails, prediction markets. $63.5k/$65.9k rails still gate for real reclaim.
- **Skills-as-primitive convergence day-6 — cross-lab plumbing added as 6th layer** — 7-04 github-trending top pick **openai/codex-plugin-cc** (634 today · 23k stars) = first cross-lab agent-runtime bridge letting Codex be called from Claude Code. Layer stack now: compute + tools + protocols + policy + rubric-evolution + cross-lab plumbing. Every layer has ≥1 shipping artifact within 7 days. **agentskills/agentskills** community spec (22k · Py) = the interface the ecosystem is consolidating on.
- **Sovereignty stack thread day-3** — jamesob local-LLM guide (HN 326p 7-04) extends 7-03 Podman v6.0.0 + Immich 3.0 + Right-to-Local-Intelligence cluster. 4 items across 3 days = pattern durable across runtime + consumer + user-rights + operator-primer layers.
- **Brandjacking is the new default supply-chain vector** — extends across verticals: AI-infra (6-30) → enterprise-data-infra (Confluent Kafka JS 7-01) → testing-framework (vitest-agent + 3-pkg Tailwind 7-02). 100% npm; pip/crates/go zero. MCP/agent-infra brandjack thread paused 7-04 (day-1) after 7-day 6-27→7-03 chain.
- **npm-malware "quiet 24h" was researcher-batch pause, NOT durable shift** — 7-03 15:35Z log noted 8-day daily-npm-malware streak broken; between 15:35Z and 16:07Z on 7-03, **14 fresh npm advisories dropped in 3 same-minute clusters** (5-pkg TS/API-node-utility + 4-pkg SQL/DB extending 7-02 db-utility cluster + decode-sdks pair + 3 stragglers). Hypothesis rejected within 32 minutes. 9-day cumulative brandjack wave 6-24→7-04 resumes.
- **Solo-researcher mega-batch pattern** — same-project coordinated disclosure batches: 7-01 Fission Go 9-CVE = 1st, 7-03 OpenClaw npm 23-CVE = 2nd (~2.5× larger). Distinct from routine brandjacking (batch-magnitude signature). 2 in 3 days = codified.
- **9router advisory cluster grew to 3 CVEs day-2** — CVE-2026-49352 hardcoded JWT + GHSA-g6g7 missing-authz/cmd-injection (7-03) + fresh CVE-2026-49353 no-fix Host-header bypass (7-04). Worst config default of year candidate; header-based access control not trustable.
- **dulwich pip RCE-via-clone with public PoC + no user interaction** — CVE-2026-52726 CVSS 7.5, git library writing `.git/hooks` on clone; any CI/dev-machine cloning untrusted repos affected. Fix 1.2.5 = highest THIS-WEEK operational priority.
- **Memory as distinct eval axis day-3** — MemSyco-Bench (7-02) → AgenticSTS (7-03) → SkillCoach ↑14 (7-04) = 3-day arc. SkillCoach adds evaluation-quality (5th layer of skills-as-primitive convergence) via self-evolving rubrics for agentic skill-use — direct aeon-runtime hit on skill-evals surface.
- **Anthropic ship-day compounding + IPO-prep tell** — 7-04 Anthropic S-1 confidentially filed post $65B Series H → **$965B valuation surpasses OpenAI**; OpenAI IPO filing next weeks. Sonnet 5 dev-preference **82% inside Claude Code** (92.4% SWE-bench vs Opus 4.6 80.8%) carries. Aeon runtime relevance: stego markers + IPO-prep both implicate proxy/gateway routing pressure.
- **search-skill SEARCH_SKILL_NO_GAP day 11** — fleet capability-complete on external-skill axis. Failures are infra (ISS-025 capture step), not gaps. Stop noise-filing new gap reports unless cron-state failure mode changes.
- **operator-scorecard Mon 10:30Z perpetually MISSED** — scheduler-side never-run gap, flagged every Monday hb. Not skill-side. Carry indefinitely until scheduler patch.
- **Fake-star pattern** — drop with confidence when: >100k stars + 1:6 (or worse) fork ratio + wrong-language tag (Shell for AI project) OR rapid semver (v3.8.42/139d) + brand-list description. **msitarzewski/agency-agents 4th-day drop (7-04)** reinforces pattern with sustained-fake-trending on rolling day-count as added tell.
- **GH Advisory `patched_versions: null` lags advisory-page reality day-4** — 7-01 all-null cascade → 7-02 inversion → 7-04 continues inversion. WebFetch on advisory page is canonical for triage, not the JSON field.
- **Alpha-filter framework — tokenomics-alignment via @Flowslikeosmo** — 7-04 day-2 VVV Venice -8.8% loser confirms 7-03 list-digest bear thesis (dual-structure critique playing out). SLX/VELVET/LIT/VVV = 4 thesis-application shape confirmed.
- **osv-api = durable single-surviving vuln-scanner leg per ISS-018** — 3rd of 4 vuln-scanner runs since 6-13 hit exact same tool-status matrix (semgrep=fail pip-install / trufflehog=fail tar-extract / osv-binary=fail exec / osv-api=ok). Sandbox-limitation durable. Prefetch step `scripts/prefetch-vuln-scanner.sh` could install binaries with full network access before Claude starts.
- **CLARITY Act 7-04 symbolic-signing MISSED — deadline slips indefinitely** — White House Crypto Council targeted July 4 (America's 250th birthday); Senate on recess until 7-13, no floor time before Aug recess. Prediction-market/RWA narrative timing implication.
- **ARB 10%-fee dune-dashboard signal** — @DefiIgnas list-digest 7-04 anchor: Robinhood/Orbit accrues 10% fees to ARB DAO — first quantified fee-accrual signal in L2 tape. Whoever ships the dune first captures narrative anchor for arbitrum reclaim arc; token-pick / defi-overview seed for 7-05.
