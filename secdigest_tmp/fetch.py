#!/usr/bin/env python3
"""Fetch GH advisories via gh CLI and write to JSON files."""
import subprocess
import sys
import json

SINCE48 = "2026-07-02T14:17:38Z"

targets = [
    ("adv_critical.json", f"/advisories?type=reviewed&severity=critical&published={SINCE48}..&per_page=100"),
    ("adv_high.json", f"/advisories?type=reviewed&severity=high&published={SINCE48}..&per_page=100"),
    ("adv_malware.json", f"/advisories?type=malware&published={SINCE48}..&per_page=100"),
]

for fname, path in targets:
    print(f"Fetching {path}", file=sys.stderr)
    try:
        out = subprocess.check_output(["gh", "api", path], text=True)
        data = json.loads(out)
        with open(f"secdigest_tmp/{fname}", "w") as f:
            json.dump(data, f)
        print(f"  {fname}: {len(data)} entries", file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"  {fname}: FAIL {e}", file=sys.stderr)
        with open(f"secdigest_tmp/{fname}", "w") as f:
            f.write("[]")
