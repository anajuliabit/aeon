# Long-term Memory
*Last consolidated: 2026-06-13*

## About This Repo
Aeon — autonomous agent on GitHub Actions via Claude Code. 43 enabled
standalone skills + chains. Inbound messaging via Telegram. soul/ populated
2026-05-25 (ana voice). Reppo-swarm ledger: **25 mints + 45 votes** on-chain
through 2026-06-10 (24th-mint 42eec09d 0xbe195419 788 ENA Close-Short 4.61h
Sharpe 134,103 **+$1,376,882 = largest single-mint pnl ever**; 25th-mint
4b7a4935 0x369daedb 1550 closes 7 perps Sharpe 1197 +$111,862 **= 1st
Step-4.2 PASS re-mint in ledger ever**). No new mints 6-11/6-12/6-13 —
chain is off-CI (Docker), ledger only advances on self-hosted runs.

## Current Goals
- **Reppo swarm runs off-CI on Docker (2026-06-10).** The reppo-swarm chain
  is disabled in aeon.yml (`enabled: false`, lines 267-270) — orchestrator/
  trading-agent/voter/digest now run self-hosted.
> **Health-skill directive (still load-bearing):** reppo-swarm chain is
> disabled in aeon.yml (`reppo-orchestrator/trading-agent/voter/digest`
> = `enabled: false`, lines 267–270) — runs self-hosted on Docker. Do NOT
> file issues about reppo-swarm not running on CI; the on-chain ledger
> continues off-CI.
- **CAPITAL-2× PROGRAM (north star): double net worth by 2027-12-31.**
  See [capital-2x-program.md](topics/capital-2x-program.md). Risk sleeve
  ≤15-20% net + moonshot sub-sleeve ≤1% for token-picks. BTC hard-level
  monitor shipped as `skills/btc-levels` (4-hourly).
- **File the weekly-limit-wave incident issue (now ISS-019).** OVERDUE
  from 2026-06-09 — **5d**. 4th occurrence proven on 2026-06-12 wave
  (~12 dailies hung 07:05–14:57Z; carryover cascaded into 6-13 morning
  guarded-dispatch misses; 12:00 UTC cluster self-recovered, 3 dailies
  still stuck at 14:38Z heartbeat). Pattern is weekly-cyclical. **Note:**
  ISS-018 was claimed today by vuln-scanner for a different
  sandbox-limitation defect, so file the weekly-limit incident as ISS-019.
  Fix locus is `.github/workflows/aeon.yml:498` — `FALLBACK_CG_SKILLS`
  covers 5 CG-price skills (defi-overview / token-movers / token-pick /
  token-alert / market-context-refresh) via Virtuals deepseek-v4-flash.
  Residual gap: non-CG dailies outside that list still `exit 1` on
  weekly limit — document explicitly.
- **INDEX bookkeeping flips for ISS-007/009/010/016.** OVERDUE from
  2026-06-10 — **4d**. All have code shipped or workarounds durable.
  ISS-010 (phantom chain dispatch) is moot — reppo-swarm chain disabled.
- **Datanet RUBRIC.md + 1 datanet config.** OVERDUE from 2026-06-12
  — **1d**. 13 unassigned datanets surface every off-CI orchestrator
  run (ids 1, 2, 4–8, 10, 11, 13, 14, 17, 18). 4th weekly slip.
- **Trading-agent: codify spot_pct threshold + Sharpe-vs-pnl tiebreak.**
  *[BLOCKED: awaiting operator decision on thresholds.]* Rules fire
  correctly in practice; Step-4.2 admission branch has working precedent
  (25th mint, 2026-06-10).
- **on-chain-monitor / defi-monitor watches.yml.** *[BLOCKED: awaiting
  operator to seed `memory/on-chain-watches.yml`.]* 8 consecutive
  NO_CONFIG days through 6-13.

## Completed Goals (since 2026-06-12 reflect)
- **6-12 weekly-limit wave proved weekly-cyclical** (4th occurrence
  6-06/07/08 + 6-12). Diagnostic split confirmed: 5 `FALLBACK_CG_SKILLS`
  succeeded via Virtuals, all non-fallback dailies hung. Evening cluster
  self-recovered 16:00–18:16Z; 6-13 12:00 UTC cluster fully drained the
  morning carryover (8 successful runs by 14:38Z). 3 dailies + 11
  weeklies still stuck at last heartbeat — all on cron-tick recovery.
- **ISS-018 filed today 2026-06-13 17:00Z** by vuln-scanner for missing
  `scripts/prefetch-vuln-scanner.sh` (sandbox-limitation high; semgrep/
  trufflehog/osv-scanner unreachable). Distinct issue from the
  weekly-limit incident — the latter still needs filing as ISS-019.
- **vuln-scanner first clean run since enablement** — target
  superloglabs/superlog (806★ TS Apache-2.0), 0 confirmed bugs across
  12 advisory candidates (esbuild Deno-path / react-router declarative-
  mode preconditions not met; next 15.5.15 demo-only sample app
  dropped per `demo/` triage). Dedup window armed through 2026-07-13.
- **28-narrative tracker rolled forward** — 5 NEW (decentralized AI bid
  standalone on Anthropic Fable-5+Mythos-5 export-control directive;
  Polymarket US CFTC-approved $969M debut; Curve gauge weight rotation
  cvxCRV+13pts / sdcrv+3.5pts; CFTC onshore BTC perp futures; AI
  engineering layoffs); 1 PROMOTED (AI×crypto agent custody hardening
  — Coinbase agent accounts 6-12 = 5th big-co primitive in 4 months);
  3 DEMOTED (HL perp DEX, stablecoin rails, capital rotation); 2 DEAD
  (XMR/ZEC privacy-coin rotation — 4th failed privacy call closed
  clean; VELVET parabolic terminal capitulation, 6-11 FADE validated).
- **Skill-health snapshot 6-12 18:09Z**: 41 healthy / 0 flagged / 2
  no_data (operator-scorecard + fork-skill-gap await first weekly tick).
  Cleaner than 6-10 baseline (7 no_data → 2). Detail in
  [fleet.md](topics/fleet.md).

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

**Last token-alert 2026-06-14 09:10Z**: WELL $0.00351 (+0.07%), MAMO
$0.00856 (+0.41%), **REPPO $0.02108 (+18.93% 24h / +45.18% 3d on
2.55× baseline vol — TRIPS 15% rail, first up-side alert since
canonical watchlist landed; follows yesterday's 61bp near-miss)**,
GITLAWB $0.00008134 (+2.68%). 1 alert fired (REPPO 24h). Detail in
[crypto.md](topics/crypto.md).
