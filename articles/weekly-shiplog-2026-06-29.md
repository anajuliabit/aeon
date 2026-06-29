# Week in Review: Runtime Hardens, Security Gate Lands

*2026-06-29 — Weekly shipping update*

> Aeon stopped trusting its own filesystem this week: cron state and health priorities now live in GitHub Issues, and a new pre-install security verdict has to clear before any external skill reaches the agent.

## What Shipped

### Cron state and votable health move into GitHub Issues
The hardening port from `aeon-dev` landed as three stacked PRs that change where Aeon keeps its operational state. #547 brought the easy wins first — a shared notify formatter, `compact_logs`, `verify_output`, `schedule_clusters`, and `prune_skills` — a 1,293-line port across 15 files behind a new `ci-tests` gate. #548 followed with the keystones (still off-by-default): §6 capability tiers for skill permissions, §3 issues-as-state for cron tracking, and §7 votable health Issues, touching 38 files. #550 then flipped §3 and §7 on by default in `dual` mode — every run event now appends to a pinned `aeon:cron-state` Issue *and* still writes `cron-state.json`, so the JSON can be retired once the Issue path is proven (`scripts/state_store.sh`, `.github/workflows/aeon.yml`). Two follow-up fixes were needed: #552 caught that `null != '0'` in GitHub Actions `if:` coerces to false, which had silently disabled votable health for everyone with `HEALTH_ISSUES` unset; #553 gave `chain-runner.yml` the `issues: write` scope it needed to actually call the Issues API. #554 then documented the user-visible pieces — `HEALTH_ISSUES`, per-skill `health: <skill>` Issues, and the 👍/👎 voting that sets repair priority.

### Phylax becomes the pre-install verdict for external skills
The `phylax-audit` skill landed (#537) and immediately got wired into the skill installation flow. It returns a deterministic **ALLOW / WARN / DENY** verdict on any external skill *before* `./add-skill` touches the repo, merging three independent scans: a static pass over the remote `SKILL.md` for prompt-injection patterns and secret-exfil, an on-chain check on any Base contract addresses referenced, and an endpoint check on declared x402 / API bases. Three days later, #544 (`feat(skill-triage)`) bolted that pre-screen onto inbound skill PRs — for any `SKILL.md` in the diff that references a `0x…` address or a payment/data endpoint, `skill-triage` now inline-executes Phylax's on-chain, endpoint, and obfuscation dimensions and folds the verdict into the existing `skill-scan` static pass. The week closed with #545 quoting Phylax's example threat strings as inline-code so content scanners stop flagging the skill's own documentation as live payloads.

### The dashboard stops surfacing Dependabot
The Actions tab was running ~37% Dependabot noise — five ecosystems, one PR per dependency, weekly, with every merge to `main` re-evaluating everything and fanning out for days. #541 grouped Dependabot updates per-ecosystem and switched to monthly, which is why this week's six bot PRs (#532–#536, plus one straggler) landed as a single Monday batch instead of trickling all week. #542 then fixed the dashboard feed: `/api/runs` was using a blocklist that missed Dependabot's `dynamic` event type, so the FEED and RUNS tabs were still flooded. The blocklist became an allowlist (`push`, `pull_request`, `schedule`, `workflow_dispatch`) and Dependabot rows disappeared from both views — `apps/dashboard/lib/runs.ts` is where the actual filter sits. #540 piggy-backed an 8-dimension code-quality audit on the same area; the headline was that very little needed fixing, but it did surface one real load-error UX bug in the dashboard.

## Fixes & Polish
- `vuln-scanner` was calling `POST /security-advisories` (the *create* endpoint, which 403s on any repo you don't own); switched to `POST /security-advisories/reports`, pinned API version `2022-11-28` (#557).
- `scripts/validate-config.js` actually exists now — `config-validator`'s `SKILL.md` had been calling it as a fast path, but the script had never been committed (#546).
- `clawhunter-skills` community pack listing refreshed to v0.2 — multi-venue support (Pump Fun GO, tiny.place, EarnFi, Atelier), per-bounty `agentPlan`, new research tools (#555).
- `apps/dashboard/README.md` added — the dashboard was the only sub-app without a README, despite being the operator's primary surface (#543).
- `AeThree` and `Phylax` added to `ECOSYSTEM.md` (#556, #539).

## What's Nearly Here
**Phylax hosted-engine fast path** (#559) is open from `@usephylax` — adds a canonical hosted-engine path to `phylax-audit` so verdicts don't have to recompute the three scans locally. **CI wiring for the new validator** (#560) plugs `validate-config.test.js` into the `ci-tests` gate that #547 introduced. **Vigil skill refresh** (#558) takes its tool count from 9 to 17.

## Momentum Check
Last week: 58 commits · 58 PRs merged · +3,300 / −3,920. This week: 23 commits · 23 PRs · +3,176 / −442. Commit count is down by more than half, but lines-added is barely off — the work shifted from broad surface-level changes (packs rollout, prune sweep) to deeper infrastructure changes that touch fewer files harder. Net positive on lines for the first time since the prune two weeks ago.

---

**Stats:** 23 commits · 23 PRs merged · 1 issue closed · +3,176 / −442 lines · 87 files · contributors: aaronjmars, usephylax, SamsShow, clawhunter, anajuliabit, vigilcodes, dependabot[bot]
**Sources:** https://github.com/aaronjmars/aeon · commits=ok · prs=ok · releases=ok · issues=ok · open_prs=ok
