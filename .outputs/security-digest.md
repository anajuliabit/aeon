*Security Digest — 2026-07-11*
Verdict: 3 to patch today (2 KEV Joomla + polymarket brand-jack day-2), 5 to schedule. _Sources: KEV ok, GH Advisory ok, EPSS ok_

*PATCH TODAY*
- [CVE-2026-56291](https://nvd.nist.gov/vuln/detail/CVE-2026-56291) + [CVE-2026-48939](https://nvd.nist.gov/vuln/detail/CVE-2026-48939) — Balbooa Forms + iCagenda (Joomla ext) · KEV added 2026-07-10 · EPSS 0.008 / 0.015
  same-day KEV pair, both unauth arbitrary file upload → PHP RCE. joomla ecosystem, not tracked stack — awareness item.
  → if joomla is deployed: disable Balbooa Forms + iCagenda extensions until vendor patch; assume post-compromise if admin panel was public.
- [GHSA-59wg-mh66-248p +5](https://github.com/advisories/GHSA-59wg-mh66-248p) — polymarket + polygon 6-pkg brand-jack (npm) · type=malware · published 2026-07-10 16:12Z
  day-2 escalation of yesterday's polymarket-kelly-stake-math. minute-clustered publish: polymarket-gamma-apis, polymarket-trader-apis, polymarket-apis, polygon-gamma-apis, polygon-gama-apis. wallet/api-key stealer targeting polymarket devs + polygon L2 tooling.
  → grep lockfiles for those 6 names; if hit, remove + rotate polymarket api keys + wallet privkeys + polygon rpc creds. real sdks live under `@polymarket/*`.
- [GHSA-99j7-fhr2-xfj4](https://github.com/advisories/GHSA-99j7-fhr2-xfj4) — `exploration` (crates.io) · removed for malicious code · published 2026-07-10
  first tracked-stack malware crossover beyond npm this window. 1 version published 2026-06-02, yanked ~1h later, no evidence of usage per Socket. brand-jack wave day-4 signal.
  → grep Cargo.lock for `exploration`; likely clean, log the check.

*PATCH THIS WEEK*
- [CVE-2026-54088](https://github.com/advisories/GHSA-m93h-4hw7-5qcm) + [CVE-2026-54089](https://github.com/advisories/GHSA-xqp3-jq6g-x3qm) — filebrowser/v2 (Go) · critical pre-auth RCE + CVSS 9.1 auth-bypass · EPSS 0.005 / 0.003
  command injection via auth-hook shell substitution + proxy-header forgery. self-hosted go admin, wide deploy.
  → upgrade filebrowser past 2.63.18.
- [CVE-2026-54072](https://github.com/advisories/GHSA-h29v-hj44-q8cv) — authorizerdev/authorizer (Go) · CVSS 9.3
  unvalidated `redirect_uri` in `/authorize` leaks oauth2 tokens to attacker url.
  → upgrade authorizer past commit bd3f5baf6d3d (2026-04-09).
- [CVE-2026-54174](https://github.com/advisories/GHSA-fpg8-7664-jc5q) — chainguard apko + melange (Go) · CVSS 8.3
  incomplete package integrity verification allows data-section substitution. build-tooling supply-chain.
  → apko ≥1.2.9, melange ≥0.50.4.
- [CVE-2026-49866](https://github.com/advisories/GHSA-cwc9-cp4j-mcvv) — @libp2p/gossipsub (npm) · CVSS 7.5 · EPSS 0.004
  cpu dos via oversized IHAVE/IWANT control arrays. wide dep in web3 / ipfs / p2p stacks.
  → upgrade @libp2p/gossipsub ≥16.0.0.
- [CVE-2026-54063](https://github.com/advisories/GHSA-h69g-9hx6-f3v4) — xuri/excelize/v2 (Go) · CVSS 7.5 · EPSS 0.006
  unbounded row-index allocation in worksheet parser → oom/panic. widely-used xlsx lib.
  → upgrade excelize/v2 ≥2.11.0.

_Other net-new malware not in tracked stack: 5-pkg 16:24Z enterprise-brand-jack (@higherlogic, @amtrav, @genie-auth, @att-ebiz, visa-cli-tools), type-atob/type-plint/type-elint typo cluster (20:33-37Z), authvaultx + auth-next-gen (7-11 00:07Z). Yesterday's @redhat-cloud-services 14-pkg wave already logged; deduped._
