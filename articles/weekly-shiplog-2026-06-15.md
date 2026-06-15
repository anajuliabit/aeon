# Week in Review: Aeon Stops Depending on One LLM

*2026-06-15 — Weekly shipping update*

> Aeon went from a single hardcoded model to a runtime gateway that picks a provider from whatever keys you've set and fails over across seven of them — the week's center of gravity was making the agent provider-agnostic.

## What Shipped

### Multi-provider LLM gateway with automatic failover
The biggest change this week: Aeon no longer assumes one model. A new gateway resolves which LLM provider to use at run time from whichever secrets are present (#430), and added OpenRouter, UsePod, Venice, and Surplus alongside the existing options (#409). If a provider fails mid-run, the gateway now cascades to the next available one instead of dying (#435) — the change touches `apps/dashboard/lib/gateway.ts`, the auth route, and `scripts/llm-gateway.sh` across 15 files. By end of week the provider plumbing was consolidated into a single registry so there's one place that knows about all of them (#469), and sidecar providers were fixed to track Aeon's configured `$MODEL` instead of a model baked in at build time (#461).

### Lowering the on-ramp: soul and strategy builders
Setting up an agent's personality used to mean hand-writing files. Now there's a SOUL.md tab in the dashboard backed by a `soul-builder` skill that constructs a voice from an X handle, a name, or a few links (#448, ~1,000 lines added), plus a one-click gallery to install pre-made souls (#449). The same pattern landed for direction: a STRATEGY.md "north star every skill follows" (#370) got its own dashboard tab and `strategy-builder` skill (#451). Telegram setup got guided too — a one-click instant-mode Worker (#368) and a deploy wizard that prompts for the variables it needs (#404).

### Skills can now call MCP servers mid-run
Skills gained opt-in access to MCP servers while they execute (#372), turning the MCP catalog from a dashboard listing into something skills actually use during a run. That unlocked new skills built directly on it — `beamr-route` for pay-per-call inference over x402 with an onchain receipt (#419), `CTRL` for on-chain automation on Base (#353), and `vigil-revoke`, which closes the loop from detecting a bad approval to revoking it via Bankr (#354).

## Fixes & Polish
- Scheduler was silently skipping skills whose definitions had been reformatted to multiple lines — fixed, and catch-up widened to 2h so trailing-minute slots aren't dropped (#439, #440).
- `./notify -f` added for multi-line notifications, retiring the brittle `./notify "$(cat ...)"` pattern (#441).
- New CI gate fails any PR that edits a `SKILL.md` without regenerating `skills.json` (#457, #458) — closes issue #455.
- `wc-resale` was miscatalogued as `category: "other"`; the missing `get_category()` arm is now in place (#456, closes #454).
- Dashboard now surfaces `gh` failures instead of masking them as empty 200 responses (#364).
- Two rounds of code-quality cleanup across dedup, types, and dead code (#467, #468).

## What's Nearly Here
One open PR is close: BEAMR as an LLM gateway (#418) — the natural next entry in the provider cascade shipped above.

---

**Stats:** 113 commits · 109 PRs merged · 2 issues closed · +11,602 / −4,784 lines · contributors: aaronjmars, Sahil, Dax, ashneil12, vritra12, mnemedb, Zorrot Chen
**Sources:** https://github.com/aaronjmars/aeon · commits=ok · prs=ok · releases=ok · issues=ok · open_prs=ok
