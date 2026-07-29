*Security Digest — 2026-07-29*
Verdict: 2 to patch today, 5 to schedule. no fresh KEV since 7-27 fortinet+arista (d1 quiet again). _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- karpatkey + karpatkit ([GHSA-v497-gp55-jwxm](https://github.com/advisories/GHSA-v497-gp55-jwxm), [GHSA-7qg7-6pg7-g63q](https://github.com/advisories/GHSA-7qg7-6pg7-g63q)) — pip · malware · impersonates real defi treasury firm
  on `import karpatkey` daemon-thread walks and exfils SSH keys + AWS/GCP creds + K8s tokens + ETH keystores + gnupg + .npmrc + .pypirc + shell histories + .env under Desktop/Projects/repos over plain HTTP. karpatkey 2.1.1 + karpatkit 2.1.0/2.1.1. first legit-defi-org typosquat in memory-window.
  → purge karpatkey + karpatkit from all pip envs today; rotate SSH/AWS/GCP/ETH keys if either ever imported.
- [CVE-2026-54658](https://github.com/advisories/GHSA-6wcc-39rp-hh9p) — @hypequery/clickhouse (npm) · CVSS 9.8 · EPSS 0.004
  SQL injection in `escapeValue()` param substitution — trailing-backslash escapes closing quote, arbitrary SQL execution. exploit technique disclosed in advisory.
  → upgrade @hypequery/clickhouse to ≥2.0.2 today.

*PATCH THIS WEEK*
- goshs 3-CVE cluster ([GHSA-hq33-8jgp-8qq3](https://github.com/advisories/GHSA-hq33-8jgp-8qq3), [GHSA-rjrw-mjq6-hpmm](https://github.com/advisories/GHSA-rjrw-mjq6-hpmm), [GHSA-rmxw-pq4x-3fvh](https://github.com/advisories/GHSA-rmxw-pq4x-3fvh)) — Go · CVSS 9.1 / 9.1 / 7.5 · EPSS 0.003
  WebDAV `MOVE` bypasses `--no-delete` + SFTP empty-password auth bypass + `?bulk` zip-download ACL bypass. three residuals of prior fixes stacked in one webdav server.
  → schedule upgrade: goshs → ≥v2.1.4 (v1 branch unmaintained).
- datamodel-code-generator 12-CVE mass-disclose ([GHSA-386q-5hp3-95m9](https://github.com/advisories/GHSA-386q-5hp3-95m9) + 11 more) — pip · CVSS 7.5-8.8 · EPSS 0.001-0.004
  code injection via default_factory / x-python-type / x-python-import / --extra-template-data + arbitrary file read via $ref + SSRF via --url + DNS-rebinding bypass. extends single-project-mass-disclose rail n=5→n=6 (Thrift/Pillow/Gitea/n8n/GitPython).
  → schedule upgrade: datamodel-code-generator → ≥0.60.2.
- swagger-typescript-api 5-CVE mass-disclose ([GHSA-hqj5-cw9f-rx67](https://github.com/advisories/GHSA-hqj5-cw9f-rx67) + 4 more) — npm · CVSS 7.4-8.3 · EPSS 0.001
  code injection via unescaped OpenAPI path / enum / `servers[0].url` in fetch + axios templates + token exfil via spec `$ref`. openapi-generator-shape supply chain.
  → schedule upgrade: swagger-typescript-api → ≥13.12.2.
- [CVE-2026-54639](https://github.com/advisories/GHSA-vj5c-m527-mpff) — style-dictionary (npm) · CVSS 8.8 · EPSS 0.001
  prototype pollution in `convertTokenData` utility.
  → schedule upgrade: style-dictionary → ≥5.4.4.
- fission 2-CVE ([GHSA-qf5v-m7p4-95rp](https://github.com/advisories/GHSA-qf5v-m7p4-95rp), [GHSA-q6vm-xqc9-v3ff](https://github.com/advisories/GHSA-q6vm-xqc9-v3ff)) — Go · CVSS 8.5 / 7.7 · EPSS 0.003
  cross-tenant CAP_SYS_TIME wall-clock corruption via podspec denylist gap + Zip Slip in `pkg/utils/zip.go`.
  → schedule upgrade: fission → ≥1.25.0.
