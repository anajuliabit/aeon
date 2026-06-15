const ev = require("./tp-poly-events.json");
const rows = [];
for (const e of ev) {
  const markets = e.markets || [];
  for (const m of markets) {
    if (m.closed) continue;
    let prices = [];
    try { prices = JSON.parse(m.outcomePrices || "[]"); } catch {}
    const yes = prices.length ? parseFloat(prices[0]) : null;
    rows.push({ q: m.question || e.title, yes, v24: m.volume24hr || 0, end: m.endDate || e.endDate, etitle: e.title });
  }
}
const seen = new Set();
const uniq = rows.filter(r => { if (seen.has(r.q)) return false; seen.add(r.q); return true; });
// non-worldcup, yes between 8 and 92, vol>=50k
console.log("=== NON-WorldCup markets, YES 8-92¢, 24h vol>=50k ===");
uniq.filter(r => r.v24 >= 50000 && r.yes != null && r.yes > 0.08 && r.yes < 0.92 && !/world cup|fifa/i.test(r.etitle))
  .sort((a,b)=>b.v24-a.v24).slice(0,30)
  .forEach(r => console.log("$"+(r.v24/1000).toFixed(0)+"k | YES "+(r.yes*100).toFixed(1)+"¢ | ends "+(r.end||"").slice(0,10)+" | "+(r.q||"").slice(0,80)));
console.log("\n=== WorldCup favorites, YES>8¢ ===");
uniq.filter(r => r.v24 >= 50000 && r.yes != null && r.yes > 0.08 && /world cup|fifa/i.test(r.etitle))
  .sort((a,b)=>b.yes-a.yes).slice(0,15)
  .forEach(r => console.log("$"+(r.v24/1000).toFixed(0)+"k | YES "+(r.yes*100).toFixed(1)+"¢ | "+(r.q||"").slice(0,70)));
