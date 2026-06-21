const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

// fp.js version
function v1() {
  const buf = [];
  for (const fn of ['aeon.yml', 'skills.json']) {
    const data = fs.readFileSync(fn);
    buf.push(`${crypto.createHash('sha1').update(data).digest('hex')}  ${fn}`);
  }
  const skillDirs = fs.readdirSync('skills').filter(d => fs.statSync(`skills/${d}`).isDirectory()).sort();
  const skillFiles = skillDirs.map(d => `skills/${d}/SKILL.md`).filter(p => fs.existsSync(p));
  for (const f of skillFiles) {
    const text = fs.readFileSync(f, 'utf8');
    const lines = text.split('\n');
    let n = 0;
    for (const line of lines) {
      if (line === '---') { n++; continue; }
      if (n === 1) buf.push(`${f}: ${line}`);
    }
    for (const line of lines) {
      if (/^depends_on:/.test(line) || /^- skill:/.test(line) ||
          /consume:/.test(line) || /parallel:/.test(line) || /trigger:/.test(line)) buf.push(line);
    }
    const found = new Set();
    const memRe = /memory\/(?:topics|state)\/[a-zA-Z0-9_.-]+/g;
    let m;
    while ((m = memRe.exec(text)) !== null) found.add(m[0]);
    for (const r of [...found].sort()) buf.push(r);
  }
  return buf;
}

// generate.js version
function v2() {
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

const b1 = v1();
const b2 = v2();
console.log('b1 len', b1.length, 'b2 len', b2.length);
let diffs = 0;
const max = Math.max(b1.length, b2.length);
for (let i = 0; i < max; i++) {
  if (b1[i] !== b2[i]) {
    console.log(`diff @ ${i}:\n  v1: ${JSON.stringify(b1[i])}\n  v2: ${JSON.stringify(b2[i])}`);
    if (++diffs > 10) break;
  }
}
console.log('diffs', diffs);
console.log('v1 sha:', crypto.createHash('sha1').update(b1.join('\n') + '\n').digest('hex'));
console.log('v2 sha:', crypto.createHash('sha1').update(b2.join('\n') + '\n').digest('hex'));
console.log('v2-raw sha (no trailing newline):', crypto.createHash('sha1').update(b2.join('\n')).digest('hex'));

