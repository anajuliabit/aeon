# Skill Freshness — 2026-06-22

**Verdict:** ⚠️ FRESHNESS_WARN — 1 cross-skill dependency past its threshold; 7 of 8 clean.

*Audited 44 enabled skills · 8 cross-skill dependencies checked · 1 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| operator-scorecard | `articles/skill-analytics-*.md` | articles/weekly | 288h (12d) | ⚠️ WARN |

## What this means per consumer

> **operator-scorecard** — depends on 5 cross-skill article files; 1 flagged. Worst: `articles/skill-analytics-*.md` — resolved to `skill-analytics-2026-06-10.md`, last updated 12 days ago (threshold 192h / 8d, class articles/weekly). Producer `skill-analytics` is weekly (`30 18 * * 3` — Wednesday). No `skill-analytics-2026-06-17.md` exists on disk — the expected run on 2026-06-17 did not produce an article. Next scheduled window: Wednesday 2026-06-24 (2 days away). `operator-scorecard` runs Monday 2026-06-23 at 10:30 UTC — by then the gap will be 312h (13 days), still in the WARN band (192h–384h). Suggested action: Check `skill-analytics` run history (`./scripts/skill-runs --skill skill-analytics --hours 168`). If it ran and failed silently, repair; if it wasn't dispatched, Wednesday 2026-06-24 clears the gap automatically.

## Healthy consumers

- vuln-scanner — 1 dep (`.outputs/github-trending.md`), OK by checkout mtime. Content is effectively empty (1 byte); github-trending shows consecutive failures per cron-state. vuln-scanner's next run is Saturday 2026-06-28 — github-trending expected to recover before then. Not flagged: MISSING only fires for canonical chain/article edges; this is an optional fallback source.
- fork-skill-gap — 1 dep (`memory/topics/fork-cohort-state.json`), now present and OK by checkout mtime. Note: was absent on disk during yesterday's run (2026-06-21T14:39Z); fork-cohort wrote it at ~19:00 UTC yesterday after that run. Transition: absent-not-flagged → present-OK. No net change to verdict.
- operator-scorecard (other refs) — `articles/heartbeat-*.md`, `articles/tweet-allocator-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`: all from disabled producers (`enabled: false`). Exempt from MISSING per methodology.
- skill-security-scan — 1 historical citation (`articles/workflow-security-audit-2026-04-11.md`, hardcoded reference, correctly excluded per methodology).
- heartbeat — 1 dep (`articles/token-report-*.md`), disabled producer, exempt.
- + 39 more enabled consumers whose `articles/`, `.outputs/`, `memory/topics/`, `memory/state/` references are self-references (`market-context-refresh`↔`market-context.md`, `aixbt-pulse`↔`aixbt-{grounding,chains,clusters}.md`, `reg-monitor`↔`reg-monitor-seen.md`, `unlock-monitor`↔`unlock-monitor-seen.json`, `fleet-control`↔`fleet-control-state.json`, `fork-skill-digest`↔`fork-skill-digest-state.json`, `skill-graph`↔`skill-graph-state.json`, `skill-freshness`↔`skill-freshness-state.json`, and 31 others). Out of scope per step 4.

## Source status

- `aeon.yml`: 130 entries parsed, 44 enabled
- `chains:` blocks: **none active** (`chains: {}`) → 0 explicit `consume:` edges
- Implicit references discovered (across all enabled SKILL.md files): 8 distinct cross-skill (consumer, path) pairs after self-reference and code-example filtering
- Explicit `chains: consume:` edges: 0
- Disabled-producer references: 5 (operator-scorecard → heartbeat, tweet-allocator, token-report, repo-pulse; heartbeat → token-report — all `enabled: false` or no matching skill, exempt from MISSING)
- Implicit references not flagged (absent optional files or never-populated paths): 0 (fork-cohort-state.json now present; .outputs/github-trending.md present-but-sparse, OK by mtime)

## Dedup note

**Status: FRESHNESS_NO_CHANGE.** Fingerprint `d522755e4af35478ef8cd44c558f87e1413fb78c` matches prior run (2026-06-21T14:39Z, < 7 days ago). Same flagged triple: `operator-scorecard:articles/skill-analytics-*.md:WARN`. Notification suppressed. Re-emits after 7 days if still unresolved (2026-06-28).

## CI checkout note

All on-disk mtimes equal the checkout time (~08:31 UTC). Freshness scored against the authoritative durable signal: date encoded in `articles/{skill}-YYYY-MM-DD.md` filenames. For `.outputs/` and `memory/topics/` files (no date in filename), mtime is the only available signal — those score OK by definition in a fresh checkout. The skill-analytics WARN is derivable from the filename alone (`2026-06-10` vs today `2026-06-22` = 288h).

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches silent-staleness the other two cannot: a consumer reading an overaged file with no API errors and a 100% own-run pass rate. Fleet defining fact this run: `chains: {}` keeps cross-skill surface area near-zero. The sole live gap — operator-scorecard reading a skill-analytics article now 12 days old — is two days away from auto-clearing when skill-analytics runs Wednesday 2026-06-24.*
