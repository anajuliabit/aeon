/**
 * Reppo Swarm demo — shared types + live-file parsers.
 *
 * The swarm is a 3-skill chain run on GitHub Actions:
 *   reppo-orchestrator  → decides RUN/SKIP per datanet, discovers new ones
 *   reppo-trading-agent → builds a labeled HL perp trade-dataset, writes intents
 *   postprocess-reppo   → mints the pod on Base, pins dataset to IPFS, votes
 *
 * The dashboard reads the artifacts those steps leave on disk (`.outputs/*.md`,
 * `.hl-cache/*.json`) and, for anything missing or unparseable, falls back to a
 * curated snapshot of the real 2026-05-31 run (see `swarm-snapshot.ts`). This
 * file owns the shapes both paths produce and the regex/JSON parsers for the
 * live path. Parsers are intentionally defensive: any failure returns `null`
 * and the caller substitutes the snapshot section.
 */

export type SwarmSource = 'live' | 'snapshot' | 'mixed'

export interface SwarmPlan {
  agent: string
  decision: 'RUN' | 'SKIP'
  reason: string
  newDatanets: number[]
  catalogSize: number
}

export interface SwarmTrader {
  address: string
  rank: number
  window: string
  pnl: number
  vlm: number
  /** margin = pnl / vlm — the ranking metric that surfaces directional alpha. */
  margin: number
  accountValue: number
  totalFills: number
  closedTrades: number
  markets: string[]
  spanDays: number
}

export interface SwarmTrade {
  market: string
  direction: 'long' | 'short'
  size: number
  price: number
  pnl: number
  win: boolean
  signal: string
  context: string
  ts: number
  hash: string
}

export interface SwarmDataset {
  winRate: number
  sharpe: number
  maxDrawdownUsd: number
  maxDrawdownPct: number
  sumPnl: number
  closedTrades: number
  ohlcvInterval: string
  signalTaxonomy: Record<string, string>
  trades: SwarmTrade[]
}

export interface SwarmPod {
  name: string
  datanet: number
  chain: string
  txHash: string
  ipfsCid: string
  gateway: string
  status: 'minted' | 'pending' | 'failed'
}

export interface SwarmVote {
  podId: string
  direction: 'like' | 'dislike'
  status: 'success' | 'rejected' | 'pending'
  reason: string
  txHash?: string
  rejectCode?: string
}

export interface SwarmData {
  source: SwarmSource
  generatedAt: string
  runDate: string
  datanet: { id: number; name: string; accessFee: string }
  plan: SwarmPlan
  trader: SwarmTrader
  dataset: SwarmDataset
  pod: SwarmPod
  votes: SwarmVote[]
}

/** The six narration beats, kept here so page + pipeline agree on order. */
export const STAGES = [
  { key: 'plan', lane: 'orchestrator', title: 'Wake & plan', blurb: 'Read datanet state, decide RUN/SKIP' },
  { key: 'rank', lane: 'trading-agent', title: 'Rank leaderboard', blurb: 'Sort by margin = pnl / vlm' },
  { key: 'fills', lane: 'trading-agent', title: 'Pull 7d fills', blurb: 'Fetch the trader’s recent executions' },
  { key: 'label', lane: 'trading-agent', title: 'Label & score', blurb: 'Join OHLCV → win-rate, Sharpe, MDD' },
  { key: 'mint', lane: 'postprocess', title: 'Mint pod', blurb: 'ERC-721 on Base + pin to IPFS' },
  { key: 'vote', lane: 'postprocess', title: 'Vote', blurb: 'Dislike off-rubric raw dumps' },
] as const

export type StageKey = (typeof STAGES)[number]['key']
export const LANES = ['orchestrator', 'trading-agent', 'postprocess'] as const
export type Lane = (typeof LANES)[number]

// ---------------------------------------------------------------------------
// Live-file parsers. Each takes raw file text/JSON and returns a section, or
// null on any failure so the API can fall back to the snapshot per-section.
// ---------------------------------------------------------------------------

/**
 * Parse the orchestrator's fenced `reppo-plan` block out of its markdown
 * output. Shape (verbatim from the skill's output contract):
 *   reppo-plan
 *   reppo-trading-agent: RUN   (reason…)
 *   new-datanet: 1    (no rubric / no agent assigned)
 */
