*Security Digest — 2026-06-23*
Verdict: 28 npm typosquats out today, kev quiet (2 net-new this week both deduped from 6-22). 5 to schedule, 2 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [free-claude](https://github.com/advisories/GHSA-7qpf-5pm7-57rh) / [free-anthropic-claude](https://github.com/advisories/GHSA-3h58-8ch3-mgp3) (npm) · type=malware · 2026-06-22 18:07Z
  Anthropic-themed typosquats — install hook runs malicious code.
  → grep lockfiles for either name; uninstall + rotate any token that touched the install env.
- 26 more npm malware drops 2026-06-23 06:10–12:15Z: `new-mjs-eslint`, `new-helper`, `new-eslint-1`, `new-ecro-helper`, `new-ts-helper`, `new-solt-1`, `eslint-helper-1`, `poly-utils`, `new-solt`, `new-ecro-1`, `local-ip-helper`, `ts-numbering`, `libsignal-node-travatiger`, `datacamp-light`, `chai-as-uphelded`, `chai-as-attested`, `node-slot`, `ts-wross`, `node-core-libs`, `node-fetch-utils`, `search-from-search`, `crud-respect`, `setka-editor`, `onboarding-respects-modal`, `carousel-controller-mixin`, `respects-switch` · type=malware
  Coordinated burst — typosquats of eslint, libsignal, node-fetch, chai, ts-tooling.
  → grep lockfiles; uninstall + rotate creds exposed to install if hit.

*PATCH THIS WEEK*
- [CVE-2026-54352](https://github.com/advisories/GHSA-w7mq-r738-x278) — @budibase/server (npm) · CVSS 9.6 · EPSS n/a · no kev
  Symlink in PWA-zip bypasses path validation → workspace builder reads `/data/.env` (JWT_SECRET, MINIO_*, REDIS_PASSWORD, COUCHDB_PASSWORD, DATABASE_URL).
  → upgrade @budibase/server to ≥3.39.9.
- [CVE-2026-33646](https://github.com/advisories/GHSA-fjj5-v948-whjj) — mise (crates.io) · CVSS 9.6 · EPSS n/a · no kev
  Tera template injection in `.tool-versions` files → arbitrary code execution on `mise trust`.
  → upgrade mise to ≥2026.3.10.
- [CVE-2026-48170](https://github.com/advisories/GHSA-9m6g-wc8r-q59c) — scim-patch (npm) · CVSS 9.1 · EPSS n/a · no kev
  Prototype pollution via unfiltered keys in scim patch ops.
  → upgrade scim-patch beyond 0.9.0.
- Budibase coordinated batch — 5 highs in @budibase/server + @budibase/backend-core (CVE-2026-54353/54351/50137/50136/50132/48153) · CVSS 7.3–8.5
  SSRF DNS-rebinding, mass-assignment in webhook trigger, unauth attachment URL, unauth S3 signed upload, account impersonation, OAuth2 SSRF.
  → upgrade @budibase/server + @budibase/backend-core to ≥3.39.9 (covers all).
- Gogs coordinated batch — 5 highs in gogs.io/gogs (CVE-2026-52801/52800/52799/52798/25119) · CVSS 7.5–8.9
  CSRF org-owner takeover, stored XSS in `.ipynb` preview, missing authz on attachment download, local-repo import via mirror, reverse-proxy header auth bypass.
  → upgrade gogs.io/gogs to ≥0.14.3.

*MONITOR*
- Glances 3-CVE batch ([CVE-2026-46606](https://github.com/advisories/GHSA-v5r2-qh84-fjx5)/[46607](https://github.com/advisories/GHSA-9837-48hr-q32j)/[46608](https://github.com/advisories/GHSA-87qc-fj39-wccr)) — glances (pip) · CVSS 7.4–7.8
  Insecure pickle deserialization (RCE), command injection via KVM/QEMU VM domain names, CORS wildcard fallback.
  → if running glances, upgrade to ≥4.5.5.
- [CVE-2026-46488](https://github.com/advisories/GHSA-r3cw-c95m-wfh9) — motioneye (pip) · severity=critical · CVSS n/a · no kev
  Authentication possible via password hash (auth bypass).
  → upgrade motioneye to ≥0.44.0.
