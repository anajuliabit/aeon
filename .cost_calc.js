const fs = require('fs');

const CUTOFF = "2026-08-04";
const PRIOR_CUTOFF = "2026-07-28";
const N = 7;

const RATES = {
  "claude-opus-4-7":           {input: 15.00, output: 75.00, cache_read: 1.50, cache_write: 18.75},
  "claude-sonnet-4-6":         {input: 3.00,  output: 15.00, cache_read: 0.30, cache_write: 3.75},
  "claude-haiku-4-5-20251001": {input: 0.80,  output: 4.00,  cache_read: 0.08, cache_write: 1.00},
};

const lines = fs.readFileSync('memory/token-usage.csv', 'utf8').trim().split('\n');
const header = lines[0].split(',');

const rows_current = [], rows_prior = [];
let malformed = 0;
const unknown_models = new Set();

for (let i = 1; i < lines.length; i++) {
  const parts = lines[i].split(',');
  if (parts.length < 7) { malformed++; continue; }
  const [date, skill, model, inp_s, out_s, cr_s, cw_s] = parts;
  const inp = parseInt(inp_s), out = parseInt(out_s), cr = parseInt(cr_s), cw = parseInt(cw_s);
  if (isNaN(inp)||isNaN(out)||isNaN(cr)||isNaN(cw)) { malformed++; continue; }

  let rates = RATES[model];
  if (!rates) { unknown_models.add(model); rates = RATES["claude-opus-4-7"]; }

  const cost = inp/1e6*rates.input + out/1e6*rates.output + cr/1e6*rates.cache_read + cw/1e6*rates.cache_write;
  const ic   = inp/1e6*rates.input;
  const oc   = out/1e6*rates.output;
  const crc  = cr/1e6*rates.cache_read;
  const cwc  = cw/1e6*rates.cache_write;

  const rec = {date, skill, model, inp, out, cr, cw, cost, ic, oc, crc, cwc};
  if (date >= CUTOFF) rows_current.push(rec);
  else if (date >= PRIOR_CUTOFF) rows_prior.push(rec);
}

function total(rows) {
  return rows.reduce((a,r)=>a+r.cost,0);
}
function totalIC(rows) { return rows.reduce((a,r)=>a+r.ic,0); }
function totalOC(rows) { return rows.reduce((a,r)=>a+r.oc,0); }
function totalCRC(rows){ return rows.reduce((a,r)=>a+r.crc,0); }
function totalCWC(rows){ return rows.reduce((a,r)=>a+r.cwc,0); }

const cur = total(rows_current);
const pri = total(rows_prior);
const wow = pri > 0 ? (cur - pri)/pri*100 : null;

console.log(`TOTAL=${cur.toFixed(4)}`);
console.log(`INPUT=${totalIC(rows_current).toFixed(4)}`);
console.log(`OUTPUT=${totalOC(rows_current).toFixed(4)}`);
console.log(`CACHE_READ=${totalCRC(rows_current).toFixed(4)}`);
console.log(`CACHE_WRITE=${totalCWC(rows_current).toFixed(4)}`);
console.log(`PRIOR=${pri.toFixed(4)}`);
console.log(`WOW=${wow !== null ? wow.toFixed(1) : 'none'}`);
console.log(`RUNS=${rows_current.length}`);

// per-skill
const skillMap = {};
for (const r of rows_current) {
  if (!skillMap[r.skill]) skillMap[r.skill] = {runs:0, tokens:0, cost:0, costArr:[], rows:[]};
  skillMap[r.skill].runs++;
  skillMap[r.skill].tokens += r.inp+r.out+r.cr+r.cw;
  skillMap[r.skill].cost += r.cost;
  skillMap[r.skill].costArr.push(r.cost);
  skillMap[r.skill].rows.push(r);
}

const top10 = Object.entries(skillMap).sort((a,b)=>b[1].cost-a[1].cost).slice(0,10);
console.log('TOP10_START');
for (const [s,d] of top10) {
  const avg = d.cost/d.runs;
  console.log(`${s}|${d.runs}|${d.tokens}|${d.cost.toFixed(4)}|${avg.toFixed(4)}`);
}
console.log('TOP10_END');

