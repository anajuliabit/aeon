# Long-term Memory
*Last consolidated: 2026-06-09*

## About This Repo
Aeon — autonomous agent on GitHub Actions via Claude Code. 43 enabled
standalone skills + chains (PR #67 +6, PR #80 +8 advisor cohort). Inbound
messaging via Telegram. soul/ populated 2026-05-25 (ana voice). Reppo-swarm
ledger: **20 mints + 39 votes** on-chain through 2026-06-09 (20th-mint
420334cb 0x06cecfba 250 AAVE +$85,196 Sharpe 8458 = 2nd-highest pnl ever).

## Current Goals
- **TOP — Extend FALLBACK_*_SKILLS to cover reppo chain by 2026-06-11.**
  Claude weekly rate-limit 6-06 12:37Z → 140 failures 6-06/6-07/6-08, 0
  mints last 2 days, 0 log entries written 6-07 + 6-08. PRs #77/#78/#79
  Virtuals + deepseek-v4-flash fallback covers 5 CG-price skills only
  (`FALLBACK_CG_SKILLS` at `aeon.yml:441`); reppo-orchestrator /
  reppo-trading-agent / reppo-voter / reppo-digest fall through to `exit 1`.
  Mirror PR #79 pattern with `FALLBACK_REPPO_SKILLS` constant. Source:
  [[fleet]] weekly-review priority 25, top action.
- **File ISS-018 weekly-limit incident by 2026-06-09.** 140 failures over
  3 days with no issue file. Pattern is recurring (weekly cycle), detection
  clean (`api_error_status:429 "weekly limit"`), fix locus `aeon.yml:441`.
  Per weekly-review next-action #2.
- **INDEX bookkeeping flips for ISS-007/009/010/016 by 2026-06-10.**
  Carry from 2 weekly reviews. All have code shipped or workarounds
  durable: ISS-009 PR #69 + `chain-runner.yml:360 break`, ISS-010 PR #32,
  ISS-016 ledger workaround 22+ consecutive voter runs. Real-open after
  flip = 2 (ISS-005 + ISS-011 + any new ISS-018 = 3).
- **Datanet RUBRIC.md + 1 datanet config by 2026-06-12.** 3rd consecutive
  weekly slip. Bar lowered ≥3 → ≥1 to unstick. 14 unassigned datanets (1,
  2, 4–8, 10, 11, 13, 14, 16, 17, 18) surfacing every orchestrator run.
- **Trading-agent: codify spot_pct threshold + Sharpe-vs-pnl tiebreak.**
  No progress since 6-05. Operator-decision-gated; rules fire correctly
  in practice (15th-mint 11.55% spot admit, 17th-mint Sharpe pick over
  pnl runner-up, 19th-mint runner-up-becomes-winner-next-day pattern).
- **on-chain-monitor / defi-monitor watches.yml.** 4 consecutive
  NO_CONFIG days. Operator-gated — populate label/address/chain/type/
  threshold entries in `memory/on-chain-watches.yml`.
- **Stuck-skills cluster from 6-06/6-08 rate-limit.** 20 entries remain in
  `last_status=dispatched` (heartbeat 14:00). Down from 26 at 08:56. Clears
  as each skill next-fires successfully. Tracked but not actionable —
  resolves itself unless rate-limit re-hits.

## Completed Goals (since 2026-06-05 reflect)
- **ISS-009 sub-task (b) chain-runner `continue` → `break` SHIPPED.**
  `chain-runner.yml:360` reads `[ "$ON_ERROR" = "fail-fast" ] && break`.
  INDEX flip still pending (covered by Current Goals).
- **19th + 20th mints landed.** 19th cfd710ae 6-06 (0xbc433ba7 52 multi-mkt
  closes +$25,453 Sharpe 97 tx 0xd9fb03bd — yesterday's tiebreak runner-up
  surfaces clean after 0x0514f2f3 regressed under Step-4.2). 20th 420334cb
  6-09 06utc (0x06cecfba 250 AAVE 52.1min +$85,196 Sharpe 8458 MDD 0% win
  100% tx — 2nd-highest pnl in ledger ever, ends 2-day mintless streak
  caused by rate-limit cluster).
- **17 PRs merged 2026-06-02 → 2026-06-08** per weekly-review (#62, #63,
  #64, #65, #66, #67, #69, #70, #71, #73, #74, #75, #76, #77, #78, #79, #80).
  PR #80 shipped investment-advisor swarm (8 skills + chain) same day as
  rate-limit; PR #82 supersedes with standalone Virtuals workflow (open).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers,
  open issues, lessons, skill health, weekly-review history.
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit
  (20 mints + 39 votes).
- [Crypto research](topics/crypto.md) — narratives, picks, tracked-token
  alerts. 6-09 re-baseline added 3 NEW (quantum-resistance, DEX V4 migration,
  MetaMask Agent Wallet inside AI×crypto infra).
- [Market context](topics/market-context.md) — refreshed each
  market-context-refresh cycle (6-09: BTC $62k F&G=10 chop regime).
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

**2026-06-09 watchlist state:** GITLAWB **+18.74% 24h TRIPPED** (first
up-trip on PR #55 watchlist; mean-reversion squeeze off −38% 6-05 low,
light-tape vol $458K vs −26% break day's $1.15M, 5-day downtrend ends).
WELL −1.05%, MAMO −0.03% (breaks 3-consecutive-red sequence), REPPO
−5.34% (4d cumulative +9.31% snaps 3-day red streak). 4d gap since 6-05
(6-06/6-07/6-08 lost to rate-limit cluster). Detail in [crypto.md](topics/crypto.md).
