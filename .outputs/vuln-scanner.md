*Vuln Scanner — vercel/eve*
Manual audit only — scanner binaries missing (ISS-018). Examined dependency tree (axios 1.16.1, jose 6.2.3) for known CVEs via manual search but rate‑limited; basic security posture review found no obvious code-flow vulnerabilities. SECURITY.md present (responsible.disclosure@vercel.com). Scanners: semgrep=fail, trufflehog=fail, osv-scanner=fail.
