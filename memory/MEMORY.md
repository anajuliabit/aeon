# Long-term Memory
*Last consolidated: 2026-06-16*

## About This Repo
Aeon — autonomous agent on GitHub Actions via Claude Code. Standalone
skills on cron. Inbound messaging via Telegram. soul/ populated
2026-05-25 (ana voice).

## Current Goals
> **Health-skill directive:** reppo-swarm (orquestra) removed entirely
> — lives at `~/code/orquestra` (self-hosted Docker). Do NOT re-add
> reppo-orchestrator/trading-agent/voter/digest skills, chains, or
> scripts here, and do NOT file issues about reppo-swarm not running
> on CI.
- **CAPITAL-2× PROGRAM (north star): double net worth by 2027-12-31.**
  See [capital-2x-program.md](topics/capital-2x-program.md). Risk sleeve
  ≤15-20% net + moonshot sub-sleeve ≤1% for token-picks. BTC hard-level
  monitor in `skills/btc-levels` (4-hourly). Both armed reclaim levels
  now SET (reclaim63500 6-11, reclaim65900 6-15 on Hormuz peace deal).
  Consolidating ~$66k+ pre-BOJ-Tuesday.
- **File ISS-019 weekly-limit wave incident.** OVERDUE from 2026-06-09
  — **8d**. 4th occurrence proven 2026-06-12; weekly-cyclical. Fix
  locus `.github/workflows/aeon.yml:498` — `FALLBACK_CG_SKILLS` covers
  5 CG-price skills via Virtuals deepseek-v4-flash. Residual gap:
  non-CG dailies + XAI-dependent skills still `exit 1` on weekly limit.
- **XAI quota exhausted (NEW 2026-06-16).** Team 3a8b4c1e monthly
  credit limit hit — 3 skills blocked (token-pick 12:42Z, agent-buzz
  17:56Z, list-digest 17:56Z). XAI-dependent skills (agent-buzz /
  token-pick / refresh-x / remix-tweets / tweet-roundup /
  narrative-tracker / reply-maker / list-digest / article /
  fetch-tweets) NOT covered by FALLBACK_CG_SKILLS. Operator action:
  top up credits or wait for monthly reset.
- **INDEX bookkeeping flips for ISS-007/009/010/016.** OVERDUE from
  2026-06-10 — **6d**. All have code shipped or workarounds durable.
- **PR #112 stalled** (skill-graph docs auto-gen, opened 6-14 17:41Z,
  ~48h+ past 24h threshold). Action-converter loop "merge #112"
  carried since 6-15 19:23Z.
- **on-chain-monitor / defi-monitor watches.yml.** *[BLOCKED: awaiting
  operator to seed `memory/on-chain-watches.yml`.]* **12 consecutive
  NO_CONFIG days** through 6-16.

## Active Topics
- [Capital-2× program](topics/capital-2x-program.md) — north-star spec
  with envelope, sub-sleeves, infra.
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers,
  open issues, lessons, skill health, weekly-review history.
- [Crypto research](topics/crypto.md) — narratives, picks, tracked-token
  alerts.
- [Market context](topics/market-context.md) — refreshed each
  market-context-refresh cycle.
- [Bitcoin 30-day snapshot](topics/last30-bitcoin.md) — stale baseline
  (05-21).

## Tracked Tokens
Canonical watchlist per `skills/token-alert/SKILL.md` format (PR #55).

| Token   | CoinGecko ID       | 24h % Threshold | Price Floor | Price Ceiling |
|---------|--------------------|-----------------|-------------|---------------|
| WELL    | moonwell-artemis   | 10%             |             |               |
| MAMO    | mamo               | 15%             |             |               |
| REPPO   | reppo              | 15%             |             |               |
| GITLAWB | gitlawb            | 15%             |             |               |

**Last token-alert 2026-06-16 ~12:45 UTC**: REPPO -15.78% TRIPPED
DOWN-SIDE (first down-side alert since canonical watchlist landed;
mirror inverse of 6-14's +18.93% up-trip). WELL -1.67%, MAMO -1.16%,
GITLAWB +9.66%. Detail in [crypto.md](topics/crypto.md).
