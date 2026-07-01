*Security Digest — 2026-07-01*
Verdict: 3 supply-chain compromises to purge now, 3 to monitor (Fission node-escape cluster, no fix yet). _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [GHSA-gf82-j362-r5f6](https://github.com/advisories/GHSA-gf82-j362-r5f6) — livekit-agents (npm) · malware
  LiveKit Agents SDK brandjack — real pkg is `@livekit/agents`. Extends agent-infra brandjack thread (day 5: ai-sdk-ollama, autotel-18, now LiveKit + Google-Cloud agent-starter-pack).
  → uninstall `livekit-agents`; rotate any tokens/creds exposed at install-time.
- [GHSA-j28m-58xp-3wgh](https://github.com/advisories/GHSA-j28m-58xp-3wgh) — confluent-kafka-javascript (npm) · malware
  Confluent's Kafka client brandjack — real pkg is `@confluentinc/kafka-javascript`. First enterprise-data-infra brandjack of the 48h wave (prior 4 days were AI-infra only).
  → uninstall; rotate broker credentials.
- [GHSA-4wm6-vmww-2544](https://github.com/advisories/GHSA-4wm6-vmww-2544) chai-as-persisted + [GHSA-m282-3m8c-qjwj](https://github.com/advisories/GHSA-m282-3m8c-qjwj) chai-as-assured (npm) · malware
  chai-as-promised brandjack pair, same-window publish 15:56–15:59Z.
  → uninstall both; use `chai-as-promised`; rotate CI install-time secrets.

*MONITOR*
- [GHSA-m63v-2g9w-2w6v](https://github.com/advisories/GHSA-m63v-2g9w-2w6v) + 8 sibling advisories — fission (Go) · 4× CVSS 9.9 crit + 5 high · no fix · EPSS ≤0.003
  Coordinated 9-CVE disclosure batch on `github.com/fission/fission` ≤ 1.23.0: podspec injection, node escape, cross-namespace EnvRef, MessageQueueTrigger secret materialization, cluster takeover.
  → track upstream; isolate Fission control plane and RBAC-block user PodSpec paths until patch ships.
- [GHSA-f5mr-q85p-6hh6](https://github.com/advisories/GHSA-f5mr-q85p-6hh6) — sigstore/fulcio (Go) · CVSS 8.7 · no fix
  OIDC redirect SSRF + JWKS substitution → K8s SA token leak on meta-issuer paths, ≤ 1.8.5.
  → track; disable meta-issuer discovery on any deployed Fulcio issuer.
- [GHSA-g4w6-vmgf-xqvx](https://github.com/advisories/GHSA-g4w6-vmgf-xqvx) — @cedar-policy/authorization-for-expressjs (npm) · CVSS 8.8 · no fix
  Authz bypass via query-string manipulation, ≤ 0.2.0.
  → track; add pre-Cedar query-param whitelist in Express middleware.

_KEV week: 0 net-new since SimpleHelp CVE-2026-48558 (6-29) — day-2 zero-cadence. Reviewed CVEs 48h: 100% no-patch (Fission 9-CVE batch, Fulcio, Cedar, Adonis bodyparser, OpenBabel). Supply-chain: 15 net-new npm malware in 8h — agent-infra brandjack still dominant (LiveKit + Google-Cloud agent-starter-pack extend yesterday's ai-sdk-ollama + autotel-18 thread). 0 pip/crates/Go malware in 48h — npm remains 100% of supply-chain surface._
