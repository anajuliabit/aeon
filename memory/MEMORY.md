# Long-term Memory
*Last consolidated: 2026-06-14*

## About This Repo
Aeon — autonomous agent on GitHub Actions via Claude Code. Enabled
standalone skills on cron. Inbound messaging via Telegram. soul/ populated
2026-05-25 (ana voice).

## Current Goals
> **Health-skill directive:** the reppo-swarm (orquestra) has been removed
> from aeon entirely — it now lives at `~/code/orquestra` (self-hosted on
> Docker). Do NOT re-add reppo-orchestrator/trading-agent/voter/digest skills,
> chains, or scripts here, and do NOT file issues about reppo-swarm not
> running on CI.
- **CAPITAL-2× PROGRAM (north star): double net worth by 2027-12-31.**
  See [capital-2x-program.md](topics/capital-2x-program.md). Risk sleeve
  ≤15-20% net + moonshot sub-sleeve ≤1% for token-picks. BTC hard-level
  monitor shipped as `skills/btc-levels` (4-hourly; reclaim63500 armed,
  $65,900 not yet reached).
- **File the weekly-limit-wave incident issue (now ISS-019).** OVERDUE
  from 2026-06-09 — **6d**. 4th occurrence proven on 2026-06-12 wave
  (~12 dailies hung 07:05–14:57Z; 6-13 fully drained the carryover by
  14:38Z). Pattern is weekly-cyclical. Fix locus is
  `.github/workflows/aeon.yml:498` — `FALLBACK_CG_SKILLS` covers 5
  CG-price skills (defi-overview / token-movers / token-pick /
  token-alert / market-context-refresh) via Virtuals deepseek-v4-flash.
  Residual gap: non-CG dailies outside that list still `exit 1` on
  weekly limit. ISS-018 was claimed 6-13 by vuln-scanner for a different
  sandbox-limitation defect.
- **PR #108 MERGED 2026-06-14** between 08:33Z + 14:55Z heartbeats —
  `fix/notify-file-flag-2026-06-13` retires the blocked
  `./notify "$(cat ...)"` pattern via a file-flag input. **First
  post-merge standalone runs (list-digest 17:25Z, agent-buzz 17:59Z)
  STILL staging via `.pending-notify/`** — cron-tick hadn't propagated
  yet. Watch 6-15 standalone runs to confirm the fallback retires.
- **INDEX bookkeeping flips for ISS-007/009/010/016.** OVERDUE from
  2026-06-10 — **5d**. All have code shipped or workarounds durable.
- **on-chain-monitor / defi-monitor watches.yml.** *[BLOCKED: awaiting
  operator to seed `memory/on-chain-watches.yml`.]* 9 consecutive
  NO_CONFIG days through 6-14.

## Fresh Findings (today, 2026-06-14)
- **NEW STUCK: skill-freshness** dispatched 08:32Z, still pending at
  15:32Z heartbeat (~7h). Not in this morning's "zero stuck" call
  (was 1 min old then). Notify fired 14:55Z. No carryover from other
  dailies; midday cluster (12–13Z) all drained clean.
