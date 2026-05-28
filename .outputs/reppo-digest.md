## Summary

Executed `reppo-digest` skill for the 2nd-run-manual of the reppo-swarm chain on 2026-05-28 (datanet 9).

**Run results:** 2 on-chain (0 mints, 2 DISLIKE votes for pods 372/373).
- vote-372 — tx `0xb2400bbc17362fcd865489b51bb817464850d0b50b8a6f839dd1306ed9b53d11`
- vote-373 — tx `0x8f3130b6c5d0bbd4125e5a8b99df09daa2dd3f1662d2b404ab3f9a2151ccb281`
- 0 mints queued — structural HL `userFills` 2000-row cap collapses every top-leaderboard wallet to <1d span, below the ≥20-trade ≥7-day rubric floor.
- 0 reverts.

**Key diagnosis surfaced this run:** ISS-009 root cause traced for the first time — chain-runner's "Capture skill output" step in `.github/workflows/aeon.yml:479-493` always `cp`s Claude CLI's `.result` (final assistant text) over `.outputs/${SKILL}.md`, silently overwriting any Write-tool output. PR #24 (prompt) and PR #27 (workflow grep guard) targeted the wrong layer. Fix path: orchestrator must emit the fenced block in its final assistant text response. Validated this run end-to-end.

**Files modified:**
- `.pending-notify/1779971434-reppo-digest.md` — digest text (sandbox blocked `./notify` arg-passing; post-run delivery picks it up).
- `memory/topics/reppo.md` — appended 2 vote rows + 1 run-history row.
- `memory/issues/ISS-009.md` — corrected-diagnosis section appended; status bumped `open` → `investigating`; frontmatter root_cause + title rewritten.
- `memory/issues/INDEX.md` — title rewritten with the new diagnosis.
- `memory/logs/2026-05-28.md` — appended `### reppo-digest (2nd run, manual)` entry.

**Follow-ups for the operator (in ISS-009):**
1. Update `skills/reppo-orchestrator/SKILL.md` to mandate fenced-block-in-final-assistant-text and explicitly forbid the Write tool for this output.
2. Still apply the chain-runner.yml fail-fast `continue` → `break` fix (so the validator can hard-abort instead of silently letting downstream dispatch).
3. ISS-005 duplicate-vote risk remains open — pods 372/373 are now at 4 DISLIKE-on-chain each.
