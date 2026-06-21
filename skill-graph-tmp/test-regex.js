const fs = require('fs');
const raw = fs.readFileSync('aeon.yml', 'utf8');

// flatten
const lines = raw.split('\n');
const flat = [];
let i = 0;
while (i < lines.length) {
  const line = lines[i];
  const m = line.match(/^(\s*)([a-z0-9-]+):\s*$/);
  if (m && i + 1 < lines.length && lines[i+1].trim() === '{') {
    let j = i + 1;
    const body = [];
    while (j < lines.length && lines[j].trim() !== '}') {
      body.push(lines[j].trim().replace(/,$/, ''));
      j++;
    }
    const inner = body.slice(1).filter(Boolean).join(', ');
    flat.push(`${m[1]}${m[2]}: { ${inner} }`);
    i = j + 1;
    continue;
  }
  flat.push(line);
  i++;
}
const flattened = flat.join('\n');
fs.writeFileSync('skill-graph-tmp/flat.yml', flattened);

const skillsStart = flattened.indexOf('\nskills:');
console.log('skills start:', skillsStart);

let skillsBlock = flattened;
if (skillsStart >= 0) {
  const after = flattened.slice(skillsStart + 1);
  const nextTop = after.match(/\n([a-z][a-z_-]*):/m);
  console.log('nextTop:', nextTop && nextTop[1], 'at:', nextTop && nextTop.index);
  if (nextTop) {
    const end = skillsStart + 1 + nextTop.index;
    skillsBlock = flattened.slice(skillsStart, end);
  } else {
    skillsBlock = flattened.slice(skillsStart);
  }
}

const skillRe = /^\s\s([a-z0-9-]+):\s*\{\s*([^}]*)\s*\}/gm;
const skills = [];
let m;
while ((m = skillRe.exec(skillsBlock)) !== null) {
  const enabled = /enabled:\s*true/.test(m[2]);
  skills.push({ slug: m[1], enabled });
}
console.log('total:', skills.length, 'enabled:', skills.filter(s => s.enabled).length);
console.log('enabled list:', skills.filter(s => s.enabled).map(s => s.slug).slice(0,10));
