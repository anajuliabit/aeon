## Summary

Ran security-digest for 2026-06-09. First successful run since 2026-06-05 (6-06/6-07/6-08 lost to Claude weekly rate-limit cluster).

**Tier counts:** today=3, this-week=5, monitor=1

**PATCH TODAY (all NEW KEV since last digest):**
- CVE-2026-42271 BerriAI litellm — KEV 6-08, EPSS 0.61, fix 1.83.7
- CVE-2026-50751 Check Point Sec Gateway IKEv1 — KEV 6-08, due 6-11
- CVE-2026-28318 SolarWinds Serv-U DoS — KEV 6-05

**PATCH THIS WEEK:** `@doaction/*` 15-pkg npm supply-chain swarm (coordinated to 2s), 14 misc npm malware, nebula-mesh Go privesc (CVSS 9.9), anyquery Go plugin RCE (CVSS 9.0), shell-quote npm 8.1.

**MONITOR:** fuxa-server npm SSRF (no fix).

**Sources:** kev=ok, gh=ok, epss=ok. Carry-watch: Linux cgroups v1 CVE-2022-0492 EPSS climbed to 0.34.

**Files modified:**
- `.pending-notify/1781015858-security-digest.md` (3025 chars, staged for delivery)
- `memory/logs/2026-06-09.md` (security-digest section appended)

**Follow-up:** scratch file `.tmp-kev.json` blocked by sandbox `rm` — postprocess cleanup step will sweep it.
