# Skill Freshness — 2026-08-01

**Verdict:** 🔴 FRESHNESS_STALE — 7 of 11 deps flagged across 5 of 43 enabled consumers

*Audited 43 enabled skills · 11 dependencies checked · 7 flagged (7 STALE, 0 WARN)*

**Exit status:** FRESHNESS_STALE — fingerprint `f789cd3bca626257444b895c8b1636402081e86e` differs from prior `1ab8c658b960f260ad98797bf06b841d9b1410ef` (last run 2026-07-30, 2d ago). Two items escalated from WARN → STALE (market-context-refresh + token-pick crossing 2× age threshold). Notification sent — first since 2026-07-25.

---

> **Methodology note:** On-disk mtimes in GitHub Actions reflect git checkout time (2026-08-01 08:36 UTC) for all committed files. Age computation uses content-embedded timestamps (`# as of YYYY-MM-DD` headers in memory/topics/ files, filename dates in articles/, content date headers in .outputs/ files). Ages below are derived from best available signal per file.

## Flagged dependencies

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles/weekly | 112d (2688h) | 192h (8d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-grounding.md` | topics | ~34d (~816h) | 168h (7d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-clusters.md` | topics | ~34d (~816h) | 168h (7d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-chains.md` | topics | ~34d (~816h) | 168h (7d) | 🔴 STALE |
| market-context-refresh | `memory/topics/market-context.md` | topics | ~16d (~380h) | 168h (7d) | 🔴 STALE ← escalated |
| token-pick | `memory/topics/market-context.md` | topics | ~16d (~380h) | 168h (7d) | 🔴 STALE ← escalated |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~23h | 4h | 🔴 STALE |

*(Sorted by severity desc, then age desc. OK rows omitted.)*

## What this means per consumer

> **skill-security-scan** — depends on 3 files; 1 flagged. Worst: `articles/workflow-security-audit-2026-04-11.md` last updated 112 days ago (threshold 192h, class articles/weekly). The producer `workflow-security-audit` is **disabled** (`enabled: false`). This is a static reference document — the canonical GitHub Actions script-injection pattern/fix example — that will not refresh while the producer is off. skill-security-scan itself ran 2026-07-28 (Monday), producing `articles/security-scan-2026-07-27.md` and refreshing `memory/state/security-scan.json`. Only the external reference doc remains stale. Suggested action: add `<!-- skill-freshness:ignore -->` to skills/skill-security-scan/SKILL.md if this historical reference is intentionally permanent, or re-enable workflow-security-audit.

> **aixbt-pulse** — depends on 3 files; all 3 flagged STALE. Worst: `memory/topics/aixbt-grounding.md` last written ~2026-06-28 21:00Z (~816h ago, threshold 168h). Per MEMORY.md, aixbt-pulse has been in a dead-slot for 34 consecutive days (frozen Jun 28 21:00Z, 65+ missed cycles). All three topic files (grounding, clusters, chains) are frozen at Jun 28 state. **Persistence note:** first_seen_at = 2026-07-25; 7-day escalation band triggers 2026-08-02. Suggested action: check `./scripts/skill-runs --skill aixbt-pulse --hours 720`; root cause in ISS-027 cluster context.

> **vuln-scanner** — depends on 1 file; 1 flagged STALE. `.outputs/github-trending.md` content header reads "GitHub Trending — 2026-07-31" (~23h old at 08:00 UTC today, threshold 4h). github-trending runs at 09:00 UTC — one hour after skill-freshness — so .outputs/ is structurally stale every day this skill fires. vuln-scanner runs Saturdays (next: 2026-08-02); by then the file will be refreshed. Self-resolves daily. Structural gap, not an operational incident.

> **market-context-refresh** — depends on 1 file; 1 flagged STALE (escalated from WARN). `memory/topics/market-context.md` last meaningfully updated ~2026-07-16 (~16d / 380h ago, threshold 168h, 2×=336h → now STALE). `.outputs/market-context-refresh.md` shows the skill IS running but falling back to 2026-06-28 cached data (fallback path active — primary fetch failing). Crosses 2× threshold today, upgrading from the WARN carried since 7-25. Part of ISS-027 12:00 cluster — partial run landed Jul 16, no successful fresh-data write since. **Persistent-staleness escalation fires 2026-08-02** (first_seen_at 7-25; 8-day mark). Suggested action: investigate why market-context-refresh falls back to Jun 28 data; ISS-027 cluster unblock resolves.

> **token-pick** — depends on 1 file; 1 flagged STALE (escalated from WARN). Same `memory/topics/market-context.md` (380h). Token picks are being made against 16d+ stale market context — regime, BTC price, and F&G shown are Jun 28 vintage. Also ISS-027 cluster. Suggested action: resolves with market-context-refresh fix.

## Healthy consumers

- skill-security-scan — 2 of 3 deps fresh. (`memory/state/security-scan.json` refreshed 7-27; `articles/security-scan-2026-07-27.md` fresh at 5d, weekly threshold 8d)
- unlock-monitor — 1 dep, all fresh. (`memory/state/unlock-monitor-seen.json`: within 30d state threshold)
- reg-monitor — 1 dep, all fresh. (`memory/topics/reg-monitor-seen.md`: last updated 7-29 Wed, 3d, within 7d threshold)
- morning-brief — no identified file deps beyond MEMORY.md context read (within expected cadence).
- daily-routine — no identified file deps beyond live API calls.
- github-trending — no identified upstream file deps; writes to .outputs/.
- narrative-tracker — no identified upstream file deps beyond live API calls.
- + 33 more all-fresh consumers with no identified file dependencies.

## Source status

- `aeon.yml`: 115 entries parsed, 43 enabled
- Implicit references discovered: 11 (files exist on disk, threshold-checked)
- Explicit `chains: consume:` edges: 0 (chains: {} — no active chains)
- Files not yet on disk (skipped — implicit references that never existed): ~6 (operator-scorecard→`articles/heartbeat-*.md`, `articles/tweet-allocator-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`)
- Fingerprint: `f789cd3bca626257444b895c8b1636402081e86e` — **changed from prior `1ab8c658b960f260ad98797bf06b841d9b1410ef`** (market-context items WARN → STALE)

### Dependency detail (all)

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `memory/state/security-scan.json` | state | ~5d (refreshed 7-27) | 720h (30d) | ✅ OK |
| skill-security-scan | `articles/security-scan-2026-07-27.md` | articles/weekly | 5d | 192h (8d) | ✅ OK |
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles/weekly | 112d | 192h | 🔴 STALE |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~23h | 4h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-grounding.md` | topics | ~34d | 168h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-clusters.md` | topics | ~34d | 168h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-chains.md` | topics | ~34d | 168h | 🔴 STALE |
| market-context-refresh | `memory/topics/market-context.md` | topics | ~16d (380h) | 168h | 🔴 STALE (was WARN) |
| token-pick | `memory/topics/market-context.md` | topics | ~16d (380h) | 168h | 🔴 STALE (was WARN) |
| unlock-monitor | `memory/state/unlock-monitor-seen.json` | state | within threshold | 720h (30d) | ✅ OK |
| reg-monitor | `memory/topics/reg-monitor-seen.md` | topics | ~3d (7-29 Wed) | 168h | ✅ OK |

### Escalation watch — next events

- **2026-08-02**: Persistent-staleness escalation band fires for all items with first_seen_at = 2026-07-25. Items already STALE by age remain STALE; no additional band change, but flag is noted in next run's state check.
- **2026-08-02**: vuln-scanner Saturday run — `.outputs/github-trending.md` refreshes; this flag expected to clear for the Saturday run window, then reappear for next skill-freshness on 8-03 (structural).
- **2026-08-04 (Monday)**: skill-security-scan runs — refreshes `articles/security-scan-*.md` and `memory/state/security-scan.json`. workflow-security-audit-2026-04-11.md flag persists (producer disabled).

### Notable since 2026-07-30

- **skill-freshness skipped 2026-07-31** — no skill-freshness article written for 7-31 despite daily 08:00 schedule. State file unchanged at 7-30T08:00Z. Root cause unknown; likely dispatch-lag or GH Actions scheduling gap.
- **market-context.md crosses STALE threshold today** — as predicted in 7-30 article: "graduates to STALE at approximately 2026-07-30 13:00 UTC." With 2-day gap (7-30 → 8-01), confirms crossing. `.outputs/market-context-refresh.md` shows skill IS running but fetching Jun 28 fallback data (primary feed unavailable).
- **github-trending ran cleanly 2026-07-31** — `.outputs/github-trending.md` content: "GitHub Trending — 2026-07-31", top pick agavra/tuicr (Rust code-review TUI). vuln-scanner flag structural (schedule offset), not a quality issue.
- **All 7 flagged items are now STALE** — this run has no WARN items for the first time in this flagged cohort's history. 7× STALE vs prior 5× STALE + 2× WARN.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: ages computed from content-embedded timestamps — mtime unreliable in GitHub Actions checkout environments.*
