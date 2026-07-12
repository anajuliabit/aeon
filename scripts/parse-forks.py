import json, sys

with open('/home/runner/.claude/projects/-home-runner-work-aeon-aeon/bdea4feb-1b1c-451b-a052-5123ddead615/tool-results/bd5ivwn3i.txt') as f:
    data = json.load(f)

total = len(data)
data_sorted = sorted(data, key=lambda x: x['pushed_at'], reverse=True)[:80]
truncated = total > 80

print(f'total={total}')
print(f'processing={len(data_sorted)}')
print(f'truncated={truncated}')

with open('/tmp/forks.json', 'w') as f:
    json.dump(data_sorted, f)

print('done')
