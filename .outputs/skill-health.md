*Skill Health — 2026-08-17*
HEALTH: CRITICAL(1)  [systemic: 12Z batch dark d52 (4 skills, ISS-027); first-run miss (2 skills)]

🔴 CRITICAL
- cost-report — 13 fails, 6d down, sdk_opt_in_required — WAIT-API → ISS-030

🟡 DEGRADED / FLAPPING (17)
- deal-flow — recovered today via bypass, sr=47% — WAIT-API → ISS-031
- unlock-monitor — recovered today via bypass, sr=41% — WAIT-API → ISS-031
- search-skill — recovered today via bypass, sr=38% — WAIT-API → ISS-031
- reg-monitor — 22% sr chronic — INVESTIGATE
- skill-analytics — 22% sr chronic — INVESTIGATE
+12 more — see memory/issues/INDEX.md

⚪ NO DATA (3): autoresearch (workflow_dispatch), fork-skill-gap (missed 8-16 21Z), operator-scorecard (missed 10:30Z) — DISPATCH-SKILL
🟢 HEALTHY: 6

Δ vs prev (8-16 18:16Z): 3 CRITICAL cleared (deal-flow / skill-security-scan / unlock-monitor via mon-batch direct-exec bypass = memory-window-first full-cohort recovery); 1 CRITICAL new (cost-report crossed consec>=3 gate at consec=13); usepod-402 SYSTEMIC cleared; 12Z batch dark extends d51→d52; NEW first-run-miss SYSTEMIC (2 skills, ~20h + ~7h past scheduled)

Open issues: 15 · Filed this run: 0 · Resolved this run: 0
