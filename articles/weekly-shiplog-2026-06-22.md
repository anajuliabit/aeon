# Week in Review: Packs Replace the Flat Skill List

*2026-06-22 — Weekly shipping update*

> the skill catalog stopped being one flat list of 202: it's a Core pack on by default plus opt-in packs now, with a one-click install path that five outside contributors already shipped onto.

## What Shipped

### From a flat skill list to packs
First-party packs landed as the new shape of the catalog (#474). Skills now carry a `category:` in their `SKILL.md` frontmatter and get authored into packs from that field — 198 files changed in one sweep to backfill every existing skill (#475). The dashboard followed: the sidebar defaults to *enabled* skills only (#477), packs became a visibility lens that filters the roster rather than a bulk on/off switch (#478), and only Core is on by default (#479). Forks now scope `enabled-packs` per-repo so a freshly forked Aeon starts Core-only instead of inheriting whatever the upstream had checked (#491). Same week, 20 redundant or one-shot skills got pruned to land the catalog at 182 (#473) — a 3,765-line deletion across 26 files — and #530 then synced the README count to 183 after `install-skill` joined Core.

### One-click community pack install, with five packs already on it
The dashboard got an "add more packs" button that drives a one-click install for community packs (#483); `install-skill-pack` now regenerates `packs.json` so a fresh install actually shows up in the roster (#487); `install-skill` got zero-touch auto-merge wired up and the Actions perms to open its own PRs (#485); installed community packs land in an always-visible "Installed" group rendered from data, not hard-coded (#486, #490); and a `scripts/validate-pack.sh` local pre-flight (#495, 292 lines) catches pack errors before a contributor opens a PR. Five external packs landed on top of it the same week: **Glim.sh** live-data MCP (#470, by `@tenequm`), **Hunch Prediction Markets** (#472, by `@rajkaria`), **ClawHunter** (#498), **Polymarket Trader by Simmer** (#499, by `@adlai88`), and **Charon for AEON** (#511, by `@CharonAI-code`) — a workflow-preflight policy layer that evaluates `charon.aeo` before the selected skill reaches Claude. The MCP catalog also gained **Robinhood Agentic Trading** (#489) and **Litebeam** (#508).

### Dependency hygiene wired into the repo
`.github/dependabot.yml` landed for npm across `apps/dashboard`, `apps/mcp-server`, `apps/a2a-server`, `apps/webhook` plus every GitHub Actions workflow (#513) — and the queue cleared in a single afternoon: `next` 16.2.6 → 16.2.9 (#524), `typescript` 5.9.3 → 6.0.3 across the mcp + a2a servers (#518, #521), `tailwindcss` 4.2.2 → 4.3.1 (#523), `gsap` 3.14.2 → 3.15.0 (#520), `yaml` 2.8.3 → 2.9.0 (#525), `actions/checkout` 4 → 7 (#514), `actions/setup-node` 5 → 6 (#515), `wrangler` 4.98 → 4.103 (#522), plus `@json-render/*` aligned on `^0.19` so the tree stops carrying two copies of `@json-render/core` (#516, #526). LICENSE copyright moved from `Aaron Elijah Mars` to `Aeon Inc` (#529).

## Fixes & Polish
- `install-skill-pack` was regenerating `packs.json` but the `--path` flag wasn't being forwarded to the install command, so packs were invisible after install (#493).
- `skills.json` got decoupled from `aeon.yml` — the leftover `schedule` field went, since `aeon.yml` already owns scheduling (#484).
- Litebeam's SVG didn't render well in the catalog's 36px logo slot — swapped to the X-profile JPEG to match how the other featured entries render (#509).
- Five follow-up cleanups for the 6-15 prune: `token-report`, `token-alert`, `defi-monitor`, `wallet-digest`, `feature`, `ecosystem-entrants`, and `competitor-radar` no longer leave dangling references in `SKILL.md`, `aeon.yml`, the status page, or the gallery (#503, #504, #505, #506, #531) — closes the `token-report`-orphan ticket (#502).
- `SECURITY.md` added with the disclosure policy and threat model (#471).

## What's Nearly Here
**BEAMR as an LLM gateway** (#418) is still open — the seventh provider for the cascade shipped last week. **LENS skill pack** (#510) is the next community pack queued behind the five that already landed.

## Momentum Check
Last week: 113 commits · 109 PRs merged · +11,602 / −4,784. This week: 58 / 58 / +3,300 / −3,920 — fewer commits, and net negative on lines for the first time in a while. The 20-skill prune (#473) is most of the deletion; the rest is the dangling-reference cleanup. The center of gravity moved from *adding* providers and skills to *shaping* what's already there into packs.

---

**Stats:** 58 commits · 58 PRs merged · 1 issue closed · +3,300 / −3,920 lines · 300 files · contributors: aaronjmars, tenequm, rajkaria, clawhunter, adlai88, logbookbase, CharonAI-code, dependabot[bot]
**Sources:** https://github.com/aaronjmars/aeon · commits=ok · prs=ok · releases=ok · issues=ok · open_prs=ok
