# Skill Freshness — 2026-07-10

**Verdict:** ✅ FRESHNESS_OK — all 5 tracked dependencies are within freshness thresholds

*Audited 43 enabled skills · 5 dependencies checked · 0 flagged*

## Flagged dependencies

*(None — every tracked dependency is fresh.)*

## Healthy consumers

- token-pick — 1 dep, all fresh. (`memory/topics/market-context.md` ← market-context-refresh)
- vuln-scanner — 1 dep, all fresh. (`.outputs/github-trending.md` ← github-trending)
- fork-skill-gap — 1 dep, all fresh. (`memory/topics/fork-cohort-state.json` ← fork-cohort)
- operator-scorecard — 2 deps, all fresh. (`articles/skill-analytics-2026-07-08.md` ← skill-analytics; `articles/project-lens-2026-06-22.md` ← project-lens/on_demand)
- + 39 more all-fresh consumers (0 cross-skill deps detected).

## Source status

- `aeon.yml`: ~115 entries, 43 enabled
- Implicit references discovered: 29
- Explicit `chains: consume:` edges: 0
- Files not yet on disk (skipped — implicit references that never existed): 10
  - `articles/heartbeat-*.md` — heartbeat outputs to `.outputs/` not `articles/`
  - `articles/tweet-allocator-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`, `articles/fork-contributor-leaderboard-*.md`, `articles/repo-article-*.md`, `articles/distribute-tokens-*.md` — producers disabled
  - `articles/repo-actions-*.md`, `articles/push-recap-*.md` — producers disabled
  - `memory/topics/agent-evals.md` — never created by any active skill

## Dependency scores

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| token-pick | `memory/topics/market-context.md` | topics | <1m | 168h | ✅ OK |
| vuln-scanner | `.outputs/github-trending.md` | outputs | <1m | 4h | ✅ OK |
| fork-skill-gap | `memory/topics/fork-cohort-state.json` | topics | <1m | 168h | ✅ OK |
| operator-scorecard | `articles/skill-analytics-2026-07-08.md` | articles (weekly) | <1m | 192h | ✅ OK |
| operator-scorecard | `articles/project-lens-2026-06-22.md` | articles (on_demand) | <1m | n/a | ✅ OK |

> **Note on mtime:** All on-disk mtimes reflect the most recent `git checkout` (~08:38 UTC today), so age readings are uniformly <1 minute. The freshness signal in this environment comes from file **existence** checks (canonical `articles/{producer}-${today}.md` patterns) rather than mtime drift. No canonical-pattern MISSING flags were raised: every reference resolves to an existing file or is an on_demand/disabled producer with no expected cadence.

> **Dedup:** Fingerprint and verdict unchanged from 2026-07-09 run (`FRESHNESS_OK`, fingerprint `da39a3ee`). Notification suppressed — `FRESHNESS_NO_CHANGE`. Re-emits after 7-day window if state persists.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
