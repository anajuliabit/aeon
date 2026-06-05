# Personal Stack — Hermes-style capture + priority-anchored review

Adapting [Naithan's Hermes + Obsidian setup](https://x.com/naithanjones/status/2062579117325717671)
to Aeon's file-first memory.

## What Naithan built

> "Hermes agent has been the single best remedy to my ADHD. I created a
> random thoughts vault in Obsidian and now whenever the flood of a
> million invasive thoughts come I just add them to this folder via
> speech to text. I then created a markdown called life priorities that
> explain[s]…"
> — @NaithanJones, 2026-06-04

The loop:

1. Voice → speech-to-text → markdown drop into a "random thoughts" folder
   in his Obsidian vault.
2. A stable `life priorities.md` the agent reads to score / contextualize
   captures.
3. The agent periodically surfaces captures back, anchored to priorities.

The point isn't the vault. The point is **a frictionless capture path
paired with a priority-anchored review path**, so dumped thoughts get
either acted on or archived instead of rotting.

## What Aeon already has

| Naithan's primitive       | Aeon equivalent                          | Status |
|--------------------------|------------------------------------------|--------|
| Obsidian vault           | `memory/` (markdown-first by design)     | shipped |
| Random thoughts folder   | `memory/logs/${today}.md` capture blocks | shipped |
| Voice → text             | Telegram inbound (text + image only)     | **gap** |
| Life priorities markdown | none — `idea-capture` uses generic PARA  | **gap** |
| Periodic review          | `evening-recap` (ops, not personal)      | **gap** |
| Persistent agent runtime | Aeon (GitHub Actions + Claude Code)      | shipped |

## What this PR adds

### 1. `vault/priorities.md`

The operator-owned anchor file (lives in the Obsidian `vault/`). One entry
per priority, ordered by weight, each with "what winning looks like" +
non-negotiables. A **Current focus** section the operator edits weekly. An
**Out of scope** section so the agent stops surfacing topics that are
intentionally cold.

This file is read-only to the agent. Edits are operator-owned.

### 2. `skills/thought-review/SKILL.md`

Scheduled 2x/day (07:00 + 21:00 UTC) via `aeon.yml`. Reads:

- `vault/priorities.md` (required)
- `memory/MEMORY.md` (context)
- `soul/SOUL.md` + `soul/STYLE.md` (notification voice)
- recent `### Idea Captured` blocks in `memory/logs/` **and** new notes in
  `vault/inbox/` over the lookback window (default 24h, configurable via `var:`)

Scores each capture as Aligned / Drift / Noise against priorities.
Writes a `### Thought Review` block back to today's log and notifies via
`./notify`. The notification is the surface; the log entry is the audit
trail.

Strict-by-default: most captures should be Noise. Aligned/Drift surfaces
only when the match is unambiguous, so the operator learns to trust the
review.

### 3. Voice transcription in `.github/workflows/messages.yml`

Patched the Telegram poller (`messages.yml:498`) to detect
`message.voice` and `message.audio`, download via `getFile`, and
transcribe via OpenAI Whisper (`whisper-1`). The transcript flows
through the existing message dispatcher — voice notes route the same
way text routes today.

**Gated on `OPENAI_API_KEY`.** Without it, voice messages are silently
acked and dropped (current behavior preserved). Setting the secret
turns the path on with no other config required.

Cost: Whisper is $0.006/min. A 30-second thought = $0.003. Cheap enough
to not gate.

### 4. `aeon.yml` registration

```yaml
thought-review: { enabled: true, schedule: "0 7,21 * * *", var: "24" }
```

Twice-daily so the morning review covers overnight captures and the
evening review covers the workday. The 24h window deliberately
overlaps — repeated noise is itself signal.

## What this PR explicitly does NOT do

- **No edits to `idea-capture`.** It already does the capture half well.
  This PR adds the read half without changing the write half.
- **No separate `voice-capture` skill.** The transcription is one inline
  step in `messages.yml`; once transcribed, the existing message handler
  routes it. Adding a skill would just be ceremony.
- **No auto-edits to `priorities.md`.** Drift detection surfaces in
  the notification — the operator decides whether to update the
  priorities file or ignore the drift.
- **Obsidian vault sync — now shipped separately.** This PR's follow-on
  adds a real two-way bridge: a curated `vault/` folder (your
  `priorities.md`, `inbox/`, `notes/`, `reviews/`) synced to a local
  Obsidian vault via git + the Obsidian Git plugin, with Aeon's
  operational files hidden from the graph. `priorities.md` now lives at
  `vault/priorities.md` and `thought-review` writes reviews to
  `vault/reviews/`. See `docs/obsidian-vault.md` for setup and
  `docs/superpowers/specs/2026-06-04-aeon-obsidian-vault-design.md` for
  the design.

## Required secrets

| Secret             | Required for         | Behavior without |
|--------------------|----------------------|------------------|
| `OPENAI_API_KEY`   | voice transcription  | voice messages silently dropped (current behavior) |
| `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` | inbound capture | already configured |

`thought-review` runs against existing files; no new secrets needed.

## Follow-ups (not in this PR)

- **Promote topic-file suggestions.** `thought-review` flags recurring
  themes that lack a topic file. Could chain into `create-topic-file`
  on operator confirmation. Out of scope until the review pattern proves
  itself.
- **Voice acks.** Today the user has to wait for the next poll cycle
  (~5min) to see the transcript echoed back via `idea-capture`'s
  restatement. Could be tightened by triggering an immediate
  `repository_dispatch` when a voice message arrives. Optimization, not
  prerequisite.
- **Weekly priority-staleness check.** If `priorities.md`'s
  "Last reviewed" date is >14d old, surface in `reflect` or
  `evening-recap`. Cheap to add later.
