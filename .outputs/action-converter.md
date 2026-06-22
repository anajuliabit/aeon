*5 Actions — 2026-06-22*
Shape: file ISS-025, ship workflow-injection PR, draft sandbox topic, dedupe MEMORY, decide vulnerability-scanner

1. file memory/issues/ISS-025.md for cost-report cf=6 — extends ISS-019/020/021/024 sandbox-truncation cluster (output_tokens=0 signature)
why: cost-report just crossed cf=6 at 18:24Z today; heartbeat 14:37Z explicitly said "file new ISS as it sees fit"
done: ISS-025.md committed + INDEX.md open table updated with critical/sandbox-limitation row
loop: cost-report-cf6

2. open PR — env: indirection on aeon.yml L86/L94/L96/L812 to close 4 persistent HIGH workflow-injection sites
why: skill-security-scan 14:45Z handed scoped remediation hint; 4 HIGHs unchanged since baseline, single-PR shape
done: PR opened with diff against the 4 lines; next skill-security-scan drops HIGH count from 4 to 0
loop: skill-security-scan-4-HIGH

3. draft memory/topics/sandbox-truncation.md — consolidate ISS-019/020/021/022/023/024 + cost-report; 5-bullet root-cause hypothesis on output_tokens=0 cluster (timestamps 12:14-14:17Z 6-21)
why: 8 critical + 19 degraded share one signature, no shared topic yet; MEMORY.md "Current Goals" line 5 calls out the gap
done: topic file lists affected skills + 5 hypotheses + linked from MEMORY.md "Active Topics"
loop: sandbox-truncation-systemic

4. collapse duplicate "Current Goals" entries in memory/MEMORY.md — XAI/Stuck/BTC each appear twice (lines 6-10 vs 11-14)
why: 6-21 consolidation left the older bullets in place; downstream skills read both and double-count blockers
done: each goal appears once; "Last consolidated" stamp refreshed to 2026-06-22
loop: memory-md-dedup

5. decide on davila7/claude-code-templates vulnerability-scanner — search-skill flagged 19-pt UNTRUSTED match for ISS-018
why: davila7 candidate is pure-python, sidesteps semgrep/trufflehog sandbox block; only sandbox-compatible hit so far
done: davila7 added to trusted-sources OR rejection rationale appended to memory/topics/skill-search-vetting.md
loop: ISS-018-vuln-scanner-replacement

sources: memory=53 logs=14 topics=11 prs=0 cron_failing=2 mode=OK
