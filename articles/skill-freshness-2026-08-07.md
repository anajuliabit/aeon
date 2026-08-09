# Skill Freshness — 2026-08-07

**Verdict:** 🔴 FRESHNESS_STALE — 1 dep stale across 1 consumer; 1 prior-run flag resolved to fresh

*Audited 43 enabled skills · 8 dependencies checked · 1 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles (weekly) | 118 days | 🔴 STALE |

## What this means per consumer

**skill-security-scan** — depends on 1 flagged file. Worst: `articles/workflow-security-audit-2026-04-11.md` last updated 2026-04-11 (threshold 192h/8d, class articles-weekly). Producer `workflow-security-audit` is disabled (schedule `0 16 * * 0`, last ran 2026-04-11, 118 days ago). References appear in prose as historical documentation (lines 19 and 132 of skill-security-scan's SKILL.md), not an active data read. Persistent since first flagged 2026-07-25 (13+ days). Suggested action: add `<!-- skill-freshness:ignore -->` to suppress if not an active runtime read, or re-enable `workflow-security-audit` if the doc reference implies a live dependency.

## Healthy consumers

- aixbt-pulse — 3 deps (memory/topics/aixbt-grounding.md, aixbt-clusters.md, aixbt-chains.md), all fresh (~47min vs 168h threshold; committed 08:28 UTC in today's daily-routine batch).
- market-context-refresh — 1 dep (memory/topics/market-context.md), fresh (~47min vs 168h threshold).
- token-pick — 1 dep (memory/topics/market-context.md), fresh.
- operator-scorecard — 1 dep (articles/skill-analytics-2026-08-05.md), fresh (~48h vs 192h threshold).
+ 38 more all-fresh consumers.

## Δ vs prior run (2026-08-06)

Prior run fingerprint `fd5c367b5476282da0197e4b22eadd3ba1b1cf56` had 2 flagged deps. 1 resolved to fresh since 2026-08-06:
- ✅ `vuln-scanner:.outputs/github-trending.md` — committed 2026-08-07 08:28Z in daily-routine batch (~47min at audit time, below 4h outputs threshold)

1 persistent STALE flag remains (first flagged 2026-07-25, 13+ days):
- 🔴 `skill-security-scan:articles/workflow-security-audit-2026-04-11.md`

## Source status

- `aeon.yml`: 415+ entries parsed, 43 enabled
- Implicit references discovered: 8 (with on-disk files)
- Explicit `chains: consume:` edges: 0 (chains: {} empty)
- Files not yet on disk (skipped — implicit references that never existed): ~11 (disabled producers: token-report, push-recap, repo-actions, heartbeat-articles, tweet-allocator, repo-pulse, fork-contributor-leaderboard, repo-article, distribute-tokens, etc.)

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes and git commit history — this skill measures nothing it does not also report.*
