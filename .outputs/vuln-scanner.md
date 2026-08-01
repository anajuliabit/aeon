🔒 *vuln-scanner — yc-software/qm*

clean audit. 8 candidates reviewed, 0 confirmed.

target: 4,302★ ts multiplayer agent harness. PVR enabled + SECURITY.md present.

npm audit clean across 6 workspaces (577 deps). 3 parallel explore agents (auth+capability / injection+ssrf+traversal / secrets+crypto) over ~350 ts files — every low/medium candidate dropped in triage (defense-in-depth, deliberate design, misconfig-not-code, dev-only + attacker-privilege exceeds-yield).

notably tight surface — alg-pinned jose, timingSafeEqual throughout, replay-deduped source-auth, host-pinned credential-broker, IP-pinned egress with fail-closed lua authz, closed dns-rebinding.

scanners: semgrep=fail, trufflehog=fail, osv-binary=fail (iss-018 sandbox day-40), npm-audit=ok, hand-audit=ok.

zero PVR filed. zero PR opened. channel warm.
