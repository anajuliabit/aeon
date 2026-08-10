# Week in Review: Fuzzing lands, catalog clears 70, spec-form takes over

*2026-08-10 — Weekly shipping update*

> The vuln-scanner started running cargo-fuzz harnesses on repos it never wrote, the skill catalog cleared 70 with five new operator skills plus community-pack machinery, and Aeon migrated wholesale off its bespoke skill frontmatter onto the Agent Skills spec.

## What Shipped

### Vuln-scanner starts fuzzing binaries it never wrote

For its entire life the vuln-scanner has been static-only: semgrep, trufflehog, osv-scanner — tools that read files without ever executing anything. That misses the class of bug where a panic only shows up on one specific malformed input. As of this week the scan arm walks the target repo for existing `cargo fuzz` harnesses and runs them (#863, `f8c5049`). The SKILL.md change is small (104 lines + a lock update); the actual work happens because the runtime-side sandbox grant and toolchain staging landed alongside it in a separate PR that Svector-anu split out for a cleaner trust-boundary review (#868, `0d2ead1`).

Riding on top of that: `hunter-22`, a bounty-discovery skill that pulls candidates from ClawHunter's free API, matches them against demonstrated capabilities (code, security-research, dependency-analysis), drops the content/social-growth work wearing a bounty costume, and hands qualifying targets over to vuln-scanner for a one-tap audit (#864, `d11f662`). The two together turn "find a bounty" and "prove there's a bug" into one operator gesture instead of two disconnected skills.

### Catalog clears 70, community-pack path becomes real

The single biggest diff of the week was `feat(skills): add spend-watch, competitor-monitor, higgsfield, remotion, weekly-aeoncard` — five skills ported from the `aeon-dev` instance into the framework and genericized for any operator (#860, `e4a5a24`, +6,542 lines across 36 files). `spend-watch` attributes cloud cost across Neon, Vercel, Railway, and GitHub Actions; the others cover competitor tracking, image and video generation via Higgsfield and Remotion, and a weekly aeon-card summary.

That bumped the catalog from 68 → 73, and the docs stopped chasing the exact digit across six unguarded surfaces — the headline is now a stable `60+` floor (#859, `8ffcb57`). `video-script` from external contributor NurstarK (#835, `db6c51d`) adds a receipts-first video-script generator that verifies every number and address against the live source before writing a line. `pack-submit` and `aeon-update` (#831 `3da9b1f`, `463b642`) close the loop for community packs — a local skill can be published as a pack, and installed instances can pull upstream updates without a manual re-fork. The first external pack under the new machinery arrived same-week: `Skim Clean Reads`, pay-per-call web reads via x402 (`fc05537`, JessieJanie).

### Agent Skills spec-form replaces OKF; traces + a Buzz channel come online

The largest structural change of the week is `Adopt Agent Skills spec form; remove OKF globally` (#824, `e1d9284`) — 154 files touched, +1,301 / −1,956, spanning `aeon.yml`, every `skills/*/SKILL.md` frontmatter, `bin/`, `catalog/`, and the docs. The old bespoke OKF (Operator Knowledge Format) headers are gone; skill files now match the Agent Skills spec that external tools can read directly. This is the change that makes `pack-submit` and community packs interoperate at all — the spec-form pivot is the substrate the whole catalog theme sits on.

OpenTelemetry landed on the Node entry points and non-claude harnesses in the same window (#821, `0e8e921`, +4,556 across 20 files), with the follow-on fix for the correct epoch encoding shipped the next day (#823, `32afd85`). Notifications gained a new outbound channel: **Buzz** joins Telegram / Discord / Slack in the `./notify` fan-out (#822, `86d09cd`) — same opt-in-via-secret pattern as the others, no code path changes required for skills that already call `./notify`.

## Fixes & Polish

- `bin/add-skill` had been broken for every repo using the standard `skills/<slug>/SKILL.md` layout — `find -maxdepth 2` never matched depth-3, so every install said "no skills found." Fixed in #866 (`0dd47a9`).
- `fix(ci): build ALL_SECRETS from an explicit allowlist, not toJSON(secrets)` (#819, `31e6a64`) — prior code was leaking every repo secret into the env; allowlist tightens it.
- `feat(memory-flush): stamp consolidation date, adaptive window, dedup, log rotation` (#828, `b28a005`) — the reflect skill's counterpart gets an idempotency stamp and stops re-processing the same window.
- `fix(webhook): clear 6 Dependabot alerts` (#826, `15fef7b`) — undici + `@opentelemetry/core` bumps.
- `ci: state egress-parser scope; gate lockfile coverage` (#839, `adeb069`) — the CI gate now fails a PR when a new skill lands without an `eyebrowlock.json` entry.
- `ci: add eyebrow capability-integrity gate for skills` (#815, `2353ebd`) — capabilities declared in SKILL.md now cross-check against the lockfile.

## What's Nearly Here

Autonomy-Labs-Tech's `taskmarket-delegate` skill sits open at #865 — browse/create/submit TaskMarket tasks, the only open PR after the operator's Sunday-batch collapsed the queue from 5 to 1.

---

**Stats:** 51 commits · 28 PRs merged · 0 releases · 0 issues closed · +16,617 / −2,128 lines · contributors: aaronjmars, Svector-anu, Autonomy-Labs-Tech, NurstarK, alexverify, JessieJanie
**Sources:** https://github.com/aaronjmars/aeon · commits=ok · prs=ok · releases=ok · issues=ok · open_prs=ok
