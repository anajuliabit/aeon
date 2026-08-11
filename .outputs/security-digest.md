*Security Digest — 2026-08-11*
verdict: nothing urgent for our stack. 4th consec malware-only day. defi-brand pypi wave is the headline. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY — malware macro*
- 19 fresh malicious packages published 8-10 20Z → 8-11 14Z (13 npm, 6 pip). all outside tracked deps (aeon-fleet clean d12 vs security surface).
- headline cluster: **8 defi-protocol-brand pip typosquats** in ~15h window — `euler-sdk`, `morpho-sdk`, `dlmm`, `dlmm-sdk`, `joule-btp-extension`, `plp-contract`, `neutrl-core`, `neutrl-contracts`. named for euler / morpho / meteora-dlmm / joule / neutrl. first pypi cluster explicitly targeting defi-dev pip surface in memory-window.
- 3rd scope on the `sqlite` brand: `@sqlite-labs/nodesql` + `@sqlite-labs/createsql` join yesterday's `@sqlite-prime/*` + `@sqlite-table/*` = same-attacker 3-scope pattern.
- npm namespace-typo risk: `commonjs-assert` + `commonjs-assertion` shadow the node builtin. `fetch-runtime`, `lines-columns`, `newtun` blend with dev tooling names.
- → if any dev on the team touched pypi for `euler` / `morpho` / `meteora` / `joule` / `neutrl` sdks in the last 24h, rotate anything the shell touched and check `~/.pypi_history`. otherwise nothing to install.

*KEV (this week)*
- 0 net-new since 8-07 (loadmaster). quiet-baseline extends to 4-consec-utc-day.

*Reviewed critical / high (48h)*
- 0 fresh in any tracked ecosystem after dedup. latest reviewed critical is 8-07 `crypto-js` (GHSA-rg76); latest high is 8-07 `pymdown-extensions` (GHSA-gm37). the reviewed pipeline stayed dark 4 days running while the malware pipeline shipped 100+ items.

*MONITOR*
- none open. no unpatched-in-tracked-stack items today.
