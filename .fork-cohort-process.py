#!/usr/bin/env python3
import sys, json

lines = sys.stdin.read().strip()

# Handle multiple JSON arrays from paginated output
# Each page is a JSON array; combine them
if lines.startswith('[['):
    # multiple arrays concatenated
    pages = json.loads('[' + lines.replace('][', '],[') + ']')
    flat = []
    for page in pages:
        if isinstance(page, list):
            flat.extend(page)
        else:
            flat.append(page)
else:
    flat = json.loads(lines)

# Deduplicate
seen = set()
unique = []
for f in flat:
    if f['full_name'] not in seen:
        seen.add(f['full_name'])
        unique.append(f)

# Sort by pushed_at desc
unique.sort(key=lambda x: x.get('pushed_at', ''), reverse=True)

# Cap at 80 by pushed_at desc
truncated = len(unique) > 80
if truncated:
    unique = unique[:80]

result = {
    'total': len(seen),
    'scanned': len(unique),
    'truncated': truncated,
    'forks': unique
}
print(json.dumps(result))
sys.stderr.write(f"Total unique forks: {len(seen)}, scanning: {len(unique)}, truncated: {truncated}\n")
