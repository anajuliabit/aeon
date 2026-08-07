*Security Digest — 2026-08-07*
Verdict: 3 actively exploited or malicious, 4 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-63077](https://github.com/advisories/GHSA-cxjq-mrr5-89rv) — JetBrains TeamCity · KEV added 2026-08-05 · CISA due 2026-08-08 · EPSS 0.010 · CVSS n/a
  Unauth RCE via deserialization in agent-polling protocol. JetBrains 8-07 update confirms post-disclosure exploitation reports.
  → upgrade TeamCity to 2025.11.7 or 2026.1.3 today.
- [claude-remote-agent + remote-claude-daemon](https://github.com/advisories?query=type%3Amalware+claude-remote) — npm · malware · first Claude-brand-typosquat in memory-window
  Two coordinated Claude Code brand-typosquats published as malware. Fleet-relevant (aeon runs on Claude Code).
  → verify no dep pulls either name; rotate any tokens exposed to a machine that npm-installed them.
- [baileys npm cluster](https://github.com/advisories?query=type%3Amalware+baileys) — npm · malware · 8-pkg supply-chain campaign
  WhatsApp-automation library targeting: alipclutch/diezyclutch/diezyyasha/prototypevip/santana/xsat10/ynastore-baileys + shadowx-fca. Credential-stealer shape.
  → block all `*-baileys` variants; if downstream fraud-tooling touches Baileys, pin known-good `@whiskeysockets/baileys` and audit installs.

*PATCH THIS WEEK*
- [Traefik 6-CVE cluster](https://github.com/advisories/GHSA-cxjq-mrr5-89rv) — Go · CVSS 9.1 top · EPSS 0.004–0.007 · public PoC in advisory
  Researcher mass-disclose: auth bypass via path traversal in ReplacePathRegex (CVE-2026-65600 crit) + 5 highs on Gateway API namespace hijacking, Ingress-NGINX RewriteTarget bypass, CONNECT pool poisoning, headerField spoofing, TeamCity-style incomplete-patch.
  → upgrade traefik to 2.11.53 / 3.6.24 / 3.7.9.
- [CVE-2026-16633](https://github.com/advisories/GHSA-hq66-cqwq-w95j) — pdfjs-dist (npm) · CVSS n/a · EPSS n/a · no public PoC
  Arbitrary JS on opening a crafted PDF. ngx-extended-pdf-viewer 29.0.0-rc.3 ships the fix downstream.
  → upgrade pdfjs-dist to 6.2.108.
- [CVE-2026-71476](https://github.com/advisories/GHSA-vp3h-ghgh-jr7g) — nx (npm) · CVSS n/a · EPSS 0.006 · no public PoC
  Zip-slip in self-hosted remote cache; 8 companion `@nx/*-cache` packages have no patch.
  → upgrade nx to 22.7.7 or 23.0.2; treat any self-hosted `@nx/*-cache` install as unpatched.
- [GHSA-5p4m-2wfm-xmqj](https://github.com/advisories/GHSA-5p4m-2wfm-xmqj) — js-yaml (npm) · CVSS 7.5 · EPSS n/a · no public PoC
  Quadratic CPU consumption in !!omap resolution; CVE-2026-59870 fix not backported to 3.x/4.x.
  → upgrade js-yaml to 3.15.1 or 4.3.1.
