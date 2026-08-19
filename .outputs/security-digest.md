*Security Digest — 2026-08-19*
Verdict: 5 actively exploited (KEV batch 8-18 breaks quiet-KEV day-1) · 5 to schedule · 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-33824](https://nvd.nist.gov/vuln/detail/CVE-2026-33824) — MS IKE Service Extensions · KEV added 2026-08-18 · EPSS 0.779 (99.5%ile) · due 2026-08-21
  double-free → RCE. memory-window-first same-day KEV add with EPSS >0.75.
  → apply august 2026 patch tuesday now.
- *KEV batch 2026-08-18* — [CVE-2026-59310](https://nvd.nist.gov/vuln/detail/CVE-2026-59310) VMware vCenter path-traversal → RCE (EPSS 0.024) · [CVE-2026-55040](https://nvd.nist.gov/vuln/detail/CVE-2026-55040) MS SharePoint weak auth bypass (EPSS 0.055, 92%ile) · [CVE-2026-65400](https://nvd.nist.gov/vuln/detail/CVE-2026-65400) Apple macOS Screen Sharing auth bypass. all due 2026-08-21.
  → patch each per vendor before 8-21 deadline.
- *NPM malware wave 8-19* — 179 fresh malicious pkgs since 09:31Z · fleet-adjacent: [@wizloft/harness-*](https://github.com/advisories/GHSA-jjpx-9cx9-ww85) 5-pkg family · [mcp-dev-toolkit](https://github.com/advisories/GHSA-rpcr-qj6g-5gw3) + 3 mcp-* pkgs · crypto cluster (eth-react-provider · evm-validation · layer2-sdk · eth-batcher).
  → block via `npm ci --ignore-scripts` · audit deps · rotate creds if any hit.

*PATCH THIS WEEK*
- [GHSA-2qvg-qr73-mqxp](https://github.com/advisories/GHSA-2qvg-qr73-mqxp) — wktk/conflibot (actions) · CVSS 9.1 · no PoC
  command injection via crafted PR branch names under `pull_request_target`. direct GHA-fleet-primitive risk.
  → upgrade wktk/conflibot to ≥1.2.1 in workflows.
- [GHSA-hfg8-hc9c-6c3h](https://github.com/advisories/GHSA-hfg8-hc9c-6c3h) — moby/go-archive (Go) · CVSS n/a · EPSS 0.002
  tar path-traversal write outside extraction dir. docker's archive lib = widely-installed transitive.
  → upgrade github.com/moby/go-archive to ≥0.3.0.
- *MONAI pip 3-CVE cluster* — [GHSA-wg9g-w2j2-8pgr](https://github.com/advisories/GHSA-wg9g-w2j2-8pgr) unsafe NumpyReader → RCE (CVSS 7.8) · [GHSA-rghg-q7wp-9767](https://github.com/advisories/GHSA-rghg-q7wp-9767) OS command injection · [GHSA-qxq5-qhx6-94qw](https://github.com/advisories/GHSA-qxq5-qhx6-94qw) incomplete-fix pickle.loads() RCE (CVSS 7.8). second deprecated-lib CVE storm after vm2 8-17.
  → upgrade monai to ≥1.6.0.
- [GHSA-rcr2-hggw-43wm](https://github.com/advisories/GHSA-rcr2-hggw-43wm) — surfio (pip) · CVSS 9.8 · EPSS 0.005
  out-of-bounds read.
  → upgrade surfio to ≥0.0.19.
- [GHSA-2mf3-mr2r-r4vf](https://github.com/advisories/GHSA-2mf3-mr2r-r4vf) — @rhinostone/swig family (npm) · CVSS 7.5 · no PoC
  path-traversal via include/extends in template engine (5-pkg family swig · swig-core · swig-twig · swig-jinja2 · swig-django).
  → upgrade family to ≥2.7.1.

*MONITOR*
- *Lemur pip 5-CVE cluster* — [GHSA-pxmc-2ffp-8j67](https://github.com/advisories/GHSA-pxmc-2ffp-8j67) + [GHSA-cfh6-pv5c-38jv](https://github.com/advisories/GHSA-cfh6-pv5c-38jv) + [GHSA-6c8m-q6g9-vrw3](https://github.com/advisories/GHSA-6c8m-q6g9-vrw3) + [GHSA-v5rc-cpwc-cfpr](https://github.com/advisories/GHSA-v5rc-cpwc-cfpr) + [GHSA-xpmj-wjcp-6pww](https://github.com/advisories/GHSA-xpmj-wjcp-6pww) · CVSS 7.3-8.1 · most no full patch
  cert-authority mismanagement + SSRF via ACME URL rewrite.
  → track; if using netflix/lemur, restrict admin API to trusted IPs.
- [GHSA-pr85-w493-9w3x](https://github.com/advisories/GHSA-pr85-w493-9w3x) — resdata (pip) · CVSS 9.8 · patched-null · EPSS n/a
  buffer overflow + null-deref + OOB read.
  → track; upgrade when 6.2.9 fully lands.
- [GHSA-j659-8xh6-5pq5](https://github.com/advisories/GHSA-j659-8xh6-5pq5) — atomic-agents-stack (pip) · CVSS n/a · no patch
  parallel fan-out bypasses cost-cap when model pricing missing = 2nd atomic-agents-stack CVE this week after 8-18 MCP-catalog. MCP-adjacent.
  → track; avoid this stack.
