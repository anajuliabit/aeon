*Security Digest — 2026-07-17*
Verdict: 3 to patch today, 5 to schedule, 0 monitor. **BOD T-0 today**: SharePoint CVE-2026-56164 + SonicWall SMA1000 pair CVE-2026-15409/-15410 (deadline hits today). _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-39808](https://nvd.nist.gov/vuln/detail/CVE-2026-39808) + [CVE-2026-25089](https://nvd.nist.gov/vuln/detail/CVE-2026-25089) — Fortinet FortiSandbox / Cloud / PaaS · **fresh KEV added 2026-07-16** · EPSS **0.842 pct 0.997** + 0.361 pct 0.983 · BOD due 2026-07-19 (T-2)
  Unauth OS command injection pair via crafted HTTP. 39808 is top EPSS today.
  → apply Fortinet PSIRT firmware today (single fix bundle covers pair).
- [CVE-2026-58644](https://nvd.nist.gov/vuln/detail/CVE-2026-58644) — Microsoft SharePoint · fresh KEV added 2026-07-16 · EPSS 0.015 pct 0.707 · BOD due 2026-07-19 (T-2)
  Deserialization of untrusted data, unauth network RCE. Second SharePoint KEV in 4 days (56164 on 7-14 is the T-0-today crossing above).
  → apply MSRC mitigations today or discontinue exposed instances.
- **npm-malware wave d4** — 13 fresh pkgs 7-16 14z → 7-17 05z (fade 16 → 13 continues from d3 30 → 16, wave still active). Standouts: **`anthropic-claude-latest`** = **2nd direct-Anthropic-scope typosquat** in memory (after 7-16 `claude-token-tracker-mcp`, published 05:39Z 7-17), `monogrok` (grok typosquat), `chai-as-const` + `chai-as-thread` (chai test-lib pair), `ai-pro-sdk` / `theta-sdk-js` / `chain-sdk-js` (SDK typosquats), `terminal-mascot` + `awesome-terminal`, `px8my` (55-version dump).
  → audit npm installs since 7-16 14z; rotate `ANTHROPIC_API_KEY` on any host that touched `anthropic-claude-latest` or `claude-token-tracker-mcp`.

*PATCH THIS WEEK*
- [CVE-2026-53713](https://github.com/advisories/GHSA-wcrf-9vrr-854f) — envoy gateway (Go) · CVSS **9.1** · EPSS n/a · no public PoC
  Auth bypass via Lua in EnvoyExtensionPolicy → secret disclosure. → upgrade to ≥1.8.1 (or ≥1.7.4 on 1.7.x).
- [MCP Python SDK 3-CVE cluster](https://github.com/advisories/GHSA-vj7q-gjh5-988w) — mcp (pip) · CVSS 7.6 / 7.1 / 7.6 · no PoC
  CVE-2026-59950 WebSocket Host/Origin unvalidated (fix ≥1.28.1), CVE-2026-52869 HTTP session auth bypass + CVE-2026-52870 cross-client task cancel (both fix ≥1.27.2). → upgrade mcp to ≥1.28.1 (covers all three). **MCP-server hardening rail extends n=4** in 72h (7-15 langbot/mcp-documentation-server/n8n-mcp + 7-16 mcp Python SDK).
- [CVE-2026-52833](https://github.com/advisories/GHSA-3v79-m2cg-89ww) — nuclio (Go) · CVSS 8.0 · no PoC
  Unsanitized `runtimeAttributes.repositories` → Groovy `build.gradle` → build-time RCE. → upgrade nuclio to ≥1.16.5.
- [CVE-2026-50289](https://github.com/advisories/GHSA-5xpp-75jx-m839) — systeminformation (npm) · CVSS v4 **8.7** · no PoC
  OS command injection in `networkInterfaces()` via `interfaces(5)` source-directive path on Linux. Widely-embedded lib. → upgrade past 5.31.6.
- [django-haystack](https://github.com/advisories/GHSA-r3hx-x5rh-p9vv) — django-haystack (pip) · CVSS v4 **8.7** · no CVE · no PoC
  RCE via `eval()` in Elasticsearch result deserialization. → upgrade to ≥3.4.0.
