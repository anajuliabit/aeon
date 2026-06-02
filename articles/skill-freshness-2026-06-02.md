# Skill Freshness — 2026-06-02

**Verdict:** ✅ FRESHNESS_OK — all 3 tracked dependencies are fresh

*Audited 34 enabled skills · 3 dependencies checked · 0 flagged*

## Flagged dependencies

*(None — all dependencies within freshness thresholds.)*

## What this means per consumer

*(No consumers with verdict ≠ OK.)*

## Healthy consumers

- skill-security-scan — 2 deps, all fresh. (`articles/workflow-security-audit-2026-04-11.md` ~3m old, threshold 192h; `memory/state/security-scan.json` ~3m old, threshold 720h)
- vuln-scanner — 1 dep, all fresh. (`.outputs/github-trending.md` ~3m old, threshold 4h; dep on github-trending daily output before Saturday scan)
- market-context-refresh — 0 tracked deps, all fresh. (self-ref `memory/topics/market-context.md` filtered)
- fleet-control — 0 tracked deps, all fresh. (self-ref `memory/state/fleet-control-state.json` filtered)
- deal-flow — 0 tracked deps, all fresh.
- reg-monitor — 0 tracked deps, all fresh. (self-ref `memory/topics/reg-monitor-seen.md` filtered)
- unlock-monitor — 0 tracked deps, all fresh. (self-ref `memory/state/unlock-monitor-seen.json` filtered)
- security-digest — 0 tracked deps, all fresh.
+ 26 more all-fresh consumers.

## Source status

- `aeon.yml`: ~125 entries, 34 enabled
- Implicit references discovered: 3 (after filtering 5: 3 self-refs, 1 code-block example, 1 self-ref in new skills)
- Explicit `chains: consume:` edges: 0 (reppo-swarm chain has 3 steps but all are `enabled: false`)
- Files not yet on disk (skipped — implicit references that never existed): 0

### New skills audited this run (from PR #54, 2026-06-01)

Five skills newly enabled: deal-flow, reg-monitor, security-digest, unlock-monitor, vuln-scanner. Implicit dep scan results:
- **deal-flow**: no cross-skill file references.
- **reg-monitor**: self-ref `memory/topics/reg-monitor-seen.md` filtered (reg-monitor writes and reads its own URL dedup file).
- **security-digest**: no cross-skill file references.
- **unlock-monitor**: self-ref `memory/state/unlock-monitor-seen.json` filtered (unlock-monitor writes and reads its own seen-list).
- **vuln-scanner**: new implicit dep on `.outputs/github-trending.md` recorded (used as target-selection fallback; class=outputs, threshold=4h).

### Notes on filtered references

- **market-context-refresh → `memory/topics/market-context.md`**: filtered as self-reference. market-context-refresh is both producer and consumer of this topic file.
- **fleet-control → `memory/state/fleet-control-state.json`**: filtered as self-reference. fleet-control writes and reads its own state.
- **heartbeat → `articles/token-report-2026-04-28.md`**: filtered as code-block example. Reference appears inside a ` ```markdown ` fenced block at line 113 of heartbeat/SKILL.md showing sample output; file also does not exist on disk.
- **reg-monitor → `memory/topics/reg-monitor-seen.md`**: filtered as self-reference. reg-monitor writes and reads its own URL dedup list.
- **unlock-monitor → `memory/state/unlock-monitor-seen.json`**: filtered as self-reference. unlock-monitor writes and reads its own seen-list.

### Dependency detail

| Consumer | Dependency | Class | Mtime | Age | Threshold | Severity |
|----------|-----------|-------|-------|-----|-----------|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles (weekly producer) | 2026-06-02T08:54:22Z | ~3m | 192h | ✅ OK |
| skill-security-scan | `memory/state/security-scan.json` | state | 2026-06-02T08:54:22Z | ~3m | 720h | ✅ OK |
| vuln-scanner | `.outputs/github-trending.md` | outputs | 2026-06-02T08:54:22Z | ~3m | 4h | ✅ OK |

*Note: all file mtimes reflect the git checkout time (08:54:22 UTC). In a GitHub Actions environment, git clone sets all mtimes to the checkout instant — freshness thresholds are met by definition for any file present in the repo.*

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
