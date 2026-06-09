#!/usr/bin/env bash
set -euo pipefail
MSG=$(cat /home/runner/work/aeon/aeon/.outputs/token-movers.md)
exec /home/runner/work/aeon/aeon/notify "$MSG"
