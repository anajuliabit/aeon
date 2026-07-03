# Skill Freshness — 2026-07-03

**Verdict:** ✅ FRESHNESS_OK — all 43 enabled consumers' dependencies are within threshold

*Audited 43 enabled skills · 3 dependencies checked · 0 flagged*

## Flagged dependencies

*(None — all tracked dependencies are within their freshness thresholds.)*

## What this means per consumer

*(Omitted — no consumers with verdict ≠ OK.)*

## Healthy consumers

- token-pick — 1 dep (`memory/topics/market-context.md` ← market-context-refresh, daily), all fresh.
- vuln-scanner — 1 dep (`.outputs/github-trending.md` ← github-trending, daily), all fresh.
- fork-skill-gap — 1 dep (`memory/topics/fork-cohort-state.json` ← fork-cohort, weekly), all fresh.
- market-context-refresh — 0 tracked cross-skill deps (self-state only), all fresh.
- aixbt-pulse — 0 tracked cross-skill deps (self-state only), all fresh.
- skill-security-scan — 0 tracked cross-skill deps (self-state only), all fresh.
- unlock-monitor — 0 tracked cross-skill deps (self-state only), all fresh.
- reg-monitor — 0 tracked cross-skill deps (self-state only), all fresh.

+ 35 more all-fresh consumers.

## Source status

- `aeon.yml`: 43 entries parsed, 43 enabled (autoresearch counted — on_demand cadence; its deps still audited as a consumer)
- Implicit references discovered: 10 (7 filtered as self-references, 3 surviving as cross-skill deps)
- Explicit `chains: consume:` edges: 0 (`chains: {}` — no active chains)
- Files not yet on disk (skipped — implicit references that never existed): 0

**Note on mtime fidelity:** GitHub Actions `checkout` sets all file mtimes to the clone time (~08:28 UTC today), so all on-disk ages resolve to ~3 minutes. This is structurally correct per the mtime methodology but masks per-file production recency. The skill's staleness signal is reliable only when a producer *fails to write its file entirely* — in which case the file would not appear and would be flagged MISSING for explicit/canonical-pattern deps.

**Dedup status:** Fingerprint identical to 2026-07-02 run (`da39a3ee5e6b4b0d3255bfef95601890afd80709`, 0 flagged rows), verdict unchanged (FRESHNESS_OK), last run 24h ago (< 7d window). Notification suppressed: FRESHNESS_NO_CHANGE.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
