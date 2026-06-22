#!/usr/bin/env python3
"""skill-graph helper: fingerprint, parse, lint, render."""
import os, sys, re, json, glob, hashlib, subprocess
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent
SKILLS_DIR = ROOT / "skills"
DOCS_OUT = ROOT / "docs" / "skill-graph.md"
STATE_FILE = ROOT / "memory" / "topics" / "skill-graph-state.json"
TODAY = os.environ.get("AEON_TODAY", "2026-06-21")

def sha1(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()

def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""

def list_skill_files():
    return sorted(SKILLS_DIR.glob("*/SKILL.md"))

def parse_frontmatter(text: str):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_raw = text[3:end].strip()
    body = text[end+4:]
    meta = {}
    current_key = None
    for line in fm_raw.splitlines():
        if not line.strip():
            continue
        m = re.match(r"^([a-zA-Z_][\w-]*)\s*:\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val.startswith("[") and val.endswith("]"):
                items = [x.strip().strip('"').strip("'") for x in val[1:-1].split(",") if x.strip()]
                meta[key] = items
            elif val:
                meta[key] = val.strip().strip('"').strip("'")
            else:
                meta[key] = []
            current_key = key
        elif line.startswith("- ") and current_key:
            v = line[2:].strip().strip('"').strip("'")
            if isinstance(meta.get(current_key), list):
                meta[current_key].append(v)
    return meta, body

def fingerprint():
    parts = []
    for p in [ROOT / "aeon.yml", ROOT / "skills.json"]:
        parts.append(sha1(read(p)) + "  " + p.name)
    for f in list_skill_files():
        text = read(f)
        meta, body = parse_frontmatter(text)
        for line in (json.dumps(meta, sort_keys=True)).splitlines():
            parts.append(f"{f}: {line}")
        for line in text.splitlines():
            if re.match(r"^depends_on:|^- skill:|consume:|parallel:|trigger:", line):
                parts.append(line)
        refs = sorted(set(re.findall(r"memory/(?:topics|state)/[a-zA-Z0-9_.-]+", text)))
        parts.extend(refs)
    blob = "\n".join(parts) + "\n"
    return sha1(blob)

def load_state():
    if not STATE_FILE.exists():
        return None
    try:
        return json.loads(STATE_FILE.read_text())
    except Exception:
        return None

def parse_aeon_yml():
    """Minimal YAML parse: per-skill enabled/schedule/var/model; chains; reactive."""
    text = read(ROOT / "aeon.yml")
    skills = {}
    chains = {}
    reactive = {}
    lines = text.splitlines()
    section = None
    cur_skill = None
    cur_chain = None
    cur_reactive = None
    cur_step = None
    chain_indent = None
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        if not stripped or stripped.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        s = line.strip()
        if indent == 0:
            if s.startswith("skills:"):
                section = "skills"; cur_skill = None; cur_chain = None; cur_reactive = None
                continue
            if s.startswith("chains:"):
                section = "chains"; cur_chain = None
                continue
            if s.startswith("reactive:"):
                section = "reactive"; cur_reactive = None
                continue
            section = None
            continue
        if section == "skills":
            if indent == 2 and s.endswith(":"):
                cur_skill = s[:-1].strip()
                skills[cur_skill] = {"enabled": False}
                continue
            if cur_skill and indent >= 4:
                m = re.match(r"^([a-zA-Z_][\w-]*)\s*:\s*(.*)$", s)
                if m:
                    k, v = m.group(1), m.group(2).strip()
                    if v.lower() in ("true", "false"):
                        skills[cur_skill][k] = (v.lower() == "true")
                    elif v:
                        skills[cur_skill][k] = v.strip().strip('"').strip("'")
        elif section == "chains":
            if indent == 2 and s.endswith(":"):
                cur_chain = s[:-1].strip()
                chains[cur_chain] = {"steps": []}
                cur_step = None
                continue
            if cur_chain and indent == 4:
                m = re.match(r"^([a-zA-Z_][\w-]*)\s*:\s*(.*)$", s)
                if m:
                    chains[cur_chain][m.group(1)] = m.group(2).strip()
            if cur_chain and s.startswith("- ") and indent >= 6:
                step_body = s[2:].strip()
                cur_step = {}
                chains[cur_chain]["steps"].append(cur_step)
                if step_body.startswith("parallel:"):
                    arr = step_body.split(":", 1)[1].strip()
                    if arr.startswith("[") and arr.endswith("]"):
                        cur_step["parallel"] = [x.strip() for x in arr[1:-1].split(",") if x.strip()]
                elif step_body.startswith("skill:"):
                    cur_step["skill"] = step_body.split(":", 1)[1].strip()
                elif step_body.startswith("consume:"):
                    arr = step_body.split(":", 1)[1].strip()
                    if arr.startswith("[") and arr.endswith("]"):
                        cur_step["consume"] = [x.strip() for x in arr[1:-1].split(",") if x.strip()]
            elif cur_step and indent >= 8:
                m = re.match(r"^([a-zA-Z_][\w-]*)\s*:\s*(.*)$", s)
                if m:
                    k, v = m.group(1), m.group(2).strip()
                    if v.startswith("[") and v.endswith("]"):
                        cur_step[k] = [x.strip() for x in v[1:-1].split(",") if x.strip()]
                    else:
                        cur_step[k] = v
        elif section == "reactive":
            if indent == 2 and s.endswith(":"):
                cur_reactive = s[:-1].strip()
                reactive[cur_reactive] = {}
                continue
            if cur_reactive and indent >= 4:
                m = re.match(r"^([a-zA-Z_][\w-]*)\s*:\s*(.*)$", s)
                if m:
                    reactive[cur_reactive][m.group(1)] = m.group(2).strip()
    return skills, chains, reactive

def parse_skills_json():
    text = read(ROOT / "skills.json")
    if not text:
        return {}
    try:
        data = json.loads(text)
    except Exception:
        return {}
    cat_map = {}
    if isinstance(data, dict):
        if "categories" in data:
            for cat, lst in data["categories"].items():
                for s in lst:
                    cat_map[s] = cat
        else:
            for k, v in data.items():
                if isinstance(v, dict) and "category" in v:
                    cat_map[k] = v["category"]
                elif isinstance(v, list):
                    for s in v:
                        cat_map[s] = k
    elif isinstance(data, list):
        for entry in data:
            if isinstance(entry, dict):
                slug = entry.get("slug") or entry.get("name")
                cat = entry.get("category")
                if slug and cat:
                    cat_map[slug] = cat
    return cat_map

def classify(slug, tags, cat_map):
    if slug in cat_map:
        return cat_map[slug]
    if tags:
        for t in tags:
            if t in ("research", "dev", "crypto", "social", "productivity", "meta"):
                return "dev" if t == "meta" else t
        return tags[0] if tags else "other"
    return "other"

def derive_shared_state(skill_data):
    """Returns list of (writer, reader, topic) tuples."""
    writes = defaultdict(set)
    reads = defaultdict(set)
    for slug, d in skill_data.items():
        text = d["text"]
        lines = text.splitlines()
        for i, line in enumerate(lines):
            for m in re.finditer(r"memory/(topics|state)/[a-zA-Z0-9_.-]+", line):
                ref = m.group(0)
                ctx = "\n".join(lines[max(0,i-1):min(len(lines),i+2)]).lower()
                if re.search(r"(write|save|append|>|update)\b.*(topics|state)/", ctx) or re.search(r"echo .*>>?.*" + re.escape(ref), ctx):
                    writes[ref].add(slug)
                else:
                    reads[ref].add(slug)
    edges = []
    for ref in writes:
        for w in writes[ref]:
            for r in reads.get(ref, set()):
                if r != w:
                    edges.append((w, r, ref))
    return edges

def gather():
    skills_yml, chains, reactive = parse_aeon_yml()
    cat_map = parse_skills_json()
    skill_data = {}
    for f in list_skill_files():
        slug = f.parent.name
        text = read(f)
        meta, body = parse_frontmatter(text)
        name = meta.get("name", slug)
        tags = meta.get("tags") if isinstance(meta.get("tags"), list) else []
        depends_on = meta.get("depends_on") if isinstance(meta.get("depends_on"), list) else []
        yml_entry = skills_yml.get(slug, {})
        enabled = bool(yml_entry.get("enabled", False))
        schedule = yml_entry.get("schedule") or yml_entry.get("cron") or ""
        category = classify(slug, tags, cat_map)
        skill_data[slug] = {
            "slug": slug,
            "name": name,
            "tags": tags,
            "depends_on": depends_on,
            "enabled": enabled,
            "schedule": schedule,
            "category": category,
            "text": text,
        }
    shared_edges = derive_shared_state(skill_data)
    consume_edges = []
    chain_edges = []
    for chain, body in chains.items():
        prev_set = []
        for step in body.get("steps", []):
            if "parallel" in step:
                cur = step["parallel"]
                for s in cur:
                    if prev_set:
                        for p in prev_set:
                            chain_edges.append((p, s, chain))
                prev_set = cur
            elif "skill" in step:
                cur = [step["skill"]]
                consume = step.get("consume", [])
                for src in consume:
                    consume_edges.append((src, step["skill"], chain))
                if prev_set and not consume:
                    for p in prev_set:
                        chain_edges.append((p, step["skill"], chain))
                prev_set = cur
    reactive_edges = []
    for slug, body in reactive.items():
        trig = body.get("trigger") or body.get("on")
        if trig:
            reactive_edges.append((trig, slug))
    depends_edges = []
    for slug, d in skill_data.items():
        for dep in d["depends_on"]:
            depends_edges.append((dep, slug))
    return skill_data, depends_edges, consume_edges, reactive_edges, shared_edges, chains, reactive

def lint(diagram, declared, valid_paths):
    issues = []
    bracket_pat = re.compile(r"\[([^\]]*)\]")
    if diagram.count("[") != diagram.count("]"):
        issues.append("unbalanced brackets")
    subgraph_open = diagram.count("subgraph ")
    subgraph_close = len(re.findall(r"^end\s*$", diagram, re.MULTILINE))
    if subgraph_open != subgraph_close:
        issues.append(f"subgraph blocks: {subgraph_open} open vs {subgraph_close} close")
    for m in re.finditer(r"click ([a-zA-Z0-9_-]+) \"([^\"]+)\"", diagram):
        node, path = m.group(1), m.group(2)
        if node not in declared:
            issues.append(f"click on undeclared node: {node}")
        full = (DOCS_OUT.parent / path).resolve()
        if not full.exists():
            issues.append(f"click path missing: {path}")
    return issues

def render_label(d):
    base = d["slug"]
    if d["enabled"] and d.get("schedule"):
        return f'{base}["{base}<br/>⏰ {d["schedule"]}"]'
    return f'{base}["{base}"]'

def category_classes(d):
    return "enabled" if d["enabled"] else "disabled"

def render(skill_data, depends, consume, reactive, shared, chains, reactive_blocks, mode, prev_state, fp):
    enabled_count = sum(1 for d in skill_data.values() if d["enabled"])
    by_cat = defaultdict(list)
    for slug, d in skill_data.items():
        by_cat[d["category"]].append(slug)
    for c in by_cat:
        by_cat[c].sort()
    declared = set(skill_data.keys())

    edges_total = {
        "depends_on": len(depends),
        "consume": len(consume),
        "reactive": len(reactive),
        "shared_state": len(shared),
    }

    cur_nodes = sorted(skill_data.keys())
    cur_edges = sorted({(a,b,"dep") for a,b in depends} |
                       {(a,b,"con") for a,b,_ in consume} |
                       {(a,b,"rx") for a,b in reactive} |
                       {(a,b,"shr") for a,b,_ in shared})
    node_sha = sha1("\n".join(cur_nodes))
    edge_sha = sha1("\n".join(f"{a}->{b}:{t}" for a,b,t in cur_edges))

    prior_nodes = []
    prior_edges_dep = []
    if DOCS_OUT.exists():
        prior_text = read(DOCS_OUT)
    else:
        prior_text = ""

    verdict_parts = []
    new_skills = []
    retired_skills = []
    new_enabled = []
    new_dep_edges = []
    if prev_state:
        prev_node_sha = prev_state.get("node_list_sha")
        prev_edge_sha = prev_state.get("edge_list_sha")
        if prev_node_sha != node_sha or prev_edge_sha != edge_sha:
            prev_nodes_total = prev_state.get("skills_total", 0)
            if len(cur_nodes) > prev_nodes_total:
                verdict_parts.append(f"NEW_SKILLS: +{len(cur_nodes) - prev_nodes_total}")
            elif len(cur_nodes) < prev_nodes_total:
                verdict_parts.append(f"RETIRED_SKILLS: -{prev_nodes_total - len(cur_nodes)}")
            prev_enabled = prev_state.get("enabled_count", 0)
            if enabled_count != prev_enabled:
                verdict_parts.append(f"ENABLED_DELTA: {prev_enabled}→{enabled_count}")
            prev_edges = prev_state.get("edges", {})
            for k, v in edges_total.items():
                pv = prev_edges.get(k, 0)
                if v != pv:
                    verdict_parts.append(f"{k.upper()}_EDGES: {pv}→{v}")
    if not verdict_parts:
        verdict = "ARCHITECTURE_OK"
    else:
        verdict = " · ".join(verdict_parts)

    lines = []
    lines.append("# Skill Dependency Graph")
    lines.append("")
    lines.append(f"_Auto-generated by skill-graph on {TODAY} · Mode: `{mode}`_")
    lines.append("")
    lines.append(f"**Verdict:** `{verdict}`")
    lines.append("")
    if mode != "SKILL_GRAPH_NEW":
        lines.append("## What changed since last run")
        lines.append("")
        if prev_state:
            lines.append(f"- Skills: {prev_state.get('skills_total','?')} → **{len(cur_nodes)}**")
            lines.append(f"- Enabled: {prev_state.get('enabled_count','?')} → **{enabled_count}**")
            prev_edges = prev_state.get("edges", {})
            for k, v in edges_total.items():
                pv = prev_edges.get(k, 0)
                lines.append(f"- {k}: {pv} → **{v}**")
        else:
            lines.append("_No prior state — full regeneration._")
        lines.append("")

    lines.append("## Overview")
    lines.append("")
    lines.append("```mermaid")
    lines.append("flowchart LR")
    cat_counts = {c: len(v) for c, v in by_cat.items()}
    for c, count in sorted(cat_counts.items()):
        cat_id = c.replace("-", "_")
        lines.append(f'  {cat_id}["{c}<br/>({count} skills)"]')
    cross_counts = defaultdict(int)
    for a, b in depends:
        ca = skill_data.get(a, {}).get("category")
        cb = skill_data.get(b, {}).get("category")
        if ca and cb and ca != cb:
            cross_counts[(ca, cb)] += 1
    for a, b, _ in shared:
        ca = skill_data.get(a, {}).get("category")
        cb = skill_data.get(b, {}).get("category")
        if ca and cb and ca != cb:
            cross_counts[(ca, cb)] += 1
    for (ca, cb), n in sorted(cross_counts.items()):
        a_id = ca.replace("-", "_")
        b_id = cb.replace("-", "_")
        lines.append(f'  {a_id} -->|{n}| {b_id}')
    lines.append("```")
    lines.append("")

    healing = ["heartbeat", "skill-health", "skill-evals", "skill-repair", "self-improve"]
    if all(s in skill_data for s in healing):
        lines.append("## Self-healing loop")
        lines.append("")
        lines.append("```mermaid")
        lines.append("flowchart LR")
        for s in healing:
            sid = s.replace("-", "_")
            lines.append(f'  {sid}["{s}"]')
        lines.append('  state[("memory/cron-state.json")]')
        for i in range(len(healing) - 1):
            a = healing[i].replace("-", "_")
            b = healing[i+1].replace("-", "_")
            lines.append(f"  {a} --> {b}")
        for s in healing:
            sid = s.replace("-", "_")
            lines.append(f"  {sid} -.-> state")
        lines.append("```")
        lines.append("")

    intra_dep = defaultdict(list)
    for a, b in depends:
        ca = skill_data.get(a, {}).get("category")
        cb = skill_data.get(b, {}).get("category")
        if ca == cb and ca:
            intra_dep[ca].append((a, b))
    intra_shared = defaultdict(list)
    cross_shared = defaultdict(list)
    for a, b, ref in shared:
        ca = skill_data.get(a, {}).get("category")
        cb = skill_data.get(b, {}).get("category")
        if ca == cb and ca:
            intra_shared[ca].append((a, b, ref))
        elif ca and cb:
            cross_shared[ca].append((a, b, ref))

    lines.append("## Per-category")
    lines.append("")
    for cat in sorted(by_cat.keys()):
        slugs = by_cat[cat]
        lines.append(f"### {cat} ({len(slugs)} skills)")
        lines.append("")
        lines.append("```mermaid")
        lines.append("flowchart LR")
        for slug in slugs:
            d = skill_data[slug]
            sid = slug.replace("-", "_")
            label = slug
            if d["enabled"] and d["schedule"]:
                label = f'{slug}<br/>⏰ {d["schedule"]}'
            elif d["enabled"]:
                label = f'{slug} ⏰'
            lines.append(f'  {sid}["{label}"]')
        ext_nodes = set()
        for a, b in depends:
            ca = skill_data.get(a, {}).get("category")
            cb = skill_data.get(b, {}).get("category")
            if cb == cat and ca != cat:
                ext_nodes.add(a)
        for a, b, _ in shared:
            ca = skill_data.get(a, {}).get("category")
            cb = skill_data.get(b, {}).get("category")
            if cb == cat and ca != cat:
                ext_nodes.add(a)
        for ext in sorted(ext_nodes)[:8]:
            sid = ext.replace("-", "_")
            if sid not in {s.replace("-","_") for s in slugs}:
                lines.append(f'  {sid}["{ext}"]:::external')
        for a, b in intra_dep.get(cat, []):
            lines.append(f"  {a.replace('-','_')} --> {b.replace('-','_')}")
        seen_shared = set()
        for a, b, ref in intra_shared.get(cat, []):
            key = (a, b)
            if key in seen_shared:
                continue
            seen_shared.add(key)
            lines.append(f"  {a.replace('-','_')} -..-> {b.replace('-','_')}")
        for a, b in depends:
            ca = skill_data.get(a, {}).get("category")
            cb = skill_data.get(b, {}).get("category")
            if cb == cat and ca != cat and a in ext_nodes:
                lines.append(f"  {a.replace('-','_')} --> {b.replace('-','_')}")
        for slug in slugs:
            d = skill_data[slug]
            cls = "enabled" if d["enabled"] else "disabled"
            lines.append(f"  class {slug.replace('-','_')} {cls}")
            lines.append(f'  click {slug.replace("-","_")} "../skills/{slug}/SKILL.md"')
        for ext in sorted(ext_nodes)[:8]:
            sid = ext.replace("-", "_")
            if sid not in {s.replace("-","_") for s in slugs}:
                lines.append(f'  click {sid} "../skills/{ext}/SKILL.md"')
        lines.append("  classDef enabled fill:#fff,stroke:#000,stroke-width:2px,color:#000")
        lines.append("  classDef disabled fill:#f5f5f5,stroke:#bbb,color:#888")
        lines.append("  classDef external fill:none,stroke:#bbb,stroke-dasharray:3 3,color:#888")
        lines.append("```")
        lines.append("")

    lines.append("## Legend")
    lines.append("")
    lines.append("- `-->` `depends_on` (explicit frontmatter)")
    lines.append("- `-.->` `consume` (chain output passing)")
    lines.append("- `-..->` shared-state / reactive (derived from `memory/topics` & `memory/state` references)")
    lines.append("- **Bold border** = `enabled: true` in `aeon.yml` (schedule shown inline when present)")
    lines.append("- Faded grey = currently disabled")
    lines.append("- Dashed ghost nodes (`:::external`) = cross-category dependency, click through to source")
    lines.append("- Click any node to jump to its `SKILL.md`")
    lines.append("- _Note: every skill writes `memory/cron-state.json` — collapsed into the self-healing legend rather than rendered as N edges._")
    lines.append("")

    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|---|---|")
    lines.append(f"| Total skills | {len(skill_data)} |")
    lines.append(f"| Enabled | {enabled_count} |")
    lines.append(f"| Disabled | {len(skill_data) - enabled_count} |")
    lines.append(f"| `depends_on` edges | {edges_total['depends_on']} |")
    lines.append(f"| `consume` edges | {edges_total['consume']} |")
    lines.append(f"| `reactive` edges | {edges_total['reactive']} |")
    lines.append(f"| shared-state edges | {edges_total['shared_state']} |")
    lines.append("")
    lines.append("| Category | Skills |")
    lines.append("|---|---|")
    for c in sorted(by_cat.keys()):
        lines.append(f"| {c} | {len(by_cat[c])} |")
    lines.append("")

    footer = (f"skills parsed: {len(skill_data)} · depends_on: {edges_total['depends_on']} · "
              f"consume: {edges_total['consume']} · reactive: {edges_total['reactive']} · "
              f"shared-state derived: {edges_total['shared_state']} · "
              f"enabled: {enabled_count}/{len(skill_data)} · mode: {mode}")
    lines.append("---")
    lines.append("")
    lines.append(f"_{footer}_")
    lines.append("")

    diagram = "\n".join(lines)
    return diagram, edges_total, verdict, node_sha, edge_sha, footer

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "run"
    if cmd == "fingerprint":
        print(fingerprint())
        return
    fp = fingerprint()
    prev = load_state()
    if prev is None:
        mode = "SKILL_GRAPH_NEW"
    elif prev.get("input_fingerprint") == fp:
        mode = "SKILL_GRAPH_NO_CHANGE"
    else:
        mode = "SKILL_GRAPH_OK"
    if cmd == "check":
        print(json.dumps({"mode": mode, "fingerprint": fp, "prev_fp": prev.get("input_fingerprint") if prev else None}))
        return
    if cmd == "render":
        skill_data, depends, consume, reactive_edges, shared, chains, reactive_blocks = gather()
        text, edges_total, verdict, node_sha, edge_sha, footer = render(
            skill_data, depends, consume, reactive_edges, shared, chains, reactive_blocks, mode, prev, fp
        )
        declared = set(d["slug"].replace("-", "_") for d in skill_data.values())
        issues = lint(text, declared, set())
        result = {
            "mode": mode,
            "fingerprint": fp,
            "verdict": verdict,
            "skills_total": len(skill_data),
            "enabled_count": sum(1 for d in skill_data.values() if d["enabled"]),
            "edges": edges_total,
            "node_list_sha": node_sha,
            "edge_list_sha": edge_sha,
            "lint_issues": issues,
            "footer": footer,
        }
        if issues:
            print(json.dumps(result, indent=2))
            return
        DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
        DOCS_OUT.write_text(text)
        state = {
            "generated_at": TODAY,
            "input_fingerprint": fp,
            "skills_total": len(skill_data),
            "enabled_count": result["enabled_count"],
            "edges": edges_total,
            "node_list_sha": node_sha,
            "edge_list_sha": edge_sha,
        }
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATE_FILE.write_text(json.dumps(state, indent=2) + "\n")
        print(json.dumps(result, indent=2))
        return

if __name__ == "__main__":
    main()
