const fs = require('fs');
const crypto = require('crypto');
const path = require('path');

function compute() {
  const buf = [];
  for (const fn of ['aeon.yml', 'skills.json']) {
    buf.push(`${crypto.createHash('sha1').update(fs.readFileSync(fn)).digest('hex')}  ${fn}`);
  }
  const skillFiles = fs.readdirSync('skills')
    .filter(d => fs.statSync(path.join('skills', d)).isDirectory())
    .sort()
    .map(d => `skills/${d}/SKILL.md`)
    .filter(p => fs.existsSync(p));
  for (const f of skillFiles) {
    const text = fs.readFileSync(f, 'utf8');
    let n = 0;
    for (const line of text.split('\n')) {
      if (line === '---') { n++; continue; }
      if (n === 1) buf.push(`${f}: ${line}`);
    }
    for (const line of text.split('\n')) {
      if (/^depends_on:/.test(line) || /^- skill:/.test(line) ||
          /consume:/.test(line) || /parallel:/.test(line) || /trigger:/.test(line)) buf.push(line);
    }
    const refs = new Set();
    for (const m of text.matchAll(/memory\/(?:topics|state)\/[a-zA-Z0-9_.-]+/g)) refs.add(m[0]);
    [...refs].sort().forEach(r => buf.push(r));
  }
  return buf;
}

const buf = compute();
fs.writeFileSync('skill-graph-tmp/dump.txt', buf.join('\n') + '\n');
console.log('sha:', crypto.createHash('sha1').update(buf.join('\n') + '\n').digest('hex'));
