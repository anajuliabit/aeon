#!/bin/bash
curl -s -o /home/runner/work/aeon/aeon/.xai-out.json -w "HTTP %{http_code}\n" -X POST "https://api.x.ai/v1/responses" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${XAI_API_KEY}" \
  -d '{
    "model": "grok-4-1-fast",
    "input": [{"role": "user", "content": "Search X from 2026-05-20 to 2026-05-21 for tweets in the AI-agents conversation: autonomous agents, agent frameworks, MCP / agent protocols, agent products, agent benchmarks, agent research papers. Return up to 40 candidates. For EACH candidate you MUST return: @handle, follower_count (integer or null), role_guess (builder|founder|researcher|investor|commentator|anon), one-line claim (what they actually said, the thesis), likes (int), retweets (int), replies (int), posted_at (ISO), direct_link (https://x.com/username/status/ID). Prefer builders/founders/researchers. Skip obvious engagement-farming threads."}],
    "tools": [{"type": "x_search", "from_date": "2026-05-20", "to_date": "2026-05-21"}]
  }'
