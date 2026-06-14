## Summary

Ran security-digest for 2026-06-14. **All three tiers empty → `SECURITY_DIGEST_OK`, no notify sent.**

**Source results:**
- KEV (7 vulns this week): all 7 deduped against 6-13 14:45Z digest. PeopleSoft KEV dueDate Mon 6-15; Ivanti Sentry dueDate hit today.
- GH critical 48h (1): GHSA-6xp4-cf37-ppjh Budibase deduped.
- GH high 48h (22): 7 tracked-stack deduped (esbuild + 2 Budibase + pyo3 + radius + chisel + 5× filebrowser cluster), 10 in non-tracked ecosystems (composer/maven/swift), 1 fresh in tracked (`GHSA-qhv3-wjg8-6fx6 / CVE-2026-48151 @budibase/server 7.5` — same `≥3.39.0` patch already shipped to operator yesterday for 9.0 + 8.1 siblings; falls off per 6-13 Baileys precedent).
- GH malware 48h (4): all deduped — first quiet 24h on malware feed since the 6-10/6-11/6-13 burst cycle.

**Notable:** first all-zero-tier digest of the canonical-watchlist era. Confirmed aeon's npm packages (mcp-server/dashboard/worker/a2a-server) don't depend on budibase or direct esbuild.

**Files:** appended `### security-digest` entry to `memory/logs/2026-06-14.md`. No notification sent.
