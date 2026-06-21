import re, os, glob, json, hashlib
from datetime import datetime, timezone

TODAY = "2026-06-15"
NOW = datetime(2026, 6, 15, 8, 0, 0, tzinfo=timezone.utc)  # nominal run time 08:00 UTC

# Cadence map from aeon.yml (enabled + relevant producers). daily/weekly/on_demand
CADENCE = {
    "morning-brief":"daily","daily-routine":"daily","github-trending":"daily",
    "token-alert":"daily","token-movers":"daily","on-chain-monitor":"daily",
    "defi-monitor":"daily","defi-overview":"daily","token-pick":"daily",
    "market-context-refresh":"daily","btc-levels":"daily","narrative-tracker":"daily",
    "unlock-monitor":"weekly","aixbt-pulse":"daily","search-skill":"daily",
    "security-digest":"daily","deal-flow":"weekly","reg-monitor":"weekly",
    "skill-security-scan":"weekly","vuln-scanner":"weekly","autoresearch":"on_demand",
    "list-digest":"daily","agent-buzz":"daily","goal-tracker":"daily",
    "skill-health":"daily","skill-analytics":"weekly","self-improve":"daily",
    "reflect":"daily","action-converter":"daily","evening-recap":"daily",
    "thought-review":"daily","cost-report":"weekly","fork-cohort":"weekly",
    "skill-evals":"weekly","skill-update-check":"weekly","fleet-control":"daily",
    "weekly-review":"weekly","weekly-shiplog":"weekly","operator-scorecard":"weekly",
    "fork-skill-digest":"weekly","fork-skill-gap":"weekly","skill-graph":"weekly",
    "skill-freshness":"daily","heartbeat":"daily",
}

ENABLED = [k for k,v in CADENCE.items()]  # all listed are enabled

# thresholds in hours
def threshold(path_class, cadence):
    if path_class == "articles":
        return 192 if cadence == "weekly" else 28
    if path_class == "outputs":
        return 4
    if path_class == "topics":
        return 168
    if path_class == "state":
        return 720
    return 28

PAT = {
    "articles": re.compile(r'articles/([a-zA-Z0-9_-]+?)(?:-\$\{today\}|-\d{4}-\d{2}-\d{2})?\.md'),
    "outputs": re.compile(r'\.outputs/([a-zA-Z0-9_-]+)\.md'),
    "topics": re.compile(r'memory/topics/([a-zA-Z0-9_.-]+)\.md'),
    "state": re.compile(r'memory/state/([a-zA-Z0-9_.-]+)\.json'),
}

def file_age_hours(path):
    if not os.path.exists(path):
        return None
    mt = datetime.fromtimestamp(os.path.getmtime(path), tz=timezone.utc)
    return (NOW - mt).total_seconds()/3600.0

# Discover edges
edges = []  # dict consumer, path, class, producer
for s in ENABLED:
    sp = f"skills/{s}/SKILL.md"
    if not os.path.isfile(sp):
        print("MISSING SKILLMD", s); continue
    txt = open(sp).read()
    for cls, pat in PAT.items():
        for m in pat.finditer(txt):
            producer = m.group(1)
            full = m.group(0)
            # skip self-references for articles/outputs (producer prefix == consumer)
            if cls in ("articles","outputs") and (producer == s or full.split('/')[1].startswith(s)):
                continue
            edges.append({"consumer":s,"raw":full,"class":cls,"producer":producer})

print("raw edges:", len(edges))

# Resolve & score
def resolve(edge):
    cls = edge["class"]; producer = edge["producer"]
    if cls == "articles":
        cands = sorted(glob.glob(f"articles/{producer}-*.md"), key=lambda p: os.path.getmtime(p) if os.path.exists(p) else 0, reverse=True)
        path = cands[0] if cands else f"articles/{producer}-{TODAY}.md"
        return path
    if cls == "outputs":
        return f".outputs/{producer}.md"
    if cls == "topics":
        return f"memory/topics/{producer}.md"
    if cls == "state":
        return f"memory/state/{producer}.json"
    return edge["raw"]

scored = []
seen_pair = set()
for e in edges:
    path = resolve(e)
    key = (e["consumer"], path)
    if key in seen_pair: continue
    seen_pair.add(key)
    cad = CADENCE.get(e["producer"], "on_demand")
    th = threshold(e["class"], cad)
    age = file_age_hours(path)
    if age is None:
        # MISSING only for canonical article patterns w/ daily|weekly producer, or explicit (none here)
        if e["class"]=="articles" and cad in ("daily","weekly"):
            sev = "MISSING"
        else:
            sev = "SKIP"  # implicit nonexistent -> ignore
    else:
        if age <= th: sev="OK"
        elif age <= 2*th: sev="WARN"
        else: sev="STALE"
    scored.append({**e,"path":path,"cadence":cad,"threshold":th,"age":age,"severity":sev})

# Filter out SKIP
ignored = [x for x in scored if x["severity"]=="SKIP"]
active = [x for x in scored if x["severity"]!="SKIP"]

rank = {"MISSING":3,"STALE":2,"WARN":1,"OK":0}
# per consumer worst
from collections import defaultdict
cons = defaultdict(list)
for x in active: cons[x["consumer"]].append(x)
consumer_verdict = {c: max(rows,key=lambda r:rank[r["severity"]])["severity"] for c,rows in cons.items()}

flagged = [x for x in active if x["severity"]!="OK"]
fleet_rank = max([rank[v] for v in consumer_verdict.values()] + [0])
fleet = {0:"FRESHNESS_OK",1:"FRESHNESS_WARN",2:"FRESHNESS_STALE",3:"FRESHNESS_STALE"}[fleet_rank]

print("=== SUMMARY ===")
print("enabled consumers:", len(ENABLED))
print("dependencies checked:", len(active))
print("ignored (implicit nonexistent):", len(ignored))
print("flagged:", len(flagged))
print("fleet verdict:", fleet)
print()
print("=== FLAGGED ===")
for x in sorted(flagged,key=lambda r:(-rank[r["severity"]],r["consumer"])):
    ah = "n/a" if x["age"] is None else f"{x['age']:.1f}h"
    print(f"  [{x['severity']}] {x['consumer']} <- {x['path']} ({x['class']}, age {ah}, thr {x['threshold']}h, producer {x['producer']}/{x['cadence']})")
print()
print("=== fingerprint ===")
fp_rows = sorted([f"{x['consumer']}:{x['path']}:{x['severity']}" for x in flagged])
fp = hashlib.sha1("\n".join(fp_rows).encode()).hexdigest()
print("fingerprint:", fp)
print("empty-sha1 da39a3ee... means no flags")

# dump active OK consumers
print()
print("=== OK consumers (dep counts) ===")
for c in sorted(cons):
    if consumer_verdict[c]=="OK":
        print(f"  {c}: {len(cons[c])} deps")
print()
print("consumers with 0 active deps:", [s for s in ENABLED if s not in cons])

# Save for later
json.dump({"active":[{k:(v if k!='age' else v) for k,v in x.items()} for x in active],
           "flagged":flagged,"fleet":fleet,"fp":fp,"fp_rows":fp_rows,
           "ignored_count":len(ignored),"cons_verdict":consumer_verdict,
           "edge_count":len(edges)}, open(".freshness-out.json","w"), default=str, indent=1)
print("\nwrote .freshness-out.json")
