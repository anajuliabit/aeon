#!/usr/bin/env node
// process token-movers data from CG markets + trending
const fs = require('fs');

const markets = JSON.parse(fs.readFileSync('.daily-tmp/cg-markets-0617.json', 'utf8'));
const trending = JSON.parse(fs.readFileSync('.daily-tmp/cg-trending-0617.json', 'utf8'));

const STABLE_RE = /^(USDT|USDC|DAI|USDS|USDE|FDUSD|TUSD|FRAX|BUSD|LUSD|GHO|CRVUSD|PYUSD|USDD|USDP|GUSD|USDX|RUSD|XAUT|PAXG|USYC|SDAI|MIM|VAI|SUSD|FXUSD|ALUSD|USD1|USDG|USDU|USDM|USDAI|NUSD|USDGO)$/i;
const WRAP_RE = /(wrapped|weth|wbtc|steth|reth|wsteth|cbeth|wbeth)/i;

const filtered = markets.filter(c =>
  c.symbol &&
  !STABLE_RE.test(c.symbol) &&
  !WRAP_RE.test(c.id || '') &&
  (c.total_volume || 0) >= 1_000_000 &&
  c.price_change_percentage_24h_in_currency != null
);

const total = filtered.length;
const green = filtered.filter(c => c.price_change_percentage_24h_in_currency > 0).length;
const top50 = filtered.slice(0, 50).map(c => c.price_change_percentage_24h_in_currency).sort((a,b)=>a-b);
const median = top50[Math.floor(top50.length / 2)];

const btc = markets.find(c => c.symbol === 'btc');
const eth = markets.find(c => c.symbol === 'eth');
const sol = markets.find(c => c.symbol === 'sol');

const fmt = (n, p=2) => n == null ? 'n/a' : Number(n).toLocaleString('en-US', {maximumFractionDigits: p});
const pct = (n) => n == null ? 'n/a' : `${n >= 0 ? '+' : ''}${n.toFixed(1)}%`;
const compact = (n) => {
  if (n == null) return 'n/a';
  if (n >= 1e9) return `$${(n/1e9).toFixed(1)}B`;
  if (n >= 1e6) return `$${(n/1e6).toFixed(0)}M`;
  if (n >= 1e3) return `$${(n/1e3).toFixed(0)}K`;
  return `$${n.toFixed(0)}`;
};
const price = (p) => {
  if (p == null) return 'n/a';
  if (p >= 100) return `$${p.toLocaleString('en-US', {maximumFractionDigits:0})}`;
  if (p >= 1) return `$${p.toFixed(2)}`;
  if (p >= 0.01) return `$${p.toFixed(3)}`;
  if (p >= 0.0001) return `$${p.toFixed(5)}`;
  return `$${p.toExponential(2)}`;
};

console.log('=== PULSE ===');
console.log(`green/total: ${green}/${total} (${(green/total*100).toFixed(0)}%)`);
console.log(`median top50: ${pct(median)}`);
console.log(`BTC ${price(btc.current_price)} ${pct(btc.price_change_percentage_24h_in_currency)} / 7d ${pct(btc.price_change_percentage_7d_in_currency)}`);
console.log(`ETH ${price(eth.current_price)} ${pct(eth.price_change_percentage_24h_in_currency)} / 7d ${pct(eth.price_change_percentage_7d_in_currency)}`);
console.log(`SOL ${price(sol.current_price)} ${pct(sol.price_change_percentage_24h_in_currency)} / 7d ${pct(sol.price_change_percentage_7d_in_currency)}`);

const winners = [...filtered].sort((a,b) => b.price_change_percentage_24h_in_currency - a.price_change_percentage_24h_in_currency).slice(0, 12);
const losers = [...filtered].sort((a,b) => a.price_change_percentage_24h_in_currency - b.price_change_percentage_24h_in_currency).slice(0, 12);

console.log('\n=== WINNERS ===');
winners.forEach((c, i) => {
  const tags = [];
  if (c.market_cap_rank && c.market_cap_rank <= 20) tags.push('MAJOR');
  if ((c.price_change_percentage_7d_in_currency || 0) > 50) tags.push('BREAKOUT');
  console.log(`${i+1}. ${c.symbol.toUpperCase()} (${c.name}) — ${price(c.current_price)}  ${pct(c.price_change_percentage_24h_in_currency)} / 7d ${pct(c.price_change_percentage_7d_in_currency)} / 1h ${pct(c.price_change_percentage_1h_in_currency)}  •  ${compact(c.total_volume)} / #${c.market_cap_rank}${tags.length ? '  ['+tags.join('+')+']' : ''}`);
});

console.log('\n=== LOSERS ===');
losers.forEach((c, i) => {
  const tags = [];
  if ((c.price_change_percentage_24h_in_currency || 0) < -25) tags.push('CAPITULATION');
  console.log(`${i+1}. ${c.symbol.toUpperCase()} (${c.name}) — ${price(c.current_price)}  ${pct(c.price_change_percentage_24h_in_currency)} / 7d ${pct(c.price_change_percentage_7d_in_currency)} / 1h ${pct(c.price_change_percentage_1h_in_currency)}  •  ${compact(c.total_volume)} / #${c.market_cap_rank}${tags.length ? '  ['+tags.join('+')+']' : ''}`);
});

console.log('\n=== TRENDING ===');
const tcoins = trending.coins || [];
tcoins.slice(0, 10).forEach((t, i) => {
  const it = t.item;
  const mkt = markets.find(m => m.id === it.id);
  const p24 = mkt ? mkt.price_change_percentage_24h_in_currency : null;
  const p = mkt ? mkt.current_price : it.data?.price;
  console.log(`${i+1}. ${it.name} (${it.symbol}) — rank #${it.market_cap_rank || 'n/a'}, ${price(p)}, 24h ${pct(p24)}`);
});
