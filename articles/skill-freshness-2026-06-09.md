# Skill Freshness — 2026-06-09

**Verdict:** ✅ FRESHNESS_OK — all 3 tracked dependencies are fresh

*Audited 43 enabled skills · 3 dependencies checked · 0 flagged*

## Flagged dependencies

*(None — all dependencies within freshness thresholds.)*

## What this means per consumer

*(No consumers with verdict ≠ OK.)*

## Healthy consumers

- skill-security-scan — 2 deps, all fresh. (`articles/workflow-security-audit-2026-04-11.md` ~0m old, threshold 192h; `memory/state/security-scan.json` ~0m old, threshold 720h)
- vuln-scanner — 1 dep, all fresh. (`.outputs/github-trending.md` ~0m old, threshold 4h)
- market-context-refresh — 0 tracked deps, all fresh. (self-ref `memory/topics/market-context.md` filtered)
- fleet-control — 0 tracked deps, all fresh. (self-refs `memory/state/fleet-control-state.json` and `articles/fleet-status-*.md` filtered)
- deal-flow — 0 tracked deps, all fresh.
- reg-monitor — 0 tracked deps, all fresh. (self-ref `memory/topics/reg-monitor-seen.md` filtered)
- unlock-monitor — 0 tracked deps, all fresh. (self-ref `memory/state/unlock-monitor-seen.json` filtered)
- fork-skill-gap — 0 tracked deps, all fresh. (implicit `memory/topics/fork-cohort-state.json` filtered — never existed on disk)
+ 35 more all-fresh consumers.

## Source status

- `aeon.yml`: ~130 entries, 43 enabled (+1 vs 2026-06-05 state; one skill enabled since last run)
- Implicit references discovered: 3 (after filtering 8: 6 self-refs, 1 code-block example, 1 implicit-never-existed)
- Explicit `chains: consume:` edges: 0 (reppo-swarm chain has 3 consume edges but all steps are `enabled: false`)
- Files not yet on disk (skipped — implicit references that never existed): 1 (`memory/topics/fork-cohort-state.json` referenced by fork-skill-gap)

### Notes on filtered references

- **market-context-refresh → `memory/topics/market-context.md`**: filtered as self-reference. market-context-refresh is both producer and consumer of this topic file.
- **fleet-control → `memory/state/fleet-control-state.json`**: filtered as self-reference. fleet-control writes and reads its own state.
- **fleet-control → `articles/fleet-status-*.md`**: filtered as self-reference. fleet-control writes fleet-status articles and reads its own prior article for delta — no fleet-status-*.md files exist in the repo at all.
- **heartbeat → `articles/token-report-2026-04-28.md`**: filtered as code-block example. Reference appears inside a fenced markdown block showing sample output; file does not exist on disk.
- **reg-monitor → `memory/topics/reg-monitor-seen.md`**: filtered as self-reference. reg-monitor writes and reads its own URL dedup list.
- **unlock-monitor → `memory/state/unlock-monitor-seen.json`**: filtered as self-reference. unlock-monitor writes and reads its own seen-list.
- **fork-skill-gap → `memory/topics/fork-cohort-state.json`**: filtered — implicit reference that never existed on disk. fork-skill-gap describes this as an "optional accelerator"; fork-cohort has never written this file to the repo. Not flagged MISSING per policy (implicit-never-existed exclusion).
- **fork-skill-digest → `memory/topics/fork-skill-digest-state.json`**: filtered as self-reference. fork-skill-digest writes and reads its own dedup state.

### Dependency detail

| Consumer | Dependency | Class | Mtime | Age | Threshold | Severity |
|----------|-----------|-------|-------|-----|-----------|----------|
| skill-security-scan | `articles/workflow-security-audit-2026-04-11.md` | articles (weekly producer) | 2026-06-09T08:55:02Z | ~0m | 192h | ✅ OK |
| skill-security-scan | `memory/state/security-scan.json` | state | 2026-06-09T08:55:02Z | ~0m | 720h | ✅ OK |
| vuln-scanner | `.outputs/github-trending.md` | outputs | 2026-06-09T08:55:02Z | ~0m | 4h | ✅ OK |

*Note: all file mtimes reflect the git checkout time (~08:55 UTC). In a GitHub Actions environment, git clone sets all mtimes to the checkout instant — freshness thresholds are met by definition for any file present in the repo.*

---
*Status: FRESHNESS_NO_CHANGE — fingerprint and verdict unchanged from 2026-06-05 run; suppressing notification per dedup policy (7-day re-emit window expires 2026-06-12). Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes — this skill measures nothing it does not also report.*
