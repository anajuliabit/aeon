#!/usr/bin/env bash
for id in 48528371 48537165 48526360 48526633 48528029 48471638; do
  curl -s "https://hn.algolia.com/api/v1/items/$id" | jq -r --arg id "$id" '
    "### STORY \($id): \(.title)",
    ([.children[]? | select(.text != null) | {t:.text, p:(.points//0), a:.author}]
      | map(select((.t|length) > 220))
      | sort_by(-.p) | .[0] // {t:"(no substantive comment)", a:"-"}
      | "TOP(@\(.a)): \(.t | gsub("<[^>]*>";"") | gsub("&#x27;";"'") | gsub("&quot;";"\"") | gsub("&gt;";">") | gsub("&lt;";"<") | gsub("&#x2F;";"/") | gsub("&amp;";"&") | .[0:420])")
  ' 2>/dev/null
  echo "---"
done
