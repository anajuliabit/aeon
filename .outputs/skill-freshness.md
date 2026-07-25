*skill freshness — 2026-07-25*
🔴 FRESHNESS_STALE — 7 of 11 deps flagged across 5 of 43 enabled consumers

worst:
- skill-security-scan ← articles/workflow-security-audit-2026-04-11.md (105d, articles/weekly, STALE — disabled producer)
- aixbt-pulse ← memory/topics/aixbt-grounding.md (636h, topics, STALE — dark d27)
- vuln-scanner ← .outputs/github-trending.md (24h, outputs, STALE — self-resolves after github-trending 09:00)

also flagged:
- aixbt-pulse ← aixbt-clusters.md + aixbt-chains.md (same 636h, STALE)
- market-context-refresh + token-pick ← market-context.md (9d/216h, WARN — 12:00 cluster dark)

action: aixbt-pulse dead-slot d27 — check ISS files. security-scan ref is static doc, add ignore marker to SKILL.md:19+132. market-context clears on next cluster recovery.
full: articles/skill-freshness-2026-07-25.md
