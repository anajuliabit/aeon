#!/usr/bin/env python3
"""Build OSV.dev batch query from go.mod dependencies."""
import json, re, sys

deps = []
with open(sys.argv[1]) as f:
    for line in f:
        m = re.match(r'^\t([^ ]+) (v[^\s]+)', line)
        if m:
            name, version = m.group(1), m.group(2)
            deps.append({"package": {"name": name, "ecosystem": "Go"}, "version": version})

print(json.dumps({"queries": deps}))
