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
For each failure, append or update an issue file under `memory/issues/`
following the structure in the project `CLAUDE.md` (frontmatter with id,
title, status: open, severity, category, detected_by: reppo-digest,
detected_at). If there were no failures, do nothing here.

### 5. Log the run
Append one line to `memory/logs/${today}.md` under a `### reppo-digest`
heading summarizing the run (mints, votes, failures) — the same one-line
summary you sent via `./notify`.

## Sandbox note
This skill reads only local files and calls `./notify` (which handles its
own sandbox fallback via `.pending-notify/`). It makes no other outbound
calls and no Reppo CLI calls.

End with a `## Summary` of what you did.
