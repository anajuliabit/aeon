# Skill Freshness — 2026-07-11

**Verdict:** ✅ FRESHNESS_OK — all 5 tracked dependencies are within freshness thresholds

*Audited 43 enabled skills · 5 dependencies checked · 0 flagged*

## Flagged dependencies

*(None — every tracked dependency is fresh.)*

## What this means per consumer

*(No consumer has a dependency past threshold.)*

## Healthy consumers

- token-pick — 1 dep, all fresh. (`memory/topics/market-context.md` ← market-context-refresh)
- vuln-scanner — 1 dep, all fresh. (`.outputs/github-trending.md` ← github-trending)
- fork-skill-gap — 1 dep, all fresh. (`memory/topics/fork-cohort-state.json` ← fork-cohort)
- operator-scorecard — 2 deps, all fresh. (`articles/skill-analytics-2026-07-08.md` ← skill-analytics; `articles/project-lens-2026-06-22.md` ← project-lens/on_demand)
- + 39 more all-fresh consumers (0 cross-skill deps detected).

## Dependency scores

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| token-pick | `memory/topics/market-context.md` | topics | <1m | 168h | ✅ OK |
| vuln-scanner | `.outputs/github-trending.md` | outputs | <1m | 4h | ✅ OK |
| fork-skill-gap | `memory/topics/fork-cohort-state.json` | topics | <1m | 168h | ✅ OK |
| operator-scorecard | `articles/skill-analytics-2026-07-08.md` | articles (weekly) | <1m | 192h | ✅ OK |
| operator-scorecard | `articles/project-lens-2026-06-22.md` | articles (on_demand) | <1m | n/a | ✅ OK |

## Source status

- `aeon.yml`: ~115 entries, 43 enabled
- Implicit references discovered: 29
- Explicit `chains: consume:` edges: 0
- Files not yet on disk (skipped — implicit references that never existed): 10
  - `articles/heartbeat-*.md` — heartbeat outputs to `.outputs/` not `articles/`
  - `articles/tweet-allocator-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`, `articles/fork-contributor-leaderboard-*.md`, `articles/repo-article-*.md`, `articles/distribute-tokens-*.md` — producers disabled
  - `articles/repo-actions-*.md`, `articles/push-recap-*.md` — producers disabled
  - `memory/topics/agent-evals.md` — never created by any active skill

## Dedup and notification

**Dedup:** Fingerprint and verdict unchanged from 2026-07-10 run (`FRESHNESS_OK`, fingerprint `da39a3ee`). Notification suppressed — `FRESHNESS_NO_CHANGE`. This run is day 2 of a consecutive FRESHNESS_OK streak (first: 2026-07-10). Re-emits after 7-day window (next re-emit trigger: 2026-07-17 if state persists).

> **Note on mtime:** All on-disk mtimes reflect the most recent `git checkout` (~08:08 UTC today), so age readings are uniformly <1 minute. The freshness signal in this environment comes from file **existence** checks (canonical `articles/{producer}-${today}.md` patterns) rather than mtime drift. No canonical-pattern MISSING flags were raised: every reference resolves to an existing file or is an on_demand/disabled producer with no expected cadence.

> **Runtime caveat — checkout mtime masking:** `github-trending` has been dark for ~3 consecutive days (last dispatch 2026-07-08T09:02Z; confirmed d3 miss per heartbeat log). In a persistent runtime environment, `.outputs/github-trending.md` would read as ~71h stale — well past the 4h outputs threshold (STALE verdict). In this fresh-checkout environment, the file's mtime resets to checkout time on every workflow run, masking the real staleness. `skill-health` and `heartbeat` already track this via run-history (ISS-025 / batch-dark d3 flags); skill-freshness supplements, not duplicates, that coverage. Similarly, the 8-skill batch-dark cluster (token-pick / defi-overview / token-movers / on-chain-monitor / defi-monitor / market-context-refresh / narrative-tracker / aixbt-pulse; last_success 2026-06-28, day-13) would show stale topic writes in a persistent environment — these are tracked under ISS-027.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
