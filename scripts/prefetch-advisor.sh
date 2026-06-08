#!/usr/bin/env bash
# Pre-fetch investiments data OUTSIDE the Claude sandbox (sandbox blocks curl with
# secrets in headers). Runs before Claude for advisor skills only.
#   - all advisor skills: GET /api/snapshot           → .investiments-cache/snapshot.json
#   - advisor-debate / -portfolio-manager: GET today's run doc → .investiments-cache/advisor-run.json
# Reads cached files inside the skill. No-op (exit 0) for non-advisor skills or when unconfigured.
set -uo pipefail

SKILL="${1:-}"
case "$SKILL" in
  portfolio-snapshot|advisor-*) ;;
  *) exit 0 ;;
esac

BASE="${INVESTIMENTS_BASE_URL:-https://investiments-production.up.railway.app}"
if [ -z "${INVESTIMENTS_BASIC_AUTH:-}" ]; then
  echo "prefetch-advisor: INVESTIMENTS_BASIC_AUTH not set, skipping"
  exit 0
fi

mkdir -p .investiments-cache
TODAY=$(date -u +%Y-%m-%d)

echo "prefetch-advisor: fetching snapshot for $SKILL ..."
curl -fsS --max-time 30 -H "Authorization: Basic ${INVESTIMENTS_BASIC_AUTH}" \
  "${BASE}/api/snapshot" -o .investiments-cache/snapshot.json \
  || echo "::warning::prefetch-advisor: snapshot fetch failed"

case "$SKILL" in
  advisor-debate|advisor-portfolio-manager)
    echo "prefetch-advisor: fetching run doc ($TODAY) for $SKILL ..."
    curl -fsS --max-time 30 -H "Authorization: Basic ${INVESTIMENTS_BASIC_AUTH}" \
      "${BASE}/api/advisor/run?date=${TODAY}" -o .investiments-cache/advisor-run.json \
      || echo "::warning::prefetch-advisor: run-doc fetch failed"
    ;;
esac

exit 0
