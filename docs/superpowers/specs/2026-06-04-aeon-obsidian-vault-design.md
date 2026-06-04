# Aeon ↔ Obsidian Vault — Design Spec

**Date:** 2026-06-04
**Branch:** stacked on `feat/personal-stack-hermes-style` (PR #71)
**Status:** approved design, pending implementation plan

## Problem

PR #71 ("personal-stack: hermes-style capture + priority-anchored review")
deliberately punted on real Obsidian sync, with the note: *"No actual Obsidian
sync — `memory/` is already a markdown vault. Open it in Obsidian locally if you
want."*

That note is wrong in practice. When the repo (or all of `memory/`) is opened as
an Obsidian vault, the graph is dominated by hundreds of disconnected
operational-markdown nodes: every `skills/*/SKILL.md`, every `docs/` file, and
especially every `memory/logs/YYYY-MM-DD.md` daily ops log (each an orphan with
no links). The operator's actual personal knowledge — priorities, captures,
reviews — is buried.

This spec defines the real bridge between Aeon's cloud-written `memory/` and a
local Obsidian vault, with a curated view that shows **only** the operator's
personal notes plus Aeon's research topics.

## Decisions (from brainstorming)

| Decision | Choice |
|---|---|
| Direction | **Two-way** — Aeon writes → Obsidian; operator edits → flow back to Aeon |
| Vault contents | **Operator notes + Aeon research topics** (`memory/topics/`); everything else hidden |
| Approach | **A — repo-as-vault + shipped `.obsidian/` config** (no new infra) |
| Relation to #71 | **Stacked on `feat/personal-stack-hermes-style`** |

## Architecture

**Transport = git.** Aeon runs in GitHub Actions (cloud); the vault is a local
clone on the operator's Mac. The Obsidian Git community plugin is the only clean
two-way transport for a cloud agent:

- **Cloud → local:** GitHub Actions commits to `main` → Obsidian Git auto-pulls
  (~10 min) → notes update locally.
- **Local → cloud:** operator edits/creates in Obsidian → Obsidian Git
  auto-commits + pushes (~10 min, or manual hotkey) → lands on the branch →
  Aeon reads it on its next run.

**Vault root = repo root** so the Obsidian Git plugin sees the git root cleanly.
The **view** is curated by Obsidian's own `userIgnoreFilters`, not by any custom
sync pipeline.

### Curated view — allow-list via regex

Obsidian `userIgnoreFilters` accepts regex entries (wrapped in `/.../`). Instead
of a fragile exclude-list that must be updated as the repo grows, use a single
negative-lookahead regex that hides everything **not** under the allowed prefixes:

```
/^(?!(vault|memory\/topics)\/)/
```

Obsidian tests each vault-relative path (e.g. `memory/logs/2026-06-04.md`)
against this. Any path not starting with `vault/` or `memory/topics/` matches the
ignore filter and is removed from file-explorer, search, graph, and quick-switch.
New Aeon directories are auto-excluded — no maintenance.

### Visible surface

| Path | Source | Role |
|---|---|---|
| `vault/priorities.md` | moved from `memory/priorities.md` (#71) | the anchor — operator-owned life priorities |
| `vault/Home.md` | new | map-of-content hub linking the vault |
| `vault/inbox/` | new | frictionless captures (default new-note location) |
| `vault/notes/` | new | operator free-form notes |
| `vault/reviews/` | new | `thought-review` writes priority-anchored output here |
| `memory/topics/` | existing Aeon | research notes (crypto/research/projects), read-only reading |

Everything else — `skills/`, `docs/`, `memory/logs/`, `memory/issues/`,
`memory/MEMORY.md`, all `*.json` state, CSVs, seen-files — is hidden.

## Components

### 1. `vault/` folder structure

```
vault/
  Home.md            # MOC: links priorities, inbox, reviews, notes, topics
  priorities.md      # moved from memory/priorities.md
  inbox/.gitkeep
  notes/.gitkeep
  reviews/.gitkeep
```

`priorities.md` moves from `memory/priorities.md` → `vault/priorities.md`. This
is safe because #71 is unmerged; the only reader is `thought-review` (updated in
component 4). No other code references `memory/priorities.md`.

### 2. `.obsidian/` config (committed to repo)

- **`.obsidian/app.json`** —
  - `userIgnoreFilters`: `["/^(?!(vault|memory\\/topics)\\/)/"]`
  - `newFileLocation`: `"folder"`
  - `newFileFolderPath`: `"vault/inbox"`
  - `attachmentFolderPath`: `"vault/inbox/attachments"`
  - `alwaysUpdateLinks`: `true`
- **`.obsidian/core-plugins.json`** — enable `graph`, `backlink`,
  `outgoing-link`, `tag-pane`, `command-palette`, `switcher` (sane defaults).
- **`.obsidian/community-plugins.json`** — `["obsidian-git"]` (enables it once
  the operator installs the plugin binary).
- **`.obsidian/plugins/obsidian-git/data.json`** — pre-configured:
  - `autoSaveInterval`: `10` (auto-commit every 10 min)
  - `autoPushInterval`: `10`
  - `autoPullInterval`: `10`
  - `autoPullOnBoot`: `true`
  - `pullBeforePush`: `true`
  - `commitMessage`: `"vault: {{date}}"`
  - `disablePopups`: `false` (so merge conflicts surface)

Note: Obsidian does **not** auto-install community plugin binaries from committed
config (by design, for security). The operator installs "Obsidian Git" once; the
committed config then enables and configures it.

**Version-verification (required at implementation).** The `obsidian-git`
`data.json` key names and the exact `userIgnoreFilters` regex-escaping vary across
plugin/app major versions — a stale key silently does nothing (no error). The
implementation plan MUST verify both against the operator's installed versions
before shipping the config: dump a real `.obsidian/plugins/obsidian-git/data.json`
from the operator's Obsidian, diff key names, and confirm the regex filter
actually hides the intended paths in the live graph. Do not assume the field
names above are correct verbatim.

### 3. `.gitignore` (append)

```
# Obsidian per-machine UI state — must not be committed (cross-machine churn)
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/workspace.json.bak
```

**Critical.** `workspace.json` records the open-pane layout and changes on every
focus event. Committing it produces a conflict storm across machines. Everything
else under `.obsidian/` is shared config and **is** committed.

### 4. `skills/thought-review/SKILL.md` (modify #71's skill)

- Read the anchor from `vault/priorities.md` (was `memory/priorities.md`).
- Scan captures from **both** `vault/inbox/*.md` **and** the existing
  `memory/logs/${today}.md` capture blocks (Telegram path from #71 still writes
  to logs).
- Write the priority-anchored review to `vault/reviews/${today}-review.md`
  (was: a `### Thought Review` block in the ops log). Still append a one-line
  pointer + the notification summary to `memory/logs/${today}.md` for the ops
  trail.

### 5. `docs/obsidian-vault.md` (new)

One-time setup guide + operating model:
- Clone, "Open folder as vault", enable community plugins, install Obsidian Git.
- How two-way sync behaves (intervals, manual push hotkey).
- Conflict handling (see below).
- The capture loop: type in Obsidian → `vault/inbox/` → push → `thought-review`.

### 6. `docs/personal-stack.md` (modify #71's doc)

Replace the "No actual Obsidian sync" paragraph with a pointer to
`docs/obsidian-vault.md` and the `vault/` model.

## Data flow

```
Aeon (GH Actions) --commit--> main --Obsidian Git auto-pull--> local vault (Obsidian)
local vault edit --Obsidian Git auto-commit+push--> main --Aeon next run reads--> Aeon
```

Both sides commit to the same branch. The files Aeon churns frequently
(`cron-state.json`, logs) are hidden from the Obsidian view but still pulled in
git — this only means frequent, clean pulls.

## Conflict handling

Conflict risk is low by design:
- #71 makes Aeon treat `priorities.md` and operator notes as operator-owned — it
  does not auto-edit them.
- The files Aeon writes (`cron-state`, logs, topics) are disjoint from the files
  the operator edits (`vault/priorities.md`, `vault/notes/`, `vault/inbox/`).
- `thought-review` writes to `vault/reviews/${today}-review.md` (date-stamped,
  no operator contention).

Obsidian Git does pull-before-push with merge. Genuine same-file conflicts
surface in the plugin for manual resolution. The setup doc tells the operator to
keep their edits to operator-owned files; if a conflict appears, resolve it in
Obsidian Git's conflict view.

## Edge cases

- **`workspace.json` churn** — handled by `.gitignore` (component 3).
- **High Aeon commit frequency** — vault pulls many hidden machine-state commits;
  acceptable, view stays clean.
- **Multiple machines** — git handles it; `workspace.json` gitignored prevents
  cross-machine UI churn.
- **Mobile** — out of scope. Desktop-first; Obsidian-Git-on-mobile is fiddly.
- **Secret exposure** — none new. The vault is the same repo at the same trust
  boundary; no content is sent anywhere it wasn't already.

## Acceptance criteria

1. Open the repo clone in Obsidian → graph and file explorer show **only**
   `vault/` contents + `memory/topics/`. No `skills/`, `docs/`, `memory/logs/`,
   `memory/issues/`, JSON, or CSV nodes.
2. Edit `vault/priorities.md` in Obsidian → within ~10 min (or manual push) the
   change is on the branch.
3. A run that writes to `memory/topics/` → Obsidian auto-pulls → the topic note
   updates locally.
4. Drop a `.md` in `vault/inbox/` → next `thought-review` reads it and writes
   `vault/reviews/${today}-review.md`.
5. `vault/Home.md` opens as a hub with working links to priorities, inbox,
   reviews, notes, and topics.

## Out of scope (YAGNI)

- Dedicated vault repo / sync workflow (Approach B) — rejected for infra cost.
- Sparse-checkout (Approach C) — fights Obsidian Git on two-way commits.
- Mobile sync.
- Auto-editing `priorities.md` from Aeon — operator owns it.
- Migrating existing `memory/logs` history into the vault — logs stay ops-side.

## Operator one-time setup (cannot be automated from the repo)

1. `git clone <repo>` to the desired vault location.
2. Obsidian → "Open folder as vault" → the clone.
3. Settings → Community plugins → enable → install **Obsidian Git**.
4. Reload. The committed config applies the filter, new-note location, and
   Obsidian Git intervals automatically.
