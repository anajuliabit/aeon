---
name: xai-quota-exhausted
description: X.AI monthly credit limit hit, blocking 10+ XAI-dependent skills (day 13 of outage as of 2026-06-28)
metadata:
  type: project
---

Team 3a8b4c1e monthly credit limit reached 2026-06-16 (day 13 as of 2026-06-28), blocking:
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

**Partial recovery via prefetched paths.** Skills that run their XAI calls through `scripts/prefetch-xai.sh` *before* the sandboxed Claude step still complete normally — confirmed working through 6-28 for list-digest, narrative-tracker, agent-buzz, token-pick. The quota error only manifests on in-sandbox calls.

**PR #148 (open) — fix(agent-buzz): rank x_search by engagement (mode:Top + min_likes:5).** Operator (Ana) opened 6-27 18:14Z in direct response to the agent-buzz 6-27 cache-quality observation. Implements the `mode:"Latest"` → `mode:"Top"` + `min_likes:5` switch. Day-2 carry as of 6-28 reflect; under 24h stall threshold the morning of 6-28, now ~24h+.

**Cache-quality observation (6-27 agent-buzz):** prefetch script uses `mode:"Latest"` only across 4 sub-queries (chronological tail, not top engagement). Result: uniformly low engagement candidates (0–13 likes max, `followers: null`). Curation degenerated to substantive-claim selection rather than engagement ranking. Addressed by PR #148.

**Fallback coverage gaps:**
- FALLBACK_CG_SKILLS workaround covers 5 CoinGecko-price skills (defi-overview, token-movers, token-pick, token-alert, market-context-refresh) via Virtuals deepseek-v4-flash.
- WebSearch fallback covers daily-routine, tweet-roundup, narrative-tracker on the X-sentiment leg.
- XAI-only sentiment paths (refresh-x, remix-tweets, fetch-tweets, reply-maker) have no fallback.

Operator action required: top up XAI credits or wait for monthly reset.

Related: [[14-29z-batch-stuck]], [[deal-flow-stuck]], [[fork-cohort-stuck]], [[pr-112-stalled]]