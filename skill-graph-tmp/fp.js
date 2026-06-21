#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

process.chdir('/home/runner/work/aeon/aeon');

const buf = [];

for (const fn of ['aeon.yml', 'skills.json']) {
  const data = fs.readFileSync(fn);
  const digest = crypto.createHash('sha1').update(data).digest('hex');
  buf.push(`${digest}  ${fn}`);
}

const skillDirs = fs.readdirSync('skills').filter(d => {
  return fs.statSync(path.join('skills', d)).isDirectory();
}).sort();

const skillFiles = skillDirs
  .map(d => `skills/${d}/SKILL.md`)
  .filter(p => fs.existsSync(p));

const memRe = /memory\/(?:topics|state)\/[a-zA-Z0-9_.-]+/g;

for (const f of skillFiles) {
  const text = fs.readFileSync(f, 'utf8');
  const lines = text.split('\n');
  let n = 0;
  for (const line of lines) {
    if (line === '---') { n++; continue; }
    if (n === 1) buf.push(`${f}: ${line}`);
  }
  // emulate grep -hE '^depends_on:|^- skill:|consume:|parallel:|trigger:'
  // grep BRE/ERE alternation: each alternative is matched independently — first 2 are anchored, rest unanchored
  for (const line of lines) {
    if (
      /^depends_on:/.test(line) ||
      /^- skill:/.test(line) ||
      /consume:/.test(line) ||
      /parallel:/.test(line) ||
      /trigger:/.test(line)
    ) {
      buf.push(line);
    }
  }
  // grep -hoE 'memory/(topics|state)/...' | sort -u
  const found = new Set();
  let m;
  memRe.lastIndex = 0;
  while ((m = memRe.exec(text)) !== null) found.add(m[0]);
  for (const r of [...found].sort()) buf.push(r);
}

const innerInput = buf.join('\n') + '\n';
const innerSha = crypto.createHash('sha1').update(innerInput).digest('hex');
console.log(`${innerSha}  -`);
