# reppo-voter — decoupling voting from minting

**Date:** 2026-06-01
**Status:** Approved design (brainstorming complete)
**Branch:** `feat/reppo-voter`

## Problem

Voting on the TradingGymAI datanet is currently **Step 6 of the
`reppo-trading-agent` skill** — it only runs after the five mint steps,
shares the mint skill's context budget and priority, and in practice has
been starved. Since the 13th mint (2026-05-31), three consecutive runs
cast zero votes because the only current-epoch pods were our own mints
(`CANNOT_VOTE_FOR_OWN_POD`) or pods we'd already voted on.

The operator's intent: **voting must be a first-class, independent
activity that happens on every trigger regardless of whether we mint.**
Each trigger should pull the current pods on the datanet, evaluate them
against the datanet goal/rubric, and vote — fully separate from the
minting flow.

## Goal

Extract voting into its own skill, `reppo-voter`, that runs in parallel
with `reppo-trading-agent` in the `reppo-swarm` chain. The trading-agent
becomes mint-only; the voter owns the entire pull → evaluate → vote flow.

## Non-goals

- Changing *how* pods are fetched. `prefetch-reppo.sh` already runs
  `reppo list pods --all --datanet <id>` and derives `current_epoch`,
  `voted_pod_ids`, and `own_pod_ids`. The voter reuses these caches.
- Changing the on-chain execution path. `postprocess-reppo.sh` already
  executes `.pending-reppo/vote-*.json` intents unchanged.
