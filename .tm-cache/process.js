const fs = require('fs');
const m = JSON.parse(fs.readFileSync('.tm-cache/cg-markets.json','utf8'));
const t = JSON.parse(fs.readFileSync('.tm-cache/cg-trending.json','utf8'));

console.log("markets count:", m.length);
console.log("trending count:", (t.coins||[]).length);

const STABLE = new Set(['tether','usd-coin','dai','first-digital-usd','usde','ethena-usde','tusd','true-usd',
  'usdd','pyusd','paypal-usd','fdusd','paxos-standard','paxg','pax-gold','usds','sky-dollar','binance-usd',
  'frax','usdt0','blackrock-usd','ethena-staked-usde','usdtb','susds','susde','ondo-us-dollar-yield',
  'global-dollar','falcon-finance','resolv-usr','binance-bridged-usdt-bnb-smart-chain','usdb','meta-usd']);
const WRAPPED = new Set(['wrapped-bitcoin','weth','wrapped-steth','staked-ether','wrapped-beacon-eth',
  'coinbase-wrapped-btc','wrapped-eeth','rocket-pool-eth','mantle-staked-ether','renzo-restaked-eth',
  'kelp-dao-restaked-eth','lombard-staked-btc','solv-btc','jupiter-staked-sol','binance-staked-sol','msol',
  'jito-staked-sol','liquid-staked-ethereum','bridged-wrapped-steth-scroll','wrapped-eth','wbeth',
  'ether-fi-staked-eth','wrapped-avax','tbtc','clbtc']);

function isStable(c){
  const sym=(c.symbol||'').toUpperCase(), name=(c.name||'').toLowerCase(), id=c.id||'';
  if(STABLE.has(id)) return true;
  if(name.includes('stablecoin')) return true;
  if(sym.startsWith('USD')||sym.startsWith('EUR')||sym.startsWith('GBP')) return true;
  const p=c.current_price||0, ch=c.price_change_percentage_24h;
  if(p>=0.95&&p<=1.05&&ch!=null&&Math.abs(ch)<0.5) return true;
  return false;
}

const filtered = m.filter(c=>{
  if(isStable(c)) return false;
  if(WRAPPED.has(c.id)) return false;
  if((c.total_volume||0)<1_000_000) return false;
  if(c.price_change_percentage_24h==null) return false;
  return true;
});
console.log("filtered survivors:", filtered.length);

const top100 = filtered.slice(0,100);
const green = top100.filter(c=>(c.price_change_percentage_24h||0)>0).length;
const top50 = filtered.slice(0,50).map(c=>c.price_change_percentage_24h||0).sort((a,b)=>a-b);
const med50 = top50.length%2 ? top50[(top50.length-1)/2] : (top50[top50.length/2-1]+top50[top50.length/2])/2;
const find=id=>m.find(c=>c.id===id);
const fmtMajor=c=>c?`${c.symbol.toUpperCase()} $${(c.current_price).toLocaleString('en-US',{maximumFractionDigits:0})} ${(c.price_change_percentage_24h||0).toFixed(1)}% / 7d ${(c.price_change_percentage_7d_in_currency||0).toFixed(1)}%`:'n/a';
console.log(`PULSE: ${green}/${top100.length} top-100 green, median top-50 24h ${med50>=0?'+':''}${med50.toFixed(2)}%`);
console.log("BTC:", fmtMajor(find('bitcoin')));
console.log("ETH:", fmtMajor(find('ethereum')));
console.log("SOL:", fmtMajor(find('solana')));

const by24=[...filtered].sort((a,b)=>(a.price_change_percentage_24h||0)-(b.price_change_percentage_24h||0));
const losers=by24.slice(0,10);
const winners=by24.slice(-10).reverse();

function capAbbr(v){if(v==null)return'n/a';if(v>=1e9)return'$'+(v/1e9).toFixed(1)+'B';if(v>=1e6)return'$'+(v/1e6).toFixed(0)+'M';return'$'+(v/1e3).toFixed(0)+'K';}
function priceFmt(p){if(p==null)return'n/a';if(p>=1)return'$'+Number(p.toPrecision(5)).toLocaleString('en-US');if(p>=0.01)return'$'+p.toFixed(4);return'$'+p.toFixed(6);}

const trendingSyms=new Set();
const trending=(t.coins||[]).slice(0,7).map(it=>{
  const d=it.item, sym=(d.symbol||'').toUpperCase();
  trendingSyms.add(sym);
  const data=d.data||{};
  const ch=(data.price_change_percentage_24h||{}).usd;
  return {name:d.name,sym,rank:d.market_cap_rank,price:data.price,ch24:ch};
});

function tags(c,isWinner){
  const out=[],sym=c.symbol.toUpperCase();
  const ch24=c.price_change_percentage_24h||0, ch7=c.price_change_percentage_7d_in_currency||0;
  const rank=c.market_cap_rank||9999, mcap=c.market_cap||0, vol=c.total_volume||0;
  const volmcap=mcap?vol/mcap:0, inTrend=trendingSyms.has(sym);
  if(inTrend&&ch24>0&&isWinner===true) out.push('TRENDING+UP');
  if(inTrend&&ch24<0&&isWinner===false) out.push('TRENDING+DOWN');
  if(ch24>15&&ch7>25) out.push('BREAKOUT');
  if(ch24>20&&ch7<0) out.push('FADE');
  if(ch24<-10&&volmcap>0.25) out.push('CAPITULATION');
  if(rank>150&&ch24>30) out.push('PUMP-RISK');
  if(mcap&&mcap<50_000_000) out.push('MICROCAP');
  if(rank<=20) out.push('MAJOR');
  return out.slice(0,2);
}
function show(c,isWinner){
  const sym=c.symbol.toUpperCase();
  const ch24=c.price_change_percentage_24h||0,ch7=c.price_change_percentage_7d_in_currency||0,ch1=c.price_change_percentage_1h_in_currency||0;
  return `${sym} (${c.name}) ${priceFmt(c.current_price)} ${ch24>=0?'+':''}${ch24.toFixed(1)}% / 7d ${ch7>=0?'+':''}${ch7.toFixed(1)}% / 1h ${ch1>=0?'+':''}${ch1.toFixed(1)}% • ${capAbbr(c.total_volume)} / #${c.market_cap_rank} ${JSON.stringify(tags(c,isWinner))}`;
}
console.log("\n=== WINNERS ===");
winners.forEach(c=>console.log(show(c,true)));
console.log("\n=== LOSERS ===");
losers.forEach(c=>console.log(show(c,false)));
console.log("\n=== TRENDING ===");
trending.forEach(tr=>console.log(`${tr.name} (${tr.sym}) #${tr.rank} ${priceFmt(tr.price)} 24h ${tr.ch24!=null?(tr.ch24>=0?'+':'')+tr.ch24.toFixed(1)+'%':'n/a'}`));
