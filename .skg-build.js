#!/usr/bin/env node
// skill-graph builder — Node port of the Python original.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ROOT = '/home/runner/work/aeon/aeon';
const OUT = path.join(ROOT, 'docs/skill-graph.md');
const STATE_FILE = path.join(ROOT, 'memory/topics/skill-graph-state.json');
const TODAY = '2026-06-28';

function sha1(s) {
  return crypto.createHash('sha1').update(s).digest('hex');
}

function readFile(p) {
  try { return fs.readFileSync(p, 'utf8'); } catch (e) { return ''; }
}
function readFileBytes(p) {
  return fs.readFileSync(p);
}

function slugify(s) {
  return s.replace(/[^a-zA-Z0-9]/g, '_');
}

// ---- Step 1: Fingerprint ----
function buildFingerprint() {
  const parts = [];
  parts.push(`${sha1(readFileBytes(path.join(ROOT, 'aeon.yml')))}  aeon.yml`);
  parts.push(`${sha1(readFileBytes(path.join(ROOT, 'skills.json')))}  skills.json`);
  const content = [];
  const skillDir = path.join(ROOT, 'skills');
  const dirs = fs.readdirSync(skillDir).sort();
  for (const d of dirs) {
    const sm = path.join(skillDir, d, 'SKILL.md');
    if (!fs.existsSync(sm)) continue;
    const text = readFile(sm);
    const fmMatch = text.match(/^---\n([\s\S]*?)\n---/);
    if (fmMatch) {
      for (const line of fmMatch[1].split('\n')) {
        content.push(`${sm}: ${line}`);
      }
    }
    for (const line of text.split('\n')) {
      if (/^(depends_on:|- skill:|consume:|parallel:|trigger:)/.test(line)) {
        content.push(line);
      }
    }
    const refs = new Set();
    const refRe = /memory\/(?:topics|state)\/[a-zA-Z0-9_.\-]+/g;
    let m;
    while ((m = refRe.exec(text))) refs.add(m[0]);
    for (const r of [...refs].sort()) content.push(r);
  }
  const contentHash = sha1(content.join('\n'));
  return sha1(parts.join('\n') + '\n' + contentHash);
}

