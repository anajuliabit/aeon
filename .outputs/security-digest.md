*Security Digest — 2026-08-09*
Verdict: nothing net-new in tracked stack (6 KEV / 8 GH high / 1 GH crit all dedup vs 8-07/8-08 logs). 3 fresh npm+pip malware sub-clusters to purge. _Sources: KEV ok, GH ok, EPSS ok_

*PATCH TODAY*
- [statist-browser-typed-client cluster](https://github.com/advisories/GHSA-4fvg-gp6j-v2qm) — npm · 7 pkgs · malware · CVSS n/a · EPSS n/a
  Full-compromise template (host secrets exfil'd, treat host as compromised). Reads as `enterprise-corp-scope-dep-confusion` sibling — pwakasko, tdevice, pwahelp, tdeal, pwainsurance, pwafamily, projects.pwa*.
  → grep lockfiles for `statist-browser-typed-client-eventea.projects.*`; if present, rotate all creds from a different machine and rebuild.

- [svelte-kit brand typosquat cluster](https://github.com/advisories/GHSA-9fg7-rqp2-7hpg) — npm · 4 pkgs · malware · CVSS n/a · EPSS n/a
  svelte-kit-cache + svelte-streak-kit + streak-map-kit + map-streak-kit — full-compromise template. Framework-brand-typosquat vector against SvelteKit users.
  → grep lockfiles for the 4 names; rotate creds on any hit.

- [pip:riakcs malicious](https://github.com/advisories/GHSA-3849-8v46-m7qx) — pip · 2 versions (0.0.1, 0.5.0) · malware · CVSS n/a · EPSS n/a
  First pip malicious of the 48h wave (npm-dominated cluster crosses ecosystem). PROBABLY_PENTEST class — host-info exfil, not full compromise.
  → uninstall riakcs if present (unlikely in aeon deps); worth logging as cross-ecosystem-escalation datapoint.
