#!/usr/bin/env bash
# scripts/build-fallback-prompt.sh — compose the text-fallback prompt for the chat
# handler. Reads SOURCE, MESSAGE, and optional RESEARCH from the environment and
# prints the prompt to stdout. With RESEARCH non-empty, ground the answer in it and
# forbid the "can't research" refusal; otherwise emit the honest degraded prompt.
set -uo pipefail
: "${SOURCE:=your channel}"
: "${MESSAGE:=}"

if [ -n "${RESEARCH:-}" ]; then
  cat <<EOF
You are Aeon replying to your operator on ${SOURCE}. The primary model hit its usage limit, so you are on a text backend — BUT you have fresh live research gathered just now from X and the web (below). Answer the operator's question concretely using ONLY this research; cite the source links; surface the non-obvious angles. Do NOT say you cannot research or to wait for capacity.

LIVE RESEARCH:
${RESEARCH}

Operator question:
"${MESSAGE}"
EOF
else
  cat <<EOF
You are Aeon, an autonomous assistant replying to your operator on ${SOURCE}. You are in a degraded text-only fallback (no file or tool access) because the primary model hit its usage limit. Reply helpfully and concisely in one short paragraph. If the request needs running a skill, editing files, or saving a note, say you will handle it once full capacity is restored.

Operator message:
"${MESSAGE}"
EOF
fi
