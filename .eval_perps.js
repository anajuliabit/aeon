#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const CACHE = '.hl-cache';
const WALLETS = Array.from(new Set([
  '0x0ddf9bae2af4b874b96d287a5ad42eb47138a902',
  '0x2b3349ff0c4cf96f7df87fd5f3d583ee625733f7',
  '0x32008fcb6bbd16532afc83ca8b6c920dde22c407',
  '0x675462411d40a169c3397ac1dc00786dc9c7d3a1',
  '0x577ae91c7b74f04ddb3a5b399ded8318e9895fd2',
  '0x477296b8f5f5525be26e5c0a82eb0dd24da3949f',
  '0x71dfc07de32c2ebf1c4801f4b1c9e40b76d4a23d',
  '0x7fdafde5cfb5465924316eced2d3715494c517d1',
  '0x856c35038594767646266bc7fd68dc26480e910d',
  '0x8def9f50456c6c4e37fa5d3d57f108ed23992dae',
  '0xa8dc22b6cc18fc27dc695bbc6e9a17603b9b095b',
  '0x9a1500b41519868039b1f95c447ba50b76d837e6',
  '0x9e875bd28ee5001478c16cb0c8329116a3c3e816',
  '0x953c5152e2f8b5ed9d92976cad478a837749182a',
  '0xb798aef79972ce8f73d47b9ebbcda6bbb7ec4fbf',
  '0xbb10bda01f56b1604f2f024f2d18fcaf5d2b20b0',
  '0xbdfa4f4492dd7b7cf211209c4791af8d52bf5c50',
  '0xd47587702a91731dc1089b5db0932cf820151a91',
  '0xebe126adabe1a8f08d3ce53b45e7cc994ca14070',
  '0xecb63caa47c7c4e77f60f1ce858cf28dc2b82b00',
  '0xa9b95f2a2e7ef219021efc5c04c32761b8553bbd',
  '0x87f9cd15f5050a9283b8896300f7c8cf69ece2cf',
  '0x4ec8fe22a531a96c8a846aaf5cbef73202649a80',
  '0xe6111266afdcdf0b1fe8505028cc1f7419d798a7',
])).sort();

// HL perp coins are bare symbols (BTC, ETH, etc.) without :, @, vntl:, xyz: prefixes
function isHLPerp(coin) {
  if (!coin) return false;
  if (coin.startsWith('@')) return false;
  if (coin.startsWith('xyz:')) return false;
  if (coin.startsWith('vntl:')) return false;
  if (coin.includes(':')) return false;
  return true;
}

function aggregate(wallet) {
  const p = path.join(CACHE, `user-fills-${wallet}.json`);
  let fills;
  try { fills = JSON.parse(fs.readFileSync(p, 'utf8')); }
  catch (e) { return { wallet, error: e.message }; }
  if (fills && fills.code) return { wallet, error: fills.code };
  if (!Array.isArray(fills)) return { wallet, error: 'not-array' };
  if (!fills.length) return { wallet, n_fills: 0, error: 'empty' };

  // Filter to HL perp markets only
  const perpFills = fills.filter(f => isHLPerp(f.coin));
  if (perpFills.length < 20) {
    return { wallet, n_fills: fills.length, n_perp_fills: perpFills.length, error: 'lt20-perp-fills' };
  }

  const closes = perpFills.filter(f => (f.dir || '').includes('Close'));
  if (closes.length < 20) {
    return { wallet, n_fills: fills.length, n_perp_fills: perpFills.length, n_closes: closes.length, error: 'lt20-closes' };
  }

  const pnls = closes.map(f => parseFloat(f.closedPnl));
  const notionals = closes.map(f => parseFloat(f.px) * parseFloat(f.sz));
  const rets = pnls.map((p, i) => notionals[i] > 0 ? p / notionals[i] : 0);

  const n = closes.length;
  const wins = pnls.filter(p => p > 0).length;
  const sum_pnl = pnls.reduce((a, b) => a + b, 0);
  const mean_pnl = sum_pnl / n;

  const first_ms = perpFills[0].time;
  const last_ms = perpFills[perpFills.length - 1].time;
  const days_covered = Math.max((last_ms - first_ms) / 1000 / 86400, 1 / 86400);

  const mean_r = rets.reduce((a, b) => a + b, 0) / n;
  const var_r = rets.reduce((a, r) => a + Math.pow(r - mean_r, 2), 0) / Math.max(n - 1, 1);
  const std_r = Math.sqrt(var_r);
  const sharpe = std_r > 0 && days_covered > 0 ? (mean_r / std_r) * Math.sqrt(n * 365.0 / days_covered) : 0;

  let cum = 0, peak = 0, max_dd_abs = 0;
  for (const p of pnls) {
    cum += p;
    if (cum > peak) peak = cum;
    const dd = peak - cum;
    if (dd > max_dd_abs) max_dd_abs = dd;
  }
  const max_dd_pct = peak > 0 ? (max_dd_abs / peak) * 100 : 0;

  const coins = [...new Set(perpFills.map(f => f.coin))].sort();
  const dirs = [...new Set(perpFills.map(f => f.dir))];
  const canonical = `trades:9:${wallet}:${first_ms}:${last_ms}:${n}`;
  const hash = crypto.createHash('sha256').update(canonical).digest('hex');

  return {
    wallet, n_fills: fills.length, n_perp_fills: perpFills.length, n_closes: n,
    win_rate: wins / n, sum_pnl, mean_pnl, sharpe_ann: sharpe, max_dd_pct, max_dd_abs,
    days_covered, first_ms, last_ms, coins, dirs, canonical, hash, hash16: hash.slice(0, 16)
  };
}

const results = WALLETS.map(aggregate);
for (const r of results) {
  if (r.error) console.log(`${r.wallet}: skip (${r.error})`);
  else console.log(`${r.wallet}: nperp=${r.n_perp_fills} closes=${r.n_closes} pnl=$${r.sum_pnl.toFixed(0)} win=${r.win_rate.toFixed(3)} sharpe=${r.sharpe_ann.toFixed(2)} mdd=${r.max_dd_pct.toFixed(1)}% days=${r.days_covered.toFixed(3)} hash16=${r.hash16} coins=${r.coins.join(',')} dirs=${r.dirs.join('|')}`);
}

const valid = results.filter(r => !r.error && (r.n_closes || 0) >= 20)
  .sort((a, b) => b.sharpe_ann - a.sharpe_ann || b.n_closes - a.n_closes);
console.log('\n=== HL-perp-only, ranked by Sharpe ===');
for (const r of valid) console.log(`${r.hash16}  ${r.wallet}  closes=${r.n_closes}  sharpe=${r.sharpe_ann.toFixed(2)}  pnl=$${r.sum_pnl.toFixed(0)}  coins=${r.coins.length}`);

fs.writeFileSync('/tmp/eval_perps.json', JSON.stringify(valid, null, 2));
console.log('\nWrote /tmp/eval_perps.json');
