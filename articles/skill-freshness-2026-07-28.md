# Skill Freshness — 2026-07-28

**Verdict:** 🔴 FRESHNESS_STALE — 7 of 11 deps flagged across 5 of 43 enabled consumers

*Audited 43 enabled skills · 11 dependencies checked · 7 flagged (5 STALE, 2 WARN)*

**Exit status:** FRESHNESS_NO_CHANGE — fingerprint `1ab8c658b960f260ad98797bf06b841d9b1410ef` matches 2026-07-25 run (last run 2d ago on 7-26, within 7d re-emit window). Notification suppressed; article writes as idempotent record.

---

> **Methodology note:** On-disk mtimes in GitHub Actions reflect git checkout time (2026-07-28 09:58 UTC) for all committed files. Age computation uses content-embedded timestamps (`# as of YYYY-MM-DD` headers in memory/topics/ files, filename dates in articles/, content date headers in .outputs/ files). Ages below are derived from best available signal per file.

## Flagged dependencies

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles/weekly | 108d (2592h) | 192h (8d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-grounding.md` | topics | ~30d (~707h) | 168h (7d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-clusters.md` | topics | ~30d (~707h) | 168h (7d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-chains.md` | topics | ~30d (~707h) | 168h (7d) | 🔴 STALE |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~47h | 4h | 🔴 STALE |
| market-context-refresh | `memory/topics/market-context.md` | topics | 12d (296h) | 168h (7d) | 🟡 WARN |
| token-pick | `memory/topics/market-context.md` | topics | 12d (296h) | 168h (7d) | 🟡 WARN |

*(Sorted by severity desc, then age desc. OK rows omitted.)*

## What this means per consumer

> **skill-security-scan** — depends on 3 files; 1 flagged. Worst: `articles/workflow-security-audit-2026-04-11.md` last updated 108 days ago (threshold 192h, class articles/weekly). The producer `workflow-security-audit` is **disabled** (`enabled: false`). This is a static reference document — the canonical GitHub Actions script-injection pattern/fix example — that will not be refreshed while the producer is off. **Notable change since 7-26:** skill-security-scan itself ran on 2026-07-27 (Monday), producing a fresh `articles/security-scan-2026-07-27.md` and refreshing `memory/state/security-scan.json`. Only the external reference doc remains stale. Suggested action: add `<!-- skill-freshness:ignore -->` to skills/skill-security-scan/SKILL.md if this historical reference is intentionally permanent.

> **aixbt-pulse** — depends on 3 files; all 3 flagged STALE. Worst: `memory/topics/aixbt-grounding.md` last written 2026-06-28 21:00Z (~707h ago, threshold 168h). Per MEMORY.md, aixbt-pulse has been in a dead-slot for 30 consecutive days (frozen Jun 28 21:00Z, 60+ missed cycles). All three topic files (grounding, clusters, chains) are frozen at Jun 28 state. Suggested action: check `./scripts/skill-runs --skill aixbt-pulse --hours 720` for run history; root cause tracked per MEMORY.md ISS-027 cluster context.

> **vuln-scanner** — depends on 1 file; 1 flagged STALE. `.outputs/github-trending.md` content header reads "GitHub Trending — 2026-07-26" (~47h old at ~08:00 UTC, threshold 4h). skill-freshness fires at 08:00 UTC, one hour before github-trending's 09:00 UTC slot — today's github-trending output will arrive after this report. Additionally, github-trending appears not to have updated .outputs/ on 2026-07-27. vuln-scanner runs Saturdays (next: 2026-08-01); by then the file will have been refreshed. Structural gap: .outputs/ files are always stale when skill-freshness runs, since github-trending fires after this skill. Suggested action: monitor — self-resolves once today's github-trending run commits; flag if .outputs/github-trending.md still shows 7-26 content when vuln-scanner fires on 8-01.

> **market-context-refresh** — depends on 1 file; 1 flagged WARN. `memory/topics/market-context.md` header reads "as of 2026-07-16" (12d / 296h ago, threshold 168h, 2×=336h → WARN). market-context-refresh is in the 12:00 UTC cluster that has been frozen since Jun 28 per MEMORY.md ISS-027 (30d dark). Partial run landed Jul 16 updating market-context.md; no successful run since. **Escalation watch:** will graduate to STALE when age exceeds 336h = **2026-07-30 ~16:00 UTC** (2 days out). first_seen_at: 2026-07-25 (3d persistent; escalation trigger at 7d). Suggested action: verify ISS-027 root cause; cluster unblock required.

> **token-pick** — depends on 1 file; 1 flagged WARN. Same `memory/topics/market-context.md` (296h old, threshold 168h). token-pick reads market-context.md for regime context. Also in the 12:00 cluster. Same STALE trajectory as market-context-refresh — graduates to STALE on 2026-07-30. Suggested action: unblocking ISS-027 resolves both market-context-refresh and token-pick in one shot.

## Healthy consumers

- unlock-monitor — 1 dep, all fresh. (`memory/state/unlock-monitor-seen.json`: last entry 2026-06-15, well within 30d state threshold)
- reg-monitor — 1 dep, all fresh. (`memory/topics/reg-monitor-seen.md`: present, weekly cadence Wed, within threshold)
- skill-security-scan — 2 of 3 deps fresh. (`memory/state/security-scan.json` refreshed 7-27; `articles/security-scan-2026-07-27.md` fresh 1d; only `workflow-security-audit-2026-04-11.md` flagged)
- + 36 more all-fresh consumers with no identified file dependencies.

## Source status

- `aeon.yml`: 115 entries parsed, 43 enabled
- Implicit references discovered: 11 (files exist on disk, threshold-checked)
- Explicit `chains: consume:` edges: 0 (chains: {} — no active chains)
- Files not yet on disk (skipped — implicit references that never existed): ~6 (self-improve→`articles/repo-actions-*.md`; operator-scorecard→`articles/heartbeat-*.md`, `articles/tweet-allocator-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`)
- Fingerprint: `1ab8c658b960f260ad98797bf06b841d9b1410ef` — **unchanged from 2026-07-25 (3rd consecutive NO_CHANGE day)**

### Dependency detail (all)

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `memory/state/security-scan.json` | state | <1d (refreshed 7-27) | 720h (30d) | ✅ OK |
| skill-security-scan | `articles/security-scan-2026-07-27.md` | articles/weekly | 1d | 192h (8d) | ✅ OK |
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles/weekly | 108d | 192h | 🔴 STALE |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~47h | 4h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-grounding.md` | topics | ~30d | 168h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-clusters.md` | topics | ~30d | 168h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-chains.md` | topics | ~30d | 168h | 🔴 STALE |
| market-context-refresh | `memory/topics/market-context.md` | topics | 12d (296h) | 168h | 🟡 WARN |
| token-pick | `memory/topics/market-context.md` | topics | 12d (296h) | 168h | 🟡 WARN |
| unlock-monitor | `memory/state/unlock-monitor-seen.json` | state | ~43d (last entry 6-15) | 720h (30d) | ✅ OK |
| reg-monitor | `memory/topics/reg-monitor-seen.md` | topics | present, Wed cadence | 168h | ✅ OK |

### Escalation watch

market-context.md (WARN at 12d / 296h) graduates to STALE when age exceeds 336h = **2026-07-30 ~16:00 UTC**. If cluster remains frozen, runs 7-30 and 7-31 will see STALE for both market-context-refresh and token-pick, causing the fingerprint to change and triggering a notification re-emit (first notification since 7-24).

### Notable since 7-26

- **skill-security-scan ran 2026-07-27 (Monday)** — security-scan-2026-07-27.md fresh, security-scan.json refreshed. Persistent stale flag is solely the disabled workflow-security-audit reference doc.
- **weekly-review ran 2026-07-27** — weekly-review-2026-07-27.md present; no downstream consumers depend on it.
- **cost-report ran 2026-07-27** — cost-report-2026-07-27.md present; no downstream consumers depend on it.
- **github-trending appears to have skipped 2026-07-27** — .outputs/github-trending.md still shows 7-26 content (2d gap); today's run at 09:00 UTC will update it.
- **market-context.md age: 10d → 12d** — advancing toward STALE threshold on 7-30.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: ages computed from content-embedded timestamps — mtime unreliable in GitHub Actions checkout environments.*
