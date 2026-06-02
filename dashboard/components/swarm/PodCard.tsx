'use client'

import type { SwarmPod } from '@/lib/swarm'

const short = (h: string, n = 8) => (h ? `${h.slice(0, n + 2)}…${h.slice(-6)}` : '—')

/**
 * The minted pod: ERC-721 on Base + the dataset pinned to IPFS via Pinata.
 * Both the tx hash and the IPFS CID are real and externally verifiable — the
 * whole point is that the pod exists independent of the Reppo platform.
 */
export function PodCard({ pod }: { pod: SwarmPod }) {
  const minted = pod.status === 'minted'
  return (
    <div className="card-hst card-hst-green p-[var(--space-lg)] h-full flex flex-col">
      <div className="flex items-center justify-between mb-[var(--space-md)]">
        <span className="text-label">Pod minted</span>
        <span
          className={`font-mono text-[11px] px-2 py-0.5 tracking-[1.5px] ${
            minted ? 'bg-eva-green text-white' : 'bg-[rgba(10,10,10,0.1)] text-primary-50'
          }`}
        >
          {minted ? '● ON-CHAIN' : pod.status.toUpperCase()}
        </span>
      </div>

      <div className="font-display text-lg leading-tight mb-[var(--space-md)]">{pod.name}</div>

      <div className="flex flex-col gap-px bg-[rgba(10,10,10,0.08)]">
        <Row label="datanet" value={`#${pod.datanet} · TradingGymAI`} />
        <Row label="chain" value={`${pod.chain} · ERC-721`} />
        <Row
          label="mint tx"
          value={short(pod.txHash)}
          href={pod.txHash ? `https://basescan.org/tx/${pod.txHash}` : undefined}
        />
        <Row label="ipfs pin" value={pod.ipfsCid ? short(pod.ipfsCid, 6) : '—'} href={pod.gateway || undefined} />
      </div>

      <div className="text-label mt-[var(--space-md)] leading-relaxed">
        dataset pinned to IPFS via Pinata, then registered to the Reppo platform — verifiable without trusting the UI
      </div>
    </div>
  )
}

function Row({ label, value, href }: { label: string; value: string; href?: string }) {
  return (
    <div className="bg-white px-[var(--space-md)] py-2.5 flex items-center justify-between gap-3">
      <span className="text-label shrink-0">{label}</span>
      {href ? (
        <a
          href={href}
          target="_blank"
          rel="noopener noreferrer"
          className="cursor-target font-mono text-[12px] text-eva-black underline decoration-eva-green decoration-2 underline-offset-2 hover:text-eva-green truncate"
        >
          {value}
        </a>
      ) : (
        <span className="font-mono text-[12px] truncate">{value}</span>
      )}
    </div>
  )
}
