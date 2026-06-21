[.children[]? | select(.text != null) | {t: .text, p: (.points // 0), a: .author}]
| map(select((.t | length) > 200))
| sort_by(-.p)
| .[0] // {t: "(no substantive comment)", a: "-"}
| "TOP(@\(.a)): \(.t | gsub("<[^>]*>"; "") | gsub("&#x27;"; "'") | gsub("&quot;"; "\"") | gsub("&gt;"; ">") | gsub("&lt;"; "<") | gsub("&#x2F;"; "/") | gsub("&amp;"; "&") | .[0:430])"
