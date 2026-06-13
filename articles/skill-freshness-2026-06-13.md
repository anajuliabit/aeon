# Skill Freshness — 2026-06-13

**Verdict:** ✅ FRESHNESS_OK — all discovered dependencies are within freshness thresholds.

*Audited 44 enabled skills · 1 dependency checked · 0 flagged*

## Flagged dependencies

*(none — all clear)*

## What this means per consumer

No enabled consumer has a stale upstream dependency. The one cross-skill `.outputs/` dependency found (`vuln-scanner` reading `.outputs/github-trending.md`) is within its 4h threshold.

## Healthy consumers

- vuln-scanner — 1 dep (`.outputs/github-trending.md`, age 0.1h, threshold 4h), all fresh.
- morning-brief — 0 deps found.
- daily-routine — 0 deps found.
- github-trending — 0 deps found.
- token-alert — 0 deps found.
- token-movers — 0 deps found.
- on-chain-monitor — 0 deps found.
- defi-monitor — 0 deps found.

+ 36 more all-fresh consumers (defi-overview, token-pick, market-context-refresh, btc-levels, narrative-tracker, unlock-monitor, aixbt-pulse, search-skill, security-digest, deal-flow, reg-monitor, skill-security-scan, autoresearch, list-digest, agent-buzz, goal-tracker, skill-health, skill-analytics, self-improve, reflect, action-converter, evening-recap, thought-review, cost-report, fork-cohort, skill-evals, skill-update-check, fleet-control, weekly-review, weekly-shiplog, operator-scorecard, fork-skill-digest, fork-skill-gap, skill-graph, skill-freshness, heartbeat).

## Context: why so few dependencies were discovered

The implicit grep discovery (step 4) only captures references where the **full path** appears literally in a SKILL.md file (`memory/topics/name.md`, `.outputs/skill.md`, `articles/skill-YYYY-MM-DD.md`). Many cross-skill reads use:
- Glob patterns (`articles/token-report-*.md`) — `*` not in the path-class regex
- Directory references (`memory/topics/` + filename separately) — not a complete path
- JSON files in `memory/topics/` (`.json` extension, not `.md`) — not captured by the topics pattern

These are accepted false negatives per the skill's constraint. The explicit `chains: consume:` mechanism is the source of truth for declared dependencies — and there are currently **0 active chains** (reppo-swarm is disabled; no other chains are defined).

Detected cross-skill dependency graph depth is effectively 1 (producer → consumer) with no multi-hop chains active. The staleness gap this skill targets does not exist today for the audited scope.

## Source status

- `aeon.yml`: ~122 entries, 44 enabled
- Implicit references discovered (matching path-class patterns): 1
- Explicit `chains: consume:` edges: 0
- Files not yet on disk (skipped — implicit references that never existed): ~15 (token-report, repo-pulse, heartbeat articles, etc.)

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
