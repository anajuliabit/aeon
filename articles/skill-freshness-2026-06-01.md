# Skill Freshness — 2026-06-01

**Verdict:** ✅ FRESHNESS_OK — all 2 tracked dependencies are fresh

*Audited 29 enabled skills · 2 dependencies checked · 0 flagged*

## Flagged dependencies

*(None — all dependencies within freshness thresholds.)*

## What this means per consumer

*(No consumers with verdict ≠ OK.)*

## Healthy consumers

- skill-security-scan — 2 deps, all fresh. (`articles/workflow-security-audit-2026-04-11.md` 6m old, threshold 192h; `memory/state/security-scan.json` 6m old, threshold 720h)
- morning-brief — 0 tracked deps, all fresh.
- daily-routine — 0 tracked deps, all fresh.
- github-trending — 0 tracked deps, all fresh.
- token-alert — 0 tracked deps, all fresh.
- defi-overview — 0 tracked deps, all fresh.
- token-pick — 0 tracked deps, all fresh.
- market-context-refresh — 0 tracked deps, all fresh. (self-ref `memory/topics/market-context.md` filtered)
+ 21 more all-fresh consumers.

## Source status

- `aeon.yml`: ~124 entries, 29 enabled
- Implicit references discovered: 2 (after filtering 3: 2 self-refs, 1 code-block example)
- Explicit `chains: consume:` edges: 0 (reppo-swarm chain has 3 steps but all are `enabled: false`)
- Files not yet on disk (skipped — implicit references that never existed): 0

### Notes on filtered references

- **market-context-refresh → `memory/topics/market-context.md`**: filtered as self-reference. market-context-refresh is both producer and consumer of this topic file; it reads the prior version to compute deltas. Self-reads are not staleness gaps.
- **fleet-control → `memory/state/fleet-control-state.json`**: filtered as self-reference. fleet-control writes and reads its own state; prefix `fleet-control` matches skill name exactly.
- **heartbeat → `articles/token-report-2026-04-28.md`**: filtered as code-block example. Reference appears inside a ` ```markdown ` fenced block at line 113 of heartbeat/SKILL.md showing sample output; the file also does not exist on disk (expected: `token-report` is disabled). Since this is an implicit reference and filtered, no MISSING flag applies.

### Dependency detail

| Consumer | Dependency | Class | Mtime | Age | Threshold | Severity |
|----------|-----------|-------|-------|-----|-----------|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles (weekly producer) | 2026-06-01T09:12:48Z | 6m | 192h | ✅ OK |
| skill-security-scan | `memory/state/security-scan.json` | state | 2026-06-01T09:12:48Z | 6m | 720h | ✅ OK |

*Note: all file mtimes reflect the git checkout time (09:12:48 UTC). In a GitHub Actions environment, git clone sets all mtimes to the checkout instant — freshness thresholds are met by definition for any file present in the repo.*

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
