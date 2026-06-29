*Security Digest — 2026-06-28*
Verdict: nothing urgent today. 4 to schedule, 1 to monitor. KEV adds: 0 net-new (3rd zero-cadence day). _Sources: KEV, GH Advisory, EPSS_

*PATCH THIS WEEK*
- [CVE-2026-48788](https://github.com/advisories/GHSA-4c8j-mgm4-qqvp) — Remark42 (Go) · CVSS 8.2 · EPSS 0.003 · no public PoC
  Image proxy at `/api/v1/img` trusts the remote `Content-Type` to accept, then sniffs bytes to serve — HTML/JS body claiming `image/png` lands as XSS on remark42's origin. → upgrade remark42 to ≥1.16.0.
- **gonic 3-CVE cluster** ([CVE-2026-49340](https://github.com/advisories/GHSA-4gxv-p5g5-j7w7) / [49339](https://github.com/advisories/GHSA-2fp4-5v5c-4448) / [49338](https://github.com/advisories/GHSA-hmgp-w9jm-vp95)) — go.senan.xyz/gonic · CVSS 8.1 / 7.1 / 7.1 · EPSS ~0.002 each
  Any authenticated Subsonic user gets arbitrary file write via `createPlaylist` (unreachable guard + no path containment, creates dirs with `0o777`) + path-traversal read + IDOR delete of any user's playlist. → upgrade gonic to ≥0.21.0.
- [CVE-2026-49291](https://github.com/advisories/GHSA-2r68-g678-7qr3) — mcp-memory-service (pip) · CVSS 8.1 · EPSS 0.003 · no public PoC
  MCP `/mcp` endpoint gates `tools/call` on OAuth `read` scope only, then dispatches mutating tools — `store_memory` / `delete_memory` callable from read-only clients. REST routes correctly require `write`; the MCP path is the bypass. → upgrade mcp-memory-service to ≥10.65.3.
- [CVE-2026-48797](https://github.com/advisories/GHSA-f65r-h4g3-3h9h) — backpropagate (pip) · severity critical · CVSS — · EPSS 0.003
  `backprop ui --auth user:pass` and `--share` documented as the security controls; the wiring is missing — UI exposes dataset upload, model load, training control, GGUF export, HF Hub push with no auth on either path. → upgrade backpropagate to ≥1.2.0; until then bind to 127.0.0.1 only.

*MONITOR*
- [GHSA-c6v2-3ffm-vcmc](https://github.com/advisories/GHSA-c6v2-3ffm-vcmc) — nebula-mesh (Go) · CVSS 8.8 · no fix yet · affects ≤0.3.4
  Web UI `/ui/*` skipped the per-operator CA scoping applied to the JSON API — any non-admin operator (e.g. self-registered / OIDC) can block, delete, or read any other operator's hosts and networks. → restrict UI to trusted operators until patch lands; treat self-registration / OIDC as admin-equivalent meantime.
