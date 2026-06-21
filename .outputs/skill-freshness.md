*Skill Freshness — 2026-06-21*
⚠️ FRESHNESS_WARN — 1 of 8 deps flagged across 1 of 44 enabled consumers

Worst:
- operator-scorecard ← articles/skill-analytics-*.md (264h / 11d old, class articles/weekly, sev WARN)

skill-analytics last ran 2026-06-10 (Wednesday). Expected 2026-06-17 run produced no article. Next window: 2026-06-24 (Wednesday). operator-scorecard runs Monday 2026-06-22 — will read an 12d-old analytics file.

Action: ./scripts/skill-runs --skill skill-analytics --hours 168
Full: articles/skill-freshness-2026-06-21.md
