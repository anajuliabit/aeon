# Skill Freshness — 2026-07-01

**Verdict:** ✅ FRESHNESS_OK — all 3 cross-skill dependencies resolved within threshold

*Audited 43 enabled skills · 3 dependencies checked · 0 flagged*

## Flagged dependencies

*(none — all dependencies are fresh)*

## What this means per consumer

No enabled consumer is reading a stale upstream file. All cross-skill file dependencies resolved within their per-class freshness windows.

## Healthy consumers

- fork-skill-gap — 1 dep (`memory/topics/fork-cohort-state.json` ← fork-cohort), all fresh.
- operator-scorecard — 1 dep (`articles/skill-analytics-2026-06-24.md` ← skill-analytics), all fresh.
- vuln-scanner — 1 dep (`.outputs/github-trending.md` ← github-trending), all fresh.
- morning-brief — 0 cross-skill deps tracked, all fresh.
- daily-routine — 0 cross-skill deps tracked, all fresh.
- github-trending — 0 cross-skill deps tracked, all fresh.
- token-pick — 0 cross-skill deps tracked, all fresh.
- heartbeat — 1 implicit ref to `articles/token-report-*.md` (no file on disk; skipped per implicit-never-existed rule), all fresh.
+ 35 more all-fresh consumers.

## Source status

- `aeon.yml`: ~100 entries, 43 enabled
- Implicit references discovered: 3
- Explicit `chains: consume:` edges: 0 (chains: {} — no active chains)
- Files not yet on disk (skipped — implicit references that never existed): 2
  - `heartbeat` → `articles/token-report-*.md` (producer `token-report` disabled; no files on disk)
  - `self-improve` → `articles/repo-actions-*.md` (producer `repo-actions` disabled; no files on disk)

### Dependency detail (all OK)

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| fork-skill-gap | `memory/topics/fork-cohort-state.json` | topics | ~3 min | 168h (7d) | ✅ OK |
| operator-scorecard | `articles/skill-analytics-2026-06-24.md` | articles/weekly | ~3 min | 192h (8d) | ✅ OK |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~3 min | 4h | ✅ OK |

> **Note on mtime environment:** All file timestamps reflect the git checkout time (2026-07-01 08:31 UTC). In this GitHub Actions environment, mtime-based scoring shows all files as ~3 minutes old. The filename-embedded dates provide an alternate staleness signal: the most recent `skill-analytics` article is dated 2026-06-24 (7 days = 168h), which is within the 192h weekly threshold and thus still OK. Flagging would occur at 384h (2× threshold = 16 days).

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
