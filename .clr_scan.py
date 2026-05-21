import subprocess, re, html, json, time, urllib.parse, datetime

NOW = datetime.datetime(2026, 5, 21, tzinfo=datetime.timezone.utc)
WINDOW = NOW - datetime.timedelta(days=7)

COHORT = ["langgraph","crewai","autogen","llamaindex","mastra","smolagents","dspy","pydantic-ai","aeon"]
KEYWORDS = ["agent framework","autonomous agent","agentic","multi-agent","mcp server",
            "mcp client","ai agent","claude agent","llm agent"]

def curl(url, timeout=30):
    try:
        r = subprocess.run(["curl","-fsSL","--max-time",str(timeout),
                            "-A","aeon-competitor-launch-radar/1.0",url],
                           capture_output=True, text=True, timeout=timeout+5)
        if r.returncode == 0:
            return r.stdout
    except Exception:
        pass
    return ""

# ---- Product Hunt ----
ph_raw = curl("https://www.producthunt.com/feed")
ph_available = bool(ph_raw)
ph_items = []
if ph_available:
    for e in re.findall(r"<entry>(.*?)</entry>", ph_raw, re.S):
        t = re.search(r"<title>(.*?)</title>", e, re.S)
        l = re.search(r'<link[^>]*href="(.*?)"', e)
        p = re.search(r"<published>(.*?)</published>", e, re.S)
        c = re.search(r"<content[^>]*>(.*?)</content>", e, re.S)
        title = html.unescape(t.group(1)).strip() if t else ""
        link = l.group(1).strip() if l else ""
        pub = p.group(1).strip() if p else ""
        content = html.unescape(c.group(1)) if c else ""
        content = re.sub(r"<[^>]+>", " ", content)
        content = re.sub(r"\s+", " ", content).strip()
        try:
            pubdt = datetime.datetime.fromisoformat(pub)
            if pubdt.tzinfo is None:
                pubdt = pubdt.replace(tzinfo=datetime.timezone.utc)
        except Exception:
            pubdt = None
        ph_items.append({"title":title,"link":link,"pub":pub,"pubdt":pubdt,"content":content})

ph_recent = [i for i in ph_items if i["pubdt"] and i["pubdt"] >= WINDOW]

print("=== PH ===")
print("PH_AVAILABLE", ph_available)
print("PH_ITEMS_TOTAL", len(ph_items))
print("PH_ITEMS_RECENT", len(ph_recent))
for i in ph_recent:
    print("--ITEM--")
    print("title:", i["title"])
    print("link:", i["link"])
    print("pub:", i["pub"])
    print("content:", i["content"][:400])

# ---- Hacker News Algolia ----
hn_hits = {}
hn_queries = 0
hn_failures = 0
for kw in KEYWORDS:
    for tag in ["show_hn","story"]:
        hn_queries += 1
        q = urllib.parse.quote(kw)
        url = f"https://hn.algolia.com/api/v1/search?tags={tag}&query={q}&hitsPerPage=50"
        body = curl(url)
        if not body:
            hn_failures += 1
            time.sleep(1)
            continue
        try:
            data = json.loads(body)
        except Exception:
            hn_failures += 1
            time.sleep(1)
            continue
        for h in data.get("hits", []):
            oid = h.get("objectID")
            if oid and oid not in hn_hits:
                hn_hits[oid] = h
        time.sleep(1)

print("=== HN ===")
print("HN_QUERIES", hn_queries)
print("HN_FAILURES", hn_failures)
print("HN_UNIQUE_HITS", len(hn_hits))

hn_recent = []
for oid, h in hn_hits.items():
    ts = h.get("created_at_i")
    if not ts:
        continue
    dt = datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc)
    if dt >= WINDOW:
        hn_recent.append(h)
print("HN_RECENT", len(hn_recent))
for h in hn_recent:
    print("--HIT--")
    print("objectID:", h.get("objectID"))
    print("title:", h.get("title"))
    print("url:", h.get("url"))
    print("points:", h.get("points"))
    print("created_at:", h.get("created_at"))
    print("author:", h.get("author"))
    st = (h.get("story_text") or "")
    st = re.sub(r"<[^>]+>"," ", html.unescape(st))
    st = re.sub(r"\s+"," ", st).strip()
    print("story_text:", st[:400])
