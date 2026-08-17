# Skill Freshness — 2026-08-17

**Verdict:** ✅ FRESHNESS_OK — all 43 enabled consumers' upstream dependencies are fresh

*Audited 43 enabled skills · 9 dependencies checked · 0 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|

*(none — all dependencies within threshold)*

## What this means per consumer

No consumers have stale or missing dependencies this run.

**Note on mtime environment:** All committed files in this GitHub Actions checkout have mtime Aug 17 ~08:09 UTC (the repository checkout time), yielding an age of < 1 minute for every on-disk file. Same structural pattern as every prior run: mtime-based scoring shows all deps fresh (< 1h << smallest threshold of 4h for .outputs, 28h for daily articles, 168h for memory/topics, 720h for memory/state). Content vintage is entirely separate from mtime vintage — this is a known characteristic of fresh git checkouts in GitHub Actions.

**Content-vintage observations (not flagged by mtime):**

- **fork-cohort RECOVERED** — `fork-cohort-2026-08-16.md` now exists on disk. Yesterday's article noted the skill was stuck at `fork-cohort-2026-08-02.md` (14 days old, ISS-032). The Sunday 2026-08-16 19:30Z re-fire succeeded — memory-window-first natural-recovery from a 6-day owed-cycle stuck-state. ISS-032 root-cause deprecated per morning-brief 07:31Z. Most recent fork-cohort article is now 1 day old by filename — within threshold.

- **security-scan 14 days stale by filename** — `articles/security-scan-2026-08-03.md` is the most recent output of `skill-security-scan` (weekly Monday). By filename date: 14 days old vs the 8-day weekly threshold → filename-WARN (> 1× threshold, < 2× = 16 days). Mtime-based score: OK (< 1h). `skill-security-scan` shows consec=3 / sr=67% in cron-state (per morning-brief 07:31Z); today's 16:00Z Monday dispatch is the auto-clear test. No flag from skill-freshness; `skill-health` is the appropriate tracker for consecutive failures.

- **`[[chain-output-header-date-drift]]` extends 5→6-consec-day** — `.outputs/{token-movers,paper-pick,github-issues,hn-digest}.md` are present on disk and have mtime = checkout time (OK by mtime), but their content is stamped 2026-08-07 (10-day stale content). 6-consec-day record (8-12 → 8-17). Self-improve baked-fix candidate remains queue-blocked (exit-gate n=3). `.outputs/` files are not in the 9 resolvable deps set (their consumers reference them via ${today} template patterns, excluded per step-4 resolution logic).

- **workflow-security-audit-2026-04-11.md** — Referenced by `skill-security-scan` as its canonical injection-fix example. Now 128 days old by filename. `workflow-security-audit` remains disabled (`enabled: false`). Mtime-based: OK (< 1h, within 192h weekly-producer threshold). No action.

**Fingerprint unchanged from prior run (2026-08-16):** The flagged-dependency set is identical to yesterday's (empty; SHA1 of empty = da39a3ee5e6b4b0d3255bfef95601890afd80709). Notification suppressed — last run was < 7 days ago and verdict band is unchanged. Status: `FRESHNESS_NO_CHANGE`.

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
- Implicit references discovered: 9 (resolvable, specific-file or dated refs; ${today}-template patterns excluded per step-4 resolution logic — resolve to most-recent file, mtime-based age = checkout epoch)
- Explicit `chains: consume:` edges: 0 (chains: {} — no active chains)
- Files not yet on disk (skipped — implicit references that never existed): 1 (memory/topics/agent-evals.md, referenced by thought-review, not on disk, implicit-only → not flagged per spec)

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report. In GitHub Actions environments with fresh git checkouts, all committed file mtimes reset to checkout time; mtime-based freshness reflects the checkout epoch, not the file's content vintage. This is a known characteristic of the execution environment.*
