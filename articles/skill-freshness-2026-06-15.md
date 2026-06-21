# Skill Freshness — 2026-06-15

**Verdict:** ✅ FRESHNESS_OK — no enabled consumer is about to read an actionably-stale file.

*Audited 44 enabled skills · 8 cross-skill dependencies checked · 0 flagged*

## Flagged dependencies

None. Every cross-skill upstream an enabled consumer reads is within its freshness window.

| Consumer | Dependency | Class | Age | Severity |
|----------|-----------|-------|-----|----------|
| — | — | — | — | ✅ OK |

## What this means per consumer

No consumer scored above OK, so there are no per-consumer escalation paragraphs this run. The two relationships worth recording explicitly (both benign):

> **vuln-scanner** — depends on 1 cross-skill file: `.outputs/github-trending.md` (declared in its `depends_on:` frontmatter). The output currently holds github-trending's **06-14** staging line. Producer `github-trending` is daily (09:00 UTC); consumer `vuln-scanner` runs **Saturdays only** (`0 16 * * 6`). Today is Monday — vuln-scanner does not run, and by its next Saturday tick the daily producer will have refreshed the file. The skill also carries a live GitHub-trending-API fallback if the chained output is empty or stale. No gap. Suggested action: none.

> **skill-security-scan** — references `articles/workflow-security-audit-2026-04-11.md`. This is a **hardcoded historical citation** (the canonical April messages.yml injection-incident pattern), not a freshness-sensitive read. The file exists. This is the textbook implicit-reference false-positive the methodology's "best-effort, false positives tolerated" clause is designed to exclude — it is correctly **not** flagged.

## Healthy consumers

All 44 enabled consumers resolve to OK. The only ones with genuine cross-skill (non-self) upstreams:

- vuln-scanner — 1 cross-skill dep (`.outputs/github-trending.md`), fresh at its Saturday cadence.
- skill-security-scan — 1 historical citation (excluded), no live freshness dep.
- + 42 more enabled consumers whose only `articles/`, `.outputs/`, `memory/topics/`, or `memory/state/` references are **self-references** (a producer reading/writing its own state — e.g. `market-context-refresh`↔`market-context.md`, `aixbt-pulse`↔`aixbt-grounding.md`, `reg-monitor`↔`reg-monitor-seen.md`, `unlock-monitor`↔`unlock-monitor-seen.json`, `fleet-control`↔`fleet-control-state.json`), which are out of scope per step 4 — a skill keeping its own state is not a freshness gap.

## Source status

- `aeon.yml`: 130 entries parsed, 44 enabled
- `chains:` blocks: **none active** (`chains: {}`) → 0 explicit `consume:` edges in the fleet
- Implicit references discovered (across all enabled SKILL.md files): 8 distinct cross-skill (consumer, path) pairs after self-reference and code-example filtering
- Explicit `chains: consume:` edges: 0
- Files not flagged as MISSING (implicit references that never existed — e.g. `memory/topics/agent-evals.md`, cited inside a thought-review *example* block as a *suggestion to create*, not a read): 1 skipped

## Methodology note

This CI run is a fresh checkout: every file's on-disk mtime is the checkout time (~09:46 UTC) and git-commit dates collapse onto today's bulk daily-routine commit, so neither raw mtime nor git-date yields true per-file age here. Freshness was therefore scored against the **authoritative per-file signal** that survives a checkout — the date encoded in each `articles/{skill}-YYYY-MM-DD.md` filename, and the content-date inside `.outputs/`/topic/state files. The single live cross-skill dep (`.outputs/github-trending.md`) carries an explicit `06-14` content date, which is within its consumer's effective window. Same conclusion either way: nothing actionably stale.

---
*Companion to `skill-health` (per-skill failure detection) and `heartbeat` (per-run pulse). This skill catches the silent-staleness gap those two cannot: a consumer reading a stale file with no API errors and a 100% pass rate. The fleet's defining structural fact this run — `chains: {}` is empty, so there are zero cross-skill chain edges; almost every file reference in the fleet is a producer touching its own state. That is why the surface area for silent upstream staleness is currently near-zero. Methodology: every age and threshold is computed from the durable on-disk signal — this skill measures nothing it does not also report.*
