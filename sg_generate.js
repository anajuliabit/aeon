#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ROOT = '/home/runner/work/aeon/aeon';
process.chdir(ROOT);

const TODAY = '2026-05-31';
const OUT_PATH = 'docs/skill-graph.md';
const STATE_PATH = 'memory/topics/skill-graph-state.json';

const sha1 = (s) => crypto.createHash('sha1').update(s).digest('hex');
const sha1File = (p) => sha1(fs.readFileSync(p));

// ---- Step 1: Fingerprint (recompute) ----
let fpLines = [];
fpLines.push(sha1File('aeon.yml') + '  aeon.yml');
fpLines.push(sha1File('skills.json') + '  skills.json');

const skillDirs = fs.readdirSync('skills', { withFileTypes: true })
  .filter(d => d.isDirectory())
  .map(d => d.name)
  .sort();

const skills = [];
for (const slug of skillDirs) {
  const skillMd = path.join('skills', slug, 'SKILL.md');
  if (!fs.existsSync(skillMd)) continue;
  const content = fs.readFileSync(skillMd, 'utf8');

  const fmMatch = content.match(/^---\n([\s\S]*?)\n---/);
  let frontmatter = {};
  if (fmMatch) {
    const fm = fmMatch[1];
    for (const ln of fm.split('\n')) {
      fpLines.push(`${skillMd}: ${ln}`);
      const m = ln.match(/^([a-zA-Z_][a-zA-Z0-9_-]*):\s*(.*)$/);
      if (m) frontmatter[m[1]] = m[2].trim();
    }
  }
  for (const ln of content.split('\n')) {
    if (/^(depends_on:|- skill:)/.test(ln) || ln.includes('consume:') || ln.includes('parallel:') || ln.includes('trigger:')) {
      fpLines.push(ln);
    }
  }
  const refs = [...new Set((content.match(/memory\/(?:topics|state)\/[a-zA-Z0-9_.-]+/g) || []))].sort();
  for (const r of refs) fpLines.push(r);

  // depends_on
  let depends_on = [];
  const doMatch = content.match(/^depends_on:\s*\[([^\]]*)\]/m);
  if (doMatch) {
    depends_on = doMatch[1].split(',').map(s => s.trim().replace(/^['"]|['"]$/g, '')).filter(Boolean);
  } else {
    // multi-line yaml list
    const lines = content.split('\n');
    let inDeps = false;
    for (const ln of lines) {
      if (/^depends_on:\s*$/.test(ln)) { inDeps = true; continue; }
      if (inDeps) {
        const mm = ln.match(/^\s*-\s*['"]?([a-z0-9-]+)['"]?/);
        if (mm) depends_on.push(mm[1]);
        else if (/^\S/.test(ln)) break;
      }
    }
  }

  // tags
  let tags = [];
  const tagsMatch = (frontmatter.tags || '').match(/\[(.*)\]/);
  if (tagsMatch) {
    tags = tagsMatch[1].split(',').map(s => s.trim().replace(/^['"]|['"]$/g, '')).filter(Boolean);
  }

  // Detect explicit "Read skills/<slug>/SKILL.md" references — these denote chain consumers
  const readsSkills = new Set();
  {
    const re = /(?:Read|read|run|consume|execute|use[s]?)\b[^\n]{0,80}?\bskills\/([a-z][a-z0-9-]+)\/SKILL\.md/gi;
    let mm;
    while ((mm = re.exec(content)) !== null) {
      if (mm[1] !== slug) readsSkills.add(mm[1]);
    }
  }
  // memory refs with tightened read/write classification
  const memRefs = [];
  const lns = content.split('\n');
  // Article-producer detection: same line must contain articles/X.md AND a write verb
  let writesArticles = false;
  for (const ln of lns) {
    if (/articles\/[^\s"'`]+\.md/.test(ln) && /(write|save|append|>\s*articles|writeFileSync|^\s*\d+\.\s*\*\*Save\*\*)/i.test(ln)) {
      writesArticles = true;
      break;
    }
  }
  for (let i = 0; i < lns.length; i++) {
    const mRe = /memory\/(topics|state)\/[a-zA-Z0-9_.-]+/g;
    let m;
    while ((m = mRe.exec(lns[i])) !== null) {
      const ctx = lns.slice(Math.max(0, i - 1), Math.min(lns.length, i + 2)).join(' ');
      const pthEsc = m[0].replace(/[.]/g, '\\.');
      const isWrite = new RegExp('(write|writeFileSync|append|save|update|>\\s*memory)[^.]{0,40}' + pthEsc, 'i').test(ctx);
      memRefs.push({ path: m[0], mode: isWrite ? 'write' : 'read' });
    }
  }

  skills.push({ slug, frontmatter, tags, depends_on, memRefs, writesArticles, readsSkills: [...readsSkills] });
}

const rawText = fpLines.join('\n') + '\n';
const fingerprint = sha1(rawText);

// ---- Step 2: Parse aeon.yml ----
const aeonYml = fs.readFileSync('aeon.yml', 'utf8');
const aeonLines = aeonYml.split('\n');

// Parse skill entries — handle inline and multi-line
const aeonSkills = {};
let curSlug = null;
let curBuf = '';
let inSkillsBlock = false;
let inChainsBlock = false;
let inReactiveBlock = false;

function parseInlineBlock(s) {
  const out = {};
  // strip outer braces
  s = s.replace(/^\{|\}$/g, '').trim();
  // split on commas not inside quotes
  const parts = [];
  let depth = 0, q = null, cur = '';
  for (const ch of s) {
    if (q) {
      cur += ch;
      if (ch === q) q = null;
    } else if (ch === '"' || ch === "'") {
      q = ch; cur += ch;
    } else if (ch === '{' || ch === '[') { depth++; cur += ch; }
    else if (ch === '}' || ch === ']') { depth--; cur += ch; }
    else if (ch === ',' && depth === 0) {
      parts.push(cur); cur = '';
    } else cur += ch;
  }
  if (cur.trim()) parts.push(cur);
  for (const p of parts) {
    const m = p.match(/^\s*([a-zA-Z_][a-zA-Z0-9_-]*)\s*:\s*(.*)$/);
    if (m) {
      let val = m[2].trim();
      if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
      else if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
      if (val === 'true') val = true;
      else if (val === 'false') val = false;
      out[m[1]] = val;
    }
  }
  return out;
}

// Strip comments (# ...) outside quotes for safer block parsing
function stripComment(line) {
  let q = null, out = '';
  for (let i = 0; i < line.length; i++) {
    const ch = line[i];
    if (q) {
      out += ch;
      if (ch === q) q = null;
    } else if (ch === '"' || ch === "'") {
      q = ch; out += ch;
    } else if (ch === '#') {
      break;
    } else out += ch;
  }
  return out;
}

for (let i = 0; i < aeonLines.length; i++) {
  const raw = aeonLines[i];
  const ln = stripComment(raw);

  if (/^skills:\s*$/.test(ln)) { inSkillsBlock = true; inChainsBlock = false; inReactiveBlock = false; continue; }
  if (/^chains:\s*$/.test(ln)) { inSkillsBlock = false; inChainsBlock = true; inReactiveBlock = false; continue; }
  if (/^reactive:\s*$/.test(ln)) { inSkillsBlock = false; inChainsBlock = false; inReactiveBlock = true; continue; }
  if (/^[a-zA-Z]/.test(ln) && !ln.startsWith(' ') && !/^(skills:|chains:|reactive:|gateway:|channels:|telegram:|model:)/.test(ln)) {
    inSkillsBlock = false; inChainsBlock = false; inReactiveBlock = false;
  }

  if (inSkillsBlock) {
    // skill entries are at 2-space indent
    const m = ln.match(/^  ([a-z][a-z0-9-]*):\s*(.*)$/);
    if (m) {
      const slug = m[1];
      const rest = m[2].trim();
      if (rest.startsWith('{') && rest.endsWith('}')) {
        aeonSkills[slug] = parseInlineBlock(rest);
      } else if (rest.startsWith('{')) {
        // multi-line: collect until matching }
        let buf = rest;
        let depth = (rest.match(/\{/g) || []).length - (rest.match(/\}/g) || []).length;
        let j = i + 1;
        while (j < aeonLines.length && depth > 0) {
          const nxt = stripComment(aeonLines[j]);
          buf += ' ' + nxt.trim();
          depth += (nxt.match(/\{/g) || []).length;
          depth -= (nxt.match(/\}/g) || []).length;
          j++;
        }
        aeonSkills[slug] = parseInlineBlock(buf);
        i = j - 1;
      } else if (rest === '' || rest === '|') {
        // Look ahead — multi-line block with `{` on a subsequent line
        let j = i + 1;
        while (j < aeonLines.length && stripComment(aeonLines[j]).trim() === '') j++;
        const next = j < aeonLines.length ? stripComment(aeonLines[j]).trim() : '';
        if (next.startsWith('{')) {
          let buf = next;
          let depth = (next.match(/\{/g) || []).length - (next.match(/\}/g) || []).length;
          let k = j + 1;
          while (k < aeonLines.length && depth > 0) {
            const nxt = stripComment(aeonLines[k]);
            buf += ' ' + nxt.trim();
            depth += (nxt.match(/\{/g) || []).length;
            depth -= (nxt.match(/\}/g) || []).length;
            k++;
          }
          aeonSkills[slug] = parseInlineBlock(buf);
          i = k - 1;
        } else {
          aeonSkills[slug] = {};
        }
      } else {
        // skip
        aeonSkills[slug] = {};
      }
    }
  }
}

// Parse chains block (the only chain we care about: reppo-swarm)
const chains = {};
{
  // find chains: line
  const idx = aeonLines.findIndex(l => /^chains:\s*$/.test(l));
  if (idx >= 0) {
    let curChain = null;
    for (let i = idx + 1; i < aeonLines.length; i++) {
      const ln = aeonLines[i];
      if (/^[a-zA-Z]/.test(ln) && !ln.startsWith(' ')) break;
      const cm = ln.match(/^  ([a-z][a-z0-9-]*):\s*$/);
      if (cm) {
        curChain = cm[1];
        chains[curChain] = { schedule: '', on_error: 'fail-fast', steps: [] };
        continue;
      }
      if (curChain) {
        const sm = ln.match(/^    schedule:\s*"([^"]+)"/);
        if (sm) chains[curChain].schedule = sm[1];
        const oe = ln.match(/^    on_error:\s*(\S+)/);
        if (oe) chains[curChain].on_error = oe[1];
        const stepMatch = ln.match(/^      -\s*skill:\s*([a-z][a-z0-9-]*)/);
        if (stepMatch) {
          chains[curChain].steps.push({ skill: stepMatch[1], consume: [] });
        }
        const consumeMatch = ln.match(/^\s+consume:\s*\[([^\]]*)\]/);
        if (consumeMatch && chains[curChain].steps.length) {
          chains[curChain].steps[chains[curChain].steps.length - 1].consume =
            consumeMatch[1].split(',').map(s => s.trim()).filter(Boolean);
        }
      }
    }
  }
}

// ---- Step 3: Categorize via skills.json + tag fallback ----
const skillsJson = JSON.parse(fs.readFileSync('skills.json', 'utf8'));
const catMap = {};
for (const s of skillsJson.skills) catMap[s.slug] = s.category;

const TAG_TO_CAT = {
  research: 'research',
  dev: 'dev',
  crypto: 'crypto',
  social: 'social',
  meta: 'productivity',
  productivity: 'productivity',
  growth: 'productivity',
  community: 'productivity',
  reppo: 'crypto',
  trading: 'crypto',
  hyperliquid: 'crypto',
};

function categorize(skill) {
  const fromJson = catMap[skill.slug];
  if (fromJson && fromJson !== 'other') return fromJson;
  for (const t of skill.tags) {
    if (TAG_TO_CAT[t]) return TAG_TO_CAT[t];
  }
  return 'productivity';
}

for (const s of skills) {
  s.category = categorize(s);
  const cfg = aeonSkills[s.slug] || {};
  s.enabled = cfg.enabled === true;
  s.schedule = cfg.schedule || '';
  s.model = cfg.model || '';
  s.var = cfg.var || '';
}

// reppo skills not in aeon.yml directly may be enabled:false; ensure they get marked
for (const s of skills) {
  if (s.enabled === undefined) s.enabled = false;
}

// ---- Step 4: Build edges ----
const slugSet = new Set(skills.map(s => s.slug));

// depends_on edges
const dependsEdges = [];
for (const s of skills) {
  for (const dep of s.depends_on) {
    if (slugSet.has(dep)) dependsEdges.push({ from: s.slug, to: dep, type: 'depends' });
  }
}

// chain consume edges
const consumeEdges = [];
for (const ch of Object.values(chains)) {
  for (const step of ch.steps) {
    for (const c of step.consume) {
      if (slugSet.has(step.skill) && slugSet.has(c)) {
        consumeEdges.push({ from: c, to: step.skill, type: 'consume' });
      }
    }
  }
}

// reactive edges: none uncommented in aeon.yml currently → 0

// shared-state edges (derived):
// For each topic/state path, find writers and readers.
const refMap = {}; // path -> { writers: [slug], readers: [slug] }
for (const s of skills) {
  for (const r of s.memRefs) {
    if (!refMap[r.path]) refMap[r.path] = { writers: new Set(), readers: new Set() };
    if (r.mode === 'write') refMap[r.path].writers.add(s.slug);
    else refMap[r.path].readers.add(s.slug);
  }
}

const sharedEdgesRaw = [];
for (const [pth, { writers, readers }] of Object.entries(refMap)) {
  for (const w of writers) {
    for (const r of readers) {
      if (w === r) continue;
      sharedEdgesRaw.push({ from: w, to: r, type: 'shared', via: pth });
    }
  }
}
// Dedup by from->to (keep first via)
const sharedSeen = new Set();
const sharedEdges = [];
for (const e of sharedEdgesRaw) {
  const key = `${e.from}->${e.to}`;
  if (sharedSeen.has(key)) continue;
  sharedSeen.add(key);
  sharedEdges.push(e);
}

// Article-pipeline edges: research-category article producers + explicit producers
const PIPELINE_TARGETS = ['syndicate-article', 'rss-feed', 'update-gallery'];
const EXPLICIT_PRODUCERS = new Set(['project-lens', 'repo-article']);
const pipelineEdges = [];
for (const s of skills) {
  const isResearchProducer = s.category === 'research' && s.writesArticles;
  const isExplicit = EXPLICIT_PRODUCERS.has(s.slug);
  if (!isResearchProducer && !isExplicit) continue;
  if (PIPELINE_TARGETS.includes(s.slug)) continue;
  for (const tgt of PIPELINE_TARGETS) {
    if (slugSet.has(tgt)) pipelineEdges.push({ from: s.slug, to: tgt, type: 'shared' });
  }
}

// Self-healing loop edges — explicit (keeps cron-state.json collapsed)
const selfHealEdges = [
  { from: 'heartbeat', to: 'skill-health', type: 'shared' },
  { from: 'skill-health', to: 'skill-evals', type: 'shared' },
  { from: 'skill-evals', to: 'skill-repair', type: 'shared' },
  { from: 'skill-repair', to: 'self-improve', type: 'shared' },
].filter(e => slugSet.has(e.from) && slugSet.has(e.to));

// Explicit skill-reads-skill edges (e.g. daily-routine "Read skills/X/SKILL.md")
// Edge convention: consumer -> source ("A depends on / consumes B").
const skillReadEdges = [];
for (const s of skills) {
  for (const target of s.readsSkills) {
    if (slugSet.has(target) && target !== s.slug) {
      skillReadEdges.push({ from: s.slug, to: target, type: 'shared' });
    }
  }
}

// Merge shared edges with pipeline + selfheal + skillRead, dedup by from->to
const allSharedMap = new Map();
for (const e of [...sharedEdges, ...pipelineEdges, ...selfHealEdges, ...skillReadEdges]) {
  const k = `${e.from}->${e.to}`;
  if (!allSharedMap.has(k)) allSharedMap.set(k, e);
}
const allSharedEdges = [...allSharedMap.values()];

// ---- Step 5: Diff vs prior ----
let priorState = null;
if (fs.existsSync(STATE_PATH)) {
  priorState = JSON.parse(fs.readFileSync(STATE_PATH, 'utf8'));
}

let mode;
if (priorState && priorState.input_fingerprint === fingerprint) {
  mode = 'SKILL_GRAPH_NO_CHANGE';
} else if (!priorState) {
  mode = 'SKILL_GRAPH_NEW';
} else {
  mode = 'SKILL_GRAPH_OK';
}

// Read prior skill-graph.md to extract prior node slugs and enabled slugs
let priorNodes = new Set();
let priorEnabled = new Set();
let priorEdges = new Set();
if (fs.existsSync(OUT_PATH)) {
  const prev = fs.readFileSync(OUT_PATH, 'utf8');
  // click <slug> "../skills/<slug>/SKILL.md" — authoritative slug source
  const clickRe = /click\s+\S+\s+"\.\.\/skills\/([a-z][a-z0-9-]*)\/SKILL\.md"/g;
  let m;
  while ((m = clickRe.exec(prev)) !== null) priorNodes.add(m[1]);
  // enabled overlay — list of enabled at the bottom
  const enmatch = prev.match(/### Enabled skills \(\d+\)\s*\n\n([^\n]+)/);
  if (enmatch) {
    const slugs = enmatch[1].match(/`([a-z][a-z0-9-]*)`/g) || [];
    for (const s of slugs) priorEnabled.add(s.replace(/`/g, ''));
  }
  // Build a nodeId → actual-slug map by parsing declarations like:
  //   syndicate_ext[syndicate-article]:::external
  //   article["article<br/>0 14 * * *"]:::enabled
  //   article[article]:::disabled
  // Map back to actual slugs.
  const nodeIdMap = {};
  // Also pre-populate with declared skills as identity mapping
  for (const s of skills) nodeIdMap[s.slug] = s.slug;
  // Match: NAME[LABEL]:::class  or  NAME["LABEL"]
  const declRe = /^\s*([a-zA-Z_][a-zA-Z0-9_-]*)\[(?:"([^"]+)"|([^\]]+))\]/gm;
  while ((m = declRe.exec(prev)) !== null) {
    const id = m[1];
    const label = (m[2] || m[3] || '').split('<br/>')[0].trim();
    if (/^[a-z][a-z0-9-]*$/.test(label) && slugSet.has(label)) {
      nodeIdMap[id] = label;
    } else if (slugSet.has(id)) {
      nodeIdMap[id] = id;
    }
  }
  // Strip code fences and only look at edges inside mermaid blocks
  const edgeRe = /\b([a-zA-Z_][a-zA-Z0-9_-]*)\s*(?:--+>|-\.->|-\.\.->)\s*([a-zA-Z_][a-zA-Z0-9_-]*)/g;
  while ((m = edgeRe.exec(prev)) !== null) {
    const fromId = m[1];
    const toId = m[2];
    if (['research', 'dev', 'crypto', 'social', 'productivity'].includes(fromId)) continue;
    if (['research', 'dev', 'crypto', 'social', 'productivity'].includes(toId)) continue;
    // self-healing loop uses local var names heartbeat/health/evals/repair/improve/state
    const selfHealMap = {
      heartbeat: 'heartbeat', health: 'skill-health', evals: 'skill-evals',
      repair: 'skill-repair', improve: 'self-improve', state: null,
    };
    let from = nodeIdMap[fromId] || (fromId in selfHealMap ? selfHealMap[fromId] : null);
    let to = nodeIdMap[toId] || (toId in selfHealMap ? selfHealMap[toId] : null);
    if (!from || !to) continue;
    priorEdges.add(`${from}->${to}`);
  }
}

const currentNodes = new Set(skills.map(s => s.slug));
const currentEnabled = new Set(skills.filter(s => s.enabled).map(s => s.slug));
const currentEdgeKeys = new Set();
for (const e of dependsEdges) currentEdgeKeys.add(`${e.from}->${e.to}`);
for (const e of consumeEdges) currentEdgeKeys.add(`${e.from}->${e.to}`);
for (const e of allSharedEdges) currentEdgeKeys.add(`${e.from}->${e.to}`);

const addedNodes = [...currentNodes].filter(n => !priorNodes.has(n));
const removedNodes = [...priorNodes].filter(n => !currentNodes.has(n));
const addedEnabled = [...currentEnabled].filter(n => !priorEnabled.has(n));
const removedEnabled = [...priorEnabled].filter(n => !currentEnabled.has(n));
const addedEdges = [...currentEdgeKeys].filter(k => !priorEdges.has(k));
const removedEdges = [...priorEdges].filter(k => !currentEdgeKeys.has(k));

// Verdict line
let verdictParts = [];
if (mode === 'SKILL_GRAPH_NEW') {
  verdictParts.push(`first run with state file; baseline established for ${skills.length} skills across 5 categories (${currentEnabled.size} enabled)`);
} else {
  if (addedNodes.length) verdictParts.push(`NEW_SKILLS: ${addedNodes.sort().join(', ')}`);
  if (removedNodes.length) verdictParts.push(`RETIRED_SKILLS: ${removedNodes.sort().join(', ')}`);
  if (addedEnabled.length) verdictParts.push(`NEW_ENABLED: ${addedEnabled.sort().join(', ')}`);
  if (removedEnabled.length) verdictParts.push(`NEW_DISABLED: ${removedEnabled.sort().join(', ')}`);
  if (addedEdges.length) verdictParts.push(`NEW_DEPS: ${addedEdges.sort().slice(0, 6).join(', ')}${addedEdges.length > 6 ? ` (+${addedEdges.length - 6} more)` : ''}`);
  if (removedEdges.length) verdictParts.push(`REMOVED_DEPS: ${removedEdges.sort().slice(0, 6).join(', ')}${removedEdges.length > 6 ? ` (+${removedEdges.length - 6} more)` : ''}`);
}
let verdictOneLine;
if (verdictParts.length === 0) verdictOneLine = 'ARCHITECTURE_OK';
else verdictOneLine = verdictParts.join(' · ');

// ---- Categorize by category for diagrams ----
const CATEGORIES = [
  { key: 'research', title: 'Research & Content' },
  { key: 'dev', title: 'Dev & Code' },
  { key: 'crypto', title: 'Crypto & Markets' },
  { key: 'social', title: 'Social' },
  { key: 'productivity', title: 'Productivity & Meta' },
];

const byCategory = {};
for (const c of CATEGORIES) byCategory[c.key] = [];
for (const s of skills) {
  if (!byCategory[s.category]) byCategory[s.category] = [];
  byCategory[s.category].push(s);
}
for (const k of Object.keys(byCategory)) byCategory[k].sort((a, b) => a.slug.localeCompare(b.slug));

const slugCategory = {};
for (const s of skills) slugCategory[s.slug] = s.category;

// ---- Build overview diagram (cross-category edge counts) ----
const crossCounts = {};
const allEdges = [
  ...dependsEdges.map(e => ({ ...e, type: 'depends' })),
  ...consumeEdges.map(e => ({ ...e, type: 'consume' })),
  ...allSharedEdges.map(e => ({ ...e, type: 'shared' })),
];
for (const e of allEdges) {
  const fc = slugCategory[e.from];
  const tc = slugCategory[e.to];
  if (!fc || !tc) continue;
  const key = `${fc}->${tc}`;
  crossCounts[key] = (crossCounts[key] || 0) + 1;
}

// ---- Build document ----
const lines = [];
lines.push('# Skill Dependency Graph');
lines.push('');
lines.push(`> Auto-generated by \`skill-graph\` on ${TODAY}. Mode: \`${mode}\`.`);
lines.push('');
lines.push(`**Verdict:** \`${verdictOneLine}\``);
lines.push('');
lines.push('Navigable Mermaid map of every Aeon skill, grouped by category, with a self-healing-loop callout, per-category drill-downs, click-through to source, and an enabled overlay.');
lines.push('');
lines.push('---');
lines.push('');

// What changed
if (mode !== 'SKILL_GRAPH_NEW') {
  lines.push('## What changed since last run');
  lines.push('');
  if (addedNodes.length === 0 && removedNodes.length === 0 && addedEnabled.length === 0 && removedEnabled.length === 0 && addedEdges.length === 0 && removedEdges.length === 0) {
    lines.push('Structural fingerprint shifted (frontmatter or embedded references), but the node/edge/enabled-state surface is unchanged.');
  } else {
    if (addedNodes.length) lines.push(`- **Added skills (${addedNodes.length})**: ${addedNodes.sort().map(s => '`' + s + '`').join(', ')}`);
    if (removedNodes.length) lines.push(`- **Removed skills (${removedNodes.length})**: ${removedNodes.sort().map(s => '`' + s + '`').join(', ')}`);
    if (addedEnabled.length) lines.push(`- **Newly enabled (${addedEnabled.length})**: ${addedEnabled.sort().map(s => '`' + s + '`').join(', ')}`);
    if (removedEnabled.length) lines.push(`- **Newly disabled (${removedEnabled.length})**: ${removedEnabled.sort().map(s => '`' + s + '`').join(', ')}`);
    if (addedEdges.length) lines.push(`- **Added edges (${addedEdges.length})**: ${addedEdges.sort().slice(0, 12).map(s => '`' + s + '`').join(', ')}${addedEdges.length > 12 ? ` and ${addedEdges.length - 12} more` : ''}`);
    if (removedEdges.length) lines.push(`- **Removed edges (${removedEdges.length})**: ${removedEdges.sort().slice(0, 12).map(s => '`' + s + '`').join(', ')}${removedEdges.length > 12 ? ` and ${removedEdges.length - 12} more` : ''}`);
  }
  lines.push('');
  lines.push('---');
  lines.push('');
}

// Overview
lines.push('## Overview');
lines.push('');
lines.push('```mermaid');
lines.push('flowchart LR');
for (const c of CATEGORIES) {
  const n = byCategory[c.key].length;
  lines.push(`    ${c.key}["${c.title}<br/>(${n})"]:::cat`);
}
lines.push('');
// emit cross-category edge counts (skip self-loops to keep it readable, but emit if any are cross)
const sortedCross = Object.entries(crossCounts).sort((a, b) => b[1] - a[1]);
for (const [k, cnt] of sortedCross) {
  const [from, to] = k.split('->');
  if (from === to) continue;
  lines.push(`    ${from} -- "${cnt}" --> ${to}`);
}
// self-loops separately at the end
for (const [k, cnt] of sortedCross) {
  const [from, to] = k.split('->');
  if (from !== to) continue;
  lines.push(`    ${from} -- "${cnt}" --> ${to}`);
}
lines.push('');
lines.push('    classDef cat fill:#fafafa,stroke:#444,stroke-width:2px,color:#000');
lines.push('```');
lines.push('');
lines.push('Edge labels = count of edges crossing that category boundary. Self-loops collapsed into a single line per category.');
lines.push('');
lines.push('---');
lines.push('');

// Self-healing loop
lines.push('## Self-Healing Loop');
lines.push('');
lines.push('The most load-bearing chain in the fleet. Five skills + one shared state file form a closed loop that detects, classifies, and patches failures without operator intervention.');
lines.push('');
lines.push('```mermaid');
lines.push('flowchart LR');
lines.push('    heartbeat[heartbeat<br/>3x daily] --> health[skill-health<br/>daily]');
lines.push('    health --> evals[skill-evals<br/>weekly]');
lines.push('    evals --> repair[skill-repair<br/>reactive]');
lines.push('    repair --> improve[self-improve<br/>every 2d]');
lines.push('    improve -.-> heartbeat');
lines.push('');
lines.push('    state[(memory/cron-state.json<br/>+ memory/issues/)]:::state');
lines.push('    heartbeat -.-> state');
lines.push('    health -.-> state');
lines.push('    evals -.-> state');
lines.push('    repair -.-> state');
lines.push('');
lines.push('    click heartbeat "../skills/heartbeat/SKILL.md"');
lines.push('    click health "../skills/skill-health/SKILL.md"');
lines.push('    click evals "../skills/skill-evals/SKILL.md"');
lines.push('    click repair "../skills/skill-repair/SKILL.md"');
lines.push('    click improve "../skills/self-improve/SKILL.md"');
lines.push('');
lines.push('    classDef state fill:#fff8e1,stroke:#f57c00,stroke-dasharray:4 4,color:#000');
lines.push('```');
lines.push('');
lines.push('> Every skill writes `memory/cron-state.json` after each run. This single shared state is what makes the loop self-correcting — rather than ~120 explicit edges into the loop, it is collapsed into one state node here. Same convention applies to the per-category diagrams below.');
lines.push('');
lines.push('---');
lines.push('');

// Per-category diagrams
lines.push('## Per-Category Diagrams');
lines.push('');

function nodeLabel(s) {
  if (s.enabled && s.schedule) {
    return `${s.slug}["${s.slug}<br/>${s.schedule}"]:::enabled`;
  } else if (s.enabled) {
    return `${s.slug}["${s.slug}"]:::enabled`;
  }
  return `${s.slug}[${s.slug}]:::disabled`;
}

for (const c of CATEGORIES) {
  const items = byCategory[c.key];
  if (!items.length) continue;
  lines.push(`### ${c.title} (${items.length})`);
  lines.push('');
  lines.push('```mermaid');
  lines.push('flowchart LR');
  lines.push(`    subgraph ${c.key} [" ${c.title} "]`);
  lines.push('        direction TB');
  for (const s of items) {
    lines.push(`        ${nodeLabel(s)}`);
  }
  lines.push('    end');
  lines.push('');

  // Collect cross-category edges that touch this category
  const intraEdges = [];
  const crossOut = []; // this -> other (other is external)
  for (const e of allEdges) {
    const fc = slugCategory[e.from];
    const tc = slugCategory[e.to];
    if (fc === c.key && tc === c.key) intraEdges.push(e);
    else if (fc === c.key && tc !== c.key) crossOut.push(e);
  }

  // Declare external ghost nodes for crossOut (dedup by slug, hyphenated IDs are valid mermaid)
  const externalSlugs = [...new Set(crossOut.map(e => e.to))].sort();
  let extIdx = 0;
  const extNameMap = {};
  for (const ex of externalSlugs) {
    extIdx++;
    const name = `${ex}_ext${extIdx}`;
    extNameMap[ex] = name;
    lines.push(`    ${name}[${ex}]:::external`);
  }
  if (externalSlugs.length) lines.push('');

  for (const e of intraEdges) {
    const arrow = e.type === 'depends' ? '-->' : (e.type === 'consume' ? '-.->' : '-..->');
    lines.push(`    ${e.from} ${arrow} ${e.to}`);
  }
  for (const e of crossOut) {
    const arrow = e.type === 'depends' ? '-->' : (e.type === 'consume' ? '-.->' : '-..->');
    lines.push(`    ${e.from} ${arrow} ${extNameMap[e.to]}`);
  }
  if (intraEdges.length || crossOut.length) lines.push('');

  for (const s of items) {
    lines.push(`    click ${s.slug} "../skills/${s.slug}/SKILL.md"`);
  }
  lines.push('');
  lines.push('    classDef enabled fill:#fff,stroke:#000,stroke-width:2px,color:#000');
  lines.push('    classDef disabled fill:#f5f5f5,stroke:#bbb,color:#888');
  lines.push('    classDef external fill:none,stroke:#bbb,stroke-dasharray:3 3,color:#888');
  lines.push('```');
  lines.push('');

  const enabledCount = items.filter(x => x.enabled).length;
  if (enabledCount === 0) {
    lines.push(`None enabled this run.`);
  } else {
    lines.push(`${enabledCount} enabled in this category.`);
  }
  lines.push('');
}

// Legend
lines.push('---');
lines.push('');
lines.push('## Legend');
lines.push('');
lines.push('| Edge | Meaning |');
lines.push('|------|---------|');
lines.push('| `-->` solid | `depends_on` — declared dependency in frontmatter |');
lines.push('| `-.->` dashed | `consume` — chain step receives output from prior step |');
lines.push('| `-..->` dotted | reactive trigger or shared-state dependency derived from `memory/topics/*` or `memory/state/*` reads/writes |');
lines.push('');
lines.push('| Visual | Meaning |');
lines.push('|--------|---------|');
lines.push('| **Bold black border** | Skill is `enabled: true` in `aeon.yml` — schedule shown in label |');
lines.push('| Faded grey fill | Skill is `enabled: false` |');
lines.push('| Dashed grey outline | Ghost node — declared in another category, shown for cross-category edges |');
lines.push('');
lines.push('**Click any node** on github.com to open its `SKILL.md` source.');
lines.push('');
lines.push('> Collapsed convention: every skill writes `memory/cron-state.json` after each run. To keep the graph readable, those ~120 edges into the self-healing loop are collapsed into the single state node above. Same applies to `memory/skill-runs/` history.');
lines.push('');
lines.push('---');
lines.push('');

// Summary table
const totalEnabled = skills.filter(s => s.enabled).length;
const totalDisabled = skills.length - totalEnabled;
lines.push('## Summary');
lines.push('');
lines.push('| Metric | Count |');
lines.push('|--------|------:|');
lines.push(`| Total skills | ${skills.length} |`);
lines.push('| Categories | 5 |');
lines.push(`| Enabled | ${totalEnabled} |`);
lines.push(`| Disabled | ${totalDisabled} |`);
lines.push(`| Direct dependencies (\`depends_on\`) | ${dependsEdges.length} |`);
lines.push(`| Chain \`consume\` edges | ${consumeEdges.length} |`);
lines.push(`| Reactive trigger edges | 0 (commented) |`);
lines.push(`| Derived shared-state edges | ${allSharedEdges.length} |`);
lines.push('');

// By category
lines.push('### By category');
lines.push('');
lines.push('| Category | Total | Enabled |');
lines.push('|----------|------:|--------:|');
for (const c of CATEGORIES) {
  const items = byCategory[c.key];
  const en = items.filter(x => x.enabled).length;
  lines.push(`| ${c.title} | ${items.length} | ${en} |`);
}
lines.push('');

const enabledList = skills.filter(s => s.enabled).map(s => s.slug).sort();
lines.push(`### Enabled skills (${enabledList.length})`);
lines.push('');
lines.push(enabledList.map(s => '`' + s + '`').join(' · '));
lines.push('');

// Chains
lines.push('### Chains');
lines.push('');
lines.push('| Chain | Schedule | Steps |');
lines.push('|-------|----------|-------|');
for (const [name, ch] of Object.entries(chains)) {
  const stepDesc = ch.steps.map(st => {
    if (st.consume.length) return `\`${st.skill}\` (consume: ${st.consume.map(c => '`' + c + '`').join(', ')})`;
    return `\`${st.skill}\``;
  }).join(' → ');
  lines.push(`| \`${name}\` | \`${ch.schedule}\` | ${stepDesc} |`);
}
lines.push('');

// Direct dependencies
if (dependsEdges.length) {
  lines.push('### Direct dependencies');
  lines.push('');
  lines.push('| Skill | Depends on |');
  lines.push('|-------|-----------|');
  for (const e of dependsEdges.sort((a, b) => a.from.localeCompare(b.from))) {
    lines.push(`| \`${e.from}\` | \`${e.to}\` |`);
  }
  lines.push('');
}

// Footer
lines.push('---');
lines.push('');
lines.push(`skills parsed: ${skills.length} · depends_on: ${dependsEdges.length} · consume: ${consumeEdges.length} · reactive: 0 · shared-state derived: ${allSharedEdges.length} · enabled: ${totalEnabled}/${skills.length} · mode: ${mode}`);

const doc = lines.join('\n') + '\n';

// ---- Lint ----
let lintErrors = [];
// Check every click directive references a valid skill path
const clickRe = /click\s+([a-z][a-z0-9_-]*)\s+"\.\.\/skills\/([a-z][a-z0-9-]*)\/SKILL\.md"/g;
let m;
while ((m = clickRe.exec(doc)) !== null) {
  const p = `skills/${m[2]}/SKILL.md`;
  if (!fs.existsSync(p)) lintErrors.push(`broken click path: ${p}`);
}
// every subgraph closed
const subgraphCount = (doc.match(/^\s*subgraph\b/gm) || []).length;
const endCount = (doc.match(/^\s+end\s*$/gm) || []).length;
if (subgraphCount > endCount) lintErrors.push(`subgraph/end mismatch: ${subgraphCount} open vs ${endCount} close`);

if (lintErrors.length) {
  console.log('LINT_FAIL');
  for (const e of lintErrors) console.log('  ' + e);
  process.exit(2);
}

// Write doc
fs.writeFileSync(OUT_PATH, doc);

// node_list_sha + edge_list_sha
const nodeListSha = sha1(skills.map(s => s.slug).sort().join('\n'));
const edgeTuples = [];
for (const e of dependsEdges) edgeTuples.push(`depends:${e.from}->${e.to}`);
for (const e of consumeEdges) edgeTuples.push(`consume:${e.from}->${e.to}`);
for (const e of allSharedEdges) edgeTuples.push(`shared:${e.from}->${e.to}`);
const edgeListSha = sha1(edgeTuples.sort().join('\n'));

const state = {
  generated_at: TODAY,
  input_fingerprint: fingerprint,
  skills_total: skills.length,
  enabled_count: totalEnabled,
  edges: {
    depends_on: dependsEdges.length,
    consume: consumeEdges.length,
    reactive: 0,
    shared_state: allSharedEdges.length,
  },
  node_list_sha: nodeListSha,
  edge_list_sha: edgeListSha,
};
fs.writeFileSync(STATE_PATH, JSON.stringify(state, null, 2) + '\n');

// Footer info for the runner
console.log('MODE:', mode);
console.log('VERDICT:', verdictOneLine);
console.log('SKILLS:', skills.length, 'ENABLED:', totalEnabled);
console.log('EDGES depends:', dependsEdges.length, 'consume:', consumeEdges.length, 'shared:', allSharedEdges.length);
console.log('FINGERPRINT:', fingerprint);
console.log('ADDED_NODES:', addedNodes.length, addedNodes.slice(0, 10).join(','));
console.log('REMOVED_NODES:', removedNodes.length, removedNodes.slice(0, 10).join(','));
console.log('ADDED_ENABLED:', addedEnabled.length, addedEnabled.slice(0, 10).join(','));
console.log('REMOVED_ENABLED:', removedEnabled.length, removedEnabled.slice(0, 10).join(','));
console.log('ADDED_EDGES:', addedEdges.length);
console.log('REMOVED_EDGES:', removedEdges.length);
console.log('WROTE:', OUT_PATH);
console.log('STATE:', STATE_PATH);
console.log('LINES:', doc.split('\n').length);
