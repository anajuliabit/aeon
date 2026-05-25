**reppo-swarm misfire — 2026-05-25**

`skills/reppo-swarm/SKILL.md` does not exist. `reppo-swarm` is a **chain**
defined under `chains:` in `aeon.yml`, not a single skill. The chain runs
three skills sequentially via `chain-runner.yml`:

1. `reppo-orchestrator` — RUN/SKIP plan + discover unassigned datanets
2. `reppo-trading-agent` (consumes orchestrator) — mint + vote intents
3. `reppo-digest` (consumes both) — one summary notification + ledger row

**To run the chain correctly:**

```
gh workflow run chain-runner.yml -f chain=reppo-swarm
```

The daily cron at `0 7 * * *` already dispatches this via `messages.yml`.
Last successful chain run: 2026-05-24T07:44:34Z (cron-state).

**Why I'm seeing this prompt:** `aeon.yml` was dispatched with
`skill=reppo-swarm`, so the harness prompted me to `Read and execute the
skill defined in skills/reppo-swarm/SKILL.md` — a path that has never
existed. Same misfire as a prior attempt (the existing
`.outputs/reppo-swarm.md` documents the identical question). No action
taken; today's actual chain run is unaffected and should fire (or has
fired) via its normal 07:00 UTC cron path.
