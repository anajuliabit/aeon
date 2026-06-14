#!/usr/bin/env node
/**
 * skill-graph: generate docs/skill-graph.md from aeon.yml + skills.json + per-skill SKILL.md files
 *
 * Implements steps 1-7 of skills/skill-graph/SKILL.md:
 *   - input fingerprint + change detection
 *   - explicit + derived edge parsing
 *   - lint + multi-diagram doc generation
 *   - state persistence
 *
 * git/PR/notify (steps 8-10) are handled by the runner outside this script.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ROOT = '/home/runner/work/aeon/aeon';
process.chdir(ROOT);

const today = process.env.TODAY || '2026-06-14';
const outVar = (process.env.SKILL_GRAPH_VAR || '').trim();
const outPath = outVar || 'docs/skill-graph.md';
const stateFile = 'memory/topics/skill-graph-state.json';

function sha1(buf) { return crypto.createHash('sha1').update(buf).digest('hex'); }

/* ---------- 1) Input fingerprint ---------- */
function computeFingerprint() {
  const lines = [];
  for (const fn of ['aeon.yml', 'skills.json']) {
    lines.push(`${sha1(fs.readFileSync(fn))}  ${fn}`);
  }
  const skillFiles = fs.readdirSync('skills')
    .filter(d => fs.statSync(path.join('skills', d)).isDirectory())
    .sort()
    .map(d => `skills/${d}/SKILL.md`)
    .filter(p => fs.existsSync(p));
  const innerBuf = [];
  for (const f of skillFiles) {
    const text = fs.readFileSync(f, 'utf8');
    let n = 0;
    for (const line of text.split('\n')) {
      if (line === '---') { n++; continue; }
      if (n === 1) innerBuf.push(`${f}: ${line}`);
    }
    for (const line of text.split('\n')) {
      if (/^depends_on:/.test(line) || /^- skill:/.test(line) ||
          /consume:/.test(line) || /parallel:/.test(line) || /trigger:/.test(line)) {
        innerBuf.push(line);
      }
    }
    const refs = new Set();
    for (const m of text.matchAll(/memory\/(?:topics|state)\/[a-zA-Z0-9_.-]+/g)) refs.add(m[0]);
    [...refs].sort().forEach(r => innerBuf.push(r));
  }
  const innerSha = sha1(innerBuf.join('\n') + '\n');
  lines.push(`${innerSha}  -`);
  const fileContent = lines.join('\n') + '\n';
  // canonical fingerprint = sha1 of the full fingerprint file (captures aeon.yml + skills.json + inner)
  const overallSha = sha1(fileContent);
  return { fileContent, innerSha, overallSha, skillFiles };
}

const { fileContent: fpFile, overallSha: fingerprint, skillFiles } = computeFingerprint();
fs.writeFileSync('skill-graph-tmp/fingerprint.txt', fpFile);

/* ---------- Load prior state ---------- */
let prior = null;
let mode = 'SKILL_GRAPH_OK';
if (fs.existsSync(stateFile)) {
  try { prior = JSON.parse(fs.readFileSync(stateFile, 'utf8')); }
  catch { prior = null; }
}
if (!prior) mode = 'SKILL_GRAPH_NEW';

if (prior && prior.input_fingerprint === fingerprint) {
  console.log('SKILL_GRAPH_NO_CHANGE');
  // append log line and exit
  const logFile = `memory/logs/${today}.md`;
  const logLine = `\n## skill-graph\nSKILL_GRAPH_NO_CHANGE — ${prior.skills_total} skills, identical fingerprint\n`;
  if (fs.existsSync(logFile)) fs.appendFileSync(logFile, logLine);
  else fs.writeFileSync(logFile, `# ${today}\n${logLine}`);
  process.exit(0);
}

