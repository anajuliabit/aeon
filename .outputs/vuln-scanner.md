## Summary

**Vuln scanner ran against superloglabs/superlog** (806★ TypeScript observability stack, Apache-2.0, PVR + SECURITY.md email).

**Files written:**
- `articles/vuln-scan-2026-06-13.md` — full report (scanner sources, candidate triage, drop reasoning, dedup state)
- `memory/vuln-scanned.json` — first entry; 30-day skip window armed through 2026-07-13
- `memory/issues/ISS-018.md` + `INDEX.md` update — sandbox-limitation issue: missing `scripts/prefetch-vuln-scanner.sh`
- `memory/logs/2026-06-13.md` — `### vuln-scanner` entry appended
- `.pending-notify/vuln-scanner-2026-06-13.md` — notification staged (sandbox blocked direct `./notify`)

**Findings:** 0 confirmed. Of 12 candidates triaged from the lockfile against GHSA, every CVE was either already patched (axios 1.16.1, better-auth 1.6.11, dompurify 3.4.7, form-data 4.0.5, @grpc/grpc-js 1.14.3) or had preconditions that don't hold (esbuild Deno-only; react-router 7.14.2 advisory excludes Declarative Mode, which superlog uses via `<BrowserRouter>`). The one real hit — next 15.5.15 with 7 high CVEs — is consumed only by `apps/sample` (a `private: true` telemetry-fixture demo), dropped per the SKILL `demo/` triage rule.

**Disclosure channels used:** none. No PVR, no public PR — there's nothing to disclose.

**Coverage caveat:** dep-CVE only. SAST (semgrep), secret scan (trufflehog), and the osv-scanner binary were all blocked by the sandbox (`pip install`, `tar -x`, and arbitrary-binary execution all require approval). ISS-018 filed to add the missing prefetch script so future runs get full scanner coverage.

**Follow-up:** None required from this run beyond ISS-018; re-scan superloglabs/superlog after 2026-07-13 (or sooner if the prefetch lands and SAST+secrets need to cover code-flow surfaces).
