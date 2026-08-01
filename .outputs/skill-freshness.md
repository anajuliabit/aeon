*Skill Freshness — 2026-08-01*
🔴 FRESHNESS_STALE — 7 of 11 deps flagged across 5 of 43 enabled consumers

Worst:
- skill-security-scan ← `articles/workflow-security-audit-2026-04-11.md` (112d old, articles/weekly, STALE)
- aixbt-pulse ← `memory/topics/aixbt-grounding.md` (~34d old, topics, STALE)
- market-context-refresh ← `memory/topics/market-context.md` (~16d old, topics, STALE) ← escalated from WARN

Escalation: market-context-refresh + token-pick cross 2× age threshold today (380h vs 336h). First fingerprint change since 2026-07-25. All 7 flagged items now STALE (was 5 STALE + 2 WARN).

Action: ISS-027 cluster unblock resolves market-context + token-pick. aixbt-pulse dead-slot d34+ needs separate fix. workflow-security-audit-2026-04-11.md stale due to disabled producer.
Full: articles/skill-freshness-2026-08-01.md
