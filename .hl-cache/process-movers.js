#!/usr/bin/env node
const fs = require('fs');
const markets = JSON.parse(fs.readFileSync('.hl-cache/cg-markets.json','utf8'));
const trending = JSON.parse(fs.readFileSync('.hl-cache/cg-trending.json','utf8'));

const STABLE_IDS = new Set([
  'tether','usd-coin','dai','first-digital-usd','usde','ethena-usde','tusd','true-usd',
  'usdd','pyusd','paypal-usd','fdusd','paxg','pax-gold','frax','lusd','susds',
  'usds','ousg','bsc-usd','binance-usd','gho','crvusd','usd0','usd0-liquid-bond',
  'tether-eurt','euro-coin','stasis-eurs','usdt0','blackrock-usd-institutional-digital-liquidity-fund',
  'sky-dollar','susd','rai','m','m-by-m0','ondo-us-dollar-yield','usdtb',
  'mountain-protocol-usdm','xaut','tether-gold','rusd','reservoir-rusd','syrupusdc',
  'syrup','usdf','falcon-usd','deusd','sdeusd','staked-usde','aave-usd-coin','aave-usdt','aave-dai'
]);

const WRAPPED_DUPES = new Set([
  'wbtc','wrapped-bitcoin','tbtc','solv-protocol-solvbtc','solv-btc',
  'weth','wsteth','wrapped-steth','wbeth','steth','staked-ether','reth','rocket-pool-eth',
  'cbeth','meth','mantle-staked-ether','wrapped-ethena-usde','liquid-staked-ethereum',
  'ether-fi-staked-eth','jito-staked-sol','wrapped-eeth','wbtc-token','msol'
]);

function isStableLike(c){
  if (STABLE_IDS.has(c.id)) return true;
  const sym = (c.symbol||'').toUpperCase();
  if (/^USD[A-Z0-9]?/.test(sym)) return true;
  if (/^EUR[A-Z0-9]?/.test(sym)) return true;
  if (/^GBP[A-Z0-9]?/.test(sym)) return true;
  if (/stablecoin/i.test(c.name||'')) return true;
  if (c.current_price > 0.97 && c.current_price < 1.03 &&
      Math.abs(c.price_change_percentage_24h||0) < 0.5 &&
      Math.abs(c.price_change_percentage_7d_in_currency||0) < 1) return true;
  return false;
}

const filtered = markets.filter(c => {
  if (!c || typeof c.price_change_percentage_24h !== 'number') return false;
  if (isStableLike(c)) return false;
  if (WRAPPED_DUPES.has(c.id)) return false;
  if (!c.total_volume || c.total_volume < 1_000_000) return false;
  return true;
});

const byPctDesc = (a,b) => (b.price_change_percentage_24h||0) - (a.price_change_percentage_24h||0);
const winners = [...filtered].sort(byPctDesc).slice(0, 10);
const losers = [...filtered].sort((a,b) => (a.price_change_percentage_24h||0) - (b.price_change_percentage_24h||0)).slice(0, 10);

const trendingCoins = (trending.coins||[]).slice(0,7).map(t => {
  const item = t.item || t;
  const full = markets.find(m => m.id === item.id) || {};
  return {
    id: item.id,
    name: item.name,
    symbol: (item.symbol||'').toUpperCase(),
    market_cap_rank: item.market_cap_rank || full.market_cap_rank || null,
    current_price: full.current_price ?? (item.data?.price ? Number(item.data.price) : null),
    price_change_percentage_24h: full.price_change_percentage_24h ?? (item.data?.price_change_percentage_24h?.usd ?? null),
    price_change_percentage_7d_in_currency: full.price_change_percentage_7d_in_currency,
    price_change_percentage_1h_in_currency: full.price_change_percentage_1h_in_currency,
    total_volume: full.total_volume,
    market_cap: full.market_cap,
  };
});

const trendingIds = new Set(trendingCoins.map(t => t.id));

