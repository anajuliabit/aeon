'use client'

import type { SwarmDataset } from '@/lib/swarm'

/**
 * The labeled trade-dataset: aggregate metrics on top, then a sample of the
 * labeled rows (signal + market context joined from OHLCV). The metric strip
 * tells the demo's sharpest story — 26.67% win-rate but 9.98 Sharpe means a
 * low hit-rate, high-asymmetry edge, exactly the directional alpha the margin
 * ranking was chasing.
 */
export function DatasetTable({ dataset }: { dataset: SwarmDataset }) {
  return (
    <div className="card-hst p-[var(--space-lg)] h-full flex flex-col">
      <div className="flex items-center justify-between mb-[var(--space-md)]">
        <span className="text-label">Labeled trade-dataset</span>
        <span className="font-mono text-[11px] text-primary-40">
          {dataset.closedTrades} closed · OHLCV {dataset.ohlcvInterval}
        </span>
      </div>

      {/* metric strip */}
      <div className="grid grid-cols-4 gap-px bg-[rgba(10,10,10,0.08)] mb-[var(--space-md)]">
        <Metric label="win rate" value={`${dataset.winRate}%`} />
        <Metric label="sharpe" value={dataset.sharpe.toFixed(2)} highlight />
        <Metric label="max dd" value={`${dataset.maxDrawdownPct}%`} red />
        <Metric label="sum pnl" value={`+$${dataset.sumPnl.toLocaleString()}`} green />
      </div>

      <p className="font-mono text-[11px] leading-snug text-primary-50 mb-[var(--space-md)] border-l-2 border-eva-orange pl-2.5">
        low hit-rate + high Sharpe = asymmetric directional edge, not a market maker
      </p>

      {/* labeled rows */}
      <div className="overflow-auto flex-1 -mx-1">
        <table className="w-full border-collapse font-mono text-[11px]">
          <thead>
            <tr className="text-label text-left">
              <th className="py-1.5 px-1.5 font-normal">mkt</th>
              <th className="py-1.5 px-1.5 font-normal">dir</th>
              <th className="py-1.5 px-1.5 font-normal">signal</th>
              <th className="py-1.5 px-1.5 font-normal">context</th>
              <th className="py-1.5 px-1.5 font-normal text-right">pnl</th>
              <th className="py-1.5 px-1.5 font-normal">tx</th>
            </tr>
          </thead>
          <tbody>
            {dataset.trades.map((t, i) => (
              <tr key={`${t.hash}-${i}`} className="border-t border-[rgba(10,10,10,0.06)]">
                <td className="py-1.5 px-1.5 font-bold">{t.market}</td>
                <td className="py-1.5 px-1.5">
                  <span className={t.direction === 'long' ? 'text-eva-green' : 'text-eva-orange'}>
                    {t.direction === 'long' ? '↑ L' : '↓ S'}
                  </span>
                </td>
                <td className="py-1.5 px-1.5 text-primary-70">{t.signal}</td>
                <td className="py-1.5 px-1.5 text-primary-50">{t.context}</td>
                <td className={`py-1.5 px-1.5 text-right ${t.win ? 'text-eva-green' : 'text-eva-red'}`}>
                  {t.pnl > 0 ? '+' : ''}
                  {t.pnl.toFixed(2)}
                </td>
                <td className="py-1.5 px-1.5 text-primary-35">{t.hash}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="text-label mt-[var(--space-sm)]">
        signals: {Object.keys(dataset.signalTaxonomy).join(' · ')} — each fill verified by HL tx hash
      </div>
    </div>
  )
}

function Metric({
  label,
  value,
  highlight,
  green,
  red,
}: {
  label: string
  value: string
  highlight?: boolean
  green?: boolean
  red?: boolean
}) {
  const color = highlight ? 'text-eva-orange' : green ? 'text-eva-green' : red ? 'text-eva-red' : ''
  return (
    <div className={`bg-white p-[var(--space-md)] ${highlight ? 'border-b-2 border-eva-orange' : ''}`}>
      <div className="text-label mb-1">{label}</div>
      <div className={`font-display text-xl ${color}`}>{value}</div>
    </div>
  )
}
