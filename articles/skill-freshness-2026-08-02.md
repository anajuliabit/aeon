# Skill Freshness — 2026-08-02

**Verdict:** 🔴 FRESHNESS_STALE — 7 of 11 deps flagged across 5 of 43 enabled consumers

*Audited 43 enabled skills · 11 dependencies checked · 7 flagged (7 STALE, 0 WARN)*

**Exit status:** FRESHNESS_NO_CHANGE — fingerprint `f789cd3bca626257444b895c8b1636402081e86e` unchanged from 2026-08-01 (1d ago). Notification suppressed (7-day dedup window; re-emits 2026-08-08 if still unchanged). All 7 flagged items persist from yesterday. Persistent-staleness 8-day mark reached for all items with first_seen_at 2026-07-25 — already STALE by age, no additional band change (STALE is ceiling).

---

> **Methodology note:** On-disk mtimes in GitHub Actions reflect git checkout time (2026-08-02 09:28 UTC) for all committed files. Age computation uses content-embedded timestamps (`# as of YYYY-MM-DD` headers in memory/topics/ files, filename dates in articles/, content date headers in .outputs/ files). Ages below are derived from best available signal per file.

## Flagged dependencies

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles/weekly | 113d (2712h) | 192h (8d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-grounding.md` | topics | ~35d (~840h) | 168h (7d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-clusters.md` | topics | ~35d (~840h) | 168h (7d) | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-chains.md` | topics | ~35d (~840h) | 168h (7d) | 🔴 STALE |
| market-context-refresh | `memory/topics/market-context.md` | topics | ~17d (~408h) | 168h (7d) | 🔴 STALE |
| token-pick | `memory/topics/market-context.md` | topics | ~17d (~408h) | 168h (7d) | 🔴 STALE |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~23h | 4h | 🔴 STALE |

*(Sorted by severity desc, then age desc. OK rows omitted.)*

## What this means per consumer

> **skill-security-scan** — depends on 3 files; 1 flagged. Worst: `articles/workflow-security-audit-2026-04-11.md` last updated 113 days ago (threshold 192h, class articles/weekly). The producer `workflow-security-audit` is **disabled** (`enabled: false`). Static reference doc — will not refresh while producer is off. **Persistent-staleness 8-day mark** (first_seen 2026-07-25). skill-security-scan itself ran 2026-07-27, producing `articles/security-scan-2026-07-27.md` (OK, 6d) and refreshing `memory/state/security-scan.json` (OK, 6d). Next run: 2026-08-04 (Monday). Suggested action: add `<!-- skill-freshness:ignore -->` to skills/skill-security-scan/SKILL.md if this historical reference is intentionally permanent, or re-enable workflow-security-audit.

> **aixbt-pulse** — depends on 3 files; all 3 flagged STALE. Worst: `memory/topics/aixbt-grounding.md` last written 2026-06-28 21:00Z (~840h / ~35d ago, threshold 168h). **Dead slot d35** — per MEMORY.md, aixbt-pulse has been silent since 2026-06-28 21:00Z; 65+ missed cycles. All three topic files frozen at Jun 28 state. **Persistent-staleness 8-day mark** (first_seen 2026-07-25). Suggested action: check `./scripts/skill-runs --skill aixbt-pulse --hours 720`; root cause in ISS-027 cluster context.

> **vuln-scanner** — depends on 1 file; 1 flagged STALE. `.outputs/github-trending.md` content header reads "GitHub Trending — 2026-08-01" (~23h old at 08:00 UTC, threshold 4h). Structural gap: github-trending fires at 09:00 UTC, one hour after skill-freshness. Today (Saturday 8-02) vuln-scanner runs at 16:00 UTC — by then github-trending will have refreshed the file (09:00 run). Next skill-freshness on 8-03 will see yesterday's output again (structural, not an incident).

> **market-context-refresh** — depends on 1 file; 1 flagged STALE. `memory/topics/market-context.md` last meaningfully updated 2026-07-16 (~17d / ~408h ago, threshold 168h, 2×=336h → STALE). Skill IS running but falling back to 2026-06-28 cached data (primary fetch unavailable). **Persistent-staleness 8-day mark** (first_seen 2026-07-25). Suggested action: investigate why primary market-context feed is unavailable; ISS-027 cluster unblock resolves.

> **token-pick** — depends on 1 file; 1 flagged STALE. Same `memory/topics/market-context.md` (~408h). Token picks being made against 17d+ stale market context — BTC price, F&G, and regime shown are Jul 16 vintage. **Persistent-staleness 8-day mark** (first_seen 2026-07-25). Resolves with market-context-refresh fix.

## Healthy consumers

- skill-security-scan — 2 of 3 deps fresh. (`memory/state/security-scan.json` 6d / 144h, threshold 720h; `articles/security-scan-2026-07-27.md` 6d / 144h, threshold 192h)
- unlock-monitor — 1 dep, all fresh. (`memory/state/unlock-monitor-seen.json`: within 30d state threshold)
- reg-monitor — 1 dep, all fresh. (`memory/topics/reg-monitor-seen.md`: last entry 2026-07-29, 3d / 72h, threshold 168h)
- morning-brief — no identified file deps beyond MEMORY.md context read.
- daily-routine — no identified file deps beyond live API calls.
- github-trending — no identified upstream file deps; writes to .outputs/.
- narrative-tracker — no identified upstream file deps beyond live API calls.
- + 33 more all-fresh consumers with no identified file dependencies.

## Source status

- `aeon.yml`: 115 entries parsed, 43 enabled
- Implicit references discovered: 11 (files exist on disk, threshold-checked)
- Explicit `chains: consume:` edges: 0 (chains: {} — no active chains)
- Files not yet on disk (skipped — implicit refs that never existed): ~6 (operator-scorecard→`articles/heartbeat-*.md`, `articles/tweet-allocator-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`)
- Fingerprint: `f789cd3bca626257444b895c8b1636402081e86e` — **unchanged from 2026-08-01** (FRESHNESS_NO_CHANGE)

### Dependency detail (all)

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `memory/state/security-scan.json` | state | 6d (144h, gen 2026-07-27) | 720h (30d) | ✅ OK |
| skill-security-scan | `articles/security-scan-2026-07-27.md` | articles/weekly | 6d (144h) | 192h (8d) | ✅ OK |
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles/weekly | 113d (2712h) | 192h | 🔴 STALE |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~23h (content: 2026-08-01) | 4h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-grounding.md` | topics | ~35d (~840h, as of 2026-06-28) | 168h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-clusters.md` | topics | ~35d (~840h, as of 2026-06-28) | 168h | 🔴 STALE |
| aixbt-pulse | `memory/topics/aixbt-chains.md` | topics | ~35d (~840h, as of 2026-06-28) | 168h | 🔴 STALE |
| market-context-refresh | `memory/topics/market-context.md` | topics | ~17d (~408h, as of 2026-07-16) | 168h | 🔴 STALE |
| token-pick | `memory/topics/market-context.md` | topics | ~17d (~408h, as of 2026-07-16) | 168h | 🔴 STALE |
| unlock-monitor | `memory/state/unlock-monitor-seen.json` | state | within 30d threshold | 720h (30d) | ✅ OK |
| reg-monitor | `memory/topics/reg-monitor-seen.md` | topics | 3d (72h, last entry 2026-07-29) | 168h | ✅ OK |

### Escalation watch — next events

- **2026-08-02 09:00 UTC (today)**: github-trending runs — refreshes `.outputs/github-trending.md`. vuln-scanner (16:00 UTC today) receives fresh file.
- **2026-08-03 (Sunday)**: skill-freshness next run — `.outputs/github-trending.md` will again be ~23h stale (structural).
- **2026-08-04 (Monday)**: skill-security-scan runs — refreshes `articles/security-scan-*.md` + `memory/state/security-scan.json`. workflow-security-audit-2026-04-11.md flag persists (producer disabled).
- **2026-08-06 (Wednesday)**: reg-monitor runs — refreshes `memory/topics/reg-monitor-seen.md`. Currently OK (3d); stays within threshold through run.
- **2026-08-08**: 7-day re-emit window expires (last notification 2026-08-01). If fingerprint still unchanged, FRESHNESS_STALE notification re-fires as periodic reminder.

### Notable since 2026-08-01

- **No new flags, no cleared flags** — identical fingerprint for consecutive day.
- **Persistent-staleness 8-day mark reached** — all items with first_seen_at 2026-07-25 cross 8 days today. Items already STALE; no severity escalation (STALE is ceiling).
- **vuln-scanner scheduled today 16:00 UTC (Saturday)** — structural flag will clear within today's run window; reappears Sunday.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: ages computed from content-embedded timestamps — mtime unreliable in GitHub Actions checkout environments.*
