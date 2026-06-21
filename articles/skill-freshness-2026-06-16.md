# Skill Freshness — 2026-06-16

**Verdict:** ✅ FRESHNESS_OK — no enabled consumer is about to read an actionably-stale file.

*Audited 44 enabled skills · 8 cross-skill dependencies checked · 0 flagged*

## Flagged dependencies

None. Every cross-skill upstream an enabled consumer reads is within its freshness window.

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| — | — | — | — | ✅ OK |

## What this means per consumer

No consumer scored above OK. The two live cross-skill relationships worth recording explicitly (both benign):

> **vuln-scanner** — depends on 1 cross-skill file: `.outputs/github-trending.md` (referenced in its SKILL.md as a primary target-repo source). Content date: **06-15** (github-trending ran ~24h ago at 09:00 UTC). Producer `github-trending` is daily; threshold under the daily-producer window is 28h. Age ~24h < 28h → **OK**. Consumer `vuln-scanner` runs **Saturdays only** (`0 16 * * 6`); by Saturday the daily producer will have refreshed the file two more times. The skill also carries a live GitHub-trending-API fallback if the chained output is absent or stale. No gap.

> **operator-scorecard** — reads `articles/skill-analytics-*.md` for fleet pass-rate and anomaly count. Most recent: `skill-analytics-2026-06-10.md` (Wednesday 06-10, 6 days ago). Producer `skill-analytics` is weekly (Wednesday `30 18 * * 3`); threshold for weekly producers is 8 days (192h). Age 144h < 192h → **OK**. Next scheduled run: 2026-06-17 (tomorrow). The scorecard also references `articles/heartbeat-*.md`, `articles/tweet-allocator-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md` — all from disabled producers; none are flagged (disabled producers are exempt from MISSING per methodology).

> **skill-security-scan** — references `articles/workflow-security-audit-2026-04-11.md`. This is a **hardcoded historical citation** (canonical April messages.yml injection-incident pattern for fix examples), not a freshness-sensitive read. File exists. Correctly not flagged per the "implicit false-positive tolerated" clause.

## Healthy consumers

All 44 enabled consumers resolve to OK. Consumers with genuine cross-skill (non-self) upstreams:

- vuln-scanner — 1 cross-skill dep (`.outputs/github-trending.md`), fresh at its Saturday consumer cadence.
- operator-scorecard — 5 cross-skill article refs; 1 live (skill-analytics, 6d/8d threshold OK), 4 from disabled producers (not flagged).
- skill-security-scan — 1 historical citation (excluded), no live freshness dep.
- + 41 more enabled consumers whose only `articles/`, `.outputs/`, `memory/topics/`, or `memory/state/` references are **self-references** (a producer reading/writing its own state — e.g., `market-context-refresh`↔`market-context.md`, `aixbt-pulse`↔`aixbt-grounding.md`, `reg-monitor`↔`reg-monitor-seen.md`, `unlock-monitor`↔`unlock-monitor-seen.json`, `fleet-control`↔`fleet-control-state.json`, `fork-skill-digest`↔`fork-skill-digest-state.json`, `skill-graph`↔`skill-graph-state.json`, `skill-freshness`↔`skill-freshness-state.json`), which are out of scope per step 4.

## Source status

- `aeon.yml`: 130 entries parsed, 44 enabled
- `chains:` blocks: **none active** (`chains: {}`) → 0 explicit `consume:` edges in the fleet
- Implicit references discovered (across all enabled SKILL.md files): 8 distinct cross-skill (consumer, path) pairs after self-reference and code-example filtering
- Explicit `chains: consume:` edges: 0
- Files not flagged as MISSING (implicit references that never existed — e.g., `memory/topics/agent-evals.md`, cited inside a thought-review *suggestion* block as something to create, not a live read): 1 skipped
- Disabled-producer references (heartbeat/operator-scorecard → token-report, tweet-allocator, repo-pulse, fork-contributor-leaderboard, repo-article, project-lens — all `enabled: false`): exempt from MISSING, not counted in flagged total

## Notable: fork-cohort-state.json

`fork-skill-gap` reads `memory/topics/fork-cohort-state.json` as an optional accelerator (falls back to live GitHub API when absent). The file is not on disk — `fork-cohort` has experienced consecutive Sunday failures (2026-06-08 and 2026-06-14 per morning-brief log). This is an implicit reference that never successfully populated, so MISSING is not fired per methodology. Tracking belongs to `skill-health`, not here. Suggested action: check `fork-cohort` run history.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. The fleet's defining structural fact this run — `chains: {}` is empty, so there are zero cross-skill chain edges; almost every file reference in the fleet is a producer touching its own state. That is why the surface area for silent upstream staleness is currently near-zero.*

*CI checkout note: every file's on-disk mtime is the checkout time (~09:09 UTC); freshness was scored against the authoritative durable signal — the date encoded in each `articles/{skill}-YYYY-MM-DD.md` filename and the content-date inside `.outputs/` and topic/state files. Same conclusion either way: nothing actionably stale.*
