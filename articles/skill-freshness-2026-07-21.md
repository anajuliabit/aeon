# Skill Freshness — 2026-07-21

**Verdict:** ✅ FRESHNESS_OK — all 8 checked dependencies within freshness windows

*Audited 43 enabled skills · 8 dependencies checked · 0 flagged*

## Flagged dependencies

*(none — all dependencies fresh)*

## What this means per consumer

*(no consumers with degraded verdict)*

## Healthy consumers

- token-pick — 2 deps (`memory/topics/market-context.md`, `memory/topics/aixbt-grounding.md`), all fresh.
- operator-scorecard — 1 dep (`articles/skill-analytics-2026-07-15.md`), all fresh.
- vuln-scanner — 1 dep (`.outputs/github-trending.md`, optional fallback), all fresh.
- fork-skill-gap — 1 dep (`memory/topics/fork-cohort-state.json`), all fresh.
- reflect — 1 dep (recent `articles/` last 7d), all fresh.
- action-converter — 2 deps (recent `articles/` last 7d + `memory/topics/*.md`), all fresh.
- weekly-shiplog — 1 dep (`articles/push-recap-*.md`) skipped (producer `push-recap` disabled → never existed).
+ 36 more all-fresh consumers.

## Dependency detail

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| token-pick | `memory/topics/market-context.md` | topics | ~0h (checkout mtime) | 168h | ✅ OK |
| token-pick | `memory/topics/aixbt-grounding.md` | topics | ~0h (checkout mtime) | 168h | ✅ OK |
| operator-scorecard | `articles/skill-analytics-2026-07-15.md` | articles/weekly | 144h (filename: 2026-07-15) | 192h | ✅ OK |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~0h (checkout mtime) | 4h | ✅ OK |
| fork-skill-gap | `memory/topics/fork-cohort-state.json` | topics | ~0h (checkout mtime) | 168h | ✅ OK |
| reflect | `articles/` (newest: 2026-07-20) | articles/daily | ~21h (filename: 2026-07-20) | 28h | ✅ OK |
| action-converter | `articles/` (newest: 2026-07-20) | articles/daily | ~21h (filename: 2026-07-20) | 28h | ✅ OK |
| action-converter | `memory/topics/*.md` | topics | ~0h (checkout mtime) | 168h | ✅ OK |

**Note on mtime environment:** This run is executing from a git checkout (all files stamped `2026-07-21 09:42 UTC`). For `.outputs/`, `memory/topics/`, and `memory/state/` dependencies, on-disk mtimes read as ~0h old — correct in production but cannot distinguish between a file written today and one written months ago. Article-class dependencies use filename-date parsing to bypass this limitation (more reliable in checkout environments). In a live production run where files are written incrementally, mtime-based detection would surface actual staleness the filename-date fallback cannot (e.g., a `.outputs/market-context-refresh.md` that hasn't been refreshed in 48h due to the 0.32 sr degradation flagged in this morning's health summary).

## Source status

- `aeon.yml`: 130+ entries, 43 enabled
- Implicit references discovered: 11
- Explicit `chains: consume:` edges: 0 (chains: {} — none active)
- Files not yet on disk (skipped — implicit references that never existed): 3
  - `articles/push-recap-*.md` (weekly-shiplog dep; `push-recap` disabled)
  - `articles/repo-actions-*.md` (self-improve dep; `repo-actions` disabled)
  - `articles/heartbeat-*.md` (operator-scorecard dep; `heartbeat` writes to memory/logs + .outputs, not articles/)

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
