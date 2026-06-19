---
name: Daily Article
description: Research trending topics and write a publication-ready article
var: ""
tags: [content]
---
> **${var}** — Topic to write about. If empty, auto-selects a trending topic.

If `${var}` is set, write about that topic instead of auto-selecting.


Today is ${today}. Your task is to research and write a high-quality article.

Steps:
1. Read `memory/MEMORY.md` for context on what topics have been covered recently.
2. **Research approach (with fallbacks):**
   - Check `.article-cache/` directory for pre-fetched content from `scripts/prefetch-article.sh`
   - If cache exists, use it as source material
   - If no cache, search the web for the most interesting recent developments in AI, crypto/DeFi, or consciousness research — pick whichever has the most compelling story today. Use WebSearch to find current sources.
   - If WebSearch fails due to sandbox restrictions, use memory/topics/ files (market-context.md, crypto.md) and recent logs/articles as sources
3. **Read sources:** Gather facts and quotes from 2-3 sources:
   - If web accessible: Use WebFetch for source articles
   - If sandbox blocked: Use cache files or existing memory/topics content
4. Write a 600-800 word article in markdown. Include:
   - A compelling title
   - A short intro hook
   - 3-4 substantive sections
   - Cited sources at the bottom (use URLs if available, otherwise note source type)
5. Save the article to: articles/${today}.md
6. Update memory/MEMORY.md to record that this article was written and its topic.
7. Log what you did to memory/logs/${today}.md. Include research method (web/cache/memory) and any fallbacks used.
8. Send a notification via `./notify`: "New article written: [title]\n\nhttps://github.com/${GITHUB_REPOSITORY}/blob/main/articles/${today}.md"

   Use the `$GITHUB_REPOSITORY` env var (GitHub Actions sets it to `owner/repo` of the running instance).

**Exit codes for monitoring:**
- ARTICLE_OK: Article successfully written
- ARTICLE_CACHE: Used cached/fallback sources (sandbox blocked web)
- ARTICLE_NO_SOURCES: No viable sources found (log and exit quietly)

## Sandbox note

GitHub Actions sandbox may block outbound curl. Always use **WebFetch** as a fallback for any URL fetch.

For auth-required APIs (not needed for this skill), use the pre-fetch/post-process pattern (see CLAUDE.md).

**Fallback research approach**: If WebFetch/WebSearch fail due to sandbox restrictions:
1. Check `.article-cache/` for pre-fetched content from `scripts/prefetch-article.sh`
2. Use memory/topics/ files as alternative sources when web research is blocked
3. If completely blocked, write about topics from recent logs/articles (BTC levels, token picks, market context)

Write complete, publication-ready content. No placeholders.
