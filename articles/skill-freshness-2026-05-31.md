# Skill Freshness — 2026-05-31

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

- `aeon.yml`: 124 entries, 29 enabled (unchanged from 2026-05-30)
- Implicit references discovered: 2
- Explicit `chains: consume:` edges: 0 (all chain-enabled skills have `enabled: false`)
- Files not yet on disk (skipped — implicit references that never existed): 0

### Dependency detail (all OK, shown for completeness)

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles / weekly | ~2 min | 192 h | ✅ OK |
| skill-security-scan | `memory/state/security-scan.json` | state | ~2 min | 720 h | ✅ OK |

**Notes on discovery:**
- `articles/workflow-security-audit-2026-04-11.md`: referenced in skill-security-scan's threat-categories section as the canonical 2026-04-11 `messages.yml` injection incident. Producer `workflow-security-audit` (disabled, weekly schedule `0 16 * * 0`); file exists on disk. By on-disk mtime (git checkout timestamp) the file is ~2 min old — within the 192 h weekly threshold. Filename date is 2026-04-11 (50 days ago); if filename-date ageing is ever adopted this dep would surface as STALE.
- `memory/state/security-scan.json`: listed explicitly in skill-security-scan's Inputs table as the prior-scan delta baseline. `generated_at: 2026-05-25` (6 days = 144 h by embedded timestamp); by on-disk mtime ~2 min — well within the 720 h state threshold. Either way: OK.
- Fleet composition unchanged from 2026-05-30: 29 enabled consumers, same skill list. `skill-evals` ran today on its Sunday 06:00 UTC schedule (`articles/skill-evals-2026-05-31.md` now present), but skill-evals reads only its own prior output (self-ref, filtered). No new cross-skill deps introduced.
- `workflow-security-audit` is disabled and would normally run Sunday 16:00 UTC — since it's disabled, no new article was produced today; the 2026-04-11 artifact remains the only on-disk file for that producer.
- `fleet-control`'s `memory/state/fleet-control-state.json` is implicit and missing (skip). `market-context-refresh`'s `memory/topics/market-context.md` is a self-ref (consumer is the producer; last header date 2026-05-30, age 25 h < 168 h threshold, OK regardless). `skill-graph`'s `memory/topics/skill-graph-state.json` is a self-ref (`generated_at: 2026-05-28`, age 72 h < 168 h threshold, OK regardless).
- `operator-scorecard` references `articles/skill-analytics-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`, `articles/tweet-allocator-*.md` — all wildcard patterns for disabled or no-articles-output producers. Filtered per implicit-reference MISSING rule.
- `weekly-shiplog`'s `articles/push-recap-*.md` is implicit and no file exists (skip). `heartbeat`'s `articles/token-report-*.md` wildcard has no matching files (skip).
- Dedup: verdict identical to 2026-05-30 run (FRESHNESS_OK, fingerprint da39a3ee), prior run within 7-day window → FRESHNESS_NO_CHANGE. Notification suppressed.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