// ---- Parse aeon.yml ----
function parseAeonYml() {
  const text = readFile(path.join(ROOT, 'aeon.yml'));
  const skills = {};
  const chains = {};
  const reactive = {};
  let mode = null; // 'skills' | 'chains' | 'reactive'
  let currentChain = null, currentReactive = null;
  for (const line of text.split('\n')) {
    if (/^skills:\s*$/.test(line)) { mode = 'skills'; continue; }
    if (/^chains:\s*$/.test(line)) { mode = 'chains'; continue; }
    if (/^reactive:\s*$/.test(line)) { mode = 'reactive'; continue; }
    if (/^[a-z_]+:\s*$/.test(line) && !line.startsWith(' ')) { mode = null; continue; }
    if (mode === 'skills') {
      const m = line.match(/^  ([a-z0-9_-]+):\s*(.*)$/);
      if (m) {
        const slug = m[1], rest = m[2].trim();
        const rec = { enabled: false, schedule: '', var: '', model: '' };
        if (rest.startsWith('{')) {
          const inner = rest.replace(/^\{/, '').replace(/\}$/, '').trim();
          // very permissive key:value parser
          const re = /(\w+)\s*:\s*("(?:[^"\\]|\\.)*"|true|false|[^,}]+?)(?=,|\s*$)/g;
          let mm;
          while ((mm = re.exec(inner + ','))) {
            let v = mm[2].trim();
            if (v.startsWith('"') && v.endsWith('"')) v = v.slice(1, -1);
            else if (v === 'true') v = true;
            else if (v === 'false') v = false;
            rec[mm[1]] = v;
          }
        }
        skills[slug] = rec;
      }
    } else if (mode === 'chains') {
      const m = line.match(/^  ([a-z0-9_-]+):\s*$/);
      if (m) {
        currentChain = m[1];
        chains[currentChain] = { schedule: '', on_error: '', steps: [] };
        continue;
      }
      if (currentChain) {
        const ms = line.match(/^\s+schedule:\s*"?([^"]+)"?/);
        if (ms) chains[currentChain].schedule = ms[1].trim();
        const me = line.match(/^\s+on_error:\s*(\S+)/);
        if (me) chains[currentChain].on_error = me[1].trim();
        const mp = line.match(/^\s+-\s*parallel:\s*\[(.+)\]/);
        if (mp) {
          const items = mp[1].split(',').map(s => s.trim().replace(/^"|"$/g, ''));
          chains[currentChain].steps.push({ parallel: items, consume: [] });
        }
        const ms2 = line.match(/^\s+-\s*skill:\s*([\w-]+)/);
        if (ms2) chains[currentChain].steps.push({ skill: ms2[1], consume: [] });
        const mc = line.match(/^\s+consume:\s*\[(.+)\]/);
        if (mc && chains[currentChain].steps.length) {
          const items = mc[1].split(',').map(s => s.trim().replace(/^"|"$/g, ''));
          chains[currentChain].steps[chains[currentChain].steps.length - 1].consume = items;
        }
      }
    } else if (mode === 'reactive') {
      const m = line.match(/^  ([a-z0-9_-]+):\s*$/);
      if (m) { currentReactive = m[1]; reactive[currentReactive] = { trigger: '', on: '', when: '' }; continue; }
      if (currentReactive) {
        for (const k of ['trigger', 'on', 'when']) {
          const mr = line.match(new RegExp(`^\\s+${k}:\\s*"?([^"]+)"?`));
          if (mr) reactive[currentReactive][k] = mr[1].trim();
        }
      }
    }
  }
  return { skills, chains, reactive };
}

function parseSkillsJson() {
  const data = JSON.parse(readFile(path.join(ROOT, 'skills.json')));
  const map = {};
  for (const s of data.skills) map[s.slug] = s.category;
  return map;
}

