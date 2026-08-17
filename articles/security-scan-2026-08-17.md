# Security Scan — 2026-08-17

**Verdict:** ATTENTION (4 persistent HIGH; 0 new; 0 resolved)
**Scope:** full corpus (skills/*/SKILL.md + companion scripts + .github/workflows/*.yml + scripts/*.sh + scripts/advisor/*.sh)
**Scanner mode:** `inline_grep_fallback` — `scan.sh` denied at the sandbox approval gate (11th consecutive scan: 2026-05-25, 06-01, 06-15, 06-22, 06-29, 07-06, 07-13, 07-20, 07-27, 08-03, 08-17). Dominant failure mode per SKILL.md step 4. Inline Grep over the same HIGH/MEDIUM/LOW pattern library + manual `${{ }}` → `run:` interpolation audit + obfuscation sweep. Never silently skipped.
**Counts:** 235 files scanned · 4 HIGH · 15 MEDIUM · 4 LOW · 0 new · 0 resolved since 2026-08-03
**Cadence note:** 14-day gap since prior scan (vs typical 7-day) — 2026-08-10 mon-batch fire missed via ISS-031 usepod-402 dispatcher stall; this run = mon-batch auto-clear test #4 at 16Z slot via direct Claude Code execution bypass (parallels unlock-monitor 10Z + search-skill 14Z + deal-flow 14Z earlier today). Dispatcher path still unproven; bypass path clean.

## Needs attention (NEW high-severity this run)

None. No new HIGH findings introduced since the 2026-08-03 scan.

## Resolved since last scan

None. All prior resolutions still hold:
- `chain-runner.yml:41` (ISS-017 env: `_CHAIN` indirection) — held.
- `chain-runner.yml:368` (ISS-017 env: `_CHAIN` indirection) — held.
- `messages.yml` L611-616 (2026-04-11 incident-class env: rebinding) — held across every site.
- `replicate-oneoff.yml` L52-55 / L78 (env: indirection) — held.

## Persistent findings (unchanged)

**4 HIGH** — all in `.github/workflows/aeon.yml`, all fingerprint-identical to 2026-08-03:

| File | Line | Pattern | Chain source | Delta |
|---|---|---|---|---|
| `.github/workflows/aeon.yml` | 86 | `inputs.skill` interpolated into `run:` block | `inputs.skill` | PERSISTENT |
| `.github/workflows/aeon.yml` | 94 | `steps.skill.outputs.name` interpolated into `run:` block | derived from `inputs.skill` | PERSISTENT |
| `.github/workflows/aeon.yml` | 96 | `steps.skill.outputs.name` interpolated into `run:` block | derived from `inputs.skill` | PERSISTENT |
| `.github/workflows/aeon.yml` | 812 | `steps.work.outputs.label` interpolated into `run:` block | derived from `steps.skill.outputs.name` → `inputs.skill` | PERSISTENT (**8th consecutive scan at `:812`**, no line drift 2026-06-22 → 2026-08-17) |

**Remediation** (unchanged from prior scans, structurally blocked): rebind each expression to an `env:` key on the step, then read `$_SAFE_NAME` from the shell — see `articles/workflow-security-audit-2026-04-11.md` and the `chain-runner.yml` `_CHAIN` fix as templates. Fix blocked from self-improve authoring by self-improve rule 5 (no `.github/workflows/` edits from a self-improve tick); requires operator direct authoring.

Note: real-risk is low because both `workflow_dispatch` and `workflow_call` require write access to trigger — attacker cannot inject via public event. This is anti-pattern hygiene, not exploitable exposure.

## Per-file results (HIGH only)

| File | Status | HIGH | Note |
|---|---|---|---|
| `.github/workflows/aeon.yml` | FAIL | 4 | Canonical-4 persistent; env: rebind pending operator PR |
| `.github/workflows/chain-runner.yml` | PASS | 0 | ISS-017 env: `_CHAIN` indirection held (L41 + L368) |
| `.github/workflows/messages.yml` | PASS | 0 | 2026-04-11 incident-class env: rebinding held (L611-616) |
| `.github/workflows/replicate-oneoff.yml` | PASS | 0 | env: indirection held (L52-55, L78) |
| `.github/workflows/sync-upstream.yml` | PASS | 0 | step outputs all internal; L79 `git push -f` is inside PR-body markdown, not a `run:` shell command |
| `.github/workflows/investment-advisor.yml` | PASS | 0 | Cron-only, no `${{ inputs/github.event/steps }}` in run blocks |
| `.github/workflows/weekly-conviction.yml` | PASS | 0 | Cron-only, no inputs |
| `.github/workflows/ci-packs-json.yml` | PASS | 0 | No `${{ }}` anywhere |
| `.github/workflows/ci-skills-json.yml` | PASS | 0 | No `${{ }}` anywhere |
| `scripts/advisor/selftest.sh` | PASS (documented FP) | 0 real | L31 `rm -rf /` in allowlist default-to-hold defensive fixture (never executed); L189/L221 `eval` extracts helpers from same-repo trusted files (line numbers shifted from 08-03 baseline L220/L252 via file growth to 651 lines; pattern context identical) |
| `scripts/eval-audit` | PASS (documented FP) | 0 real | 'eval' string appears in comments/echo, never as command execution |
| `skills/*/SKILL.md` (191 files) | PASS | 0 real | ~80 curl-with-secret matches all inside fenced code blocks; ~10 prompt-override matches are defensive documentation (agent instructed to REJECT) |
| `skills/skill-health/tests/smoke.sh` | PASS | 0 | Static validator |
| `skills/skill-freshness/check_mtimes.py` | PASS | 0 | Python mtime checker, no exec/eval |

## Obfuscation sweep

| Category | Result |
|---|---|
| Zero-width Unicode (U+200B, U+FEFF) in scope | Clean |
| Bidi override (U+202E / Trojan Source) | Clean |
| `fromCharCode` in active code | Clean (substring appears in ~40 JSON caches as coin-description data + scanner's own pattern library) |
| base64 decode → shell | Clean (all `base64 -d` sites decode GitHub API `contents` responses or chunk a jq-built Telegram payload; none pipe to a shell) |
| SSRF webhook hosts (ngrok, interact.sh, webhook.site, burpcollaborator, pipedream, requestbin) | Clean (only mentions are in the scanner's pattern definition + prior scan articles) |

**Out-of-scope note:** the 2026-07-12 zero-width memory-log match remains out-of-scope (memory logs are data files, not skills/workflows/scripts). CoinGecko-supplied token name artifact, not a payload in executable code.

## Delta

| Metric | 2026-08-03 | 2026-08-17 | Δ |
|---|---|---|---|
| Files scanned | 235 | 235 | 0 |
| SKILL.md count | 191 | 191 | 0 |
| Workflow count | 9 | 9 | 0 |
| Repo scripts | 21 | 21 | 0 |
| Advisor scripts | 10 | 10 | 0 |
| Companion scripts (sh + py in skills/) | 4 | 4 | 0 |
| HIGH (post-filter) | 4 | 4 | 0 |
| MEDIUM (post-filter) | 15 | 15 | 0 |
| LOW (post-filter) | 4 | 4 | 0 |
| NEW HIGH | 0 | 0 | 0 |
| RESOLVED HIGH | 0 | 0 | 0 |

**Exit status:** `SECURITY_SCAN_NOCHANGE` — findings byte-for-byte identical to 2026-08-03. `:812` held for **8th consecutive scan** (2026-06-22 → 2026-08-17 span, no line drift). Only local commit in the 14-day window is `d629a96 chore(cron): cost-report failed` — a cron-state metadata write, no scan-scope surface change. No new attack surface introduced.

## Appendix — all current HIGH findings (post code-fence downgrade + baseline suppression)

```json
[
  {"file": ".github/workflows/aeon.yml", "line": 86, "pattern": "inputs.skill interpolated into run: block", "severity": "high", "fingerprint": "aeon.yml:86:inputs.skill", "delta": "PERSISTENT"},
  {"file": ".github/workflows/aeon.yml", "line": 94, "pattern": "steps.skill.outputs.name interpolated into run: block", "severity": "high", "fingerprint": "aeon.yml:94:steps.skill.outputs.name", "delta": "PERSISTENT"},
  {"file": ".github/workflows/aeon.yml", "line": 96, "pattern": "steps.skill.outputs.name interpolated into run: block", "severity": "high", "fingerprint": "aeon.yml:96:steps.skill.outputs.name", "delta": "PERSISTENT"},
  {"file": ".github/workflows/aeon.yml", "line": 812, "pattern": "steps.work.outputs.label interpolated into run: block", "severity": "high", "fingerprint": "aeon.yml:812:steps.work.outputs.label", "delta": "PERSISTENT"}
]
```

Notification: **skipped** (no NEW HIGH, no RESOLVED HIGH — report written for on-demand read, no operator interrupt warranted).
