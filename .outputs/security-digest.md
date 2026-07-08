*Security Digest — 2026-07-08*
Verdict: 4 fresh KEV entries end a 4-day quiet window, 5 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-48282](https://nvd.nist.gov/vuln/detail/CVE-2026-48282) — Adobe ColdFusion · KEV added 2026-07-07 · EPSS 0.032 (p87) · CVSS n/a
  path traversal → arbitrary code execution. exploited per CISA.
  → apply Adobe emergency bulletin today on any ColdFusion instance.
- [CVE-2026-55255](https://github.com/advisories/GHSA-qrpv-q767-xqq2) — langflow (pip) · KEV added 2026-07-07 · EPSS 0.004 · CVSS 8.4
  IDOR on `/api/v1/responses` — authenticated attacker runs any user's flow. PoC in advisory.
  → upgrade langflow to ≥1.9.1 today.
- npm malware surge — 240 new advisories in 48h (post-holiday brand-jack backlog flushes)
  typosquats: `nodemon-node`, `vite-json-pwa`, `tailwindcss-effector`, `mci-sdk`. all confirmed malicious.
  → audit npm installs from 2026-07-06 forward; rotate creds exposed to fresh unfamiliar deps.

*PATCH THIS WEEK*
- [GHSA-qvfm-67h2-2qfx](https://github.com/advisories/GHSA-qvfm-67h2-2qfx) — 9router (npm) · CVSS 9.9 · plus GHSA-vjc7 CVSS 10.0 · no patch yet
  credential theft + DB takeover + unauth CRUD on `/api/providers`. two criticals same package.
  → drop 9router pending upstream fix; audit deploys using it now.
- [GHSA-q9p7-wqxg-mrhc](https://github.com/advisories/GHSA-q9p7-wqxg-mrhc) — langroid (pip) · CVSS 10.0 · 3 criticals (54769/55615/54760) · no patch yet
  sandbox escape → RCE via TableChatAgent `eval()`. also Cypher injection in Neo4jChatAgent + SQL blocklist bypass.
  → drop langroid pending upstream fix; rotate DB creds if it touched them.
- [GHSA-pw9m-5jxm-xr6h](https://github.com/advisories/GHSA-pw9m-5jxm-xr6h) — better-auth (npm) · CVSS 9.6 / 9.1 · 13-CVE cluster · fix 1.6.11
  OAuth refresh-token replay + SSO SSRF + `alg=none` default + oidc-provider bugs. one package, many holes.
  → upgrade better-auth to ≥1.6.11 across all apps using it.
- [GHSA-mp2f-45pm-3cg9](https://github.com/advisories/GHSA-mp2f-45pm-3cg9) — decompress (npm) · CVE-2026-53486 · CVSS 9.1 · no EPSS
  zip-slip in archive extraction. original `decompress` unpatched (EOL); maintained fork carries the fix.
  → swap `decompress` → `@xhmikosr/decompress` ≥10.2.1 (10.x) or ≥11.1.3 (11.x).
- [GHSA-3fcv-jvfp-m4q9](https://github.com/advisories/GHSA-3fcv-jvfp-m4q9) — cilium (Go) · CVE-2026-49445 · CVSS 9.2
  local Envoy admin socket → info disclosure + cluster disruption. backport lines shipped.
  → upgrade cilium to ≥1.19.2 (or 1.18.8 / 1.17.14).

*MONITOR*
- [GHSA-26rh-24rg-j3vv](https://github.com/advisories/GHSA-26rh-24rg-j3vv) — goploy (Go) · CVSS 9.6 (CVE-2026-53552 + 53553) · no fix yet
  cross-namespace IDOR + RCE + path-traversal file read.
  → track for patched release; don't expose goploy admin.
- [GHSA-ww9q-8r59-xv46](https://github.com/advisories/GHSA-ww9q-8r59-xv46) — halo2_gadgets / orchard / zebrad (crates.io) · CVE-2026-54496 · CVSS 9.3
  Zcash Orchard Action circuit soundness break in halo2_gadgets scalar mult. fixes: halo2_gadgets 0.5.0, orchard 0.14.0, zcash_primitives 0.28.0.
  → upgrade only if consuming these crates (niche outside Zcash tooling).
- 8 open-webui (pip) XSS/RCE cluster — CVSS 7.3–8.5, all published 2026-07-07
  stored XSS via iframe embeds + unescaped markdown → account takeover + RCE via functions.
  → track open-webui deployments; upgrade at next planned window.
