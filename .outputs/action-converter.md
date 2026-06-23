*5 Actions — 2026-06-23*
Shape: root-cause ISS-025, stage NEWT pre-cliff short, kill EIGEN pick, seed defi pools, refresh skill-analytics

1. open probe PR against ISS-025 — instrument cost-report output_tokens=0 path on the claude-sonnet-4-6 dispatch leg
why: cf=23 today (was 17 last night), same signature as ISS-019/020/021/022/024 — 22 skills sr<0.5 roll up here
done: branch iss-025-probe pushed, PR linked from memory/issues/ISS-025.md, instruments at least one failing leg
loop: iss-025-rootcause

2. stage NEWT pre-cliff short to .pending-picks/2026-06-23-newt-short.json
why: 139.58M tokens = 64.9% circ supply unlock 6-24, $11M mcap roughly doubles tomorrow per unlock-monitor
done: pick json on disk with side=short / entry / invalidation, postprocess-picks.sh picks it up next run
loop: newt-unlock-cliff

3. kill .pending-picks/2026-06-22-token-pick.json EIGEN — invalidation tripped
why: 13:12Z -17% leg puts spot ~$0.253, under the $0.26 invalidation rail set at yesterday's $0.305 entry
done: pick file marked status:invalidated, exit recorded in memory/logs/2026-06-23.md
loop: eigen-pick-reversal

4. populate type:pool entries in memory/on-chain-watches.yml — Aave V3 USDC Base + Aerodrome USDC-AERO LP + Moonwell WELL market
why: defi-monitor 16 days NO_CONFIG, only type:wallet entries exist, blocks contract-state queries entirely
done: yml has ≥3 type:pool blocks with abi field, defi-monitor exits OK on next cron tick
loop: defi-monitor-config

5. trigger skill-analytics via gh workflow run aeon.yml -f skill=skill-analytics
why: articles/skill-analytics-*.md at 312h/13d, operator-scorecard FRESHNESS_WARN clock 42/168h, escalates 2026-06-28
done: fresh articles/skill-analytics-2026-06-23.md written, skill-freshness fingerprint flips
loop: skill-analytics-stale

sources: memory=60 lines logs=7 days topics=11 files prs=0 cron_failing=1 mode=OK
