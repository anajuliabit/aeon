const fs = require('fs');
const prev = fs.readFileSync('docs/skill-graph.md', 'utf8');
const nodes = new Set();
for (const m of prev.matchAll(/^\s*click\s+([a-z0-9-]+)\s+"/gm)) nodes.add(m[1]);

const skillDirs = fs.readdirSync('skills').filter(d => fs.statSync(`skills/${d}`).isDirectory()).sort();
const newNodes = new Set(skillDirs);

console.log('removed:', [...nodes].filter(x => !newNodes.has(x)));
console.log('added:', [...newNodes].filter(x => !nodes.has(x)));
