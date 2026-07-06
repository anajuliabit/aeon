#!/usr/bin/env python3
"""skill-graph builder — parses aeon.yml, skills.json, all SKILL.md, builds Mermaid doc."""
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path("/home/runner/work/aeon/aeon")
OUT = ROOT / "docs/skill-graph.md"
STATE_FILE = ROOT / "memory/topics/skill-graph-state.json"
TODAY = "2026-06-28"

# ------------------- Step 1: Fingerprint -------------------
def sha1(data):
    return hashlib.sha1(data).hexdigest()

def file_sha1(path):
    return sha1(path.read_bytes())

def build_fingerprint():
    parts = []
    parts.append(f"{file_sha1(ROOT/'aeon.yml')}  aeon.yml")
    parts.append(f"{file_sha1(ROOT/'skills.json')}  skills.json")
    content = []
    for skill_md in sorted((ROOT/"skills").glob("*/SKILL.md")):
        text = skill_md.read_text(errors="replace")
        # frontmatter only (between first two ---)
        m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
        if m:
            for line in m.group(1).splitlines():
                content.append(f"{skill_md}: {line}")
        # grep -hE '^depends_on:|^- skill:|consume:|parallel:|trigger:'
        for line in text.splitlines():
            if re.match(r"^(depends_on:|- skill:|consume:|parallel:|trigger:)", line):
                content.append(line)
        # memory refs
        refs = set(re.findall(r"memory/(?:topics|state)/[a-zA-Z0-9_.\-]+", text))
        content.extend(sorted(refs))
    content_hash = sha1("\n".join(content).encode())
    fingerprint = sha1(("\n".join(parts) + "\n" + content_hash).encode())
    return fingerprint

# ------------------- Step 2: Parse inputs -------------------
def parse_aeon_yml():
    """Custom parser — aeon.yml uses inline-flow YAML mixed with block. Use a tolerant approach."""
    text = (ROOT / "aeon.yml").read_text()
    skills = {}
    chains = {}
    reactive = {}
    # Find skills: block
    in_skills = False
    in_chains = False
    in_reactive = False
    current_chain = None
    current_reactive = None
    pending_steps = []
    for line in text.splitlines():
        stripped = line.rstrip()
        if re.match(r"^skills:\s*$", stripped):
            in_skills, in_chains, in_reactive = True, False, False
            continue
        if re.match(r"^chains:\s*$", stripped):
            in_skills, in_chains, in_reactive = False, True, False
            continue
        if re.match(r"^reactive:\s*$", stripped):
            in_skills, in_chains, in_reactive = False, False, True
            continue
        if re.match(r"^[a-z_]+:\s*$", stripped) and not line.startswith(" "):
            in_skills = in_chains = in_reactive = False
            continue
        if in_skills:
            # Match "  slug: { enabled: true, schedule: "...", var: "...", model: "..." }"
            # Or "  slug:" (no inline)
            m = re.match(r"^  ([a-z0-9_-]+):\s*(.*)$", line)
            if m:
                slug, rest = m.group(1), m.group(2).strip()
                rec = {"enabled": False, "schedule": "", "var": "", "model": ""}
                if rest.startswith("{"):
                    inner = rest.rstrip("}").lstrip("{").strip()
                    parts = re.findall(r'(\w+)\s*:\s*(true|false|"[^"]*"|\S+?)(?=,|\s*}|$)', inner + ",")
                    for k, v in parts:
                        if v.startswith('"') and v.endswith('"'):
                            v = v[1:-1]
                        elif v in ("true", "false"):
                            v = (v == "true")
                        rec[k] = v
                skills[slug] = rec
        if in_chains:
            # parse minimal: chain_name: { schedule, steps: [...] } — multi-line YAML
            m = re.match(r"^  ([a-z0-9_-]+):\s*$", line)
            if m:
                current_chain = m.group(1)
                chains[current_chain] = {"schedule": "", "steps": [], "on_error": ""}
                continue
            if current_chain:
                m2 = re.match(r"^\s+schedule:\s*\"?([^\"]+)\"?", line)
                if m2:
                    chains[current_chain]["schedule"] = m2.group(1)
                m3 = re.match(r"^\s+on_error:\s*(\S+)", line)
                if m3:
                    chains[current_chain]["on_error"] = m3.group(1)
                # parallel: [a, b]
                mp = re.match(r"^\s+-\s*parallel:\s*\[(.+)\]", line)
                if mp:
                    items = [x.strip().strip('"') for x in mp.group(1).split(",")]
                    chains[current_chain]["steps"].append({"parallel": items, "consume": []})
                ms = re.match(r"^\s+-\s*skill:\s*([\w-]+)", line)
                if ms:
                    chains[current_chain]["steps"].append({"skill": ms.group(1), "consume": []})
                mc = re.match(r"^\s+consume:\s*\[(.+)\]", line)
                if mc and chains[current_chain]["steps"]:
                    items = [x.strip().strip('"') for x in mc.group(1).split(",")]
                    chains[current_chain]["steps"][-1]["consume"] = items
        if in_reactive:
            m = re.match(r"^  ([a-z0-9_-]+):\s*$", line)
            if m:
                current_reactive = m.group(1)
                reactive[current_reactive] = {"trigger": "", "on": "", "when": ""}
                continue
            if current_reactive:
                for key in ("trigger", "on", "when"):
                    mr = re.match(rf"^\s+{key}:\s*\"?([^\"]+)\"?", line)
                    if mr:
                        reactive[current_reactive][key] = mr.group(1)
    return skills, chains, reactive

