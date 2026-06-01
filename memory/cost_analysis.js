const fs = require('fs');

// Pricing (per million tokens)
const PRICING = {
  "claude-opus-4-7":           { input: 15.00, output: 75.00, cache_read:  1.50, cache_write: 18.75 },
  "claude-sonnet-4-6":         { input:  3.00, output: 15.00, cache_read:  0.30, cache_write:  3.75 },
  "claude-haiku-4-5-20251001": { input:  0.80, output:  4.00, cache_read:  0.08, cache_write:  1.00 },
};

const WINDOW_START = new Date("2026-05-25");
const WINDOW_END   = new Date("2026-05-31");

function parseDate(s) { return new Date(s); }
function inWindow(d)  { return d >= WINDOW_START && d <= WINDOW_END; }

function rowCost(r) {
  const p = PRICING[r.model];
  return (
    r.input_tokens   / 1e6 * p.input  +
    r.output_tokens  / 1e6 * p.output +
    r.cache_read     / 1e6 * p.cache_read +
    r.cache_creation / 1e6 * p.cache_write
  );
}
function rowCostBreakdown(r) {
  const p = PRICING[r.model];
  return {
    ic:  r.input_tokens   / 1e6 * p.input,
    oc:  r.output_tokens  / 1e6 * p.output,
    rrc: r.cache_read     / 1e6 * p.cache_read,
    wrc: r.cache_creation / 1e6 * p.cache_write,
  };
}

// Parse CSV
const lines = fs.readFileSync('/home/runner/work/aeon/aeon/memory/token-usage.csv', 'utf8').trim().split('\n');
const headers = lines[0].split(',');
const allRows = lines.slice(1).map(line => {
  const parts = line.split(',');
  const r = {};
  headers.forEach((h, i) => r[h.trim()] = parts[i] ? parts[i].trim() : '');
  r.input_tokens   = parseInt(r.input_tokens);
  r.output_tokens  = parseInt(r.output_tokens);
  r.cache_read     = parseInt(r.cache_read);
  r.cache_creation = parseInt(r.cache_creation);
  r._date = parseDate(r.date);
  r._cost = rowCost(r);
  return r;
});

const windowRows = allRows.filter(r => inWindow(r._date));

const f4 = n => n.toFixed(4);

// ─── 1. In-window row count ────────────────────────────────────────────────
console.log("=".repeat(70));
console.log("1. IN-WINDOW ROW COUNT");
console.log("=".repeat(70));
console.log(`   In-window rows: ${windowRows.length}`);

// ─── 2. Total cost breakdown ───────────────────────────────────────────────
let total_ic=0, total_oc=0, total_rrc=0, total_wrc=0;
for (const r of windowRows) {
  const b = rowCostBreakdown(r);
  total_ic  += b.ic;
  total_oc  += b.oc;
  total_rrc += b.rrc;
  total_wrc += b.wrc;
}
const totalCost = total_ic + total_oc + total_rrc + total_wrc;

console.log("\n" + "=".repeat(70));
console.log("2. TOTAL COST BREAKDOWN (in-window)");
console.log("=".repeat(70));
console.log(`   input_cost:       $${f4(total_ic)}`);
console.log(`   output_cost:      $${f4(total_oc)}`);
console.log(`   cache_read_cost:  $${f4(total_rrc)}`);
console.log(`   cache_write_cost: $${f4(total_wrc)}`);
console.log(`   TOTAL:            $${f4(totalCost)}`);

// ─── 3. Total runs ─────────────────────────────────────────────────────────
console.log("\n" + "=".repeat(70));
console.log("3. TOTAL RUNS (in-window row count)");
console.log("=".repeat(70));
console.log(`   Total runs: ${windowRows.length}`);

// ─── 4. Per-skill aggregates ───────────────────────────────────────────────
const skillMap = {};
for (const r of windowRows) {
  if (!skillMap[r.skill]) skillMap[r.skill] = { runs: 0, total_tokens: 0, total_cost: 0 };
  const d = skillMap[r.skill];
  d.runs++;
  d.total_tokens += r.input_tokens + r.output_tokens + r.cache_read + r.cache_creation;
  d.total_cost   += r._cost;
}

