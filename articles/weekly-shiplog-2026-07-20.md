# Week in Review: MCP goes production, ADK opens the door

*2026-07-20 — Weekly shipping update*

> mcp integrations moved from prototype to production this week: oauth stopped breaking on rotating-token providers, three new mcp skills swapped in for the retired ctrl skill, and the aeon developer kit landed for outside builders.

## What Shipped

### OAuth for MCP servers becomes durable

The dashboard now runs a real OAuth flow for MCP connectors — one-click connect, and the connection survives past token rotation. The foundation is a 900-line change in `apps/dashboard/lib/mcp-oauth.ts` (+232) plus a companion server module `apps/dashboard/lib/mcp-oauth-server.ts` (+80), two new API routes at `apps/dashboard/app/api/mcp-auth/route.ts` and `mcp-auth/callback/route.ts`, a test file `apps/dashboard/lib/mcp-oauth.test.ts` (+97), and reference docs at `docs/mcp-oauth.md` (+76) — all in #730. A follow-up (#732) makes refresh durable for providers that rotate the refresh token on every use — the class that used to silently strand you a day after connecting. The mechanics are recorded in the MCP catalog docs (#733), including the Robinhood-specific note on why `offline_access` isn't requested. Glim gets the one-click Connect wired up (#731), the McpPanel's status line is replaced with a proper PAT setup section (#737, `apps/dashboard/components/McpPanel.tsx`, 15 lines changed), and the PAT-setup URL is now clickable (#740). Together this is the shift from "MCP works if you're willing to reconnect daily" to "MCP works."

### Three new MCP skills, CTRL retires

The old `ctrl` skill (226 lines) is deleted and replaced by three focused MCP skills in the same PR (#734): `skills/robinhood-mcp/SKILL.md` for portfolio and holdings reads, `skills/glim-mcp/SKILL.md` for account access via the durable-refresh OAuth path built earlier in the week, and — added alongside in a separate PR (#736) — `skills/executor-mcp/SKILL.md` for Executor Cloud. Each new skill is roughly 60 lines; the swap is net -100 lines and one skill traded for three narrower ones. A same-day fix (#735) tightens both skills to one `./notify` call per run instead of the double-notify pattern the earlier draft had. Catalog and pack listings are updated in `catalog/skills.json` and `catalog/packs.json` in the same commits, and `apps/dashboard/lib/mcp-catalog.ts` picks up the new entries so they show in the dashboard's MCP panel out of the box.

### Aeon Developer Kit lands

Outside builders can now integrate with Aeon via a documented surface. #741 introduces the Developer Kit — build on Aeon through a GitHub App, the GitHub API, and skill packs — and #742 renames it to ADK (Aeon Developer Kit) and adds an Integrate Aeon section to the README. The three surfaces already existed as separate pieces; ADK is the framing that makes them one entry point for third parties. The skill-pack catalog was synced to reflect the current inventory of 61 skills across the packs, with Basics at 15 (#747), and the new MCP servers + skills got proper coverage in the catalog table, README packs, and `CONFIGURATION` (#739). The docs pass also picked up hyphen cleanup (#743), README polish (#748, #749, #750), and stripped the private aeon-connect repo references now that the public surface is the entry point (#749).

## Fixes & Polish

- Grok 4.5 support across the fleet, plus a migration of the deprecated `x_search` model to `grok-4.3` — touches `scripts/run-grok.sh`, `apps/dashboard/lib/constants.ts`, `docs/harnesses.md`, `scripts/tests/test_run_grok.sh`, and per-skill model references (#725). Companion cleanup (#728) drops `grok-build` from the picker and quiets benign harness log notices.
- Workflows now stamp `type:` frontmatter on OKF outputs before the auto-commit, closing a gap where downstream consumers saw untyped entries (#738, `.github/workflows/aeon.yml` + `messages.yml`).
- Typescript held on 6.x for the dashboard — Next 16 + TS7 breaks the build, so the dependabot bump to TS7 in `apps/dashboard` gets pinned back (#724). Non-blocking bumps (wrangler in `apps/webhook` #719, typescript in `apps/mcp-server` #718) went through cleanly.
- `chore(ci)`: attestation-gate log only fires when `attest=true` — quiets the noise on runs that don't need it (#729).
- `actions/cache@v4 → v6` — drops the Node 20 deprecation warning from every workflow (#726).
- Attribution updated to `aeonfun / Aeon Inc` across the repo (#721) — the corporate footprint the ADK announcement can point at.

## What's Nearly Here

Community skill pack submission from sparkleware (#723) — three skills bundled as a pack: `proof-of-loadout`, `aeon-pulse`, `eth-gas-watch`. First outside contributor pack lands in the catalog once merged. And #751 expands `validate-pack` test coverage from 3 to 20 cases (BBridgeers) — the pack-validation surface gets real teeth before the ADK opens the door wider.

---

**Stats:** 29 commits · 26 PRs merged · 0 issues closed · +1,692 / −355 lines · contributors: aaronjmars, dependabot[bot]
**Sources:** https://github.com/aaronjmars/aeon · commits=ok · prs=ok · releases=ok · issues=ok · open_prs=ok
