# Skill Freshness — 2026-07-12

**Verdict:** ✅ FRESHNESS_OK — all 11 dependencies across 7 consumers are fresh

*Audited 43 enabled skills · 11 dependencies checked · 0 flagged*

## Flagged dependencies

*(none — all dependencies within freshness thresholds)*

## What this means per consumer

*(all consumers OK — no action needed)*

## Healthy consumers

- aixbt-pulse — 3 deps (memory/topics/aixbt-grounding.md, aixbt-clusters.md, aixbt-chains.md), all fresh.
- autoresearch — 1 dep (.outputs/github-trending.md), all fresh.
- market-context-refresh — 1 dep (memory/topics/market-context.md), all fresh.
- reg-monitor — 1 dep (memory/topics/reg-monitor-seen.md), all fresh.
- skill-security-scan — 3 deps (memory/state/security-scan.json · articles/security-scan-2026-07-06.md · articles/workflow-security-audit-2026-04-11.md), all fresh.
- unlock-monitor — 1 dep (memory/state/unlock-monitor-seen.json), all fresh.
- vuln-scanner — 1 dep (articles/vuln-scan-2026-07-11.md), all fresh.
+ 36 more all-fresh consumers (no detectable upstream file dependencies).

## Source status

- `aeon.yml`: 43 entries enabled (of ~130 total); `chains: {}` — no active chains, zero explicit consume: edges
- Implicit references discovered: 11
- Explicit `chains: consume:` edges: 0
- Files not yet on disk (skipped — implicit references that never existed): 1 (`articles/token-report-2026-04-28.md` in fork-skill-digest example output; producer skill disabled and never ran in this fork)
- Dedup status: `FRESHNESS_NO_CHANGE` — fingerprint identical to 2026-07-11 run (sha1=da39a3ee, same FRESHNESS_OK verdict, last run 24h ago, within 7-day re-emit window)

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
