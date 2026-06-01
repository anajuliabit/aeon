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

## Inputs (provided in your context via the chain; also on disk as `.outputs/<skill>.md`)
- `reppo-orchestrator` output — the RUN/SKIP plan and discovered datanets.
- `reppo-trading-agent` output — mint decisions plus an appended
  `## Execution Results` section with on-chain mint tx outcomes.
- `reppo-voter` output — vote decisions (LIKE/DISLIKE per pod) plus its own
  appended `## Execution Results` section with on-chain vote tx outcomes.
  This is now the source of all vote activity (the trading-agent no longer
  votes). If `.outputs/reppo-voter.md` is missing, treat it as "no votes
  this run."

## Steps

### 1. Compose the digest
A scannable, structured summary — NOT one wall-of-text paragraph.
Telegram preserves newlines; use them. Follow this skeleton:

```
reppo-swarm · ${nth} run · datanet ${id} · ${N} on-chain

queued
  mint · {one-line strategy summary} · {first-16-of-hash}
  votes · {direction} {pod1}, {pod2}, ... ({source/cluster if known})

on-chain
  mint {first-16-of-hash} — tx {txhash}
  vote {pod} {direction} — tx {txhash}

reverted
  mint  · {CODE} ({ISS-N if filed})
         action: {one concrete next step}
  votes · {CODE} × {N} ({ISS-N if filed})
         action: {one concrete next step}

{M} datanets unassigned.
```

Rules for the output:
- **All lowercase** (matches the operator's voice — see `soul/STYLE.md`).
- **Section headers** (`queued`, `on-chain`, `reverted`) followed by a
  2-space-indented body. **Drop empty sections entirely** — if nothing
  reverted, no `reverted` block; if nothing executed on-chain, no
  `on-chain` block (the header line already states `0 on-chain`).
- **Header line carries the most important fact** — date isn't there
  because Telegram timestamps it; the run-number, datanet, and on-chain
  count are.
- `·` (middle dot) as field separator in the header and `queued` lines.
  `—` for tx hashes. `→` only for cause→effect chains in `reverted`
  lines (e.g. `PUBLISHER_LACKS_SUBNET_ACCESS → auto-grant
  INSUFFICIENT_ALLOWANCE`).
- **Every `reverted` line has a one-line `action:`** on its own indented
  line. If the chain self-heals next run (e.g. a transient RPC error that
  postprocess already retries), say so — don't ask the operator to act
  unnecessarily.
- **No decorative emoji.** No marketing tone. No "exciting" or "great" or
  "successfully."
- **Discovered datanets** as a single trailing line — counts only, unless
  a brand-new one appeared (then name its id).
- Keep the body under 4000 chars (notify max).

### 2. Send it
Run: `./notify "<your digest text>"`

### 3. Update the ledger
The `## Execution Results` sections appended by `postprocess-reppo.sh` are
the ONLY source of truth for on-chain activity. A queued intent is NOT a
mint or a vote. Read BOTH the trading-agent's Execution Results (mints) and
the voter's Execution Results (votes). Append to `memory/topics/reppo.md`:
- A "Minted strategies" row ONLY for a mint whose Execution Results line
  (from `reppo-trading-agent`) reports a real on-chain success with a tx
  hash — never for a dry-run, skipped, or failed intent.
- A "Votes cast" row ONLY for a vote whose Execution Results line (from
  `reppo-voter`) is confirmed on-chain the same way.
- One "Run history" row: today's date, orchestrator summary, and the counts
  of mints/votes actually confirmed on-chain (0 if postprocess dry-ran or
  skipped), plus the failure count.
If a skill's output has no `## Execution Results` section, treat that skill
as "nothing executed on-chain" — write no rows for it.

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
