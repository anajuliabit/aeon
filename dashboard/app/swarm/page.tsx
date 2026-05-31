'use client'

import { useState, useEffect, useCallback } from 'react'
import type { SwarmData } from '@/lib/swarm'
import { STAGES } from '@/lib/swarm'
import { SWARM_SNAPSHOT } from '@/lib/swarm-snapshot'
import { SwarmPipeline } from '@/components/swarm/SwarmPipeline'
import { PlaybackControls } from '@/components/swarm/PlaybackControls'
import { StageDetail } from '@/components/swarm/StageDetail'

const AUTO_MS = 4200

const SOURCE_BADGE: Record<SwarmData['source'], { label: string; cls: string }> = {
  live: { label: '● LIVE', cls: 'bg-eva-green text-white' },
  mixed: { label: '◐ LIVE + SNAPSHOT', cls: 'bg-eva-amber text-eva-black' },
  snapshot: { label: '◌ SNAPSHOT', cls: 'border-2 border-[rgba(10,10,10,0.2)] text-primary-50' },
}

/**
 * Reppo Swarm demo. The entire view is a pure function of `stage` (0..5):
 * the pipeline hero, the progress rail, and the detail panel all derive from
 * it. Auto-mode advances on a timer; manual mode (arrows / buttons / scrubber)
 * pauses it. Data is seeded from the curated snapshot so the page is fully
 * rendered on first paint, then upgraded with whatever the live API returns.
 */
export default function SwarmDemo() {
  const [data, setData] = useState<SwarmData>(SWARM_SNAPSHOT)
  const [stage, setStageRaw] = useState(0)
  const [auto, setAuto] = useState(false)

  // Fetch live/hybrid data; keep the snapshot on any failure.
  useEffect(() => {
    fetch('/api/swarm')
      .then((r) => (r.ok ? r.json() : null))
      .then((d: SwarmData | null) => d && setData(d))
      .catch(() => {})
  }, [])

  // Manual interaction always pauses auto-advance.
  const setStage = useCallback((n: number) => {
    setStageRaw(n)
    setAuto(false)
  }, [])

  // Auto-advance timer. Stops itself at the last stage.
  useEffect(() => {
    if (!auto) return
    if (stage >= STAGES.length - 1) {
      setAuto(false)
      return
    }
    const id = setTimeout(() => setStageRaw((s) => Math.min(STAGES.length - 1, s + 1)), AUTO_MS)
    return () => clearTimeout(id)
  }, [auto, stage])

  // Keyboard transport: ←/→ step, space toggles auto.
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'ArrowRight') setStage(Math.min(STAGES.length - 1, stage + 1))
      else if (e.key === 'ArrowLeft') setStage(Math.max(0, stage - 1))
      else if (e.key === ' ') {
        e.preventDefault()
        setAuto((a) => !a)
      }
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [stage, setStage])

  const badge = SOURCE_BADGE[data.source]

  return (
    <div className="min-h-screen bg-eva-white text-eva-black bg-grid">
      <div className="warning-stripes" />

      <div className="max-w-[1400px] mx-auto px-[var(--space-lg)] py-[var(--space-lg)] flex flex-col gap-[var(--space-lg)]">
        {/* header */}
        <header className="flex items-end justify-between flex-wrap gap-[var(--space-md)]">
          <div className="flex items-center gap-[var(--space-md)]">
            <div className="logo-mark">
              <div className="logo-mark-inner" />
              <span className="logo-mark-letter">R</span>
            </div>
            <div>
              <h1 className="font-display text-3xl leading-none">Reppo Swarm</h1>
              <p className="font-mono text-[11px] tracking-[2px] text-primary-40 mt-1.5 uppercase">
                datanet #{data.datanet.id} · {data.datanet.name} · run {data.runDate}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <span className={`font-mono text-[11px] px-3 py-1.5 tracking-[1.5px] ${badge.cls}`}>{badge.label}</span>
            <div className="text-right hidden sm:block">
              <div className="text-label">3 claude-opus skills</div>
              <div className="font-mono text-[11px] text-primary-50">via GitHub Actions</div>
            </div>
          </div>
        </header>

        {/* controls */}
        <div className="card-hst px-[var(--space-lg)] py-[var(--space-md)]">
          <PlaybackControls stage={stage} setStage={setStage} auto={auto} setAuto={setAuto} />
        </div>

        {/* hero pipeline */}
        <SwarmPipeline stage={stage} onPick={setStage} />

        {/* detail */}
        <StageDetail data={data} stage={stage} />

        <footer className="text-label text-center pt-[var(--space-md)] pb-[var(--space-xl)]">
          built on aeon · orchestrator → trading-agent → postprocess · every datanet deserves its own swarm
        </footer>
      </div>
    </div>
  )
}
