# Skill Freshness — 2026-06-17

**Verdict:** ✅ FRESHNESS_OK — no enabled consumer is about to read an actionably-stale file.

*Audited 44 enabled skills · 8 cross-skill dependencies checked · 0 flagged*

## Flagged dependencies

None. Every cross-skill upstream an enabled consumer reads is within its freshness window.

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| — | — | — | — | ✅ OK |

## What this means per consumer

No consumer scored above OK. Three live cross-skill relationships worth recording explicitly (all benign):

> **vuln-scanner** — depends on 1 cross-skill file: `.outputs/github-trending.md` (declared in its `depends_on:` frontmatter and used as a fallback source in step 1). Content date: **06-16** (github-trending ran ~24h ago at 09:00 UTC). Producer `github-trending` is daily; the `.outputs/` class threshold is 4h for active chain steps. Chains are `{}` (no active edges), so this reference is assessed against the consumer's actual cadence: `vuln-scanner` runs **Saturdays only** (`0 16 * * 6`). By Saturday 06-21 the daily producer will have refreshed the file on Wednesday (today), Thursday, and Friday. The skill also carries a live GitHub-trending-API fallback if `.outputs/github-trending.md` is empty or absent. No gap. **OK**.

> **operator-scorecard** — reads `articles/skill-analytics-*.md` for fleet pass-rate and anomaly count. Most recent: `skill-analytics-2026-06-10.md` (Wednesday 06-10, 7 days ago = 168h). Producer `skill-analytics` is weekly (`30 18 * * 3` — Wednesday); threshold for weekly producers is 8 days (192h). Age 168h < 192h → **OK**. **Scheduled refresh today**: `skill-analytics` fires at 18:30 UTC today (Wednesday 06-17), producing a fresh article that clears the 168h count entirely. The scorecard also references `articles/heartbeat-*.md`, `articles/tweet-allocator-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md` — all from disabled producers; exempt from MISSING per methodology.

> **skill-security-scan** — references `articles/workflow-security-audit-2026-04-11.md`. This is a **hardcoded historical citation** (canonical April messages.yml injection-incident pattern for fix examples), not a freshness-sensitive read. File exists on disk. Correctly excluded from flagging per the implicit-false-positive clause.

## Healthy consumers

All 44 enabled consumers resolve to OK. Consumers with genuine cross-skill (non-self) upstreams:

- vuln-scanner — 1 cross-skill dep (`.outputs/github-trending.md`), fresh at its Saturday consumer cadence.
- operator-scorecard — 5 cross-skill article refs; 1 live (skill-analytics 7d/8d threshold OK, refreshes at 18:30 UTC today), 4 from disabled producers (not flagged).
- skill-security-scan — 1 historical citation (excluded), no live freshness dep.
- + 41 more enabled consumers whose only `articles/`, `.outputs/`, `memory/topics/`, or `memory/state/` references are **self-references** (a producer reading/writing its own state — e.g. `market-context-refresh`↔`market-context.md`, `aixbt-pulse`↔`aixbt-grounding.md`, `reg-monitor`↔`reg-monitor-seen.md`, `unlock-monitor`↔`unlock-monitor-seen.json`, `fleet-control`↔`fleet-control-state.json`, `fork-skill-digest`↔`fork-skill-digest-state.json`, `skill-graph`↔`skill-graph-state.json`, `skill-freshness`↔`skill-freshness-state.json`). Out of scope per step 4 — a producer keeping its own state is not a freshness gap.

## Source status

- `aeon.yml`: 130 entries parsed, 44 enabled
- `chains:` blocks: **none active** (`chains: {}`) → 0 explicit `consume:` edges in the fleet
- Implicit references discovered (across all enabled SKILL.md files): 8 distinct cross-skill (consumer, path) pairs after self-reference and code-example filtering
- Explicit `chains: consume:` edges: 0
- Files not flagged as MISSING (implicit references that never existed — e.g. `memory/topics/agent-evals.md`, cited inside a thought-review suggestion block as something to create, not a live read): 1 skipped
- Disabled-producer references (operator-scorecard → token-report, tweet-allocator, repo-pulse, fork-contributor-leaderboard — all `enabled: false`): exempt from MISSING, not counted

## Notable: fork-cohort-state.json (persistent absent)

`fork-skill-gap` and `fork-cohort` both reference `memory/topics/fork-cohort-state.json` as an optional accelerator (fallback to live GitHub API when absent). The file is not on disk — `fork-cohort` has experienced consecutive Sunday failures: 06-08 and 06-14 per this morning's brief log entry. This is an implicit reference that never successfully populated; MISSING is not fired per methodology (only explicit `chains: consume:` edges + canonical daily/weekly article patterns qualify). Today's morning-brief also confirmed fork-cohort is stuck as of 06-14 (~60h). Tracking and resolution belong to `skill-health`, not here.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. The fleet's defining structural fact this run — `chains: {}` is empty, so there are zero cross-skill chain edges; almost every file reference in the fleet is a producer touching its own state. Surface area for silent upstream staleness is near-zero.*

*CI checkout note: every file's on-disk mtime is the checkout time (~09:16 UTC); freshness was scored against the authoritative durable signal — the date encoded in each `articles/{skill}-YYYY-MM-DD.md` filename and the content-date inside `.outputs/` files. Same conclusion either way: nothing actionably stale.*
