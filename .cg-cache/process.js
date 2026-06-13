const fs = require('fs');
const markets = JSON.parse(fs.readFileSync('.cg-cache/markets.json', 'utf8'));
const trending = JSON.parse(fs.readFileSync('.cg-cache/trending.json', 'utf8'));

const STABLE_IDS = new Set(['tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg','usds','ethena-usde','frax','usdt0','susds','ondo-us-dollar-yield','blackrock-usd-institutional-digital-liquidity-fund','sky-dollar','resolv-usr','falcon-usd','m0-foundation','tether-eurt','usdx-money-usdx','tether-gold','staked-frax','crypto-com-staked-eth','ethena-staked-usde','usdq','usd0','dola-usd','first-digital-labs-usd','usdtb']);
const WRAPPED_IDS = new Set(['wrapped-bitcoin','wrapped-steth','staked-ether','weth','wbeth','wrapped-eeth','rocket-pool-eth','coinbase-wrapped-btc','lombard-staked-btc','jito-staked-sol','binance-staked-sol','marinade-staked-sol','liquid-staked-ether','solv-protocol-solvbtc','renzo-restaked-eth','kelp-dao-restaked-eth','mantle-staked-ether','mantle-restaked-eth','tbtc','m-by-m0','ondo-us-dollar-yield','staked-frax-ether','stader-ethx','frax-ether','rocket-pool-eth','sky-dollar']);

function isStable(c) {
  if (STABLE_IDS.has(c.id)) return true;
  const sym = (c.symbol||'').toUpperCase();
  const name = (c.name||'').toLowerCase();
  if (sym.startsWith('USD')||sym.startsWith('EUR')||sym.startsWith('GBP')) return true;
  if (name.includes('stablecoin')||name.includes('stable coin')) return true;
  const p = c.current_price||0;
  if (p>=0.97 && p<=1.03 && Math.abs(c.price_change_percentage_24h||0)<0.5 && (c.market_cap_rank||9999)<=200) return true;
  return false;
}

const filtered = markets.filter(c => !isStable(c) && !WRAPPED_IDS.has(c.id) && (c.total_volume||0)>=1_000_000 && c.price_change_percentage_24h != null);

const trendingIds = new Set();
const trendingSyms = new Set();
for (const t of (trending.coins||[])) {
  const item = t.item||{};
  trendingIds.add(item.id);
  trendingSyms.add((item.symbol||'').toLowerCase());
}

function tagsFor(c, inTrending, listName) {
  const tags = [];
  const p24 = c.price_change_percentage_24h||0;
  const p7d = c.price_change_percentage_7d_in_currency||0;
  const rank = c.market_cap_rank||9999;
  const mcap = c.market_cap||0;
  const vol = c.total_volume||0;
  const volMcap = mcap>0 ? vol/mcap : 0;
  if (inTrending && listName==='win') tags.push('TRENDING+UP');
  if (inTrending && listName==='lose') tags.push('TRENDING+DOWN');
  if (p24>15 && p7d>25) tags.push('BREAKOUT');
  if (p24>20 && p7d<0) tags.push('FADE');
  if (p24<-10 && volMcap>0.25) tags.push('CAPITULATION');
  if (rank>150 && p24>30) tags.push('PUMP-RISK');
  if (mcap < 50_000_000) tags.push('MICROCAP');
  if (rank<=20) tags.push('MAJOR');
  return tags.slice(0,2);
}

const winners = [...filtered].sort((a,b)=> (b.price_change_percentage_24h||0)-(a.price_change_percentage_24h||0)).slice(0,10);
const losers = [...filtered].sort((a,b)=> (a.price_change_percentage_24h||0)-(b.price_change_percentage_24h||0)).slice(0,10);

const top100 = filtered.slice(0,100);
const green = top100.filter(c=>(c.price_change_percentage_24h||0)>0).length;
const top50ch = filtered.slice(0,50).map(c=>c.price_change_percentage_24h||0).sort((a,b)=>a-b);
const median = top50ch.length ? top50ch[Math.floor(top50ch.length/2)] : 0;

