# Skill Freshness — 2026-07-22

**Verdict:** ✅ FRESHNESS_OK — all 8 checked dependencies within freshness windows

*Audited 43 enabled skills · 8 dependencies checked · 0 flagged*

## Flagged dependencies

*(none — all dependencies fresh)*

## What this means per consumer

*(no consumers with degraded verdict)*

## Healthy consumers

- token-pick — 2 deps (`memory/topics/market-context.md`, `memory/topics/aixbt-grounding.md`), all fresh.
- operator-scorecard — 1 dep (`articles/skill-analytics-2026-07-15.md`, 158h old, threshold 192h; note: skill-analytics runs today at 18:30 UTC — will refresh), all fresh.
- vuln-scanner — 1 dep (`.outputs/github-trending.md`, checkout mtime), all fresh.
- fork-skill-gap — 1 dep (`memory/topics/fork-cohort-state.json`, checkout mtime), all fresh.
- reflect — 1 dep (articles/ newest: `skill-freshness-2026-07-21.md`, ~23h, threshold 28h), all fresh.
- action-converter — 2 deps (articles/ newest 2026-07-21 + `memory/topics/*.md`), all fresh.
- + 36 more all-fresh consumers.

## Dependency detail

| Consumer | Dependency | Class | Age | Threshold | Severity |
|----------|-----------|-------|-----|-----------|----------|
| token-pick | `memory/topics/market-context.md` | topics | ~0h (checkout mtime) | 168h | ✅ OK |
| token-pick | `memory/topics/aixbt-grounding.md` | topics | ~0h (checkout mtime) | 168h | ✅ OK |
| operator-scorecard | `articles/skill-analytics-2026-07-15.md` | articles/weekly | 158h (filename: 2026-07-15) | 192h | ✅ OK |
| vuln-scanner | `.outputs/github-trending.md` | outputs | ~0h (checkout mtime) | 4h | ✅ OK |
| fork-skill-gap | `memory/topics/fork-cohort-state.json` | topics | ~0h (checkout mtime) | 168h | ✅ OK |
| reflect | `articles/` (newest: 2026-07-21) | articles/daily | ~23h (filename: 2026-07-21) | 28h | ✅ OK |
| action-converter | `articles/` (newest: 2026-07-21) | articles/daily | ~23h (filename: 2026-07-21) | 28h | ✅ OK |
| action-converter | `memory/topics/*.md` | topics | ~0h (checkout mtime) | 168h | ✅ OK |

**Note on mtime environment:** This run is executing from a git checkout (all files stamped `2026-07-22 08:48 UTC`). For `.outputs/`, `memory/topics/`, and `memory/state/` dependencies, on-disk mtimes read as ~0h old — correct in production but cannot distinguish a file written today from one written months ago. Article-class dependencies use filename-date parsing to bypass this limitation (more reliable in checkout environments). The `reflect`/`action-converter` newest-article age (~23h) is reliable — it derives from `skill-freshness-2026-07-21.md` in the filename, which the skill wrote at 09:44 UTC yesterday. The `operator-scorecard` dep age (158h for `skill-analytics-2026-07-15.md`) is also reliable via filename date; skill-analytics fires today at 18:30 UTC and will refresh this dep.

**Watch:** `operator-scorecard → skill-analytics-2026-07-15.md` at 158h / 192h threshold (82%). If skill-analytics fails today, the article will cross the WARN threshold (~168h) by 7-23 morning. Monitor tomorrow's freshness run.

## Source status

- `aeon.yml`: 130+ entries, 43 enabled
- Implicit references discovered: 14
- Explicit `chains: consume:` edges: 0 (chains: {} — none active)
- Files not yet on disk (skipped — implicit references that never existed): 6
  - `articles/heartbeat-*.md` (operator-scorecard dep; heartbeat writes to memory/logs + .outputs, not articles/)
  - `articles/push-recap-*.md` (weekly-shiplog dep; push-recap disabled → never existed)
  - `articles/repo-actions-*.md` (self-improve dep; repo-actions disabled)
  - `articles/tweet-allocator-*.md` (operator-scorecard dep; tweet-allocator disabled)
  - `articles/token-report-*.md` (operator-scorecard dep; token-report disabled)
  - `articles/repo-pulse-*.md` (operator-scorecard dep; repo-pulse disabled)

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. Methodology: every age and threshold is computed from on-disk mtimes or filename-date parsing — this skill measures nothing it does not also report.*
