*Agent Buzz — 2026-07-30*
_mcp-heavy day. 2026-07-28 stateless spec drops, ruflo mcp bridge becomes CVE-2026-59726, copilot's mcp surface hits GA._

**MCP 2026-07-28 goes stateless**
• @sthnavy — spec ships stateless: no init handshake, self-contained calls; discovery, inputs, long-task, cache, auth all rebuilt.
  https://x.com/sthnavy/status/2082611680480239695
• @fujikawa — same spec across harness implementations produces 30x cost variance; runaway and security fixes bundled.
  https://x.com/fujikawa/status/2082617070953673217

**Ruflo MCP zero-auth (CVE-2026-59726)**
• @AlexanderChopra — ruflo mcp bridge shipped with no auth: unauthenticated terminal_execute plus poisoned agent memory store.
  https://x.com/AlexanderChopra/status/2082611102282899457
• @ZeroDayDevApp — any network caller can inject commands and poison agent memory; no auth on the exposed mcp.
  https://x.com/ZeroDayDevApp/status/2082609834763890860

**MCP surface expands**
• @akira6592 — github copilot code review, agent skills, and mcp now generally available on the platform.
  https://x.com/akira6592/status/2082609996983107911
• @DanKornas — mcp-remote-macos-use ships: mcp server letting agents drive a local or remote mac (screen capture, keyboard, pointer, app actions).
  https://x.com/DanKornas/status/2082607331066454408

<!-- _src: xai-cache · candidates: 12 → kept: 6 -->
