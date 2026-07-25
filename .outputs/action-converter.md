*5 Actions — 2026-07-25*
Shape: aeon-runtime CVE verify · ISS-027 d18 file · patch-week deps grep · ISS-028 file · github-issues SKILL patch

1. verify `claude --version` is ≥ 2.1.163 on any 2026-07-25 CI run log — CVE-2026-55607 `@anthropic-ai/claude-code` sandbox-escape hits aeon-runtime directly
why: RCE via git-worktree path confusion on the fleet's own CLI; auto-patched via unpinned `npm install -g` per aeon.yml but unconfirmed
done: grep any today's actions-run job log for "claude --version" line ≥ 2.1.163 (or `.github/workflows/aeon.yml` install step output)
loop: ai-framework-attack-surface-aeon-runtime-cve-2026-55607

2. file `memory/issues/ISS-027.md` for 12:00 UTC batch-DARK per-skill blockage n=28 durable since 2026-06-28
why: MEMORY.md line 6 references ISS-027 as if it exists = load-bearing doc-gap d18, blocks any resolve/wontfix reasoning
done: `memory/issues/ISS-027.md` exists with YAML frontmatter (id/title/status=open/severity=high/category=sandbox-limitation/affected_skills=[defi-overview,token-pick,token-movers,narrative-tracker,market-context-refresh,fleet-control,on-chain-monitor,defi-monitor,aixbt-pulse]) + row appended to `memory/issues/INDEX.md` open table
loop: iss-027-batch-dark-file-carry-d18

3. grep `scripts/ apps/ package.json .github/workflows/` for `velocityjs|@prompty/core|^ray$|GitPython|@fastify/static` — verify none of today's PATCH-THIS-WEEK deps reach aeon-runtime
why: security-digest 14Z surfaced 5 fresh RCEs (velocityjs 9.8 · @prompty/core 10.0 · ray 8.8 pickle · GitPython 5-CVE · @fastify/static 7.5) across npm+pip
done: `grep -rEn 'velocityjs|@prompty/core|ray|GitPython|@fastify/static' scripts/ apps/ package.json .github/` output empty (expected) or triaged
loop: security-digest-patch-this-week-grep-verify

4. file `memory/issues/ISS-028.md` for bash-`>`-redirect sandbox regression n=7+ same-family across 3 UTC-day span
why: workaround chain (curl `-o` / Write / Read+Edit) durable but reflect itself hit it 7-24 mid-run = ISS-file threshold firmly crossed
done: `memory/issues/ISS-028.md` exists with root-cause + validated-workaround chain + affected_skills [security-digest, agent-buzz, daily-routine, github-trending, reflect] + row in INDEX
loop: bash-redirect-regression-iss-028-file-carry-d2

5. apply `comments` → `commentsCount` field rename in `skills/github-issues/SKILL.md` step 2 `gh search issues` query
why: gh API field renamed; d3 carry from morning-brief 7-23 flag surfaced in daily-routine issue-fetch stubs
done: `skills/github-issues/SKILL.md` step 2 uses `--json ...,commentsCount,...` (git diff shows single-line rename)
loop: github-issues-skill-md-field-rename-carry-d3

sources: memory=67 logs=7 topics=8 prs=2 cron_failing=0 mode=OK
