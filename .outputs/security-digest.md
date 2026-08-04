*Security Digest — 2026-08-04*
Verdict: 3 supply-chain compromises live, 5 to schedule, 1 no-patch monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- npm keyv / cacheable ecosystem compromise — 25+ malicious packages: keyv, cacheable, cache-manager, cacheable-request, flat-cache, file-entry-cache, 21× @keyv/*, 4× @cacheable/*
  keyv is a transitive dep of axios / got / eslint / nest / jest. blast radius fleet-wide across npm.
  → audit `npm ls` for the names above; pin to last-known-clean or drop; rotate any credentials touched by affected versions.
- npm enterprise corp-scope batch — 88 fresh malicious packages: @servicetitan (47) + @onereach (23) + @or-sdk (18). largest single-day corp-scope batch in memory-window.
  → block internal npm publishes on those scopes; verify private-registry precedence over public; rotate scope-tokens.
- bitcoin-wallet-targeted batch — coldcard-helpers, psbt-utils, psbt-helpers, @zzzgenesis00/bip39-generator. fresh crypto-seed / psbt attack surface, sibling to today's Coldcard $89M escalation.
  → uninstall on any wallet-adjacent host; treat installed hosts as compromised; migrate keys off-device.

*PATCH THIS WEEK*
- [CVE-2026-69240](https://github.com/advisories/GHSA-v8fg-2rw7-q452) — sequelize (npm) · CVSS 9.8 · EPSS 0.003 · public PoC
  SQL injection on Oracle dialect via unsanitized TO_DATE / TO_TIMESTAMP. → upgrade sequelize to ≥6.37.4.
- [CVE-2026-69251](https://github.com/advisories/GHSA-g32j-mmxr-gfq5) — flowise (npm) · critical · EPSS too-new · public PoC
  authenticated RCE via TypeORM DataSource options. → upgrade flowise / flowise-components to ≥3.1.3.
- [CVE-2026-69250](https://github.com/advisories/GHSA-r745-8hwv-h473) — flowise (npm) · high · EPSS too-new · public PoC
  unauth SSRF + secret exfil via OAuth2 refresh. same 3.1.3 upgrade covers both.
- [CVE-2026-69244](https://github.com/advisories/GHSA-cq5v-8q36-5273) — aiohttp (pip) · high · EPSS 0.003 · no PoC
  OOB heap read in C parser on malformed chunked responses. → upgrade aiohttp to ≥3.14.3.
- [CVE-2026-69247](https://github.com/advisories/GHSA-g6cj-pr64-35w5) — cryptography (pip) · high · EPSS 0.002 · no PoC
  PKCS#7 EnvelopedData Bleichenbacher timing oracle. → upgrade cryptography to ≥50.0.0.

*MONITOR*
- [CVE-2026-69249](https://github.com/advisories/GHSA-jwv3-5hgf-82ww) — cryptography (pip) · high · EPSS 0.002 · no patch yet
  duplicate self-signed intermediates → exponential path-building. → constrain cert-chain sources; track fix.
