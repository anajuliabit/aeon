heartbeat 20z — fork-cohort STUCK

fork-cohort dispatched 19:05z (sunday-weekly), workflow cancelled 19:35z at 30-min timeout, cron-state still shows `dispatched` at 20:14z (>45min stuck threshold). first fork-cohort stall of memory-window (last success 8-02). state-update race — "Update cron state" step ran on the cancelled workflow but didn't clear the dispatched marker.

otherwise clean: chronic-cohort 10-skill composition unchanged 12-consec-tick, all skills consec=0, pr queue 1→3 via sunday scheduled churn (#176 skill-graph + #177 self-improve claude-md fix).
