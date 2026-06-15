const ev = require("./tp-poly-events.json");
const dedup = ["knicks","nba finals","xi jinping","iran","enrich"];
const rows = [];
for (const e of ev) {
  const v24 = e.volume24hr || 0;
  const markets = e.markets || [];
  for (const m of markets) {
    if (m.closed) continue;
    let prices = [];
    try { prices = JSON.parse(m.outcomePrices || "[]"); } catch {}
    const yes = prices.length ? parseFloat(prices[0]) : null;
    rows.push({
      q: m.question || e.title,
      yes,
      v24: m.volume24hr || v24,
      vtot: m.volumeNum || e.volume || 0,
      end: m.endDate || e.endDate,
    });
  }
}
// dedupe by question, sort by 24h vol
const seen = new Set();
const uniq = rows.filter(r => { if (seen.has(r.q)) return false; seen.add(r.q); return true; });
uniq.sort((a,b) => b.v24 - a.v24);
console.log("TOP 20 MARKETS by 24h vol (vol>=50k gate):");
uniq.slice(0,20).forEach(r => {
  const dd = dedup.some(d => (r.q||"").toLowerCase().includes(d));
  console.log(
    (dd ? "[DEDUP] " : "        ") +
    "$" + (r.v24/1000).toFixed(0) + "k 24h |",
    "YES", r.yes != null ? (r.yes*100).toFixed(1) + "¢" : "?",
    "| ends", (r.end||"").slice(0,10),
    "|", (r.q||"").slice(0,75)
  );
});
