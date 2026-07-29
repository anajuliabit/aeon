# Long-term Memory
*Last consolidated: 2026-07-29*

## Current Goals
- **ISS-025 capture-step PR T+11 day-14 (8 days past 1-week slip milestone)** — operator direct-author against `.github/workflows/aeon.yml:479-495`. iss-025-hand-off due 2026-07-30 (**T-1 day**) per weekly-review 7-27 action #1. Cost-report weakest at 12% (7/58) durable.
- **12:00 UTC batch DARK day-32** — 8-skill 6-28 cluster (defi-overview / token-pick / token-movers / narrative-tracker / market-context-refresh / fleet-control / on-chain-monitor / defi-monitor) frozen since 6-28 21:00Z. ISS-027 signature confirmed durable through 7-29 12:00Z clean same-slot token-alert fire under signature.
- **ISS-027/028 doc-gap d23 — +3d past weekly-review 7-27 last-chance window** — MEMORY line 4 + line 8 reference ISS-027 authoritatively; no file exists in `memory/issues/`. ISS-028 (bash-redirect n=10+ durable 7-UTC-day span) also absent. Load-bearing gap. Action-converter 7-24 shaped 2 file-create actions (score 125 + 80) — still pending.
- **PR #165 d10 past-gate CONFLICTING** — created 7-19 17:38Z, weekly-review 7-27 absorbed 7d gate cross; still CONFLICTING through 7-29 heartbeat = 10d open. Operator batch-merge cadence window.
- **PR #167 d6** — bash-redirect fix (7-23 18:21Z self-improve). Under 7d weekly-batch cadence, waiting operator batch.
- **Operator on-chain config day-53** — defi-monitor NO_CONFIG; needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Operator-gated.
- **priorities.md 55d stale** — last reviewed 2026-06-04. Thought-review 7-29 07:26Z flagged in notify. Operator-owned refresh candidate.

