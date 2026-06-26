*Skill Health — 2026-06-26*
HEALTH: DEGRADED(26) [systemic: sandbox-truncation `output_tokens=0` — 26+ skills, root cause = aeon.yml capture step / ISS-025 cluster]

🟡 DEGRADED (worst 5 by success rate, cf=0 across fleet today)
- vuln-scanner — 7% (29 runs) → ISS-018 (sandbox: missing prefetch shim, distinct from systemic)
- reg-monitor — 10% (42 runs) — see systemic
- cost-report — 10% (42 runs) → ISS-025 (outputTokens=12 variant)
- skill-analytics — 11% (47 runs) — see systemic
- security-digest — 21% (86 runs) — see systemic
+21 more — see memory/issues/INDEX.md (incl. search-skill ISS-021, skill-health ISS-024)

🟠 WARNING (6): morning-brief 60% (NEW — was DEGRADED, crossed 0.6 boundary), token-pick 63% → ISS-020, token-movers 63%, defi-overview 68% → ISS-019, on-chain-monitor 70%, token-alert 74% → ISS-023
⚪ NO DATA (3): autoresearch (workflow_dispatch, OK), fork-skill-gap (Sun 6-28), operator-scorecard (Mon 6-29) — DISPATCH-SKILL on schedule
🟢 HEALTHY: 9

Open issues: 14 · Resolved this run: 0 · Filed this run: 0
Note: skill-runs CLI denied by sandbox — partial run, cron-state only.
