*Security Digest — 2026-08-13 15:42Z (delta since 14:46Z)*
Verdict: nothing urgent since prior digest. 19 fresh npm malware pkgs (100% npm), 0 fresh KEV, 0 fresh reviewed critical/high. Aeon-fleet clean d14 holds. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- 19 npm malware advisories 15:04Z→15:36Z — 3 fleet-adjacent: [ai-analyzer](https://github.com/advisories/GHSA-v54f-w8mv-c6xf) (ai-tooling typosquat), [ac_semantic-ui_ts](https://github.com/advisories/GHSA-hjh8-hv66-6mwc) + [ac_calendar_ts](https://github.com/advisories/GHSA-xgwp-29j2-jxj3) (react-ecosystem typosquats). Rest = @easy-entry/* x3 + @demica/* x3 + @frostnode/* x2 + @shell-*/routes x2 + @open-banking/cabinet-providers + @chunklab/hexparse + @bytemend/mfebus + @briskforge/envcheck + datetime-format-xutil + datetime-fmt-xutil. 0/19 impact tracked deps.
  → remove any `ai-analyzer` / `ac_semantic-ui_ts` / `ac_calendar_ts` install; rotate npm creds if consumed.
