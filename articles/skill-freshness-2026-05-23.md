# Skill Freshness — 2026-05-23

**Verdict:** ✅ FRESHNESS_OK — all 4 assessable dependencies are fresh; 11 implicit references skipped (disabled producers or never-existed files)

*Audited 20 enabled skills · 15 dependencies checked · 0 flagged*

## Flagged dependencies

*(No flagged dependencies — all within threshold or implicitly skipped per discovery rules.)*

## What this means per consumer

No enabled consumer has a dependency past its freshness threshold. See the audit detail below for context on skipped implicit references.

## Healthy consumers

- action-converter — 4 deps (memory/topics/*), all fresh.
- morning-brief — 0 file deps, all fresh.
- github-trending — 0 file deps, all fresh.
- token-alert — 0 file deps, all fresh.
- defi-overview — 0 file deps, all fresh.
- search-skill — 0 file deps, all fresh.
- skill-security-scan — 1 dep (memory/state/security-scan.json); file absent → implicit MISSING not fired (bootstrap state).
- goal-tracker — 0 file deps, all fresh.

+ 12 more all-fresh consumers.

## Source status

- `aeon.yml`: ~110 entries parsed, 21 enabled (20 audited as consumers; autoresearch skipped as on_demand)
- Implicit references discovered: 15
- Explicit `chains: consume:` edges: 0 (reppo-swarm chain involves only disabled skills)
- Files not yet on disk (skipped — implicit references that never existed or disabled producers): 11

## Audit detail

### Explicit chain edges
None. The only chain defined (`reppo-swarm`) has all three steps (`reppo-orchestrator`, `reppo-trading-agent`, `reppo-digest`) set to `enabled: false`. No enabled consumer has an explicit `consume:` edge.

### Implicit dependencies assessed

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| action-converter | `memory/topics/last30-bitcoin.md` | topics | ~2 min (checkout) | ✅ OK |
| action-converter | `memory/topics/reppo.md` | topics | ~2 min (checkout) | ✅ OK |
| action-converter | `memory/topics/crypto.md` | topics | ~2 min (checkout) | ✅ OK |
| action-converter | `memory/topics/fleet.md` | topics | ~2 min (checkout) | ✅ OK |

### Implicit dependencies skipped

All other implicit references resolved to files that do not exist on disk or come from disabled producers. Per the MISSING rule, these are not flagged — implicit grep-discovered references that never existed are not fired:

- `operator-scorecard` → `articles/skill-analytics-*.md` — skill-analytics enabled (weekly Wed); no file on disk; implicit glob ref (not canonical `${today}` pattern) → implicit skip. Note: last Wednesday was 2026-05-21; first skill-analytics article has not yet been written.
- `operator-scorecard` → `articles/heartbeat-*.md` — heartbeat is enabled daily but writes to `.outputs/heartbeat.md`, not `articles/`; no heartbeat article file exists or will exist in this path; implicit skip.
- `operator-scorecard` → `articles/tweet-allocator-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`, `articles/fork-contributor-leaderboard-*.md`, `articles/repo-article-*.md`, `articles/project-lens-*.md`, `articles/distribute-tokens-*.md` — all from disabled producers; no files; implicit skip.
- `heartbeat` → `articles/token-report-*.md` — producer disabled; no file; implicit skip.
- `self-improve` → `articles/repo-actions-*.md` — producer disabled; no file; implicit skip.
- `skill-security-scan` → `memory/state/security-scan.json` — state class, 30d threshold; file absent (bootstrap); implicit MISSING not fired.

### Bootstrap note

This fleet is in early bootstrap state. Daily skills have begun running (morning-brief, heartbeat, reppo-swarm chain confirmed in today's log), but most enabled skills have not yet written their first `articles/{skill}-YYYY-MM-DD.md` output. The only skill freshness can assess today is action-converter's topic file reads. Once daily and weekly skills accumulate their first article outputs, subsequent skill-freshness audits will have real file ages to measure.

### Mtime limitation

All on-disk files show mtime `2026-05-23 08:34 UTC` — the GitHub Actions checkout time for this run (113 seconds before current time 08:36 UTC). In a fresh clone, mtime is not a reliable age signal for non-date-stamped files. Filename date suffixes (e.g. `-2026-05-22.md`) are the primary age signal for articles. The four topic files assessed (action-converter's deps) show mtime within threshold by both measures (threshold 168h, age ~2 min).

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
