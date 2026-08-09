*Skill Analytics — 2026-08-05*
10 scheduled skills didn't run this window — token-movers

Window: last 7d · 246 runs · 31 skills · 75.2% success
Anomalies: 24 (10 🔴 SILENT + 14 🟠 LOW_SUCCESS)

🔴 Critical:
- token-movers — SILENT: `10 12 * * *`, zero runs (ISS-027 batch-dark d39+)
- on-chain-monitor — SILENT: `20 12 * * *`, zero runs (ISS-027)
- defi-monitor — SILENT: `40 12 * * *`, zero runs (ISS-027)
(+7 more SILENT: defi-overview, market-context-refresh, narrative-tracker, aixbt-pulse, weekly-shiplog, operator-scorecard, fork-skill-gap)

🟠 Degraded:
- cost-report — LOW_SUCCESS: 5.3% over 19 runs (ISS-030 sdk_opt_in_required)
- skill-freshness — LOW_SUCCESS: 44.4% over 9 runs (ISS-029 + 08Z slot miss)
- unlock-monitor — LOW_SUCCESS: 20.0% over 5 runs (ISS-029 cascade)
(+11 more LOW_SUCCESS: deal-flow, search-skill, skill-security-scan, daily-routine, security-digest, thought-review, morning-brief, action-converter, goal-tracker, reflect, skill-health)

Top by runs: btc-levels (39), heartbeat (21), cost-report (19)

Full: articles/skill-analytics-2026-08-05.md
