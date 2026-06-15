# Long-term Memory
*Last consolidated: 2026-06-15*

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
  monitor in `skills/btc-levels` (4-hourly). **Both targets armed:
  reclaim63500 set 6-11; reclaim65900 set 6-15 14:00Z** ($66,427 spot
  reclaim print).
- **File the weekly-limit-wave incident issue (now ISS-019).** OVERDUE
  from 2026-06-09 — **7d**. 4th occurrence proven on 2026-06-12 wave.
  Pattern is weekly-cyclical. Fix locus is `.github/workflows/aeon.yml:498`
  — `FALLBACK_CG_SKILLS` covers 5 CG-price skills (defi-overview /
  token-movers / token-pick / token-alert / market-context-refresh) via
  Virtuals deepseek-v4-flash. Residual gap: non-CG dailies outside that
  list still `exit 1` on weekly limit. ISS-018 was claimed 6-13 by
  vuln-scanner for a different sandbox-limitation defect.
- **INDEX bookkeeping flips for ISS-007/009/010/016.** OVERDUE from
  2026-06-10 — **6d**. All have code shipped or workarounds durable.
- **on-chain-monitor / defi-monitor watches.yml.** *[BLOCKED: awaiting
  operator to seed `memory/on-chain-watches.yml`.]* **10 consecutive
  NO_CONFIG days** through 6-15.

## Fresh Findings (today, 2026-06-15)
- **PR #108 file-flag path CONFIRMED retired the `.pending-notify/`
  fallback fleet-wide.** Today's list-digest (17:52Z) + agent-buzz
  (17:59Z) both delivered inline via `./notify -f`; 6-14 caveat
  ("standalone runs still staging") cleared. Goal dropped from MEMORY.md
  this consolidation.
- **BTC reclaim65900 fired at 14:00Z** ($66,427 spot vs $65,713.62 prior
  close). Both armed levels now SET (reclaim63500 6-11 + reclaim65900
  6-15). Quiet 17:50Z run at $66,877 — stabilization confirmed.
- **btc-levels recovered same-day** — failed 05:42Z (first failure since
  skill landed, empty-usage `total_cost_usd:0` error) → RECOVERED
  07:38Z. sr 0.96, cf 0.
- **skill-freshness recovered** — was stuck 6-14 08:32Z ~25h → today's
  09:48Z tick cleared it (later FRESHNESS_OK at 09:50Z, 44 enabled
  consumers · 8 cross-skill deps · 0 flagged).
- **Risk-on regime flip CONFIRMED on Hormuz peace deal landing.**
  Polymarket "US × Iran peace deal by June 15" YES 11%→93% (+82pp) as
  deadline arrived; oil premium drained into risk. Tape: 86/100 → 92/100
  top-100 green, ETH +8.7% / SOL +8.7% now outrunning BTC +3.3% (alt-bid
  stage). New narrative #27 in tracker.
- **Narrative tracker consolidated 34→27.** 1 NEW (#27 risk-on regime
  flip), 1 RESURRECTED (#13 XMR/ZEC privacy on ZEC +24.5% squeeze+whale+
  audit), 2 PROMOTED (#26 BOJ-tuesday Rising, #1 decAI thesis-hardening),
  2 DEAD (#7 BTC capitulation, #15 VELVET parabolic-reflexivity).
- **Today's token-pick: NEAR HIGH 10/10** ($2.47, +17.5% 24h / +16.3% 7d).
  Dynamic resharding upgrade (v2.13 shipping June) auto-splits shards;
  $32M NEAR Intents fees + $19B cross-chain vol = real usage under the
  move. Target $2.90 / inv $2.10 / 14d. Market SKIPPED — Polymarket
  field ~entirely World Cup futures (efficient, sub-5pp).
- **defi-overview Mixed (risk-on-leaning)** — TVL +2.55% snap (biggest
  1d gain in a week), DEX vol +24% clean ex-Polymarket-US (real bid, not
  just the $2.16b PM artifact day 3). HL Perps fees +69% c1d. WETH-USDT
  real-yield resurrected 11.36 → 40.47 (reverses 6-14 rollover call).
  /v2/chains c1d/c7d null DAY 17 of API regression.
- **weekly-shiplog (Monday) — SHIPLOG_OK.** Aaronjmars/aeon: 113 commits
  / 109 PRs merged / 2 issues closed last 7d. Themes: Multi-provider LLM
  gateway w/ failover; Soul & strategy builders lower on-ramp; Skills
  can call MCP servers mid-run. Window: 2026-06-08→2026-06-15.

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

**Last token-alert 2026-06-15 14:00Z**: WELL $0.00385916 (+9.08% 24h
on 2.55× vol — 92bp under 10% rail, broadest watchlist participation),
MAMO $0.00894360 (+5.06%), REPPO $0.02348886 (+11.03% 24h / +61.7%
from 6-11 — cooled off the 6-14 trip but held gains + added +11.41%
d/d on baseline vol = follow-through not fade), GITLAWB $0.00008605
(+6.42%). Whole watchlist green (median +7.75%). 0 alerts fired —
TOKEN_ALERT_OK. Detail in [crypto.md](topics/crypto.md).
