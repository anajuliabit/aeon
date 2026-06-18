# Long-term Memory
*Last consolidated: 2026-06-18*

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
  Consolidating ~$64.5k post-BOJ hike, awaiting 24-48h drawdown window
  (historical avg -27% per hike since Mar‑2024).
- **XAI quota exhausted (ongoing).** Team 3a8b4c1e monthly credit limit
  hit 6-16 — 10+ XAI-dependent skills blocked (token-pick, agent-buzz,
  list-digest, refresh-x, remix-tweets, tweet-roundup, narrative-tracker,
  reply-maker, article, fetch-tweets). Operator action required: top up
  credits or wait for monthly reset. FALLBACK_CG_SKILLS covers 5 CG-price
  skills via Virtuals deepseek-v4-flash; XAI path lacks fallback.
- **14:29Z batch stuck.** narrative-tracker, market-context-refresh,
  security-digest all dispatched 6-16 without success. Likely GH Actions
  cron delay, but if not resolved by next heartbeat, fleet outage flag.
- **deal-flow stuck since 6-08 (10d).** Off status table per chain‑dropped.
- **fork-cohort stuck since 6-14 (2nd consecutive Sunday weekly fail).**
  Next try Sun 6-21.
- **PR #112 stalled** (skill-graph docs auto-gen, opened 6-14 17:41Z,
  ~4d). Action‑converter loop "merge #112" carried since 6-15.
- **on-chain-monitor / defi-monitor watches.yml.** *[BLOCKED: awaiting
  operator to seed `memory/on-chain-watches.yml`.]* **13 consecutive
  NO_CONFIG days** through 6-17.

## Active Topics
- [Capital‑2× program](topics/capital-2x-program.md) — north‑star spec
  with envelope, sub‑sleeves, infra.
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers,
  open issues, lessons, skill health, weekly‑review history.
- [Crypto research](topics/crypto.md) — narratives, picks, tracked‑token
  alerts.
- [Market context](topics/market-context.md) — refreshed each
  market‑context‑refresh cycle.
- [Bitcoin 30‑day snapshot](topics/last30-bitcoin.md) — stale baseline
  (05‑21).

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