function computeTags(c){
  const tags = [];
  const inTrend = trendingIds.has(c.id);
  const ch24 = c.price_change_percentage_24h || 0;
  const ch7d = c.price_change_percentage_7d_in_currency || 0;
  const volMcapRatio = c.market_cap ? (c.total_volume / c.market_cap) : 0;
  const rank = c.market_cap_rank || 9999;
  const mcap = c.market_cap || 0;

  if (inTrend && ch24 > 0) tags.push('TRENDING+UP');
  if (inTrend && ch24 < 0) tags.push('TRENDING+DOWN');
  if (ch24 > 15 && ch7d > 25) tags.push('BREAKOUT');
  if (ch24 > 20 && ch7d < 0) tags.push('FADE');
  if (ch24 < -10 && volMcapRatio > 0.25) tags.push('CAPITULATION');
  if (rank > 150 && ch24 > 30) tags.push('PUMP-RISK');
  if (mcap > 0 && mcap < 50_000_000) tags.push('MICROCAP');
  if (rank <= 20) tags.push('MAJOR');
  return tags.slice(0, 2);
}

function shape(c){
  return {
    id: c.id,
    name: c.name,
    symbol: (c.symbol||'').toUpperCase(),
    rank: c.market_cap_rank,
    price: c.current_price,
    ch_1h: c.price_change_percentage_1h_in_currency,
    ch_24h: c.price_change_percentage_24h,
    ch_7d: c.price_change_percentage_7d_in_currency,
    vol: c.total_volume,
    mcap: c.market_cap,
    tags: computeTags(c),
  };
}

const winnersOut = winners.map(shape);
const losersOut = losers.map(shape);
const trendingOut = trendingCoins.map(shape);

const top100 = filtered.slice(0, 100);
const greens = top100.filter(c => (c.price_change_percentage_24h||0) > 0).length;
const top50 = filtered.slice(0, 50);
const sorted50 = [...top50].sort((a,b) => (a.price_change_percentage_24h||0) - (b.price_change_percentage_24h||0));
const median50 = sorted50.length ? sorted50[Math.floor(sorted50.length/2)].price_change_percentage_24h : 0;

const btc = markets.find(m => m.id === 'bitcoin');
const eth = markets.find(m => m.id === 'ethereum');
const sol = markets.find(m => m.id === 'solana');

const out = {
  pulse: {
    top100_greens: greens,
    top100_total: top100.length,
    median50: median50,
    btc: btc ? {price: btc.current_price, ch_24h: btc.price_change_percentage_24h, ch_7d: btc.price_change_percentage_7d_in_currency} : null,
    eth: eth ? {price: eth.current_price, ch_24h: eth.price_change_percentage_24h, ch_7d: eth.price_change_percentage_7d_in_currency} : null,
    sol: sol ? {price: sol.current_price, ch_24h: sol.price_change_percentage_24h, ch_7d: sol.price_change_percentage_7d_in_currency} : null,
  },
  winners: winnersOut,
  losers: losersOut,
  trending: trendingOut,
};

fs.writeFileSync('.hl-cache/movers-out.json', JSON.stringify(out, null, 2));

console.log(JSON.stringify({
  filtered: filtered.length,
  total: markets.length,
  greens,
  median50: Number(median50.toFixed(2)),
  pulse_btc: btc ? `${btc.current_price} ${btc.price_change_percentage_24h.toFixed(2)}%/${btc.price_change_percentage_7d_in_currency.toFixed(2)}%7d` : null,
  pulse_eth: eth ? `${eth.current_price} ${eth.price_change_percentage_24h.toFixed(2)}%/${eth.price_change_percentage_7d_in_currency.toFixed(2)}%7d` : null,
  pulse_sol: sol ? `${sol.current_price} ${sol.price_change_percentage_24h.toFixed(2)}%/${sol.price_change_percentage_7d_in_currency.toFixed(2)}%7d` : null,
  top_winners: winnersOut.map(w => `${w.symbol} ${w.ch_24h.toFixed(1)}%[${w.tags.join('/')}]`),
  top_losers: losersOut.map(w => `${w.symbol} ${w.ch_24h.toFixed(1)}%[${w.tags.join('/')}]`),
  trending: trendingOut.map(w => `${w.symbol} ${(w.ch_24h||0).toFixed(1)}%[${w.tags.join('/')}]`),
}, null, 2));
