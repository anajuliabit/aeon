#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const ROOT = '/home/runner/work/aeon/aeon';
process.chdir(ROOT);

const dirs = fs.readdirSync('skills', { withFileTypes: true }).filter(d => d.isDirectory()).map(d => d.name).sort();

const refMap = {};
const pipelineCandidates = [];

for (const slug of dirs) {
  const f = path.join('skills', slug, 'SKILL.md');
  if (!fs.existsSync(f)) continue;
  const c = fs.readFileSync(f, 'utf8');
  const lns = c.split('\n');

  // Pipeline detection criteria
  const articleHits = [];
  for (let i = 0; i < lns.length; i++) {
    if (/articles\/[^\s"'`]+\.md/.test(lns[i]) && /(write|save|append|>\s*articles|writeFileSync|create)\b/i.test(lns[i])) {
      articleHits.push(lns[i].trim().slice(0, 100));
    }
  }
  if (articleHits.length) pipelineCandidates.push({ slug, hits: articleHits });

  // memory ref classification - tighter
  for (let i = 0; i < lns.length; i++) {
    const mRe = /memory\/(topics|state)\/[a-zA-Z0-9_.-]+/g;
    let m;
    while ((m = mRe.exec(lns[i])) !== null) {
      const ctx = lns.slice(Math.max(0, i-1), Math.min(lns.length, i+2)).join(' ');
      // Tighter write detection: explicit write verb near the path
      const isWrite = new RegExp('(write|writeFileSync|append|save|update|>\\s*memory)[^.]{0,40}' + m[0].replace(/[.]/g, '\\.'), 'i').test(ctx);
      const pth = m[0];
      if (!refMap[pth]) refMap[pth] = { writers: new Set(), readers: new Set() };
      if (isWrite) refMap[pth].writers.add(slug);
      else refMap[pth].readers.add(slug);
    }
  }
}

console.log('=== Pipeline candidates (article producers) ===');
for (const p of pipelineCandidates) {
  console.log(p.slug);
  for (const h of p.hits.slice(0, 2)) console.log('  ', h);
}

console.log('');
console.log('=== Topics/state with both writers and readers ===');
for (const [pth, {writers, readers}] of Object.entries(refMap)) {
  const w = [...writers]; const r = [...readers];
  if (w.length && r.length) {
    console.log(pth, '→ writers:', w.join(','), '| readers:', r.slice(0, 6).join(','), r.length > 6 ? `(+${r.length-6})` : '');
  }
}
