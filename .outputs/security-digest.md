*Security Digest — 2026-08-03*
Verdict: 1 actively exploited, 5 to schedule, 2 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-18577](https://nvd.nist.gov/vuln/detail/CVE-2026-18577) — N-able N-central · KEV added 2026-08-03 · CISA due 2026-08-06 · EPSS 0.015 (71st pct)
  auth bypass via alternate path/channel, incomplete patch for CVE-2026-18556. exploited per CISA.
  → apply N-central 2026.3 HF1 today or discontinue per BOD 26-04.
- Malware batch — 26 fresh packages (25 npm + 1 pip) in 24h post-yesterday's digest
  beaver-ui-* 5-pack (dep-confusion corp-scope: header/layout/grid/date-range-picker/items-with-more) + simple-date-formatter-* 4-pack + houzidawang80* 3-pack (numeric variants) + accounts-final-form/accounts-loading-state + fluid-type-ui + @types-beta/sdk + tailwind-anim + @custombots/custombot + tailwindcss-anim + internallib_v568 + bigops-chat-messages + lifestyle-test-utils + list-issue-predecessor-dependencies-block (npm) + trongriden (pip). aeon-fleet grep clean.
  → block @beaver-ui/* + simple-date-formatter-* + houzidawang80* installs; rotate any creds exposed to fresh installs in the last 24h.

*PATCH THIS WEEK*
- [CVE-2026-69151](https://github.com/advisories/GHSA-jj27-h5hq-8x99) / [69149](https://github.com/advisories/GHSA-vpx6-8pjr-4g3v) / [68945](https://github.com/advisories/GHSA-jhpw-976m-542j) — Angular @common/@core/@compiler/@platform-server (npm) · 3 fresh advisories
  i18n XSS via event-handler attrs + SSR raw-content escaping gap + HttpTransferCache cross-request response reuse. → upgrade angular to ≥22.0.7 / ≥21.2.19 / ≥20.3.27 (19.x EOL, patch by upgrading major).
- [CVE-2026-69152](https://github.com/advisories/GHSA-rgw5-rvv9-x895) — brace-expansion (npm) · CVSS 7.5
  DoS via unbounded intermediate arrays, bypasses CVE-2026-14257 mitigation. near-universal transitive dep. → upgrade to ≥1.1.18 / ≥2.1.4 / ≥3.0.6 / ≥5.0.9.
- [CVE-2026-18446](https://github.com/advisories/GHSA-7p8r-x3mc-p8w7) — fast-uri (npm) · CVSS 7.5 · EPSS 0.002
  host confusion via backslash authority introducer. → upgrade to ≥2.4.4 / ≥3.1.5 / ≥4.1.2.
- [CVE-2026-69185](https://github.com/advisories/GHSA-2m8v-j782-fhvr) — socket.io-parser (npm) · CVSS 7.5
  zero-attachment memory exhaustion. → upgrade to ≥3.3.6 / ≥3.4.5 / ≥4.2.7.
- [CVE-2026-13697](https://github.com/advisories/GHSA-4cwx-7wf7-3272) — undici (npm) · CVSS 7.4 · EPSS 0.003
  cross-user info disclosure + parse-time crash via degenerate private cache directives. → upgrade to ≥7.29.0 / ≥8.9.0.

*MONITOR*
- [GHSA-3f7w-8rr8-f37f](https://github.com/advisories/GHSA-3f7w-8rr8-f37f) — GitPython (pip) · CVSS 8.1 · no fix yet · ≤3.1.56
  unguarded git-option forwarding in IndexFile.checkout() + TagReference.create() → arbitrary file overwrite + read. → avoid untrusted refspec input; watch for patched release.
- [CVE-2026-69192](https://github.com/advisories/GHSA-mwp4-54f8-5fhr) — ip-address (npm) · no fix yet · ≤10.3.0
  Address4 decodes leading-zero octets as decimal while resolvers decode as octal → SSRF + trust-boundary bypass. → don't rely on Address4 for SSRF prevention until patched.
