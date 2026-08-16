*Security Digest — 2026-08-16*
Verdict: nothing urgent today. 0 to schedule, 0 to monitor. malware wave collapsed 99% in 24h.
_Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [axios-fast](https://github.com/advisories/GHSA-7f9g-2m48-c7v6) · npm · malware · axios brand-jack · aeon dep-clean
  supply-chain compromise. → block install; rotate creds if pulled in dev.

_no fresh tracked-stack CVEs (3 new high advisories all outside stack: maven mchange-commons-java, maven OpenAM, composer Grav). `[[quiet-KEV-baseline]]` extends 3-consec → 4-consec-UTC-day (all 3 KEV adds still land on 8-11). malware wave 5,219+ → 57 in 48h (99% decompression) breaks `[[malware-only-security-surface]]` 6-consec streak and `[[security-surface-inversion]]` composite regime on day-2. residual clusters: notafollower* mass-registration (3 pkgs / 28 versions) + alelo-* brand-jack (7 pkgs = brazilian fuel-card) + hackerone-poc probes (tw-pkgprobe / hunterone-build-probe / twilio-hackerone-poc = bug-bounty dep-confusion tests, benign class). aeon fleet clean d17._