// per-model
const modelMap = {};
for (const r of rows_current) {
  if (!modelMap[r.model]) modelMap[r.model] = {runs:0, tokens:0, cost:0};
  modelMap[r.model].runs++;
  modelMap[r.model].tokens += r.inp+r.out+r.cr+r.cw;
  modelMap[r.model].cost += r.cost;
}
console.log('MODELS_START');
for (const [m,d] of Object.entries(modelMap).sort((a,b)=>b[1].cost-a[1].cost)) {
  console.log(`${m}|${d.runs}|${d.tokens}|${d.cost.toFixed(4)}`);
}
console.log('MODELS_END');

// anomalies (per run, >= 3 runs in (skill,model) group)
const smMap = {};
for (const r of rows_current) {
  const k = r.skill+'|'+r.model;
  if (!smMap[k]) smMap[k] = [];
  smMap[k].push(r);
}

const anomalies = [];
for (const [k, group] of Object.entries(smMap)) {
  if (group.length < 3) continue;
  const costs = group.map(r=>r.cost);
  const mu = costs.reduce((a,b)=>a+b,0)/costs.length;
  const sigma = Math.sqrt(costs.map(c=>(c-mu)**2).reduce((a,b)=>a+b,0)/costs.length);
  for (const r of group) {
    if (r.cost > mu + 2*sigma && r.cost > 0.10) {
      anomalies.push({...r, mu, sigma});
    }
  }
}

// skill doubles vs prior
const priorSkill = {};
for (const r of rows_prior) {
  if (!priorSkill[r.skill]) priorSkill[r.skill] = 0;
  priorSkill[r.skill] += r.cost;
}

console.log('ANOMALIES_START');
for (const a of anomalies) {
  console.log(`${a.skill}|${a.model}|${a.date}|${a.cost.toFixed(4)}|${a.mu.toFixed(4)}|${a.sigma.toFixed(4)}|${a.inp}|${a.out}|${a.cw}`);
}
console.log('ANOMALIES_END');

console.log('DOUBLES_START');
for (const [skill,d] of Object.entries(skillMap)) {
  const prior = priorSkill[skill]||0;
  if (prior >= 0.25 && d.cost >= 2*prior) {
    console.log(`${skill}|${d.cost.toFixed(4)}|${prior.toFixed(4)}`);
  }
}
console.log('DOUBLES_END');

const daily = cur/N;
const monthly = daily*30;
console.log(`DAILY=${daily.toFixed(4)}`);
console.log(`MONTHLY=${monthly.toFixed(4)}`);

// optimization: model downgrade candidates
console.log('OPT_START');
const downgrade_candidates = [];
for (const [skill, d] of Object.entries(skillMap)) {
  const opusRows = d.rows.filter(r=>r.model==='claude-opus-4-7');
  if (!opusRows.length) continue;
  const avgCost = d.cost/d.runs;
  if (avgCost <= 0.25) continue;
  const ratios = opusRows.filter(r=>r.inp>0).map(r=>r.out/r.inp);
  if (!ratios.length) continue;
  const sorted = [...ratios].sort((a,b)=>a-b);
  const medRatio = sorted[Math.floor(sorted.length/2)];
  if (medRatio < 0.3) {
    const savings = d.cost * (1 - 18/90);
    downgrade_candidates.push({skill, avgCost, medRatio, savings, cost: d.cost});
  }
}
downgrade_candidates.sort((a,b)=>b.savings-a.savings);
for (const c of downgrade_candidates.slice(0,3)) {
  console.log(`DOWNGRADE|${c.skill}|${c.cost.toFixed(4)}|${c.avgCost.toFixed(4)}|${c.medRatio.toFixed(3)}|${c.savings.toFixed(4)}`);
}

// cache underuse
const cache_candidates = [];
for (const [skill, d] of Object.entries(skillMap)) {
  const avgCost = d.cost/d.runs;
  if (avgCost <= 0.10) continue;
  const totalCR = d.rows.reduce((a,r)=>a+r.cr,0);
  const totalInp = d.rows.reduce((a,r)=>a+r.inp,0);
  if (totalCR+totalInp === 0) continue;
  const ratio = totalCR/(totalCR+totalInp);
  if (ratio < 0.2) {
    cache_candidates.push({skill, ratio, avgCost, cost: d.cost});
  }
}
cache_candidates.sort((a,b)=>b.cost-a.cost);
for (const c of cache_candidates.slice(0,3)) {
  console.log(`CACHE|${c.skill}|${c.cost.toFixed(4)}|${c.avgCost.toFixed(4)}|${c.ratio.toFixed(3)}`);
}
console.log('OPT_END');

console.log(`UNKNOWN=${[...unknown_models].join(',') || 'none'}`);
console.log(`MALFORMED=${malformed}`);