console.log("\n" + "=".repeat(70));
console.log("4. PER-SKILL AGGREGATES (sorted by total cost desc)");
console.log("=".repeat(70));
console.log("Skill                          Runs  Total Tokens   Total Cost    Avg/Run");
console.log("-".repeat(75));
const sortedSkills = Object.entries(skillMap).sort((a,b) => b[1].total_cost - a[1].total_cost);
for (const [sk, d] of sortedSkills) {
  const avg = d.total_cost / d.runs;
  console.log(`${sk.padEnd(30)} ${String(d.runs).padStart(5)}  ${String(d.total_tokens.toLocaleString()).padStart(13)}  $${f4(d.total_cost).padStart(10)}  $${f4(avg).padStart(9)}`);
}

// ─── 5. Per-model aggregates ───────────────────────────────────────────────
const modelMap = {};
for (const r of windowRows) {
  if (!modelMap[r.model]) modelMap[r.model] = { runs: 0, total_tokens: 0, total_cost: 0 };
  const d = modelMap[r.model];
  d.runs++;
  d.total_tokens += r.input_tokens + r.output_tokens + r.cache_read + r.cache_creation;
  d.total_cost   += r._cost;
}

console.log("\n" + "=".repeat(70));
console.log("5. PER-MODEL AGGREGATES (in-window)");
console.log("=".repeat(70));
console.log("Model                               Runs  Total Tokens   Total Cost");
console.log("-".repeat(70));
for (const [m, d] of Object.entries(modelMap).sort((a,b) => b[1].total_cost - a[1].total_cost)) {
  console.log(`${m.padEnd(35)} ${String(d.runs).padStart(5)}  ${String(d.total_tokens.toLocaleString()).padStart(13)}  $${f4(d.total_cost).padStart(10)}`);
}

// ─── 6. Daily avg and projected monthly ───────────────────────────────────
const dailyAvg   = totalCost / 7;
const monthlyProj = dailyAvg * 30;

console.log("\n" + "=".repeat(70));
console.log("6. DAILY AVG AND PROJECTED MONTHLY");
console.log("=".repeat(70));
console.log(`   Daily avg (total / 7):    $${f4(dailyAvg)}`);
console.log(`   Projected monthly (* 30): $${f4(monthlyProj)}`);

// ─── 7. Date range overall ─────────────────────────────────────────────────
const allDates = allRows.map(r => r._date);
const minDate  = new Date(Math.min(...allDates));
const maxDate  = new Date(Math.max(...allDates));
const totalDays = Math.round((maxDate - minDate) / 86400000) + 1;

console.log("\n" + "=".repeat(70));
console.log("7. DATE RANGE IN CSV");
console.log("=".repeat(70));
console.log(`   Min date:   ${minDate.toISOString().slice(0,10)}`);
console.log(`   Max date:   ${maxDate.toISOString().slice(0,10)}`);
console.log(`   Total days: ${totalDays}`);

// ─── 8. Anomaly detection ─────────────────────────────────────────────────
const smMap = {};
for (const r of windowRows) {
  const key = `${r.skill}|||${r.model}`;
  if (!smMap[key]) smMap[key] = [];
  smMap[key].push(r);
}

console.log("\n" + "=".repeat(70));
console.log("8. ANOMALY DETECTION (>=3 runs, cost > mean+2*sigma AND cost > $0.10)");
console.log("=".repeat(70));
let anomaliesFound = false;
for (const [key, entries] of Object.entries(smMap).sort()) {
  if (entries.length < 3) continue;
  const costs = entries.map(e => e._cost);
  const mean = costs.reduce((a,b) => a+b, 0) / costs.length;
  const variance = costs.reduce((a,b) => a + (b-mean)**2, 0) / costs.length;
  const sigma = Math.sqrt(variance);
  const threshold = mean + 2 * sigma;
  for (const r of entries) {
    if (r._cost > threshold && r._cost > 0.10) {
      anomaliesFound = true;
      const [sk, mo] = key.split("|||");
      console.log(`  ANOMALY: skill=${sk}, model=${mo}`);
      console.log(`    date=${r.date}, run_cost=$${f4(r._cost)}, mean=$${f4(mean)}, sigma=$${f4(sigma)}`);
      console.log(`    input_tokens=${r.input_tokens}, output_tokens=${r.output_tokens}, cache_creation=${r.cache_creation}`);
    }
  }
}
if (!anomaliesFound) console.log("  No anomalies detected.");

// ─── 9. Model downgrade candidates ────────────────────────────────────────
const opusSkill = {};
for (const r of windowRows) {
  if (r.model !== "claude-opus-4-7") continue;
  if (!opusSkill[r.skill]) opusSkill[r.skill] = [];
  opusSkill[r.skill].push(r);
}

