# Obsidian Vault — Setup & Operating Model

Two-way bridge between Aeon's cloud-written `memory/` and a local Obsidian vault
on your Mac. Design rationale: `docs/superpowers/specs/2026-06-04-aeon-obsidian-vault-design.md`.

## What you see

The vault root is the **`vault/` subfolder** of the repo clone — not the repo
root. Obsidian only shows what's physically inside `vault/`, so the explorer and
graph are clean by construction (no filter, no dimming). **Visible:**

- `priorities.md`, `inbox/`, `notes/`, `reviews/`, `Home.md` — your stuff
- `topics/` — a symlink to `../memory/topics` (Aeon's research notes, read-only)

Everything else in the repo (`skills/`, `docs/`, `memory/logs/`,
`memory/issues/`, `MEMORY.md`, JSON state, CSVs) lives *above* the vault root, so
Obsidian never sees it. New Aeon directories can never leak in.

> Why not the repo root + an "Excluded files" filter? Because Obsidian's
> excluded-files setting only *de-emphasizes* files — it does **not** hide them
> from the explorer or graph. Rooting the vault at `vault/` is the only reliable
> way to get a truly clean view.

## One-time setup

1. **Clone the repo** to wherever you keep vaults:
   ```bash
   git clone https://github.com/anajuliabit/aeon.git ~/obsidian/aeon-vault
   ```
2. **Open the `vault/` subfolder in Obsidian:** *Open folder as vault* →
   `~/obsidian/aeon-vault/vault` (the subfolder — **not** the repo root).
3. **Trust + enable community plugins:** Settings → Community plugins → *Turn on*.
4. **Install Obsidian Git:** Browse → search "Obsidian Git" (by Vinzent03) →
   Install → Enable. The committed `vault/.obsidian/plugins/obsidian-git/data.json`
   sets `basePath: ".."` so the plugin operates on the parent repo even though the
   vault is a subfolder — it starts auto-syncing immediately.
5. **Reload Obsidian.** The graph and file explorer show only your notes +
   `topics/`. New notes default to `inbox/`.

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

`vault/.obsidian/workspace.json` (and `workspace-mobile.json`) record your
per-machine pane layout and change constantly. They're in `.gitignore` — leave
them there, or you'll get cross-machine conflict churn. All other
`vault/.obsidian/` files are shared config and are committed intentionally.

## Out of scope

- **Mobile.** Desktop-first; Obsidian Git on mobile is fiddly. Use Obsidian Sync
  if you need phone access.
- **Editing skills/docs in Obsidian.** They're hidden. Edit Aeon's code in your
  normal editor on a feature branch.
