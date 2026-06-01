## Summary

**Cost report generated** for 2026-06-01 (last 7 days, direct gateway).

**Key findings:**
- **Total spend: $785.01** across 157 runs — no prior-week baseline (only 11 days of data, need 14 for WoW)
- **4 anomalies:** `reppo-trading-agent` spiked $33.96 (May 28) and $31.65 (May 29); `reppo-digest` spiked $9.16 and $8.77 (both May 29) — all output-heavy outliers from the same chain runs
- **30-day projection: $3,364 ⚠** — driven by reppo-swarm chain frequency (trading-agent + digest = 55% of weekly spend at $428/week)
- **No optimization levers found:** cache utilization is near-perfect (≥99.7%), all opus skills are output-heavy (ratios far above the 0.3 downgrade threshold), no model override drift
- **Files written:** `articles/cost-report-2026-06-01.md`, `memory/logs/2026-06-01.md`, `.pending-notify/cost-report-20260601.md` (notification staged for post-run delivery)
