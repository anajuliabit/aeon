## Summary

The skill aborted at step 1 (var parse). The supplied variable `var=sherwood.sh` is neither empty nor `dry-run` — the only two values the skill accepts. Per the skill's own rule, anything else triggers an immediate `BAD_VAR` exit.

**Outcome:**
- No Product Hunt / HN fetch
- No article written
- No state mutation (`memory/topics/competitor-launch-radar-state.json` untouched)
- No notification sent
- Log entry appended to `memory/logs/2026-05-21.md`

**Files modified:** `memory/logs/2026-05-21.md` (one log block recording the aborted run)

**Follow-up:** Re-run with `var=` (empty, for a normal run) or `var=dry-run` (full run, no notify) to get an actual radar scan.

Status: COMPETITOR_LAUNCH_RADAR_BAD_VAR
