*security digest — 2026-08-13*
verdict: 0 fresh KEV · 70 fresh malware pkgs (53 alphabet-namespace) · 1 to schedule · 3 to monitor. _sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- **70 fresh npm malware pkgs** (post-8-12 15:12Z cutoff, all npm) — `@years17/18/19/20/n8n-nodes-utils-helper-*` alphabet-namespace explodes 53 variants (a→y across 4 handles, extends 8-12 n=1 candidate); fleet-adjacent typosquats: `cc-skills-helper`, `mcp-util-helpers`, `passkeys-react`, `nolimit-agent` (+ linux-x64/win32-x64), `@dreamguyxeon/libsignal-node`.
  → block installs from `@years17/18/19/20/*` scopes and `*-agent`/`*-helper` unknown-publisher pkgs; rotate any tokens exposed to installs from these handles.

*PATCH THIS WEEK*
- [GHSA-49m4-vp58-wgc9](https://github.com/advisories/GHSA-49m4-vp58-wgc9) — stata-mcp (pip) · CVSS 8.4 · EPSS n/a · no fix yet
  MCP server for Stata: unsanitized `package` arg in `ado_package_install` = shell command injection. → pin/exclude `stata-mcp` <1.19.0 until a patched release ships.

*MONITOR*
- [GHSA-w62w-66v9-vvgv](https://github.com/advisories/GHSA-w62w-66v9-vvgv) — seaweedfs (Go) · CVE-2026-54917 · EPSS 0.004 · no fix
  path traversal in S3 and Iceberg REST gateways = cross-bucket access. 2nd SeaweedFS high in 48h (8-12 SSRF GHSA-87fv). → watch for a fix; do not expose S3 gateway publicly.
- [GHSA-48p8-g2fx-3wwm](https://github.com/advisories/GHSA-48p8-g2fx-3wwm) — argo-workflows (Go) · CVE-2026-54526 · EPSS 0.004 · no fix
  ArtifactGC.PodSpecPatch bypasses Strict/Secure template allow-list (incomplete fix for CVE-2026-31892). → audit ArtifactGC usage on production Argo installs; watch for release.
- [GHSA-3763-qp59-59vf](https://github.com/advisories/GHSA-3763-qp59-59vf) — nimiq-blockchain (rust) · CVE-2026-46369 · CVSS 7.5 · EPSS n/a · no fix
  validity store off-by-one. → track for patched crate release.
