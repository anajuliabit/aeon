# Long-term Memory
*Last consolidated: 2026-07-16*

## Current Goals
- **ISS-025 capture-step PR T-0 firm today (7-16)** — weekly-review 7-13 action #1 priority 20, operator direct-author against `.github/workflows/aeon.yml:479-495` chain-runner. Rule-5 workflow-file class blocks self-improve routing (now n=4 with PR #164 CONFLICTING resolve — see below). cost-report STUCK d3 ~66h+ is current-shape manifest.
- **Rule-5 primitive EXTENDS past workflow-file class** — 7-16 14:52Z: PR #164 (script-file class touching `scripts/advisor/run.sh` + `.outputs/` + `memory/logs/` + `memory/token-usage.csv`) flipped CONFLICTING at ~19h20m. All 3 self-improve authored PRs in flight (#162/#163/#164) now CONFLICTING. Read: **conflict source = auto-committed state drift**, not file-class-specific. Codification action #3 (self-improve → CLAUDE.md, deadline 7-17) needs re-scope: routing rule is broader than "workflow-file only".
- **PR #164 CONFLICTING d1** — `fix(investment-advisor): fail-fast committee retries` (7-15 19:31Z), self-improve authored per weekly-review action #4. Under 24h stall gate until 19:31Z 7-16 (~4h out at last check). CONFLICTING flip = rule-5 primitive extension test resolved (see above).
- **PR #162 T+2 deadline-missed day-3** — `fix(daily-routine)` XAI-fallback tightening (7-11), ~117h stall, CONFLICTING, reviewDecision empty. SKILL.md-class (rule-5 clean pre-extension); day-3 slip is on operator review.
- **PR #163 T+3 stall approaches 72h gate** — `fix(skill-security-scan)` (7-13), ~68h at 14:52Z hb, crosses 72h at 18:09Z 7-16.
- **CLAUDE.md rule-5 codification T-1** — self-improve authors addition under "Skill authoring boundaries" section by 2026-07-17 (weekly-review action #3). Next self-improve fire = 7-17 = deadline day. Re-scope needed per rule-5 extension above.
- **cost-report STUCK d3 ~66h+** — `last_status: dispatched` at 2026-07-13T20:44:24Z, cf=5, sr=0.10, ~17d since last_success. ISS-025 signature. Resolves with operator PR.
- **12:00 UTC batch DARK day-19** — 8-skill 6-28 cluster last_success 2026-06-28 (~18d stale). **7-16 batch-dark extends to morning slot** (07:00Z morning-brief/daily-routine/thought-review MISSED today, ~7h52m past variance precedent). Scheduler-side per ISS-027, same rule-5 primitive as ISS-025.
- **Operator on-chain config day-40** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` pool/position entries + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Blocked.

## Recently Cleared
- **Investment Advisor 7-consec-cancellation investigation CLOSED via PR #164** (7-15 19:31Z) — weekly-review action #4 shipped-on-target (T-1). First cross-week weekly-review action closed via self-improve authored PR since PR #160 flipped ISS-022 on 7-06/7-07. PR itself CONFLICTING (rule-5 extension), but investigation-authorship signal delivered.
- **XAI quota RETIRED as active goal** (7-15 reflect) — day-31, cache-prefetch path (list-digest 7-16 clean cache run) covers surface cleanly. Reference-only in [[xai-quota-exhausted]].
- **BTC $63.5k arc REOPENS d2 confirmed** — 7-15 daily close $64,722 (second consecutive close above gate since 7-14 $64,977 reclaim); 7-16 spot $63,905–$64,579 all-day holds above $63,500 gate. `reclaim63500Alerted=true` intact (re-arm only sub-$60,500). $65,900 full-reclaim gate now $1,321–$1,995 above spot.

## Fleet Health
See [[fleet]] for the full snapshot. Highlights (2026-07-16 14:52Z hb): 11 open issues (4 critical / 4 high / 3 medium). Sandbox-truncation family day-24. cost-report cf=5 sr=0.10 STUCK d3. Chronic 17-skill sr<0.5 tail all ISS-019/020/021/025 class. aixbt-pulse dead-slot d19 (13 consecutive twice-daily misses). 07:00Z morning batch MISSED today = batch-dark d19 extends to morning slot. weekly-shiplog + operator-scorecard chronic Mon miss (same ISS-027 primitive).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns (breakout-unwind n=5 · LAB -95% zero-arc reference · PUMP 2-step-shape · DCR/XEC whipsaw n=1 · **GITLAWB round-trip whipsaw n=1 CODIFIES** · DEXE momentum breaking).
- [Market context](topics/market-context.md) — 7-16 tape holds risk-on, BTC arc REOPENS d2 confirmed, macro CPI-cools cut fully priced.
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).
- [XAI quota state](topics/xai-quota-exhausted.md) — Retired reference; cache-prefetch primary path.
- [AIXBT signals](topics/aixbt-grounding.md), [clusters](topics/aixbt-clusters.md), [chains](topics/aixbt-chains.md) — 36 clusters / ~205 chains as of 6-28 21:00Z (aixbt-pulse dead-slot day-19 = state frozen).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format. Anchors refreshed per 7-16 09:35Z token-alert (0/12 checks fire; 15% rail intact 3-run streak).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 7-16 -2.25% 24h vol $127K = **0.18× 5-window baseline** ($690K mean, dropped 7-08 spike); optical improvement off 7-15 0.08× floor but real print still $100K-neighborhood = participation-vanish state d10 extends; floor-hunt branch holds |
| MAMO    | mamo               | 15%           | 7-16 -1.18% 24h vol $912K = **0.98× baseline** ($931K mean) = **first exact-baseline print in 5-window** = day-6 bounce pauses cleanly at mean, sustainable-shape holds (participation returns to mean, no distribution risk) |
| REPPO   | reppo              | 15%           | 7-16 -3.45% 24h vol $140K = 0.31× baseline ($456K mean); **fade-back-to-trend continuation d2 confirms** — 7-15 -6.74% below $0.0275 gate + 7-16 -3.45% continuation validates mean-reversion framing (7-14 bounce was mechanical) |
| GITLAWB | gitlawb            | 15%           | 7-16 -9.70% 24h vol $328K = 0.63× baseline ($518K mean); **round-trip whipsaw CLOSES n=1 CODIFIES** — 7-14 -11.97% (80% rail) → 7-15 +13.36% (89% rail) → 7-16 -9.70% (65% rail) = 3-session full round-trip, log-to-log -12.00% gives back essentially all of 7-15's +12.80% pop; both legs participation-thin (mechanical whipsaw, not real-bid) |

## Recurring patterns (durable)
- **One-day-breakout-unwind n=5** — MORPHO/EIGEN/NEX/TIBBIR/DRV. "Breakout must hold d2 to be trusted." BEAT/B stay n=2 dead-cat-with-legs exception.
- **LAB -95% zero-arc reference case** — cumulative ~99.4% at d7; `-59%/day sellers-exhaust` heuristic 0/7. Reference class for -95% projections.
- **DCR/XEC pair-flip round-trip 3 days (whipsaw candidate n=1)** — 7-13 top-2 → 7-14 bottom → 7-15 top-2. Privacy-narrative rotation-as-whipsaw not sustained.
- **GITLAWB round-trip whipsaw n=1 CODIFIES** (7-16 close) — single-token 3-session round-trip, participation-thin both legs = mechanical shape confirms; same mechanic as DCR/XEC pair-flip but on a single token.
- **Rule-5 primitive EXTENDS past workflow-file class (n=4)** — PRs #160/#162/#163/#164 all CONFLICTING; PR #164 = script-file class not workflow-file class. Conflict source reads as **auto-committed state drift** (self-improve authored PR based on stale state; main advances with new log rows/token-usage rows/self-improve outputs between authorship and merge attempt) rather than specific file class. Operator direct-author remains sole reliable path for any self-improve output.
- **Skills-primitive convergence day-16 EXTENDS with compounding** — 7-13 stitch-skills, 7-14 hallmark, 7-15 mattpocock/skills, 7-16 hallmark d3 + mattpocock d2 = library-shaped survivors only, 0 framework-shape survived.
- **Rust-rewrite-of-python-classics n=1 NEW** (7-16) — openinterpreter Python→Rust rewrite in one release cycle (rust-v0.0.23→v0.0.25 in 24h). Targets ACP + deepseek/kimi/qwen = explicit low-cost-open-model bet. First "OG-tool-picking-sides-in-model-tier" signal.
- **Non-MCP-primitive n=1 NEW** (7-16) — pi-computer-use README explicitly positions against MCP ("not a replacement for app APIs or MCP servers … when only interface is app on screen"). Complements MCP-becomes-infra by naming its edge case.
- **Agent-safety-guardrail rail day-3** — 7-14 destructive_command_guard + 7-15 Cursor DuneSlide 0day + 7-16 pi-computer-use accessibility-primitive = n=3 pattern extension.
- **Consumer-tool viral-moment day-3 FADE** — OpenCut 7-14 1,229 → 7-15 4,276 → 7-16 1,664 = day-3 down 61% from peak. Revises 7-15 "viral-day-2 CONFIRMED" verdict: shape is peak-then-fade, not durable-viral. Pattern updates to n=1 3-day-shape.
- **npm-malware wave d3 fades 30→16** (7-15 → 7-16) — wave carries into d3 but not steady-state. `claude-token-tracker-mcp` = first direct-Anthropic-scope malware pkg in memory (fleet-adjacent typosquat).
- **MCP-server RCE cluster n=3 in 48h** (7-15 → 7-16) — langbot pip + mcp-documentation-server npm + n8n-mcp npm. MCP attack surface hardening becomes durable rail.
- **dd-trace polyglot cluster n=6** (7-16) — same-day W3C baggage DoS across pip/npm/go/rubygems/nuget/maven. **First cross-ecosystem single-vendor cluster in memory.**
- **Old-CVE-fresh-KEV n=2 codifies** — 2008 Cisco IOS 12.4 CVE-2008-4128 (KEV 7-13, BOD T-0 today) + 2023 KNX Protocol CVE-2023-4346 (KEV 7-15). Long-tail EOL/legacy stacks getting fresh KEV = active exploitation.
- **Package-clusters durable pattern n=4** — 7-13 SiYuan Go 5-CVE + 7-14 DIRAC pip 4-CVE + 7-15 nebula-mesh Go 4-CVE + 7-16 dd-trace 6-lang polyglot. Two shapes emerging: single-vendor-multi-language same-day vs single-package-multi-advisory single-release-fix.
- **Small-MoE-frontier-close cluster n=2** — Meta Muse Spark 1.1 + Claude Sonnet 5 near-Opus. Production-economics shift.
- **search-skill SEARCH_SKILL_NO_GAP day 21** — fleet capability-complete on external-skill axis. Failures = infra (ISS-025/027), not gaps.
