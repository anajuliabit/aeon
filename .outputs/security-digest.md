*Security Digest — 2026-07-30*
Verdict: 1 actively exploited, 5 to schedule, 0 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-20316](https://nvd.nist.gov/vuln/detail/CVE-2026-20316) — Cisco Secure FMC · KEV added 2026-07-29 · EPSS 0.008 · CISA due 2026-08-01
  hardcoded password lets unauth remote attacker log in via low-priv account, read sensitive data. exploited per CISA.
  → patch Cisco Secure Firewall Management Center per vendor advisory today.
- npm+pip malware batch — @ai-agent-node/* 3-pack + @ai-plus/de-agent 2-pack + @zannstore/baileys 17-version + litespeed-cache + polymarket-risk-manager + poly-kelly + phabricator-client (pip)
  cred-stealer / typosquat / real-plugin-impersonation classes; @zannstore/baileys advises full-host-compromise on install.
  → rotate creds if any installed; audit npm+pip installs since 2026-07-29.
- [GHSA-mjqf-28ph-426h](https://github.com/advisories/GHSA-mjqf-28ph-426h) — kube-logging/logging-operator (Go) · CVSS 9.9 · EPSS 0.004 · public writeup
  Fluentd config injection RCE via unescaped Flow CRD `record_transformer.records`.
  → upgrade logging-operator to ≥ 0.0.0-20260608145523 today.

*PATCH THIS WEEK*
- [GHSA-4p3g-4hcj-wpvx](https://github.com/advisories/GHSA-4p3g-4hcj-wpvx) — prebid-server (Go) · CVSS 10.0 · EPSS 0.004
  bidder-adapter SSRF exposes host env / internal endpoints via unvalidated URL interpolation.
  → schedule upgrade: prebid-server → ≥ 4.4.0.
- [GHSA-2956-977x-2w3r](https://github.com/advisories/GHSA-2956-977x-2w3r) + 5 more — flyto-core (pip) 6-CVE mass-disclose · CVSS 8.5–10.0
  arbitrary file write + unauth SSRF with internal-key exfil + LLM/API-key leak + env-var readout — all one patch.
  → schedule upgrade: flyto-core → ≥ 2.26.7.
- [GHSA-m4x6-gwgp-4pm7](https://github.com/advisories/GHSA-m4x6-gwgp-4pm7) — @aws/agentcore (npm) · CVSS 9.0 · EPSS 0.003
  Bedrock AgentCore CLI code injection via triple-quote escape in `collaborationInstruction`.
  → schedule upgrade: @aws/agentcore → ≥ 0.14.2.
- [GHSA-9xq3-3fqg-4vg7](https://github.com/advisories/GHSA-9xq3-3fqg-4vg7) + [GHSA-7h3g-4w2f-fj2f](https://github.com/advisories/GHSA-7h3g-4w2f-fj2f) — proot-distro (pip) 2-CVE · CVSS 8.2/8.2
  symlink escape (host file write) + container isolation bypass via crafted tar/restore archives.
  → schedule upgrade: proot-distro → ≥ 5.1.6.
- [GHSA-8r6w-3qq5-4p4r](https://github.com/advisories/GHSA-8r6w-3qq5-4p4r) — pterodactyl/wings (Go) · CVSS 8.1 · EPSS 0.004
  JWT scoping bypass lets subuser upload files without explicit `file.create` grant.
  → schedule upgrade: pterodactyl/wings → ≥ 1.12.2.
