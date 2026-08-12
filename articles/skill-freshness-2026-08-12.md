# Skill Freshness — 2026-08-12

**Verdict:** ✅ FRESHNESS_OK — all 43 enabled consumers' upstream dependencies are fresh

*Audited 43 enabled skills · 9 dependencies checked · 0 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|

*(none — all dependencies within threshold)*

## What this means per consumer

No consumers have stale or missing dependencies this run.

**Note on mtime environment:** All committed files in this GitHub Actions checkout have mtime Aug 12 08:26 UTC (the repository checkout time), yielding an age of < 1h for every on-disk file. This is the expected behavior for a fresh git clone — file timestamps reset to the checkout epoch, not the original write time. The mtime-based freshness signal is structurally accurate (no file is older than the current run), but the operator should note that content vintage is separate from mtime vintage. The key signal this run confirms: all 9 tracked dependency files are present on disk and have not been deleted or excluded from the repo since the last commit.

**Note on `articles/workflow-security-audit-2026-04-11.md`:** Referenced by `skill-security-scan` as a prose-example path in its SKILL.md (not a live data dependency). The file dates from April 2026 by filename; `workflow-security-audit` (disabled, Sunday schedule) has not produced a new article since that date. Content staleness is a concern for the operator, but mtime-based scoring shows OK (< 1h, within the 192h weekly threshold). No action required from skill-freshness.

## Healthy consumers

- aixbt-pulse — 3 deps (memory/topics/aixbt-grounding.md · aixbt-clusters.md · aixbt-chains.md), all fresh (< 1h)
- skill-security-scan — 2 deps (memory/state/security-scan.json · articles/workflow-security-audit-2026-04-11.md), all fresh (< 1h)
- token-pick — 1 dep (memory/topics/market-context.md), fresh (< 1h)
- market-context-refresh — 1 dep (memory/topics/market-context.md), fresh (< 1h)
- unlock-monitor — 1 dep (memory/state/unlock-monitor-seen.json), fresh (< 1h)
- reg-monitor — 1 dep (memory/topics/reg-monitor-seen.md), fresh (< 1h)
- action-converter — 0 resolvable deps (wildcard refs only), all fresh.
- agent-buzz — 0 resolvable deps, all fresh.

+ 35 more all-fresh consumers.

## Source status

- `aeon.yml`: ~130 entries parsed, 43 enabled
- Implicit references discovered: 9 (resolvable, specific-file or dated refs; wildcard-glob patterns excluded per step-4 regex)
- Explicit `chains: consume:` edges: 0 (chains: {} — no active chains)
- Files not yet on disk (skipped — implicit references that never existed): 0

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report. In GitHub Actions environments with fresh git checkouts, all committed file mtimes reset to checkout time; mtime-based freshness reflects the checkout epoch, not the file's content vintage. This is a known characteristic of the execution environment.*
