const fs = require('fs');
const prev = fs.readFileSync('docs/skill-graph.md', 'utf8');
const nodes = new Set();
const edges = new Set();
for (const m of prev.matchAll(/^\s*click\s+([a-z0-9-]+)\s+"/gm)) nodes.add(m[1]);
for (const m of prev.matchAll(/^\s*([a-z0-9-]+)\s+(-+\.{0,2}-*>|-->|-\.->|-\.\.->)\s+([a-z0-9-]+)\b/gm)) {
  edges.add(`${m[1]}->${m[3]}`);
}
console.log('nodes containing health/evals/repair/improve/state:');
for (const n of nodes) if (/(health|evals|repair|improve|state)/.test(n)) console.log(' ', n);
console.log('edges containing health/evals/repair/improve/state:');
let ct = 0;
for (const e of edges) if (/(health|evals|repair|improve|state)/.test(e)) { console.log(' ', e); ct++; if (ct>30) break; }
console.log('total nodes', nodes.size, 'total edges', edges.size);
