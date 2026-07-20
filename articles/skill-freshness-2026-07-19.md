# Skill Freshness — 2026-07-19

**Verdict:** ✅ FRESHNESS_OK — all 11 dependencies across 7 consumers are within freshness thresholds

*Audited 43 enabled skills · 11 dependencies checked · 0 flagged*

## Flagged dependencies

*(none — all dependencies within freshness thresholds)*

## What this means per consumer

*(all consumers OK — no action needed)*

## Healthy consumers

- aixbt-pulse — 3 deps (`memory/topics/aixbt-grounding.md`, `aixbt-clusters.md`, `aixbt-chains.md`), all fresh.
- fork-skill-gap — 1 dep (`memory/topics/fork-cohort-state.json`), all fresh.
- market-context-refresh — 1 dep (`memory/topics/market-context.md`), all fresh.
- reg-monitor — 1 dep (`memory/topics/reg-monitor-seen.md`), all fresh.
- skill-security-scan — 3 deps (`memory/state/security-scan.json` · `articles/security-scan-2026-07-13.md` · `articles/workflow-security-audit-2026-04-11.md`), all fresh.
- unlock-monitor — 1 dep (`memory/state/unlock-monitor-seen.json`), all fresh.
- vuln-scanner — 1 dep (`.outputs/github-trending.md`), all fresh.
+ 36 more all-fresh consumers (no detectable upstream file dependencies).

## Source status

- `aeon.yml`: 43 entries enabled (of ~130 total); `chains: {}` — no active chains, zero explicit `consume:` edges
- Implicit references discovered: 11
- Explicit `chains: consume:` edges: 0
- Files not yet on disk (skipped — implicit references that never existed): 1 (`memory/topics/fork-skill-gap-state.json` in fork-skill-gap; implicit ref, MISSING flag suppressed per spec)
- Dedup status: `FRESHNESS_OK` — fingerprint identical to 2026-07-18 run (sha1=da39a3ee, same FRESHNESS_OK verdict, last run ~24 h ago, within 7-day re-emit window); no notification sent (OK verdict is always silent)

### Methodology note

All file ages are computed from on-disk mtimes. In the GitHub Actions sandbox every file is checked out with mtime = clone time, making topic and output files appear 0 h old regardless of when they were actually written. Article staleness is cross-checked against filename dates where available; no filename-date divergence exceeded thresholds for any consumed dependency this run. Non-article deps (`.outputs/`, `memory/topics/`, `memory/state/`) carry mtime = 0 h and read as within-threshold on every checkout-based run — a known limitation of the mtime approach in ephemeral CI runners.

### Observer notes (producer-only, not consumed)

The following producer articles are stale by filename date but are not consumed as explicit dependencies by any enabled skill — not flagged, noted for context:

| Producer | Latest article | Age | Class | Band |
|----------|---------------|-----|-------|------|
| cost-report | `cost-report-2026-06-29.md` | ~480 h (20 d) | articles/weekly | STALE (>384 h, >2×192 h) |
| weekly-shiplog | `weekly-shiplog-2026-06-29.md` | ~480 h (20 d) | articles/weekly | STALE (>384 h, >2×192 h) |

Both remain in the STALE band (entered 2026-07-15; +24 h since yesterday's run, +48 h d2). Root cause per MEMORY.md: Monday-slot scheduler miss streak (ISS-025 / ISS-027). `skill-health` tracks and files issues; this skill reports only.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
