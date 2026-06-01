#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { execSync } = require('child_process');

const ROOT = '/home/runner/work/aeon/aeon';
process.chdir(ROOT);

const sha1 = (s) => crypto.createHash('sha1').update(s).digest('hex');
const sha1File = (p) => sha1(fs.readFileSync(p));

// --- Step 1: Fingerprint ---
let lines = [];
lines.push(sha1File('aeon.yml') + '  aeon.yml');
lines.push(sha1File('skills.json') + '  skills.json');

const skillDirs = fs.readdirSync('skills', { withFileTypes: true })
  .filter(d => d.isDirectory())
  .map(d => d.name)
  .sort();

const skills = [];
for (const slug of skillDirs) {
  const skillMd = path.join('skills', slug, 'SKILL.md');
  if (!fs.existsSync(skillMd)) continue;
  const content = fs.readFileSync(skillMd, 'utf8');

  // frontmatter (between first two ---)
  const fmMatch = content.match(/^---\n([\s\S]*?)\n---/);
  let frontmatter = {};
  if (fmMatch) {
    const fm = fmMatch[1];
    for (const ln of fm.split('\n')) {
      lines.push(`${skillMd}: ${ln}`);
      const m = ln.match(/^([a-zA-Z_][a-zA-Z0-9_-]*):\s*(.*)$/);
      if (m) {
        frontmatter[m[1]] = m[2].trim();
      }
    }
  }
  // edges-ish content
  for (const ln of content.split('\n')) {
    if (/^(depends_on:|- skill:)/.test(ln) || ln.includes('consume:') || ln.includes('parallel:') || ln.includes('trigger:')) {
      lines.push(ln);
    }
  }
  const refs = [...new Set((content.match(/memory\/(?:topics|state)\/[a-zA-Z0-9_.-]+/g) || []))].sort();
  for (const r of refs) lines.push(r);

  // capture memory refs with read/write classification
  const memRefs = [];
  const lns = content.split('\n');
  for (let i = 0; i < lns.length; i++) {
    const mRe = /memory\/(topics|state)\/[a-zA-Z0-9_.-]+/g;
    let m;
    while ((m = mRe.exec(lns[i])) !== null) {
      const ctxStart = Math.max(0, i - 1);
      const ctxEnd = Math.min(lns.length, i + 2);
      const ctx = lns.slice(ctxStart, ctxEnd).join(' ');
      const isWrite = /(write|save|append|>|update)\b.*?(topics|state)\//i.test(ctx);
      memRefs.push({ path: m[0], mode: isWrite ? 'write' : 'read' });
    }
  }

  skills.push({ slug, frontmatter, memRefs, content });
}

const rawText = lines.join('\n') + '\n';
fs.writeFileSync('/tmp/sg-raw.txt', rawText);
const fingerprint = sha1(rawText);

// --- Step 1: Compare with state file ---
let priorState = null;
const stateFile = 'memory/topics/skill-graph-state.json';
if (fs.existsSync(stateFile)) {
  priorState = JSON.parse(fs.readFileSync(stateFile, 'utf8'));
}

let mode;
if (priorState && priorState.input_fingerprint === fingerprint) {
  mode = 'SKILL_GRAPH_NO_CHANGE';
} else if (!priorState) {
  mode = 'SKILL_GRAPH_NEW';
} else {
  mode = 'SKILL_GRAPH_OK';
}

console.log('FINGERPRINT:', fingerprint);
console.log('PRIOR_FINGERPRINT:', priorState ? priorState.input_fingerprint : '(none)');
console.log('MODE:', mode);
console.log('SKILLS_PARSED:', skills.length);
console.log('SKILL_DIRS:', skillDirs.length);

// dump skills metadata for later steps
fs.writeFileSync('/tmp/sg-skills.json', JSON.stringify({ fingerprint, mode, skills, priorState }, null, 0));
console.log('STATE_WRITTEN:/tmp/sg-skills.json');