export function parsePlan(md: string): SwarmPlan | null {
  try {
    const block = md.match(/```[^\n]*\n(reppo-plan[\s\S]*?)```/)?.[1]
    if (!block) return null
    const agentLine = block.match(/^([\w-]+):\s*(RUN|SKIP)\s*\(([^)]*)\)/m)
    if (!agentLine) return null
    const newDatanets = [...block.matchAll(/^new-datanet:\s*(\d+)/gm)].map((m) => Number(m[1]))
    // Catalog size is reported in the prose, e.g. "Catalog available (15 datanets)".
    const catalogSize = Number(
      md.match(/(\d+)\s+active\s+datanets|catalog available \((\d+)/i)?.slice(1).find(Boolean) ?? 0,
    )
    return {
      agent: agentLine[1],
      decision: agentLine[2] as 'RUN' | 'SKIP',
      reason: agentLine[3].trim(),
      newDatanets,
      catalogSize: catalogSize || newDatanets.length + 1,
    }
  } catch {
    return null
  }
}

/**
 * Pull mint tx + IPFS pin + status out of the trading-agent's
 * `## Execution Results` section (written by postprocess-reppo.sh).
 */
export function parsePod(md: string, datanetId: number): SwarmPod | null {
  try {
    const tx = md.match(/mint-[0-9a-f]+\.json`?\s*—\s*\*\*success\*\*\s*\(tx:\s*(0x[0-9a-fA-F]+)/)?.[1]
    const cid = md.match(/ipfs:\/\/([A-Za-z0-9]+)/)?.[1]
    if (!tx && !cid) return null
    const name = md.match(/HL perps[^\n"]*/)?.[0]?.trim()
    return {
      name: name || `HL perp trades — datanet ${datanetId}`,
      datanet: datanetId,
      chain: 'Base',
      txHash: tx || '',
      ipfsCid: cid || '',
      gateway: cid ? `https://ipfs.io/ipfs/${cid}` : '',
      status: tx ? 'minted' : 'pending',
    }
  } catch {
    return null
  }
}

/**
 * Parse the vote outcomes from `## Execution Results`. Lines look like:
 *   `vote-466-dislike.json` — **success** (tx: 0x…)
 *   `vote-462-like.json` — **dry-run failed** (code: CANNOT_VOTE_FOR_OWN_POD), …
 */
export function parseVotes(md: string): SwarmVote[] | null {
  try {
    const votes: SwarmVote[] = []
    const re = /`?vote-([\w]+)-(like|dislike)\.json`?\s*—\s*\*\*([^*]+)\*\*\s*\(([^)]*)\)/g
    for (const m of md.matchAll(re)) {
      const [, podId, dir, statusRaw, detail] = m
      const ok = /success/i.test(statusRaw)
      votes.push({
        podId,
        direction: dir as 'like' | 'dislike',
        status: ok ? 'success' : 'rejected',
        reason: '',
        txHash: ok ? detail.match(/0x[0-9a-fA-F]+/)?.[0] : undefined,
        rejectCode: ok ? undefined : detail.match(/code:\s*([A-Z_]+)/)?.[1],
      })
    }
    return votes.length ? votes : null
  } catch {
    return null
  }
}

interface LeaderboardRow {
  ethAddress: string
  accountValue: string
  displayName: string | null
  windowPerformances: [string, { pnl: string; roi: string; vlm: string }][]
}

/**
 * Rank leaderboard rows by margin (pnl / vlm) in the given window and return
 * the top directional trader. This is the orchestrator's alpha thesis: raw PnL
 * favors market makers churning volume; margin surfaces real directional edge.
 */
