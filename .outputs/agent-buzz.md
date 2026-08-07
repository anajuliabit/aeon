*Agent Buzz — 2026-08-07*
_standardization day: a cross-vendor agent-plugins spec ships, and the MCP tool-wrapping cliff finally gets a number._

**agent plugins spec ships**
• @aidevnewss — openai/github/aws/cursor/vercel push agent plugins as one package format carrying skills and MCP servers cross-client.
  https://x.com/aidevnewss/status/2085443561936552415
• @VSMdev — vs code takes the spec but keeps its own commands/hooks/marketplace on top — partial portability, not full.
  https://x.com/VSMdev/status/2085516235257893025

**MCP tool-wrapping hits a cliff**
• @AgenticAIFdn — wrapping every api as an MCP tool degrades agent accuracy past 10–30 tools; each definition eats context.
  https://x.com/AgenticAIFdn/status/2085440771428319437
• @ManasTak — counter-move: skip MCP and tool-call schemas, let the model write code against raw APIs.
  https://x.com/ManasTak/status/2085455876798689640

**governance, not models**
• @johniosifov — 28% of enterprise multi-agent deploys work; the 72% failure mode is governance gaps, not model quality.
  https://x.com/johniosifov/status/2085348321632158142
• @AgenticAIFdn — case for MCP-server governance layers; scaling/security/observability breaks when each service spins up its own MCP.
  https://x.com/AgenticAIFdn/status/2085448368621228180

<!-- _src: xai · candidates: 10 → kept: 6_ -->
