## Summary

Ran `skills/security-digest/SKILL.md`. 2 new KEV adds + 5 new GH advisories cleared dedup.

**Output**
- Notification staged: `.pending-notify/1780496205-security-digest.md` (post-run delivery picks it up — sandbox blocks `./notify "$(cat ...)"` arg-passing per the MEMORY.md-noted pattern).
- Log appended: `memory/logs/2026-06-03.md` — `### security-digest` section.

**Tiers**
- **PATCH TODAY (2):** CVE-2022-0492 linux kernel cgroups v1 release_agent (KEV 6-02, EPSS 0.263, CVSS 7.8, public docker-escape PoC, fix kernel ≥5.17); CVE-2025-48595 android framework integer overflow (KEV 6-02, EPSS 0.004, CVSS 8.4, affects android 14/15/16, dueDate 6-05).
- **PATCH THIS WEEK (2 entries, 5 CVEs):** GHSA-xwq8-frcg-77q8 praisonai-platform (pip) — bundled 4-CVE audit cluster (47412/47415/47417/47418, CVSS 8.1-8.3 IDORs), fix ≥0.1.4. GHSA-63gr-g7jc-v8rg @agenticmail/mcp (npm) — unauth HTTP MCP exposes master-key admin tools, **public PoC (bash+python)**, fix ≥0.9.27.
- **MONITOR:** empty.

**Notable**
- First kernel CVE in KEV in 3+ weeks (cgroups v1 escape — patched since 2022 but KEV add signals active exploitation now).
- First **MCP-server advisory** to surface in this skill (relevance to aeon/reppo MCP architecture flagged on watch radar).
- Scratch files left at repo root (`kev.json`, `nvd-22-0492.html` not created, `.tmp-kev-recent.json` empty stub) — sandbox blocks `rm` mid-run, MEMORY.md cleanup-scratch goal carries.

**Files modified**
- `memory/logs/2026-06-03.md` (security-digest section appended)
- `.pending-notify/1780496205-security-digest.md` (created)
- `kev.json`, `.tmp-kev-recent.json` (working scratch, will be cleaned in a future cleanup pass)
