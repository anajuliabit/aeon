Notification staged. Summary:

## Summary

Ran security-digest for 2026-06-04. Lead with KEV-confirmed exploitation, enriched with EPSS, filtered GH Advisories to the tracked stack (npm, pip, Go, crates.io, GitHub Actions).

**Tier counts: 2 / 4 / 1.**

- **PATCH TODAY:** CVE-2026-45247 (mirasvit fpc warmer, fresh KEV add 2026-06-03, EPSS 0.061 pct 0.91, fix ≥1.11.12); CVE-2026-44180 (jupyter_enterprise_gateway pip, CVSS 9.8, public PoC, siblings 44181/44182, fix ≥3.3.0).
- **PATCH THIS WEEK:** docling-core ≥2.74.1; nuclio ≥v0.0.0-20260513101907-1915cd26d514; docling ≥2.91.0; react-router ≥7.15.0.
- **MONITOR:** browserstack-runner CVE-2026-49143 (CVSS 8.8, public PoC, no patch yet — vulnerable ≤0.9.5).

**Sources:** kev=ok, gh=ok, epss=ok (most new CVEs not yet scored).

**Files:**
- Staged: `.pending-notify/1780586227-security-digest.md` (2,301 chars).
- Appended `### security-digest` entry to `memory/logs/2026-06-04.md`.

**Follow-up:** axios npm 4-CVE cluster (CVE-2026-44496/44488/44487/44486, all CVSS 7.5, fix 1.16.0) failed the ≥8.0 gate but is a dependency-graph hub worth flagging at next operator review. Sandbox blocked deletion of `kev.json` scratch file — same pattern as MEMORY-noted cleanup-chain-runner-scratch goal; needs the postprocess cleanup step.
