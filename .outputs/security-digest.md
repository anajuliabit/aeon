*Security Digest — 2026-07-19*
Verdict: nothing urgent today. 3 to schedule, 1 to monitor. _Sources: KEV (0 net-new = day-3 zero-cadence), GH Advisory (0 malware net-new = wave breaks after d5=22), EPSS_

*PATCH THIS WEEK*
- [GHSA-rwxx-mrjm-wc2m](https://github.com/advisories/GHSA-rwxx-mrjm-wc2m) + [GHSA-8wr5-jm2h-8r4f](https://github.com/advisories/GHSA-8wr5-jm2h-8r4f) — vllm (pip) · CVSS 7.5 + 7.5 · EPSS 0.003 · no public PoC
  Same-day DoS pair — ReDoS in `structured_outputs.regex` (xgrammar/outlines backends compile without timeout) + remote DoS via invalid recovered token reinjection. → upgrade vllm to ≥0.24.0 (single bump covers both).
- [GHSA-q38v-wp89-2w55](https://github.com/advisories/GHSA-q38v-wp89-2w55) — sh (pip) · CVSS 7.9 · EPSS n/a · no public PoC
  `_uid` fails to drop supplementary groups → incomplete privilege drop. Widely-embedded subprocess wrapper; defense-in-depth erosion for anything spawning children as a lower-privileged uid. → upgrade sh to ≥2.2.4.
- [GHSA-2v2f-mvfg-ph56](https://github.com/advisories/GHSA-2v2f-mvfg-ph56) — meta-ads-mcp (pip) · CVSS 7.4 · EPSS n/a
  `X-Pipeboard-Token` header auth bypass reuses operator meta token. Same-package sibling to yesterday's CVE-2026-54549 SSRF (fixed by same version bump). → upgrade meta-ads-mcp to ≥1.0.115.

*MONITOR*
- [GHSA-r95q-fp26-h3hc](https://github.com/advisories/GHSA-r95q-fp26-h3hc) — @tak-ps/cloudtak (npm) · high · CVSS n/a · fix 13.10.0
  Authenticated full-read SSRF in `/api/esri*` routes — user-controlled URL fetched with no IP classification. → upgrade if CloudTAK is in your fleet; otherwise watch.
