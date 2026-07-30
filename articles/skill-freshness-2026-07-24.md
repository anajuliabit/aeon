# Skill Freshness — 2026-07-24

**Verdict:** ✅ FRESHNESS_OK — all 8 tracked dependencies within threshold

*Audited 43 enabled skills · 8 dependencies checked · 0 flagged*

## Flagged dependencies

*(none — all dependencies OK)*

## What this means per consumer

All consumers with identified file dependencies are current. No action needed.

## Healthy consumers

- skill-security-scan — 3 deps, all fresh. (`memory/state/security-scan.json` · `articles/workflow-security-audit-2026-04-11.md` · `articles/security-scan-${today}.md` → `security-scan-2026-07-20.md`)
- vuln-scanner — 1 dep, all fresh. (`.outputs/github-trending.md`)
- aixbt-pulse — 3 deps, all fresh. (`memory/topics/aixbt-grounding.md` · `memory/topics/aixbt-clusters.md` · `memory/topics/aixbt-chains.md`)
- market-context-refresh — 1 dep, all fresh. (`memory/topics/market-context.md`)
- + 39 more all-fresh consumers with no identified implicit file dependencies.

## Source status

- `aeon.yml`: 115 entries parsed, 43 enabled
- Implicit references discovered: 8
- Explicit `chains: consume:` edges: 0 (chains: {} — no active chains)
- Files not yet on disk (skipped — implicit references that never existed): 0

### Dependency detail (all OK)

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| skill-security-scan | `memory/state/security-scan.json` | state | ~5m | 30d | ✅ OK |
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles (weekly) | ~5m | 8d | ✅ OK |
| skill-security-scan | `articles/security-scan-2026-07-20.md` | articles (weekly) | ~5m | 8d | ✅ OK |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~5m | 4h | ✅ OK |
| aixbt-pulse | `memory/topics/aixbt-grounding.md` | topics | ~5m | 7d | ✅ OK |
| aixbt-pulse | `memory/topics/aixbt-clusters.md` | topics | ~5m | 7d | ✅ OK |
| aixbt-pulse | `memory/topics/aixbt-chains.md` | topics | ~5m | 7d | ✅ OK |
| market-context-refresh | `memory/topics/market-context.md` | topics | ~5m | 7d | ✅ OK |

*Note: All on-disk mtimes reflect the repository checkout time (2026-07-24 08:44:59 UTC). In a GitHub Actions fresh-checkout environment, file mtimes are set at clone time, making all files appear maximally fresh. No dependency exceeded any threshold.*

*Dedup: verdict and flagged-set fingerprint (da39a3ee) identical to 2026-07-23 run (09:48Z, 23h ago, within 7d window) → FRESHNESS_NO_CHANGE. Notification suppressed.*

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
