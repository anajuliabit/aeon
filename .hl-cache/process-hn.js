const fs = require('fs');
const front = JSON.parse(fs.readFileSync('.hl-cache/hn-frontpage.json', 'utf8'));
const hits = front.hits || [];
const now = Math.floor(Date.now() / 1000);
const scored = hits.map(h => {
  const age_h = (now - h.created_at_i) / 3600;
  const pts = h.points || 0;
  const cmts = h.num_comments || 0;
  const ageP = Math.max(0, age_h - 12) * 2;
  return {
    id: h.objectID,
    title: h.title,
    url: h.url || `https://news.ycombinator.com/item?id=${h.objectID}`,
    points: pts,
    comments: cmts,
    age_h: age_h.toFixed(1),
    score: pts + 1.5 * cmts - ageP,
    author: h.author,
  };
});
scored.sort((a,b) => b.score - a.score);
console.log(JSON.stringify(scored.slice(0, 15), null, 2));
