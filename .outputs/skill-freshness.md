*Skill Freshness — 2026-08-06*
🔴 FRESHNESS_STALE — 2 of 8 deps flagged across 2 of 43 enabled consumers

5 prior-run flags resolved to fresh (aixbt-pulse ×3, market-context-refresh, token-pick — all updated 2026-08-05 22:06Z). 2 persistent STALE flags unchanged since 2026-07-25 (12+ days):

Worst:
- skill-security-scan ← articles/workflow-security-audit-2026-04-11.md (117d old, class articles-weekly, sev STALE)
- vuln-scanner ← .outputs/github-trending.md (~11h old, class outputs, sev STALE)

Action: workflow-security-audit is disabled — reference in skill-security-scan is historical docs. vuln-scanner flag clears after today's github-trending 09:00Z run.
Full: articles/skill-freshness-2026-08-06.md
