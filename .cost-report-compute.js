const fs = require('fs');

const PRICING = {
  'claude-opus-4-7':           { input: 15.00, output: 75.00, cache_read: 1.50,  cache_write: 18.75 },
  'claude-sonnet-4-6':         { input:  3.00, output: 15.00, cache_read: 0.30,  cache_write:  3.75 },
  'claude-haiku-4-5-20251001': { input:  0.80, output:  4.00, cache_read: 0.08,  cache_write:  1.00 },
};

const OPUS_RATES = PRICING['claude-opus-4-7'];

const today = '2026-06-29';
const N = 7;
const todayDate = new Date('2026-06-29');
const cutoffDate = new Date(todayDate); cutoffDate.setDate(cutoffDate.getDate() - N); // 2026-06-22
const priorCutoffDate = new Date(todayDate); priorCutoffDate.setDate(priorCutoffDate.getDate() - 2*N); // 2026-06-15

function calcCost(model, inp, out, cr, cw) {
  const rates = PRICING[model] || OPUS_RATES;
  const isUnknown = !PRICING[model];
  const cost = (inp * rates.input + out * rates.output + cr * rates.cache_read + cw * rates.cache_write) / 1e6;
  return { cost, isUnknown };
}

const csvText = fs.readFileSync('memory/token-usage.csv', 'utf8');
const lines = csvText.trim().split('\n');
const header = lines[0].split(',');

let malformed = 0;
const unknownModels = {};
const inWindow = [];
const priorWindow = [];

for (let i = 1; i < lines.length; i++) {
  const cols = lines[i].split(',');
  if (cols.length < 7) { malformed++; continue; }
  const [dateStr, skill, model, inp_s, out_s, cr_s, cw_s] = cols;
  const inp = parseInt(inp_s), out = parseInt(out_s), cr = parseInt(cr_s), cw = parseInt(cw_s);
  if (isNaN(inp) || isNaN(out) || isNaN(cr) || isNaN(cw)) { malformed++; continue; }
  const d = new Date(dateStr);
  const { cost, isUnknown } = calcCost(model, inp, out, cr, cw);
  if (isUnknown) {
    if (!unknownModels[model]) unknownModels[model] = { inp: 0, out: 0 };
    unknownModels[model].inp += inp;
    unknownModels[model].out += out;
  }
  const entry = { date: d, dateStr, skill, model, inp, out, cr, cw, cost };
  if (d >= cutoffDate) inWindow.push(entry);
  else if (d >= priorCutoffDate) priorWindow.push(entry);
}

const totalCost = inWindow.reduce((s, e) => s + e.cost, 0);
const priorCost = priorWindow.reduce((s, e) => s + e.cost, 0);

console.log(`IN_WINDOW_ROWS=${inWindow.length}`);
console.log(`PRIOR_WINDOW_ROWS=${priorWindow.length}`);
console.log(`MALFORMED=${malformed}`);
console.log(`TOTAL_COST=${totalCost.toFixed(6)}`);
console.log(`PRIOR_COST=${priorCost.toFixed(6)}`);

function getRates(model) { return PRICING[model] || OPUS_RATES; }

const compInp = inWindow.reduce((s, e) => s + e.inp * getRates(e.model).input / 1e6, 0);
const compOut = inWindow.reduce((s, e) => s + e.out * getRates(e.model).output / 1e6, 0);
const compCR  = inWindow.reduce((s, e) => s + e.cr  * getRates(e.model).cache_read / 1e6, 0);
const compCW  = inWindow.reduce((s, e) => s + e.cw  * getRates(e.model).cache_write / 1e6, 0);
console.log(`COMP_INP=${compInp.toFixed(6)}`);
console.log(`COMP_OUT=${compOut.toFixed(6)}`);
console.log(`COMP_CR=${compCR.toFixed(6)}`);
console.log(`COMP_CW=${compCW.toFixed(6)}`);

// Per-skill stats
const skillStats = {};
for (const e of inWindow) {
  if (!skillStats[e.skill]) skillStats[e.skill] = { runs: 0, inp: 0, out: 0, cr: 0, cw: 0, cost: 0, rows: [] };
  const s = skillStats[e.skill];
  s.runs++; s.inp += e.inp; s.out += e.out; s.cr += e.cr; s.cw += e.cw; s.cost += e.cost; s.rows.push(e);
}

const topSkills = Object.entries(skillStats).sort((a, b) => b[1].cost - a[1].cost).slice(0, 10);
console.log('\nTOP10_SKILLS:');
for (const [sk, st] of topSkills) {
  const totalTok = st.inp + st.out + st.cr + st.cw;
  const avg = st.cost / st.runs;
  console.log(`  ${sk.padEnd(28)} runs=${st.runs} tokens=${totalTok.toLocaleString().padStart(14)} cost=${st.cost.toFixed(4)} avg=${avg.toFixed(4)}`);
}

// Per-model
const modelStats = {};
for (const e of inWindow) {
  if (!modelStats[e.model]) modelStats[e.model] = { runs: 0, inp: 0, out: 0, cost: 0 };
  const m = modelStats[e.model];
  m.runs++; m.inp += e.inp; m.out += e.out; m.cost += e.cost;
}
console.log('\nMODEL_STATS:');
for (const [m, st] of Object.entries(modelStats).sort()) {
  console.log(`  ${m.padEnd(35)} runs=${st.runs} cost=${st.cost.toFixed(4)}`);
}

