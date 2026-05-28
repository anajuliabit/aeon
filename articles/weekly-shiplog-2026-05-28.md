# Week in Review: Pack Registry Lands, Fleet Hits 156

*2026-05-28 — Weekly shipping update*

> aeon shipped a community skill-pack registry with a one-command install path, folded 34 derivative-fork skills back into the public framework, and stood up three new self-observability skills — total schedulable skill count now sits at 156.

## What Shipped

### a pack registry and one-command install

the week's center of gravity is `install-skill-pack` (#213) — a single CLI that reads a `skills-pack.json` manifest at any pack repo root, runs the security scanner against each declared `SKILL.md`, and installs approved skills with provenance recorded in `skills.lock`. one day later `skill-packs.json` (#215, sha `ac43d46`) lands as a machine-readable mirror of the README registry, with `--list` browsing wired into the same CLI. community packs land in waves: zer0 / gitbounty / AntFleet / LiquidPad bundled in (#218), Luca pack (#198), mythosforge (#228, then #236 / #248 to track pack expansion), signa (#241), noelclaw (#250), and seven sparkleware packs in a single PR (#249). `ECOSYSTEM.md` (#220) ships alongside as the canonical 39-project list of products built on aeon, distinct from the skill-pack registry.

### 34 skills ported back from forks, then actually wired in

PR #219 (`Port 34 skills from derivative aeon instances`, +6162 / −69) pulls skills built in `aeon-aaron`, `aeon-agent`, and `miroshark-aeon` back into the public framework — new files include `skills/agent-displacement/`, `batch-health/`, `builder-map/`, `compute-pulse/`, `config-validator/`, `disclosure-tracker/` and 28 more. two days later PR #230 closes the gap #219 left behind: the 34 skills landed in `skills/` and `skills.json` but were never registered in `aeon.yml`, so they couldn't schedule and didn't appear as dashboard toggles. #230 adds the 49-line `aeon.yml` block and syncs README counts and the splash image to 156 — only now is the port real.

### three new skills watching the fleet

`ecosystem-pulse` (#227, +416 lines) — weekly liveness check over `ECOSYSTEM.md`'s 39 projects, reports stars / forks / last-push recency / release activity per project. `fleet-skill-adoption` (#245, +359 lines) — leaderboard of which catalog skills are enabled across active forks, with top-15 / bottom-15 / "shipped into silence" zero-adoption / freshly shipped sections. `sparkleware-catalog` (#252, +300 lines) — turns the static `skill-packs.json` registry into a live-refreshed health feed enriched with current GitHub signals per pack. all three run weekly. all three measure the surface that landed earlier in the same week.

## Fixes & Polish

- opt-in Fleet Watcher authorization layer wraps the existing `Run` step in `.github/workflows/aeon.yml` with preflight + postflight calls against a self-hosted control plane (#200, +120 lines)
- workflow_dispatch shell-injection guard — `inputs.skill` was template-interpolated directly into `run:` bash bodies before bash quoting; #222 adds `env: INPUT_SKILL` validation against `^[a-zA-Z0-9_-]+$`
- Resend email-send step wired into `morning-brief` and `weekly-review`, HTML + plain-text per run, recipients via `$BRIEF_RECIPIENTS` (#205)
- two fleet-state hardening fixes from AntFleet review: `.bak` created before write + tmp validated before promote (#203), empty spotlight history no longer aborts the digest (#207)
- `v4-readiness` manifest reconciled with the skill's actual read set, closing Issue #184 H1 (#226)
- dashboard refactor: dedupe helpers, type consolidation, dead code removed (#255, +173 / −275)

## What's Nearly Here

two community PRs opened this morning sit downstream of the work that landed this week: `pr-skill-triage` (#259) — a structured receipt skill for inbound skill PRs, which plugs straight into the registry/install pipeline that hit `main` two days ago — and `liquidpad-launch` (#231), the first skill submission from the LiquidPad pack now that the install path exists.

---

**Stats:** 38 commits · 37 PRs merged · 2 issues closed · ~+9,100 / −430 lines · contributors: aaronjmars, antfleet-ops, ryjin111, codexvritra, sparkleware, noelclaw, danbuildss, wx888, opengrid1, 0xShak, liquidpadbot, Yehor Kaliberda
**Sources:** https://github.com/aaronjmars/aeon · commits=ok · prs=ok · releases=ok · issues=ok · open_prs=ok
