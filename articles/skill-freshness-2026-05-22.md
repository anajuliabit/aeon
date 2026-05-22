# Skill Freshness — 2026-05-22

**Verdict:** ✅ FRESHNESS_OK — all enabled consumers' file dependencies are fresh or have no assessable stale file

*Audited 20 enabled skills · 12 dependencies checked · 0 flagged*

## Flagged dependencies

*(No flagged dependencies — all within threshold or implicitly skipped per discovery rules.)*

## What this means per consumer

No enabled consumer has a dependency past its freshness threshold. See notes below on the bootstrap context and mtime limitation.

## Healthy consumers

- morning-brief — 0 file deps, all fresh.
- github-trending — 0 file deps, all fresh.
- token-alert — 0 file deps, all fresh.
- defi-overview — 0 file deps, all fresh.
- search-skill — 0 file deps, all fresh.
- skill-security-scan — 1 dep (memory/state/security-scan.json); file absent → implicit MISSING not fired (bootstrap state).
- goal-tracker — 0 file deps, all fresh.
- skill-health — 0 file deps, all fresh.

+ 12 more all-fresh consumers.

## Source status

- `aeon.yml`: ~110 entries parsed, 21 enabled (20 audited as consumers; autoresearch skipped as on_demand)
- Implicit references discovered: 12
- Explicit `chains: consume:` edges: 0 (reppo-swarm chain involves only disabled skills)
- Files not yet on disk (skipped — implicit references that never existed): 10

## Audit detail

### Explicit chain edges
None. The only chain defined (`reppo-swarm`) has all three steps (`reppo-orchestrator`, `reppo-trading-agent`, `reppo-digest`) set to `enabled: false`. No enabled consumer has an explicit `consume:` edge.

### Implicit dependencies assessed

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| action-converter | `memory/topics/last30-bitcoin.md` | topics | ~0h (checkout) | ✅ OK |
| action-converter | `memory/topics/reppo.md` | topics | ~0h (checkout) | ✅ OK |

All other implicit references resolved to files that do not exist on disk. Per the MISSING rule, these are not flagged — they are implicit grep-discovered references from disabled or on_demand producers that have legitimately never written their first output:

- `skill-security-scan` → `memory/state/security-scan.json` — state class, 30d threshold; file absent (bootstrap); implicit MISSING not fired.
- `self-improve` → `articles/repo-actions-*.md` — producer `repo-actions` is disabled; no file; implicit skip.
- `operator-scorecard` → `articles/skill-analytics-*.md` — producer enabled but weekly (Wednesday); no prior run; no file on disk; implicit skip.
- `operator-scorecard` → `articles/heartbeat-*.md` — heartbeat writes to `.outputs/heartbeat.md`, not `articles/`; no heartbeat article on disk; implicit skip.
- `operator-scorecard` → `articles/token-report-*.md`, `articles/repo-pulse-*.md`, `articles/fork-contributor-leaderboard-*.md`, `articles/repo-article-*.md`, `articles/project-lens-*.md` — all from disabled producers; no files; implicit skip.
- `heartbeat` → `articles/token-report-*.md` — producer disabled; no file; implicit skip.

### Bootstrap note

This fleet is in early bootstrap state. The only articles on disk are from disabled skills (`competitor-launch-radar`, `last30`, `workflow-security-audit`, `changelog`) and one date-named file with no skill prefix. No enabled daily skill has yet written its first `articles/{skill}-YYYY-MM-DD.md` output. Once daily skills accumulate their first runs, subsequent skill-freshness audits will have real file ages to measure.

### Mtime limitation

All on-disk files show mtime `2026-05-22 08:45 UTC` — the GitHub Actions checkout time. In a fresh clone, mtime is not a reliable age signal for non-date-stamped files (`memory/topics/`, `memory/state/`). Filename date suffixes (e.g. `-2026-05-21.md`) are the primary age signal for articles. The two topic files assessed (action-converter's deps) show mtime within threshold by both measures.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
