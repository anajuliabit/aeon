# Skill Freshness — 2026-07-08

**Verdict:** ✅ FRESHNESS_OK — all 43 enabled consumers' dependencies are within threshold

*Audited 43 enabled skills · 4 dependencies checked · 0 flagged*

## Flagged dependencies

*(None — all tracked dependencies are within their freshness thresholds.)*

## What this means per consumer

*(Omitted — no consumers with verdict ≠ OK.)*

## Healthy consumers

- token-pick — 1 dep (`memory/topics/market-context.md` ← market-context-refresh, daily), all fresh.
- vuln-scanner — 1 dep (`.outputs/github-trending.md` ← github-trending, daily), all fresh.
- operator-scorecard — 1 dep (`articles/skill-analytics-2026-07-01.md` ← skill-analytics, weekly), all fresh.
- fork-skill-gap — 1 dep (`memory/topics/fork-cohort-state.json` ← fork-cohort, weekly), all fresh.

+ 39 more all-fresh consumers.

## Source status

- `aeon.yml`: 43 entries parsed, 43 enabled (autoresearch counted — on_demand cadence; deps still audited as consumer)
- Implicit references discovered: ~22 raw (18 filtered — 11 self-references, 7 implicit paths never on disk from disabled producers)
- Explicit `chains: consume:` edges: 0 (`chains: {}` — no active chains)
- Files not yet on disk (skipped — implicit references from disabled-skill producers): 7 (`articles/repo-actions-*.md`, `articles/push-recap-*.md`, `articles/repo-pulse-*.md`, `articles/token-report-*.md`, `articles/tweet-allocator-*.md`, `articles/fork-contributor-leaderboard-*.md`, `articles/distribute-tokens-*.md`)

**Methodology note vs prior run:** Today's dep catalog (4 surviving deps) differs from 2026-07-07's (10 deps). Fresh SKILL.md grep this run applied the spec filters strictly: agent-buzz, goal-tracker, security-digest, and fork-skill-digest were found to not explicitly reference the upstream files the prior run attributed to them. Prior run inferred those edges from context/documentation rather than SKILL.md file-reference extraction. Today's narrower catalog is the authoritative count. Flagged-row fingerprint is unaffected (0 flagged in both runs → same SHA1).

**Note on mtime fidelity:** GitHub Actions `checkout` sets all file mtimes to the clone time (~09:02 UTC today), so all on-disk ages resolve to ~2 minutes. This is structurally correct per the mtime methodology but masks per-file production recency. The skill's staleness signal is reliable only when a producer *fails to write its file entirely* — in which case the file would not appear and would be flagged MISSING for explicit/canonical-pattern deps.

**Secondary content-date signal (informational, not part of mtime verdict):**

- **AIXBT dead-slot day 10** — `.outputs/aixbt-pulse.md`, `memory/topics/aixbt-grounding.md`, `memory/topics/aixbt-clusters.md`, `memory/topics/aixbt-chains.md` all content-dated 2026-06-28 (~228h = 9.5d). Producer aixbt-pulse has no enabled consumer reading these files per today's dep scan (agent-buzz and goal-tracker do not explicitly reference them in their SKILL.md). Tracked as an awareness signal: per MEMORY.md, ISS-019/020 cluster active, 7-07 09:00Z and 21:00Z ticks both missed despite PR #156 removing `usepod_model:` drift.

- **`.outputs/github-trending.md`** — content-dated 2026-07-05 (~72h old). Consumer vuln-scanner (weekly Saturday Jul 12) will not run until the gap is 7d — well within the 4h .outputs threshold at that point the content *is* stale relative to class. Gap will persist through the 7d window. If github-trending misses its daily run before Jul 12, vuln-scanner will consume 7-day-old trending data. Watch if github-trending shows failure in skill-health.

- **`memory/topics/market-context.md`** — content-dated 2026-07-07 (~21h). market-context-refresh ran yesterday 13:00 UTC. OK ✓

- **`articles/skill-analytics-2026-07-01.md`** — content-dated 2026-07-01 (183h = 7d 15h vs 192h weekly threshold). Skill-analytics runs Wednesday 18:30 UTC — will refresh today at 18:30 UTC, clearing the threshold boundary. OK (barely) ✓

**Dedup status:** Fingerprint unchanged from 2026-07-07 run (`da39a3ee5e6b4b0d3255bfef95601890afd80709`, 0 flagged rows), verdict unchanged (FRESHNESS_OK), last run ~24h ago (< 7d window). Notification suppressed: FRESHNESS_NO_CHANGE. (FRESHNESS_OK also suppresses notification independently of dedup.)

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
