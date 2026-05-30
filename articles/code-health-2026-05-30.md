# Code Health Report — 2026-05-30

watched repo: `aaronjmars/aeon` (1 of 1). audited at HEAD 011dee9.

scope: ts/tsx/js/jsx/py/sh code + skill prompts under `skills/`. 8,020 lines of
executable source across ~50 files; 35,421 lines of skill markdown across 172
skill dirs. this is a prompt-dominated repo, so "coverage" reads differently
than a normal codebase.

---

## aaronjmars/aeon

### TODOs (1 actionable, 40 false positives)

real:

- `skills/workflow-security-audit/SKILL.md:36` — `# TODO: bump ZIZMOR_VERSION
  to the latest stable on the next audit of this skill.` Pinned at `1.24.1` on
  line 29. one-line bump on next workflow-security-audit run.

the other 40 grep hits are false positives — pattern strings inside skills that
*scan for* TODO/FIXME (`skill-evals/evals.json`, `skill-health/tests/smoke.sh`,
`repo-actions/SKILL.md`, `create-skill/SKILL.md`, etc.). all expected.

### Large files

one file over 500 lines:

- `a2a-server/src/index.ts` — 578 lines. cohesive (A2A protocol server, single
  responsibility), but borderline. natural seam: types + JSON-RPC handlers
  could move to siblings if it grows past ~700.

every other code file is <340 lines. dashboard components and lib helpers are
appropriately small.

### Test coverage gaps

executable tests in the repo:

- `dashboard/lib/security/api-gate.test.ts` — 188 lines, the only real unit
  test file. covers the auth/permission boundary, which is the right place
  to invest first.
- `skills/skill-health/tests/smoke.sh` — 321 lines, sanity-checks skill
  scaffolding (frontmatter, placeholder strings, etc.).
- `examples/mcp/test_connection.py` — example-only, not a real test.

gaps:

- no `"test"` script in any of the three `package.json` files
  (`dashboard/`, `a2a-server/`, `mcp-server/`). meaning even the api-gate test
  isn't wired to `npm test` — has to run via the framework directly.
- `dashboard/lib/` has 9 helper modules (`memory.ts`, `github.ts`,
  `config.ts`, `frontmatter.ts`, `gh.ts`, …) and the JSON parsing /
  YAML-frontmatter paths are untested.
- `dashboard/app/api/` has 13 route handlers — including `secrets/`,
  `upload/`, `auth/`, `analytics/` — none of them have route-level tests.
  the security-relevant ones (secrets, upload, auth) are the highest-value
  targets.
- `a2a-server/src/index.ts` (578-line protocol server) has zero tests.
  JSON-RPC handlers without tests are a known footgun.
- `mcp-server/src/index.ts` — same shape, zero tests.

caveat: the 172 skills under `skills/` aren't tested by unit tests by design —
the real "test suite" for skills is `skill-evals` + `skill-health` smoke +
`heartbeat`. that pattern is intentional and not a gap.

### Hardcoded secrets

clean. no `sk-*`, `ghp_*`, `xoxb-*`, `AIza*`, `AKIA*` patterns. no quoted
20+-char strings on `api_key|secret|token|password|bearer` keys. all auth
flows through env vars.

### Dead code indicators

- ~124 inline comments across 20 TS/JS files — normal density, no
  commented-out code blocks found.
- `console.log` count: 9 across 4 files (`add-a2a`, `add-mcp`, plus 2 skill
  prompts referencing the pattern). all in CLI scaffolding scripts where
  stdout *is* the contract. not noise.
- no `debugger` statements. no `debug: true` literals.

### Concerns

- **route-level + a2a-server tests are the real gap.** the codebase's security
  surface (secrets endpoint, upload endpoint, JSON-RPC server) is in code that
  has zero unit tests today. one solid api-gate test isn't enough scaffolding
  to catch regressions on the rest.
- **no `npm test` entry points.** even the test that does exist is
  off-the-rails. CI almost certainly isn't running it.
- **`a2a-server/src/index.ts`** is the next file to watch — 578 lines today,
  adding any new RPC method will push it past 600 fast.

### Recommendations

1. add `"test": "tsc --noEmit && next test"` (or vitest/jest equivalent) to
   `dashboard/package.json` and wire it into CI. without an entry point, the
   one existing test rots.
2. write route-handler tests for the three security-sensitive routes first:
   `app/api/secrets/route.ts`, `app/api/upload/route.ts`, `app/api/auth/route.ts`.
   model after the existing `api-gate.test.ts` pattern.
3. add a minimal JSON-RPC test harness to `a2a-server/` — at least
   `tasks/send`, `tasks/get`, `tasks/cancel` happy-path + one malformed-input
   case each. the protocol surface is the bug-trap.
4. bump `ZIZMOR_VERSION` in `skills/workflow-security-audit/SKILL.md` next
   time that skill runs (the TODO is right there waiting).
5. set a soft 500-line ceiling and revisit `a2a-server/src/index.ts` on the
   next added RPC method — split types + handlers into siblings then, not
   speculatively now.