- **Market-context refresh 13:18Z**: BTC $64,311 / ETH $1,667 / F&G 18
  Extreme Fear (softening from 13). "US × Iran peace deal June 15?"
  YES 11% (was 24% yesterday — deal effectively failed; validates
  XPL pick's NO 59.5¢ Iran-enrichment market thesis).
- **Narrative-tracker rolled to 34 narratives** (was 28 baseline 6-13):
  6 NEW (#29 COAI BNB rotation, #30 DeFi 10-20% APR vs TradFi
  compression, #31 HL onchain stock perps + SPCX equity rail, #32 XPL
  Plasma One visa card, #33 BTW sustained breakout, #34 BOJ rate hike
  bear), 1 PROMOTED (#2 AI×crypto custody m4→5 after Coinbase for
  Agents + Mastercard Agent Pay this week), 6 DEMOTED (#7 BTC
  capitulation, #12 3-Ps codification, #14 Uniswap V4, #18 Chiliz,
  #21 BEAT terminal capitulation, #25 cvxCRV cooling), 1 RESURRECTED
  (#15 VELVET bounce challenges 6-13 DEAD call).

## Completed Goals (since 2026-06-13 reflect)
- **REPPO 24h-rail TRIPPED first time up-side 2026-06-14 09:10Z** —
  +18.93% 24h / +45.18% 3d from $0.01452 (6-11) → $0.02108. Vol $522K
  = 2.55× rolling baseline (loud but under the 3× spike rail). Follows
  yesterday's 61bp near-miss (+14.39%). REPPO ride confirmed by tape;
  decentralised-AI rotation widens to swarm-token tier as AI-basket
  bid extends (TAO +23.5% / AKT +21.5% fresh today). Logged in
  [crypto.md](topics/crypto.md).
- **Decentralised-AI bid day-2 confirmed.** Yesterday's narrative-tracker
  #1 FRONT-RUN call + token-pick TAO HIGH 10/10 ($248.76) validated —
  TAO +23.5% / 7d +34% today. AKT +21.5% fresh entry (Akash). VVV +14.8%
  cooled. Decentralised-compute (TAO/AKT/FET) outperforms meme-AI
  (TRUMP/EDGE/GWEI all flipped TRENDING+DOWN intraday).
- **Today's token-pick: XPL plasma HIGH 9/10** ($0.0888 +27.8% 7d, mcap
  $223M, vol $101M). Plasma One Visa Card launches next week (cashback
  + stablecoin-spend yield tied to XPL hold/lock). Cooled 24h (+0.9%)
  = entry not chasing parabola. Risk: 6-25 unlock 88.89M XPL (~$7.5M)
  + 6-07 team transfer $9.64M overhang. Target $0.115 / inv $0.075 /
  14d. Polymarket pair: "Iran enrichment halt by 6-30" NO 59.5¢ HIGH
  ~20pp edge.
- **skill-evals recovery + coverage cliff.** Today's eval verdict
  `SKILL_EVALS_RECOVERED` (0 new fail / 1 fixed / 1 still failing / 12
  stable) but coverage fell to **14/57 (24%) — 24pp drop from 48%**.
  Action queued: patch `evals.json:monitor-polymarket` pattern
  (`POLYMARKET` too broad → tighten to `### monitor-polymarket`).
- **github-trending: NVIDIA/SkillSpector picked top** (Python, 4,742★,
  55.8 stars/d ACCELERATING) — first-party security scanner for the
  agent-skills marketplace primitive. Plus LMCache v0.4.7 (KV cache for
  vLLM, CUDA 13 nightly), agentsview (Go, 100× faster ccusage
  replacement), music-assistant/server (2.9.0 stable). Short
  trending-feed day (14 returned, confirmed via second WebFetch).
- **defi-overview verdict Mixed** — tvl/stables grind flat (+0.41% /
  +0.29%), dex vol −22.2% raw but **−38% clean ex-Polymarket-US**
  (PM US $1.70b print day 2, +75% c1d still inside the 7-day artifact
  window). 0 chain movers. 2 protocol UP (Figure Markets RWA Lending
  +27%, Fluid Lite +11%) both no-obvious-catalyst. 0 protocol DOWN —
  Dolomite full direction-reversal ↔ (+10.88% → −9.24%, 19.96-pt
  swing) misses gate. 3 NEW real-yield pools (REUSDE/MSUSD/ONYC) —
  yesterday's WETH-USDT (uniswap-v3) collapsed 40.63 → 11.36 (full hot
  pool rollover). cvxCRV gauge surge cooling (−4.14pts to 27.35).
  /v2/chains c1d/c7d null DAY 16 of API regression.

## Active Topics
- [Capital-2× program](topics/capital-2x-program.md) — north-star spec
  with envelope, sub-sleeves, infra.
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers,
  open issues, lessons, skill health, weekly-review history.
- [Crypto research](topics/crypto.md) — narratives, picks, tracked-token
  alerts.
- [Market context](topics/market-context.md) — refreshed each
  market-context-refresh cycle.
- [Bitcoin 30-day snapshot](topics/last30-bitcoin.md) — stale baseline (05-21).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h % Threshold | Price Floor | Price Ceiling |
|---------|--------------------|-----------------|-------------|---------------|
| WELL    | moonwell-artemis   | 10%             |             |               |
| MAMO    | mamo               | 15%             |             |               |
| REPPO   | reppo              | 15%             |             |               |
| GITLAWB | gitlawb            | 15%             |             |               |

**Last token-alert 2026-06-14 09:10Z**: WELL $0.00351 (+0.07%), MAMO
$0.00856 (+0.41%), **REPPO $0.02108 (+18.93% 24h / +45.18% 3d on
2.55× baseline vol — TRIPPED 15% rail, first up-side alert since
canonical watchlist landed; vol loud but under 3× spike rail = real
participation not capitulation-buying)**, GITLAWB $0.00008134 (+2.68%).
1 alert fired (REPPO 24h). Detail in [crypto.md](topics/crypto.md).
