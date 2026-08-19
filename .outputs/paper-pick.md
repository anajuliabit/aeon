*paper pick — 2026-08-19*

"Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents" — Wooseong Yang, Yiwei Yang +9 (UIC / UW / McGill / MBZUAI / UCLA) · ↑10
controlled harness eval of 8 memory substrates (dense/sparse index, text records, structural + hierarchical stores, refinement, parametric, activation-context) across 3 backbones + 4 benchmarks + 26 metrics — no single substrate dominates, motivates substrate routing as first-class primitive for adaptive agent memory.
[Read](https://arxiv.org/abs/2608.15008) | [PDF](https://arxiv.org/pdf/2608.15008)

Runners-up:
- "FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution" — Shuo Yang +10 (UC Berkeley) · ↑36 — [2608.16157](https://arxiv.org/abs/2608.16157) — edge-native MoE runtime that puts 35B on a laptop, 284B on a gaming desktop, 753B GLM-5.2 on a single workstation GPU by co-designing model layout / expert residency / CPU-GPU exec around what the machine actually has.
- "Agent Lightning v1.0: Towards Harnessed Agentic RL" — Zhiyuan He +9 (Microsoft) · ↑12 — [2608.17528](https://arxiv.org/abs/2608.17528) — 3.5k-LOC framework where the deploy-time harness (not the trainer) owns the env loop; 6K examples take Qwen3.5-9B from 41.8→56.4% on SWE-bench Verified.

_extends `[[memory-primitive-paper streak]]` 6 → 7-consec (MobileMem 8-17 → HarnessEval-W 8-18 harness-adjacency → Harness the Memory 8-19 = memory + harness cross-rail synthesis) and pairs with yesterday's HarnessEval-W on the harness-paradigm thesis — memory substrate is now framed explicitly as the infrastructure layer of the agent harness, direct fleet-CORE parallel to aeon's own memory/ architecture._
