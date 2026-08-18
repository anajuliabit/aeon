# Skill Freshness — 2026-08-18

**Verdict:** 🔴 FRESHNESS_STALE — 3 of 9 deps flagged across 3 of 43 enabled consumers

*Audited 43 enabled skills · 9 dependencies checked · 3 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| token-pick | `memory/topics/market-context.md` | memory/topics | ~33d (792h) | 🔴 STALE |
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles | ~128d (3072h) | 🔴 STALE |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~23h | 🔴 STALE |

*(Sorted by severity desc, then consumer name. OK rows omitted.)*

## What this means per consumer

> **token-pick** — depends on 1 file; 1 flagged. Worst: `memory/topics/market-context.md` last updated 2026-07-16 (~33d ago, threshold 168h, class memory/topics). The producer `market-context-refresh` is enabled and scheduled daily at 13:00 UTC but has not written a fresh file since 2026-07-16 (per file content header). MEMORY.md notes this explicitly: "STALE ~32d/768h+, crossed 2× threshold 8-01; refresh chained on next batch-dark thaw or manual invoke." Suggested action: Verify `market-context-refresh` is still on schedule; if so, the producer ran but did not write a new article.

> **skill-security-scan** — depends on 2 files; 1 flagged. Worst: `articles/workflow-security-audit-2026-04-11.md` last produced 2026-04-11 (~128d ago, threshold 192h for weekly producer, class articles). The producer `workflow-security-audit` has `enabled: false` (weekly Sunday schedule). **Note:** This reference in `skill-security-scan/SKILL.md` is a documentary citation ("see the 2026-04-11 messages.yml incident…") rather than a live data dependency — it's unlikely to affect skill output quality. If a fresh audit is needed, re-enable `workflow-security-audit` or ignore this flag. Suggested action: Verify `workflow-security-audit` is still on schedule; if so, the producer ran but did not write a new article.

> **vuln-scanner** — depends on 1 file; 1 flagged. Worst: `.outputs/github-trending.md` content dated 2026-08-17 (~23h ago, threshold 4h, class outputs). The producer `github-trending` is enabled and runs daily at 09:00 UTC — it had not yet run today at audit time (08:18 UTC). **Note:** vuln-scanner is not in a formal chain with github-trending (chains: {} in aeon.yml), so the 4h outputs threshold is stricter than the practical cadence warrants. The file will be refreshed when github-trending fires at 09:00 UTC today. Suggested action: Monitor — one missed run, expected to clear on next producer cadence.

## Healthy consumers

- operator-scorecard — 1 dep (articles/skill-analytics-2026-08-12.md, 6d old, threshold 8d), all fresh.
- fork-skill-gap — 1 dep (memory/topics/fork-cohort-state.json, 2d old, threshold 7d), all fresh.
- reg-monitor — 1 dep (memory/topics/reg-monitor-seen.md, self-reference filtered), all fresh.
- fork-cohort — 1 dep (memory/topics/fork-cohort-state.json, self-reference filtered), all fresh.
- fork-skill-digest — 1 dep (memory/topics/fork-skill-digest-state.json, self-reference filtered), all fresh.
- skill-security-scan — 1 dep (memory/state/security-scan.json, self-reference filtered), all fresh.

+ 37 more all-fresh consumers (no cross-skill article/topic/state references discovered).

## Source status

- `aeon.yml`: 130+ entries, 43 enabled
- Implicit references discovered: 9 (5 cross-skill, 4 self-references filtered)
- Explicit `chains: consume:` edges: 0 (chains: {} — none active)
- Files not yet on disk (skipped — implicit references that never existed): 6 (heartbeat articles, tweet-allocator articles, token-report articles, repo-pulse articles, push-recap articles, repo-actions articles — all from disabled producers)

**Methodology note:** GitHub Actions checks out all files at a single point in time (2026-08-18 07:08:21 UTC), making on-disk mtimes unreliable. Ages above are derived from file content headers (market-context.md → "as of 2026-07-16"; workflow-security-audit article → filename date 2026-04-11; github-trending output → content header "2026-08-17") and article filename dates (skill-analytics-2026-08-12.md → filename date; fork-cohort-state.json → "last_run": "2026-08-16"). This is the correct approach for persistent-file auditing in an ephemeral checkout environment.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from file content timestamps and filename dates — this skill measures nothing it does not also report.*
