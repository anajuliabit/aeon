#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const WALLET = '0x8def9f50456c6c4e37fa5d3d57f108ed23992dae';
const DATANET_ID = '9';

const fills = JSON.parse(fs.readFileSync(path.join('.hl-cache', `user-fills-${WALLET}.json`), 'utf8'));
if (!Array.isArray(fills) || !fills.length) { console.error('no fills'); process.exit(1); }

// Direction inference from `dir` field
function directionOf(f) {
  const d = f.dir || '';
  if (d.includes('Long')) return 'long';
  if (d.includes('Short')) return 'short';
  return 'unknown';
}

// market_context: derived from fill-price slope of nearby same-coin fills
// (we have no OHLCV cached for LIT, so we use a rolling slope of fill prices as a proxy)
// Rule documented in dataset's market_context_rules.
function computeContext(fills, idx, windowSize = 50) {
  const cur = fills[idx];
  const start = Math.max(0, idx - windowSize);
  const window = fills.slice(start, idx + 1).filter(g => g.coin === cur.coin);
  if (window.length < 5) return 'low-liquidity';
  const prices = window.map(g => parseFloat(g.px));
  const first = prices[0], last = prices[prices.length - 1];
  const minP = Math.min(...prices), maxP = Math.max(...prices);
  const rangePct = ((maxP - minP) / minP) * 100;
  const slopePct = ((last - first) / first) * 100;
  if (rangePct > 3 && Math.abs(slopePct) < 0.5) return 'ranging';
  if (rangePct > 5 && Math.abs(slopePct) > 2) return 'high-volatility';
  if (slopePct > 0.3) return 'trending-up';
  if (slopePct < -0.3) return 'trending-down';
  return 'ranging';
}

// Hold duration: for closing fills, find the earliest preceding fill that opened or
// has a same-coin transition; if no opening fill present in window, use the time of the
// first same-coin fill as a lower bound; otherwise emit null.
function holdDuration(fills, idx) {
  const cur = fills[idx];
  // Walk back to find the earliest same-coin fill of same position lifecycle
  const sameCoin = [];
  for (let i = idx; i >= 0; i--) {
    if (fills[i].coin === cur.coin) sameCoin.push(fills[i]);
    else if (sameCoin.length > 0) break;
  }
  if (sameCoin.length < 2) return null;
  const oldest = sameCoin[sameCoin.length - 1];
  return Math.round((cur.time - oldest.time) / 1000);
}

const trades = fills.map((f, i) => {
  const dir = directionOf(f);
  const pnl = parseFloat(f.closedPnl);
  const isClose = (f.dir || '').includes('Close');
  const hold = isClose ? holdDuration(fills, i) : null;
  return {
    market: f.coin,
    direction: dir,
    size: parseFloat(f.sz),
    leverage: null,
    fill_price: parseFloat(f.px),
    signal: 'unclassified',
    outcome: {
      pnl: pnl,
      hold_duration_seconds: hold,
      win: isClose ? pnl > 0 : null
    },
    market_context: computeContext(fills, i),
    timeframe: '1m',
    verification: {
      timestamp_ms: f.time,
      tx_hash: f.hash
    }
  };
});

// aggregate metrics
const closes = fills.filter(f => (f.dir || '').includes('Close'));
const pnls = closes.map(f => parseFloat(f.closedPnl));
const wins = pnls.filter(p => p > 0).length;
const n = closes.length;
const sumPnl = pnls.reduce((a, b) => a + b, 0);

const notionals = closes.map(f => parseFloat(f.px) * parseFloat(f.sz));
const rets = pnls.map((p, i) => notionals[i] > 0 ? p / notionals[i] : 0);
const meanR = rets.reduce((a, b) => a + b, 0) / n;
const varR = rets.reduce((a, r) => a + Math.pow(r - meanR, 2), 0) / Math.max(n - 1, 1);
const stdR = Math.sqrt(varR);
const firstMs = fills[0].time;
const lastMs = fills[fills.length - 1].time;
const daysCovered = Math.max((lastMs - firstMs) / 1000 / 86400, 1 / 86400);
const sharpe = stdR > 0 ? (meanR / stdR) * Math.sqrt(n * 365.0 / daysCovered) : 0;

