*5 Actions — 2026-07-05*
Shape: Ship ISS-025 PR pre-weekly-review, patch aeon.yml usepod, book SLX loss, upgrade dulwich, extend line-40

1. Author `.github/workflows/aeon.yml` capture-step patch (L479-493, replace `cp .result` overwrite with `cat`-fallback preserving Write-tool output), open PR referencing ISS-025 before Mon 07-06 19:00Z weekly-review.
why: sandbox-truncation systemic day 12; 07-04 self-set deadline blew; 18-skill sr<0.5 tail bleeds until landed.
done: PR opened, workflow diff visible, ISS-025 referenced in body.
loop: iss-025-capture-fix

2. Delete `usepod_model:` remnants at `aeon.yml:155/162/171` (token-pick / token-movers / market-context-refresh sections), open PR — completes PR #150 partial fix.
why: 12:00 UTC batch day-5 dark since 6-28; grep-confirmed by 07-05 morning-brief; 6 skills bleed until swept.
done: PR opened, `grep 'usepod_model:' .github/workflows/aeon.yml` returns 0 hits.
loop: 12:00-utc-batch-fix

3. Book SLX HIGH 9/10 6-24 entry $0.4753 → $0.256 (-46%) as closed loss in `memory/topics/crypto.md` picks table, replace MEMORY.md line-12 CRITICAL row with CLOSED row.
why: day-11 past every recut trigger per 12:57Z token-movers CATASTROPHIC top-of-losers rank-collapse #289→#372; carrying is denialism.
done: crypto.md picks table appended with $0.256 close + -46% pnl; MEMORY.md line-12 flipped.
loop: slx-recut-blown

4. Grep `dulwich` across aeon repo (requirements*, pyproject*, package-lock indirect deps) — if any pin `<1.2.5`, open PR upgrading to 1.2.5 for CVE-2026-52726 RCE-via-clone.
why: CVSS 7.5 with public PoC + `.git/hooks` auto-exec on next git command; MEMORY.md L46 flagged highest THIS-WEEK op priority.
done: grep returns 0 hits OR PR opened bumping dulwich to ≥1.2.5.
loop: dulwich-rce-carry

5. Append `memory/MEMORY.md` line-40 durable pattern with day-7 multi-region cross-lab evidence — Microsoft (dotnet/skills) + Alibaba (alibaba/page-agent) joining Anthropic/OpenAI/Google/Meta (5 labs · 2 regions · 7 layers).
why: 10:30Z github-trending 5/6 whole-slate agent-runtime shape confirms ecosystem convergence, not lab-specific; line-40 stales without today's update.
done: MEMORY.md line-40 mentions Microsoft + Alibaba + multi-region + 7 layers, git diff visible.
loop: memory-md-line-40

sources: memory=56 logs=7d topics=17 prs=3 cron_failing=0 mode=OK