## Recently Cleared
- **Self-improve queue-exit gate breach RESOLVED 7-28 22:36Z** — dupe pair #168 + #169 both merged (github-issues comments→commentsCount field-rename), queue 4→2. First gate-breach in memory-window closed in ~30h. Root-cause investigation (whether self-improve correctly evaluates gate at authoring time) still open per 7-28 reflect follow-up #3.
- **skill-health hash flip 467ce959 → 7bf88238 (7-28 19:02Z)** — first hash break in 168h+ span. Composition delta: defi-overview + token-pick DEGRADED→WARNING (SR 0.69/0.64 above <0.6 gate); defi-monitor + evening-recap + list-digest crossed WARNING→DEGRADED (SR 0.53/0.59/0.56); btc-levels crossed WARNING→HEALTHY (SR 0.81 clears 0.8 gate). 10 HEALTHY (up from 9).
- **Broad-tape restore 8→40 top-100 green 7-29 = largest 1-day breadth restore in memory-window** — 7-28 4/4-red day fully unwinds. Suggests 7-28 risk-off was single-day flush not regime shift.
- **BEAT/UB/HOLO one-day-round-trip snap-back 7-29 = n=2 sub-class extends 7-28 BANK pattern** — broad-risk-off d1 losers → risk-on d2 winners same tokens.
- **REPPO capitulation-attempt fully digests d1 7-29** — 24h -20.10% → -2.41% = 10× deceleration, vol 2.075× → 1.003× baseline. Drought-break head-fake resolves to flat-on-baseline stall, not liquidation continuation.
- **META rank 187 mid-cap breakout 7-29** — +66.8% TRENDING+UP+PUMP-RISK on $6.5M vol = biggest low-rank breakout in memory-window. Extends [[low-rank-mid-cap-trending-breakout]] rail candidate.
- **KEV quiet-cadence restarts d1 7-29** — zero-fresh in 24h window since 7-27 Fortinet+Arista, mirrors 7-23→7-26 4-day drought post 7-22 Check Point+SharePoint.
- **Malware campaign consolidation ends 7-29** — 3-day mass-cluster rail (@antv/* 52-pack 7-27 + wagni_bot/polymarket/mcp-server 63-pack 7-28) does NOT extend d3; today's 61 fresh malware entries are diverse-1-off publishes.
- **7-28 tag-ambiguity drop reversal 7-29 via opengeos/GeoLibre** — 7-28 dropped for 48/d velocity just under 50 gate; today crosses at 58.1/d as cumulative stars catch up. First "one-day-below-gate-then-above" reversal in memory-window.

## Fleet Health
See [[fleet]] for full snapshot. skill-health hash **7bf88238** (fresh 7-28 19:02Z NOTIFY, 168h+ 467ce959 identity broken): 0 CRITICAL / 18 DEGRADED / 13 WARNING / 10 HEALTHY / 3 NO_DATA. 11 open issues. **22+ consec heartbeat NOOP** through 7-29 14:36Z (~220h+ span since 7-19 09:17Z regime-onset). Sandbox-truncation family **day-37** (T+12 day-14). aixbt-pulse dead-slot **d32** (63+ consec 12h cycles missed). **Bash `>` redirect regression n=10+ durable 7-UTC-day span** (7-22 → 7-29 security-digest 14:42Z + agent-buzz 17:37Z + reg-monitor + list-digest 17:36Z all hit + workaround chain held on every fire).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, health snapshot, blockers, weekly-batch cadence.
- [Crypto research](topics/crypto.md) — Narratives, picks, durable patterns.
- [Market context](topics/market-context.md) — Baseline snapshot (stale from 7-16; refresh next fire).
- [Capital-2× program](topics/capital-2x-program.md) — North-star spec; SLX -70% terminal (operator-owned).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md`. 7-29 12:00Z snapshot: 0/4 alerts (all sub-threshold, 36th consec clean CG day). Broad watchlist participation-lift-day — 3 of 4 tokens at-or-above baseline vol for first time in run; leader-of-ratio shifts REPPO→GITLAWB (2.009× on -6.66% give-back d6, first above-baseline vol since 7-24, still 2/3 of 3× gate).

| Token   | CoinGecko ID       | 24h Threshold | Recent Activity |
|---------|--------------------|---------------|-----------------|
| WELL    | moonwell-artemis   | 10%           | 7-29 +0.08%, vol $1.69M = 1.113× baseline (post-drain fade fully arrests at noise floor; 2nd-consec above-baseline print, low-momentum consolidation on maintained participation) |
| MAMO    | mamo               | 15%           | 7-29 -0.65%, vol $872K = 1.063× baseline (digestion d8 first above-baseline print in 7 runs; participation-lift-without-price-move mirrors WELL's early vol-spike-only class) |
| REPPO   | reppo              | 15%           | 7-29 -2.41%, vol $105K = 1.003× baseline (capitulation-attempt fully digests d1 — 24h -20.10%→-2.41% 10× deceleration; drought-break head-fake resolves flat) |
| GITLAWB | gitlawb            | 15%           | 7-29 -6.66%, vol $452K = 2.009× baseline (cliff-give-back d6 accelerates on 2× vol spike; log-to-log -10.81% deepens; active-distribution-on-give-back reasserts) |

## Recurring patterns (durable — brief pointers; details in topic files)
- **Broad-tape restore 8→40 = largest 1-day breadth restore in memory-window 7-29** — extends 7-shape breadth-regime rail; 7-28 risk-off was single-day flush not regime shift.
- **One-day-round-trip pattern class n=2 7-29** — BEAT/UB/HOLO snap-back extends 7-28 BANK; shape "broad-risk-off d1 losers → risk-on d2 winners same tokens" firms.
- **[[skill-pack-primitive-rail]] extends n=5 in 6 UTC-days 7-29** — virgiliojr94/book-to-skill (one-shot PDF→Claude skill) tops slate. Rail: mattpocock/skills (7-24) → obra/superpowers (7-26) → bradautomates/claude-video (7-28) → mvanhorn/last30days-skill (7-28) → virgiliojr94/book-to-skill (7-29). Sub-taxonomy expands: framework → collection → vision-skill → research-skill → ingestion-skill.
- **[[embodied-agent-runtime-primitive]] extends n=2 in 2 UTC-days 7-29** — huggingface/speech-to-speech (open-weights local voice) pairs with 7-28 moeru-ai/airi (Minecraft/Factorio). Common thread: agent-as-runtime vs agent-as-chat-frontend.
- **[[MCP-enforcement-primitive-cluster]] n=1 NEW 7-29** — agent-buzz surfaces 2 independent builders same day (policylayer_dan + emadgnia) authoring MCP-infra-maturity primitives. Rail candidate; watch 7-30 for 2nd-consec.
- **[[training-curriculum-as-a-service]] NEW 7-29** — Qwen Skill Self-Play (DeFi Minty link, arxiv paper): proposer/solver/controller loop refines own task pool, +6.5pts vs unguided on Qwen3-4B. Extends [[small-MoE-frontier-close]] rail.
- **[[legit-defi-org-typosquat]] NEW sub-class 7-29** — karpatkey + karpatkit pip malware impersonates real DAO treasury firm (Gnosis/ENS/MakerDAO/Aave advisor). Full-scope cred stealer (ETH keystores + K8s + AWS/GCP + SSH + gnupg + npmrc + `.env`). Extends [[full-scope-cred-stealer-supply-chain]] + [[mass-parallel-real-package-account-takeover]] with defi-org attack angle (contrasts 7-28 AI-tooling-typosquat).
- **[[single-project-mass-disclose]] extends n=6 7-29** — datamodel-code-generator 12-CVE pip mass-disclose (all 12 published within 40min at 21:26-21:50Z) + swagger-typescript-api 5-CVE npm concurrent same-day. **Rail acceleration from monthly → same-day**.
- **[[federal-CEA-authority-reassert]] NEW 7-29** — MN prediction-market ban enjoined by D. Minn. (Judge Menendez, CEA-preemption) + CFTC self-cert crackdown (event-contract advisory 9273-26 / Letter 26-22) same-week. n=2 opposing-direction rulings in 22d window post-Torres NY loss 7-7 = state-vs-federal jurisdiction fragmentation escalates.
- **[[low-rank-mid-cap-trending-breakout]] candidate 7-29** — META rank 187 +66.8% TRENDING+UP on $6.5M vol = first low-rank mid-cap breakout with trending confirmation in memory-window.
- **[[one-day-below-gate-then-above]] reversal NEW 7-29** — opengeos/GeoLibre 48→58.1/d velocity cross documents first "just-below-gate → above-gate on d2" reversal in memory-window.
- **Star-anomaly rail n=4-durable via ECC 4th-consec drop 7-29** — drop-decision codifies star-count-inflation-vs-authentic-viral hypothesis; investigation candidate.
- **KEV quiet-cadence pattern n=2 shape emerges 7-29** — 7-23→7-26 4d drought + 7-28→7-29 2d drought, both bounded by enterprise-network-vendor cluster fires.
- **Malware mass-cluster rail terminates d3 7-29** — 7-27 @antv/* + 7-28 wagni_bot/polymarket/mcp-server → 7-29 diverse-1-off publishes, no >2-package cluster (karpatkey+karpatkit sibling pair the standout).
- **AEON trending +17.8% at rank 781 7-29** — project's own token in trending endpoint. Note but do not act.
- **Chain-mode gap durable** — aeon.yml `chains: {}` inactive; daily-routine standalone fallback fires correctly each cycle per SKILL.md.
- **Fleet-relevance agent-thesis 13-consec-day 7-29** — pbakaus/impeccable + alibaba/open-code-review + skill-packs + book-to-skill + speech-to-speech = agentic-primitive dominance persists 7-17 → 7-29.
- **Search-skill NO_GAP durability rail day-32** — fleet capability-complete on external-skill axis. Failures = infra (ISS-025/027/028), not gaps.
- Claude Opus 5 shipped 7-24 = Aeon-fleet meta-signal; effort-toggle per-request gives per-skill cost-lever.
- FTX $900M distribution jul 31 T-2 = largest single supply event of quarter (unlock-monitor confirmed as headline, not vesting cliff).
- CVE-2026-55607 Claude Code auto-patched 7-25 via unpinned `npm install -g` (fix 2.1.163).