/* ---------- 2) Parse aeon.yml ---------- */
function parseAeon() {
  const raw = fs.readFileSync('aeon.yml', 'utf8');
  // Flatten multi-line skill entries: `name:\n    {\n      enabled: true,\n      ...\n    }` → single line
  const lines = raw.split('\n');
  const flat = [];
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    // detect `<key>:\n  {`
    const m = line.match(/^(\s*)([a-z0-9-]+):\s*$/);
    if (m && i + 1 < lines.length && lines[i+1].trim() === '{') {
      let j = i + 1;
      const body = [];
      while (j < lines.length && !lines[j].trim().startsWith('}')) {
        body.push(lines[j].trim().replace(/,$/, ''));
        j++;
      }
      // skip the open `{` (body[0])
      const inner = body.slice(1).filter(Boolean).join(', ');
      flat.push(`${m[1]}${m[2]}: { ${inner} }`);
      i = j + 1;
      continue;
    }
    flat.push(line);
    i++;
  }
  const flattened = flat.join('\n');

  const skills = {};
  // Match: `  skill-name: { enabled: true, schedule: "...", var: "...", model: "..." }`
  const skillRe = /^\s\s([a-z0-9-]+):\s*\{\s*([^}]*)\s*\}/gm;
  // We need to restrict to the `skills:` block. Find block bounds.
  const skillsStart = flattened.indexOf('\nskills:');
  let skillsBlock = flattened;
  let restAfter = '';
  if (skillsStart >= 0) {
    // find next top-level key after `skills:`
    const after = flattened.slice(skillsStart + 1);
    const nextTop = after.match(/\n([a-z][a-z_-]*):/m);
    if (nextTop) {
      const end = skillsStart + 1 + nextTop.index;
      skillsBlock = flattened.slice(skillsStart, end);
      restAfter = flattened.slice(end);
    } else {
      skillsBlock = flattened.slice(skillsStart);
    }
  }
  let m;
  while ((m = skillRe.exec(skillsBlock)) !== null) {
    const slug = m[1];
    const body = m[2];
    const enabled = /enabled:\s*true/.test(body);
    const schedule = (body.match(/schedule:\s*"([^"]*)"/) || [])[1] || '';
    const varVal = (body.match(/var:\s*"([^"]*)"/) || [])[1] || '';
    const model = (body.match(/model:\s*"([^"]*)"/) || [])[1] || '';
    skills[slug] = { slug, enabled, schedule, var: varVal, model };
  }

  /* chains */
  const chains = {};
  const chainsMatch = flattened.match(/\nchains:\s*\n([\s\S]*?)(?=\n[a-z][a-z_-]*:|$)/);
  if (chainsMatch) {
    // Parse only un-commented chain definitions.
    const cb = chainsMatch[1].split('\n');
    let curChain = null;
    let curStep = null;
    for (const line of cb) {
      const stripped = line.replace(/#.*$/, '');
      const cm = stripped.match(/^\s\s([a-z][a-z0-9_-]*):\s*$/);
      if (cm && !line.trim().startsWith('#')) {
        curChain = cm[1];
        chains[curChain] = { steps: [] };
        continue;
      }
      if (!curChain) continue;
      const stepM = stripped.match(/^\s*-\s*skill:\s*([a-z0-9-]+)/);
      const parM = stripped.match(/^\s*-\s*parallel:\s*\[([^\]]+)\]/);
      const conM = stripped.match(/consume:\s*\[([^\]]+)\]/);
      if (parM && !line.trim().startsWith('#')) {
        const ps = parM[1].split(',').map(s => s.trim());
        chains[curChain].steps.push({ parallel: ps });
        curStep = chains[curChain].steps[chains[curChain].steps.length - 1];
      } else if (stepM && !line.trim().startsWith('#')) {
        const obj = { skill: stepM[1] };
        chains[curChain].steps.push(obj);
        curStep = obj;
      } else if (conM && curStep && !line.trim().startsWith('#')) {
        const cs = conM[1].split(',').map(s => s.trim());
        curStep.consume = cs;
      }
    }
  }

  /* reactive */
  const reactive = {};
  const reMatch = flattened.match(/\nreactive:\s*\n([\s\S]*?)(?=\n[a-z][a-z_-]*:|$)/);
  if (reMatch) {
    const rb = reMatch[1].split('\n');
    let curSkill = null;
    for (const line of rb) {
      if (line.trim().startsWith('#')) continue;
      const sm = line.match(/^\s\s([a-z][a-z0-9_-]*):\s*$/);
      if (sm) { curSkill = sm[1]; reactive[curSkill] = []; continue; }
      const tm = line.match(/on:\s*"?([a-z0-9*_-]+)"?,\s*when:\s*"([^"]+)"/);
      if (tm && curSkill) reactive[curSkill].push({ on: tm[1], when: tm[2] });
    }
  }

  return { skills, chains, reactive };
}

