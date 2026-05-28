# Skill Freshness — 2026-05-28

**Verdict:** ✅ FRESHNESS_OK — all 2 checked dependencies are within threshold across 21 enabled consumers

*Audited 21 enabled skills · 2 dependencies checked · 0 flagged*

## Flagged dependencies

*(None — no dependencies exceeded their freshness threshold.)*

## Healthy consumers

- action-converter — 0 deps, all fresh.
- autoresearch — 0 deps, all fresh.
- cost-report — 0 deps, all fresh.
- defi-overview — 0 deps, all fresh.
- evening-recap — 0 deps, all fresh.
- github-trending — 0 deps, all fresh.
- goal-tracker — 0 deps, all fresh.
- heartbeat — 0 deps, all fresh.

+ 13 more all-fresh consumers. (morning-brief, operator-scorecard, reflect, search-skill, self-improve, skill-analytics, skill-evals, skill-freshness, skill-health, skill-security-scan [2 deps OK], skill-update-check, token-alert, weekly-review)

## Source status

- `aeon.yml`: 124 entries, 21 enabled
- Implicit references discovered: 2
- Explicit `chains: consume:` edges: 0 (all chain-enabled skills have `enabled: false`)
- Files not yet on disk (skipped — implicit references that never existed): 0

### Dependency detail (all OK, shown for completeness)

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles / weekly | ~1 min | 192 h | ✅ OK |
| skill-security-scan | `memory/state/security-scan.json` | state | ~1 min | 720 h | ✅ OK |

**Notes on discovery:**
- `articles/workflow-security-audit-2026-04-11.md`: referenced in skill-security-scan's threat-categories table as the canonical 2026-04-11 `messages.yml` injection incident. Producer `workflow-security-audit` (disabled, weekly schedule `0 16 * * 0`); file exists on disk. By on-disk mtime (git checkout timestamp) the file is ~1 min old — within the 192 h weekly threshold. Filename date is 2026-04-11 (47 days); if filename-date ageing is ever adopted this dep would surface as STALE.
- `memory/state/security-scan.json`: listed explicitly in skill-security-scan's Inputs table as the prior-scan delta baseline. Content `generated_at: 2026-05-25`; by on-disk mtime ~1 min — well within the 720 h state threshold.
- operator-scorecard references `articles/skill-analytics-*.md`, `articles/heartbeat-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`, `articles/tweet-allocator-*.md`, `articles/fork-contributor-leaderboard-*.md` — all wildcard patterns. skill-analytics and heartbeat are enabled producers but have no matching article files on disk; all others are disabled producers. All filtered per implicit-reference MISSING rule (no canonical-pattern or explicit chain-consume match).
- action-converter's generic `memory/topics/` read and reflect's generic `articles/` browse are directory-level operations — no extractable producer name, omitted from dep table per methodology.
- Dedup: verdict identical to 2026-05-27 run (FRESHNESS_OK, fingerprint da39a3ee), prior run within 7-day window → FRESHNESS_NO_CHANGE. Notification suppressed.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
