const fs = require('fs');
const papers = JSON.parse(fs.readFileSync('.hl-cache/hf-papers.json', 'utf8'));
const out = papers.map(p => ({
  id: p.paper?.id,
  title: p.paper?.title,
  upvotes: p.paper?.upvotes,
  authors: (p.paper?.authors || []).slice(0, 3).map(a => a.name).join(', '),
  summary: (p.paper?.summary || p.paper?.ai_summary || '').slice(0, 400).replace(/\s+/g, ' '),
  publishedAt: p.paper?.publishedAt,
}));
// sort by upvotes
out.sort((a,b) => (b.upvotes||0) - (a.upvotes||0));
console.log(JSON.stringify(out.slice(0, 12), null, 2));
