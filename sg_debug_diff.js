#!/usr/bin/env node
const fs = require('fs');
const { execSync } = require('child_process');
const prev = execSync('git show HEAD:docs/skill-graph.md').toString();

// Rebuild slugSet
const skillDirs = fs.readdirSync('skills').filter(n => fs.statSync('skills/' + n).isDirectory());
const slugSet = new Set(skillDirs);

const nodeIdMap = {};
for (const s of skillDirs) nodeIdMap[s] = s;
const declRe = /^\s*([a-zA-Z_][a-zA-Z0-9_-]*)\[(?:"([^"]+)"|([^\]]+))\]/gm;
let m;
while ((m = declRe.exec(prev)) !== null) {
  const id = m[1];
  const label = (m[2] || m[3] || '').split('<br/>')[0].trim();
  if (/^[a-z][a-z0-9-]*$/.test(label) && slugSet.has(label)) nodeIdMap[id] = label;
  else if (slugSet.has(id)) nodeIdMap[id] = id;
}

const edgeRe = /\b([a-zA-Z_][a-zA-Z0-9_-]*)\s*(?:--+>|-\.->|-\.\.->)\s*([a-zA-Z_][a-zA-Z0-9_-]*)/g;
const priorEdges = new Set();
while ((m = edgeRe.exec(prev)) !== null) {
  const fromId = m[1], toId = m[2];
  if (['research', 'dev', 'crypto', 'social', 'productivity'].includes(fromId)) continue;
  if (['research', 'dev', 'crypto', 'social', 'productivity'].includes(toId)) continue;
  const selfHealMap = { heartbeat: 'heartbeat', health: 'skill-health', evals: 'skill-evals', repair: 'skill-repair', improve: 'self-improve', state: null };
  let from = nodeIdMap[fromId] || selfHealMap[fromId];
  let to = nodeIdMap[toId] || selfHealMap[toId];
  if (!from || !to) continue;
  priorEdges.add(from + '->' + to);
}

console.log('PRIOR_EDGES:', priorEdges.size);
for (const k of [...priorEdges].sort()) console.log('  ', k);
