*Security Digest — 2026-07-25*
Verdict: 3 to patch today (aeon-runtime hit included), 5 this week, 3 to monitor. _Sources: KEV, GH Advisory, EPSS._

*PATCH TODAY*
- [CVE-2026-55607](https://github.com/advisories/GHSA-7835-87q9-rgvv) — `@anthropic-ai/claude-code` (npm) · sandbox escape via git worktree path confusion · CVSS n/a · EPSS 0.006 · **aeon-runtime direct hit**
  Fix 2.1.163. `.github/workflows/aeon.yml` `npm install -g @anthropic-ai/claude-code` auto-pulls latest (2.1.181+ per MEMORY 7-21) = already patched. Verify `claude --version` next run ≥ 2.1.163.
- [CVE-2026-59940](https://github.com/advisories/GHSA-mv8w-475r-vwqw) — `seroval` (npm) · CVSS 9.8 · EPSS n/a · Promise-resolver type confusion → RCE on `fromJSON()`
  → upgrade seroval to ≥1.5.3 today. React RSC transitive dep; check `npm ls seroval`.
- [GHSA-4xc7-2jx9-rp5j](https://github.com/advisories/GHSA-4xc7-2jx9-rp5j) — `app-node-layer` + `app-data-{layer,lts,ist}` npm-malware 4-pack · fresh 7-24 17:20Z
  Targeted `app-*` scope typosquat. → uninstall + grep CI logs for accidental installs; rotate any creds exposed.

*PATCH THIS WEEK*
- [GHSA-7gfh-x38p-prh3](https://github.com/advisories/GHSA-7gfh-x38p-prh3) — `velocityjs` (npm) · CVSS 9.8 · RCE via property-read to Function constructor — **bypass of GHSA-j658-c2gf-x6pq fix**
  → schedule upgrade velocityjs to ≥2.1.7.
- [GHSA-w28w-gp39-m4p6](https://github.com/advisories/GHSA-w28w-gp39-m4p6) — `@prompty/core` (npm) · CVSS 10.0 · Nunjucks SSTI → RCE
  → schedule upgrade @prompty/core to ≥0.1.5 (or ≥2.0.0-beta.5).
- [CVE-2026-57516](https://github.com/advisories/GHSA-hhrp-gw25-jr43) — `ray` (pip) · CVSS 8.8 · `ray.data.read_webdataset` default decoder → `pickle.loads` + `torch.load(weights_only=False)` RCE
  → schedule upgrade ray to ≥2.56.0.
- **GitPython 5-CVE mass-disclose** (pip) · [r9mr](https://github.com/advisories/GHSA-r9mr-m37c-5fr3) 8.8 config-inject RCE + [6p8h](https://github.com/advisories/GHSA-6p8h-3wgx-97gf) clone-template RCE + [fjr4](https://github.com/advisories/GHSA-fjr4-x663-mwxc) 8.1 arb file overwrite + [3rp5](https://github.com/advisories/GHSA-3rp5-jjmw-4wv2) 7.0 section-inject + [94p4](https://github.com/advisories/GHSA-94p4-4cq8-9g67) 7.5 env exfil
  [[single-project-mass-disclose]] extends n=4 (Pillow / Gitea / n8n / GitPython). → upgrade GitPython to ≥3.1.55.
- [CVE-2026-15074](https://github.com/advisories/GHSA-83w8-p2f5-377r) — `@fastify/static` (npm) · CVSS 7.5 · path-traversal route-guard bypass
  → schedule upgrade @fastify/static to ≥10.1.1.

*MONITOR*
- [GHSA-qq9h-g4jm-xgf3](https://github.com/advisories/GHSA-qq9h-g4jm-xgf3) — `better-auth` (npm) · CVSS 8.3 · pre-account hijacking on magic-link + email-OTP · fix 1.6.22 / 1.7.0-beta.10
  → track; upgrade when convenient.
- [GHSA-r277-6w6q-xmqw](https://github.com/advisories/GHSA-r277-6w6q-xmqw) — `kin-openapi` (Go) · CVSS 9.1 · fail-open auth bypass via `NoopAuthenticationFunc` default · fix 0.144.0
  → track; not-installed per grep.
- npm-malware batch d1 = 4-pack `app-*` scope typosquat vs 7-24's 45-batch = **~11× lower rate**. [[wallet-credential-stealer-supply-chain]] rail quiet day; 0 fresh KEV additions this run.
