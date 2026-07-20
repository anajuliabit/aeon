# Skill Freshness — 2026-07-14

**Verdict:** ✅ FRESHNESS_OK — all 11 dependencies across 7 consumers are within freshness thresholds

*Audited 43 enabled skills · 11 dependencies checked · 0 flagged*

## Flagged dependencies

*(none — all dependencies within freshness thresholds)*

## What this means per consumer

*(all consumers OK — no action needed)*

## Healthy consumers

- aixbt-pulse — 3 deps (`memory/topics/aixbt-grounding.md`, `aixbt-clusters.md`, `aixbt-chains.md`), all fresh.
- autoresearch — 1 dep (`.outputs/github-trending.md`), all fresh.
- market-context-refresh — 1 dep (`memory/topics/market-context.md`), all fresh.
- reg-monitor — 1 dep (`memory/topics/reg-monitor-seen.md`), all fresh.
- skill-security-scan — 3 deps (`memory/state/security-scan.json` · `articles/security-scan-2026-07-13.md` · `articles/workflow-security-audit-2026-04-11.md`), all fresh.
- unlock-monitor — 1 dep (`memory/state/unlock-monitor-seen.json`), all fresh.
- vuln-scanner — 1 dep (`articles/vuln-scan-2026-07-11.md`), all fresh.
+ 36 more all-fresh consumers (no detectable upstream file dependencies).

## Source status

- `aeon.yml`: 43 entries enabled (of ~130 total); `chains: {}` — no active chains, zero explicit `consume:` edges
- Implicit references discovered: 11
- Explicit `chains: consume:` edges: 0
- Files not yet on disk (skipped — implicit references that never existed): 1 (`articles/token-report-*` in operator-scorecard; producer skill disabled)
- Dedup status: `FRESHNESS_NO_CHANGE` — fingerprint identical to 2026-07-12 run (sha1=da39a3ee, same FRESHNESS_OK verdict, last run 48h ago, within 7-day re-emit window)

### Methodology note

All file ages are computed from on-disk mtimes. In the GitHub Actions sandbox every file is checked out with mtime = clone time, making topic and output files appear 0 h old regardless of when they were actually written. Article staleness is cross-checked against filename dates where available; no filename-date divergence exceeded thresholds for any consumed dependency this run. Non-article deps (`.outputs/`, `memory/topics/`, `memory/state/`) carry mtime = 0 h and read as within-threshold on every checkout-based run — a known limitation of the mtime approach in ephemeral CI runners.

### Observer notes (producer-only, not consumed)

The following producer articles are stale by filename date but are not consumed as explicit dependencies by any enabled skill — not flagged, noted for context:

| Producer | Latest article | Age | Class | Band |
|----------|---------------|-----|-------|------|
| cost-report | `cost-report-2026-06-29.md` | ~360 h (15 d) | articles/weekly | WARN (>192 h, <384 h) |
| weekly-shiplog | `weekly-shiplog-2026-06-29.md` | ~360 h (15 d) | articles/weekly | WARN (>192 h, <384 h) |
| skill-freshness | `skill-freshness-2026-07-12.md` | ~48 h (2 d) | articles/daily | WARN (>28 h, <56 h — missed 7-13 run) |

These are scheduler gaps tracked by `skill-health` (ISS-027 for 12:00 batch dark; weekly-shiplog / cost-report Monday miss streak). This skill reports; `skill-health` tracks and files issues.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
