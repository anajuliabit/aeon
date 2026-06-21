---
name: xai-quota-exhausted
description: X.AI monthly credit limit hit, blocking 10+ XAI-dependent skills
metadata:
  type: project
---

Team 3a8b4c1e monthly credit limit reached 2026-06-16, blocking:
-Token-pick
-Agent-buzz  
-List-digest
-Refresh-x
-Remix-tweets
-Tweet-roundup
-Narrative-tracker
-Reply-maker
-Article
-Fetch-tweets

FALLBACK_CG_SKILLS workaround covers 5 CoinGecko-price skills (defi-overview, token-movers, token-pick, token-alert, market-context-refresh) via Virtuals deepseek-v4-flash, but XAI path lacks fallback.

Operator action required: top up XAI credits or wait for monthly reset.

Related: [[14-29z-batch-stuck]], [[deal-flow-stuck]], [[fork-cohort-stuck]], [[pr-112-stalled]]