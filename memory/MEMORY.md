# Long-term Memory
*Last consolidated: 2026-06-10*

## About This Repo
Aeon — autonomous agent on GitHub Actions via Claude Code. 43 enabled
standalone skills + chains. Inbound messaging via Telegram. soul/ populated
2026-05-25 (ana voice). Reppo-swarm ledger: **24 mints + 45 votes** on-chain
through 2026-06-10 (24th-mint 42eec09d 0xbe195419 788 ENA Close-Short 4.61h
Sharpe 134,103 **+$1,376,882 = largest single-mint pnl ever**, 2nd-highest
Sharpe behind only 6th-mint BRENTOIL 295,747).

## Current Goals
- **CAPITAL-2× PROGRAM (north star): double net worth by 2027-12-31.**
  See [capital-2x-program.md](topics/capital-2x-program.md). Risk sleeve
  ≤15-20% net + moonshot sub-sleeve ≤1% for token-picks. BTC hard-level
  monitor shipped as `skills/btc-levels` (4-hourly).
- **TOP — Extend FALLBACK_*_SKILLS to cover reppo chain by 2026-06-11.**
  PRs #77/#78/#79 Virtuals + deepseek-v4-flash fallback covers 5 CG-price
  skills only (`FALLBACK_CG_SKILLS` at `aeon.yml:441`); reppo-orchestrator /
  reppo-trading-agent / reppo-voter / reppo-digest fall through to `exit 1`.
  Mirror PR #79 pattern with `FALLBACK_REPPO_SKILLS` constant. 1 day to deadline.
- **File ISS-018 weekly-limit incident.** OVERDUE from 2026-06-09. 140
  failures 6-06/6-07/6-08, pattern is recurring (weekly cycle), detection
  clean (`api_error_status:429 "weekly limit"`), fix locus `aeon.yml:441`.
- **INDEX bookkeeping flips for ISS-007/009/010/016.** OVERDUE from
  2026-06-10. All have code shipped or workarounds durable.
- **Datanet RUBRIC.md + 1 datanet config by 2026-06-12.** 3rd consecutive
  weekly slip. 13 unassigned datanets surfacing every orchestrator run
  (ids 1, 2, 4–8, 10, 11, 13, 14, 17, 18).
- **Trading-agent: codify spot_pct threshold + Sharpe-vs-pnl tiebreak.**
  Operator-decision-gated; rules fire correctly in practice.
- **on-chain-monitor / defi-monitor watches.yml.** 5 consecutive
  NO_CONFIG days. Operator-gated.

## Completed Goals (since 2026-06-09 reflect)
- **4 new mints landed 2026-06-10 (21st → 24th)** — biggest single day ever
  by pnl, ends 2-day mintless streak: 21st cc128e78 BTC+XPL HFT 70 closes
  Sharpe 4064 +$1,147 tx 0x74ced26d; 22nd canonical re-mint 214cd4c2 (after
  ledger backfill gap); 23rd 19e8cfb3 0x369daedb 1337 closes 7 perps Sharpe
  427 +$104,013 tx 0xf1b68196; **24th 42eec09d 0xbe195419 788 ENA close-short
  Sharpe 134,103 +$1,376,882 tx 0xf68bc9f5 — largest pnl in ledger ever**.
- **ISS-016 new "concurrent-same-run variant" filed 2026-06-10** + new fix
  path: voter consumes trading-agent's queued mint intents from
  `.pending-reppo/`. Ledger workaround now **25 consecutive voter runs**
  with cache count=0 — defensive cross-ref durable, 1 same-day own-pod
  catch (pod 934 minted earlier this UTC day).
- **Stuck-skills cluster drained 20 → 11.** All 11 remaining are weekly
  slots (Sun/Mon/Sat) that won't fire until next cron tick. Self-resolves.

## Active Topics
- [Capital-2× program](topics/capital-2x-program.md) — north-star spec
  with envelope, sub-sleeves, infra.
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers,
  open issues, lessons, skill health, weekly-review history.
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit
  (24 mints + 45 votes).
- [Crypto research](topics/crypto.md) — narratives, picks, tracked-token
  alerts.
- [Market context](topics/market-context.md) — refreshed each
  market-context-refresh cycle.
- [TradingGymAI (datanet 9) contributor spec](topics/tradinggymai-spec.md) —
  operator-shared 2026-05-26.
- [Bitcoin 30-day snapshot](topics/last30-bitcoin.md) — stale baseline (05-21).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h % Threshold | Price Floor | Price Ceiling |
|---------|--------------------|-----------------|-------------|---------------|
| WELL    | moonwell-artemis   | 10%             |             |               |
| MAMO    | mamo               | 15%             |             |               |
| REPPO   | reppo              | 15%             |             |               |
| GITLAWB | gitlawb            | 15%             |             |               |

**2026-06-10 watchlist state:** GITLAWB **-13.71% gives back 73% of
yesterday's +18.74% squeeze** on $455K light tape (mean-reversion loop
closed, 6-04 cap → 6-05 low → 6-09 squeeze → 6-10 give-back; net +22.85%
from 6-05 low). WELL -2.68%, MAMO -3.56%, REPPO -0.26% (vol drained to
$113K, 88% below baseline). 0 alerts triggered. Detail in [crypto.md](topics/crypto.md).
