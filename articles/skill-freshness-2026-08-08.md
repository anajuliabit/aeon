# Skill Freshness — 2026-08-08

**Verdict:** 🔴 FRESHNESS_STALE — 1 dep stale across 1 consumer; no change since 2026-08-07

*Audited 43 enabled skills · 8 dependencies checked · 1 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles (weekly) | 119 days | 🔴 STALE |

## What this means per consumer

**skill-security-scan** — depends on 1 flagged file. Worst: `articles/workflow-security-audit-2026-04-11.md` last updated 2026-04-11 (threshold 192h/8d, class articles-weekly). Producer `workflow-security-audit` is disabled (schedule `0 16 * * 0`, last ran 2026-04-11, 119 days ago). References appear in prose as historical documentation (lines 19 and 132 of skill-security-scan's SKILL.md), not an active data read. Persistent since first flagged 2026-07-25 (14 days). Suggested action: add `<!-- skill-freshness:ignore -->` to suppress if not an active runtime read, or re-enable `workflow-security-audit` if the doc reference implies a live dependency.

## Healthy consumers

- aixbt-pulse — 3 deps (memory/topics/aixbt-grounding.md, aixbt-clusters.md, aixbt-chains.md), all fresh (~39min vs 168h threshold; committed 07:27 UTC today's daily-routine batch).
- market-context-refresh — 1 dep (memory/topics/market-context.md), fresh (~39min vs 168h threshold).
- token-pick — 1 dep (memory/topics/market-context.md), fresh.
- vuln-scanner — 1 dep (.outputs/github-trending.md), fresh (~39min vs 4h threshold; committed 07:27 UTC today's daily-routine batch).
- operator-scorecard — 1 dep (articles/skill-analytics-2026-08-05.md), fresh (~72h vs 192h/8d threshold).
+ 38 more all-fresh consumers.

## Δ vs prior run (2026-08-07)

No change. Prior run fingerprint `4774f3475673deec0e4da911d37853d32691fa32` is unchanged — same 1 flagged dep, same severity band.

1 persistent STALE flag (first flagged 2026-07-25, 14 days):
- 🔴 `skill-security-scan:articles/workflow-security-audit-2026-04-11.md`

Notification suppressed: `FRESHNESS_NO_CHANGE` (fingerprint stable since 2026-08-07, within 7-day re-emit window).

## Source status

- `aeon.yml`: 415+ entries parsed, 43 enabled
- Implicit references discovered: 8 (with on-disk files)
- Explicit `chains: consume:` edges: 0 (chains: {} empty)
- Files not yet on disk (skipped — implicit references that never existed): ~11 (disabled producers: token-report, push-recap, repo-actions, heartbeat-articles, tweet-allocator, repo-pulse, fork-contributor-leaderboard, repo-article, distribute-tokens, etc.)

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: article ages derived from filename dates; .outputs/ and memory/topics/ ages from git commit history (single-commit shallow clone — checkout batch time used as baseline).*
