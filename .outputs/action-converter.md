*5 Actions — 2026-07-02*
Shape: scope ISS-025 fix pre-07-04, nudge PR #149, refresh stale MEMORY, close VELVET, add on-chain pool entries

1. scope the ISS-025 capture-step fix in memory/issues/ISS-025.md — root cause + aeon.yml diff + smoke-test target; commit before weekly-review 2026-07-04 T-2d
why: 19-skill chronic tail bleeds output_tokens=0 day 14; weekly-review hard deadline is 2d out
done: memory/issues/ISS-025.md has "Fix plan" section with named skill + concrete config diff
loop: iss025

2. post a comment on PR #149 tagging @anajuliabit — merge or close, 5-line docs diff, day-3.9 stall
why: same author batch-merged #150+#151 at 13:20Z today, docs PR still open + operator active
done: comment visible on `gh pr view 149 --comments`
loop: pr149

3. rewrite memory/MEMORY.md Current Goals — PR #150/#151 both merged 13:20Z, sandbox-truncation day 14, BTC breakdown day 7 confirmed, 07-02 relief bounce added
why: MEMORY still says "PR #150 44h stall day 8" — 6 lines behind reality after today's merges
done: git diff shows updated Current Goals block, "last consolidated: 2026-07-02"
loop: memory-refresh

4. flag VELVET pick invalidated in memory/topics/crypto.md — HIGH 11/10 blown −68.5% ($1.97 → $0.62), note July-10 unlock priced 8d early
why: pick tracker still lists VELVET active; today's −60.1% single-day full unwind
done: crypto.md has "VELVET closed 2026-07-02 —68.5%" line + 3-bullet post-mortem
loop: velvet-cleanup

5. add 2 type:pool + 1 type:position entries to memory/on-chain-watches.yml (Morpho cbBTC market + REPPO/MAMO vaults once ID'd) — file's own header says "add once confirmed on-chain"
why: defi-monitor NO_CONFIG day 25; entries stage the exit as soon as operator lands ALCHEMY_API_KEY
done: memory/on-chain-watches.yml adds ≥3 new watches passing yaml lint
loop: onchain-config

sources: memory=42 logs=7 topics=17 prs=1 cron_failing=1 mode=OK
