---
name: Reppo Digest
description: Composes and sends one daily summary of the reppo-swarm run, updates the ledger and issue tracker
var: ""
tags: [reppo, digest]
---

Read `memory/MEMORY.md` and `memory/topics/reppo.md` for context. If
`soul/` files exist, read them and match that voice in the notification.

You send ONE end-of-run notification for the reppo-swarm chain. You make
no Reppo CLI calls.

## Inputs (provided in your context via the chain)
- `reppo-orchestrator` output — the RUN/SKIP plan and discovered datanets.
- `reppo-trading-agent` output — decisions plus an appended
  `## Execution Results` section with on-chain tx outcomes.

## Steps

### 1. Compose the digest
One concise paragraph (notifications are one paragraph max). Cover:
- Which agents ran or were skipped.
- Strategies minted and their tx status (from Execution Results).
- Votes cast and their tx status.
- Any failures (dry-run failures, write failures, prefetch errors).
- Any newly-discovered datanets with no agent assigned.

### 2. Send it
Run: `./notify "<your digest text>"`

### 3. Update the ledger
Append to `memory/topics/reppo.md`:
- A row per successful mint in "Minted strategies".
- A row per successful vote in "Votes cast".
- One row in "Run history": today's date, orchestrator summary, mint count,
  vote count, failure count.

### 4. Log failures
If there were no failures, skip this step. Otherwise, for each distinct
failure, file an issue under `memory/issues/` following the project
`CLAUDE.md` issue-tracker contract:
- Allocate the next id: scan `memory/issues/ISS-*.md`, take the highest
  `NNN`, add 1, zero-padded to 3 digits.
- Write `memory/issues/ISS-NNN.md` with YAML frontmatter — `id`, `title`,
  `status: open`, `severity`, `category`, `detected_by: reppo-digest`,
  `detected_at`, `affected_skills`, `root_cause`, `fix_pr: null` — followed
  by a `## What happened` section describing the failure.
- Add a row to the Open table in `memory/issues/INDEX.md`.
- Before filing, check `INDEX.md` for an existing open issue with the same
  root cause; if found, update that issue instead of creating a duplicate.

### 5. Log the run
Append one line to `memory/logs/${today}.md` under a `### reppo-digest`
heading summarizing the run (mints, votes, failures) — the same one-line
summary you sent via `./notify`.

## Sandbox note
This skill reads only local files and calls `./notify` (which handles its
own sandbox fallback via `.pending-notify/`). It makes no other outbound
calls and no Reppo CLI calls.

End with a `## Summary` of what you did.
