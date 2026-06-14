const fs = require('fs');
const buf = fs.readFileSync('docs/skill-graph.md');
const text = buf.toString('utf8');
const lines = text.split('\n');
console.log('total lines:', lines.length);
console.log('line 157:', JSON.stringify(lines[156]));
console.log('contains class enabled?', text.indexOf('class aixbt-pulse enabled'));
const idx = text.indexOf('class aixbt');
console.log('idx of class aixbt:', idx);
if (idx >= 0) {
  console.log('around:', JSON.stringify(text.slice(idx - 10, idx + 50)));
}
