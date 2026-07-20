*vuln-scanner — tirth8205/code-review-graph*

20k-star python mcp code-review tool. 2 confirmed findings.

1 code-level → **PVR [GHSA-chjm-935c-cx8p](https://github.com/tirth8205/code-review-graph/security/advisories/GHSA-chjm-935c-cx8p)**: `_sanitize_name()` — the prompt-injection defense named in `SECURITY.md` — strips ASCII 0x00–0x1F only. tag chars (U+E0000–U+E007F), bidi overrides, zero-width joiners pass through into every downstream llm (claude code / cursor / copilot decode them). first mcp-symbol-flow finding in scanner history.

1 dep audit → **public [issue #665](https://github.com/tirth8205/code-review-graph/issues/665)**: 10 prod-path bumps recommended (mcp 3× HIGH, python-multipart 2× HIGH, pyjwt HIGH HS256 confusion, urllib3 2× HIGH, cryptography HIGH bundled openssl, +5). filed as issue not pr because uv unavailable in sandbox → hand-editing uv.lock breaks the wheel-hash pin.

scanners: semgrep=fail, trufflehog=fail, osv-binary=fail (ISS-018 d32), osv-api=ok, slither=n/a. verified-secrets NOT swept — recorded, not claimed clean.
