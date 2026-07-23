*Security Digest — 2026-07-23*
Verdict: 2 actively exploited, 1 malware trio to purge, 5 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-50522](https://nvd.nist.gov/vuln/detail/CVE-2026-50522) — Microsoft SharePoint · KEV added 2026-07-22 · EPSS 0.21 · CISA due 2026-07-25
  Deserialization RCE, unauth over network. 2nd SharePoint KEV add in 7 days after CVE-2026-58644.
  → patch SharePoint to latest July CU today.
- [CVE-2026-16232](https://nvd.nist.gov/vuln/detail/CVE-2026-16232) — Check Point SmartConsole · KEV added 2026-07-22 · EPSS 0.01 · CISA due 2026-07-25
  Improper auth → unauth attacker obtains login token, authenticates with full admin.
  → apply Check Point hotfix on management server today.
- npm malware trio: `ethers-wallet-package`, `ethers-wallet-packages`, `ethers-packge` — [GHSA-7pvf-g7jg-rxpj](https://github.com/advisories/GHSA-7pvf-g7jg-rxpj) + gm49 + 67vw · ethers.js typosquat wallet-stealer, published 2026-07-23
  → grep lockfiles; any host that installed = compromised. Rotate keys from a clean box.

*PATCH THIS WEEK*
- [GHSA-8fpg-xm3f-6cx3](https://github.com/advisories/GHSA-8fpg-xm3f-6cx3) — next-auth (npm) · critical · published 2026-07-23
  Auth.js v5 fails open — the docs-recommended `if (auth) …` gate returns truthy on config error.
  → upgrade next-auth to ≥5.0.0-beta.32.
- [GHSA-7rqj-j65f-68wh](https://github.com/advisories/GHSA-7rqj-j65f-68wh) — next-auth, @auth/core (npm) · critical · published 2026-07-23
  Email normalizer validates before NFKC — Unicode homoglyph `@` bypasses address check in magic-link sign-in.
  → upgrade @auth/core ≥0.41.3, next-auth ≥4.24.15 / ≥5.0.0-beta.32.
- [GHSA-2p49-hgcm-8545](https://github.com/advisories/GHSA-2p49-hgcm-8545) — svgo (npm) · CVSS 8.2
  removeScripts plugin left executable scripts intact → XSS if you served the "sanitized" output.
  → upgrade svgo to ≥2.8.3 / ≥3.3.4 / ≥4.0.2.
- [GHSA-6g55-p6wh-862q](https://github.com/advisories/GHSA-6g55-p6wh-862q) — postcss (npm) · CVSS 7.5 · published 2026-07-23
  Attacker CSS `sourceMappingURL` dereferences arbitrary local path → first ~10 bytes of any Node-readable file leak.
  → upgrade postcss to ≥8.5.12.
- [GHSA-gx64-gj6p-pc4c](https://github.com/advisories/GHSA-gx64-gj6p-pc4c) — jupyterlab (pip) · high · published 2026-07-22
  Image viewer XSS + settings-import XSS pair ([GHSA-pppj-hq3g-57pj](https://github.com/advisories/GHSA-pppj-hq3g-57pj)).
  → upgrade jupyterlab to ≥4.5.10 or ≥4.6.2.

*MONITOR*
- pyasn1 DoS trio — [GHSA-8ppf-4f7h-5ppj](https://github.com/advisories/GHSA-8ppf-4f7h-5ppj) + m4p7 + hm4w (pip) · CVSS 7.5 · fix 0.6.4. Transitive under `cryptography`. → schedule upgrade.
- [GHSA-v56q-mh7h-f735](https://github.com/advisories/GHSA-v56q-mh7h-f735) — immutable.js `List` 32-bit trie overflow DoS · CVSS 7.5 → upgrade ≥4.3.9 / ≥5.1.8 when convenient.
- Malware feed: 100+ advisories in 48h (61 pip / 38 npm / 1 composer). ethers trio the only crypto-adjacent hit. → nothing installed today; watch for lockfile matches.
