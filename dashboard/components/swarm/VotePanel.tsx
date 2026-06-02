'use client'

import type { SwarmVote } from '@/lib/swarm'

const short = (h?: string) => (h ? `${h.slice(0, 10)}…${h.slice(-6)}` : '')

/**
 * Votes cast on other pods. The agent dislikes off-rubric raw dumps to keep the
 * datanet clean, and the contract correctly rejects the self-vote — a nice
 * "the rules are enforced on us too" beat for the demo.
 */
export function VotePanel({ votes }: { votes: SwarmVote[] }) {
  return (
    <div className="card-hst p-[var(--space-lg)] h-full flex flex-col">
      <div className="flex items-center justify-between mb-[var(--space-md)]">
        <span className="text-label">Votes cast</span>
        <span className="font-mono text-[11px] text-primary-40">curating the datanet</span>
      </div>

      <div className="flex flex-col gap-[var(--space-sm)]">
        {votes.map((v) => {
          const rejected = v.status === 'rejected'
          const dislike = v.direction === 'dislike'
          return (
            <div
              key={v.podId}
              className={`p-[var(--space-md)] border-2 ${
                rejected
                  ? 'border-dashed border-[rgba(10,10,10,0.25)] opacity-80'
                  : dislike
                    ? 'border-eva-orange'
                    : 'border-eva-green'
              }`}
            >
              <div className="flex items-center justify-between mb-1.5">
                <div className="flex items-center gap-2">
                  <span
                    className={`font-mono text-[11px] px-2 py-0.5 tracking-[1.5px] text-white ${
                      dislike ? 'bg-eva-orange' : 'bg-eva-green'
                    }`}
                  >
                    {dislike ? '▼ DISLIKE' : '▲ LIKE'}
                  </span>
                  <span className="font-mono text-[12px] text-primary-50">pod #{v.podId}</span>
                </div>
                <span className={`font-mono text-[10px] tracking-[1.5px] ${rejected ? 'text-eva-red' : 'text-eva-green'}`}>
                  {rejected ? '✕ REVERTED' : '✓ CONFIRMED'}
                </span>
              </div>

              <p className="font-mono text-[11px] leading-snug text-primary-70">{v.reason}</p>

              {rejected && v.rejectCode ? (
                <p className="font-mono text-[10px] text-eva-red mt-1.5 tracking-[0.5px]">
                  contract: {v.rejectCode} — you can’t vote on your own pod
                </p>
              ) : v.txHash ? (
                <a
                  href={`https://basescan.org/tx/${v.txHash}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="cursor-target font-mono text-[10px] text-primary-40 hover:text-eva-green underline decoration-1 underline-offset-2 mt-1.5 inline-block"
                >
                  {short(v.txHash)}
                </a>
              ) : null}
            </div>
          )
        })}
      </div>

      <div className="text-label mt-auto pt-[var(--space-md)] leading-relaxed">
        dislikes filter raw exports + unlabeled dumps off-rubric · self-vote reverts by design
      </div>
    </div>
  )
}
