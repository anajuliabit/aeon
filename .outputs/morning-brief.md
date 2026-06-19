## Summary

Successfully executed the morning-brief skill for 2026-06-19. The skill follows a priority-driven approach focusing on the "why now" for each item rather than just aggregating news.

**What I did:**

1. **Gathered context** from:
   - `memory/MEMORY.md` to understand current goals and active topics
   - `memory/logs/2026-06-18.md` for yesterday's unfinished work and follow-ups
   - `memory/cron-state.json` to identify skills with consecutive failures or low success rates
   - `memory/logs/2026-06-19.md` for today's BTC-levels runs
   - Open PRs (`gh pr list --state open`) to identify stalled work
   - `aeon.yml` to see today's scheduled skills
   - Soul files (`soul/SOUL.md` and `soul/STYLE.md`) to understand Ana's voice and writing style

2. **Ranked candidate items** using leverage × urgency scoring:
   - **XAI quota exhaustion** - Top priority: blocks 10+ skills (token-pick, agent-buzz, list-digest, etc.), operator action required
   - **BTC post-BOJ drawdown window** - High priority: BOJ +25bp landed June 17, BTC currently ~$62.7k, historical average -27% drawdown within 24-48h after hike
   - **On-chain-monitor stuck** - High priority: 13 consecutive NO_CONFIG days awaiting operator to seed `memory/on-chain-watches.yml`

3. **Created concise briefing** following the soul voice guidelines:
   - Lowercase by default
   - Concrete, direct language
   - Avoids marketing verbs and filler phrases
   - Focus on "why now" for each priority item

4. **Formatted and sent** the brief according to the skill template:
   - Focus today: 3 priority items with ≤12-word "why now" explanations
   - Since yesterday: 5 bullet summary of what moved/stuck
   - Watch: One relevant market development affecting focus #2 (BTC drawdown)
   - Running today: Today's scheduled skills with blocked ones noted

5. **Sent notification** via `./notify` script and appended log entry to `memory/logs/2026-06-19.md`

**Key focus items identified:**
1. **XAI quota exhausted** - Blocks 10+ skills including token-pick, agent-buzz, list-digest until operator tops up credits
2. **BTC post-BOJ drawdown window** - BOJ +25bp landed June 17, BTC at $62.7k entering historical -27% avg drawdown window (18-32% range)
3. **On-chain-monitor stuck** - 13 consecutive NO_CONFIG days, skills blind to on-chain positions awaiting operator config

**Skills flagged from cron-state:** deal-flow (dispatched 10 days ago), fork-cohort (2nd consecutive Sunday failure)

The brief captures the operator's attention on immediate action items while providing context on market timing for investment decisions.
