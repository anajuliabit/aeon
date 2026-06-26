# Skill Freshness — 2026-06-26

**Verdict:** ✅ FRESHNESS_OK — all enabled consumers' dependencies are within freshness thresholds

*Audited 44 enabled skills · 2 dependencies checked · 0 flagged*

## Flagged dependencies

*(None — all checked dependencies are fresh)*

## What this means per consumer

All consumers are healthy. No dependencies are past their freshness threshold.

## Healthy consumers

- **operator-scorecard** — 1 dep, all fresh. (`articles/skill-analytics-2026-06-24.md`, ~38h old, weekly threshold 192h ✅)
- **token-pick** — 1 dep, all fresh. (`memory/topics/market-context.md`, updated by daily market-context-refresh, topics threshold 168h ✅)
- morning-brief — 0 tracked deps, all fresh.
- daily-routine — 0 tracked deps, all fresh.
- github-trending — 0 tracked deps, all fresh.
- token-alert — 0 tracked deps, all fresh.
- token-movers — 0 tracked deps, all fresh.
- on-chain-monitor — 0 tracked deps, all fresh.

+ 36 more all-fresh consumers.

## Source status

- `aeon.yml`: 44 entries parsed, 44 enabled
- Explicit `chains: consume:` edges: 0 (`chains: {}` — none active)
- Implicit references discovered: 2 (post-filter: self-reads, self-states, and disabled-producer paths excluded)
- Files not yet on disk (skipped — implicit references that never existed): ~12 (heartbeat articles, push-recap, repo-actions, token-report, repo-pulse, tweet-allocator, repo-article, distribute-tokens — all from disabled producers)

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk article filename dates — this skill measures nothing it does not also report.*
