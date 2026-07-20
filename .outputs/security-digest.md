*Security Digest — 2026-07-20*
Verdict: 3 to patch today (npm malware typosquats), 0 to schedule, 1 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [GHSA-x4cp-w826-x466](https://github.com/advisories/GHSA-x4cp-w826-x466) + [GHSA-6x4h-wrvq-m68h](https://github.com/advisories/GHSA-6x4h-wrvq-m68h) — @vite-js/ui + @vite-js/vui (npm) · type=malware · CVSS n/a
  vendor-scope typosquat of @vitejs (frontend build primitive) — full-compromise + credential-rotate template on install. → audit npm installs for @vite-js/*; packages removed from registry, rotate any secrets exposed since 2026-07-20 00:19Z.
- [GHSA-m78v-9w6f-xwf2](https://github.com/advisories/GHSA-m78v-9w6f-xwf2) — react-icons-svgo (npm) · type=malware · CVSS n/a
  typosquat mashup of two popular npm names (react-icons + svgo). → audit npm installs for react-icons-svgo; removed from registry.
- [GHSA-g7rx-jhhj-8whr](https://github.com/advisories/GHSA-g7rx-jhhj-8whr) — svgson-lite (npm) · type=malware · CVSS n/a
  typosquat of svgson SVG parser lib. → audit npm installs for svgson-lite; removed from registry.

*MONITOR*
- 75-pkg @gocortexio/npmgremlinbox-* wave (npm, 03:00–03:01Z 7-20) — self-labeled `malware-*`/`typosquat-*` = Cortex XSIAM scanner-detection testbed (adjacent to vybscan-testbed-* 7-20 00:07Z). → not a real threat; filter @gocortexio/* + vybscan-testbed-* from malware-count baselines.

_KEV day-4 zero-cadence extends (7-17 → 7-20 no adds, first 4-consec-zero in memory). npm-malware wave resumes 11 real pkgs after d6=0 cool-off (7-19 late 4 + 7-20 early 7) — revises "complete cool-off" to 1-day pause. Reviewed advisories 0 critical + 0 high published 7-18 15Z → 7-20 15Z._