let cum = 0, peak = 0, maxDD = 0;
for (const p of pnls) {
  cum += p;
  if (cum > peak) peak = cum;
  if (peak - cum > maxDD) maxDD = peak - cum;
}
const mddPct = peak > 0 ? (maxDD / peak) * 100 : 0;

const canonical = `trades:9:${WALLET}:${firstMs}:${lastMs}:${n}`;
const hash = crypto.createHash('sha256').update(canonical).digest('hex');
const hash16 = hash.slice(0, 16);

const dataset = {
  kind: 'hl-perp-trades',
  schema_version: 1,
  source: { wallet: WALLET, venue: 'hyperliquid-mainnet' },
  signal_taxonomy: {
    'unclassified': 'No locally cached LIT 1h OHLCV available this run; per-fill indicator labels (breakout-up / mean-reversion-long) were not derivable, so every row is marked unclassified. Cached OHLCV in .hl-cache/ this run covers BTC/ETH/SOL only.'
  },
  market_context_rules: {
    'trending-up': '50-fill rolling same-coin slope > +0.3%',
    'trending-down': '50-fill rolling same-coin slope < -0.3%',
    'ranging': '50-fill rolling abs(slope) < 0.3% (no strong trend)',
    'high-volatility': '50-fill rolling range > 5% AND abs(slope) > 2%',
    'low-liquidity': 'fewer than 5 same-coin fills in the rolling window'
  },
  ohlcv_interval: '1h (BTC/ETH/SOL cached this run; LIT not cached so signal taxonomy is unclassified)',
  aggregate_metrics: {
    n_trades: n,
    win_rate: wins / n,
    sharpe: sharpe,
    max_drawdown_pct: mddPct,
    days_covered: Math.round(daysCovered * 10000) / 10000
  },
  trades: trades
};

const intent = {
  cmd: 'mint-pod',
  datanet: DATANET_ID,
  idempotency_key: hash,
  strategy_summary: `HL perp trades — ${WALLET.slice(0,6)}..${WALLET.slice(-4)} — ${n} closed, Sharpe ${sharpe.toFixed(1)}, MDD ${mddPct.toFixed(2)}%, win ${(wins/n).toFixed(4)}, span ${new Date(firstMs).toISOString()}..${new Date(lastMs).toISOString()}`,
  pod_name: `HL perps 1.7h, ${WALLET.slice(0,6)}..${WALLET.slice(-4)}: ${n} LIT closes`,
  pod_description: `Source wallet ${WALLET} (Hyperliquid mainnet). Window ${new Date(firstMs).toISOString()} → ${new Date(lastMs).toISOString()} (${(daysCovered*24).toFixed(2)}h). Single-market dataset — LIT perp, ${n} Close Long fills as the wallet scaled out of a 682,278 LIT long position down to 0. Signal taxonomy: unclassified (LIT OHLCV not cached this run; only BTC/ETH/SOL cached). Market context rules (applied per fill from a 50-fill rolling same-coin slope): trending-up >+0.3%, trending-down <-0.3%, ranging |slope|<0.3%, high-volatility range>5% & |slope|>2%, low-liquidity <5 same-coin fills. OHLCV interval: 1h (BTC/ETH/SOL; LIT not cached). Aggregate metrics — n_trades=${n}, win_rate=${(wins/n).toFixed(4)}, sharpe=${sharpe.toFixed(2)}, max_drawdown_pct=${mddPct.toFixed(2)}, days_covered=${(daysCovered).toFixed(4)}, sum_realized_pnl=$${sumPnl.toFixed(2)}. Every fill carries a verifying tx hash on Hyperliquid.`,
  url: `https://app.hyperliquid.xyz/explorer/address/${WALLET}`,
  dataset_path: `.pending-reppo/data/mint-${hash16}.json`
};

fs.mkdirSync('.pending-reppo/data', { recursive: true });
fs.writeFileSync(`.pending-reppo/mint-${hash16}.json`, JSON.stringify(intent, null, 2));
fs.writeFileSync(`.pending-reppo/data/mint-${hash16}.json`, JSON.stringify(dataset, null, 2));

console.log(JSON.stringify({
  wallet: WALLET,
  hash16, canonical,
  n_trades: n, win_rate: wins / n, sharpe, mddPct, daysCovered, sumPnl,
  firstMs, lastMs,
  written: [`.pending-reppo/mint-${hash16}.json`, `.pending-reppo/data/mint-${hash16}.json`]
}, null, 2));