const aeon = parseAeon();

/* ---------- 3) Parse skills.json ---------- */
const skillsJson = JSON.parse(fs.readFileSync('skills.json', 'utf8'));
const catalogByName = {};
for (const s of skillsJson.skills) catalogByName[s.slug] = s;
const CATEGORIES = ['research', 'dev', 'crypto', 'social', 'productivity'];
const CATEGORY_LABEL = skillsJson.categories;

/* ---------- 4) Parse each SKILL.md frontmatter ---------- */
function parseFrontmatter(text) {
  const lines = text.split('\n');
  if (lines[0] !== '---') return {};
  const fm = {};
  let i = 1;
  let curArrayKey = null;
  while (i < lines.length && lines[i] !== '---') {
    const line = lines[i];
    const km = line.match(/^([a-z_]+):\s*(.*)$/);
    if (km) {
      const key = km[1]; const val = km[2].trim();
      curArrayKey = null;
      if (val === '' ) { fm[key] = []; curArrayKey = key; }
      else if (val.startsWith('[') && val.endsWith(']')) {
        fm[key] = val.slice(1, -1).split(',').map(s => s.trim()).filter(Boolean);
      } else {
        // strip surrounding quotes
        fm[key] = val.replace(/^["']|["']$/g, '');
      }
    } else if (curArrayKey && line.match(/^\s*-\s+/)) {
      const v = line.replace(/^\s*-\s+/, '').replace(/^["']|["']$/g, '');
      fm[curArrayKey].push(v);
    }
    i++;
  }
  return fm;
}

const skillData = {};
for (const f of skillFiles) {
  const slug = path.basename(path.dirname(f));
  const text = fs.readFileSync(f, 'utf8');
  const fm = parseFrontmatter(text);
  const enabled = aeon.skills[slug]?.enabled || false;
  const schedule = aeon.skills[slug]?.schedule || '';
  const cat = (catalogByName[slug] && CATEGORIES.includes(catalogByName[slug].category))
    ? catalogByName[slug].category
    : (Array.isArray(fm.tags) && CATEGORIES.find(c => fm.tags.includes(c))) || 'productivity';
  // derived: memory refs classified as read vs write
  const lines = text.split('\n');
  const writes = new Set(), reads = new Set();
  for (let i = 0; i < lines.length; i++) {
    const matches = [...lines[i].matchAll(/memory\/(?:topics|state)\/[a-zA-Z0-9_.-]+/g)];
    for (const m of matches) {
      const ref = m[0];
      // look at surrounding 3 lines (i-1, i, i+1)
      const start = Math.max(0, i-1), end = Math.min(lines.length-1, i+1);
      const ctx = lines.slice(start, end+1).join('\n');
      if (/\b(write|save|append|update)\b.*(topics|state)\//.test(ctx)
          || /(>+|>>)\s*memory\/(topics|state)/.test(ctx)) writes.add(ref);
      else reads.add(ref);
    }
  }
  // research → articles edges
  const tags = Array.isArray(fm.tags) ? fm.tags : [];
  const isArticleProducer = tags.includes('research') || /articles\//.test(text);
  skillData[slug] = {
    slug,
    name: fm.name || slug,
    tags,
    depends_on: Array.isArray(fm.depends_on) ? fm.depends_on : [],
    enabled,
    schedule,
    category: cat,
    writes: [...writes],
    reads: [...reads],
    isArticleProducer,
  };
}

const allSkills = Object.keys(skillData).sort();

/* ---------- Build edges ---------- */
const edges = []; // {from, to, type}
function addEdge(from, to, type) {
  if (!skillData[from] || !skillData[to]) return;
  if (from === to) return;
  if (edges.some(e => e.from === from && e.to === to && e.type === type)) return;
  edges.push({ from, to, type });
}

// explicit depends_on
for (const s of allSkills) {
  for (const d of skillData[s].depends_on) addEdge(s, d, 'depends_on');
}
// chains: each step.consume → consume edges to consumer
for (const [cname, c] of Object.entries(aeon.chains)) {
  for (const step of c.steps) {
    if (step.consume && step.skill) {
      for (const src of step.consume) addEdge(src, step.skill, 'consume');
    }
  }
}
// reactive triggers
for (const [s, triggers] of Object.entries(aeon.reactive)) {
  for (const t of triggers) {
    if (t.on === '*') continue;
    addEdge(t.on, s, 'reactive');
  }
}
// derived shared-state: A writes ref, B reads same ref → A -..-> B
{
  const writers = new Map(); // ref → Set<slug>
  const readers = new Map(); // ref → Set<slug>
  for (const s of allSkills) {
    for (const w of skillData[s].writes) {
      if (/cron-state\.json/.test(w)) continue; // collapse via legend
      if (!writers.has(w)) writers.set(w, new Set());
      writers.get(w).add(s);
    }
    for (const r of skillData[s].reads) {
      if (/cron-state\.json/.test(r)) continue;
      if (!readers.has(r)) readers.set(r, new Set());
      readers.get(r).add(s);
    }
  }
  for (const [ref, ws] of writers) {
    const rs = readers.get(ref) || new Set();
    for (const w of ws) for (const r of rs) if (w !== r) addEdge(w, r, 'shared_state');
  }
}
// research → article pipeline
for (const s of allSkills) {
  if (skillData[s].isArticleProducer) {
    for (const downstream of ['syndicate-article', 'rss-feed', 'update-gallery']) {
      if (skillData[downstream] && s !== downstream) addEdge(s, downstream, 'shared_state');
    }
  }
}

/* ---------- Categorize ---------- */
const byCat = Object.fromEntries(CATEGORIES.map(c => [c, []]));
for (const s of allSkills) {
  const c = skillData[s].category;
  if (byCat[c]) byCat[c].push(s);
  else byCat.productivity.push(s);
}
Object.values(byCat).forEach(arr => arr.sort());

const skillToCat = {};
for (const s of allSkills) skillToCat[s] = skillData[s].category;

/* ---------- Diff vs prior file ---------- */
const priorDocPath = outPath;
let priorNodes = new Set(), priorEdges = new Set(), priorEnabled = new Set();
if (fs.existsSync(priorDocPath)) {
  const prev = fs.readFileSync(priorDocPath, 'utf8');
  // grab click directives → nodes
  // skip historical self-heal aliases (health/evals/repair/improve) that were renamed to canonical skill slugs in this regen
  const SELF_HEAL_ALIAS = new Set(['health', 'evals', 'repair', 'improve', 'state']);
  for (const m of prev.matchAll(/^\s*click\s+([a-z0-9-]+)\s+"\.\.\/skills\/([a-z0-9-]+)/gm)) {
    const id = m[1];
    const realSlug = m[2];
    // node IDs that already match the linked skill slug → real
    // legacy aliases (id != realSlug, short) → fold into realSlug to avoid diff churn
    if (SELF_HEAL_ALIAS.has(id) && id !== realSlug) priorNodes.add(realSlug);
    else priorNodes.add(id);
  }
  // edges in mermaid: `from --> to`, `from -.-> to`, `from -..-> to`, with optional labels
  const ALIAS_REMAP = {
    'health': 'skill-health', 'evals': 'skill-evals', 'repair': 'skill-repair',
    'improve': 'self-improve', 'state': 'cron-state', 'cron-state': 'cron-state',
  };
  const remap = s => ALIAS_REMAP[s] || s;
  const stripExt = s => s.replace(/_ext[0-9]*$/, '');
  for (const m of prev.matchAll(/^\s*([a-z0-9_-]+)\s+(-+\.{0,2}-*>|-->|-\.->|-\.\.->)\s+([a-z0-9_-]+)\b/gm)) {
    const from = remap(stripExt(m[1]));
    const to = remap(stripExt(m[3]));
    priorEdges.add(`${from}->${to}`);
  }
  // enabled overlay can be expressed two ways:
  //   1) `class slug enabled` directive
  //   2) inline `slug["label"]:::enabled` node declaration
  for (const m of prev.matchAll(/^\s*class\s+([a-z0-9_-]+)\s+enabled\b/gm)) {
    priorEnabled.add(remap(stripExt(m[1])));
  }
  for (const m of prev.matchAll(/^\s*([a-z0-9_-]+)\[[^\]]+\]:::enabled\b/gm)) {
    priorEnabled.add(remap(stripExt(m[1])));
  }
}

const newNodes = new Set(allSkills);
const newEdges = new Set(edges.map(e => `${e.from}->${e.to}`));
const newEnabled = new Set(allSkills.filter(s => skillData[s].enabled));

// Self-heal loop edges are emitted in a dedicated callout, not in the `edges` array.
// Include them in newEdges so they line up with how priorDoc gets parsed.
const SELF_HEAL_EDGES = [
  'heartbeat->skill-health', 'skill-health->skill-evals', 'skill-evals->skill-repair',
  'skill-repair->self-improve', 'self-improve->heartbeat',
  'heartbeat->cron-state', 'skill-health->cron-state', 'skill-repair->cron-state',
];
for (const e of SELF_HEAL_EDGES) newEdges.add(e);

function diff(a, b) {
  const added = [...b].filter(x => !a.has(x));
  const removed = [...a].filter(x => !b.has(x));
  return { added, removed };
}
const nodesDiff = diff(priorNodes, newNodes);
const edgesDiff = diff(priorEdges, newEdges);
const enabledDiff = diff(priorEnabled, newEnabled);

/* ---------- Verdict ---------- */
function buildVerdict() {
  const parts = [];
  if (nodesDiff.added.length) parts.push(`NEW_SKILLS: ${nodesDiff.added.slice(0,8).join(', ')}${nodesDiff.added.length>8?' (+'+(nodesDiff.added.length-8)+' more)':''}`);
  if (nodesDiff.removed.length) parts.push(`RETIRED_SKILLS: ${nodesDiff.removed.slice(0,8).join(', ')}${nodesDiff.removed.length>8?' (+'+(nodesDiff.removed.length-8)+' more)':''}`);
  if (edgesDiff.added.length) parts.push(`NEW_DEPS: ${edgesDiff.added.slice(0,6).join(', ')}${edgesDiff.added.length>6?' (+'+(edgesDiff.added.length-6)+' more)':''}`);
  if (edgesDiff.removed.length) parts.push(`REMOVED_DEPS: ${edgesDiff.removed.slice(0,6).join(', ')}${edgesDiff.removed.length>6?' (+'+(edgesDiff.removed.length-6)+' more)':''}`);
  if (enabledDiff.added.length) parts.push(`NEW_ENABLED: ${enabledDiff.added.slice(0,8).join(', ')}${enabledDiff.added.length>8?' (+'+(enabledDiff.added.length-8)+' more)':''}`);
  if (enabledDiff.removed.length) parts.push(`NEW_DISABLED: ${enabledDiff.removed.slice(0,8).join(', ')}${enabledDiff.removed.length>8?' (+'+(enabledDiff.removed.length-8)+' more)':''}`);
  if (!parts.length) return 'ARCHITECTURE_OK';
  return parts.join(' · ');
}
const verdict = buildVerdict();

/* ---------- 5) Generate document ---------- */
function edgeArrow(type) {
  return type === 'consume' ? '-.->' : type === 'shared_state' ? '-..->' : '-->';
}

function escapeLabel(s) { return s.replace(/"/g, "'"); }

function nodeLabel(slug) {
  const sd = skillData[slug];
  const sch = sd.schedule ? `<br/><i>${sd.schedule}</i>` : '';
  return `${slug}["${slug}${sd.enabled ? sch : ''}"]`;
}

function buildOverview() {
  const lines = ['```mermaid', 'flowchart LR'];
  for (const c of CATEGORIES) {
    lines.push(`    ${c}["${CATEGORY_LABEL[c]}<br/>(${byCat[c].length})"]:::cat`);
  }
  lines.push('');
  // count cross-category edges
  const crossCounts = new Map();
  for (const e of edges) {
    const a = skillToCat[e.from], b = skillToCat[e.to];
    if (!a || !b) continue;
    const key = `${a}|${b}`;
    crossCounts.set(key, (crossCounts.get(key) || 0) + 1);
  }
  for (const [k, n] of [...crossCounts.entries()].sort((x,y)=>y[1]-x[1])) {
    const [a, b] = k.split('|');
    if (a === b) lines.push(`    ${a} -- "${n}" --> ${a}`);
    else lines.push(`    ${a} -- "${n}" --> ${b}`);
  }
  lines.push('');
  lines.push('    classDef cat fill:#fafafa,stroke:#444,stroke-width:2px,color:#000');
  lines.push('```');
  return lines.join('\n');
}

function buildSelfHealLoop() {
  const cls = s => skillData[s]?.enabled ? 'enabled' : 'disabled';
  const lines = ['```mermaid', 'flowchart LR',
    `    heartbeat["heartbeat"]:::${cls('heartbeat')}`,
    `    skill-health["skill-health"]:::${cls('skill-health')}`,
    `    skill-evals["skill-evals"]:::${cls('skill-evals')}`,
    `    skill-repair["skill-repair"]:::${cls('skill-repair')}`,
    `    self-improve["self-improve"]:::${cls('self-improve')}`,
    '    cron-state[("memory/cron-state.json")]:::state',
    '',
    '    heartbeat --> skill-health',
    '    skill-health --> skill-evals',
    '    skill-evals --> skill-repair',
    '    skill-repair --> self-improve',
    '    self-improve -.-> heartbeat',
    '    heartbeat -..-> cron-state',
    '    skill-health -..-> cron-state',
    '    skill-repair -..-> cron-state',
    '',
    '    click heartbeat "../skills/heartbeat/SKILL.md"',
    '    click skill-health "../skills/skill-health/SKILL.md"',
    '    click skill-evals "../skills/skill-evals/SKILL.md"',
    '    click skill-repair "../skills/skill-repair/SKILL.md"',
    '    click self-improve "../skills/self-improve/SKILL.md"',
    '',
    '    classDef enabled fill:#fff,stroke:#000,stroke-width:2px,color:#000',
    '    classDef disabled fill:#f5f5f5,stroke:#bbb,color:#888',
    '    classDef state fill:#fffbe6,stroke:#b3a000,color:#333',
    '```'];
  return lines.join('\n');
}

function buildCategoryDiagrams() {
  const out = [];
  for (const cat of CATEGORIES) {
    const nodes = byCat[cat];
    if (!nodes.length) continue;
    out.push(`### ${CATEGORY_LABEL[cat]} (${nodes.length})`);
    out.push('');
    const m = ['```mermaid', 'flowchart LR'];
    m.push(`    subgraph ${cat}_cluster["${CATEGORY_LABEL[cat]}"]`);
    for (const s of nodes) m.push(`      ${nodeLabel(s)}`);
    m.push('    end');
    // intra edges
    const intra = edges.filter(e => skillToCat[e.from]===cat && skillToCat[e.to]===cat);
    const cross = edges.filter(e => skillToCat[e.from]===cat && skillToCat[e.to]!==cat);
    for (const e of intra) m.push(`    ${e.from} ${edgeArrow(e.type)} ${e.to}`);
    // ghost external
    const ghosts = new Set();
    for (const e of cross) {
      const ext = `${e.to}_ext`;
      if (!ghosts.has(ext)) {
        m.push(`    ${ext}["${e.to}"]:::external`);
        ghosts.add(ext);
      }
      m.push(`    ${e.from} ${edgeArrow(e.type)} ${ext}`);
    }
    // classes + clicks
    for (const s of nodes) {
      m.push(`    class ${s} ${skillData[s].enabled ? 'enabled' : 'disabled'}`);
      m.push(`    click ${s} "../skills/${s}/SKILL.md"`);
    }
    m.push('    classDef enabled fill:#fff,stroke:#000,stroke-width:2px,color:#000');
    m.push('    classDef disabled fill:#f5f5f5,stroke:#bbb,color:#888');
    m.push('    classDef external fill:none,stroke:#bbb,stroke-dasharray:3 3,color:#888');
    m.push('```');
    out.push(m.join('\n'));
    out.push('');
  }
  return out.join('\n');
}

function buildLegend() {
  return [
    '## Legend',
    '',
    '| Element | Meaning |',
    '|---------|---------|',
    '| `A --> B` | `depends_on` (frontmatter) |',
    '| `A -.-> B` | `consume` (chain output passed into B) |',
    '| `A -..-> B` | reactive trigger or derived shared-state edge |',
    '| **bold border** | `enabled: true` in `aeon.yml` |',
    '| _grey faded_ | `enabled: false` (catalog only) |',
    '| dashed ghost | cross-category dependency (drawn in target category) |',
    '',
    'Every node is clickable — points to `skills/<slug>/SKILL.md`. Click-through paths are relative to this file.',
    '',
    `> **Cron-state collapse:** every skill writes \`memory/cron-state.json\` as a heartbeat side effect. Those ${allSkills.length}+ edges are not drawn; treat \`heartbeat → skill-health → skill-evals → skill-repair\` as the canonical reader of that state.`,
  ].join('\n');
}

function buildSummaryTable() {
  const enabledCount = newEnabled.size;
  const byTypeCounts = { depends_on: 0, consume: 0, reactive: 0, shared_state: 0 };
  for (const e of edges) byTypeCounts[e.type]++;
  const rows = [];
  rows.push('| Metric | Count |');
  rows.push('|--------|-------|');
  rows.push(`| Skills total | ${allSkills.length} |`);
  rows.push(`| Skills enabled | ${enabledCount} |`);
  rows.push(`| Skills disabled | ${allSkills.length - enabledCount} |`);
  for (const c of CATEGORIES) rows.push(`| ${CATEGORY_LABEL[c]} | ${byCat[c].length} |`);
  rows.push(`| Edges (depends_on) | ${byTypeCounts.depends_on} |`);
  rows.push(`| Edges (consume) | ${byTypeCounts.consume} |`);
  rows.push(`| Edges (reactive) | ${byTypeCounts.reactive} |`);
  rows.push(`| Edges (shared-state derived) | ${byTypeCounts.shared_state} |`);
  return rows.join('\n');
}

function buildChangedSection() {
  if (mode === 'SKILL_GRAPH_NEW') return null;
  const lines = ['## What changed since last run', ''];
  if (!nodesDiff.added.length && !nodesDiff.removed.length &&
      !edgesDiff.added.length && !edgesDiff.removed.length &&
      !enabledDiff.added.length && !enabledDiff.removed.length) {
    lines.push('No structural delta vs prior `docs/skill-graph.md`. Generation was triggered by an input-fingerprint change (frontmatter / wording / non-graph edits).');
    return lines.join('\n');
  }
  if (nodesDiff.added.length) lines.push(`- **Added nodes (${nodesDiff.added.length})**: ${nodesDiff.added.map(s=>'`'+s+'`').join(', ')}`);
  if (nodesDiff.removed.length) lines.push(`- **Removed nodes (${nodesDiff.removed.length})**: ${nodesDiff.removed.map(s=>'`'+s+'`').join(', ')}`);
  if (edgesDiff.added.length) {
    const show = edgesDiff.added.slice(0, 12);
    const tail = edgesDiff.added.length > 12 ? ` and ${edgesDiff.added.length-12} more` : '';
    lines.push(`- **Added edges (${edgesDiff.added.length})**: ${show.map(e=>'`'+e+'`').join(', ')}${tail}`);
  }
  if (edgesDiff.removed.length) {
    const show = edgesDiff.removed.slice(0, 12);
    const tail = edgesDiff.removed.length > 12 ? ` and ${edgesDiff.removed.length-12} more` : '';
    lines.push(`- **Removed edges (${edgesDiff.removed.length})**: ${show.map(e=>'`'+e+'`').join(', ')}${tail}`);
  }
  if (enabledDiff.added.length) lines.push(`- **Newly enabled (${enabledDiff.added.length})**: ${enabledDiff.added.map(s=>'`'+s+'`').join(', ')}`);
  if (enabledDiff.removed.length) lines.push(`- **Newly disabled (${enabledDiff.removed.length})**: ${enabledDiff.removed.map(s=>'`'+s+'`').join(', ')}`);
  return lines.join('\n');
}

/* ---------- 4) Lint ---------- */
function lintMermaid(doc) {
  const errors = [];
  // gather code fences for mermaid
  const blocks = [];
  const fenceRe = /```mermaid\n([\s\S]*?)\n```/g;
  let m;
  while ((m = fenceRe.exec(doc)) !== null) blocks.push(m[1]);
  for (const block of blocks) {
    // bracket balance per line for [..]
    for (const line of block.split('\n')) {
      const lb = (line.match(/\[/g) || []).length;
      const rb = (line.match(/\]/g) || []).length;
      if (lb !== rb) errors.push(`unbalanced [] in mermaid line: ${line}`);
    }
    // subgraph/end balance
    const sg = (block.match(/^\s*subgraph\b/gm) || []).length;
    const en = (block.match(/^\s*end\s*$/gm) || []).length;
    if (sg !== en) errors.push(`subgraph/end mismatch (${sg} subgraph vs ${en} end)`);
  }
  // click directives reference real paths
  for (const m of doc.matchAll(/^\s*click\s+[a-z0-9-]+\s+"([^"]+)"/gm)) {
    let p = m[1];
    if (p.startsWith('../')) p = p.slice(3);
    if (!fs.existsSync(p)) errors.push(`click path missing: ${p}`);
  }
  return errors;
}

/* ---------- Compose ---------- */
const doc = [];
doc.push('# Skill Dependency Graph');
doc.push('');
doc.push(`> Auto-generated by \`skill-graph\` on ${today}. Mode: \`${mode}\`.`);
doc.push('');
doc.push(`**Verdict:** \`${verdict}\``);
doc.push('');
doc.push('Navigable Mermaid map of every Aeon skill, grouped by category, with a self-healing-loop callout, per-category drill-downs, click-through to source, and an enabled overlay.');
doc.push('');
doc.push('---');
doc.push('');

const changed = buildChangedSection();
if (changed) { doc.push(changed); doc.push(''); doc.push('---'); doc.push(''); }

doc.push('## Overview');
doc.push('');
doc.push(buildOverview());
doc.push('');
doc.push('Edge labels = number of edges crossing that category boundary (or staying inside it). Self-loops collapsed into a single line per category.');
doc.push('');
doc.push('---');
doc.push('');
doc.push('## Self-Healing Loop');
doc.push('');
doc.push('The most load-bearing chain in the fleet. Five skills + one shared state file form a closed loop that detects, classifies, and patches failures without operator intervention.');
doc.push('');
doc.push(buildSelfHealLoop());
doc.push('');
doc.push('---');
doc.push('');
doc.push('## Per-Category Drill-Downs');
doc.push('');
doc.push(buildCategoryDiagrams());
doc.push('---');
doc.push('');
doc.push(buildLegend());
doc.push('');
doc.push('---');
doc.push('');
doc.push('## Summary');
doc.push('');
doc.push(buildSummaryTable());
doc.push('');
const byType = { depends_on: 0, consume: 0, reactive: 0, shared_state: 0 };
for (const e of edges) byType[e.type]++;
doc.push(`> **Source-status:** skills parsed: ${allSkills.length} · depends_on: ${byType.depends_on} · consume: ${byType.consume} · reactive: ${byType.reactive} · shared-state derived: ${byType.shared_state} · enabled: ${newEnabled.size}/${allSkills.length} · mode: \`${mode}\``);
const docText = doc.join('\n') + '\n';

const lintErrors = lintMermaid(docText);
if (lintErrors.length) {
  mode = 'SKILL_GRAPH_ERROR';
  console.log('LINT_ERROR');
  for (const e of lintErrors) console.log(e);
  process.exit(2);
}

fs.writeFileSync(outPath, docText);

/* ---------- 7) Persist state ---------- */
const nodeListSha = sha1(allSkills.join('\n'));
const edgeListSha = sha1(edges.map(e => `${e.from}->${e.to}:${e.type}`).sort().join('\n'));
const state = {
  generated_at: today,
  input_fingerprint: fingerprint,
  skills_total: allSkills.length,
  enabled_count: newEnabled.size,
  edges: byType,
  node_list_sha: nodeListSha,
  edge_list_sha: edgeListSha,
};
fs.writeFileSync(stateFile, JSON.stringify(state, null, 2) + '\n');

/* ---------- 6) README idempotent insertion ---------- */
let readme = fs.readFileSync('README.md', 'utf8');
if (!/docs\/skill-graph\.md/.test(readme)) {
  // append a small section
  readme += '\n\n## Skill Graph\n\nSee [`docs/skill-graph.md`](docs/skill-graph.md) — a visual map of how skills connect, with the self-healing loop and content pipeline highlighted.\n';
  fs.writeFileSync('README.md', readme);
}

/* ---------- Output summary for runner ---------- */
const summary = {
  mode,
  verdict_one_line: verdict,
  skills_total: allSkills.length,
  enabled_count: newEnabled.size,
  edges: byType,
  added_nodes: nodesDiff.added.length,
  removed_nodes: nodesDiff.removed.length,
  added_edges: edgesDiff.added.length,
  removed_edges: edgesDiff.removed.length,
  enabled_added: enabledDiff.added.length,
  enabled_removed: enabledDiff.removed.length,
};
fs.writeFileSync('skill-graph-tmp/summary.json', JSON.stringify(summary, null, 2));
console.log(JSON.stringify(summary, null, 2));
