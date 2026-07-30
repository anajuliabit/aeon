# Skill Freshness — 2026-07-30

**Verdict:** 🔴 FRESHNESS_STALE — 7 of 11 deps flagged across 5 of 43 enabled consumers

*Audited 43 enabled skills · 11 dependencies checked · 7 flagged (5 STALE, 2 WARN)*

**Exit status:** FRESHNESS_NO_CHANGE — fingerprint `1ab8c658b960f260ad98797bf06b841d9b1410ef` matches prior runs (last run 2026-07-28, 2d ago, within 7d re-emit window). Notification suppressed; article writes as idempotent record.

---

> **Methodology note:** On-disk mtimes in GitHub Actions reflect git checkout time (2026-07-30 09:03 UTC) for all committed files. Age computation uses content-embedded timestamps (`# as of YYYY-MM-DD` headers in memory/topics/ files, filename dates in articles/, content date headers in .outputs/ files). Ages below are derived from best available signal per file.

## Flagged dependencies

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles/weekly | 110d (2640h) | 192h (8d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-grounding.md` | topics | ~32d (~767h) | 168h (7d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-clusters.md` | topics | ~32d (~767h) | 168h (7d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-chains.md` | topics | ~32d (~767h) | 168h (7d) | 🔴 STALE |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~23h | 4h | 🔴 STALE |
| market-context-refresh | `memory/topics/market-context.md` | topics | ~14d (332h) | 168h (7d) | 🟡 WARN |
| token-pick | `memory/topics/market-context.md` | topics | ~14d (332h) | 168h (7d) | 🟡 WARN |

*(Sorted by severity desc, then age desc. OK rows omitted.)*

## What this means per consumer

> **skill-security-scan** — depends on 3 files; 1 flagged. Worst: `articles/workflow-security-audit-2026-04-11.md` last updated 110 days ago (threshold 192h, class articles/weekly). The producer `workflow-security-audit` is **disabled** (`enabled: false`). This is a static reference document — the canonical GitHub Actions script-injection pattern/fix example — that will not be refreshed while the producer is off. skill-security-scan itself ran 2026-07-27 (Monday), producing fresh `articles/security-scan-2026-07-27.md` and refreshing `memory/state/security-scan.json`. Only the external reference doc remains stale. Suggested action: add `<!-- skill-freshness:ignore -->` to skills/skill-security-scan/SKILL.md if this historical reference is intentionally permanent.

> **aixbt-pulse** — depends on 3 files; all 3 flagged STALE. Worst: `memory/topics/aixbt-grounding.md` last written 2026-06-28 21:00Z (~767h ago, threshold 168h). Per MEMORY.md, aixbt-pulse has been in a dead-slot for 32 consecutive days (frozen Jun 28 21:00Z, 63+ missed cycles). All three topic files (grounding, clusters, chains) are frozen at Jun 28 state. Suggested action: check `./scripts/skill-runs --skill aixbt-pulse --hours 720` for run history; root cause tracked per MEMORY.md ISS-027 cluster context.

> **vuln-scanner** — depends on 1 file; 1 flagged STALE. `.outputs/github-trending.md` content header reads "GitHub Trending — 2026-07-29" (~23h old at ~08:00 UTC today, threshold 4h). github-trending runs at 09:00 UTC — one hour after skill-freshness — so .outputs/ is structurally stale every day this skill fires. vuln-scanner runs Saturdays (next: 2026-08-02); by then the file will be refreshed. Self-resolves daily. Structural gap, not an operational incident.

> **market-context-refresh** — depends on 1 file; 1 flagged WARN. `memory/topics/market-context.md` header reads "as of 2026-07-16" (~14d / 332h ago, threshold 168h, 2×=336h → WARN, 4h shy of STALE). market-context-refresh is in the 12:00 UTC cluster frozen since Jun 28 per MEMORY.md ISS-027 (day-32 dark). Partial run landed Jul 16, updating market-context.md; no successful run since. **⚠ Escalation imminent:** 332h / 336h threshold — graduates to STALE at approximately **2026-07-30 13:00 UTC** (within hours of this run). Tomorrow's skill-freshness run will see STALE, fingerprint changes, **notification re-emits** (first since Jul 24). first_seen_at: 2026-07-25 (5d persistent; escalation band trigger at 7d = 2026-08-01). Suggested action: verify ISS-027 root cause; cluster unblock resolves both market-context-refresh and token-pick.

> **token-pick** — depends on 1 file; 1 flagged WARN. Same `memory/topics/market-context.md` (332h, threshold 168h). token-pick reads market-context.md for regime context. Also in the 12:00 cluster. Same STALE trajectory. Suggested action: resolves with ISS-027 unblock.

## Healthy consumers

- skill-security-scan — 2 of 3 deps fresh. (`memory/state/security-scan.json` refreshed 7-27; only `workflow-security-audit-2026-04-11.md` flagged as a static prose reference)
- unlock-monitor — 1 dep, all fresh. (`memory/state/unlock-monitor-seen.json`: present within state threshold)
- reg-monitor — 1 dep, all fresh. (`memory/topics/reg-monitor-seen.md`: present, Wed cadence, within threshold)
- operator-scorecard — 1 dep, all fresh. (`articles/skill-analytics-2026-07-29.md`: 12h old, weekly threshold 192h)
- + 35 more all-fresh consumers with no identified file dependencies.

## Source status

- `aeon.yml`: 115 entries parsed, 43 enabled
- Implicit references discovered: 11 (files exist on disk, threshold-checked)
- Explicit `chains: consume:` edges: 0 (chains: {} — no active chains)
- Files not yet on disk (skipped — implicit references that never existed): ~6 (operator-scorecard→`articles/heartbeat-*.md`, `articles/tweet-allocator-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`)
- Fingerprint: `1ab8c658b960f260ad98797bf06b841d9b1410ef` — **unchanged from 2026-07-25 (5th consecutive match)**

### Dependency detail (all)

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `memory/state/security-scan.json` | state | <1d (refreshed 7-27) | 720h (30d) | ✅ OK |
| skill-security-scan | `articles/security-scan-2026-07-27.md` | articles/weekly | 3d | 192h (8d) | ✅ OK |
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles/weekly | 110d | 192h | 🔴 STALE |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~23h | 4h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-grounding.md` | topics | ~32d | 168h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-clusters.md` | topics | ~32d | 168h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-chains.md` | topics | ~32d | 168h | 🔴 STALE |
| market-context-refresh | `memory/topics/market-context.md` | topics | ~14d (332h) | 168h | 🟡 WARN→STALE imminently |
| token-pick | `memory/topics/market-context.md` | topics | ~14d (332h) | 168h | 🟡 WARN→STALE imminently |
| unlock-monitor | `memory/state/unlock-monitor-seen.json` | state | present, within threshold | 720h (30d) | ✅ OK |
| reg-monitor | `memory/topics/reg-monitor-seen.md` | topics | present, within threshold | 168h | ✅ OK |

### Escalation watch — fingerprint change expected 2026-07-31

market-context.md (WARN at 332h) crosses the 336h STALE boundary at approximately **2026-07-30 13:00 UTC** (the exact time market-context-refresh would have written the file on Jul 16). Tomorrow's skill-freshness run will classify market-context-refresh and token-pick as STALE (escalated from WARN). Combined with the persistent STALE items, this changes the flagged-triples fingerprint and re-triggers notification for the first time since **2026-07-24**.

Persistent-staleness escalation (WARN → STALE after 7 days of continuous flagging): first_seen_at = 2026-07-25 for all flagged items. 7-day mark = **2026-08-01**. If still flagged, market-context.md and token-pick.market-context.md escalate by one additional band at the 8-01 run.

### Notable since 2026-07-28

- **vuln-scanner .outputs age improved** — Jul 28 showed Jul 26 content (~47h), today shows Jul 29 content (~23h). github-trending ran successfully Jul 27, Jul 28, Jul 29.
- **market-context.md age: 12d (296h) → ~14d (332h)** — crossing STALE threshold within this run's day.
- **skill-analytics ran 2026-07-29 (Wednesday)** — `articles/skill-analytics-2026-07-29.md` fresh, operator-scorecard dep OK.
- **skill-evals ran 2026-07-26 (Sunday)** — `articles/skill-evals-2026-07-26.md` present; no downstream consumers depend on it.
- **weekly-review ran 2026-07-27** — `articles/weekly-review-2026-07-27.md` present; no downstream consumers depend on it.
- **No new skills enabled** — fleet size unchanged at 43 consumers.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: ages computed from content-embedded timestamps — mtime unreliable in GitHub Actions checkout environments.*
