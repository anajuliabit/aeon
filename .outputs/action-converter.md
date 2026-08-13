*5 Actions — 2026-08-13*
Shape: file iss-032, ship usepod-402 gate, land 2 self-improve PRs, add switchyard watched-repo

1. write memory/issues/ISS-032.md with YAML frontmatter + root-cause on state-update-race + fix-target, then add INDEX Open row for fork-cohort workflow-race
why: 7th+ owed cycle since 8-11 18:40Z; 8-12 file+ISS-032 action never landed; fork-cohort ~120h stuck, run 31330721650 cancelled with dispatched marker never cleared
done: memory/issues/ISS-032.md exists, INDEX.md Open row added, commit pushed to main
loop: fork-cohort-stuck-120h

2. wire scripts/detect-usepod-402.sh operator-page gate before 20Z heartbeat
why: 8-13 today is final workday deadline per ISS-031; stopgap for 2nd 7d-recurrence signature that crossed one-off→pattern 8-10
done: script exists + executable, wired into prefetch path or workflow step, commit on main
loop: iss-031-detect-usepod-gate

3. patch skills/skill-health/SKILL.md step 2 rule table with stuck-in-flight branch (status='dispatched' AND days_since_last_dispatch >= 3)
why: today's 18Z self-improve window is the natural slot; classification-rule-gap surfaced by 8-12 skill-health run — fork-cohort classifies HEALTHY under current rules despite ~120h stuck
done: PR opened against main with the rule-table edit
loop: fork-cohort-workflow-audit

4. bake CFTC HTML-fallback into skills/reg-monitor/SKILL.md step 1C
why: 2-consec CFTC RSS 404 observation (8-05 + 8-12) crosses self-improve threshold; removes runtime pivot from every future wed cycle; second baked-fix ready for 18Z window
done: PR opened with SKILL.md edit + HTML-parser fallback URL wired
loop: reg-monitor-cftc-rss-404-durable

5. add NVIDIA-NeMo/Switchyard to memory/watched-repos.md
why: today's github-trending top pick (37× baseline) is first fleet-visible vendor-tier LLM router — mandate-portability primitive for anthropic-anchored fleet
done: memory/watched-repos.md carries the new line, commit pushed
loop: track-vendor-tier-llm-router

sources: memory=90 logs=7d topics=20 prs=4 cron_failing=3 mode=OK