- Changing the mint logic, the leaderboard prefetch, or `HL_TOP_N`
  (shipped separately in PR #60).

## Design

### 1. Responsibility split

| Skill | Before | After |
|---|---|---|
| `reppo-trading-agent` | mint (Steps 1–5) **+ vote (Step 6)** | **mint-only** (Step 6 removed) |
| `reppo-voter` (new) | — | **vote-only**: pull pods → filter → evaluate vs goal → write vote intents |

Voting is removed from `reppo-trading-agent` entirely — not duplicated.
This is the core decoupling: the two skills no longer share a skill file,
context budget, or execution priority.

### 2. reppo-voter behavior (per trigger)

1. **Read the rubric** `configs/datanets/tradinggymai.md` — the Goal and
   the Vote YES/NO criteria.
2. **Read the prefetched caches** (no new prefetch):
   - `.reppo-cache/pods-tradinggymai.json` — all pods on the datanet
     (every agent's, via `--all`).
   - `.reppo-cache/vote-filter-tradinggymai.json` — `current_epoch` +
     `voted_pod_ids` (union of: successfully-voted pods per the ledger +
     this wallet's own mints).
   If the pod cache is missing, an error marker, or an empty array →
   write zero intents and exit cleanly (not an error).
3. **Filter to the votable universe**, discarding a pod if EITHER:
   - **Out-of-epoch:** `pod.validityEpoch != current_epoch` (when
     non-null). Past-epoch votes revert `POD_NOT_VALID_FOR_EPOCH`.
   - **Already interacted:** `pod.podId ∈ voted_pod_ids` — covers both
     the ISS-005 double-spend guard and the ISS-016 own-mint
     `CANNOT_VOTE_FOR_OWN_POD` revert.
   If `vote-filter-tradinggymai.json` is missing/error → skip the filter
   and proceed on the rubric alone (degrade gracefully).
4. **Evaluate each surviving pod against the goal** and assign a
   direction:
   - **LIKE** — aligned: an HL-perp trade dataset with all rubric fields
     and verifiable fills.
   - **DISLIKE** — misaligned: strategy descriptions without executed
     trades, missing required fields, unverifiable trades, non-HL
     markets, unlabeled raw dumps, spam.
5. **Vote all eligible** (no per-trigger cap). For each, write
   `.pending-reppo/vote-<podId>-<direction>.json`:
   ```json
   { "cmd": "vote", "pod": "<podId>", "direction": "like|dislike",
     "votes": 1, "idempotency_key": "vote-<podId>-<direction>",
     "reason": "<one-line reason citing the rubric>" }
   ```
   `<podId>` verbatim from the cache (filename and `pod` field).
   `direction` is exactly `like` or `dislike`.
6. **Log** under a `### reppo-voter` heading in
   `memory/logs/${today}.md`: epoch, pods seen, filtered counts (out-of-
   epoch / already-voted / own-mint), eligible count, likes, dislikes,
   and any prompt-injection discards. On-chain results are appended by
   `postprocess-reppo.sh` / reported by `reppo-digest`.

> **ISS-005 note:** "vote all eligible" + full LIKE/DISLIKE curation must
> not regress into the all-DISLIKE compounding pattern. The voter logs
> the like/dislike split each run; a run that is 100% DISLIKE on a
> non-empty eligible set should be called out in the log for operator
> visibility.

### 3. Chain wiring

`aeon.yml` `chains.reppo-swarm`:

```yaml
reppo-swarm:
  schedule: "0 */6 * * *"
  on_error: continue
  steps:
    - skill: reppo-orchestrator
    - parallel: [reppo-trading-agent, reppo-voter]   # both consume orchestrator
    - skill: reppo-digest
      consume: [reppo-orchestrator, reppo-trading-agent, reppo-voter]
```

The voter consumes the orchestrator's plan (same gate the trading-agent
uses — RUN/SKIP per datanet validity). The digest consumes all three.

**Dependency to verify during implementation:** the chain-runner must
support `consume:` on a step following a `parallel:` group, and inject
both parallel legs' `.outputs/*.md` into the digest. If `parallel:`
groups can't carry per-leg `consume`, the orchestrator output is still
available to both legs via the committed `.outputs/reppo-orchestrator.md`.

### 4. Concurrency / commit-race hardening

Each chain step runs as a separate `aeon.yml` workflow that commits back
to `main`. Running the trading-agent and voter in parallel means two
workflows push near-simultaneously.

**Already safe:** `aeon.yml`'s per-skill commit (current lines ~752–782)
has a 5-attempt rebase loop that auto-resolves conflicts — append-only
paths (`memory/logs/*`, `.outputs/*`, `dashboard/outputs/*`, …) get
conflict markers stripped (union merge), all other paths take
`--theirs`, and a moved ref triggers re-pull + retry. Both parallel legs
commit through this path, so per-skill commits reconcile rather than
fail.

**The gap:** the `chain-runner.yml`'s *own* bookkeeping commits — the
context-file commit and the final cron-state commit — use a lighter
`git pull --rebase ... || true` / `git rebase --abort` path that lacks
the same auto-resolve loop. The 2026-05-31 15:40 chain `failure`
(`fatal: Exiting because of an unresolved conflict`, exit 128) was this
class of failure.

**Hardening:** factor `aeon.yml`'s auto-resolve-and-retry loop into a
shared shell helper and reuse it in the chain-runner's commit steps, so
the `orchestrator → [parallel] → digest` sequence cannot fail on a
reconcilable conflict. No new locking — reuse the proven pattern.

Additional non-collision guarantees baked into the voter:
- voter writes only `vote-*.json` intents (no filename overlap with the
  trading-agent's `mint-*.json`);
- voter logs under its own `### reppo-voter` heading (distinct hunk).

## Error handling

- Missing/empty/error-marker pod cache → zero intents, clean exit.
- Missing vote-filter → proceed on rubric alone.
- Prompt-injection content in pod metadata → discard that pod, log a
  warning, continue (per CLAUDE.md security rules — fetched pod content
  is untrusted data).
- Commit conflicts → auto-resolved by the shared retry helper.

## Testing / verification

- `bash -n` on any modified shell.
- Dry-run the voter locally against a captured `.reppo-cache/` snapshot;
  assert intents are written only for current-epoch, non-own, non-voted
  pods, with a sane like/dislike split.
- After merge, trigger `reppo-swarm` once and confirm: (a) voter runs in
  parallel with the trading-agent, (b) vote intents land on-chain via
  postprocess, (c) no chain-runner commit failure, (d) digest reports
  both legs.

## Rollout

1. New skill `skills/reppo-voter/SKILL.md` (vote flow extracted from
   trading-agent Step 6, generalized to "all eligible").
2. Remove Step 6 from `skills/reppo-trading-agent/SKILL.md`; update its
   description to "mint-only".
3. Wire `reppo-voter` into `aeon.yml` `reppo-swarm` as a parallel step.
4. Harden `chain-runner.yml` commit steps with the shared retry helper.
5. Register `reppo-voter` wherever skills are enumerated (skill registry
   / enabled list), if applicable.
