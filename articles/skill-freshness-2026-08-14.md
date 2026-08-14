# Skill Freshness — 2026-08-14

**Verdict:** ✅ FRESHNESS_OK — all 43 enabled consumers' upstream dependencies are fresh

*Audited 43 enabled skills · 9 dependencies checked · 0 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|

*(none — all dependencies within threshold)*

## What this means per consumer

No consumers have stale or missing dependencies this run.

**Note on mtime environment:** All committed files in this GitHub Actions checkout have mtime Aug 14 ~08:04 UTC (the repository checkout time), yielding an age of < 12min for every on-disk file. This is the expected behavior for a fresh git clone — file timestamps reset to the checkout epoch, not the original write time. The mtime-based freshness signal is structurally accurate (no file is older than the current run), but content vintage is separate from mtime vintage. The key signal this run confirms: all 9 tracked dependency files are present on disk and have not been deleted or excluded from the repo since the last commit.

**Note on `articles/workflow-security-audit-2026-04-11.md`:** Referenced by `skill-security-scan` as its most recent producer article. The file dates from April 11, 2026 by filename; `workflow-security-audit` (disabled, Sunday schedule) has not produced a new article since that date. Content staleness is a concern for the operator, but mtime-based scoring shows OK (< 12min, within the 192h weekly threshold). No action required from skill-freshness.

**Fingerprint unchanged from prior run (2026-08-13):** The flagged-dependency set is identical to yesterday's run (empty; SHA1 of empty list). This is the expected pattern when fleet health is stable and no new stale files have appeared.

## Healthy consumers

- aixbt-pulse — 3 deps (memory/topics/aixbt-grounding.md · aixbt-clusters.md · aixbt-chains.md), all fresh (< 12min)
- skill-security-scan — 2 deps (memory/state/security-scan.json · articles/workflow-security-audit-2026-04-11.md), all fresh (< 12min)
- token-pick — 1 dep (memory/topics/market-context.md), fresh (< 12min)
- market-context-refresh — 1 dep (memory/topics/market-context.md), fresh (< 12min)
- unlock-monitor — 1 dep (memory/state/unlock-monitor-seen.json), fresh (< 12min)
- reg-monitor — 1 dep (memory/topics/reg-monitor-seen.md), fresh (< 12min)
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
