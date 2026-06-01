'use client'

import { STAGES } from '@/lib/swarm'

/**
 * Demo transport bar. The whole UI is a pure function of `stage` (0..5); this
 * just mutates it. Auto-mode advances on a timer owned by the page; here we
 * only render the toggle + prev/next + a stage scrubber.
 */
export function PlaybackControls({
  stage,
  setStage,
  auto,
  setAuto,
}: {
  stage: number
  setStage: (n: number) => void
  auto: boolean
  setAuto: (b: boolean) => void
}) {
  const last = STAGES.length - 1
  const atStart = stage <= 0
  const atEnd = stage >= last

  return (
    <div className="flex items-center gap-[var(--space-md)] flex-wrap">
      <button
        onClick={() => setAuto(!auto)}
        className={`cursor-target font-mono text-[11px] uppercase tracking-[2px] px-3 py-2 border-2 transition-colors ${
          auto
            ? 'border-eva-orange text-eva-orange'
            : 'border-[rgba(10,10,10,0.15)] text-primary-50 hover:border-eva-black'
        }`}
        aria-pressed={auto}
      >
        {auto ? '⏸ Auto' : '▶ Auto'}
      </button>

      <div className="flex items-center">
        <button
          onClick={() => setStage(Math.max(0, stage - 1))}
          disabled={atStart}
          className="cursor-target font-mono text-sm px-3 py-2 border-2 border-[rgba(10,10,10,0.15)] disabled:opacity-30 hover:border-eva-black transition-colors"
          aria-label="Previous stage"
        >
          ◀
        </button>
        <button
          onClick={() => setStage(Math.min(last, stage + 1))}
          disabled={atEnd}
          className="cursor-target font-mono text-sm px-3 py-2 border-2 border-l-0 border-[rgba(10,10,10,0.15)] disabled:opacity-30 hover:border-eva-black transition-colors"
          aria-label="Next stage"
        >
          ▶
        </button>
      </div>

      {/* Stage scrubber — six ticks, click to jump */}
      <div className="flex items-center gap-1.5">
        {STAGES.map((s, i) => (
          <button
            key={s.key}
            onClick={() => setStage(i)}
            title={`${i + 1}. ${s.title}`}
            className={`cursor-target h-2 transition-all ${
              i === stage
                ? 'w-8 bg-eva-orange'
                : i < stage
                  ? 'w-4 bg-eva-green'
                  : 'w-4 bg-[rgba(10,10,10,0.12)] hover:bg-[rgba(10,10,10,0.25)]'
            }`}
            aria-label={`Go to stage ${i + 1}: ${s.title}`}
          />
        ))}
      </div>

      <div className="font-mono text-[11px] uppercase tracking-[2px] text-primary-40 ml-auto">
        {String(stage + 1).padStart(2, '0')} / {String(STAGES.length).padStart(2, '0')} · {STAGES[stage].title}
      </div>
    </div>
  )
}
