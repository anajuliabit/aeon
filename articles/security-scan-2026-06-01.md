---
title: Security Scan — 2026-06-01
date: 2026-06-01
generator: skill-security-scan
---

# Security Scan — 2026-06-01

**Verdict:** ATTENTION
**Scope:** full corpus (skills/*/SKILL.md, skills/*/*.sh|*.py, .github/workflows/*.yml, scripts/*.sh)
**Counts:** 145 files scanned · 6 HIGH · 14 MEDIUM · 4 LOW · **2 NEW HIGH** · **1 RESOLVED HIGH** · 4 PERSISTENT HIGH

First delta-eligible run after the 2026-05-25 baseline bootstrap. Scanner
was blocked from direct execution by the sandbox approval gate (same
condition as bootstrap), so the inline-Grep fallback from `SKILL.md` step 4
was applied — never silently skipped.

## Needs attention (NEW high-severity this run)

### ISS-017 · chain-runner.yml — `${{ inputs.chain }}` interpolated into `run:` shell

| Line | Snippet |
|------|---------|
| `.github/workflows/chain-runner.yml:41` | `CHAIN="${{ inputs.chain }}"` inside the `Run chain` step's `run: \|` |
| `.github/workflows/chain-runner.yml:416` | `CHAIN="${{ inputs.chain }}"` inside the `Update cron state` step's `run: \|` |

**Threat class.** Same 2026-04-11 incident pattern that produced the
messages.yml fix. A chain name carrying shell metacharacters would expand
into the shell context rather than a quoted env-var. Real-world exposure
today is low — the only trigger paths are `workflow_dispatch` (write-auth
required) and a YAML-level concurrency-group expansion at line 17 (not
executed). But the anti-pattern is the same as the lines aeon.yml has
carried since baseline, and the canonical messages.yml fix is right there
to copy.

**Remediation (mirror messages.yml:586-595).**
```yaml
- name: Run chain
  env:
    GH_TOKEN: ${{ secrets.GH_GLOBAL || secrets.GITHUB_TOKEN }}
    _CHAIN: ${{ inputs.chain }}
  run: |
    set -euo pipefail
    CHAIN="$_CHAIN"
    # ...
```

Apply the same `_CHAIN: ${{ inputs.chain }}` env-binding to the
`Update cron state` step (line 411-468) and replace line 416's direct
interpolation with `CHAIN="$_CHAIN"`. Lines 2 (`run-name:`) and 17
(`concurrency.group:`) are YAML-level fields, not shell — leave as-is.

Tracking: **ISS-017** (filed this run by `skill-security-scan`).

## Resolved since last scan

### messages.yml:578 → fixed via `env:` indirection ✅

The 2026-05-25 baseline flagged `${{ github.event.action }}` interpolated
directly into the `run:` block at messages.yml:578. The current file binds
**every** template expression (`inputs.message`, `inputs.source`,
`github.event_name`, `github.event.action`, `github.event.client_payload.message`)
to `env:` keys (`_INPUT_MESSAGE`, `_INPUT_SOURCE`, `_EVENT_NAME`,
`_EVENT_ACTION`, `_PAYLOAD_MESSAGE`) at lines 586-591, and the shell at
lines 592-655 reads `$_EVENT_NAME` / `$_PAYLOAD_MESSAGE` / `$_INPUT_SOURCE`
etc. — the canonical 2026-04-11 fix shape. No open ISS existed for this
finding (baseline was bootstrap mode), so nothing to flip in `INDEX.md`,
but the messages.yml hardening is the standout improvement this week.

## Persistent findings (unchanged)

| File:Line | Pattern | Why it persists |
|-----------|---------|-----------------|
| `.github/workflows/aeon.yml:86` | `inputs.skill` direct in `run:` | Baseline-noted, workflow_dispatch-gated. No PR yet. |
| `.github/workflows/aeon.yml:94` | `steps.skill.outputs.name` direct in `run:` | Derived from `inputs.skill`, same risk profile. |
| `.github/workflows/aeon.yml:96` | `steps.skill.outputs.name` direct in `run:` | Same. |
| `.github/workflows/aeon.yml:725` | `steps.work.outputs.label` direct in `run:` | Was line 718 at baseline — code added above shifted line, anti-pattern intact. |

Recommended fix: bind these via `env:` (e.g. `_SKILL_NAME: ${{ steps.skill.outputs.name }}`)
and let the shell read `$_SKILL_NAME`. The pattern aeon.yml has used for
years pre-dates the `env:` indirection convention; it's eligible for the
same one-shot sweep that fixed messages.yml.

## Per-file results

| File | Status | HIGH | MEDIUM | LOW | Delta |
|------|--------|------|--------|-----|-------|
| `.github/workflows/aeon.yml` | FAIL | 11 | 1 | 0 | PERSISTENT |
| `.github/workflows/chain-runner.yml` | FAIL | 2 | 0 | 0 | **NEW** |
| `.github/workflows/messages.yml` | WARN | 8 | 1 | 0 | RESOLVED (line 578) |
| `.github/workflows/replicate-oneoff.yml` | PASS | 0 | 0 | 0 | NEW FILE (clean) |
| `.github/workflows/sync-upstream.yml` | PASS | 0 | 0 | 0 | unchanged |
| `scripts/postprocess-reppo.sh` | WARN | 9 | 0 | 0 | unchanged (echo-string false positives) |
| `scripts/prefetch-xai.sh` | WARN | 2 | 0 | 0 | unchanged |
| `scripts/postprocess-admanage.sh` | WARN | 1 | 0 | 0 | unchanged |
| `scripts/postprocess-admanage-create.sh` | WARN | 2 | 0 | 0 | unchanged |
| `scripts/postprocess-replicate.sh` | WARN | 2 | 0 | 0 | unchanged |
| `scripts/postprocess-devto.sh` | WARN | 1 | 0 | 0 | NEW FILE (standard API header) |
| `scripts/postprocess-farcaster.sh` | WARN | 1 | 0 | 0 | NEW FILE (standard API header) |
| `scripts/prefetch-hl.sh` | WARN | 3 | 0 | 0 | NEW FILE (public Hyperliquid API, no auth) |
| `scripts/prefetch-reppo.sh` | PASS | 0 | 0 | 0 | NEW FILE |
| `scripts/prefetch-vibecoding.sh` | WARN | 3 | 0 | 0 | NEW FILE (ISS-015 fix — oauth.reddit.com) |
| `scripts/generate-feed.sh` | PASS | 0 | 0 | 0 | NEW FILE |
| `scripts/reppo-lock.sh` | PASS | 0 | 0 | 0 | NEW FILE |
| `scripts/sync-site-data.sh` | PASS | 0 | 0 | 0 | NEW FILE |
| `scripts/sync-upstream.sh` | WARN | 0 | 1 | 0 | unchanged |
| `notify` | WARN | 0 | 1 | 0 | unchanged |
| `skills/skill-security-scan/scan.sh` | WARN | 9 | 0 | 0 | self-reference (pattern definitions) |
| `skills/skill-security-scan/SKILL.md` | WARN | 17 | 0 | 0 | baseline-suppressed |
| `skills/security-digest/SKILL.md` | WARN | 5 | 0 | 0 | baseline-suppressed + code-fence |
| `skills/monitor-runners/SKILL.md` | WARN | 2 | 0 | 0 | code-fence downgrade applied (eval in ```bash fence) |
| `skills/competitor-launch-radar/SKILL.md` | WARN | 1 | 0 | 0 | unchanged (security-advice quote) |
| `skills/fork-release-tracker/SKILL.md` | WARN | 1 | 0 | 0 | unchanged |
| `skills/research-brief/SKILL.md` | WARN | 1 | 0 | 0 | unchanged |
| `skills/deep-research/SKILL.md` | WARN | 1 | 0 | 0 | unchanged |
| `skills/last30/SKILL.md` | WARN | 1 | 0 | 0 | unchanged |
| `skills/repo-actions/SKILL.md` | WARN | 1 | 0 | 0 | unchanged |
| `skills/fork-skill-gap/SKILL.md` | WARN | 1 | 0 | 0 | unchanged (data-vs-code JSON example) |

All other 113 `SKILL.md` files: PASS.

## Coverage notes

- **Trusted-source downgrade:** the active git remote is `anajuliabit/aeon`,
  which is NOT in `skills/security/trusted-sources.txt` (entries:
  `aaronjmars`, `aaronjmars/aeon`, `aaronjmars/aeon-agent`). No skill files
  carry an `origin:` frontmatter field. Therefore zero skills were
  downgraded to format-only this run — every file got the full pattern
  sweep.
- **Code-fence downgrade:** applied to `skills/monitor-runners/SKILL.md`
  (lines 74, 77 — `eval` inside a ```bash code fence; `$NETWORKS` is an
  internal controlled list, not user input).
- **Baseline suppression:** 8 seed entries in
  `skills/security/scan-baseline.yml` filter the self-documenting
  prompt-override patterns in `skill-security-scan/SKILL.md` and the
  example curl-with-secret blocks in `security-digest/SKILL.md`. No new
  suppressions auto-added.
- **3 NEW SKILL.md files** + **5 NEW scripts** + **1 NEW workflow**
  (`replicate-oneoff.yml`) since baseline. The new workflow is clean
  (`env:` indirection used correctly at lines 52-55). The new scripts are
  standard API-call patterns (api-key in header, payload from local file).

## Appendix — all current real HIGH findings

```
.github/workflows/aeon.yml:86       PERSISTENT  inputs.skill in run:
.github/workflows/aeon.yml:94       PERSISTENT  steps.skill.outputs.name in run:
.github/workflows/aeon.yml:96       PERSISTENT  steps.skill.outputs.name in run:
.github/workflows/aeon.yml:725      PERSISTENT  steps.work.outputs.label in run: (line drift from baseline :718)
.github/workflows/chain-runner.yml:41   NEW     inputs.chain in run:     [ISS-017]
.github/workflows/chain-runner.yml:416  NEW     inputs.chain in run:     [ISS-017]
```

Exit status: `SECURITY_SCAN_NEW`
