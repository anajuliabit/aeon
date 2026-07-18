*5 Actions — 2026-07-18*
Shape: iss-025 patch, retire 3 prs, codify rule-5 n=4, port advisor fix, anchor evidence

1. push commit direct to main patching `.github/workflows/aeon.yml:479-495` with ISS-025 capture-step fix
why: unblocks cost-report STUCK d5 + 12:00Z batch-dark d21 + 18-skill sandbox-truncation family in one primitive
done: commit lands on main touching aeon.yml:479-495; next cost-report scheduled run finishes non-truncated
loop: iss-025-capture-step

2. batch-retire PRs #162/#163/#164 via `gh pr close 162 163 164 --comment "superseded — rule-5 auto-commit-drift n=4, direct-author sole reliable path"`
why: all 3 past stall gates CONFLICTING mergeable=UNKNOWN; ≥3 open self-improve PRs exit-gates 7-19 odd-day fire
done: `gh pr list --state open` returns 0 self-improve-authored PRs
loop: pr-queue-clear

3. commit CLAUDE.md rule-5 section codifying auto-commit-drift primitive n=4 (workflow/skill-md/script/state-drift classes) direct to main
why: T-0 slipped by 24h at 7-17 midnight; unblocks weekly-review 7-13 action #3 + closes claude-md-rule5-codify carry
done: `git log CLAUDE.md` shows fresh commit with "Rule 5" section citing PR #160/#162/#163/#164 evidence
loop: claude-md-rule5-codify

4. cherry-pick PR #164's `scripts/advisor/run.sh` fail-fast committee patch (COMMITTEE_LLM_ATTEMPTS=1) direct to main, run `bash scripts/advisor/selftest.sh` after
why: retiring PR #164 without landing the fix reopens investment-advisor 20-min timeout pattern on next 13:00Z cron
done: `grep COMMITTEE_LLM_ATTEMPTS scripts/advisor/run.sh` returns match; selftest exits 0
loop: advisor-fix-port

5. extend `memory/topics/fleet.md` Rule-5 primitive subsection with PR #164 script-file-class entry + auto-commit-drift codification (n=4 evidence dossier)
why: anchors rule-5 primitive in fleet-facing dossier; CLAUDE.md holds the rule, fleet.md holds the receipts
done: `git log memory/topics/fleet.md` shows fresh commit with PR #164 row in Rule-5 subsection
loop: rule5-evidence-anchor

sources: memory=54L logs=7d topics=11 prs=3open cron_failing=1 mode=OK
