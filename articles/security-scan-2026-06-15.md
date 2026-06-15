# Security Scan — 2026-06-15

**Verdict:** ATTENTION
**Scope:** full corpus (123 skills · 7 workflows · 13 repo scripts · 8 advisor scripts · 1 companion script = 152 files)
**Counts:** 152 files scanned · 4 HIGH (post-filter, all persistent) · ~15 MEDIUM · ~4 LOW · 0 new · 2 resolved since last persisted state (2026-06-01)

**Scanner mode:** inline Grep fallback. `scan.sh` execution was blocked by the
sandbox approval gate (same edge case as the 2026-05-25 and 2026-06-01 runs).
Per SKILL.md step 4 + sandbox note, the scan was performed inline with Grep over
`scan.sh`'s exact HIGH/MEDIUM/LOW pattern library, plus a manual GitHub Actions
script-injection audit of every `${{ ... }}` expression interpolated into `run:`
blocks. Never silently skipped.

## Needs attention (NEW high-severity this run)

**None.** No new HIGH findings introduced since the last scan.

## Resolved since last scan

Two HIGH findings (ISS-017) cleared versus the 2026-06-01 persisted-state
snapshot — both `inputs.chain` direct interpolations in `chain-runner.yml`:

| File | Line (then → now) | Pattern | Status |
|------|-------------------|---------|--------|
| `.github/workflows/chain-runner.yml` | 41 → 41 | `CHAIN="${{ inputs.chain }}"` inside `run: |` | **RESOLVED** |
| `.github/workflows/chain-runner.yml` | 416 → 368 | `CHAIN="${{ inputs.chain }}"` inside `run: |` | **RESOLVED** |

Both `run:` blocks now bind `inputs.chain` through an `env: _CHAIN` rebind and
read `CHAIN="$_CHAIN"` from the shell body — the canonical 2026-04-11
`messages.yml` fix shape. Explicit `# ISS-017` comments document the rebind at
both sites (the "Run chain" step and the "Update cron state" step).

> **Note on staleness:** ISS-017 was already filed 2026-06-01 and **closed
> 2026-06-03** (fix branch `focus/iss-017-chain-runner-env`); it sits in the
> `## Resolved` table of `memory/issues/INDEX.md`. The delta only surfaces it as
> RESOLVED because the persisted state file (`security-scan.json`) was never
> refreshed after the 06-03 fix landed. This is a state-bookkeeping artifact, not
> a fresh resolution — no operator notification is warranted (see Constraints:
> "Never notify on a pure no-op week"). This run refreshes the state file to
> current reality.

## Persistent findings (unchanged)

**HIGH — 4** (all in `.github/workflows/aeon.yml`, all workflow_dispatch-gated,
low real-world risk, baseline-noted since 2026-05-25):

| File | Line | Pattern | Note |
|------|------|---------|------|
| `aeon.yml` | 86  | `echo "name=${{ inputs.skill }}"` in `run:` | `workflow_dispatch`/`workflow_call` requires repo write auth to trigger |
| `aeon.yml` | 94  | `if [ -n "${{ steps.skill.outputs.name }}" ]` in `run:` | Derived from `inputs.skill`; same risk profile |
| `aeon.yml` | 96  | `echo "label=${{ steps.skill.outputs.name }}"` in `run:` | Derived from `inputs.skill`; same risk profile |
| `aeon.yml` | 849 | `LABEL="${{ steps.work.outputs.label }}"` in `run:` | Was :725 at the 06-01 snapshot — line drift only, same anti-pattern (derived from `steps.skill.outputs.name` → `inputs.skill`) |

**Remediation (same for all four):** rebind to an `env:` key first, then read
`$_SAFE_NAME` from the shell — the exact pattern `chain-runner.yml` now uses for
ISS-017 and `messages.yml` uses post-2026-04-11. These remain unfiled as a
standalone ISS by baseline decision: the only trigger paths require repo write
access, so real exposure is low. Tracked here as persistent debt, not a new
incident.

**MEDIUM / LOW** — unchanged from baseline. All `base64 -d` matches decode
GitHub API `contents` responses (the API returns base64) or, at `aeon.yml:359`,
a chunked Telegram message that flows into a `jq`-built JSON payload — **none
pipe to a shell**, so no decode-then-execute path. Path-traversal and
force-push MEDIUM matches are documentation or internally-computed step outputs
(not user-controllable). Full list in the appendix of `security-scan.json`.

## Per-file results (notable)

| File | Status | HIGH | Note |
|------|--------|------|------|
| `.github/workflows/aeon.yml` | FAIL | 4 real | Persistent workflow_dispatch-gated interpolation (86/94/96/849) |
| `.github/workflows/chain-runner.yml` | PASS | 0 real | ISS-017 fixed — `env: _CHAIN` indirection at both sites |
| `.github/workflows/messages.yml` | PASS | 0 real | env: indirection from 2026-04-11 fix holds (lines 612-616) |
| `.github/workflows/investment-advisor.yml` | PASS | 0 | **NEW since baseline.** No `${{ }}` → `run:` injection |
| `.github/workflows/weekly-conviction.yml` | PASS | 0 | **NEW since baseline.** No `${{ }}` → `run:` injection |
| `scripts/advisor/*.sh` (8 files) | PASS | 0 real | **NEW since baseline.** curl secrets flow only to intended API hosts (Railway investiments, CoinGecko, DefiLlama, x.ai/Grok, Telegram, Hyperliquid, GeckoTerminal) — no SSRF/webhook hosts |
| `scripts/advisor/selftest.sh` | PASS | 0 real | `rm -rf /` at L31 is a **defensive test fixture** — a string fed through a `case` allowlist that defaults to `hold`, proving the direction sanitizer defangs malicious input. Never executed. |
| `skills/*/SKILL.md` (123 files) | — | 0 real | All HIGH matches are documented false positives: curl-with-secret usage examples (sandbox pattern), `eval` inside `monitor-runners` code fence ($NETWORKS controlled internal list), prompt-override strings in Threat-categories / untrusted-content-handling docs (baseline-suppressed) |

## New-surface audit (since 2026-06-01)

The investment advisor (`scripts/advisor/`, `investment-advisor.yml`,
`weekly-conviction.yml`) is the largest new attack surface since the last scan.
Audit findings:

- **Workflows:** zero `${{ github.event.* }}` / `${{ inputs.* }}` interpolation
  into `run:` blocks. Clean.
- **External-data handling:** the pipeline ingests Grok `x_search` results and
  market feeds (untrusted external content). These are written to
  `.investiments-cache/advisor/*.json` and consumed as `jq`-parsed data / LLM
  prompt context — not interpolated into shell. No injection path observed.
- **Secret flow:** `DASHBOARD_PASSWORD` (Basic auth), `XAI_API_KEY`,
  `TELEGRAM_BOT_TOKEN` reach only their intended hosts. No env var is piped to
  an attacker-controllable destination.
- **Obfuscation sweep:** no zero-width/bidi Unicode, no `fromCharCode`, no
  base64-decode-to-shell, no webhook SSRF hosts (ngrok/interact.sh/webhook.site/
  burpcollaborator/pipedream/requestbin) anywhere in the corpus.

## Appendix

Full structured finding set persisted to `memory/state/security-scan.json`.
