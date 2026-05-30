# Skill Freshness — 2026-05-30

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

- `aeon.yml`: 124 entries, 29 enabled (unchanged from 2026-05-29)
- Implicit references discovered: 2
- Explicit `chains: consume:` edges: 0 (all chain-enabled skills have `enabled: false`)
- Files not yet on disk (skipped — implicit references that never existed): 0

### Dependency detail (all OK, shown for completeness)

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles / weekly | ~4 min | 192 h | ✅ OK |
| skill-security-scan | `memory/state/security-scan.json` | state | ~4 min | 720 h | ✅ OK |

**Notes on discovery:**
- `articles/workflow-security-audit-2026-04-11.md`: referenced in skill-security-scan's threat-categories table as the canonical 2026-04-11 `messages.yml` injection incident. Producer `workflow-security-audit` (disabled, weekly schedule `0 16 * * 0`); file exists on disk. By on-disk mtime (git checkout timestamp) the file is ~4 min old — within the 192 h weekly threshold. Filename date is 2026-04-11 (49 days ago); if filename-date ageing is ever adopted this dep would surface as STALE.
- `memory/state/security-scan.json`: listed explicitly in skill-security-scan's Inputs table as the prior-scan delta baseline. File exists; by on-disk mtime ~4 min — well within the 720 h state threshold.
- Fleet composition unchanged from 2026-05-29: 29 enabled consumers, same skill list. No new SKILL.md edits introducing trackable dependencies (git status confirms no SKILL.md modifications; .hl-cache and notify artifacts are the only pending changes).
- Today's chain activity (reppo-swarm ran twice): 10th mint on-chain (CHIP perp 0x71dfc07d, hash a3ea5a09); ISS-009 5th recurrence on 2nd chain run (trading-agent SKIP due to missing fenced reppo-plan block); ISS-012/ISS-013 RESOLVED; ISS-014 NEW (platform POST HTTP 500). None of this affects the freshness dep picture — all reppo skills have `enabled: false` standalone and do not enter the ENABLED consumer set.
- operator-scorecard references `articles/skill-analytics-*.md`, `articles/heartbeat-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`, `articles/tweet-allocator-*.md` — all wildcard patterns for disabled or no-articles-output producers. All filtered per implicit-reference MISSING rule.
- weekly-shiplog's `articles/push-recap-*.md` is implicit and missing (skip). weekly-shiplog runs Monday-only; today is Saturday — no new article produced.
- fleet-control's `memory/state/fleet-control-state.json` is implicit and missing (skip). market-context-refresh's `memory/topics/market-context.md` is a self-ref (consumer is the producer). skill-graph's `memory/topics/skill-graph-state.json` is a self-ref.
- Dedup: verdict identical to 2026-05-29 run (FRESHNESS_OK, fingerprint da39a3ee), prior run within 7-day window → FRESHNESS_NO_CHANGE. Notification suppressed.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
