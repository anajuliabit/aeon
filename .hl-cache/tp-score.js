const m = require("./tp-markets.json");
const t = require("./tp-trending.json");
const dex = require("./tp-dex.json");

const byId = {};
m.forEach(c => byId[c.id] = c);
const btc = byId["bitcoin"], eth = byId["ethereum"];
const btc7 = btc.price_change_percentage_7d_in_currency;
const eth7 = eth.price_change_percentage_7d_in_currency;
console.log("BENCHMARK BTC 24h", btc.price_change_percentage_24h_in_currency?.toFixed(2), "7d", btc7?.toFixed(2));
console.log("BENCHMARK ETH 24h", eth.price_change_percentage_24h_in_currency?.toFixed(2), "7d", eth7?.toFixed(2));

// trending set
const trendIds = new Set(t.coins.map(x => x.item.id));
console.log("\nTRENDING:");
t.coins.forEach(x => {
  const i = x.item;
  const ch = i.data && i.data.price_change_percentage_24h && i.data.price_change_percentage_24h.usd;
  console.log(" ", i.symbol, "| id:", i.id, "| rank:", i.market_cap_rank, "| 24h%:", ch != null ? ch.toFixed(1) : "?");
});

// dex symbols for cross-confirm
const dexSyms = new Set();
if (dex.pairs) dex.pairs.forEach(p => { if (p.baseToken && p.baseToken.symbol) dexSyms.add(p.baseToken.symbol.toUpperCase()); });

const dedup = new Set(["WLD","SENT","MORPHO","MON","TAO","XPL"]);

const scored = [];
for (const c of m) {
  const mc = c.market_cap || 0;
  if (mc < 20e6) continue;
  const p24 = c.price_change_percentage_24h_in_currency;
  const p7 = c.price_change_percentage_7d_in_currency;
  const vol = c.total_volume || 0;
  const vmc = mc > 0 ? vol / mc : 0;
  let s = 0;
  const br = [];
  if (p24 > 0) { s += 1; br.push("24h+"); }
  if (p7 > 0) { s += 1; br.push("7d+"); }
  if (p24 > 5 && p7 > 5) { s += 2; br.push("both>5%+2"); }
  if (trendIds.has(c.id)) { s += 2; br.push("trending+2"); }
  if (vmc >= 0.20) { s += 3; br.push("vmc>=.20+3"); }
  else if (vmc >= 0.10) { s += 2; br.push("vmc>=.10+2"); }
  if (p7 > btc7 && p7 > eth7) { s += 2; br.push("RSvsBTC/ETH+2"); }
  const sym = (c.symbol || "").toUpperCase();
  if (dexSyms.has(sym)) { s += 1; br.push("dex+1"); }
  scored.push({ sym, id: c.id, rank: c.market_cap_rank, price: c.current_price, mc, vol, vmc, p24, p7, s, br: br.join(","), dd: dedup.has(sym) });
}
scored.sort((a,b) => b.s - a.s);
console.log("\nTOP 25 SCORED (excl mc<20M):");
scored.slice(0,25).forEach(c => {
  console.log(
    (c.dd ? "[DEDUP] " : "        ") +
    c.sym.padEnd(8), "s=" + c.s, "| $" + (c.price < 1 ? c.price.toPrecision(4) : c.price.toFixed(2)),
    "| 24h", (c.p24||0).toFixed(1) + "%", "7d", (c.p7||0).toFixed(1) + "%",
    "| mc $" + (c.mc/1e6).toFixed(0) + "M", "vmc", c.vmc.toFixed(2),
    "| rk" + c.rank, "|", c.br
  );
});
