*Goal Tracker — 2026-06-25*

Summary: 5 goals — 0 at risk, 0 needs attention, 2 on track, 2 blocked, 1 done (overall ↑ improving — skill-freshness cleared, others held flat)

BLOCKED
• XAI quota recovery — waiting on operator credit top-up for Team 3a8b4c1e since 2026-06-16 (day 10). Prefetched .xai-cache covered narrative-tracker/list-digest today; daily-routine tweet-roundup still on WebSearch fallback.
  → Action: top up Team 3a8b4c1e monthly credit
• Operator on-chain config — waiting on operator for `type: pool`/`type: position` entries + ALCHEMY_API_KEY since 2026-06-08 (defi-monitor NO_CONFIG day 18, key absent day 9). on-chain-monitor still green on Blockscout keyless. Operator did seed `memory/known-addresses.yml` today — partial progress.
  → Action: add type:pool entries to memory/on-chain-watches.yml and set ALCHEMY_API_KEY

ON TRACK
• Sandbox-truncation systemic — 0d idle, 35+ activity/14d (→ flat). 22-skill chronic tail unchanged in today's 08:43Z + 14:53Z heartbeats, all sharing output_tokens=0 signature. cost-report cf=0 holds since 6-24 03:48Z recovery (sr still 10%). ISS-025 capture-fix PR flagged by action-converter 6-24 18:14Z (quality 4.6/5) but not yet opened.
• BTC hard levels — 0d idle, 35+ activity/14d (→ flat). btc-levels ran 4x today (00:51/04:51/08:42/13:09/16:39Z). Spot range 6-25 $59,317–$61,801, daily close 6-24 $60,909 (above $60,500 breakdown threshold, no alerts fired). Reclaim flags still false (already triggered 6-11/6-15).

DONE
• skill-freshness FRESHNESS_WARN — cleared 2026-06-25 (skill-analytics ran 6-24, resolving operator-scorecard stale-dep that had persisted since 2026-06-21; skill-freshness 6-25 returned FRESHNESS_OK)

Sources: logs=ok, git=ok, gh_pr=ok, gh_issue=ok, cron-state=ok
