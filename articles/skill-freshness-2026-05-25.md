# Skill Freshness — 2026-05-25

**Verdict:** ✅ FRESHNESS_OK — all 14 tracked dependencies are within their freshness windows

*Audited 21 enabled skills · 14 dependencies checked · 0 flagged*

## Flagged dependencies

*(None — no dependencies exceeded their freshness threshold.)*

## What this means per consumer

No consumer has a stale or missing upstream dependency this run.

## Healthy consumers

- morning-brief — 0 tracked deps, all fresh.
- github-trending — 0 tracked deps, all fresh.
- token-alert — 0 tracked deps, all fresh.
- defi-overview — 0 tracked deps, all fresh.
- search-skill — 0 tracked deps, all fresh.
- skill-security-scan — 0 tracked deps (documentary refs to `articles/workflow-security-audit-2026-04-11.md` excluded as non-runtime references).
- action-converter — 4 deps (`memory/topics/crypto.md`, `fleet.md`, `last30-bitcoin.md`, `reppo.md`), all fresh (last git commit ~10.8h ago, well within 168h threshold).
- autoresearch — 0 tracked deps (on_demand, skip).
+ 13 more all-healthy consumers.

## Source status

- `aeon.yml`: 70 entries, 21 enabled
- Implicit references discovered: 14
- Explicit `chains: consume:` edges: 0 (reppo-swarm chain skills all `enabled: false`)
- Files not yet on disk (skipped — implicit references that never existed): 9

## Methodology note

*GitHub Actions checkout resets all file mtimes to the checkout timestamp (~08:20 UTC today). On-disk mtime analysis therefore shows all files as ≤ 1h old. For article files, filename-date provides the staleness signal: `skill-freshness-2026-05-24.md` (24h, OK vs 28h daily threshold), `skill-evals-2026-05-24.md` (1d, OK vs 192h weekly threshold), `competitor-launch-radar-2026-05-21.md` (4d = 96h, OK vs 192h weekly threshold). For topic files, git log confirms last modification at 2026-05-24T21:30:35Z (~10.8h ago, well within 168h threshold). The mtime-based verdict (FRESHNESS_OK) is consistent with the filename-date and git-log analysis.*

## Dedup status

Fingerprint `da39a3ee5e6b4b0d3255bfef95601890afd80709` (SHA1 of empty flagged set) is identical to prior run (2026-05-24, within 7-day window). Notification suppressed: **FRESHNESS_NO_CHANGE**.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
