import { NextResponse } from 'next/server'
import { readFile } from 'fs/promises'
import { join, resolve } from 'path'
import { parsePlan, parsePod, parseVotes, buildDataset, type SwarmData, type SwarmSource } from '@/lib/swarm'
import { SWARM_SNAPSHOT } from '@/lib/swarm-snapshot'

/**
 * Hybrid loader for the Reppo swarm demo: read the live artifacts the chain
 * leaves at the repo root and, per-section, fall back to the curated snapshot
 * whenever a file is missing or unparseable. Always returns a complete, well-
 * shaped `SwarmData` so the demo never renders a blank section, plus a
 * `source` flag ("live" | "snapshot" | "mixed") the UI surfaces honestly.
 *
 * `process.cwd()` is the `dashboard/` dir under `next dev`; the artifacts live
 * one level up — same `resolve(cwd, '..')` convention as `/api/outputs`.
 */
const REPO_ROOT = resolve(process.cwd(), '..')

async function readText(rel: string): Promise<string | null> {
  try {
    return await readFile(join(REPO_ROOT, rel), 'utf-8')
  } catch {
    return null
  }
}

async function readJson(rel: string): Promise<unknown | null> {
  const txt = await readText(rel)
  if (!txt) return null
  try {
    return JSON.parse(txt)
  } catch {
    return null
  }
}

export async function GET() {
  const snap = SWARM_SNAPSHOT
  let anyLive = false
  let anySnapshot = false
  const mark = (live: boolean) => {
    if (live) anyLive = true
    else anySnapshot = true
  }

  // --- plan (orchestrator) ---
  const orchMd = await readText('.outputs/reppo-orchestrator.md')
  const livePlan = orchMd ? parsePlan(orchMd) : null
  mark(!!livePlan)
  const plan = livePlan ?? snap.plan

  // --- pod + votes (trading-agent execution results) ---
  const taMd = await readText('.outputs/reppo-trading-agent.md')
  const livePod = taMd ? parsePod(taMd, snap.datanet.id) : null
  const liveVotes = taMd ? parseVotes(taMd) : null
  mark(!!livePod)
  mark(!!liveVotes)
  // Keep the live tx/CID/status, but prefer the snapshot's richer pod title
  // when the parser only recovered the generic fallback name.
  const pod = livePod
    ? { ...livePod, name: livePod.name.startsWith('HL perp trades — datanet') ? snap.pod.name : livePod.name }
    : snap.pod
  // Live votes carry status/tx but not the human reason; borrow reasons from
  // the snapshot by podId when available so the panel still explains itself.
  const votes = liveVotes
    ? liveVotes.map((v) => ({ ...v, reason: v.reason || snap.votes.find((s) => s.podId === v.podId)?.reason || '' }))
    : snap.votes

  // --- trader + dataset (both from the winning wallet's actual fills) ---
  // We intentionally do NOT rank the live leaderboard here: that cache is a
  // different-time prefetch than the run that produced these fills, so naively
  // ranking it surfaces an incoherent trader. The dataset's own fills give a
  // margin (pnl / traded-volume) consistent with the trades shown.
  const fills = await readJson(`.hl-cache/user-fills-${snap.trader.address}.json`)
  const built = fills ? buildDataset(fills) : null
  mark(!!built)

  const trader = built
    ? {
        ...snap.trader,
        pnl: built.sumPnl,
        vlm: built.tradedVlm,
        margin: built.margin,
        totalFills: built.totalFills,
        closedTrades: built.closedTrades,
      }
    : snap.trader

  const dataset = built
    ? {
        ...snap.dataset,
        winRate: built.winRate,
        maxDrawdownUsd: built.maxDrawdownUsd,
        maxDrawdownPct: built.maxDrawdownPct,
        sumPnl: built.sumPnl,
        closedTrades: built.closedTrades,
        trades: built.trades.length ? built.trades : snap.dataset.trades,
        // Sharpe needs a per-trade return series we don't recompute here; keep
        // the snapshot's verified figure rather than emit a wrong number.
        sharpe: snap.dataset.sharpe,
      }
    : snap.dataset

  const source: SwarmSource = anyLive && anySnapshot ? 'mixed' : anyLive ? 'live' : 'snapshot'

  const data: SwarmData = {
    ...snap,
    source,
    generatedAt: new Date().toISOString(),
    plan,
    trader,
    dataset,
    pod,
    votes,
  }

  return NextResponse.json(data, { headers: { 'Cache-Control': 'no-store' } })
}