function fmtPrice(p){
  if (p==null) return '?';
  if (p>=1000) return '$'+p.toLocaleString(undefined,{maximumFractionDigits:0});
  if (p>=1) return '$'+p.toFixed(2);
  if (p>=0.01) return '$'+p.toFixed(4);
  if (p>=0.0001) return '$'+p.toFixed(6);
  return '$'+p.toFixed(8);
}
function fmtAbbr(v){
  if (v==null) return '?';
  if (v>=1e9) return '$'+(v/1e9).toFixed(1)+'B';
  if (v>=1e6) return '$'+(v/1e6).toFixed(0)+'M';
  if (v>=1e3) return '$'+(v/1e3).toFixed(0)+'K';
  return '$'+v.toFixed(0);
}

function render(c, listName){
  const inTrending = trendingIds.has(c.id) || trendingSyms.has((c.symbol||'').toLowerCase());
  const tg = tagsFor(c, inTrending, listName);
  return {
    symbol: (c.symbol||'').toUpperCase(),
    name: c.name,
    id: c.id,
    price: fmtPrice(c.current_price),
    p24: c.price_change_percentage_24h||0,
    p7d: c.price_change_percentage_7d_in_currency||0,
    p1h: c.price_change_percentage_1h_in_currency||0,
    vol: fmtAbbr(c.total_volume),
    rank: c.market_cap_rank,
    tags: tg,
  };
}

const winnersR = winners.map(c=>render(c,'win'));
const losersR = losers.map(c=>render(c,'lose'));

console.log(`PULSE: ${green}/100 top-100 green, median_top50=${median.toFixed(2)}%`);
console.log('\n=== WINNERS ===');
for (const w of winnersR) {
  const tg = w.tags.length ? ` [${w.tags.join('/')}]` : '';
  console.log(`  ${w.symbol} (${w.name}) — ${w.price}  ${w.p24>=0?'+':''}${w.p24.toFixed(1)}% / 7d ${w.p7d>=0?'+':''}${w.p7d.toFixed(1)}% / 1h ${w.p1h>=0?'+':''}${w.p1h.toFixed(1)}%  •  ${w.vol} / #${w.rank}${tg}`);
}
console.log('\n=== LOSERS ===');
for (const l of losersR) {
  const tg = l.tags.length ? ` [${l.tags.join('/')}]` : '';
  console.log(`  ${l.symbol} (${l.name}) — ${l.price}  ${l.p24>=0?'+':''}${l.p24.toFixed(1)}% / 7d ${l.p7d>=0?'+':''}${l.p7d.toFixed(1)}% / 1h ${l.p1h>=0?'+':''}${l.p1h.toFixed(1)}%  •  ${l.vol} / #${l.rank}${tg}`);
}

console.log('\n=== TRENDING ===');
const trendingItems = (trending.coins||[]).slice(0,7).map(t=>{
  const item = t.item||{};
  const data = item.data||{};
  return {
    symbol: (item.symbol||'').toUpperCase(),
    name: item.name,
    id: item.id,
    rank: item.market_cap_rank,
    price: fmtPrice(data.price),
    change_24h: (data.price_change_percentage_24h||{}).usd,
  };
});
for (const t of trendingItems) {
  const ch = t.change_24h;
  const chs = ch!=null ? `${ch>=0?'+':''}${ch.toFixed(1)}%` : '?';
  const inWin = winnersR.some(w=>w.symbol===t.symbol);
  const inLose = losersR.some(l=>l.symbol===t.symbol);
  const ex = [];
  if (inWin) ex.push('TRENDING+UP');
  if (inLose) ex.push('TRENDING+DOWN');
  const tg = ex.length ? ` [${ex.join('/')}]` : '';
  console.log(`  ${t.symbol} (${t.name}) — #${t.rank}, ${t.price}, 24h ${chs}${tg}`);
}

fs.writeFileSync('.cg-cache/results.json', JSON.stringify({
  pulse:{green100:green, median_top50:median},
  winners:winnersR,
  losers:losersR,
  trending:trendingItems,
}, null, 2));
console.log('\nSaved .cg-cache/results.json');
