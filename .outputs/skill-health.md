*skill health — 2026-08-13 18Z*
HEALTH: CRITICAL(3)

systemic:
- 3 skills stuck on api.usepod.ai 402 stale-state (unlock-monitor / deal-flow / skill-security-scan) — mon-cadence, next dispatch tick clears the marker (10Z/14Z/16Z mon 8-17). ISS-031
- 4 skills 47d cold in 12Z batch dark (aixbt-pulse / defi-monitor / market-context-refresh / narrative-tracker) — scheduler-side gap frozen since 6-28. ISS-027

🔴 CRITICAL (3, all ISS-031)
- unlock-monitor — 7 fails, 10d down — wait-api (usepod-402)
- deal-flow — 6 fails, 10d down — wait-api (usepod-402)
- skill-security-scan — 3 fails, 10d down — wait-api (usepod-402)

🟡 DEGRADED (17, top-5 non-systemic)
- cost-report — 8% sr, sdk_opt_in_required chronic — investigate → ISS-030
- reg-monitor — 22% sr chronic — investigate
- skill-analytics — 22% sr chronic — investigate
- vuln-scanner — 25% sr chronic — investigate
- security-digest — 44% sr chronic — investigate
+12 more — see memory/issues/INDEX.md

⚪ NO DATA (3): autoresearch / fork-skill-gap / operator-scorecard — dispatch-skill
🟢 HEALTHY: 7 (+1 vs 8-12; btc-levels recovered, removed from ISS-031 affected_skills 20→19)

spec-gap: fork-cohort ~117h stuck (last_success 8-02T19:52Z, last_dispatch 8-09T19:05Z) still classifies HEALTHY under strict rules. ISS-032 filing 6th+ owed cycle. self-improve 18Z candidate: bake `status='dispatched' AND days_since_last_dispatch>=3` branch into step 2.

open: 15 · resolved this run: 0 · filed: 0 · modified: 1 (ISS-031)
