---
name: xai-quota-exhausted
description: X.AI monthly credit limit hit, blocking 10+ XAI-dependent skills (day 11 of outage as of 2026-06-26)
metadata:
  type: project
---

Team 3a8b4c1e monthly credit limit reached 2026-06-16 (day 11 as of 2026-06-26), blocking:
- token-pick
- agent-buzz
- list-digest
- refresh-x
- remix-tweets
- tweet-roundup
- narrative-tracker
- reply-maker
- article
- fetch-tweets

**Partial recovery via prefetched paths.** Skills that run their XAI calls through `scripts/prefetch-xai.sh` *before* the sandboxed Claude step still complete normally — confirmed working through 6-26 for list-digest, narrative-tracker, agent-buzz. The quota error only manifests on in-sandbox calls.

**Fallback coverage gaps:**
- FALLBACK_CG_SKILLS workaround covers 5 CoinGecko-price skills (defi-overview, token-movers, token-pick, token-alert, market-context-refresh) via Virtuals deepseek-v4-flash.
- WebSearch fallback covers daily-routine, tweet-roundup, narrative-tracker on the X-sentiment leg.
- XAI-only sentiment paths (refresh-x, remix-tweets, fetch-tweets, reply-maker) have no fallback.

Operator action required: top up XAI credits or wait for monthly reset.

Related: [[14-29z-batch-stuck]], [[deal-flow-stuck]], [[fork-cohort-stuck]], [[pr-112-stalled]]