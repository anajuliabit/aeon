# Skill Freshness — 2026-07-07

**Verdict:** ✅ FRESHNESS_OK — all 43 enabled consumers' dependencies are within threshold

*Audited 43 enabled skills · 10 dependencies checked · 0 flagged*

## Flagged dependencies

*(None — all tracked dependencies are within their freshness thresholds.)*

## What this means per consumer

*(Omitted — no consumers with verdict ≠ OK.)*

## Healthy consumers

- token-pick — 1 dep (`memory/topics/market-context.md` ← market-context-refresh, daily), all fresh.
- vuln-scanner — 1 dep (`.outputs/github-trending.md` ← github-trending, daily), all fresh.
- fork-skill-gap — 1 dep (`memory/topics/fork-cohort-state.json` ← fork-cohort, weekly), all fresh.
- operator-scorecard — 1 dep (`articles/skill-analytics-2026-07-01.md` ← skill-analytics, weekly), all fresh.
- agent-buzz — 2 deps (`memory/topics/aixbt-grounding.md` · `memory/topics/aixbt-clusters.md` ← aixbt-pulse taxonomy, daily), all fresh.
- goal-tracker — 1 dep (`.outputs/aixbt-pulse.md` ← aixbt-pulse, daily), all fresh.
- security-digest — 1 dep (`articles/security-scan-2026-07-06.md` ← skill-security-scan, weekly), all fresh.
- fork-skill-digest — 1 dep (`articles/fork-cohort-2026-07-05.md` ← fork-cohort, weekly), all fresh.

+ 35 more all-fresh consumers.

## Source status

- `aeon.yml`: 43 entries parsed, 43 enabled (autoresearch counted — on_demand cadence; deps still audited as consumer)
- Implicit references discovered: 15 (5 filtered — 3 self-references, 2 implicit paths never on disk)
- Explicit `chains: consume:` edges: 0 (`chains: {}` — no active chains)
- Files not yet on disk (skipped — implicit references that never existed): 2 (`articles/fork-skill-gap-${today}.md`, `articles/operator-scorecard-${today}.md`)

**Note on mtime fidelity:** GitHub Actions `checkout` sets all file mtimes to the clone time (~08:52 UTC today), so all on-disk ages resolve to ~0 minutes. This is structurally correct per the mtime methodology but masks per-file production recency. The skill's staleness signal is reliable only when a producer *fails to write its file entirely* — in which case the file would not appear and would be flagged MISSING for explicit/canonical-pattern deps.

**Secondary content-date signal (informational, not part of mtime verdict):**
Four AIXBT-sourced files show 9-day content-age gap vs their daily producer cadence: `.outputs/aixbt-pulse.md`, `memory/topics/aixbt-grounding.md`, `memory/topics/aixbt-clusters.md`, `memory/topics/aixbt-chains.md` — all content-dated 2026-06-28. This matches the known aixbt-pulse dead-slot (day-9 at this run; last_success 6-28T21:21Z, ISS-019/020 cluster). PR #156 merged 2026-07-06 removed the `usepod_model:` blocker — next 09:00Z or 21:00Z tick today should clear the content gap. Similarly, `.outputs/github-trending.md` content is 2 days old (2026-07-05) vs 4h threshold, but its sole consumer (vuln-scanner, weekly Saturday) won't run until 2026-07-12 — gap expected to self-resolve before consumption.

**Dedup status:** Fingerprint identical to 2026-07-05 run (`da39a3ee5e6b4b0d3255bfef95601890afd80709`, 0 flagged rows), verdict unchanged (FRESHNESS_OK), last run 48h ago (< 7d window). Notification suppressed: FRESHNESS_NO_CHANGE. Note: 2026-07-06 run was absent (morning-slot gap, consistent with GH Actions cron catch-up from holiday weekend — logged in MEMORY.md).

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
