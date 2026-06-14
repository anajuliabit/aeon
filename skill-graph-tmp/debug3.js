const fs = require('fs');
const prev = fs.readFileSync('docs/skill-graph.md', 'utf8');
const priorEnabled = new Set();
for (const m of prev.matchAll(/^\s*class\s+([a-z0-9_-]+)\s+enabled\b/gm)) {
  priorEnabled.add(m[1]);
}
console.log('count:', priorEnabled.size);
console.log([...priorEnabled].slice(0,20));
