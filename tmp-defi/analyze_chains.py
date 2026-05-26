import json
chains = json.load(open('/home/runner/work/aeon/aeon/tmp-defi/chains.json'))
total_tvl = sum(c.get('tvl', 0) or 0 for c in chains)
print(f"total_tvl_B={total_tvl/1e9:.3f}")
print(f"chains_count={len(chains)}")
top10 = sorted(chains, key=lambda c: c.get('tvl', 0) or 0, reverse=True)[:10]
for c in top10:
    print(f"  {c.get('name','?')}: ${(c.get('tvl',0) or 0)/1e9:.3f}B  keys={list(c.keys())}")
