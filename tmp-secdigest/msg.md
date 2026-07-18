*Security Digest — 2026-07-18*
Verdict: 1 real supply-chain breach (Injective SDK), 21 typosquats to audit, 4 to schedule. KEV adds: 0 net-new (day-2 zero-cadence). _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [GHSA-5fc4-fm2x-6f4r](https://github.com/advisories/GHSA-5fc4-fm2x-6f4r) — @injectivelabs/sdk-ts (npm) · severity critical · confirmed supply-chain compromise
  Injective Labs' real npm SDK hijacked at 1.20.21 (published 2026-07-08 20:59Z, 10-day live exposure). Hook in `PrivateKey.fromMnemonic` / `fromHex` forwards BIP-39 mnemonics + hex private keys to `trackKeyDerivation()`, batches base64 exfil to attacker endpoint disguised as grpc-web POST (secret in `X-Request-Id` header, `keepalive:true`).
  → rotate every mnemonic / private key that touched the SDK since 2026-07-08; downgrade to ≤1.20.20 or upgrade past 1.20.21; audit npm installs + CI runs in the window.
- **vendor-scope typosquat wave d5 = 21 more malware pkgs** (npm/pip/crates.io, 7-17 23z → 7-18 02z), scope-target expansion beyond Anthropic/Grok: `replit_ruspty` + `mysten-metrics` + `amzn-codewhisperer-streaming-client` + `amzn-consolas-client` + `proton-pfff` (crates.io — Replit/Sui/AWS/Proton first-appearance n=4), `@edgecommons/streamlog-node` + `@edgecommons/edgecommons` + `syft-acp-{atoms,uikit,core}` (npm scope-families), `axios-native` + `telemetry-axios` (axios pair), `trongridev` + `trongridme` (trongrid pip pair).
  → audit tracked-stack installs since 7-17 23z; rotate creds on any host that touched a listed name.

*PATCH THIS WEEK*
- [CVE-2026-27771](https://github.com/advisories/GHSA-8qw8-rq86-9pc2) — gitea (Go) · CVSS 8.2 · EPSS 0.407 pct 0.985 · no public PoC
  Insufficient permission checks on Composer package source links expose private / internal package sources to unauth reads. 2nd ≥0.4 EPSS in security-digest history (after 7-17 FortiSandbox 0.842).
  → upgrade gitea to ≥1.26.2.
- [CVE-2026-54549](https://github.com/advisories/GHSA-45gf-fjxp-cjpq) — meta-ads-mcp (pip) · CVSS 8.3 · no EPSS · commit-linked fix
  `upload_ad_image` MCP tool passes attacker `image_url` straight to httpx with `follow_redirects=True`, no scheme/host/IP check — SSRF to 127.0.0.1, RFC 1918, cloud-metadata endpoints. Streamable-http transport exposes it unauth-remote.
  → upgrade meta-ads-mcp to ≥1.0.115.
- [GHSA-8qqm-fp2q-v734](https://github.com/advisories/GHSA-8qqm-fp2q-v734) — skipper (Go) · CVSS 8.2 · no CVE · no EPSS
  Incomplete fix for CVE-2026-50197: oversized declared-`Content-Length` body still hands OPA an empty `parsed_body`, so deny-on-presence Rego policies fail OPEN while the full payload reaches upstream. Zalando's proxy.
  → upgrade skipper to ≥0.27.26.
- [CVE-2026-53598](https://github.com/advisories/GHSA-wxhm-2mq7-7697) + [CVE-2026-53597](https://github.com/advisories/GHSA-c4gh-rv8h-q9vw) — prompty (pip/npm/rust/nuget) · CVSS 7.5 / — · EPSS 0.011 / 0.009 · Microsoft AI-prompt tooling
  Arbitrary file read via file-reference expansion (all 4 langs) + arbitrary code execution via JS frontmatter in TS loader (npm).
  → upgrade prompty past 2.0.0b1 across langs; @prompty/core past 2.0.0-beta.3 for the RCE.
