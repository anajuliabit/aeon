# Security Scan — 2026-08-03

**Verdict:** ATTENTION (4 persistent HIGH; 0 new; 0 resolved)
**Scope:** full corpus (skills/*/SKILL.md + companion scripts + .github/workflows/*.yml + scripts/*.sh + scripts/advisor/*.sh)
**Scanner mode:** `inline_grep_fallback` — `scan.sh` denied at the sandbox approval gate (10th consecutive scan; dominant failure mode per SKILL.md step 4). Inline Grep over the same HIGH/MEDIUM/LOW pattern library + manual `${{ }}` → `run:` interpolation audit + obfuscation sweep.
**Counts:** 235 files scanned · 4 HIGH · 15 MEDIUM · 4 LOW · 0 new · 0 resolved since 2026-07-27

## Needs attention (NEW high-severity this run)

None. No new HIGH findings introduced since the 2026-07-27 scan.

## Resolved since last scan

None. All prior resolutions still hold:
- `chain-runner.yml:41` (ISS-017 env: `_CHAIN` indirection) — held.
- `chain-runner.yml:368` (ISS-017 env: `_CHAIN` indirection) — held.
- `messages.yml` L612-616 / L684-685 / L838-863 (2026-04-11 incident-class env: rebinding) — held across every site.
- `replicate-oneoff.yml` L52-55 / L78 (env: indirection) — held.

## Persistent findings (unchanged)

**4 HIGH** — all in `.github/workflows/aeon.yml`, all fingerprint-identical to 2026-07-27:

| File | Line | Pattern | Chain source | Delta |
|---|---|---|---|---|
| `.github/workflows/aeon.yml` | 86 | `inputs.skill` interpolated into `run:` block | `inputs.skill` | PERSISTENT |
| `.github/workflows/aeon.yml` | 94 | `steps.skill.outputs.name` interpolated into `run:` block | derived from `inputs.skill` | PERSISTENT |
| `.github/workflows/aeon.yml` | 96 | `steps.skill.outputs.name` interpolated into `run:` block | derived from `inputs.skill` | PERSISTENT |
| `.github/workflows/aeon.yml` | 812 | `steps.work.outputs.label` interpolated into `run:` block | derived from `steps.skill.outputs.name` → `inputs.skill` | PERSISTENT (7th consecutive scan at `:812`, no line drift) |

**Remediation** (unchanged from prior scans, structurally blocked): rebind each expression to an `env:` key on the step, then read `$_SAFE_NAME` from the shell — see `articles/workflow-security-audit-2026-04-11.md` and the `chain-runner.yml` `_CHAIN` fix as templates. Fix is blocked from self-improve autoring by self-improve rule 5 (no `.github/workflows/` edits from a self-improve tick); requires operator direct authoring.

Note: real-risk is low because both `workflow_dispatch` and `workflow_call` require write access to trigger — attacker cannot inject via public event. This is anti-pattern hygiene, not exploitable exposure.

## Per-file results (HIGH only)

| File | Status | HIGH | Note |
|---|---|---|---|
| `.github/workflows/aeon.yml` | FAIL | 4 | Canonical-4 persistent; env: rebind pending operator PR |
| `.github/workflows/chain-runner.yml` | PASS | 0 | ISS-017 env: `_CHAIN` indirection held |
| `.github/workflows/messages.yml` | PASS | 0 | 2026-04-11 incident-class env: rebinding held |
| `.github/workflows/replicate-oneoff.yml` | PASS | 0 | env: indirection held |
| `.github/workflows/sync-upstream.yml` | PASS | 0 | step outputs all internal; L79 `git push -f` is inside PR-body markdown, not a `run:` shell command |
| `.github/workflows/investment-advisor.yml` | PASS | 0 | Cron-only, no inputs |
| `.github/workflows/weekly-conviction.yml` | PASS | 0 | Cron-only, no inputs |
| `.github/workflows/ci-packs-json.yml` | PASS | 0 | No `${{ }}` anywhere |
| `.github/workflows/ci-skills-json.yml` | PASS | 0 | No `${{ }}` anywhere |
| `scripts/advisor/selftest.sh` | PASS (documented FP) | 0 real | L31 `rm -rf /` in allowlist default-to-hold test; L220/L252 `eval` extracts helpers from same-repo trusted files |
| `scripts/eval-audit` | PASS (documented FP) | 0 real | 'eval' string appears in comments/echo, never as command execution |
| `skills/*/SKILL.md` (191 files) | PASS | 0 real | ~80 curl-with-secret matches all inside fenced code blocks; 10 prompt-override matches are defensive documentation (agent instructed to REJECT) |
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

**Out-of-scope note:** one zero-width match at `memory/logs/2026-07-12.md:82` captures a CoinGecko-supplied token name "Stable" with RTL zero-width chars. Memory logs are data files, not skills/workflows/scripts — outside the SKILL.md coverage rules. It's a data-in-log observation of an untrusted upstream (CoinGecko aggregator artifact), not a payload in executable code. No action.

## Delta

| Metric | 2026-07-27 | 2026-08-03 | Δ |
|---|---|---|---|
| Files scanned | 232 | 235 | +3 (companion script recount) |
| SKILL.md count | 191 | 191 | 0 |
| Workflow count | 9 | 9 | 0 |
| Repo scripts | 21 | 21 | 0 |
| Advisor scripts | 10 | 10 | 0 |
| HIGH (post-filter) | 4 | 4 | 0 |
| MEDIUM (post-filter) | 15 | 15 | 0 |
| LOW (post-filter) | 4 | 4 | 0 |
| NEW HIGH | 0 | 0 | 0 |
| RESOLVED HIGH | 0 | 0 | 0 |

**Exit status:** `SECURITY_SCAN_NOCHANGE` — findings byte-for-byte identical to 2026-07-27. `:812` held for 7th consecutive scan (2026-06-22 → 08-03 span, no line drift).

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
