# Skill Freshness — 2026-08-10

**Verdict:** 🔴 FRESHNESS_STALE — 1 dep stale across 1 consumer; no change since 2026-08-09

*Audited 43 enabled skills · 8 dependencies checked · 1 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles (weekly) | 121 days | 🔴 STALE |

## What this means per consumer

**skill-security-scan** — depends on 1 flagged file. Worst: `articles/workflow-security-audit-2026-04-11.md` last updated 2026-04-11 (threshold 192h/8d, class articles-weekly). Producer `workflow-security-audit` is disabled (schedule `0 16 * * 0`, last ran 2026-04-11, 121 days ago). References appear in prose as historical documentation in skill-security-scan's SKILL.md, not an active data read. Persistent since first flagged 2026-07-25 (16 days). Suggested action: add `<!-- skill-freshness:ignore -->` to suppress if not an active runtime read, or re-enable `workflow-security-audit` if the doc reference implies a live dependency.

## Healthy consumers

- aixbt-pulse — 3 deps (memory/topics/aixbt-grounding.md, aixbt-clusters.md, aixbt-chains.md), all fresh.
- market-context-refresh — 1 dep (memory/topics/market-context.md), fresh.
- token-pick — 1 dep (memory/topics/market-context.md), fresh.
- vuln-scanner — 1 dep (.outputs/github-trending.md), fresh.
- operator-scorecard — 1 dep (articles/skill-analytics-2026-08-05.md), fresh (~120h vs 192h/8d threshold).
- heartbeat — 1 dep (articles/token-report-*.md), on-demand producer; no file on disk (skipped).
+ 37 more all-fresh consumers.

## Δ vs prior run (2026-08-09)

No change. Prior run fingerprint `4774f3475673deec0e4da911d37853d32691fa32` is unchanged — same 1 flagged dep, same severity band.

1 persistent STALE flag (first flagged 2026-07-25, day 16):
- 🔴 `skill-security-scan:articles/workflow-security-audit-2026-04-11.md`

Notification suppressed: `FRESHNESS_NO_CHANGE` (fingerprint stable, within 7-day re-emit window; last run 2026-08-09).

## Source status

- `aeon.yml`: 415+ entries parsed, 43 enabled
- Implicit references discovered: 8 (with on-disk files)
- Explicit `chains: consume:` edges: 0 (chains: {} empty)
- Files not yet on disk (skipped — implicit references that never existed): ~11 (disabled producers: token-report, push-recap, repo-actions, tweet-allocator, repo-pulse, fork-contributor-leaderboard, repo-article, distribute-tokens, etc.)

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: article ages derived from filename dates; .outputs/ and memory/topics/ ages from git commit timestamp (single-commit shallow clone — checkout batch time used as baseline).*
