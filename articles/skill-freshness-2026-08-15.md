# Skill Freshness — 2026-08-15

**Verdict:** ✅ FRESHNESS_OK — all 43 enabled consumers' upstream dependencies are fresh

*Audited 43 enabled skills · 9 dependencies checked · 0 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|

*(none — all dependencies within threshold)*

## What this means per consumer

No consumers have stale or missing dependencies this run.

**Note on mtime environment:** All committed files in this GitHub Actions checkout have mtime Aug 15 ~08:17 UTC (the repository checkout time), yielding an age of < 1 hour for every on-disk file. Same structural pattern as 2026-08-14: mtime-based scoring shows all deps fresh (< 1h << smallest threshold of 4h for .outputs, 28h for daily articles, 168h for memory/topics, 720h for memory/state). Content vintage is entirely separate from mtime vintage — this is a known characteristic of fresh git checkouts in GitHub Actions.

**Note on `articles/workflow-security-audit-2026-04-11.md`:** Referenced by `skill-security-scan` as its canonical injection-fix example. By filename date, this article is now ~126 days old (well past any threshold). `workflow-security-audit` is disabled (`enabled: false`, Sunday 16:00 UTC schedule) and has not produced a new article since April 2026. Mtime-based scoring shows OK (< 1h, within the 192h weekly-producer threshold). Content vintage is not signalable via mtime in this environment — no action from skill-freshness; if live-divergence is a concern, skill-security-scan should reference current workflow state directly.

**Fingerprint unchanged from prior run (2026-08-14):** The flagged-dependency set is identical to yesterday's (empty; SHA1 of empty = da39a3ee5e6b4b0d3255bfef95601890afd80709). Expected pattern when fleet health is stable and no new stale files have appeared since the prior commit.

## Healthy consumers

- aixbt-pulse — 3 deps (memory/topics/aixbt-grounding.md · aixbt-clusters.md · aixbt-chains.md), all fresh (< 1h)
- skill-security-scan — 2 deps (memory/state/security-scan.json · articles/workflow-security-audit-2026-04-11.md), all fresh (< 1h)
- token-pick — 1 dep (memory/topics/market-context.md), fresh (< 1h)
- market-context-refresh — 1 dep (memory/topics/market-context.md), fresh (< 1h)
- unlock-monitor — 1 dep (memory/state/unlock-monitor-seen.json), fresh (< 1h)
- reg-monitor — 1 dep (memory/topics/reg-monitor-seen.md), fresh (< 1h)
- morning-brief — 0 resolvable deps, all fresh.
- daily-routine — 0 resolvable deps, all fresh.

+ 35 more all-fresh consumers.

## Source status

- `aeon.yml`: ~130 entries parsed, 43 enabled
- Implicit references discovered: 9 (resolvable, specific-file or dated refs; wildcard-glob patterns excluded per step-4 regex)
- Explicit `chains: consume:` edges: 0 (chains: {} — no active chains)
- Files not yet on disk (skipped — implicit references that never existed): 0

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report. In GitHub Actions environments with fresh git checkouts, all committed file mtimes reset to checkout time; mtime-based freshness reflects the checkout epoch, not the file's content vintage. This is a known characteristic of the execution environment.*