function parseSkillMd(p) {
  const text = readFile(p);
  const fm = {};
  const fmMatch = text.match(/^---\n([\s\S]*?)\n---/);
  if (fmMatch) {
    for (const line of fmMatch[1].split('\n')) {
      const kv = line.match(/^([a-z_]+):\s*(.*)$/);
      if (kv) fm[kv[1]] = kv[2].trim();
    }
  }
  let dependsOn = [];
  const d1 = text.match(/^depends_on:\s*\[(.+?)\]/m);
  if (d1) dependsOn = d1[1].split(',').map(s => s.trim().replace(/^["']|["']$/g, ''));
  let tags = [];
  if (fm.tags) {
    const t = fm.tags.match(/\[(.+?)\]/);
    if (t) tags = t[1].split(',').map(s => s.trim().replace(/^["']|["']$/g, ''));
  }
  return {
    name: fm.name || path.basename(path.dirname(p)),
    tags,
    depends_on: dependsOn,
    raw: text,
  };
}

function classifyMemoryRefs(text) {
  const refs = { read: new Set(), write: new Set() };
  const lines = text.split('\n');
  const writeRe = /\b(write|writes|save|saved|saves|append|appends|appended|update|updates|updated|>)\b/i;
  const refRe = /memory\/(?:topics|state)\/[a-zA-Z0-9_.\-]+/g;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    let m;
    refRe.lastIndex = 0;
    while ((m = refRe.exec(line))) {
      const window = lines.slice(Math.max(0, i - 1), i + 2).join('\n').toLowerCase();
      if (writeRe.test(window)) refs.write.add(m[0]);
      else refs.read.add(m[0]);
    }
  }
  return refs;
}

function lintBlocks(blocks, clickPaths) {
  const errs = [];
  for (const [label, block] of blocks) {
    // Skip bracket count for class definitions and mermaid native tokens — count [] in node decls
    // We only care about matched pairs in node labels
    const opens = (block.match(/\[/g) || []).length;
    const closes = (block.match(/\]/g) || []).length;
    if (opens !== closes) errs.push(`${label}: bracket mismatch [=${opens} ]=${closes}`);
    const sgs = (block.match(/^\s*subgraph\b/gm) || []).length;
    const ends = (block.match(/^\s*end\s*$/gm) || []).length;
    if (sgs !== ends) errs.push(`${label}: subgraph=${sgs} end=${ends}`);
  }
  for (const [node, p] of clickPaths) {
    const abs = path.resolve(path.dirname(OUT), p);
    if (!fs.existsSync(abs)) errs.push(`click path missing: ${p} (node ${node})`);
  }
  return errs;
}

function main() {
  const fingerprint = buildFingerprint();
  process.stderr.write(`FINGERPRINT=${fingerprint}\n`);

  let prior = {};
  if (fs.existsSync(STATE_FILE)) prior = JSON.parse(readFile(STATE_FILE));
  if (prior.input_fingerprint === fingerprint) {
    const log = path.join(ROOT, `memory/logs/${TODAY}.md`);
    fs.mkdirSync(path.dirname(log), { recursive: true });
    let existing = fs.existsSync(log) ? readFile(log) : '';
    existing += `\n## skill-graph\nSKILL_GRAPH_NO_CHANGE — identical fingerprint ${fingerprint.slice(0, 12)}\n`;
    fs.writeFileSync(log, existing);
    console.log(JSON.stringify({ mode: 'SKILL_GRAPH_NO_CHANGE' }));
    return 0;
  }

  const mode = Object.keys(prior).length === 0 ? 'SKILL_GRAPH_NEW' : 'SKILL_GRAPH_OK';

  const { skills: cfg, chains, reactive } = parseAeonYml();
  const catMap = parseSkillsJson();
  const skillDir = path.join(ROOT, 'skills');
  const dirs = fs.readdirSync(skillDir).filter(d => {
    const p = path.join(skillDir, d, 'SKILL.md');
    return fs.statSync(path.join(skillDir, d)).isDirectory() && fs.existsSync(p);
  }).sort();

  const CANONICAL = new Set(['research', 'dev', 'crypto', 'social', 'productivity']);
  // Map non-canonical tags into one of the 5 canonical buckets
  const TAG_TO_CANONICAL = {
    'ai': 'research', 'AI': 'research', 'agent': 'research',
    'research': 'research', 'content': 'research', 'article': 'research', 'creative': 'research',
    'dev': 'dev', 'security': 'dev', 'audit': 'dev', 'tooling': 'dev',
    'crypto': 'crypto', 'defi': 'crypto', 'market': 'crypto', 'token': 'crypto',
    'on-chain': 'crypto', 'trading': 'crypto', 'wallet': 'crypto',
    'social': 'social', 'twitter': 'social', 'tweet': 'social', 'farcaster': 'social',
    'productivity': 'productivity', 'meta': 'productivity', 'fleet': 'productivity',
    'health': 'productivity', 'admin': 'productivity', 'config': 'productivity',
  };
  function bucketize(rawCat, tags) {
    if (CANONICAL.has(rawCat)) return rawCat;
    for (const t of tags) {
      if (CANONICAL.has(t)) return t;
      if (TAG_TO_CANONICAL[t]) return TAG_TO_CANONICAL[t];
    }
    if (TAG_TO_CANONICAL[rawCat]) return TAG_TO_CANONICAL[rawCat];
    return 'productivity';
  }

  const skills = {};
  for (const slug of dirs) {
    const sm = parseSkillMd(path.join(skillDir, slug, 'SKILL.md'));
    const rawCat = catMap[slug] || (sm.tags[0] || 'productivity');
    const cat = bucketize(rawCat, sm.tags);
    const c = cfg[slug] || { enabled: false, schedule: '', var: '', model: '' };
    skills[slug] = {
      ...sm,
      slug,
      category: cat,
      enabled: c.enabled === true,
      schedule: c.schedule || '',
      var: c.var || '',
      model: c.model || '',
    };
  }

  const cats = {};
  for (const slug of Object.keys(skills)) {
    const c = skills[slug].category;
    (cats[c] = cats[c] || []).push(slug);
  }
  for (const c of Object.keys(cats)) cats[c].sort();
  const catOrder = ['research', 'dev', 'crypto', 'social', 'productivity'];
  const orderedCats = catOrder.filter(c => cats[c]);

  // Shared-state edges
  const writers = {};
  const readers = {};
  for (const slug of Object.keys(skills)) {
    const refs = classifyMemoryRefs(skills[slug].raw);
    for (const r of refs.write) (writers[r] = writers[r] || new Set()).add(slug);
    for (const r of refs.read) (readers[r] = readers[r] || new Set()).add(slug);
  }
  const sharedEdges = [];
  const allPaths = new Set([...Object.keys(writers), ...Object.keys(readers)]);
  for (const p of [...allPaths].sort()) {
    if (p.includes('cron-state')) continue;
    const ws = [...(writers[p] || [])].sort();
    const rs = [...(readers[p] || [])].sort();
    for (const w of ws) for (const r of rs) if (w !== r) sharedEdges.push([w, r, p]);
  }

  // depends_on
  const dependsEdges = [];
  for (const slug of Object.keys(skills)) {
    for (const dep of skills[slug].depends_on) {
      if (skills[dep]) dependsEdges.push([slug, dep]);
    }
  }

  // chain consume edges
  const chainEdges = [];
  for (const [cn, c] of Object.entries(chains)) {
    for (const step of c.steps) {
      if (step.skill && step.consume && step.consume.length) {
        for (const prod of step.consume) {
          if (skills[prod] && skills[step.skill]) chainEdges.push([prod, step.skill, cn]);
        }
      }
    }
  }

  // reactive
  const reactiveEdges = [];
  for (const [trig, r] of Object.entries(reactive)) {
    if (r.on && skills[r.on] && skills[trig]) reactiveEdges.push([r.on, trig, 'reactive']);
  }

  const nTotal = Object.keys(skills).length;
  const nEnabled = Object.values(skills).filter(s => s.enabled).length;
  const edgeCounts = {
    depends_on: dependsEdges.length,
    consume: chainEdges.length,
    reactive: reactiveEdges.length,
    shared_state: sharedEdges.length,
  };

  // Diff vs prior
  const priorTotal = prior.skills_total || 0;
  const priorEnabled = prior.enabled_count || 0;
  const priorEdges = prior.edges || {};
  const diffLines = [];
  if (Object.keys(prior).length) {
    diffLines.push(nTotal !== priorTotal
      ? `- Skills: ${priorTotal} -> **${nTotal}** (${(nTotal - priorTotal >= 0 ? '+' : '')}${nTotal - priorTotal})`
      : `- Skills: ${nTotal} (no change)`);
    diffLines.push(nEnabled !== priorEnabled
      ? `- Enabled: ${priorEnabled} -> **${nEnabled}** (${(nEnabled - priorEnabled >= 0 ? '+' : '')}${nEnabled - priorEnabled})`
      : `- Enabled: ${nEnabled} (no change)`);
    for (const k of ['depends_on', 'consume', 'reactive', 'shared_state']) {
      const pv = priorEdges[k] || 0;
      const cv = edgeCounts[k];
      diffLines.push(pv !== cv
        ? `- \`${k}\` edges: ${pv} -> **${cv}** (${cv - pv >= 0 ? '+' : ''}${cv - pv})`
        : `- \`${k}\` edges: ${cv} (no change)`);
    }
  }

  // Verdict
  const verdictParts = [];
  if (!Object.keys(prior).length) verdictParts.push(`INITIALIZED: ${nTotal} skills`);
  else {
    if (nTotal > priorTotal) verdictParts.push(`NEW_SKILLS: +${nTotal - priorTotal}`);
    else if (nTotal < priorTotal) verdictParts.push(`RETIRED_SKILLS: ${nTotal - priorTotal}`);
    if (nEnabled !== priorEnabled) verdictParts.push(`ENABLED_DELTA: ${nEnabled - priorEnabled >= 0 ? '+' : ''}${nEnabled - priorEnabled}`);
    for (const k of ['depends_on', 'consume', 'reactive', 'shared_state']) {
      const pv = priorEdges[k] || 0;
      const cv = edgeCounts[k];
      if (pv !== cv) verdictParts.push(`${k.toUpperCase()}: ${pv}->${cv}`);
    }
  }
  const verdict = verdictParts.length ? verdictParts.join(' | ') : 'ARCHITECTURE_OK';

  // ---- Build mermaid blocks ----
  const blocks = [];
  const clickPaths = [];

  function mermaidNode(slug, sched) {
    return sched ? `${slugify(slug)}["${slug}<br/>(${sched})"]` : `${slugify(slug)}["${slug}"]`;
  }

  // Overview
  const ov = ['```mermaid', 'flowchart LR'];
  for (const c of orderedCats) {
    ov.push(`  ${slugify(c)}["${c}<br/>(${cats[c].length} skills)"]`);
  }
  const crossCounts = {};
  const allEdgesForCross = [
    ...dependsEdges,
    ...chainEdges.map(([a, b]) => [a, b]),
    ...reactiveEdges.map(([a, b]) => [a, b]),
    ...sharedEdges.map(([a, b]) => [a, b]),
  ];
  for (const [a, b] of allEdgesForCross) {
    const ca = skills[a].category, cb = skills[b].category;
    if (ca !== cb) {
      const k = `${ca}|${cb}`;
      crossCounts[k] = (crossCounts[k] || 0) + 1;
    }
  }
  for (const k of Object.keys(crossCounts).sort()) {
    const [ca, cb] = k.split('|');
    ov.push(`  ${slugify(ca)} -->|${crossCounts[k]}| ${slugify(cb)}`);
  }
  ov.push('```');
  blocks.push(['overview', ov.join('\n')]);

  // Self-healing loop
  const sh = ['```mermaid', 'flowchart LR'];
  const shChain = ['heartbeat', 'skill-health', 'skill-evals', 'skill-repair', 'self-improve'];
  for (const slug of shChain) if (skills[slug]) sh.push(`  ${slugify(slug)}["${slug}"]`);
  sh.push('  state[("memory/cron-state.json")]');
  for (let i = 0; i < shChain.length - 1; i++) {
    if (skills[shChain[i]] && skills[shChain[i + 1]]) sh.push(`  ${slugify(shChain[i])} --> ${slugify(shChain[i + 1])}`);
  }
  for (const slug of shChain) if (skills[slug]) sh.push(`  ${slugify(slug)} -.-> state`);
  sh.push('```');
  blocks.push(['self_healing', sh.join('\n')]);

  // Per-category
  const catBlocks = [];
  for (const cat of orderedCats) {
    const slugs = cats[cat];
    const lines = ['```mermaid', 'flowchart LR'];
    for (const slug of slugs) {
      lines.push(`  ${mermaidNode(slug, skills[slug].schedule)}`);
      clickPaths.push([slugify(slug), `../skills/${slug}/SKILL.md`]);
      lines.push(`  click ${slugify(slug)} "../skills/${slug}/SKILL.md"`);
    }
    for (const [a, b] of dependsEdges) {
      if (skills[a].category === cat && skills[b].category === cat) lines.push(`  ${slugify(a)} --> ${slugify(b)}`);
    }
    for (const [a, b] of chainEdges) {
      if (skills[a].category === cat && skills[b].category === cat) lines.push(`  ${slugify(a)} -.-> ${slugify(b)}`);
    }
    for (const [a, b] of reactiveEdges) {
      if (skills[a].category === cat && skills[b].category === cat) lines.push(`  ${slugify(a)} -..-> ${slugify(b)}`);
    }
    for (const [a, b] of sharedEdges) {
      if (skills[a].category === cat && skills[b].category === cat) lines.push(`  ${slugify(a)} -..-> ${slugify(b)}`);
    }
    const external = new Set();
    for (const [a, b] of dependsEdges) {
      if (skills[a].category === cat && skills[b].category !== cat) {
        external.add(b);
        lines.push(`  ${slugify(a)} --> ext_${slugify(b)}`);
      } else if (skills[b].category === cat && skills[a].category !== cat) {
        external.add(a);
        lines.push(`  ext_${slugify(a)} --> ${slugify(b)}`);
      }
    }
    for (const [a, b] of sharedEdges) {
      if (skills[a].category === cat && skills[b].category !== cat) {
        external.add(b);
        lines.push(`  ${slugify(a)} -..-> ext_${slugify(b)}`);
      } else if (skills[b].category === cat && skills[a].category !== cat) {
        external.add(a);
        lines.push(`  ext_${slugify(a)} -..-> ${slugify(b)}`);
      }
    }
    for (const ext of [...external].sort()) {
      lines.push(`  ext_${slugify(ext)}["${ext}<br/>(${skills[ext].category})"]:::external`);
    }
    for (const slug of slugs) {
      lines.push(`  class ${slugify(slug)} ${skills[slug].enabled ? 'enabled' : 'disabled'}`);
    }
    lines.push('  classDef enabled fill:#fff,stroke:#000,stroke-width:2px,color:#000');
    lines.push('  classDef disabled fill:#f5f5f5,stroke:#bbb,color:#888');
    lines.push('  classDef external fill:none,stroke:#bbb,stroke-dasharray:3 3,color:#888');
    lines.push('```');
    catBlocks.push([cat, lines.join('\n')]);
    blocks.push([`cat:${cat}`, lines.join('\n')]);
  }

  // Lint
  const errs = lintBlocks(blocks, clickPaths);
  if (errs.length) {
    for (const e of errs.slice(0, 10)) process.stderr.write(`LINT_ERROR: ${e}\n`);
    process.exit(2);
  }

  // Build document
  const doc = [];
  doc.push('# Skill Dependency Graph');
  doc.push('');
  doc.push(`_Auto-generated by \`skill-graph\` on ${TODAY} · Mode: \`${mode}\`_`);
  doc.push('');
  doc.push(`**Verdict:** \`${verdict}\``);
  doc.push('');

  if (mode !== 'SKILL_GRAPH_NEW' && diffLines.length) {
    doc.push('## What changed since last run');
    doc.push('');
    doc.push(...diffLines);
    doc.push('');
    doc.push(`Prior run: ${prior.generated_at || '?'} (${priorTotal} skills, ${priorEnabled} enabled).`);
    doc.push('');
  }

  doc.push('## Overview');
  doc.push('');
  doc.push(`${orderedCats.length} categories, ${nTotal} skills total (${nEnabled} enabled). Cross-category coupling is sparse — most edges are intra-category. Edge counts on arrows below.`);
  doc.push('');
  doc.push(blocks.find(([k]) => k === 'overview')[1]);
  doc.push('');

  doc.push('## Self-healing loop');
  doc.push('');
  doc.push('The fleet\'s reliability loop: `heartbeat` detects, `skill-health` diagnoses, `skill-evals` validates, `skill-repair` fixes, `self-improve` evolves. All five share `memory/cron-state.json` as the implicit ledger — collapsed into this single sub-graph rather than rendered as N edges everywhere.');
  doc.push('');
  doc.push(blocks.find(([k]) => k === 'self_healing')[1]);
  doc.push('');

  doc.push('## Per-category');
  doc.push('');
  for (const [cat, block] of catBlocks) {
    doc.push(`### ${cat} (${cats[cat].length} skills)`);
    doc.push('');
    doc.push(block);
    doc.push('');
  }

  doc.push('## Legend');
  doc.push('');
  doc.push('- `A --> B` — `depends_on` (declared in frontmatter)');
  doc.push('- `A -.-> B` — chain `consume` (downstream step reads upstream output)');
  doc.push('- `A -..-> B` — `reactive` trigger OR shared-state edge (A writes a `memory/topics` or `memory/state` resource that B reads)');
  doc.push('- **Bold-outline node** — `enabled: true` in `aeon.yml`; faded grey — disabled');
  doc.push('- Faded dashed `external` node — a dependency that lives in another category');
  doc.push('- Every node is a hyperlink — click through to the SKILL.md source');
  doc.push('- The universal `memory/cron-state.json` is excluded from shared-state edges (every skill writes it; rendering as N edges would obscure real structure). See the self-healing loop above for its actual usage.');
  doc.push('');

  doc.push('## Summary');
  doc.push('');
  doc.push('| Category | Skills | Enabled |');
  doc.push('|---|---:|---:|');
  for (const cat of orderedCats) {
    const en = cats[cat].filter(s => skills[s].enabled).length;
    doc.push(`| ${cat} | ${cats[cat].length} | ${en} |`);
  }
  doc.push(`| **total** | **${nTotal}** | **${nEnabled}** |`);
  doc.push('');
  doc.push('| Edge type | Count |');
  doc.push('|---|---:|');
  for (const [k, v] of Object.entries(edgeCounts)) doc.push(`| \`${k}\` | ${v} |`);
  doc.push('');

  doc.push('---');
  doc.push('');
  const footer = `skills parsed: ${nTotal} · depends_on: ${edgeCounts.depends_on} · consume: ${edgeCounts.consume} · reactive: ${edgeCounts.reactive} · shared-state derived: ${edgeCounts.shared_state} · enabled: ${nEnabled}/${nTotal} · mode: ${mode}`;
  doc.push(`_${footer}_`);
  doc.push('');

  fs.writeFileSync(OUT, doc.join('\n'));

  // Persist state
  const sortedSlugs = Object.keys(skills).sort();
  const nodeSha = sha1(sortedSlugs.join('\n'));
  const allEdgesList = [
    ...dependsEdges.map(([a, b]) => `dep:${a}->${b}`),
    ...chainEdges.map(([a, b]) => `consume:${a}->${b}`),
    ...reactiveEdges.map(([a, b]) => `reactive:${a}->${b}`),
    ...sharedEdges.map(([a, b]) => `shared:${a}->${b}`),
  ].sort();
  const edgeSha = sha1(allEdgesList.join('\n'));
  const stateOut = {
    generated_at: TODAY,
    input_fingerprint: fingerprint,
    skills_total: nTotal,
    enabled_count: nEnabled,
    edges: edgeCounts,
    node_list_sha: nodeSha,
    edge_list_sha: edgeSha,
  };
  fs.writeFileSync(STATE_FILE, JSON.stringify(stateOut, null, 2) + '\n');

  // Log
  const log = path.join(ROOT, `memory/logs/${TODAY}.md`);
  fs.mkdirSync(path.dirname(log), { recursive: true });
  let existing = fs.existsSync(log) ? readFile(log) : '';
  existing += `
## skill-graph
- Mode: ${mode}
- Verdict: ${verdict}
- Skills: ${nTotal} (enabled: ${nEnabled})
- Edges: depends_on=${edgeCounts.depends_on}, consume=${edgeCounts.consume}, reactive=${edgeCounts.reactive}, shared_state=${edgeCounts.shared_state}
- PR: (pending)
- Source-status: ${footer}
`;
  fs.writeFileSync(log, existing);

  console.log(JSON.stringify({
    mode, verdict, n_total: nTotal, n_enabled: nEnabled, edges: edgeCounts,
    fingerprint, footer,
  }));
  return 0;
}

process.exit(main());
