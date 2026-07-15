*5 Actions — 2026-07-15*
Shape: unstick PR #162, commit ISS-025 patch, ship PR #163, draft ISS-027, register DEXE

1. Unstick PR #162 — rebase branch `fix/self-improve-2026-07-11` onto `main`, force-push, then merge or request review.
why: T+1 past weekly-review action #2 deadline (7-14); ~100h stalled; SKILL.md-editable class rebase clears the conflict.
done: `gh pr view 162 --json mergeable` returns MERGEABLE and PR is merged or has fresh reviewDecision.
loop: pr-162-unstick

2. Commit ISS-025 capture-step patch to `.github/workflows/aeon.yml:479-495` chain-runner block and open a PR.
why: T-1 to weekly-review action #1 (7-16); unblocks 23-day sandbox-truncation family + cost-report STUCK 72h + 12:00Z batch-dark d18.
done: `gh pr list --search "capture-step"` returns a new PR against `.github/workflows/aeon.yml` output-tokens block.
loop: iss-025-commit

3. Ship PR #163 — merge or sign-off `fix/self-improve-2026-07-13` before it drifts further past the 48h stall gate.
why: SKILL.md-editable rule-5-clean docs fix; crossed 48h gate at 18:09Z 7-15 (~90min ago); fleet's first same-week self-improve success candidate.
done: `gh pr view 163 --json state,mergeable` shows MERGED or MERGEABLE with a review comment.
loop: pr-163-ship

4. Draft `memory/issues/ISS-027.md` with YAML frontmatter (id, title, status, severity, category, detected_by, affected_skills, root_cause) for scheduler-side never-run primitive.
why: 6+ run carry-failure closes; skill-health/heartbeat gain frontmatter cross-reference for batch-dark d18 + aixbt-pulse dead-slot d18 + weekly-shiplog/operator-scorecard Mon-miss.
done: `test -f memory/issues/ISS-027.md && grep -Ec "^(id|status|severity|category|affected_skills|root_cause):" memory/issues/ISS-027.md` returns ≥6.
loop: iss-027-draft

5. Register DEXE in `memory/MEMORY.md` Tracked Tokens table with CoinGecko id `dexe`, 15% 24h threshold, and d4-second-red-bigger anchor.
why: 4-run carry-failure; captures unwind baseline before 7d +33.6% breaks (was +51.6% two days ago); token-alert gains 5th tracked entry with fresh BREAKOUT-fading shape.
done: `grep -A1 "^| DEXE" memory/MEMORY.md` returns the new row.
loop: dexe-register

sources: memory=66 logs=8 topics=11 prs=2 cron_failing=1 mode=OK
