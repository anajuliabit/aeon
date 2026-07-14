*5 Actions — 2026-07-14*
Shape: decide PR #162 today, land ISS-025 PR, merge PR #163, scaffold ISS-027, add DEXE row

1. Operator decides PR #162 today — merge (if rebase clears CONFLICTING), close, or comment with concrete blocker on branch `fix/self-improve-2026-07-11`; end the ~69h no-review stall before the 72h mark at 20:16Z.
why: weekly-review action #2 T-0 deadline today; 24h stall gate crossed 7-12 20:34Z; empty reviewDecision + rule-5 workflow-file class blocks any self-improve re-authoring path.
done: `gh pr view 162 --json state,mergedAt` returns MERGED or CLOSED, or PR gains a new operator comment ≥50 chars.
loop: pr-162-decide

2. Operator direct-authors ISS-025 capture-step PR against `.github/workflows/aeon.yml:479-493` chain-runner env-indirection fix; pin the copy-paste-ready diff-spec from `articles/weekly-review-2026-07-13.md` action #1.
why: weekly-review priority-20 action, T-2 to 2026-07-16 deadline; unblocks 22-day sandbox-truncation-systemic bleed + 12:00Z 8-skill batch-dark day-17 (same rule-5 primitive).
done: `gh pr list --state open --json headRefName,files` shows a PR touching `.github/workflows/aeon.yml` chain-runner capture step against `main`.
loop: iss-025-land

3. Operator merges PR #163 (`fix/self-improve-2026-07-13`, skill-security-scan sandbox-block-as-expected-failure docs) before the 24h stall gate crosses at 18:09Z 7-14 (~3h out from 15:08Z heartbeat).
why: PR #163 is SKILL.md-editable (rule-5-clean), authored by 7-13 18:00Z self-improve tick; blocks a second workflow-file-adjacent PR from crossing the 24h stall threshold; would land the fleet's first same-week rule-5-clean self-improve ship.
done: `gh pr view 163 --json state,mergedAt` returns MERGED.
loop: pr-163-pre-stall-merge

4. Scaffold `memory/issues/ISS-027.md` with 6 YAML frontmatter fields (id=ISS-027, title, status=open, severity=high, category=sandbox-limitation, detected_by=heartbeat, affected_skills=[token-pick,defi-overview,token-movers,on-chain-monitor,defi-monitor,market-context-refresh,narrative-tracker,aixbt-pulse]) + a matching row in `memory/issues/INDEX.md` Open Issues table.
why: 6-run carry-failure — 7-07 file / 7-08 file / 7-09 create+codify / 7-12 open / 7-13 write all did not land; 8-skill batch-dark day-17 still last_success 2026-06-28; ISS-027 gap blocks skill-health frontmatter cross-reference on the batch-dark cluster.
done: `ls memory/issues/ISS-027.md` returns the file and `grep -c '^| ISS-027' memory/issues/INDEX.md` returns ≥1.
loop: iss-027-scaffold

5. Add a DEXE row to `memory/MEMORY.md` under `## Tracked Tokens` using CoinGecko id `dexe`, 15% 24h threshold, and fresh 7-14 anchor: rank #41 $46+ / 7d +51.64% intact / **d3 first breakout red print -7.5%** / watchlist-add flag holds.
why: 3-run carry-failure — 7-12 `append+DEXE-watchlist` and 7-13 `insert+DEXE-row` both failed to land; d3 first red print keeps the signal alive; next token-alert tick gains a 5th tracked entry with a fresh BREAKOUT baseline before the 7d +51.6% starts unwinding.
done: `grep -A1 '^| DEXE' memory/MEMORY.md` returns a Tracked Tokens row with `dexe` id and 15% threshold.
loop: dexe-add-row

sources: memory=60L logs=8d topics=11 prs=2 cron_failing=1 mode=OK
