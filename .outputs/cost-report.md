*Cost Report — 2026-05-25 (last 7 days)*

Spent $179.73 across 61 runs (no prior-week baseline); 1 anomaly flagged, projected monthly burn ~$770.35.

Top 3 by cost:
1. defi-overview — $32.79 (4 runs)
2. reppo-trading-agent — $24.60 (7 runs)
3. heartbeat — $19.06 (8 runs)

Actions this week:
• No strict optimization levers triggered (cache underuse / model-downgrade filters don't fire for this cache-dominated workload)
• Manual review: defi-overview + heartbeat + reppo-digest on Opus account for 38% of spend; Sonnet override could cut ~$55–65/wk — operator call

⚠ 1 anomaly: reppo-digest 2026-05-24 — cache_read spiked to 1.51M (2–6× typical), cost $4.12 vs µ $2.03
⚠ burn-rate watch: $770/mo projection driven partly by heavy bootstrap day (2026-05-21); need another week to confirm trend

30-day projection: ~$770.35
Full: articles/cost-report-2026-05-25.md
