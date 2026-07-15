*Security Digest — 2026-07-15*
Verdict: 3 KEV items in fresh 7-14 batch (SharePoint + SonicWall pair + AD FS), npm-malware wave d2 (30 pkgs), 5 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-56164](https://nvd.nist.gov/vuln/detail/CVE-2026-56164) — Microsoft SharePoint · KEV added 2026-07-14 · EPSS 0.070 (p 0.935) · CVSS n/a
  Missing auth allows unauth priv esc over network. BOD due 2026-07-17 (T-2).
  → apply MSRC mitigations today or discontinue.
- [SNWLID-2026-0008](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0008) — SonicWall SMA1000 (CVE-2026-15409 SSRF + CVE-2026-15410 code inj) · KEV added 2026-07-14 · EPSS 0.014 / 0.016 · CVSS n/a
  Unauth SSRF + authenticated admin OS-command injection pair. BOD due 2026-07-17 (T-2).
  → patch SMA1000 per SNWLID-2026-0008 today.
- npm-malware wave d2 — 30 fresh pkgs 02:53–10:03Z (baileys typosquats @fhkry / @sauruslord / @bcs-mi-ui, gulp-jscrambler, jscrambler-metro-plugin, fastify-addon, webpack-cache scope, @achuthvp/postinstall-poc). Confirmed malicious per GH `type=malware`; same-day-multi-batch shape continues from 7-14.
  → audit installs since 7-13 + rotate any creds exposed.

*PATCH THIS WEEK*
- [CVE-2026-54052](https://github.com/advisories/GHSA-j6r7-6fhx-77wx) — n8n-mcp (npm) · CVSS 9.9 · EPSS n/a
  Cross-tenant workflow backup access in multi-tenant HTTP mode; snapshots leak credential refs.
  → upgrade n8n-mcp to ≥2.56.1.
- [CVE-2026-50006](https://github.com/advisories/GHSA-xrcf-6jh3-ggvx) — anyquery (Go) · CVSS 9.1 · EPSS n/a
  AFW → RCE via unrestricted SQLite virtual tables in server mode; SSRF 8.6 + LFR 7.5 fixed same release.
  → upgrade anyquery to ≥0.4.5.
- [CVE-2026-50131](https://github.com/advisories/GHSA-xw9q-2mv6-9fr8) — @fedify/fedify (npm) · CVSS 8.6 · EPSS 0.003
  SSRF incomplete mitigation after GHSA-p9cg-vqcc-grcx.
  → upgrade per branch: 1.9.12 / 1.10.11 / 2.0.19 / 2.1.15 / 2.2.4.
- [CVE-2026-61699](https://github.com/advisories/GHSA-cm26-5974-52h8) — nebula-mesh (Go) · CVSS 8.1 · EPSS n/a
  Certificate revocation never enforced at mesh; 4-advisory cluster fixed same release.
  → upgrade nebula-mesh to ≥0.7.1.
- [CVE-2026-56155](https://nvd.nist.gov/vuln/detail/CVE-2026-56155) — Microsoft AD FS · KEV added 2026-07-14 · EPSS 0.004 · CVSS n/a
  Local priv esc from authorized attacker. BOD due 2026-07-28.
  → apply MSRC mitigations or decommission per AD FS decommission guide.

*MONITOR*
- [GHSA-9hc2-hjx8-q6pv](https://github.com/advisories/GHSA-9hc2-hjx8-q6pv) — tidgi (npm) · CVSS 9.6 · EPSS n/a · no fix yet
  RCE via malicious TiddlyWiki repo import. → avoid importing untrusted repos in TidGi Desktop.
- [GHSA-pqg7-v6wh-3pfp](https://github.com/advisories/GHSA-pqg7-v6wh-3pfp) — tsdproxy (Go) · CVSS 8.5 · EPSS n/a · alpha-only fix
  XFF header injection → IP spoofing to backend services. → hold on 3.0.0-alpha.3 or wait for stable.