def parse_skill_md(path):
    text = path.read_text(errors="replace")
    fm = {}
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            kv = re.match(r"^([a-z_]+):\s*(.*)$", line)
            if kv:
                k, v = kv.group(1), kv.group(2).strip()
                fm[k] = v
    depends_on = []
    m2 = re.search(r"^depends_on:\s*\[(.+?)\]", text, re.M)
    if m2:
        depends_on = [x.strip().strip('"').strip("'") for x in m2.group(1).split(",")]
    # also support block-list depends_on
    if not depends_on:
        m3 = re.search(r"^depends_on:\s*\n((?:^- .+\n)+)", text, re.M)
        if m3:
            depends_on = [re.sub(r"^- ", "", l).strip().strip('"').strip("'") for l in m3.group(1).splitlines()]
    # tags
    tags = []
    mt = re.search(r"^tags:\s*\[(.+?)\]", text, re.M)
    if mt:
        tags = [x.strip().strip('"').strip("'") for x in mt.group(1).split(",")]
    return {
        "name": fm.get("name", path.parent.name),
        "tags": tags,
        "depends_on": depends_on,
        "raw": text,
    }

def parse_skills_json():
    data = json.loads((ROOT / "skills.json").read_text())
    cat_map = {s["slug"]: s["category"] for s in data["skills"]}
    return cat_map

# ------------------- Step 2/3: Build derived edges -------------------
WRITE_VERBS = re.compile(r"(?:^|\s)(?:write|writes|save|saved|saves|append|appends|appended|update|updates|updated|>{1,2})\s+[^\n]*?memory/(topics|state)/", re.IGNORECASE)
WRITE_LINE = re.compile(r"(write|writes|save|saved|saves|append|appends|appended|updates|update|updated|>)", re.IGNORECASE)

def classify_memory_refs(skill_text):
    """Per-skill: collect memory refs and classify each as write or read."""
    refs = defaultdict(set)  # 'read' or 'write' -> set of paths
    lines = skill_text.splitlines()
    for i, line in enumerate(lines):
        for match in re.finditer(r"memory/(?:topics|state)/[a-zA-Z0-9_.\-]+", line):
            ref = match.group(0)
            # Look at surrounding 3 lines for write verbs
            window = "\n".join(lines[max(0, i-1):i+2]).lower()
            if WRITE_LINE.search(window):
                refs["write"].add(ref)
            else:
                refs["read"].add(ref)
    return refs

# ------------------- Step 5: Generate document -------------------
def slugify(s):
    return re.sub(r"[^a-zA-Z0-9]", "_", s)

def sched_short(s):
    return s if s else ""

def lint_mermaid(blocks, declared_nodes, click_paths):
    """Validate Mermaid for matching brackets, subgraph/end pairs, click paths."""
    errors = []
    for label, block in blocks:
        opens = block.count("[")
        closes = block.count("]")
        if opens != closes:
            errors.append(f"{label}: bracket mismatch [={opens} ]={closes}")
        sgs = len(re.findall(r"^\s*subgraph\b", block, re.M))
        ends = len(re.findall(r"^\s*end\s*$", block, re.M))
        if sgs != ends:
            errors.append(f"{label}: subgraph={sgs} end={ends}")
    for click_node, click_path in click_paths:
        # path is relative from docs/ — check exists at root + path
        resolved = (OUT.parent / click_path).resolve()
        if not resolved.exists():
            errors.append(f"click path missing: {click_path} (node {click_node})")
    return errors

