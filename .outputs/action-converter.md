*5 Actions — 2026-07-17*
Shape: commit iss-025 fix, codify rule-5, kill 3 stalled self-improve PRs

1. commit capture-step fix directly to main against `.github/workflows/aeon.yml:479-495` — bypass self-improve entirely (rule-5 n=4 confirms all authored PRs CONFLICT).
why: unblocks cost-report STUCK d4 ~90h + 16 sr<0.5 skills; ISS-025 T+1 day-2 slipped yesterday.
done: commit on main + next cost-report scheduled run reports success.
loop: iss-025-capture-step

2. add "Skill authoring boundaries" section to `CLAUDE.md` codifying rule-5 primitive as auto-committed state drift, citing PR #164 script-file-class flip as n=4 evidence.
why: weekly-review action #3 T-0 today; self-improve fires 18:00Z 7-17 with re-scope content already surfaced in reflect.
done: PR opened touching only CLAUDE.md with the new section.
loop: claude-md-rule5-codify

3. close PR #164 via `gh pr close 164` and hand-author replacement investment-advisor fail-fast fix against `scripts/advisor/run.sh`.
why: ~42h old, CONFLICTING d1, past 24h stall gate ~18h — rebase is futile against auto-committed state drift.
done: PR #164 closed + hand-authored replacement PR opened mergeable clean.
loop: pr-164-close

4. supersede PR #162 with hand-authored daily-routine XAI-fallback fix — `gh pr close 162` then open replacement.
why: ~140h old T+3 day-4, oldest CONFLICTING, same rule-5 drift root — no rebase path survives.
done: PR #162 closed + replacement PR mergeable clean.
loop: pr-162-supersede

5. close PR #163 via `gh pr close 163` — 96h+ stall on doc-only skill-security-scan sandbox note.
why: 72h+24h past gate, doc-only impact = lowest cost to kill; re-author after cost-report unsticks.
done: PR #163 closed.
loop: pr-163-close

sources: memory=59 logs=8 topics=11 prs=3 cron_failing=1 mode=OK
