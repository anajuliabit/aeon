*Goal Tracker — 2026-06-23*

Summary: 9 goals — 0 at risk, 0 needs attention, 4 on track, 3 blocked, 2 done (overall → flat, +1 done)

BLOCKED
• XAI quota recovery — waiting on operator top-up since 2026-06-16 (7d). websearch fallback holds.
  → Action: operator — top up Team 3a8b4c1e xai credits, or formalize websearch fallback as durable
• Operator action: on-chain config completion — waiting on ALCHEMY_API_KEY / ETHERSCAN_API_KEY (probe 13:25Z: len=0 / null)
  → Action: operator — set ALCHEMY_API_KEY env to lift on-chain-monitor degraded
• Operator-gated monitors — defi-monitor 16d NO_CONFIG streak; no type:pool / type:position entries
  → Action: operator — add type:pool / type:position rows to memory/on-chain-watches.yml

ON TRACK
• Sandbox-truncation systemic — 0d idle, ~32 activity/14d (→ flat; ISS-025 widened cf 17→23 today, no durable fix yet)
• Stuck skills — 0d idle, ~14 activity/14d (→ flat; deal-flow/token-alert/fork-cohort all recovered 6-21/6-22)
• skill-freshness FRESHNESS_WARN — 0d idle, ~13 activity/14d (→ flat; operator-scorecard articles 312h/13d, re-emit 6-28)
• BTC hard levels — 0d idle, ~25 activity/14d (→ flat; spot $62.0–64.0k, close 6-22 $63,957, no breakdown)

DONE
• MemoClaw soul-strip PR pending — completed 2026-06-22 (PR #137 merged 15:08Z)
• PR backlog — completed 2026-06-21 (still 0 open at today's heartbeats)

Sources: logs=ok, git=ok, gh_pr=ok, gh_issue=ok(empty), cron-state=ok