def main():
    fingerprint = build_fingerprint()
    print(f"FINGERPRINT={fingerprint}", file=sys.stderr)

    # Check prior state
    prior = {}
    if STATE_FILE.exists():
        prior = json.loads(STATE_FILE.read_text())
    prior_fp = prior.get("input_fingerprint")
    if prior_fp == fingerprint:
        # NO_CHANGE — exit silently, append log
        log = ROOT / f"memory/logs/{TODAY}.md"
        log.parent.mkdir(parents=True, exist_ok=True)
        existing = log.read_text() if log.exists() else ""
        existing += f"\n## skill-graph\nSKILL_GRAPH_NO_CHANGE — identical fingerprint {fingerprint[:12]}\n"
        log.write_text(existing)
        print("NO_CHANGE", file=sys.stderr)
        return 0

    mode = "SKILL_GRAPH_NEW" if not prior else "SKILL_GRAPH_OK"

    # Parse
    cfg, chains, reactive = parse_aeon_yml()
    cat_map = parse_skills_json()
    skill_dirs = sorted([d for d in (ROOT/"skills").iterdir() if d.is_dir() and (d/"SKILL.md").exists()])

    skills = {}
    for sd in skill_dirs:
        slug = sd.name
        sm = parse_skill_md(sd / "SKILL.md")
        # category fallback to first tag if not in skills.json
        cat = cat_map.get(slug, sm["tags"][0] if sm["tags"] else "other")
        if cat == "other":
            # fall back to first tag if available
            if sm["tags"]:
                cat = sm["tags"][0]
        cfg_entry = cfg.get(slug, {"enabled": False, "schedule": "", "var": "", "model": ""})
        skills[slug] = {
            **sm,
            "slug": slug,
            "category": cat,
            "enabled": cfg_entry.get("enabled", False),
            "schedule": cfg_entry.get("schedule", ""),
            "var": cfg_entry.get("var", ""),
            "model": cfg_entry.get("model", ""),
        }

    # Categorize
    cats = defaultdict(list)
    for slug, s in skills.items():
        cats[s["category"]].append(slug)
    for c in cats:
        cats[c].sort()
    # Order categories
    cat_order = ["research", "dev", "crypto", "social", "productivity", "other"]
    ordered_cats = [c for c in cat_order if c in cats] + [c for c in sorted(cats) if c not in cat_order]

    # Derive shared-state edges
    writers = defaultdict(set)  # path -> set of writer slugs
    readers = defaultdict(set)  # path -> set of reader slugs
    for slug, s in skills.items():
        refs = classify_memory_refs(s["raw"])
        for r in refs["write"]:
            writers[r].add(slug)
        for r in refs["read"]:
            readers[r].add(slug)

    # Exclude universal cron-state.json
    EXCLUDE = {"memory/cron-state.json", "memory/state/cron-state.json", "memory/cron-state"}
    shared_state_edges = []  # (writer, reader, path)
    for path in sorted(set(writers) | set(readers)):
        if path in EXCLUDE or "cron-state" in path:
            continue
        for w in sorted(writers[path]):
            for r in sorted(readers[path]):
                if w != r:
                    shared_state_edges.append((w, r, path))

    # depends_on edges
    depends_edges = []
    for slug, s in skills.items():
        for dep in s["depends_on"]:
            if dep in skills:
                depends_edges.append((slug, dep))

    # chain edges (consume = dashed)
    chain_edges = []  # (from_skill, to_skill, chain_name)
    for cn, c in chains.items():
        # For each step with consume, build edges from each producer to this consumer
        for step in c["steps"]:
            if "skill" in step and step.get("consume"):
                for prod in step["consume"]:
                    if prod in skills and step["skill"] in skills:
                        chain_edges.append((prod, step["skill"], cn))

    # reactive edges
    reactive_edges = []
    for trig_skill, r in reactive.items():
        on_skill = r.get("on", "")
        if on_skill in skills and trig_skill in skills:
            reactive_edges.append((on_skill, trig_skill, "reactive"))

    # Counts
    n_total = len(skills)
    n_enabled = sum(1 for s in skills.values() if s["enabled"])
    edge_counts = {
        "depends_on": len(depends_edges),
        "consume": len(chain_edges),
        "reactive": len(reactive_edges),
        "shared_state": len(shared_state_edges),
    }

    # What-changed diff vs prior file
    diff_lines = []
    prior_total = prior.get("skills_total", 0)
    prior_enabled = prior.get("enabled_count", 0)
    prior_edges = prior.get("edges", {})
    if prior:
        if n_total != prior_total:
            diff_lines.append(f"- Skills: {prior_total} -> **{n_total}** ({n_total - prior_total:+d})")
        else:
            diff_lines.append(f"- Skills: {n_total} (no change)")
        if n_enabled != prior_enabled:
            diff_lines.append(f"- Enabled: {prior_enabled} -> **{n_enabled}** ({n_enabled - prior_enabled:+d})")
        else:
            diff_lines.append(f"- Enabled: {n_enabled} (no change)")
        for k in ("depends_on", "consume", "reactive", "shared_state"):
            pv = prior_edges.get(k, 0)
            cv = edge_counts[k]
            if pv != cv:
                diff_lines.append(f"- `{k}` edges: {pv} -> **{cv}** ({cv-pv:+d})")
            else:
                diff_lines.append(f"- `{k}` edges: {cv} (no change)")

    # Verdict line
    verdict_parts = []
    if not prior:
        verdict_parts.append(f"INITIALIZED: {n_total} skills")
    else:
        if n_total > prior_total:
            verdict_parts.append(f"NEW_SKILLS: +{n_total - prior_total}")
        elif n_total < prior_total:
            verdict_parts.append(f"RETIRED_SKILLS: {n_total - prior_total}")
        if n_enabled != prior_enabled:
            verdict_parts.append(f"ENABLED_DELTA: {n_enabled - prior_enabled:+d}")
        for k in ("depends_on", "consume", "reactive", "shared_state"):
            pv = prior_edges.get(k, 0)
            cv = edge_counts[k]
            if pv != cv:
                verdict_parts.append(f"{k.upper()}: {pv}->{cv}")
    verdict = " | ".join(verdict_parts) if verdict_parts else "ARCHITECTURE_OK"

    # ----- Mermaid build -----
    blocks = []
    click_paths = []
    declared_nodes = set()

    def mermaid_label(slug, sched=""):
        if sched:
            return f'{slugify(slug)}["{slug}<br/>({sched})"]'
        return f'{slugify(slug)}["{slug}"]'

    # Overview diagram — categories as boxes + cross-category edge counts
    overview_lines = ["```mermaid", "flowchart LR"]
    for c in ordered_cats:
        n = len(cats[c])
        overview_lines.append(f'  {slugify(c)}["{c}<br/>({n} skills)"]')
        declared_nodes.add(slugify(c))
    # Cross-cat edge counts
    cross_counts = defaultdict(int)
    for edges_list in (depends_edges, [(a, b) for a, b, _ in chain_edges],
                       [(a, b) for a, b, _ in reactive_edges],
                       [(a, b) for a, b, _ in shared_state_edges]):
        for a, b in edges_list:
            ca, cb = skills[a]["category"], skills[b]["category"]
            if ca != cb:
                cross_counts[(ca, cb)] += 1
    for (ca, cb), n in sorted(cross_counts.items()):
        overview_lines.append(f"  {slugify(ca)} -->|{n}| {slugify(cb)}")
    overview_lines.append("```")
    blocks.append(("overview", "\n".join(overview_lines)))

    # Self-healing loop callout
    sh_lines = ["```mermaid", "flowchart LR"]
    sh_chain = ["heartbeat", "skill-health", "skill-evals", "skill-repair", "self-improve"]
    for slug in sh_chain:
        if slug in skills:
            sh_lines.append(f'  {slugify(slug)}["{slug}"]')
            declared_nodes.add(slugify(slug))
    sh_lines.append('  state[("memory/cron-state.json")]')
    declared_nodes.add("state")
    for a, b in zip(sh_chain, sh_chain[1:]):
        if a in skills and b in skills:
            sh_lines.append(f"  {slugify(a)} --> {slugify(b)}")
    for slug in sh_chain:
        if slug in skills:
            sh_lines.append(f"  {slugify(slug)} -.-> state")
    sh_lines.append("```")
    blocks.append(("self_healing", "\n".join(sh_lines)))

    # Per-category mini-diagrams
    cat_blocks = []
    for cat in ordered_cats:
        slugs = cats[cat]
        lines = ["```mermaid", "flowchart LR"]
        for slug in slugs:
            sched = skills[slug]["schedule"]
            lines.append(f"  {mermaid_label(slug, sched)}")
            declared_nodes.add(slugify(slug))
            click_paths.append((slugify(slug), f"../skills/{slug}/SKILL.md"))
            lines.append(f'  click {slugify(slug)} "../skills/{slug}/SKILL.md"')
        # intra-category edges
        for a, b in depends_edges:
            if skills[a]["category"] == cat and skills[b]["category"] == cat:
                lines.append(f"  {slugify(a)} --> {slugify(b)}")
        for a, b, _ in chain_edges:
            if skills[a]["category"] == cat and skills[b]["category"] == cat:
                lines.append(f"  {slugify(a)} -.-> {slugify(b)}")
        for a, b, _ in reactive_edges:
            if skills[a]["category"] == cat and skills[b]["category"] == cat:
                lines.append(f"  {slugify(a)} -..-> {slugify(b)}")
        for a, b, _ in shared_state_edges:
            if skills[a]["category"] == cat and skills[b]["category"] == cat:
                lines.append(f"  {slugify(a)} -..-> {slugify(b)}")
        # cross-category dependencies as faded ghosts
        external = set()
        for a, b in depends_edges:
            if skills[a]["category"] == cat and skills[b]["category"] != cat:
                external.add(b)
                lines.append(f"  {slugify(a)} --> ext_{slugify(b)}")
            elif skills[b]["category"] == cat and skills[a]["category"] != cat:
                external.add(a)
                lines.append(f"  ext_{slugify(a)} --> {slugify(b)}")
        for a, b, _ in shared_state_edges:
            if skills[a]["category"] == cat and skills[b]["category"] != cat:
                external.add(b)
                lines.append(f"  {slugify(a)} -..-> ext_{slugify(b)}")
            elif skills[b]["category"] == cat and skills[a]["category"] != cat:
                external.add(a)
                lines.append(f"  ext_{slugify(a)} -..-> {slugify(b)}")
        for ext_slug in sorted(external):
            lines.append(f'  ext_{slugify(ext_slug)}["{ext_slug}<br/>({skills[ext_slug]["category"]})"]:::external')
            declared_nodes.add(f"ext_{slugify(ext_slug)}")
        # apply enabled/disabled classes
        for slug in slugs:
            cls = "enabled" if skills[slug]["enabled"] else "disabled"
            lines.append(f"  class {slugify(slug)} {cls}")
        # class definitions
        lines.append("  classDef enabled fill:#fff,stroke:#000,stroke-width:2px,color:#000")
        lines.append("  classDef disabled fill:#f5f5f5,stroke:#bbb,color:#888")
        lines.append("  classDef external fill:none,stroke:#bbb,stroke-dasharray:3 3,color:#888")
        lines.append("```")
        cat_blocks.append((cat, "\n".join(lines)))
        blocks.append((f"cat:{cat}", "\n".join(lines)))

    # Lint
    errors = lint_mermaid(blocks, declared_nodes, click_paths)
    if errors:
        # SKILL_GRAPH_ERROR
        for e in errors[:5]:
            print(f"LINT_ERROR: {e}", file=sys.stderr)
        sys.exit(2)

    # Build document
    doc_lines = []
    doc_lines.append("# Skill Dependency Graph")
    doc_lines.append("")
    doc_lines.append(f"_Auto-generated by `skill-graph` on {TODAY} · Mode: `{mode}`_")
    doc_lines.append("")
    doc_lines.append(f"**Verdict:** `{verdict}`")
    doc_lines.append("")

    if mode != "SKILL_GRAPH_NEW" and diff_lines:
        doc_lines.append("## What changed since last run")
        doc_lines.append("")
        doc_lines.extend(diff_lines)
        doc_lines.append("")
        doc_lines.append(f"Prior run: {prior.get('generated_at', '?')} ({prior_total} skills, {prior_enabled} enabled).")
        doc_lines.append("")

    doc_lines.append("## Overview")
    doc_lines.append("")
    doc_lines.append(f"{len(ordered_cats)} categories, {n_total} skills total ({n_enabled} enabled). Cross-category coupling is sparse — most dependencies are intra-category.")
    doc_lines.append("")
    doc_lines.append(dict(blocks)["overview"])
    doc_lines.append("")

    doc_lines.append("## Self-healing loop")
    doc_lines.append("")
    doc_lines.append("The fleet's reliability loop: `heartbeat` detects, `skill-health` diagnoses, `skill-evals` validates, `skill-repair` fixes, `self-improve` evolves. All five share `memory/cron-state.json` as the implicit ledger — collapsed into this single sub-graph rather than rendered as N edges everywhere.")
    doc_lines.append("")
    doc_lines.append(dict(blocks)["self_healing"])
    doc_lines.append("")

    doc_lines.append("## Per-category")
    doc_lines.append("")
    for cat, block in cat_blocks:
        doc_lines.append(f"### {cat} ({len(cats[cat])} skills)")
        doc_lines.append("")
        doc_lines.append(block)
        doc_lines.append("")

    # Legend
    doc_lines.append("## Legend")
    doc_lines.append("")
    doc_lines.append("- `A --> B` — `depends_on` (declared in frontmatter)")
    doc_lines.append("- `A -.-> B` — chain `consume` (downstream step reads upstream output)")
    doc_lines.append("- `A -..-> B` — `reactive` trigger OR shared-state edge (A writes a `memory/topics` or `memory/state` resource that B reads)")
    doc_lines.append("- **Bold-outline node** — `enabled: true` in `aeon.yml`; faded grey — disabled")
    doc_lines.append("- Faded dashed `external` node — a dependency that lives in another category")
    doc_lines.append("- Every node is a hyperlink — click through to the SKILL.md source")
    doc_lines.append("- The universal `memory/cron-state.json` is excluded from shared-state edges (every skill writes it; rendering as N edges would obscure real structure). See the self-healing loop above for its actual usage.")
    doc_lines.append("")

    # Summary table
    doc_lines.append("## Summary")
    doc_lines.append("")
    doc_lines.append("| Category | Skills | Enabled |")
    doc_lines.append("|---|---:|---:|")
    for cat in ordered_cats:
        en = sum(1 for s in cats[cat] if skills[s]["enabled"])
        doc_lines.append(f"| {cat} | {len(cats[cat])} | {en} |")
    doc_lines.append(f"| **total** | **{n_total}** | **{n_enabled}** |")
    doc_lines.append("")
    doc_lines.append("| Edge type | Count |")
    doc_lines.append("|---|---:|")
    for k, v in edge_counts.items():
        doc_lines.append(f"| `{k}` | {v} |")
    doc_lines.append("")

    # Source-status footer
    doc_lines.append("---")
    doc_lines.append("")
    footer = (
        f"skills parsed: {n_total} · "
        f"depends_on: {edge_counts['depends_on']} · "
        f"consume: {edge_counts['consume']} · "
        f"reactive: {edge_counts['reactive']} · "
        f"shared-state derived: {edge_counts['shared_state']} · "
        f"enabled: {n_enabled}/{n_total} · "
        f"mode: {mode}"
    )
    doc_lines.append(f"_{footer}_")
    doc_lines.append("")

    OUT.write_text("\n".join(doc_lines))

    # Persist state
    sorted_slugs = sorted(skills.keys())
    node_sha = sha1("\n".join(sorted_slugs).encode())
    all_edges = (
        [("dep", a, b) for a, b in depends_edges]
        + [("consume", a, b) for a, b, _ in chain_edges]
        + [("reactive", a, b) for a, b, _ in reactive_edges]
        + [("shared", a, b) for a, b, _ in shared_state_edges]
    )
    all_edges.sort()
    edge_sha = sha1("\n".join(f"{t}:{a}->{b}" for t, a, b in all_edges).encode())
    state_out = {
        "generated_at": TODAY,
        "input_fingerprint": fingerprint,
        "skills_total": n_total,
        "enabled_count": n_enabled,
        "edges": edge_counts,
        "node_list_sha": node_sha,
        "edge_list_sha": edge_sha,
    }
    STATE_FILE.write_text(json.dumps(state_out, indent=2) + "\n")

    # Log
    log = ROOT / f"memory/logs/{TODAY}.md"
    log.parent.mkdir(parents=True, exist_ok=True)
    existing = log.read_text() if log.exists() else ""
    existing += f"""
## skill-graph
- Mode: {mode}
- Verdict: {verdict}
- Skills: {n_total} (enabled: {n_enabled})
- Edges: depends_on={edge_counts['depends_on']}, consume={edge_counts['consume']}, reactive={edge_counts['reactive']}, shared_state={edge_counts['shared_state']}
- PR: (pending)
- Source-status: {footer}
"""
    log.write_text(existing)

    # Print summary for orchestrator
    print(json.dumps({
        "mode": mode,
        "verdict": verdict,
        "n_total": n_total,
        "n_enabled": n_enabled,
        "edges": edge_counts,
        "fingerprint": fingerprint,
        "footer": footer,
    }))
    return 0

if __name__ == "__main__":
    sys.exit(main())
