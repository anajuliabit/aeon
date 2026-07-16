*Security Digest — 2026-07-16*
verdict: 3 to patch today, 5 to schedule, 0 monitor. _sources: kev, gh advisory, epss_

*PATCH TODAY*
- npm-malware wave d3 · 16 pkgs 7-15 14z→7-16 08z
  `claude-token-tracker-mcp` (claude api token typosquat, fleet-adjacent scope) · `n8n-nodes-rce-poc` (n8n rce, adjacent to 7-15's n8n-mcp cve-2026-54052) · 08:13z 4-pkg p2p batch (`websight-p2p`/`websight2-p2p`/`ai-p2p`/`loader1`) · `fflask` (pip flask typosquat) · `rhynpm` (multi-version) · `npm-rce-poc` · `datefmt-helper`. count fades 30→16 vs d2 but wave carries into d3.
  → audit installs since 7-15 14z; rotate any anthropic api keys touched by `claude-token-tracker-mcp`.

- [CVE-2008-4128](https://nvd.nist.gov/vuln/detail/CVE-2008-4128) cisco ios 12.4 · kev added 7-13 · epss 0.239 pct 0.976 · **bod 26-04 due today**
  csrf on eol platform; 17-yr-old cve confirmed exploited. yesterday t-2, today t-0.
  → retire eol ios 12.4 or apply cisco mitigations; bod clock hits.

- [CVE-2026-46817](https://nvd.nist.gov/vuln/detail/CVE-2026-46817) oracle e-business suite · **kev fresh 7-15** · epss 0.010 pct 0.603 · bod due 7-18 t-2 · cvss 9.1
  improper privilege management, exploited per cisa. ebs = enterprise-crown-jewel scope.
  → patch per oracle cpu bulletin today.

*PATCH THIS WEEK*
- sharepoint + sonicwall sma1000 pair · **kev bod due t-1 tomorrow** · [CVE-2026-56164](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-56164) sharepoint epss 0.056 pct **0.920** (decays from 7-15's 0.070/0.935) · [CVE-2026-15409](https://nvd.nist.gov/vuln/detail/CVE-2026-15409)/[CVE-2026-15410](https://nvd.nist.gov/vuln/detail/CVE-2026-15410) sonicwall epss 0.013/0.015
  microsoft-infra 7-14 batch surfaced yesterday, deadline-imminent today.
  → apply msrc mitigations or discontinue; sonicwall single-release fix per snwlid-2026-0008.

- **mcp-server rce cluster n=3 · 48h shape** · [GHSA-3pvh](https://github.com/advisories/GHSA-3pvh-63gf-j9mw) langbot pip cvss 8.8 auth rce via mcp config (≤4.10.5, no fix) · [GHSA-6f5r](https://github.com/advisories/GHSA-6f5r-5672-72j7) `@andrea9293/mcp-documentation-server` npm cvss 8.8 web ui binds all interfaces no auth (=1.13.0) · n8n-mcp npm cve-2026-54052 from 7-15
  → audit mcp servers for open bind + auth; hold langbot + pin off mcp-documentation-server 1.13.0.

- **dd-trace polyglot cluster n=6** · same-day w3c baggage dos across pip/npm/go/rubygems/nuget/maven · all cvss 7.5 · [CVE-2026-50271](https://github.com/advisories/GHSA-mw54-j2v2-42hr) ddtrace pip <4.8.2 · CVE-2026-50272 dd-trace npm <5.100.0 · CVE-2026-50274 dd-trace-go v2 <2.8.1 (+dd-trace-rb/dotnet/java kin)
  → upgrade every dd-trace client; first cross-ecosystem single-vendor cluster in memory.

- [GHSA-xv26](https://github.com/advisories/GHSA-xv26-6w52-cph6) `websocket-driver` npm cve-2026-54466 · critical (cvss n/a, epss n/a) · protocol-length-header abuse corrupts messages · patched 0.7.5
  widely-embedded ws lib (faye deps, socket.io ancestor).
  → upgrade websocket-driver to ≥0.7.5.

- [CVE-2023-4346](https://nvd.nist.gov/vuln/detail/CVE-2023-4346) knx protocol · **kev fresh 7-15** · epss 0.009 pct 0.542 · bod due 7-29
  3-yr-old cve into kev; pairs with 7-13 cisco ios 12.4 2008-old = **old-cve-fresh-kev n=2 codifies**. iot/building-automation scope.
  → apply knx mitigations or air-gap admin plane.

state: d3 npm-malware carries with 30→16 fade · 2 fresh kev on 7-15 breaks 1-day quiet post-7-14 batch · sharepoint pct decays 0.935→0.920 · mcp-server rce cluster reaches n=3.
