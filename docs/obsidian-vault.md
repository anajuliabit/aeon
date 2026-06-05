# Obsidian Vault — Setup & Operating Model

Two-way bridge between Aeon's cloud-written `memory/` and a local Obsidian vault
on your Mac. Design rationale: `docs/superpowers/specs/2026-06-04-aeon-obsidian-vault-design.md`.

## What you see vs. what's hidden

The repo is the vault, but Obsidian's view is curated by one allow-list filter
(`.obsidian/app.json` → `userIgnoreFilters`). **Visible:**

- `vault/` — your stuff: `priorities.md`, `inbox/`, `notes/`, `reviews/`, `Home.md`
- `memory/topics/` — Aeon's research notes (read-only reading)

**Hidden:** everything else — `skills/`, `docs/`, `memory/logs/`, `memory/issues/`,
`memory/MEMORY.md`, all `*.json` state, CSVs. New Aeon directories are auto-hidden
(the filter is a negative lookahead, not an exclude list).

## One-time setup

1. **Clone the repo** to wherever you keep vaults:
   ```bash
   git clone https://github.com/anajuliabit/aeon.git ~/obsidian/aeon-vault
   ```
2. **Open it in Obsidian:** Obsidian → *Open folder as vault* → pick the clone.
3. **Trust + enable community plugins:** Settings → Community plugins → *Turn on*.
4. **Install Obsidian Git:** Browse → search "Obsidian Git" (by Vinzent03) →
   Install → Enable. The committed `.obsidian/plugins/obsidian-git/data.json`
   already holds the sync settings, so it starts auto-syncing immediately.
5. **Reload Obsidian.** The graph and file explorer now show only `vault/` and
   `memory/topics/`. New notes default to `vault/inbox/`.

## How sync behaves

| Direction | Mechanism | Cadence |
|---|---|---|
| Aeon → you | Obsidian Git auto-pull | every 10 min + on app boot |
| You → Aeon | Obsidian Git commit-and-sync (commit + push) | every 10 min |

`pullBeforePush` is on, so your pushes rebase cleanly on top of Aeon's commits.
To push immediately instead of waiting, run the command palette →
*Obsidian Git: Commit-and-sync*.

## The capture loop

1. A thought hits → new note in `vault/inbox/` (or type into the daily note).
2. Obsidian Git pushes it within ~10 min.
3. `thought-review` (07:00 + 21:00 UTC) reads `vault/inbox/` + the day's log
   captures, scores them against `vault/priorities.md`, and writes
   `vault/reviews/YYYY-MM-DD-review.md` — which syncs back to you.

Edit `vault/priorities.md` whenever your focus shifts; Aeon picks it up next run.

## Conflict handling

Conflicts are rare by design: Aeon never edits `vault/priorities.md` or your
notes, and the files it does churn (`cron-state.json`, logs, topics) are disjoint
from what you edit. If Obsidian Git ever reports a merge conflict:

- Open the conflicted file; resolve the `<<<<<<<` / `>>>>>>>` markers in Obsidian.
- Run *Obsidian Git: Commit-and-sync* to finish the merge.

Keep your edits to operator-owned files (`vault/`) and you'll effectively never
hit one.

## Don't commit `workspace.json`

`.obsidian/workspace.json` (and `workspace-mobile.json`) record your per-machine
pane layout and change constantly. They're in `.gitignore` — leave them there, or
you'll get cross-machine conflict churn. All other `.obsidian/` files are shared
config and are committed intentionally.

## Out of scope

- **Mobile.** Desktop-first; Obsidian Git on mobile is fiddly. Use Obsidian Sync
  if you need phone access.
- **Editing skills/docs in Obsidian.** They're hidden. Edit Aeon's code in your
  normal editor on a feature branch.
