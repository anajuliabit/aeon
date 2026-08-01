---
name: Daily Routine
description: Morning briefing combining token movers, tweet roundup, paper pick, GitHub issues, and HN digest
var: ""
tags: [news]
---
> **${var}** — Area to emphasize (e.g. "crypto", "AI", "security"). If empty, covers all areas equally.

This skill is designed to run as part of a chain (see `chains:` in `aeon.yml`). When chained, prior step outputs (token-movers, paper-pick, github-issues, hn-digest) are provided in the chain context above. Use those outputs directly — do not re-run the sub-skills.

If running standalone (no chain context provided), fall back to reading each sub-skill and executing it inline:
- Read `skills/token-movers/SKILL.md` and execute its steps
- Read `skills/paper-pick/SKILL.md` and execute its steps
- Read `skills/github-issues/SKILL.md` and execute its steps
- Read `skills/hacker-news-digest/SKILL.md` and execute its steps

Read memory/MEMORY.md for context.
Read the last 2 days of memory/logs/ to avoid repeating items.

---

## Tweet Roundup

Covers three default topics: **crypto**, **AI**, **dev**.

**Primary source — XAI pre-fetched cache.** The workflow pre-fetches Grok x_search results for all three topics into `.xai-cache/daily-routine.json` (single combined call, each tweet tagged with topic=crypto|AI|dev). Read it. If the file exists and contains usable results, split tweets by topic tag and use that as the source. Note in the log line: "XAI cache HIT (.xai-cache/daily-routine.json, N tweets)".

**Fallback — WebSearch.** If any of these apply, skip XAI entirely and use `WebSearch` per topic instead:
- `.xai-cache/daily-routine.json` is missing or empty (prefetch didn't run, or `XAI_API_KEY` unset), OR
- the cached response contains an error (HTTP 429, 401/403, quota-exhausted / credit-out), OR
- `memory/MEMORY.md` flags XAI as quota-exhausted or otherwise unavailable — trust the memory signal.

Do NOT attempt a direct `curl` to `api.x.ai` from inside the skill — the sandbox strips `$XAI_API_KEY` from bash env, so every direct call fails. Cache-or-WebSearch is the only working path.

Note at the top of the tweet-roundup log line which source path fired: `XAI cache HIT` or `WebSearch fallback used — <reason>`.

For each topic, write 2-3 bullet points capturing the gist. Include links.

---

## Format & Send

Combine everything (chain context outputs + tweet roundup) into a single notification via `./notify` (keep under 4000 chars):

```
*Daily Routine — ${today}*

*Top 10 Winners (24h)*
1. SYMBOL: $price (+X%)
...

*Top 10 Losers (24h)*
1. SYMBOL: $price (-X%)
...

*Tweet Roundup*
*Crypto:* gist of what's happening
*AI:* gist
*Dev:* gist

*Paper of the Day*
"Title" — why you should read it [link]

*GitHub Issues*
- repo: #N title (or "No new issues")

*HN Digest*
1. [Title](url) (Xpts) — summary
   [Discuss](hn_link)
...
```

If the combined message exceeds 4000 chars, trim the HN and tweet sections first — token data and paper pick are highest priority.

## Sandbox note

The sandbox may block outbound curl. Use **WebFetch** as a fallback for any URL fetch. For auth-required APIs, use the pre-fetch/post-process pattern (see CLAUDE.md).

## Log

Log everything to memory/logs/${today}.md.
