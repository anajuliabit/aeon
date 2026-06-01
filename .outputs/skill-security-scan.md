`SECURITY_SCAN_NEW`

## Summary

First delta-eligible `skill-security-scan` after the 2026-05-25 baseline bootstrap. Sandbox blocked direct `scan.sh --all --json` execution, so per SKILL.md step 4 I ran the inline-Grep fallback over the full corpus (145 files: 125 SKILL.md + 5 workflows + 14 scripts + 1 skill-companion script).

**Verdict: ATTENTION** — 6 HIGH · 14 MEDIUM · 4 LOW post-filter.

**Delta vs baseline:**
- **2 NEW HIGH** — `.github/workflows/chain-runner.yml:41` + `:416` interpolate `${{ inputs.chain }}` directly into `run:` shell (same 2026-04-11 incident class as messages.yml fix). Filed as **ISS-017**.
- **1 RESOLVED HIGH** — `messages.yml:578` now uses canonical `env:` indirection (lines 586-591 bind `_INPUT_MESSAGE`/`_EVENT_ACTION`/etc., shell reads `$_EVENT_NAME`). No open ISS to flip.
- **4 PERSISTENT HIGH** — `aeon.yml:86`, `:94`, `:96`, `:725` (was `:718` at baseline; code drift, same finding). Same anti-pattern, low real risk, eligible for the same env-binding sweep.

**Files written/modified:**
- `articles/security-scan-2026-06-01.md` — full report
- `memory/issues/ISS-017.md` — new HIGH finding
- `memory/issues/INDEX.md` — appended ISS-017 row
- `memory/state/security-scan.json` — refreshed snapshot + delta annotations
- `memory/logs/2026-06-01.md` — appended `### skill-security-scan` section
- `.pending-notify/2026-06-01-skill-security-scan.md` — notification staged for post-run delivery (sandbox blocks `./notify` arg-passing)

**Follow-up:** chain-runner.yml fix is one-for-one with messages.yml:586-595 — bind `_CHAIN: ${{ inputs.chain }}` in `env:`, read `$_CHAIN` in the shell, for both `run:` blocks. Same one-shot sweep would clear the 4 PERSISTENT aeon.yml HIGHs.
