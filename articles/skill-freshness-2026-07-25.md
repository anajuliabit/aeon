# Skill Freshness — 2026-07-25

**Verdict:** 🔴 FRESHNESS_STALE — 7 of 11 deps flagged across 5 of 43 enabled consumers

*Audited 43 enabled skills · 11 dependencies checked · 7 flagged (5 STALE, 2 WARN)*

---

> **Methodology note:** On-disk mtimes in GitHub Actions reflect git checkout time (2026-07-25 08:52 UTC) for all committed files, making mtime-based age computation unreliable for historical staleness detection. This run uses content-embedded timestamps (`# as of YYYY-MM-DD` headers in memory/topics/ files, filename dates in articles/) as the authoritative age proxy. Files written during this Actions run would carry real mtimes; committed files use content dating. Ages below are derived from the best available signal per file.

## Flagged dependencies

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles/weekly | 105d (2520h) | 192h (8d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-grounding.md` | topics | 26.5d (636h) | 168h (7d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-clusters.md` | topics | 26.5d (636h) | 168h (7d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-chains.md` | topics | 26.5d (636h) | 168h (7d) | 🔴 STALE |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~24h | 4h | 🔴 STALE |
| market-context-refresh | `memory/topics/market-context.md` | topics | 9d (216h) | 168h (7d) | 🟡 WARN |
| token-pick | `memory/topics/market-context.md` | topics | 9d (216h) | 168h (7d) | 🟡 WARN |

*(Sorted by severity desc, then age desc. OK rows omitted.)*

## What this means per consumer

> **skill-security-scan** — depends on 3 files; 1 flagged. Worst: `articles/workflow-security-audit-2026-04-11.md` last updated 105 days ago (threshold 192h, class articles/weekly). The producer `workflow-security-audit` is **disabled** (`enabled: false`). This is a static reference document (canonical GitHub Actions script-injection pattern/fix example) that will never be refreshed while the producer is off. Suggested action: add `<!-- skill-freshness:ignore -->` to skills/skill-security-scan/SKILL.md lines 19 and 132 if this historical reference is intentionally permanent.

> **aixbt-pulse** — depends on 3 files; all 3 flagged STALE. Worst: `memory/topics/aixbt-grounding.md` last written 2026-06-28 21:00Z (636h ago, threshold 168h). Per MEMORY.md, aixbt-pulse has been in a dead-slot for 27 consecutive days (frozen Jun 28 21:00Z, 54 missed cycles). All three topic files (grounding, clusters, chains) are frozen at Jun 28 state. Suggested action: check `./scripts/skill-runs --skill aixbt-pulse --hours 672` for run history; verify root cause per MEMORY.md ISS-027 cluster context.

> **vuln-scanner** — depends on 1 file; 1 flagged STALE. `.outputs/github-trending.md` content shows "2026-07-24" (written ~24h ago, threshold 4h, 2× = 8h). github-trending writes this file on its daily 09:00 UTC run. Current time is 08:53 UTC — github-trending fires in ~7 minutes and will refresh the file. By the time vuln-scanner runs at 16:00 UTC the file will be ~7h old, still past the 4h threshold but within an expected operational window. Self-resolves today. Suggested action: monitor — no manual intervention needed.

> **market-context-refresh** — depends on 1 file; 1 flagged WARN. `memory/topics/market-context.md` header reads "as of 2026-07-16" (9 days ago, 216h, threshold 168h). market-context-refresh is in the 12:00 UTC cluster that has been dark per MEMORY.md (8-skill cluster frozen ~Jun 28; the .outputs/market-context-refresh.md shows Jun 28 state, but the actual market-context.md was last written Jul 16 — suggesting a partial run landed). Suggested action: verify market-context-refresh is still on schedule; file will clear on next successful run.

> **token-pick** — depends on 1 file; 1 flagged WARN. Same `memory/topics/market-context.md` dependency (216h old, threshold 168h). token-pick reads market-context.md for regime context at each run. Also in the 12:00 cluster dark per MEMORY.md. Suggested action: same as market-context-refresh — clears on next successful market-context-refresh run.

## Healthy consumers

- unlock-monitor — 1 dep, all fresh. (`memory/state/unlock-monitor-seen.json`: entries through Jul 25, threshold 30d)
- reg-monitor — 1 dep, all fresh. (`memory/topics/reg-monitor-seen.md`: file present, weekly cadence Wed, age indeterminate but not flagged)
- + 36 more all-fresh consumers with no identified file dependencies.

## Source status

- `aeon.yml`: 115 entries parsed, 43 enabled
- Implicit references discovered: 11 (files exist on disk, threshold-checked)
- Explicit `chains: consume:` edges: 0 (chains: {} — no active chains)
- Files not yet on disk (skipped — implicit references that never existed): ~6 (self-improve→`articles/repo-actions-*.md`; operator-scorecard→`articles/heartbeat-*.md`, `articles/tweet-allocator-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`)
- New flags this run: 7 (first detection — prior runs used on-disk mtime which equals checkout time, masking all real staleness)

### Dependency detail (all)

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `memory/state/security-scan.json` | state | 5d (Jul 20) | 720h (30d) | ✅ OK |
| skill-security-scan | `articles/security-scan-2026-07-20.md` | articles/weekly | 5d | 192h (8d) | ✅ OK |
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles/weekly | 105d | 192h | 🔴 STALE |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~24h | 4h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-grounding.md` | topics | 26.5d | 168h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-clusters.md` | topics | 26.5d | 168h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-chains.md` | topics | 26.5d | 168h | 🔴 STALE |
| market-context-refresh | `memory/topics/market-context.md` | topics | 9d | 168h | 🟡 WARN |
| token-pick | `memory/topics/market-context.md` | topics | 9d | 168h | 🟡 WARN |
| unlock-monitor | `memory/state/unlock-monitor-seen.json` | state | < 1h | 720h | ✅ OK |
| reg-monitor | `memory/topics/reg-monitor-seen.md` | topics | unknown | 168h | ✅ OK |

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: ages computed from content-embedded timestamps (file headers, filename dates) — mtime unreliable in GitHub Actions checkout environments. First run to report non-OK: prior runs (through 2026-07-24) used mtime and reported FRESHNESS_OK due to checkout-time masking.*