const dailyAvg = totalCost / N;
const projMonthly = dailyAvg * 30;
console.log(`\nDAILY_AVG=${dailyAvg.toFixed(6)}`);
console.log(`PROJ_MONTHLY=${projMonthly.toFixed(6)}`);

if (priorCost > 0) {
  const delta = (totalCost - priorCost) / priorCost * 100;
  console.log(`WOW_DELTA=${delta.toFixed(1)}`);
} else {
  console.log('WOW_DELTA=NONE');
}

// Anomaly detection
console.log('\nANOMALIES:');
const anomalies = [];
for (const [sk, st] of Object.entries(skillStats)) {
  const modelsUsed = [...new Set(st.rows.map(e => e.model))];
  for (const m of modelsUsed) {
    const runs = st.rows.filter(e => e.model === m);
    if (runs.length < 3) continue;
    const costs = runs.map(e => e.cost);
    const mu = costs.reduce((a, b) => a + b, 0) / costs.length;
    const variance = costs.reduce((a, c) => a + (c - mu) ** 2, 0) / costs.length;
    const sigma = Math.sqrt(variance);
    for (const e of runs) {
      if (e.cost > mu + 2 * sigma && e.cost > 0.10) {
        anomalies.push({ skill: sk, model: m, dateStr: e.dateStr, cost: e.cost, mu, sigma, inp: e.inp, out: e.out, cw: e.cw });
        console.log(`  ANOMALY: skill=${sk} model=${m} date=${e.dateStr} cost=${e.cost.toFixed(4)} mu=${mu.toFixed(4)} sigma=${sigma.toFixed(4)} inp=${e.inp} out=${e.out} cw=${e.cw}`);
      }
    }
  }
}
if (anomalies.length === 0) console.log('  NONE');

// WoW spikes per skill
console.log('\nSPIKE_SKILLS:');
const priorSkillCost = {};
for (const e of priorWindow) {
  priorSkillCost[e.skill] = (priorSkillCost[e.skill] || 0) + e.cost;
}
let spikeCount = 0;
for (const [sk, st] of Object.entries(skillStats)) {
  const pc = priorSkillCost[sk] || 0;
  if (pc >= 0.25 && st.cost >= 2 * pc) {
    console.log(`  SPIKE: skill=${sk} cur=${st.cost.toFixed(4)} prior=${pc.toFixed(4)} ratio=${(st.cost/pc).toFixed(1)}x`);
    spikeCount++;
  }
}
if (spikeCount === 0) console.log('  NONE');

// Optimization: model downgrade
console.log('\nDOWNGRADE_CANDIDATES:');
let optCount = 0;
const sortedByOpusCost = Object.entries(skillStats)
  .map(([sk, st]) => {
    const opusRows = st.rows.filter(e => e.model === 'claude-opus-4-7');
    if (!opusRows.length) return null;
    const totalInp = opusRows.reduce((s, e) => s + e.inp, 0);
    const totalOut = opusRows.reduce((s, e) => s + e.out, 0);
    const avgCost = opusRows.reduce((s, e) => s + e.cost, 0) / opusRows.length;
    const totalCostSk = opusRows.reduce((s, e) => s + e.cost, 0);
    const sonnetCost = opusRows.reduce((s, e) => s + (e.inp*3 + e.out*15 + e.cr*0.30 + e.cw*3.75)/1e6, 0);
    const savings = totalCostSk - sonnetCost;
    const ratio = totalInp > 0 ? totalOut / totalInp : 999;
    return { sk, ratio, avgCost, totalCostSk, sonnetCost, savings };
  })
  .filter(x => x && x.ratio < 0.3 && x.avgCost > 0.25)
  .sort((a, b) => b.savings - a.savings);

for (const x of sortedByOpusCost.slice(0, 5)) {
  console.log(`  DOWNGRADE: skill=${x.sk} ratio=${x.ratio.toFixed(3)} avg_run=${x.avgCost.toFixed(4)} opus=${x.totalCostSk.toFixed(4)} sonnet=${x.sonnetCost.toFixed(4)} savings=${x.savings.toFixed(4)}`);
  optCount++;
}
if (optCount === 0) console.log('  NONE');

// Cache underuse
console.log('\nCACHE_UNDERUSE:');
let cacheCount = 0;
for (const [sk, st] of Object.entries(skillStats).sort((a, b) => b[1].cost - a[1].cost)) {
  const totalInp = st.rows.reduce((s, e) => s + e.inp, 0);
  const totalCR = st.rows.reduce((s, e) => s + e.cr, 0);
  const avgCost = st.cost / st.runs;
  const denom = totalCR + totalInp;
  if (denom > 0) {
    const ratio = totalCR / denom;
    if (ratio < 0.2 && avgCost > 0.10) {
      console.log(`  CACHE_LOW: skill=${sk} cr_ratio=${ratio.toFixed(3)} avg_run=${avgCost.toFixed(4)} total=${st.cost.toFixed(4)}`);
      cacheCount++;
      if (cacheCount >= 5) break;
    }
  }
}
if (cacheCount === 0) console.log('  NONE');

console.log('\nUNKNOWN_MODELS:');
if (Object.keys(unknownModels).length > 0) {
  for (const [m, t] of Object.entries(unknownModels)) {
    console.log(`  UNKNOWN: model=${m} inp=${t.inp} out=${t.out}`);
  }
} else {
  console.log('  NONE');
}

console.log(`\nTOTAL_RUNS=${inWindow.length}`);
