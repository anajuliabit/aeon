const fs = require('fs');
const markets = JSON.parse(fs.readFileSync('.hl-cache/cg-markets.json', 'utf8'));
const trendingRaw = JSON.parse(fs.readFileSync('.hl-cache/cg-trending.json', 'utf8'));

const stableIds = new Set(['tether','usd-coin','dai','first-digital-usd','ethena-usde','usde','true-usd','tusd','usdd','pax-dollar','frax','susd','paypal-usd','pyusd','fdusd','paxg','wrapped-steth','wrapped-bitcoin','wrapped-eth','staked-ether','rocket-pool-eth','liquid-staked-ethereum','ether-fi-staked-eth','jito-staked-sol','wsteth','crvusd','lusd','gusd','usdt','tronusdt','first-digital-usd','aave-usd-coin','ondo-us-dollar-yield','aave-usdt','aave-dai','aave-usdc']);

const usdSyms = /^(usd|eur|gbp|jpy|cny|brl|aud|chf|cad|krw|hkd)/i;

function isStable(c) {
  if (stableIds.has(c.id)) return true;
  if (usdSyms.test(c.symbol)) return true;
  if (/stablecoin/i.test(c.name)) return true;
  if (/wrapped|staked|liquid/i.test(c.name)) return true;
  return false;
}

const filtered = markets.filter(c => {
  if (isStable(c)) return false;
  if (!c.total_volume || c.total_volume < 1_000_000) return false;
  if (c.price_change_percentage_24h == null) return false;
  return true;
});

function tag(c, trendingSyms) {
  const tags = [];
  const sym = c.symbol.toUpperCase();
  const ch24 = c.price_change_percentage_24h || 0;
  const ch7d = c.price_change_percentage_7d_in_currency || 0;
  const rank = c.market_cap_rank || 999;
  const mcap = c.market_cap || 0;
  const volRatio = mcap > 0 ? c.total_volume / mcap : 0;
  const inTrending = trendingSyms.has(sym);
  if (inTrending && ch24 > 5) tags.push('TRENDING+UP');
  if (inTrending && ch24 < -5) tags.push('TRENDING+DOWN');
  if (ch24 > 15 && ch7d > 25) tags.push('BREAKOUT');
  if (ch24 > 20 && ch7d < 0) tags.push('FADE');
  if (ch24 < -10 && volRatio > 0.25) tags.push('CAPITULATION');
  if (rank > 150 && ch24 > 30) tags.push('PUMP-RISK');
  if (mcap < 50_000_000) tags.push('MICROCAP');
  if (rank <= 20) tags.push('MAJOR');
  return tags.slice(0, 2);
}

const trendingItems = (trendingRaw.coins || []).map(x => x.item);
const trendingSyms = new Set(trendingItems.map(t => (t.symbol || '').toUpperCase()));

const sorted24 = [...filtered].sort((a,b) => b.price_change_percentage_24h - a.price_change_percentage_24h);
const winners = sorted24.slice(0, 12);
const losers = [...sorted24].reverse().slice(0, 12);

// market pulse
const top100 = filtered.slice(0, 100);
const greenCount = top100.filter(c => c.price_change_percentage_24h > 0).length;
const top50 = filtered.slice(0, 50);
const ch24Sorted = [...top50].map(c => c.price_change_percentage_24h).sort((a,b)=>a-b);
const median50 = ch24Sorted[Math.floor(ch24Sorted.length/2)];

function fmt(c) {
  const ch24 = c.price_change_percentage_24h?.toFixed(1);
  const ch7d = c.price_change_percentage_7d_in_currency?.toFixed(1) ?? 'n/a';
  const ch1h = c.price_change_percentage_1h_in_currency?.toFixed(1) ?? 'n/a';
  const price = c.current_price < 0.01 ? c.current_price.toPrecision(3) : c.current_price < 1 ? c.current_price.toFixed(4) : c.current_price.toFixed(2);
  const vol = (c.total_volume/1e6).toFixed(0) + 'M';
  return { sym: c.symbol.toUpperCase(), name: c.name, price, ch24, ch7d, ch1h, vol, rank: c.market_cap_rank, mcap: c.market_cap };
}

const tagsFor = c => tag(c, trendingSyms);

const out = {
  pulse: { greenCount, median50: median50?.toFixed(1) },
  winners: winners.map(c => ({...fmt(c), tags: tagsFor(c)})),
  losers: losers.map(c => ({...fmt(c), tags: tagsFor(c)})),
  trending: trendingItems.slice(0, 8).map(t => ({
    sym: (t.symbol || '').toUpperCase(),
    name: t.name,
    rank: t.market_cap_rank,
    price_btc: t.price_btc,
    data: t.data,
  })),
};

fs.writeFileSync('.hl-cache/movers-out.json', JSON.stringify(out, null, 2));
console.log(JSON.stringify({pulse: out.pulse, winners_top: out.winners.slice(0, 12).map(w => `${w.sym} ${w.ch24}% 7d=${w.ch7d}% rank=${w.rank} vol=${w.vol} tags=${w.tags.join(',')}`), losers_top: out.losers.slice(0, 12).map(w => `${w.sym} ${w.ch24}% 7d=${w.ch7d}% rank=${w.rank} vol=${w.vol} tags=${w.tags.join(',')}`), trending: out.trending.map(t => `${t.sym} rank=${t.rank} 24h=${t.data?.price_change_percentage_24h?.usd?.toFixed(1)}%`)}, null, 2));
