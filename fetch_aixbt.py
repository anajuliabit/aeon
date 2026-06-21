#!/usr/bin/env python3
import json
import subprocess
from datetime import datetime

# Fetch data
g_result = subprocess.run(['curl', '-s', 'https://api.aixbt.tech/v2/grounding'], capture_output=True, text=True, timeout=10)
c_result = subprocess.run(['curl', '-s', 'https://api.aixbt.tech/v2/clusters'], capture_output=True, text=True, timeout=10)
ch_result = subprocess.run(['curl', '-s', 'https://api.aixbt.tech/v2/projects/chains'], capture_output=True, text=True, timeout=10)

if not g_result.stdout or not c_result.stdout or not ch_result.stdout:
    print("ERROR: One or more endpoints returned empty")
    exit(1)

try:
    grounding = json.loads(g_result.stdout)
    clusters = json.loads(c_result.stdout)
    chains = json.loads(ch_result.stdout)
except json.JSONDecodeError as e:
    print(f"ERROR: Failed to parse JSON: {e}")
    exit(1)

# Save combined data
data = {
    'grounding': grounding,
    'clusters': clusters,
    'chains': chains,
    'fetched_at': datetime.now().isoformat()
}

with open('aixbt-raw.json', 'w') as f:
    json.dump(data, f, indent=2)

print("OK: Fetched and saved")
print(f"createdAt: {grounding['data']['createdAt']}")
print(f"sections: {','.join(grounding['data']['sections'].keys())}")
print(f"clusters: {len(clusters['data'])}")
print(f"chains: {len(chains['data'])}")
