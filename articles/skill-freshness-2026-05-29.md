# Skill Freshness — 2026-05-29

**Verdict:** ✅ FRESHNESS_OK — all 2 checked dependencies are within threshold across 29 enabled consumers

*Audited 29 enabled skills · 2 dependencies checked · 0 flagged*

## Flagged dependencies

*(None — no dependencies exceeded their freshness threshold.)*

## Healthy consumers

- action-converter — 0 deps, all fresh.
- agent-buzz — 0 deps, all fresh.
- autoresearch — 0 deps, all fresh.
- cost-report — 0 deps, all fresh.
- daily-routine — 0 deps, all fresh.
- defi-overview — 0 deps, all fresh.
- evening-recap — 0 deps, all fresh.
- fleet-control — 0 deps, all fresh.

+ 21 more all-fresh consumers. (github-trending, goal-tracker, heartbeat, market-context-refresh, morning-brief, operator-scorecard, reflect, search-skill, self-improve, skill-analytics, skill-evals, skill-freshness, skill-graph, skill-health, skill-security-scan [2 deps OK], skill-update-check, token-alert, token-pick, vibecoding-digest, weekly-review, weekly-shiplog)

## Source status

- `aeon.yml`: 124 entries, 29 enabled (+8 since 2026-05-28: agent-buzz, daily-routine, fleet-control, market-context-refresh, skill-graph, token-pick, vibecoding-digest, weekly-shiplog)
- Implicit references discovered: 2
- Explicit `chains: consume:` edges: 0 (all chain-enabled skills have `enabled: false`)
- Files not yet on disk (skipped — implicit references that never existed): 0

### Dependency detail (all OK, shown for completeness)

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles / weekly | ~4 min | 192 h | ✅ OK |
| skill-security-scan | `memory/state/security-scan.json` | state | ~4 min | 720 h | ✅ OK |

**Notes on discovery:**
- `articles/workflow-security-audit-2026-04-11.md`: referenced in skill-security-scan's threat-categories table as the canonical 2026-04-11 `messages.yml` injection incident. Producer `workflow-security-audit` (disabled, weekly schedule `0 16 * * 0`); file exists on disk. By on-disk mtime (git checkout timestamp) the file is ~4 min old — within the 192 h weekly threshold. Filename date is 2026-04-11 (48 days); if filename-date ageing is ever adopted this dep would surface as STALE.
- `memory/state/security-scan.json`: listed explicitly in skill-security-scan's Inputs table as the prior-scan delta baseline. File exists; by on-disk mtime ~4 min — well within the 720 h state threshold.
- 8 new consumers added since yesterday (commit `f3414fa chore(chain): reppo-swarm success`): agent-buzz, daily-routine, fleet-control, market-context-refresh, skill-graph, token-pick, vibecoding-digest, weekly-shiplog. None introduce new trackable dependencies — fleet-control's `memory/state/fleet-control-state.json` is implicit and missing (skip per MISSING rule), market-context-refresh's `memory/topics/market-context.md` is a self-ref (consumer writes this file), skill-graph's `memory/topics/skill-graph-state.json` is a self-ref, weekly-shiplog's `articles/push-recap-*.md` is implicit and missing (skip).
- operator-scorecard references `articles/skill-analytics-*.md`, `articles/heartbeat-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`, `articles/tweet-allocator-*.md`, `articles/fork-contributor-leaderboard-*.md` — all wildcard patterns. skill-analytics (enabled, weekly-Wednesday) has not yet produced an article on disk; heartbeat is a daily producer with no articles directory output. All filtered per implicit-reference MISSING rule.
- action-converter's generic `memory/topics/` read and reflect's generic `articles/` browse are directory-level operations — no extractable producer name, omitted from dep table per methodology.
- Dedup: verdict identical to 2026-05-28 run (FRESHNESS_OK, fingerprint da39a3ee), prior run within 7-day window → FRESHNESS_NO_CHANGE. Notification suppressed.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
