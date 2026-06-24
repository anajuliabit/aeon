# Skill Freshness — 2026-06-24

**Verdict:** ⚠️ FRESHNESS_WARN — 1 cross-skill dependency past its threshold; 7 of 8 clean.

*Audited 44 enabled skills · 8 cross-skill dependencies checked · 1 flagged*

## Flagged dependencies

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| operator-scorecard | `articles/skill-analytics-*.md` | articles/weekly | 336h (14d) | ⚠️ WARN |

(Sorted by severity desc, then consumer name. OK rows omitted.)

## What this means per consumer

> **operator-scorecard** — depends on 5 cross-skill article files; 1 flagged. Worst: `articles/skill-analytics-*.md` — resolved to `skill-analytics-2026-06-10.md`, last updated 14 days ago (threshold 192h / 8d, class articles/weekly). Producer `skill-analytics` is weekly (`30 18 * * 3` — Wednesday). No `skill-analytics-2026-06-17.md` exists — the expected run on 2026-06-17 did not produce an article. `skill-analytics-2026-06-24.md` has not yet been written; today's run is scheduled for 18:30 UTC (~10.5h from now). If it succeeds, the gap auto-clears for next Monday's operator-scorecard. Risk: `skill-analytics` sr=9% (sandbox-truncation cluster, ISS-019). Suggested action: Check `skill-analytics` run history with `./scripts/skill-runs --skill skill-analytics --hours 168`. If it ran on 2026-06-17 but failed without writing an article, flag for repair.

## Healthy consumers

- vuln-scanner — 1 dep (`.outputs/github-trending.md`), OK by checkout mtime. Content is effectively empty due to consecutive github-trending failures per cron-state. vuln-scanner next runs Saturday 2026-06-28 — not flagged: MISSING only fires on canonical chain/article edges, not optional fallback sources.
- fork-skill-gap — 1 dep (`memory/topics/fork-cohort-state.json`), present and OK by checkout mtime.
- operator-scorecard (other refs) — 4 refs from disabled producers (`articles/heartbeat-*.md`, `articles/tweet-allocator-*.md`, `articles/token-report-*.md`, `articles/repo-pulse-*.md`): all `enabled: false` or no file on disk. Exempt from MISSING per methodology.
- heartbeat — 1 dep (`articles/token-report-*.md`), disabled producer, no file on disk, exempt.
- + 39 more enabled consumers with only self-references, no cross-skill file dependencies, or no file dependencies at all. Out of scope per step 4 filtering.

## Source status

- `aeon.yml`: 130 entries parsed, 44 enabled
- `chains:` blocks: **none active** (`chains: {}`) → 0 explicit `consume:` edges
- Implicit references discovered (across all enabled SKILL.md files): 8 distinct cross-skill (consumer, path) pairs after self-reference and code-example filtering
- Explicit `chains: consume:` edges: 0
- Disabled-producer references: 5 (operator-scorecard → heartbeat, tweet-allocator, token-report, repo-pulse; heartbeat → token-report — all `enabled: false` or no matching file, exempt from MISSING)
- Implicit references not flagged (absent optional files, never-populated paths, or hardcoded historical citations): 1 (`skill-security-scan` → `articles/workflow-security-audit-2026-04-11.md`, correctly excluded as a documentation reference, not a runtime file read)

## Dedup note

**Status: FRESHNESS_NO_CHANGE.** Fingerprint `d522755e4af35478ef8cd44c558f87e1413fb78c` matches prior run (2026-06-23T08:23:00Z, < 7 days ago). Same flagged triple: `operator-scorecard:articles/skill-analytics-*.md:WARN`. Age advanced from 312h (13d) to 336h (14d) — still within the WARN band (192h–384h). Severity band unchanged → fingerprint unchanged. Notification suppressed. Re-emits 2026-06-28 if still unresolved (7-day window from first_seen_at 2026-06-21T14:39Z).

**first_seen_at escalation check:** `operator-scorecard:articles/skill-analytics-*.md` first crossed threshold 2026-06-21T14:39Z (~66h ago as of 08:00 UTC). Escalation to STALE fires at 168h (7 days) — not yet reached. Running clock: 66h of 168h.

**STALE threshold crossing:** If skill-analytics fails today, age reaches 384h (2× threshold = STALE boundary) at approximately 2026-06-26 18:30 UTC. The 2026-06-25 08:00 skill-freshness run would still score WARN (~360h). The 2026-06-26 08:00 run would score WARN (~374h). Crossing to STALE would trigger a fingerprint change and resume notification.

## CI checkout note

All on-disk mtimes equal the checkout time (~08:42 UTC). Freshness scored against the authoritative durable signal: date encoded in `articles/{skill}-YYYY-MM-DD.md` filenames. For `.outputs/` and `memory/topics/` files (no date in filename), mtime is the only available signal — those score OK by definition in a fresh checkout. The skill-analytics WARN is derivable from the filename alone (`2026-06-10` vs today `2026-06-24` = 336h).

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches silent-staleness the other two cannot: a consumer reading an overaged file with no API errors and a 100% own-run pass rate. Fleet defining fact this run: `chains: {}` keeps cross-skill surface area near-zero. The sole live gap — operator-scorecard reading a skill-analytics article now 14 days old — clears automatically if skill-analytics succeeds today at 18:30 UTC. Risk: sr=9% (ISS-019, sandbox-truncation cluster). Monitor.*
