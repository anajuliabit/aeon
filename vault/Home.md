# Home

Your vault — your knowledge surface. Everything here is yours, or written *for*
you by Aeon's `thought-review`. Aeon's operational files (logs, issues, skills,
docs, state) are hidden from this vault by design.

## Anchor

- [[priorities]] — life priorities, current focus, out-of-scope. Aeon reads
  this to triage your captures; **you own it** (Aeon never edits it).

## Capture

- **Inbox** → drop quick thoughts as notes in `vault/inbox/` (new notes land
  here by default). `thought-review` reads them.
- **Notes** → `vault/notes/` for your free-form writing.

## Review

- `vault/reviews/` — `thought-review` writes priority-anchored reviews here
  (`YYYY-MM-DD-review.md`), surfacing what aligned, what drifted, what to act on.

## Reading (Aeon-curated)

- `memory/topics/` — Aeon's research notes (crypto, research, projects).
  Read-only reading material, surfaced here on purpose.

## How sync works

Two-way via git + the **Obsidian Git** plugin: Aeon writes → auto-pulls here
(~10 min); you edit → auto-commit + push (~10 min) → Aeon reads on its next run.
Full setup and conflict handling live in `docs/obsidian-vault.md` (hidden from
this vault — open it on GitHub or in your code editor).
