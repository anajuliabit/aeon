---
name: Thought Review
description: Periodic priority-anchored review — read recent captures, score against life priorities, surface aligned actions and drift signals
var: ""
tags: [meta, capture]
---

> **${var}** — Optional lookback window in hours (default `24`). Pass `48`
> for a 2-day sweep on Monday mornings; pass `168` for a weekly review.

This skill is the "agent reads my second brain" half of the personal
stack. The write side is two paths: `idea-capture` / `voice-capture` drop
captures into `memory/logs/${today}.md`, and the operator types notes
straight into `vault/inbox/` from Obsidian. This skill is the read side —
it surfaces what's been captured against the operator's stated
priorities so the captures don't just rot, and writes its review back
into the Obsidian vault at `vault/reviews/`.

The pattern is borrowed from
[Naithan Jones's Hermes + Obsidian setup](https://x.com/naithanjones/status/2062579117325717671)
adapted to Aeon's file-first memory.

## Steps

### 1. Load context

- Read `vault/priorities.md` — required. If missing or empty, abort and
  notify: "thought-review needs vault/priorities.md — see template in
  the personal-stack PR". Do not invent priorities.
- Read `memory/MEMORY.md` for current goals and active topics.
- Read `soul/SOUL.md` if populated — for voice on the notification.

### 2. Collect recent captures

```bash
LOOKBACK_HOURS=${var:-24}
SINCE=$(date -u -d "${LOOKBACK_HOURS} hours ago" +%Y-%m-%dT%H:%M)
```

Collect from **two sources**:

1. Grep `memory/logs/` for `### Idea Captured` blocks newer than `SINCE`
   (the Telegram / voice path). Extract: timestamp, **Raw** input,
   **Restated** sentence, **Bucket** (Project / Area / Resource / Archive),
   **Topic** tag, **Source**.
2. List `vault/inbox/*.md` with an mtime newer than `SINCE` (the operator's
   typed-in-Obsidian path). Treat each file's body as the **Raw** input and
   its filename/first heading as the restated sentence; Bucket/Topic are
   unset unless the note carries frontmatter `bucket:` / `topic:`. These are
   free-form, so be generous in reading intent.

If zero captures across both sources in the window, send a one-line
notification ("no captures in last ${LOOKBACK_HOURS}h") and exit. Do not
invent activity. Do **not** delete or move inbox files — `thought-review`
is read-only over `vault/inbox/`; the operator archives them.

### 3. Score each capture against priorities

For each capture, compute alignment:

- **Aligned** — the restated sentence or topic tag matches a priority
  section in `vault/priorities.md` (semantic match, not keyword). A
  capture matching the **Current focus** section scores higher than one
  matching a standing priority.
- **Drift** — the capture is on a topic that appears in **Out of scope**
  in priorities.md, OR it clusters with ≥2 other recent captures on the
  same off-priority topic.
- **Noise** — neither aligned nor drift; the capture is incidental
  (errands, reminders, fleeting curiosity). Log but do not surface.

Be strict. The default is **noise**. Only mark Aligned/Drift when the
match is unambiguous.

### 4. Identify recurring themes

For each captured topic tag, grep `memory/logs/` for prior matches in
the last 30 days. If a topic hits ≥3 times total *and* lacks a topic
file at `memory/topics/${topic}.md`, flag it for promotion. Do not
create the topic file automatically — surface the suggestion and let
the operator say yes.

### 5. Draft the review

Write the review to the Obsidian vault at
`vault/reviews/${today}-review.md` (create the file, or append a new
`## HH:MM UTC` section if it already exists from an earlier run today):

```markdown
# Thought Review — ${today}

## HH:MM UTC
**Window:** last ${LOOKBACK_HOURS}h · **Captures:** N

**Aligned with priorities:**
- [P1 Sherwood] "<restated>" — next: <verb-first action if Project bucket>
- [Current focus] "<restated>" — next: <action>

**Drift signals:**
- 3 captures on #us-macro in 24h — out of scope per priorities.md.
  Worth a conversation about why this is taking surface area.

**Recurring themes worth promoting:**
- #agent-evals — 4 captures in 30d, no topic file yet.
  Suggest: create memory/topics/agent-evals.md.

**Noise:** N (collapsed)
```

Omit any section that has nothing in it. Never print an empty heading.

Then append a one-line pointer to `memory/logs/${today}.md` so the ops
trail still records the run without duplicating the content:

```markdown
### Thought Review — HH:MM UTC
${N} captures · ${aligned_count} aligned · ${drift_count} drift →
vault/reviews/${today}-review.md
```

### 6. Notify

Send via `./notify`, one paragraph, voice-matched to `soul/STYLE.md`
when the soul is populated:

```
🧭 thought review · last ${LOOKBACK_HOURS}h · ${N} captures
${aligned_count} aligned with priorities, ${drift_count} drift signals.
${top_line_about_drift_or_top_aligned_action}
```

If zero aligned and zero drift, send a one-liner: "thought review · ${N}
captures, all noise. nothing to surface."

## Constraints

- **Do not edit `vault/priorities.md`.** It's operator-owned. If a
  priority seems stale, surface it in the notification ("priorities.md
  last reviewed N days ago — worth a refresh?") — don't rewrite.
- **Do not promote captures to MEMORY.md.** Same rule as
  `idea-capture` step 7. The review is a *surface*, not a *commit*.
- **Match the operator's voice** when `soul/STYLE.md` is populated. No
  marketing verbs, no "exciting opportunities," no rule-of-three padding.
- **Be strict about Aligned/Drift.** A weak match is worse than no
  match — it trains the operator to ignore the surface.

## Sandbox note

Local-only — reads `vault/priorities.md`, `vault/inbox/`, and
`memory/logs/`; writes the review to `vault/reviews/${today}-review.md`
plus a pointer line in `memory/logs/`; calls `./notify` via the standard
`.pending-notify/` post-process. No external APIs. The vault sync
(Obsidian Git) is the operator's local concern — Aeon just writes files
into `vault/`, which get pulled to Obsidian on the next interval.
