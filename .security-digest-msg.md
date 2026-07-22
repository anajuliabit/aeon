*security digest — 2026-07-22*
verdict: 3 actively exploited (2 no-patch-yet), 3 to schedule, 3 to monitor. _sources: kev, gh advisory, epss_

*PATCH TODAY*
- [CVE-2026-39808](https://nvd.nist.gov/vuln/detail/CVE-2026-39808) — fortinet fortisandbox · kev 7-16 · epss 0.84 · cvss 9.8
  unauth os command injection via crafted http. highest epss in feed, public poc, no vendor patch yet.
  → isolate mgmt interface + follow FG-IR-26-100 mitigations today.
- [CVE-2026-25089](https://nvd.nist.gov/vuln/detail/CVE-2026-25089) — fortinet fortisandbox · kev 7-16 · epss 0.36 · cvss 9.8
  second unauth cmd injection in same line (4.2 / 4.4.0-4.4.8 / 5.0.0-5.0.5). no vendor patch.
  → isolate + follow FG-IR-26-141 mitigations today.
- [CVE-2021-27137](https://nvd.nist.gov/vuln/detail/CVE-2021-27137) — dd-wrt firmware · kev 7-21 · epss 0.11 · cvss 9.8
  4-year-old upnp m-search stack overflow re-flagged after in-the-wild use. poc public.
  → upgrade dd-wrt to build 45724+ or disable upnp.

*PATCH THIS WEEK*
- [GHSA-pf56-329r-95rw](https://github.com/advisories/GHSA-pf56-329r-95rw) — @sigstore/oci (npm) · cvss 9.6 · epss 0.32%
  substring credential match leaks docker config creds to attacker-controlled registry.
  → upgrade @sigstore/oci to ≥0.7.1.
- [GHSA-p63j-vcc4-9vmv](https://github.com/advisories/GHSA-p63j-vcc4-9vmv) — @vitest/browser (npm) · cvss 9.4 · no cve
  browser mode bypasses allowwrite gate; arbitrary local fs read/write/delete during tests.
  → upgrade to ≥4.1.10 (v4) / ≥3.2.7 (v3) / ≥5.0.0-beta.6 (v5).
- gitea (go) · 8-cve mass-disclosure 7-21 · cvss 8.1–9.8
  X-WEBAUTH-USER any-ip impersonation, ssrf filter bypass, actions artifact hmac ambiguity, pr permission bypasses.
  → self-hosted: upgrade gitea to ≥1.27.0.

*MONITOR*
- [GHSA-2f96-g7mh-g2hx](https://github.com/advisories/GHSA-2f96-g7mh-g2hx) — gitpython (pip) · 3 ghsas 7-21 · cvss 8.4–8.8 · no fix ≤3.1.50
  cmd injection via git long-option prefix, unguarded ls_remote/archive, joined-short-option bypass.
  → avoid untrusted-input remote urls in git ops; wait for patched release.
- [GHSA-fmm7-x4gx-8jhr](https://github.com/advisories/GHSA-fmm7-x4gx-8jhr) — file browser (go) · cve-2026-55667 · cvss 8.2 · no fix ≤2.63.15
  out-of-scope file delete via symlink-following removeall in create-only scope.
  → restrict create-only scopes; watch for patched release.
- pip supply-chain: 100+ typosquat malware batch 7-21 17:24z (extends 14:14z wave)
  yfinance clone-cluster (yfnance / yfiance / yfinace / yfiannce / yfinaance / yfinannce / yfinancee) + xolof-* + yc-* stubs, same-second alphabet-sort = scanner retro-ingest.
  → tighten pinning; verify yfinance install path is authentic.