function median(arr) {
  const s = [...arr].sort((a,b) => a-b);
  const n = s.length;
  return n % 2 ? s[Math.floor(n/2)] : (s[n/2-1] + s[n/2]) / 2;
}

console.log("\n" + "=".repeat(70));
console.log("9. MODEL DOWNGRADE CANDIDATES (opus, median ratio<0.3, avg cost>$0.25)");
console.log("=".repeat(70));
let candidatesFound = false;
const opusStats = {};
for (const [sk, rows] of Object.entries(opusSkill)) {
  const ratios = rows.map(r => r.output_tokens / Math.max(r.input_tokens, 1));
  const medRatio = median(ratios);
  const avgCost  = rows.reduce((a,r) => a + r._cost, 0) / rows.length;
  opusStats[sk] = { medRatio, avgCost, runs: rows.length };
  if (medRatio < 0.3 && avgCost > 0.25) {
    candidatesFound = true;
    console.log(`  skill=${sk}, median_ratio=${medRatio.toFixed(4)}, avg_cost/run=$${f4(avgCost)}, runs=${rows.length}`);
  }
}
if (!candidatesFound) console.log("  No downgrade candidates found.");

console.log("\n  (All opus skills -- median output/input ratio and avg cost/run:)");
console.log(`  ${"Skill".padEnd(30)} ${"Runs".padStart(5)} ${"MedianRatio".padStart(12)} ${"AvgCost".padStart(10)}`);
console.log("  " + "-".repeat(62));
for (const [sk, d] of Object.entries(opusStats).sort((a,b) => b[1].avgCost - a[1].avgCost)) {
  console.log(`  ${sk.padEnd(30)} ${String(d.runs).padStart(5)} ${d.medRatio.toFixed(4).padStart(12)} $${f4(d.avgCost).padStart(9)}`);
}

// ─── 10. Cache underuse candidates ────────────────────────────────────────
const cacheSkill = {};
for (const r of windowRows) {
  if (!cacheSkill[r.skill]) cacheSkill[r.skill] = { cache_read: 0, input_tokens: 0, total_cost: 0, runs: 0 };
  const d = cacheSkill[r.skill];
  d.cache_read    += r.cache_read;
  d.input_tokens  += r.input_tokens;
  d.total_cost    += r._cost;
  d.runs++;
}

console.log("\n" + "=".repeat(70));
console.log("10. CACHE UNDERUSE CANDIDATES (cache_ratio<0.2 AND avg cost/run>$0.10)");
console.log("=".repeat(70));
console.log(`  ${"Skill".padEnd(30)} ${"CacheRatio".padStart(11)} ${"AvgCost/Run".padStart(12)} ${"Runs".padStart(5)}`);
console.log("  " + "-".repeat(63));
let underuseFound = false;
const cacheStats = Object.entries(cacheSkill).map(([sk, d]) => {
  const denom = d.cache_read + d.input_tokens;
  const ratio = denom > 0 ? d.cache_read / denom : 0;
  const avgCost = d.total_cost / d.runs;
  return { sk, ratio, avgCost, runs: d.runs };
}).sort((a,b) => b.avgCost - a.avgCost);

for (const e of cacheStats) {
  if (e.ratio < 0.2 && e.avgCost > 0.10) {
    underuseFound = true;
    console.log(`  ${e.sk.padEnd(30)} ${e.ratio.toFixed(4).padStart(11)} $${f4(e.avgCost).padStart(11)} ${String(e.runs).padStart(5)}`);
  }
}
if (!underuseFound) console.log("  No cache underuse candidates found.");

console.log("\n  (All skills -- cache ratio and avg cost for full picture:)");
console.log(`  ${"Skill".padEnd(30)} ${"CacheRatio".padStart(11)} ${"AvgCost/Run".padStart(12)} ${"Runs".padStart(5)}  Flag`);
console.log("  " + "-".repeat(70));
const cacheStatsSorted = [...cacheStats].sort((a,b) => a.ratio - b.ratio);
for (const e of cacheStatsSorted) {
  const flag = (e.ratio < 0.2 && e.avgCost > 0.10) ? " << UNDERUSE" : "";
  console.log(`  ${e.sk.padEnd(30)} ${e.ratio.toFixed(4).padStart(11)} $${f4(e.avgCost).padStart(11)} ${String(e.runs).padStart(5)}${flag}`);
}

console.log("\n" + "=".repeat(70));
console.log("DONE");
console.log("=".repeat(70));
