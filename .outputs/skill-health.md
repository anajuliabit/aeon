*skill health — 2026-08-10*
HEALTH: CRITICAL(16) [systemic: api.usepod.ai 402 — 21 skills, ISS-029 recurrence]

🔴 CRITICAL (16) — top 5 by severity
- weekly-shiplog — 12 fails, 21d down — WAIT-API (usepod 402) → ISS-031
- cost-report — 15 fails, 6d down — WAIT-API (usepod 402) → ISS-031
- btc-levels — 17 fails, <1d down — WAIT-API (usepod 402) → ISS-031
- daily-routine — 14 fails, 1.5d down — WAIT-API (usepod 402) → ISS-031
- thought-review — 15 fails, <1d down — WAIT-API (usepod 402) → ISS-031
+11 more (heartbeat/skill-freshness/security-digest/morning-brief/github-trending/unlock-monitor/token-alert/deal-flow/goal-tracker/list-digest/skill-security-scan) — same signature — see memory/issues/INDEX.md

🟡 DEGRADED (13): action-converter, aixbt-pulse, defi-monitor, market-context-refresh, narrative-tracker, reflect, reg-monitor, search-skill, self-improve, skill-analytics, skill-evals, skill-health, vuln-scanner

⚪ NO DATA (3): autoresearch, fork-skill-gap, operator-scorecard — DISPATCH-SKILL
🟢 HEALTHY: 5

composition shock from 8-09 (0→16 CRITICAL in 24h) — every failing skill lands identical usepod 402 payload, same byte-for-byte as ISS-029. self-improve exit-gate re-engages by ISS-031 severity, not queue depth.

fix ownership: operator. either top up usepod, or flip aeon.yml gateway.provider from direct → bankr/virtuals. aeon cannot self-repair — the failure surface is the LLM proxy aeon runs on.

open issues: 15 · resolved this run: 0 · filed this run: 1 (ISS-031)
