Scratch cleanup blocked — leaving `.tmp-*` files (already noted in MEMORY.md as a tracked cleanup item).

## Summary

Executed `security-digest` skill. Pulled CISA KEV (5 new entries since 2026-05-25), GitHub Advisory Database (3 critical + 7 high since 2026-05-30), and FIRST EPSS scores. Ranked into actionable tiers and staged a notification.

**Headline:** 2 npm supply-chain KEV adds in one week — Nx Console and TanStack (42 packages) — both ransomware-linked. First time tracked stack has had concurrent npm KEV entries.

**Output:**
- **PATCH TODAY (3):** PAN-OS auth bypass (EPSS 0.415), Nx Console npm malware → ≥18.100.0, TanStack npm malware → @tanstack/react-router ≥1.169.9 + rotate npm tokens
- **PATCH THIS WEEK (5):** vitest RCE → ≥4.1.0 (CVSS 9.8, public PoC confirmed), praisonai-platform → ≥0.1.4 (covers 5 IDOR CVEs), @vitest/browser → ≥4.1.6, dompurify → ≥3.4.5, nezha → ≥2.0.12
- **MONITOR:** dropped (all remaining have fix versions; strict tier rule wasn't met)

**Files:**
- Created `.pending-notify/1748736000-security-digest.md` (~2.4K chars, post-run delivery)
- Appended `### security-digest` entry to `memory/logs/2026-06-01.md`

**Exit:** SECURITY_DIGEST_OK — all 3 sources ok (kev, gh, epss), tiers non-empty.
