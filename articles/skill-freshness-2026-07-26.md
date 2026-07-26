# Skill Freshness — 2026-07-26

**Verdict:** 🔴 FRESHNESS_STALE — 7 of 11 deps flagged across 5 of 43 enabled consumers

*Audited 43 enabled skills · 11 dependencies checked · 7 flagged (5 STALE, 2 WARN)*

**Exit status:** FRESHNESS_NO_CHANGE — fingerprint `1ab8c658b960f260ad98797bf06b841d9b1410ef` matches 2026-07-25 run (last run 1d ago, within 7d re-emit window). Notification suppressed; article writes as idempotent record.

---

> **Methodology note:** On-disk mtimes in GitHub Actions reflect git checkout time (2026-07-26 09:35 UTC) for all committed files. Age computation uses content-embedded timestamps (`# as of YYYY-MM-DD` headers in memory/topics/ files, filename dates in articles/). Ages below are derived from best available signal per file.

## Flagged dependencies

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles/weekly | 106d (2544h) | 192h (8d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-grounding.md` | topics | 28d (672h) | 168h (7d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-clusters.md` | topics | 28d (672h) | 168h (7d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-chains.md` | topics | 28d (672h) | 168h (7d) | 🔴 STALE |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~24.6h | 4h | 🔴 STALE |
| market-context-refresh | `memory/topics/market-context.md` | topics | 10d (240h) | 168h (7d) | 🟡 WARN |
| token-pick | `memory/topics/market-context.md` | topics | 10d (240h) | 168h (7d) | 🟡 WARN |

*(Sorted by severity desc, then age desc. OK rows omitted.)*

## What this means per consumer

> **skill-security-scan** — depends on 3 files; 1 flagged. Worst: `articles/workflow-security-audit-2026-04-11.md` last updated 106 days ago (threshold 192h, class articles/weekly). The producer `workflow-security-audit` is **disabled** (`enabled: false`). This is a static reference document — a canonical GitHub Actions script-injection pattern/fix example — that will never be refreshed while the producer is off. Suggested action: add `<!-- skill-freshness:ignore -->` to skills/skill-security-scan/SKILL.md if this historical reference is intentionally permanent.

> **aixbt-pulse** — depends on 3 files; all 3 flagged STALE. Worst: `memory/topics/aixbt-grounding.md` last written 2026-06-28 21:00Z (672h ago, threshold 168h). Per MEMORY.md, aixbt-pulse has been in a dead-slot for 28 consecutive days (frozen Jun 28 21:00Z, 56 missed cycles). All three topic files (grounding, clusters, chains) are frozen at Jun 28 state. Suggested action: check `./scripts/skill-runs --skill aixbt-pulse --hours 672` for run history; root cause tracked per MEMORY.md ISS-027 cluster context.

> **vuln-scanner** — depends on 1 file; 1 flagged STALE. `.outputs/github-trending.md` content reads "GitHub Trending — 2026-07-25" (~24.6h old at 09:36 UTC, threshold 4h). github-trending fires daily at 09:00 UTC and likely ran ~36 minutes ago — output will be committed in a separate workflow run. vuln-scanner runs at 16:00 UTC; by then the refreshed file will be ~7h old (still past 4h threshold but within timing window). Self-resolves once today's github-trending commit lands. Suggested action: monitor — chronic structural gap unless .outputs/ files are committed between workflow runs.

> **market-context-refresh** — depends on 1 file; 1 flagged WARN. `memory/topics/market-context.md` header reads "as of 2026-07-16" (10d / 240h ago, threshold 168h, 2×=336h → WARN). market-context-refresh is in the 12:00 UTC cluster that has been frozen since Jun 28 per MEMORY.md ISS-027 (28d dark). Partial run landed Jul 16 updating market-context.md; no successful run since. Will graduate to STALE on 2026-07-30 (when 240h → 336h crosses). Suggested action: verify ISS-027 root cause; cluster unblock required.

> **token-pick** — depends on 1 file; 1 flagged WARN. Same `memory/topics/market-context.md` (240h old, threshold 168h). token-pick reads market-context.md for regime context. Also in the 12:00 cluster. Same trajectory as market-context-refresh — graduates to STALE on 2026-07-30. Suggested action: unblocking ISS-027 resolves both market-context-refresh and token-pick in one shot.

## Healthy consumers

- unlock-monitor — 1 dep, all fresh. (`memory/state/unlock-monitor-seen.json`: entries through Jul 25, threshold 30d)
- reg-monitor — 1 dep, all fresh. (`memory/topics/reg-monitor-seen.md`: present, weekly cadence Wed, within threshold)
- + 36 more all-fresh consumers with no identified file dependencies.

## Source status

- `aeon.yml`: 115 entries parsed, 43 enabled
- Implicit references discovered: 11 (files exist on disk, threshold-checked)
- Explicit `chains: consume:` edges: 0 (chains: {} — no active chains)
- Files not yet on disk (skipped — implicit references that never existed): ~6 (self-improve→`articles/repo-actions-*.md`; operator-scorecard→`articles/heartbeat-*.md`, `articles/tweet-allocator-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`)
- Fingerprint: `1ab8c658b960f260ad98797bf06b841d9b1410ef` — **unchanged from 2026-07-25**

### Dependency detail (all)

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `memory/state/security-scan.json` | state | 6d (Jul 20) | 720h (30d) | ✅ OK |
| skill-security-scan | `articles/security-scan-2026-07-20.md` | articles/weekly | 6d | 192h (8d) | ✅ OK |
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles/weekly | 106d | 192h | 🔴 STALE |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~24.6h | 4h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-grounding.md` | topics | 28d | 168h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-clusters.md` | topics | 28d | 168h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-chains.md` | topics | 28d | 168h | 🔴 STALE |
| market-context-refresh | `memory/topics/market-context.md` | topics | 10d | 168h | 🟡 WARN |
| token-pick | `memory/topics/market-context.md` | topics | 10d | 168h | 🟡 WARN |
| unlock-monitor | `memory/state/unlock-monitor-seen.json` | state | < 1h | 720h | ✅ OK |
| reg-monitor | `memory/topics/reg-monitor-seen.md` | topics | unknown | 168h | ✅ OK |

### Escalation watch

market-context.md (WARN at 10d / 240h) graduates to STALE when age exceeds 336h = **2026-07-30 ~16:00 UTC**. If cluster remains frozen, next week's runs will escalate this from WARN → STALE for both market-context-refresh and token-pick, and the fingerprint will change, triggering a notification re-emit.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: ages computed from content-embedded timestamps — mtime unreliable in GitHub Actions checkout environments.*
