# Week in Review: taskmarket delegation lands, add-skill unbreaks

*2026-08-17 — Weekly shipping update*

> A quieter week after last week's spec-form migration and catalog surge: aeon gains a delegation primitive that hands work to an external agent-worker market, and the `bin/add-skill` installer that had been quietly broken for every downstream repo since launch gets fixed.

## What Shipped

### aeon can now delegate to an outside agent market

`taskmarket-delegate` is the substantive new skill of the week (#865, `1183057`, +344 / −5). External contributor Autonomy-Labs-Tech landed a self-contained skill that wires aeon into the TaskMarket agent-worker market (`tasks.taskmarket.dev` / `api.taskmarket.dev`) as a delegation target — instead of burning inference on unreliable or low-confidence work, the agent can browse open tasks, create new ones, or submit results.

The skill ships in three modes. `browse` is keyless — it fetches and ranks open TaskMarket tasks winnable-first (lowest submission count wins the top rows). `create` and `submit` are key-gated for real interaction. The runtime is a small Node script (`skills/taskmarket-delegate/scripts/taskmarket.js`, 84 lines) with a matching test file (`tests/test-taskmarket.js`, 55 lines) — light, no framework baggage. The skill lands with a full lockfile entry (+97 lines in `eyebrowlock.json`), a catalog icon, and doc/pack entries, so it moves through the `ci-skills-json` and eyebrow-integrity gates cleanly.

What this shifts: aeon's catalog has been almost entirely about doing work locally in Claude Code or delegating to LLM providers. This is the first skill that treats a public agent marketplace as another executor — a router option, not a subordinate model. It complements the `pack-submit` / `aeon-update` community-pack machinery that shipped last week: one publishes skills outward, this one dispatches work outward.

### bin/add-skill was broken for every downstream repo — now it isn't

`fix(add-skill): enumerate and install skills under skills/ (was broken for all repos)` is 14 lines of diff (#866, `0dd47a9`, +11 / −3) fixing a bug that quietly disabled the installer for every fork of this repo. Discovery ran `find "$REPO_DIR" -maxdepth 2 -name SKILL.md`, but the standard layout is `skills/<slug>/SKILL.md` at depth 3 — so every external install returned "no skills found." The install path had the mirror bug: `src="$REPO_DIR/$skill"` missed the `skills/` subdir. Both fixed together, `-maxdepth` bumped to 3 and the source path corrected. This is the kind of fix where the LoC count understates the blast radius — every operator running `add-skill` against a repo shaped like this one was hitting the failure until this landed.

## Fixes & Polish

- `fix(deps): patch nanoid advisories via lockfile bump` (#871, `573f06c`) — dashboard lock-only bump for the nanoid CVE, no `package.json` change.
- `docs: add Finance District to ECOSYSTEM.md` (#869, `c366b5b`) — one row, alphabetized between Echo Oracle and GitBlock; Finance District's Agent Wallet went live as a supported wallet 2026-08-05.
- `docs: sync PRs #795-#871 to aeon docs` (#873, `c6faeb8`) — closes the docs-sync ledger gap after the true watermark (website changelog, #864) had drifted past the in-repo stragglers.
- `chore(vuln-scanner): stage cargo-fuzz toolchain + widen sandbox grant` (#868, `0d2ead1`) — the runtime-half of last week's cargo-fuzz feature (#863), split out for a separate trust-boundary review and merged into the window alongside the skill-scope change.

## What's Nearly Here

One open PR: Svector-anu's `fix(aeon-update): don't silently delete a currently-enabled skill retired upstream` (#874, opened 2026-08-16). The failure mode is exactly what the title says — the update path was capable of removing a skill an operator was actively depending on, if upstream had retired it. The fix is queued for the next batch.

## Momentum Check

Last week (weekly-shiplog 2026-08-10): 51 commits · 28 PRs merged · +16,617 / −2,128 lines · 6 contributors. This week: 7 commits · 7 PRs merged · +556 / −21 lines · 4 contributors. A one-week 7× drop in both commit and PR count, with almost all of last week's throughput concentrated in the OKF→Agent Skills spec migration (#824, 154 files) and the five-skill catalog port (#860, +6,542 lines). This week is the post-surge tail: one substantive new skill from an external contributor, one bug fix with wide blast radius, three polish PRs. Not stalled — repointed to smaller-shaped work.

---

**Stats:** 7 commits · 7 PRs merged · 0 releases · 0 issues closed · +556 / −21 lines · contributors: aaronjmars, Autonomy-Labs-Tech, Svector-anu, raul1stdigital
**Sources:** https://github.com/aaronjmars/aeon · commits=ok · prs=ok · releases=ok · issues=ok · open_prs=ok
