## Summary

Executed the **reppo-digest** skill for the 2026-05-29 1st run of the reppo-swarm chain.

**Digest sent** — staged at `.pending-notify/1748477700.md` (sandbox blocks `./notify "$(cat …)"` arg-passing per the documented pattern; post-run step delivers). Header: `reppo-swarm · 1st run · datanet 9 · 4 on-chain`. Sections: `queued`, `on-chain`, `reverted` with one-line `action:` per revert, trailing `14 datanets unassigned.` All lowercase per `soul/STYLE.md`.

**Ledger updated** at `memory/topics/reppo.md`:
- 1 mint row — hash `9794ed8044e6e7ea` (LIT perp, 2000 closes, sharpe 19515, tx `0xca4b0a63…`, 5th mint ever).
- 2 vote rows — pod 332 dislike (tx `0xd0ec80b6…`), pod 390 dislike (tx `0x2d6cf782…`). vote-391 deliberately omitted (REVERT).
- 1 run-history row — 1 mint / 2 votes / 3 failures, full narrative.

**3 distinct failures filed** (checked INDEX.md, none matched existing open issues):
- **ISS-011** (medium, unknown) — vote-391 REVERT nonce-too-low after siblings 332/390 landed in same batch.
- **ISS-012** (medium, api-change) — Phase 2 metadata POST HTTP 400 for queued mint 397ee2e8.
- **ISS-013** (medium, missing-secret) — Phase 2 IPFS pin HTTP 403 (Pinata JWT) for mint 9794ed80.

Indexed all three in `memory/issues/INDEX.md` Open table.

**Run logged** under `### reppo-digest` in `memory/logs/2026-05-29.md`.

**Files modified**: `memory/topics/reppo.md`, `memory/issues/INDEX.md`, `memory/logs/2026-05-29.md`, `.pending-notify/1748477700.md`, `memory/issues/ISS-011.md` (new), `memory/issues/ISS-012.md` (new), `memory/issues/ISS-013.md` (new).

**Follow-ups for the operator**: rotate or set `PINATA_JWT` (ISS-013, blocks every future mint's IPFS pin); diff `postprocess-reppo.sh` payload vs current Reppo `/pods` schema (ISS-012); watch next run for nonce-too-low recurrence to decide if ISS-011 needs a postprocess-side retry.
