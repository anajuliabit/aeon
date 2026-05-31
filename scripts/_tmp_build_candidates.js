#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const DATANET = "9";
const LEDGER = new Set([
  "8d47851b7762a319","da7a36f4094a24f9","3abb43986aea32fd",
  "397ee2e8e5e7e593","9794ed8044e6e7ea","7029a48db1b4e5db",
  "086b715f7a1de343","0d4b168331d58f61","e02fef4e76668a31",
  "a3ea5a0973858464","06e7715d81cdedca","956a3b01c98e6730",
  "dce17be300855e07",
]);

const files = fs.readdirSync(".hl-cache")
  .filter(f => f.startsWith("user-fills-") && f.endsWith(".json"))
  .sort()
  .map(f => path.join(".hl-cache", f));

const results = [];
for (const fp of files) {
  const addr = path.basename(fp).replace("user-fills-", "").replace(".json", "");
  let data;
  try { data = JSON.parse(fs.readFileSync(fp, "utf8")); } catch (e) { results.push({addr, status: "INVALID"}); continue; }
  if (data && data.code === "PREFETCH_FAILED") { results.push({addr, status: "ERROR"}); continue; }
  if (!Array.isArray(data) || data.length === 0) { results.push({addr, status: "EMPTY", n_fills: 0}); continue; }

  const n_total = data.length;
  const n_spot = data.filter(x => ["Buy","Sell","Spot Dust Conversion"].includes(x.dir) || (x.coin || "").startsWith("@")).length;
  const spot_pct = n_spot / n_total;
  const perp_fills = data.filter(x => x.dir && (x.dir.includes("Open") || x.dir.includes("Close")));
  const close_fills = perp_fills.filter(x => x.dir.includes("Close"));
  const n_perp = perp_fills.length;
  const n_close = close_fills.length;
  if (n_close === 0) {
    const has_perp = perp_fills.length > 0;
    results.push({addr, status: has_perp ? "NO_CLOSE" : "NO_PERP_CLOSE", n_fills: n_total, n_perp, spot_pct: +spot_pct.toFixed(4)});
    continue;
  }

  const pnls = close_fills.map(x => parseFloat(x.closedPnl || "0") || 0);
  const sum_pnl = pnls.reduce((a,b) => a+b, 0);
  const wins = pnls.filter(p => p > 0).length;
  const win_rate = wins / pnls.length;

  const rets = [];
  for (const x of close_fills) {
    const sz = parseFloat(x.sz || "0") || 0;
    const px = parseFloat(x.px || "0") || 0;
    const pnl = parseFloat(x.closedPnl || "0") || 0;
    const notional = sz * px;
    if (notional > 0) rets.push(pnl / notional);
  }
  const first_t = data[0].time;
  const last_t = data[data.length - 1].time;
  const span_ms = last_t - first_t;
  const days_covered = Math.max(span_ms / 86400000, 1/86400);
  let sharpe = 0;
  if (rets.length > 0) {
    const mean = rets.reduce((a,b)=>a+b,0) / rets.length;
    const variance = rets.reduce((a,b)=>a+(b-mean)*(b-mean),0) / rets.length;
    const std = Math.sqrt(variance);
    const annual_factor = Math.sqrt(rets.length * 365 / days_covered);
    sharpe = std > 0 ? (mean / std * annual_factor) : 0;
  }
  let cum = 0, peak = 0, mdd = 0;
  for (const p of pnls) {
    cum += p;
    if (cum > peak) peak = cum;
    const dd = peak - cum;
    if (dd > mdd) mdd = dd;
  }
  const mdd_pct = peak > 0 ? (mdd / peak * 100) : (sum_pnl < 0 ? 100 : 0);

  const canonical = `trades:${DATANET}:${addr}:${first_t}:${last_t}:${n_close}`;
  const full_hash = crypto.createHash("sha256").update(canonical).digest("hex");
  const short_hash = full_hash.slice(0, 16);
  const dedup = LEDGER.has(short_hash);
  const markets = [...new Set(close_fills.map(x => x.coin))].sort();

  results.push({
    addr,
    status: dedup ? "DEDUP" : (spot_pct > 0.05 ? "SPOT_MIX" : "CAND"),
    n_fills: n_total,
    n_perp,
    n_close,
    spot_pct: +spot_pct.toFixed(4),
    first_t, last_t,
    days_covered: +days_covered.toFixed(4),
    win_rate: +win_rate.toFixed(4),
    sum_pnl: +sum_pnl.toFixed(2),
    sharpe: +sharpe.toFixed(2),
    mdd_pct: +mdd_pct.toFixed(2),
    mdd_usd: +mdd.toFixed(2),
    canonical, short_hash, full_hash, markets,
  });
}

const ORD = { CAND:0, SPOT_MIX:1, DEDUP:2, NO_CLOSE:3, NO_PERP_CLOSE:4, EMPTY:5, ERROR:6, INVALID:7 };
results.sort((a,b) => (ORD[a.status]||99) - (ORD[b.status]||99) || ((b.sharpe||0) - (a.sharpe||0)));
for (const r of results) {
  if (r.status === "EMPTY" || r.status === "ERROR" || r.status === "INVALID") {
    console.log(`${r.status.padEnd(14)} ${r.addr}`);
  } else if (r.status.startsWith("NO_")) {
    console.log(`${r.status.padEnd(14)} ${r.addr} fills=${r.n_fills} perp=${r.n_perp||0} spot%=${((r.spot_pct||0)*100).toFixed(1)}`);
  } else {
    console.log(`${r.status.padEnd(14)} ${r.addr} fills=${r.n_fills} close=${r.n_close} sharpe=${r.sharpe} pnl=$${r.sum_pnl.toFixed(2)} win=${(r.win_rate*100).toFixed(1)}% mdd_pct=${r.mdd_pct.toFixed(2)}% spot%=${(r.spot_pct*100).toFixed(1)} hash=${r.short_hash} days=${r.days_covered} mkts=${r.markets.slice(0,6).join(",")}`);
  }
}
fs.writeFileSync(".tmp-candidates.json", JSON.stringify(results, null, 2));
