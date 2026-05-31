'use client'

import type { SwarmTrader } from '@/lib/swarm'

const short = (a: string) => `${a.slice(0, 6)}..${a.slice(-4)}`
const usd = (n: number) =>
  n >= 1_000_000 ? `$${(n / 1_000_000).toFixed(2)}M` : n >= 1000 ? `$${(n / 1000).toFixed(1)}k` : `$${n.toFixed(0)}`

/**
 * The chosen trader. Headline is the alpha thesis made concrete: ranked #1 by
 * margin (pnl/vlm), not raw PnL — that's what filters out market makers.
 */
export function TraderCard({ trader }: { trader: SwarmTrader }) {
  return (
    <div className="card-hst card-hst-orange p-[var(--space-lg)] h-full flex flex-col">
      <div className="flex items-center justify-between mb-[var(--space-md)]">
        <span className="text-label">Top directional trader</span>
        <span className="font-mono text-[11px] px-2 py-0.5 bg-eva-orange text-white tracking-[1.5px]">AGENT PICK</span>
      </div>

      <div className="font-mono text-lg mb-1 break-all">{short(trader.address)}</div>
      <div className="font-mono text-[11px] text-primary-40 mb-[var(--space-md)]">
        {trader.spanDays}d span · {trader.closedTrades} closed of {trader.totalFills} fills
      </div>

      {/* the margin call-out */}
      <div className="border-2 border-eva-orange p-[var(--space-md)] mb-[var(--space-md)]">
        <div className="flex items-baseline justify-between">
          <span className="text-label">margin = pnl / vlm</span>
          <span className="font-display text-2xl text-eva-orange">{(trader.margin * 100).toFixed(3)}%</span>
        </div>
        <div className="font-mono text-[11px] text-primary-50 mt-1.5">
          ranked by margin, not raw PnL — surfaces alpha over market-maker churn
        </div>
      </div>

      <div className="grid grid-cols-2 gap-px bg-[rgba(10,10,10,0.08)] mt-auto">
        <Stat label="realized pnl" value={`+${usd(trader.pnl)}`} green />
        <Stat label="traded vlm" value={usd(trader.vlm)} />
        <Stat label="total fills" value={String(trader.totalFills)} />
        <Stat label="closed trades" value={String(trader.closedTrades)} />
      </div>

      <div className="flex flex-wrap gap-1.5 mt-[var(--space-md)]">
        {trader.markets.map((m) => (
          <span key={m} className="font-mono text-[10px] tracking-[1px] px-2 py-1 border border-[rgba(10,10,10,0.15)]">
            {m}
          </span>
        ))}
      </div>
    </div>
  )
}

function Stat({ label, value, green }: { label: string; value: string; green?: boolean }) {
  return (
    <div className="bg-white p-[var(--space-md)]">
      <div className="text-label mb-1">{label}</div>
      <div className={`font-display text-xl ${green ? 'text-eva-green' : ''}`}>{value}</div>
    </div>
  )
}
