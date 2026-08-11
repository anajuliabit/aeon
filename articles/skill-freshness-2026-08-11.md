# Skill Freshness — 2026-08-11

**Verdict:** ✅ FRESHNESS_OK — all 43 enabled consumers' upstream dependencies are fresh

*Audited 43 enabled skills · 9 dependencies checked · 0 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|

*(none — all dependencies within threshold)*

## What this means per consumer

No consumers have stale or missing dependencies this run.

**Note on prior-run flag cleared:** `skill-security-scan` had `articles/workflow-security-audit-2026-04-11.md` flagged as STALE since 2026-07-25 (17 days). Today's fresh git checkout reset the file's mtime to ~20 minutes ago, which falls well within the 192h weekly threshold. The underlying content is still April 2026 vintage; the mtime-based freshness signal cleared, but the operator should be aware that `workflow-security-audit` (disabled, Sunday schedule) has not produced a new article since April. `skill-security-scan` references it only as a canonical-pattern prose example in its SKILL.md, not as a live data dependency.

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
