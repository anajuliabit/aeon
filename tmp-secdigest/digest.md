*Security Digest — 2026-06-26*
Verdict: 2 actively exploited, 3 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-20230](https://nvd.nist.gov/vuln/detail/CVE-2026-20230) — Cisco Unified CM / SME · KEV added 2026-06-25 · EPSS 0.512/p98.8 · CVSS 8.6
  unauth SSRF → arbitrary file write → root. public PoC live (denizhalil 6-12), CISA-ADP flipped poc→active 6-25. CISA due 2026-06-28.
  → apply cisco-sa-cucm-ssrf advisory today.
- [CVE-2026-12569](https://nvd.nist.gov/vuln/detail/CVE-2026-12569) — PTC Windchill / FlexPLM · KEV added 2026-06-25 · EPSS 0.009 · CVSS 9.3 (v4.0)
  unauth deserialization → RCE. active exploitation per CISA. affects Windchill ≤13.1.3.0 / FlexPLM ≤13.0.3.0.
  → apply PTC CS473270 mitigation today (CISA due 2026-06-28).
- npm **leo-sdk supply chain — 15-package wave** (malware advisories) · 6-25: 3 (leo-sdk/cron/logger) · 6-26: +12 (leo-streams / leo-cache / leo-cli / leo-auth / leo-connector-{mongo,mysql,elasticsearch,oracle} / rstreams-{metrics,shard-util} / serverless-{convention,leo})
  → remove every `leo-*` / `rstreams-*` / `serverless-leo` dep today; rotate any AWS keys + DB creds touched by those processes.

*PATCH THIS WEEK*
- **golang.org/x/crypto/ssh cluster — 9 CVEs published 2026-06-25** (coordinated golang-announce drop). top: [CVE-2026-46595](https://github.com/advisories/GHSA-x527-x647-q7gg) verifiedPublicKeyCallback skip enforcement (CVSS 10.0, bypass of 2024 CVE-2024-45337 fix); [CVE-2026-42508](https://github.com/advisories/GHSA-5cgq-3rg8-m6cv) knownhosts `@revoked` bypass; FIDO/U2F presence-check bypass; agent forwarding leaks constraints. all EPSS <0.005 (fresh).
  → upgrade golang.org/x/crypto to ≥0.52.0 across every Go service.
- [CVE-2026-55166](https://github.com/advisories/GHSA-v2wp-frmc-5q3v) + [CVE-2026-48508](https://github.com/advisories/GHSA-qcqw-jwxc-2hqg) — Netflix Lemur (pip) · CVSS 9.9 + 8.8 · no public PoC
  ACME SSRF + creator-equality IDOR → AWS IAM / PKI compromise; plus authz bypass in StrictRolePermission.
  → upgrade lemur to ≥1.9.2.
- [CVE-2026-48713](https://github.com/advisories/GHSA-2933-q333-qg83) + [CVE-2026-48714](https://github.com/advisories/GHSA-f49m-vf83-692w) — i18next (npm) · CVSS 9.1×2
  prototype pollution via crafted missing-key strings.
  → upgrade i18next-fs-backend ≥2.6.6, i18next-http-middleware ≥3.9.7.

*MONITOR*
- [GHSA-rjr7-jggh-pgcp](https://github.com/advisories/GHSA-rjr7-jggh-pgcp) — chi (Go) X-Forwarded-For IP spoofing · no CVE · v5 fix 5.3.0, v1-v4 no fix
  → bump chi v5 to ≥5.3.0; legacy lines pin behind a trusted proxy.
- [CVE-2026-48702](https://github.com/advisories/GHSA-47q9-m4ww-924m) — sigstore Rekor (Go) · CVSS 7.5 · EPSS 0.004
  gzip-bomb OOM in Alpine APK parser. → upgrade rekor to ≥1.5.2.
- [CVE-2026-9291](https://github.com/advisories/GHSA-g697-2xrc-gc46) — amazon-braket-sdk (pip) · CVSS 7.1
  insecure pickle.loads(). → upgrade to ≥1.117.0.
