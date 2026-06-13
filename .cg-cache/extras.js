const fs = require('fs');
const markets = JSON.parse(fs.readFileSync('.cg-cache/markets.json', 'utf8'));
const trending = JSON.parse(fs.readFileSync('.cg-cache/trending.json', 'utf8'));

const STABLE_IDS = new Set(['tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg','usds','ethena-usde','frax','usdt0','susds','ondo-us-dollar-yield','blackrock-usd-institutional-digital-liquidity-fund','sky-dollar','resolv-usr','falcon-usd','m0-foundation','tether-eurt','usdx-money-usdx','tether-gold','staked-frax','crypto-com-staked-eth','ethena-staked-usde','usdq','usd0','dola-usd','first-digital-labs-usd','usdtb']);
const WRAPPED_IDS = new Set(['wrapped-bitcoin','wrapped-steth','staked-ether','weth','wbeth','wrapped-eeth','rocket-pool-eth','coinbase-wrapped-btc','lombard-staked-btc','jito-staked-sol','binance-staked-sol','marinade-staked-sol','liquid-staked-ether','solv-protocol-solvbtc','renzo-restaked-eth','kelp-dao-restaked-eth','mantle-staked-ether','mantle-restaked-eth','tbtc','m-by-m0','ondo-us-dollar-yield','staked-frax-ether','stader-ethx','frax-ether','sky-dollar']);
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
const winners = [...filtered].sort((a,b)=> (b.price_change_percentage_24h||0)-(a.price_change_percentage_24h||0)).slice(0,20);
const losers = [...filtered].sort((a,b)=> (a.price_change_percentage_24h||0)-(b.price_change_percentage_24h||0)).slice(0,20);

console.log('--- WINNERS 1-20 ---');
winners.forEach((c,i)=>console.log(`${i+1}. ${c.symbol.toUpperCase()} ${c.name} #${c.market_cap_rank} 24h ${c.price_change_percentage_24h?.toFixed(1)}% 7d ${c.price_change_percentage_7d_in_currency?.toFixed(1)}% vol ${(c.total_volume/1e6).toFixed(1)}M mcap ${(c.market_cap/1e6).toFixed(0)}M`));
console.log('--- LOSERS 1-20 ---');
losers.forEach((c,i)=>console.log(`${i+1}. ${c.symbol.toUpperCase()} ${c.name} #${c.market_cap_rank} 24h ${c.price_change_percentage_24h?.toFixed(1)}% 7d ${c.price_change_percentage_7d_in_currency?.toFixed(1)}% vol ${(c.total_volume/1e6).toFixed(1)}M mcap ${(c.market_cap/1e6).toFixed(0)}M`));
