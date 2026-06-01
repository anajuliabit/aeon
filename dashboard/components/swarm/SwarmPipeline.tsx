'use client'

import { useEffect, useRef } from 'react'
import { gsap } from 'gsap'
import { STAGES, LANES, type Lane } from '@/lib/swarm'

const LANE_META: Record<Lane, { label: string; skill: string; accent: string }> = {
  orchestrator: { label: 'Orchestrator', skill: 'reppo-orchestrator', accent: 'var(--color-orange)' },
  'trading-agent': { label: 'Trading Agent', skill: 'reppo-trading-agent', accent: 'var(--color-black)' },
  postprocess: { label: 'Postprocess', skill: 'postprocess-reppo.sh', accent: 'var(--color-green)' },
}

/**
 * The hero: three skill swimlanes with the six pipeline stages laid out in
 * order. Everything is driven by `stage` — done stages go green, the active
 * stage glows orange and pulses (GSAP), future stages stay faint. A thin
 * progress rail under the title tracks overall completion.
 */
export function SwarmPipeline({ stage, onPick }: { stage: number; onPick: (n: number) => void }) {
  const activeRef = useRef<HTMLButtonElement | null>(null)

  useEffect(() => {
    const el = activeRef.current
    if (!el) return
    const tween = gsap.fromTo(
      el,
      { boxShadow: '0 0 0 0 rgba(255,107,26,0.0)' },
      {
        boxShadow: '0 0 0 6px rgba(255,107,26,0.10)',
        duration: 1.1,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
      },
    )
    return () => {
      tween.kill()
    }
  }, [stage])

  return (
    <div className="card-hst corner-markers p-[var(--space-lg)] relative">
      <span className="corner-marker corner-marker-sm top-left" />
      <span className="corner-marker corner-marker-sm top-right" />
      <span className="corner-marker corner-marker-sm bottom-left" />
      <span className="corner-marker corner-marker-sm bottom-right" />

      {/* progress rail */}
      <div className="mb-[var(--space-lg)]">
        <div className="flex items-center justify-between mb-2">
          <span className="text-label">Pipeline</span>
          <span className="font-mono text-[11px] tracking-[2px] text-primary-40">
            stateless chain · output → consume
          </span>
        </div>
        <div className="progress-bar">
          <div
            className="h-full bg-eva-orange transition-all duration-500 ease-out"
            style={{ width: `${((stage + 1) / STAGES.length) * 100}%` }}
          />
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-[1fr_auto_2fr_auto_1.4fr] gap-[var(--space-md)] items-stretch">
        {LANES.map((lane, li) => {
          const meta = LANE_META[lane]
          const stagesInLane = STAGES.map((s, i) => ({ s, i })).filter(({ s }) => s.lane === lane)
          return (
            <div key={lane} className="contents">
              <div className="flex flex-col gap-[var(--space-sm)]">
                {/* lane header */}
                <div className="flex items-baseline justify-between border-b-2 border-[rgba(10,10,10,0.1)] pb-1.5">
                  <span className="font-display text-base" style={{ color: meta.accent }}>
                    {meta.label}
                  </span>
                  <span className="font-mono text-[10px] tracking-[1.5px] text-primary-35 hidden lg:inline">
                    {meta.skill}
                  </span>
                </div>

                {stagesInLane.map(({ s, i }) => {
                  const state = i < stage ? 'done' : i === stage ? 'active' : 'pending'
                  return (
                    <button
                      key={s.key}
                      ref={state === 'active' ? activeRef : undefined}
                      onClick={() => onPick(i)}
                      className={`cursor-target text-left p-[var(--space-md)] border-2 transition-all duration-300 ${
                        state === 'active'
                          ? 'border-eva-orange bg-white'
                          : state === 'done'
                            ? 'border-[rgba(67,193,101,0.5)] bg-[rgba(67,193,101,0.04)]'
                            : 'border-[rgba(10,10,10,0.08)] opacity-50 hover:opacity-80'
                      }`}
                    >
                      <div className="flex items-center gap-2 mb-1.5">
                        <span
                          className={`font-mono text-[10px] w-5 h-5 flex items-center justify-center border ${
                            state === 'active'
                              ? 'border-eva-orange text-eva-orange'
                              : state === 'done'
                                ? 'border-eva-green text-eva-green'
                                : 'border-[rgba(10,10,10,0.2)] text-primary-40'
                          }`}
                        >
                          {state === 'done' ? '✓' : i + 1}
                        </span>
                        <span className="font-display text-[15px] leading-tight">{s.title}</span>
                      </div>
                      <p className="font-mono text-[11px] leading-snug text-primary-50">{s.blurb}</p>
                    </button>
                  )
                })}
              </div>

              {/* lane connector arrow (not after the last lane) */}
              {li < LANES.length - 1 && (
                <div className="hidden md:flex items-center justify-center">
                  <span
                    className={`font-mono text-xl transition-colors duration-300 ${
                      stage > STAGES.findLastIndex((s) => s.lane === lane) ? 'text-eva-green' : 'text-primary-35'
                    }`}
                  >
                    →
                  </span>
                </div>
              )}
            </div>
          )
        })}
      </div>
    </div>
  )
}
