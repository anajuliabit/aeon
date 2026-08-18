*Security Digest — 2026-08-18*
Verdict: 3 to patch today, 3 this week, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [vm2 triple sandbox escape](https://github.com/advisories/GHSA-m283-3h24-438v) — vm2 (npm) · CVSS 9.9/9.8/10.0 · sandbox-escape → RCE by definition · EPSS 0 (fresh)
  3 fresh critical CVEs same package: Error.cause bypass + host-proto mutators + NodeVM builtin:['*'] exposing os/dns. vm2 was deprecated in 2023.
  → upgrade vm2 to ≥3.11.6 today, or migrate off vm2.
- [checkout-* + chai-* + bcc-* npm brand-jack cluster](https://github.com/advisories/GHSA-cpmp-7ffm-4j7c) — npm · malware · 10 fresh pkgs 8-18
  Coordinated PayPal-checkout + Chai + BCC-design + core-tailwindcss brand-jack burst.
  → remove any of: checkout-{mobile-pay-button,create-pos-order-am,common-tokens,desktop-total}, chai-{foundry,as-deployer}, bcc-design{,-icons}, core-tailwindcss-utility, cerebrum-core; rotate creds if installed.
- [Sui/Mysten Labs npm brand-jack cluster](https://github.com/advisories/GHSA-xgmm-vq93-f5vx) — npm · malware · 5 pkgs same 16:24Z 8-17 batch
  Coordinated Sui-blockchain typosquat: sui-move-graphql, sui-move-rpc, sui-gql-core, bcs-core, bucket-protocol-sdk-v2.
  → remove any installed; audit lockfiles + rotate any keys exposed.

*PATCH THIS WEEK*
- [CVE-2026-64849](https://github.com/advisories/GHSA-7gwp-5pfp-969j) — mlflow (pip) · CVSS 9.3 · EPSS 0 (fresh) · no public PoC
  Unauth full-read SSRF in webhook delivery via HTTP-redirect bypass of `_validate_webhook_url`. → upgrade mlflow to ≥3.15.0.
- [CVE-2026-71479 + CVE-2026-64859](https://github.com/advisories/GHSA-8r8v-xf7q-rcpr) — QuantumNous/new-api (Go) · CVSS 9.1 both · EPSS 0
  Integer-overflow self-crediting in quota billing + root user token leak in user list API. LLM-proxy pkg.
  → upgrade new-api to ≥1.0.0-rc.18.
- [CVE-2026-62982](https://github.com/advisories/GHSA-73wf-9vmv-5pv9) — glances (pip) · CVSS 8.8 · EPSS 0
  Command injection bypass via nested stat values (incomplete fix of CVE-2026-32608). → upgrade glances to ≥4.5.6.

*MONITOR*
- [CVE-2026-56677](https://github.com/advisories/GHSA-8g4w-4ffg-8vgx) — 9router (npm) · CVSS 8.6 · no fix yet · EPSS 0
  Authenticated SSRF via OIDC provider test endpoint. → track advisory; don't expose OIDC admin.
- [GHSA-xhcr-cqfr-m3hv](https://github.com/advisories/GHSA-xhcr-cqfr-m3hv) — atomic-agents-stack (pip) · high · no fix yet
  HTTP MCP catalog accepts cleartext http + spawns catalog-supplied commands = MITM→RCE. MCP-adjacent.
- [CVE-2026-55090](https://github.com/advisories/GHSA-2jp7-wwpg-3p9w) — ep_etherpad-lite (npm) · high · no fix yet · EPSS 0
  Stored XSS in HTML export via unescaped attribute-pool values. → track patch; sanitize exports.
