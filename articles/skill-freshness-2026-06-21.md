# Skill Freshness — 2026-06-21

**Verdict:** ⚠️ FRESHNESS_WARN — 1 cross-skill dependency past its threshold; 7 of 8 clean.

*Audited 44 enabled skills · 8 cross-skill dependencies checked · 1 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| operator-scorecard | `articles/skill-analytics-*.md` | articles/weekly | 264h (11d) | ⚠️ WARN |

## What this means per consumer

> **operator-scorecard** — depends on 5 cross-skill article files; 1 flagged. Worst: `articles/skill-analytics-*.md` — resolved to `skill-analytics-2026-06-10.md`, last updated 11 days ago (threshold 192h / 8d, class articles/weekly). Producer `skill-analytics` is weekly (`30 18 * * 3` — Wednesday). The expected run on 2026-06-17 did not produce an article; no `skill-analytics-2026-06-17.md` exists on disk. Next scheduled window: Wednesday 2026-06-24. `operator-scorecard` runs Monday 2026-06-22 at 10:30 UTC — by then the gap will be 288h (12 days), still in the WARN band (192h–384h) but approaching two missed Wednesdays. Suggested action: Check `skill-analytics` run history (`./scripts/skill-runs --skill skill-analytics --hours 168`). If it ran and failed silently, repair; if it wasn't dispatched, the next Wednesday (06-24) clears the gap.

## Healthy consumers

- vuln-scanner — 1 dep (`.outputs/github-trending.md`), OK by checkout mtime. Content is effectively empty (1 byte); github-trending shows 11 consecutive failures per morning-brief cron-state. vuln-scanner's next run is Saturday 2026-06-28 — github-trending is expected to recover before then. Not flagged: MISSING only fires for canonical chain/article edges, and this is an optional fallback source. Cadence-contextual: OK.
- skill-security-scan — 1 historical citation (`articles/workflow-security-audit-2026-04-11.md`, hardcoded reference, correctly excluded per methodology).
- fork-skill-gap / fork-cohort — `memory/topics/fork-cohort-state.json` absent on disk. Implicit reference that never populated (fork-cohort has consecutive Sunday failures: 2026-06-08, 2026-06-14). Not flagged: MISSING per methodology requires explicit `chains: consume:` edges or canonical daily/weekly article patterns. Resolution tracked in `skill-health`, not here.
- operator-scorecard (other refs) — `articles/heartbeat-*.md`, `articles/tweet-allocator-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`: all from disabled producers (`enabled: false`). Exempt from MISSING per methodology.
- + 40 more enabled consumers whose `articles/`, `.outputs/`, `memory/topics/`, `memory/state/` references are self-references (producer reading/writing its own state — `market-context-refresh`↔`market-context.md`, `aixbt-pulse`↔`aixbt-{grounding,chains,clusters}.md`, `reg-monitor`↔`reg-monitor-seen.md`, `unlock-monitor`↔`unlock-monitor-seen.json`, `fleet-control`↔`fleet-control-state.json`, `fork-skill-digest`↔`fork-skill-digest-state.json`, `skill-graph`↔`skill-graph-state.json`, `skill-freshness`↔`skill-freshness-state.json`). Out of scope per step 4.

## Source status

- `aeon.yml`: 130 entries parsed, 44 enabled
- `chains:` blocks: **none active** (`chains: {}`) → 0 explicit `consume:` edges
- Implicit references discovered (across all enabled SKILL.md files): 8 distinct cross-skill (consumer, path) pairs after self-reference and code-example filtering
- Explicit `chains: consume:` edges: 0
- Disabled-producer references: 4 (operator-scorecard → heartbeat, tweet-allocator, token-report, repo-pulse — all `enabled: false`, exempt from MISSING)
- Implicit references not flagged (absent optional files or never-populated paths): 2 (`memory/topics/fork-cohort-state.json`, `.outputs/github-trending.md` content)

## CI checkout note

All on-disk mtimes equal the checkout time (~14:37 UTC). Freshness scored against the authoritative durable signal: date encoded in `articles/{skill}-YYYY-MM-DD.md` filenames. For `.outputs/` files (no date in filename), mtime is the only available signal — those score OK by definition in a fresh checkout. The skill-analytics WARN is derivable from the filename alone (`2026-06-10` vs today `2026-06-21` = 264h).

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches silent-staleness the other two cannot: a consumer reading an overaged file with no API errors and a 100% own-run pass rate. Fleet defining fact this run: `chains: {}` keeps cross-skill surface area near-zero. The sole live gap — operator-scorecard reading a skill-analytics article now 11 days old — is one missed Wednesday away from auto-clearing on 2026-06-24.*
