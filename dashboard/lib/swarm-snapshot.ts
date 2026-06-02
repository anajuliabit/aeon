import type { SwarmData } from './swarm'

/**
 * Curated snapshot of the real Reppo swarm run on 2026-05-31 (chain
 * `reppo-swarm`, datanet 9 / TradingGymAI). Every value here is taken from the
 * actual artifacts that run produced:
 *   - plan          → `.outputs/reppo-orchestrator.md`
 *   - trader/dataset→ `.hl-cache/leaderboard.json` + the winning wallet's
 *                      `user-fills-0x9a15…json` (45 closed perp fills)
 *   - pod/votes     → `.outputs/reppo-trading-agent.md` (## Execution Results):
 *                       mint tx 0xccba0d07…, pinned ipfs://Qme9oiYw8…,
 *                       votes 466/467 DISLIKE (success), 462 LIKE (rejected,
 *                       CANNOT_VOTE_FOR_OWN_POD).
 *
 * It is the demo-safe fallback: the API serves it whenever a live file is
 * missing or unparseable, so the screen is never blank mid-demo. The trades
 * below are real closing fills from the winning wallet.
 */
export const SWARM_SNAPSHOT: SwarmData = {
  source: 'snapshot',
  generatedAt: '2026-05-31T08:21:57Z',
  runDate: '2026-05-31',
  datanet: { id: 9, name: 'TradingGymAI', accessFee: '50 REPPO' },
  plan: {
    agent: 'reppo-trading-agent',
    decision: 'RUN',
    reason:
      'datanet 9 tradinggymai, valid=true, accessFee 50 REPPO — re-run is safe (content-hash dedup + idempotency keys)',
    newDatanets: [1, 2, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17],
    catalogSize: 15,
  },
  trader: {
    address: '0x9a1500b41519868039b1f95c447ba50b76d837e6',
    rank: 1,
    window: 'week',
    pnl: 1140,
    vlm: 99830,
    margin: 0.011424,
    accountValue: 18420,
    totalFills: 87,
    closedTrades: 45,
    markets: ['BTC', 'HYPE', 'NEAR', 'ONDO', 'PENGU', 'ORCL', 'SPCX'],
    spanDays: 5.38,
  },
  dataset: {
    winRate: 26.67,
    sharpe: 9.98,
    maxDrawdownUsd: 1958,
    maxDrawdownPct: 171.7,
    sumPnl: 1140,
    closedTrades: 45,
    ohlcvInterval: '1h',
    signalTaxonomy: {
      'mean-reversion': 'entry near swing low after ATR spike',
      'breakout-fade': 'entry against the prevailing 20-bar trend',
    },
    trades: [
      { market: 'SPCX', direction: 'long', size: 5.99, price: 200.6, pnl: -47.2, win: false, signal: 'breakout-fade', context: 'high-volatility', ts: 1779465982424, hash: '0xf4fa1df57d65…' },
      { market: 'BTC', direction: 'long', size: 0.03229, price: 76280, pnl: -72.01, win: false, signal: 'breakout-fade', context: 'ranging', ts: 1779475537143, hash: '0x1f399e282fb5…' },
      { market: 'BTC', direction: 'long', size: 0.06442, price: 75824, pnl: -173.04, win: false, signal: 'breakout-fade', context: 'ranging', ts: 1779478237718, hash: '0x33f4a94fdc4a…' },
      { market: 'BTC', direction: 'long', size: 0.12807, price: 75819, pnl: -344.65, win: false, signal: 'breakout-fade', context: 'ranging', ts: 1779478237718, hash: '0x33f4a94fdc4a…' },
      { market: 'PENGU', direction: 'long', size: 3282, price: 0.008936, pnl: -2.85, win: false, signal: 'breakout-fade', context: 'high-volatility', ts: 1779488937413, hash: '0xf359890ab7d0…' },
      { market: 'PENGU', direction: 'long', size: 251741, price: 0.008936, pnl: -218.26, win: false, signal: 'breakout-fade', context: 'high-volatility', ts: 1779488937413, hash: '0xf359890ab7d0…' },
      { market: 'NEAR', direction: 'long', size: 453.9, price: 2.0386, pnl: 69.17, win: true, signal: 'mean-reversion', context: 'breakout', ts: 1779521148816, hash: '0x92ee24f96a38…' },
      { market: 'NEAR', direction: 'long', size: 133.5, price: 2.0386, pnl: 20.35, win: true, signal: 'mean-reversion', context: 'breakout', ts: 1779521148816, hash: '0x92ee24f96a38…' },
      { market: 'BTC', direction: 'long', size: 0.02917, price: 74583, pnl: -114.55, win: false, signal: 'breakout-fade', context: 'ranging', ts: 1779522633875, hash: '0x523b245f067b…' },
      { market: 'ONDO', direction: 'long', size: 1840, price: 0.612, pnl: 412.6, win: true, signal: 'mean-reversion', context: 'breakout', ts: 1779598411902, hash: '0x8a71b0c4d219…' },
      { market: 'HYPE', direction: 'short', size: 92.4, price: 31.18, pnl: 588.1, win: true, signal: 'mean-reversion', context: 'trending-up', ts: 1779655120773, hash: '0x4c9f2ea7b6d8…' },
      { market: 'SPCX', direction: 'long', size: 2.03, price: 205.67, pnl: -1.79, win: false, signal: 'breakout-fade', context: 'high-volatility', ts: 1779782800356, hash: '0xe79548c5aab0…' },
    ],
  },
  pod: {
    name: 'HL perps 7d, 0x9a15..37e6: 45 trades',
    datanet: 9,
    chain: 'Base',
    txHash: '0xccba0d07341811173d8e03ae1598e84d05878da67ae9d46a1bd28f7d134b6e4a',
    ipfsCid: 'Qme9oiYw8TvutJY1AWXkdyRg7V7m3FJmbku8AwRneoiRkx',
    gateway: 'https://ipfs.io/ipfs/Qme9oiYw8TvutJY1AWXkdyRg7V7m3FJmbku8AwRneoiRkx',
    status: 'minted',
  },
  votes: [
    { podId: '467', direction: 'dislike', status: 'success', reason: 'HotBot v4 raw export — off-rubric, unlabeled dump', txHash: '0x031510e9749a3ca4a76f11909f92a8f575ee887eec94dbe9df9a8beddda148b6' },
    { podId: '466', direction: 'dislike', status: 'success', reason: 'HotBot v4 raw export — off-rubric, unlabeled dump', txHash: '0xf7f5c37c2e642315ebd0fc3a96966857ca4aa5bf76044c4d633608f0c91e081d' },
    { podId: '462', direction: 'like', status: 'rejected', reason: 'rubric-compliant — but it is our own mint', rejectCode: 'CANNOT_VOTE_FOR_OWN_POD' },
  ],
}
