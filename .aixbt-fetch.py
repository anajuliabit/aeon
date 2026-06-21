#!/usr/bin/env python3
import json
import sys
import urllib.request

def fetch_aixbt():
    endpoints = {
        'grounding': 'https://api.aixbt.tech/v2/grounding',
        'clusters': 'https://api.aixbt.tech/v2/clusters',
        'chains': 'https://api.aixbt.tech/v2/projects/chains'
    }

    data = {}
    for name, url in endpoints.items():
        try:
            with urllib.request.urlopen(url, timeout=10) as resp:
                raw = resp.read()
                data[name] = json.loads(raw)
                print(f"✓ {name} fetched ({len(raw)} bytes)")
        except Exception as e:
            print(f"✗ {name} failed: {e}", file=sys.stderr)
            return None

    return data

if __name__ == '__main__':
    data = fetch_aixbt()
    if data:
        for k, v in data.items():
            with open(f'/home/runner/work/aeon/aeon/.cache-{k}.json', 'w') as f:
                json.dump(v, f)
        print("\nData written to .cache-*.json files")
    else:
        sys.exit(1)
