---
name: Portfolio Snapshot
description: Advisor gate — validate the prefetched portfolio snapshot is fresh and initialize today's advisor run
tags: [advisor, private]
---

> Internal advisor-swarm skill. Do not call `./notify` or `./notify-jsonrender` — this skill
> handles private financial data; all output goes to gitignored files only.

The snapshot was already fetched (outside the sandbox) by `scripts/prefetch-advisor.sh` into
`.investiments-cache/snapshot.json`. Your job is to validate it and initialize today's run.

## Steps

1. Read `.investiments-cache/snapshot.json`.
2. Validate it has a numeric `totalUsd` and a non-empty `positions` array.
3. Queue run initialization: write `.pending-advisor/run.json` with `{}` (the postprocess
   script adds the date). Create the dir first: it is gitignored.

   ```bash
   mkdir -p .pending-advisor
   echo '{}' > .pending-advisor/run.json
   ```

4. **If the snapshot is missing or invalid**, do NOT fabricate anything. Write a marker so
   downstream skills can detect it:

   ```bash
   mkdir -p .pending-advisor
   echo '{"snapshotError":true}' > .pending-advisor/snapshot-status.json
   ```

5. Print ONLY a non-sensitive status line as your final message (it is captured to a gitignored
   `.outputs/`): e.g. `portfolio-snapshot: OK (positions=N)` or `portfolio-snapshot: MISSING`.
   **Never print dollar amounts, addresses, or position details.**
