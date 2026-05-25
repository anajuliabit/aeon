*5 Actions — 2026-05-25*
Shape: Close today's reppo issues, ship ISS-005 durable fix, patch security + evals, sweep MEMORY.

1. Move ISS-004 / ISS-006 / ISS-007 to the resolved table in memory/issues/INDEX.md and set status=resolved + fix_pr to PR #10 / #11 / #13 in each ISS-*.md file
why: Today's 5-PR wave (#10 auto-grant, #11 reppo-lock helper, #13 RPC retry) shipped the fixes but tracker still flags them open
done: INDEX.md resolved table grew by 3 rows; ISS-004.md / ISS-006.md / ISS-007.md all carry status: resolved + fix_pr links
loop: iss-bookkeeping

2. Extend scripts/prefetch-reppo.sh to record per-pod validityEpoch in the pod cache and patch skills/reppo-trading-agent/SKILL.md to filter on validityEpoch >= currentEpoch — replaces the in-prompt <= current-1 workaround and resolves ISS-005
why: ISS-005 is the last cascade blocker without a PR; the contract belongs in prefetch, not the prompt
done: PR opened touching scripts/prefetch-reppo.sh + skills/reppo-trading-agent/SKILL.md; ISS-005.md gets fix_pr
loop: iss-005-durable-prefetch

3. Fix the 5 workflow-injection sites flagged in articles/security-scan-2026-05-25.md (.github/workflows/messages.yml:578, .github/workflows/aeon.yml:86/94/96/718) — replace inline \${{ inputs.skill }} / \${{ github.event.action }} with env-var indirection per articles/workflow-security-audit-2026-04-11.md
why: Five HIGH findings match the 2026-04-11 incident class and the fix shape is already documented — preemptive close while the audit is fresh
done: PR opened with env-var indirection at all 5 sites; next skill-security-scan delta drops these from the HIGH list
loop: security-scan-workflow-injection

4. Rewrite the 4 spec-drift rows in skills/skill-evals/evals.json — change token-alert + skill-health output_pattern from articles/*.md to memory/logs/YYYY-MM-DD.md, and delete the orphaned hn-digest + polymarket entries (no matching skills/ directory)
why: skill-evals coverage stuck at 12/29 because evals.json carries stale paths — surfaced as action-queue head in 2026-05-24 skill-evals bootstrap and untouched 1d
done: evals.json has 4 fewer wrong rows; next skill-evals run reports ≥14/29 coverage and 0 NO_OUTPUT from these four
loop: evals-json-output-pattern-fix

5. Sweep memory/MEMORY.md and memory/topics/fleet.md for today's 5-PR wave — drop "Populate soul/" from Current Goals (PR #12 closed it), drop PR #9 from Open PRs (merged), add ISS-007 row to Open Issues, and append PRs #10/#11/#12/#13 rows to the fleet.md infrastructure table
why: MEMORY.md and fleet.md are the next morning-brief's primary read; stale entries push the brief toward already-shipped work
done: MEMORY.md Current Goals = 2 bullets (soul gone); Open PRs reflects 0 open; fleet.md PR table has rows through #13
loop: memory-fleet-md-sweep

sources: memory=59 logs=5 topics=4 prs=0 cron_failing=0 mode=OK
