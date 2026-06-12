# Long-term Memory
*Last consolidated: 2026-06-12*

## About This Repo
Aeon — autonomous agent on GitHub Actions via Claude Code. 43 enabled
standalone skills + chains. Inbound messaging via Telegram. soul/ populated
2026-05-25 (ana voice). Reppo-swarm ledger: **25 mints + 45 votes** on-chain
through 2026-06-10 (24th-mint 42eec09d 0xbe195419 788 ENA Close-Short 4.61h
Sharpe 134,103 **+$1,376,882 = largest single-mint pnl ever**; 25th-mint
4b7a4935 0x369daedb 1550 closes 7 perps Sharpe 1197 +$111,862 **= 1st
Step-4.2 PASS re-mint in ledger ever**). No new mints 6-11/6-12 — chain is
off-CI (Docker), ledger only advances on self-hosted runs.

## Current Goals
- **Reppo swarm MIGRATED to Docker (2026-06-10).** The reppo-swarm chain
  is disabled in aeon.yml (`enabled: false`, lines 267-270) — orchestrator/
  trading-agent/voter/digest now run self-hosted. Health skills: do NOT
  file issues about reppo-swarm not running on CI; the on-chain ledger
  continues off-CI.
> **Health-skill directive (still load-bearing):** reppo-swarm chain is
> disabled in aeon.yml (`reppo-orchestrator/trading-agent/voter/digest`
> = `enabled: false`, lines 267–270) — runs self-hosted on Docker. Do NOT
> file issues about reppo-swarm not running on CI; the on-chain ledger
> continues off-CI.
- **CAPITAL-2× PROGRAM (north star): double net worth by 2027-12-31.**
  See [capital-2x-program.md](topics/capital-2x-program.md). Risk sleeve
  ≤15-20% net + moonshot sub-sleeve ≤1% for token-picks. BTC hard-level
  monitor shipped as `skills/btc-levels` (4-hourly).
- **File ISS-018 weekly-limit incident.** OVERDUE from 2026-06-09. 140
  failures 6-06/6-07/6-08, pattern is recurring (weekly cycle), detection
  clean (`api_error_status:429 "weekly limit"`). Fix locus is
  `.github/workflows/aeon.yml:498` (`FALLBACK_CG_SKILLS` covers 5 CG-price
  skills: defi-overview / token-movers / token-pick / token-alert /
  market-context-refresh via Virtuals deepseek-v4-flash). Non-reppo CI
  skills outside that list still fall through to `exit 1` on weekly limit
  — that's the residual gap to document. (Reppo no longer on CI, so
  FALLBACK_REPPO_SKILLS is moot — superseded by the Docker migration.)
- **INDEX bookkeeping flips for ISS-007/009/010/016.** OVERDUE from
  2026-06-10. All have code shipped or workarounds durable. ISS-010
  (phantom chain dispatch) is also moot now — reppo-swarm chain disabled.
- **Datanet RUBRIC.md + 1 datanet config — due TODAY 2026-06-12.** 13
  unassigned datanets surface every off-CI orchestrator run (ids 1, 2,
  4–8, 10, 11, 13, 14, 17, 18).
- **Trading-agent: codify spot_pct threshold + Sharpe-vs-pnl tiebreak.**
  Operator-decision-gated; rules fire correctly in practice. Step-4.2
  admission branch now has working precedent (25th mint, 2026-06-10).
- **on-chain-monitor / defi-monitor watches.yml.** 6 consecutive
  NO_CONFIG days. Operator-gated.

## Completed Goals (since 2026-06-10 reflect)
- **25th mint landed 2026-06-10 18:35Z** — 4b7a4935 0x369daedb 1550 closes
  7 perps Sharpe 1197 +$111,862 tx 0xf81fa571. **1st Step-4.2 PASS re-mint
  in the ledger ever** (re-mint of 23rd-mint same wallet, both metrics
  improved: Sharpe 427→1197, pnl +$104k→+$112k). Ties the 4-mint same-day
  record (2026-06-05). Ledger now 25 mints + 45 votes through 2026-06-10.
- **Corrected stale FALLBACK reference.** MEMORY.md/fleet.md cited
  `aeon.yml:441` for `FALLBACK_CG_SKILLS` — it actually lives at
  `.github/workflows/aeon.yml:498`. FALLBACK_REPPO_SKILLS goal dropped:
  reppo is off-CI post-Docker, so CI rate-limit fallback can't apply.
- **Skill health clean** — last-report 2026-06-10 18:24Z: 37 healthy, 0
  critical/degraded/flapping, 7 no_data (never-run weeklies: autoresearch,
  fork-cohort, fork-skill-digest, fork-skill-gap, operator-scorecard,
  unlock-monitor, vuln-scanner).
  Operator-decision-gated; rules fire correctly in practice. *[BLOCKED:
  awaiting operator decision on thresholds.]*
- **on-chain-monitor / defi-monitor watches.yml.** 7 consecutive
  NO_CONFIG days (through 6-11). Operator-gated. *[BLOCKED: awaiting
  operator to seed memory/on-chain-watches.yml.]*

## Completed Goals (since 2026-06-09 reflect)
- **Reppo swarm MIGRATED to Docker — completed 2026-06-10** (PR #103 merged
  18:34Z, "chore: stop reppo-swarm chain on CI"). Chain disabled in aeon.yml;
  orchestrator/trading-agent/voter/digest now self-hosted off-CI. Directive
  kept at top of Current Goals so health skills don't misfire.
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
  (25 mints + 45 votes).
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

**Last token-alert 2026-06-11 09:10Z** (calmest tape in a week, all 4 green
inside +0.73 to +3.81%, 0 alerts): WELL $0.00360, MAMO $0.00815, REPPO
$0.01452 (+3.65%, snapped its dead-flat band), GITLAWB $0.00009111
(stabilizing after 6-10's -13.71% give-back). REPPO vol still 36% of
baseline. Detail in [crypto.md](topics/crypto.md).
