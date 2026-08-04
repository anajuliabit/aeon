*skill-health — 2026-08-04*
HEALTH: CRITICAL(1) — 1 critical / 17 degraded / 14 warning / 8 healthy / 3 no-data (43 enabled)

🔴 CRITICAL (1)
- cost-report — 17 fails, 8d down · sdk_opt_in_required (distinct from ISS-025 truncation + ISS-029 usepod 402) · FIX CONFIG → ISS-030 filed

🟡 DEGRADED (17, sr<60%)
- reg-monitor 19% · skill-analytics 19% · vuln-scanner 23% · market-context-refresh 32% · narrative-tracker 33% · search-skill 38% · security-digest 43% · aixbt-pulse 47%
- +9 more (skill-health 50, self-improve 51, action-converter 53, defi-monitor 53, goal-tracker 53, reflect 54, skill-evals 56, unlock-monitor 57, list-digest 58) — see memory/issues/INDEX.md

⚪ NO DATA (3): autoresearch, fork-skill-gap, operator-scorecard → DISPATCH-SKILL
🟢 HEALTHY: 8

Δ prev tick (8-03 20:16Z): CRITICAL 11→1 (fleet recovered), DEGRADED 8→17 (formerly-critical settled at historic low-sr), WARNING 15→14, HEALTHY 6→8.

ISS-029 RESOLVED — usepod gateway self-healed ~2h window (18:27Z→20:14Z 8-03), 17-of-18 skills booked clean successes since. cost-report split off to ISS-030 under distinct sdk_opt_in_required signature.

Open issues: 14 · Resolved this run: 1 (ISS-029) · Filed this run: 1 (ISS-030)
