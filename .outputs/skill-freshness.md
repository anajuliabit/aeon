*Skill Freshness — 2026-08-18*
🔴 FRESHNESS_STALE — 3 of 9 deps flagged across 3 of 43 enabled consumers

Worst:
- token-pick ← memory/topics/market-context.md (~33d old, class memory/topics, sev STALE)
- skill-security-scan ← articles/workflow-security-audit-2026-04-11.md (~128d old, class articles, sev STALE)
- vuln-scanner ← .outputs/github-trending.md (~23h old, class outputs, sev STALE)

Action: verify market-context-refresh is still on schedule; if so, producer ran but did not write a new article (market-context.md stale 33d, crosses 2× threshold — token-pick reads it daily)
Full: articles/skill-freshness-2026-08-18.md
