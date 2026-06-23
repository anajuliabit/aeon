# Skill Freshness — 2026-06-23

**Verdict:** ⚠️ FRESHNESS_WARN — 1 cross-skill dependency past its threshold; 7 of 8 clean.

*Audited 44 enabled skills · 8 cross-skill dependencies checked · 1 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| operator-scorecard | `articles/skill-analytics-*.md` | articles/weekly | 312h (13d) | ⚠️ WARN |

## What this means per consumer

> **operator-scorecard** — depends on 5 cross-skill article files; 1 flagged. Worst: `articles/skill-analytics-*.md` — resolved to `skill-analytics-2026-06-10.md`, last updated 13 days ago (threshold 192h / 8d, class articles/weekly). Producer `skill-analytics` is weekly (`30 18 * * 3` — Wednesday). No `skill-analytics-2026-06-17.md` exists on disk — the expected run on 2026-06-17 did not produce an article, and `skill-analytics-2026-06-24.md` has not yet been written. **operator-scorecard runs today (2026-06-23 at 10:30 UTC)** — it will read the 13-day-old article. The gap will auto-clear when `skill-analytics` runs Wednesday 2026-06-24 at 18:30 UTC (provided that run succeeds; it has a 9% success rate per 6-22 heartbeat snapshot — sandbox-truncation cluster). Suggested action: Check `skill-analytics` run history with `./scripts/skill-runs --skill skill-analytics --hours 168`. If it ran on 2026-06-17 but failed silently without writing an article, flag for repair ahead of Wednesday.

## Healthy consumers

- vuln-scanner — 1 dep (`.outputs/github-trending.md`), OK by checkout mtime. Content is effectively empty (1 byte); github-trending shows consecutive failures per cron-state. vuln-scanner's next run is Saturday 2026-06-28 — github-trending expected to recover before then. Not flagged: MISSING only fires for canonical chain/article edges; this is an optional fallback source.
- fork-skill-gap — 1 dep (`memory/topics/fork-cohort-state.json`), present and OK by checkout mtime.
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
- Implicit references not flagged (absent optional files or never-populated paths): 0

## Dedup note

**Status: FRESHNESS_NO_CHANGE.** Fingerprint `d522755e4af35478ef8cd44c558f87e1413fb78c` matches prior run (2026-06-22T08:32:07Z, < 7 days ago). Same flagged triple: `operator-scorecard:articles/skill-analytics-*.md:WARN`. Age advanced from 288h (12d) to 312h (13d) — still within the WARN band (192h–384h). Severity band unchanged → fingerprint unchanged. Notification suppressed. Re-emits 2026-06-28 if still unresolved (7-day window).

**first_seen_at escalation check:** `operator-scorecard:articles/skill-analytics-*.md` first crossed threshold 2026-06-21T14:39Z (~42h ago). Escalation to STALE fires at 168h (7 days) — not yet reached. Running clock: 42h of 168h.

## CI checkout note

All on-disk mtimes equal the checkout time (~08:22 UTC). Freshness scored against the authoritative durable signal: date encoded in `articles/{skill}-YYYY-MM-DD.md` filenames. For `.outputs/` and `memory/topics/` files (no date in filename), mtime is the only available signal — those score OK by definition in a fresh checkout. The skill-analytics WARN is derivable from the filename alone (`2026-06-10` vs today `2026-06-23` = 312h).

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches silent-staleness the other two cannot: a consumer reading an overaged file with no API errors and a 100% own-run pass rate. Fleet defining fact this run: `chains: {}` keeps cross-skill surface area near-zero. The sole live gap — operator-scorecard reading a skill-analytics article now 13 days old — clears automatically if skill-analytics succeeds Wednesday 2026-06-24 at 18:30 UTC. Risk: skill-analytics sr=9% (sandbox-truncation cluster, ISS-019). Monitor.*
