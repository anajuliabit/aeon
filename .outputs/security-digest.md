## Summary

Ran `skills/security-digest/SKILL.md` for 2026-06-05. KEV had **0 new entries since yesterday** (all 5 in-window adds already deduped from 6-03/6-04 logs — first zero-new-KEV day since digest went live).

**Tier output:**
- **PATCH TODAY (1):** `@cap-js/openapi` (npm) supply chain compromise — v1.4.1 shipped credential-harvesting + self-propagation code on 2026-05-19. CVSS 9.6, fix 1.4.2. Elevated by analogy to KEV (confirmed in-wild credential theft, though formally outside strict ≥9.8+PoC TODAY rule). **First supply-chain PATCH TODAY since digest went live.**
- **PATCH THIS WEEK (1):** `stata-mcp` (pip) CVE-2026-47708 — critical command injection via `log_file_name`, public PoC in advisory, fix 1.17.3.
- **MONITOR (1):** `browserstack-runner` (npm) CVE-2026-49144 — unauth path traversal, no patch yet (≤0.9.5). Sibling to yesterday's 49143 RCE in same package.

**Files modified:**
- `.pending-notify/1780669255-security-digest.md` (1,272 chars, staged for post-run delivery per sandbox pattern — `./notify "$(cat ...)"` arg-passing blocked)
- `memory/logs/2026-06-05.md` (appended `### security-digest` entry with full tier-counts, IDs, dedup audit, ranking decisions, WebFetch patch details, EPSS results, sources status)

**Follow-up flagged for next reflect:** Skill's strict `CVSS ≥9.8 AND public PoC` PATCH TODAY rule didn't catch CVSS 9.6 supply-chain-compromise — applied KEV-analog elevation this run, may want to codify a "confirmed-malicious-package-published" supply-chain rule alongside KEV in step 5.

**Status:** SECURITY_DIGEST_OK · sources kev=ok gh=ok epss=ok.
