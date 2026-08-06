# Skill Freshness — 2026-08-06

**Verdict:** 🔴 FRESHNESS_STALE — 2 deps stale across 2 consumers; 5 prior-run flags resolved to fresh

*Audited 43 enabled skills · 8 dependencies checked · 2 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles (weekly) | 117 days | 🔴 STALE |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~11h | 🔴 STALE |

## What this means per consumer

**skill-security-scan** — depends on 1 flagged file. Worst: `articles/workflow-security-audit-2026-04-11.md` last updated 2026-04-11 (threshold 192h/8d, class articles-weekly). Producer `workflow-security-audit` is disabled (schedule `0 16 * * 0`, last ran 2026-04-11, 117 days ago). References appear in prose as historical documentation (lines 19 and 132 of skill-security-scan's SKILL.md), not an active data read. Persistent since first flagged 2026-07-25 (12+ days). Suggested action: add `<!-- skill-freshness:ignore -->` to suppress if not an active runtime read, or re-enable `workflow-security-audit` if the doc reference implies a live dependency.

**vuln-scanner** — depends on 1 flagged file. Worst: `.outputs/github-trending.md` last committed 2026-08-05 22:06 UTC (~11h ago, threshold 4h, class outputs). Producer `github-trending` is enabled (daily 09:00 UTC) and ran yesterday evening. The 4h threshold flags because `chains: {}` means no explicit chain edge exists — this is a heuristic `.outputs/` class match. The file will refresh on today's `github-trending` run at 09:00 UTC. Persistent since 2026-07-25 (12+ days — non-chain implicit dep keeps triggering on pre-09Z audit). Suggested action: Monitor — expected to clear after today's github-trending run; if this is noise, add `<!-- skill-freshness:ignore -->` to vuln-scanner's SKILL.md for this path.

## Healthy consumers

- aixbt-pulse — 3 deps (memory/topics/aixbt-grounding.md, aixbt-clusters.md, aixbt-chains.md), all fresh (last committed 2026-08-05 22:06 UTC, ~11h vs 168h threshold).
- market-context-refresh — 1 dep (memory/topics/market-context.md), fresh (~11h vs 168h threshold).
- token-pick — 1 dep (memory/topics/market-context.md), fresh.
- operator-scorecard — 1 dep (articles/skill-analytics-2026-08-05.md), fresh (~12h vs 192h threshold).
+ 39 more all-fresh consumers.

## Δ vs prior run (2026-08-03)

Prior run fingerprint `f789cd3bca626257444b895c8b1636402081e86e` had 7 flagged deps. 5 resolved to fresh since 2026-08-03:
- ✅ `aixbt-pulse:memory/topics/aixbt-grounding.md` — updated 2026-08-05 22:06Z
- ✅ `aixbt-pulse:memory/topics/aixbt-clusters.md` — updated 2026-08-05 22:06Z
- ✅ `aixbt-pulse:memory/topics/aixbt-chains.md` — updated 2026-08-05 22:06Z
- ✅ `market-context-refresh:memory/topics/market-context.md` — updated 2026-08-05 22:06Z
- ✅ `token-pick:memory/topics/market-context.md` — updated 2026-08-05 22:06Z

2 persistent STALE flags remain (both first flagged 2026-07-25, 12+ days):
- 🔴 `skill-security-scan:articles/workflow-security-audit-2026-04-11.md`
- 🔴 `vuln-scanner:.outputs/github-trending.md`

## Source status

- `aeon.yml`: 415+ entries parsed, 43 enabled
- Implicit references discovered: 8 (with on-disk files)
- Explicit `chains: consume:` edges: 0 (chains: {} empty)
- Files not yet on disk (skipped — implicit references that never existed): ~11 (disabled producers: token-report, push-recap, repo-actions, heartbeat-articles, tweet-allocator, repo-pulse, fork-contributor-leaderboard, repo-article, distribute-tokens, etc.)

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes and git commit history — this skill measures nothing it does not also report.*
