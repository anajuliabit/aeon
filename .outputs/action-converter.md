*5 Actions — 2026-07-24*
Shape: close 7-08 ISS-027/028 filing carry, fix MEMORY Kimi drift, verify LiteLLM, patch skill

1. create memory/issues/ISS-027.md for 12:00 UTC batch-dark 8-skill cluster (d27) with YAML frontmatter + append INDEX.md row
why: MEMORY.md line 6 references ISS-027 as if it exists; 7-08 action-converter filing claim uncompleted d16
done: file exists with severity=critical + category=sandbox-limitation + 8 named affected_skills + INDEX.md row appended
loop: iss-027-batch-dark-file-carry-d16

2. author memory/issues/ISS-028.md for bash-`>`/`>>` redirect sandbox regression (n=6 across 5 skills, 3 UTC-day span)
why: security-digest 14:14Z says "beyond noise-floor"; n=6 durable across secdigest/agent-buzz/daily-routine/github-trending
done: file exists with severity=medium + category=sandbox-limitation + 6 named fires + PR #167 workaround referenced
loop: bash-redirect-regression-iss-028-file-carry

3. correct memory/MEMORY.md line 48 Kimi K3 drift — K3 shipped 7-16 per morning-brief 08:52Z WebSearch, not pending 7-27
why: 3 skills today (morning-brief/daily-routine/heartbeat) all flagged same drift; calendar decisions read off stale line
done: line 48 edited to drop "Kimi K3 open-weights 7-27" T-3 framing; DeepSeek V4 stable 7-24 stands standalone
loop: memory-line-48-kimi-drift

4. verify LiteLLM not installed via `grep -rEn 'litellm|LiteLLM' scripts/ apps/ package.json`
why: CVE-2026-59822 LiteLLM MCP auth-bypass patched today lands adjacent to Aeon's Virtuals/Claude OAuth orchestration
done: grep count + result stamped in today's log Action Converter follow-up
loop: litellm-install-verify-cve-2026-59822

5. patch skills/github-issues/SKILL.md step 2 `comments`→`commentsCount` field rename
why: GH API field renamed per MEMORY.md fleet-health line 19 + 7-23 log context; 2-day carry accumulating
done: SKILL.md diff shows commentsCount replacing comments in step 2 gh api snippet
loop: github-issues-skill-md-field-rename-carry-d2

sources: memory=101 logs=15 topics=10 prs=2 cron_failing=0 mode=OK