export function rankTopTrader(
  raw: unknown,
  window = 'week',
  preferAddress?: string,
): Omit<SwarmTrader, 'totalFills' | 'closedTrades' | 'markets' | 'spanDays'> | null {
  try {
    const rows = (raw as { leaderboardRows?: LeaderboardRow[] })?.leaderboardRows
    if (!Array.isArray(rows) || !rows.length) return null
    const scored = rows
      .map((r) => {
        const w = r.windowPerformances?.find(([k]) => k === window)?.[1]
        if (!w) return null
        const pnl = Number(w.pnl)
        const vlm = Number(w.vlm)
        if (!vlm || vlm <= 0) return null
        return {
          address: r.ethAddress,
          pnl,
          vlm,
          margin: pnl / vlm,
          accountValue: Number(r.accountValue),
        }
      })
      .filter((x): x is NonNullable<typeof x> => x != null && x.pnl > 0)
      .sort((a, b) => b.margin - a.margin)
    if (!scored.length) return null
    // The real run pinned a specific wallet; honor it if present so the live
    // ranking and the trades table describe the same trader.
    const idx = preferAddress ? scored.findIndex((s) => s.address.toLowerCase() === preferAddress.toLowerCase()) : -1
    const pick = idx >= 0 ? scored[idx] : scored[0]
    return { ...pick, rank: (idx >= 0 ? idx : 0) + 1, window }
  } catch {
    return null
  }
}

interface RawFill {
  coin: string
  px: string
  sz: string
  side: 'B' | 'A'
  dir?: string
  closedPnl: string
  time: number
  hash: string
}

/** A coarse market-context label from a fill's PnL sign and coin, used only
 * for the demo table when no OHLCV join is available live. The real skill
 * derives this from candles; we keep it deterministic and clearly labeled. */
function contextFor(coin: string, win: boolean): string {
  if (coin === 'BTC' || coin === 'ETH') return win ? 'trending-up' : 'ranging'
  return win ? 'breakout' : 'high-volatility'
}

/**
 * Build the trades table + aggregate stats from a wallet's raw HL fills.
 * Also returns `tradedVlm` (Σ|sz·px| over every fill) and `margin` so the
 * trader card can show a margin that is coherent with this exact dataset,
 * rather than a different-time leaderboard snapshot.
 */
export function buildDataset(
  rawFills: unknown,
  limit = 16,
): (Omit<SwarmDataset, 'signalTaxonomy' | 'ohlcvInterval' | 'sharpe'> & {
  totalFills: number
  tradedVlm: number
  margin: number
}) | null {
  try {
    const fills = rawFills as RawFill[]
    if (!Array.isArray(fills) || !fills.length) return null
    const closed = fills.filter((f) => Number(f.closedPnl) !== 0)
    if (closed.length < 1) return null
    const wins = closed.filter((f) => Number(f.closedPnl) > 0).length
    const sumPnl = closed.reduce((a, f) => a + Number(f.closedPnl), 0)
    const tradedVlm = fills.reduce((a, f) => a + Math.abs(Number(f.sz) * Number(f.px)), 0)
    // Max drawdown on the cumulative-PnL curve.
    let peak = 0
    let cum = 0
    let maxDd = 0
    for (const f of closed) {
      cum += Number(f.closedPnl)
      peak = Math.max(peak, cum)
      maxDd = Math.max(maxDd, peak - cum)
    }
    const trades: SwarmTrade[] = closed.slice(0, limit).map((f) => {
      const pnl = Number(f.closedPnl)
      const win = pnl > 0
      const direction: 'long' | 'short' = (f.dir || '').includes('Short') ? 'short' : 'long'
      const market = f.coin.replace('xyz:', '')
      return {
        market,
        direction,
        size: Number(f.sz),
        price: Number(f.px),
        pnl: Math.round(pnl * 100) / 100,
        win,
        signal: win ? 'mean-reversion' : 'breakout-fade',
        context: contextFor(market, win),
        ts: f.time,
        hash: f.hash.slice(0, 14) + '…',
      }
    })
    return {
      winRate: Math.round((wins / closed.length) * 10000) / 100,
      maxDrawdownUsd: Math.round(maxDd),
      maxDrawdownPct: peak > 0 ? Math.round((maxDd / peak) * 1000) / 10 : 0,
      sumPnl: Math.round(sumPnl),
      closedTrades: closed.length,
      totalFills: fills.length,
      tradedVlm: Math.round(tradedVlm),
      margin: tradedVlm > 0 ? sumPnl / tradedVlm : 0,
      trades,
    }
  } catch {
    return null
  }
}
