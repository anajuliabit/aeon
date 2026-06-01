'use client'

import type { SwarmData } from '@/lib/swarm'
import { TraderCard } from './TraderCard'
import { DatasetTable } from './DatasetTable'
import { PodCard } from './PodCard'
import { VotePanel } from './VotePanel'

/**
 * The detail surface under the hero. It's a pure switch on `stage`: each beat
 * reveals the panel(s) that make that step concrete. Stages 2 and 4 show two
 * panels so the narration has continuity (trader→dataset, dataset→pod).
 */
export function StageDetail({ data, stage }: { data: SwarmData; stage: number }) {
  return (
    <div key={stage} className="swarm-fade">
      {stage === 0 && <PlanDetail data={data} />}
      {stage === 1 && (
        <div className="max-w-xl">
          <TraderCard trader={data.trader} />
        </div>
      )}
      {stage === 2 && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-[var(--space-md)]">
          <TraderCard trader={data.trader} />
          <DatasetTable dataset={data.dataset} />
        </div>
      )}
      {stage === 3 && <DatasetTable dataset={data.dataset} />}
      {stage === 4 && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-[var(--space-md)]">
          <PodCard pod={data.pod} />
          <DatasetTable dataset={data.dataset} />
        </div>
      )}
      {stage === 5 && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-[var(--space-md)]">
          <VotePanel votes={data.votes} />
          <PodCard pod={data.pod} />
        </div>
      )}
    </div>
  )
}

/** Stage 0 — the orchestrator's routing decision + datanet discovery. */
function PlanDetail({ data }: { data: SwarmData }) {
  const { plan, datanet } = data
  return (
    <div className="grid grid-cols-1 lg:grid-cols-[1.2fr_1fr] gap-[var(--space-md)]">
      <div className="card-hst card-hst-orange p-[var(--space-lg)]">
        <span className="text-label">Routing decision</span>
        <div className="flex items-center gap-3 mt-[var(--space-md)] mb-[var(--space-md)]">
          <span className="font-mono text-[12px] px-3 py-1 bg-eva-green text-white tracking-[2px]">{plan.decision}</span>
          <span className="font-display text-lg">{plan.agent}</span>
        </div>
        <p className="font-mono text-[12px] leading-relaxed text-primary-70 border-l-2 border-eva-orange pl-3">
          {plan.reason}
        </p>
        <div className="text-label mt-[var(--space-md)]">
          emits a fenced <span className="text-eva-orange">reppo-plan</span> block — the trading-agent gates on it. no
          block, no on-chain activity.
        </div>
      </div>

      <div className="card-hst p-[var(--space-lg)]">
        <div className="flex items-center justify-between mb-[var(--space-md)]">
          <span className="text-label">Datanet catalog</span>
          <span className="font-mono text-[11px] text-primary-40">{plan.catalogSize} on mainnet</span>
        </div>
        <div className="border-2 border-eva-green p-[var(--space-md)] mb-[var(--space-md)]">
          <div className="font-display text-xl">
            #{datanet.id} · {datanet.name}
          </div>
          <div className="font-mono text-[11px] text-primary-50 mt-1">assigned · accessFee {datanet.accessFee}</div>
        </div>
        <span className="text-label">{plan.newDatanets.length} unassigned — next swarms</span>
        <div className="flex flex-wrap gap-1.5 mt-2">
          {plan.newDatanets.map((id) => (
            <span
              key={id}
              className="font-mono text-[11px] px-2 py-1 border border-dashed border-[rgba(10,10,10,0.25)] text-primary-50"
            >
              #{id}
            </span>
          ))}
        </div>
        <p className="font-mono text-[11px] text-primary-40 mt-[var(--space-md)] leading-snug">
          TradingGymAI is the first — every Reppo datanet deserves its own agent swarm.
        </p>
      </div>
    </div>
  )
}
