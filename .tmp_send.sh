#!/usr/bin/env bash
set -euo pipefail
MSG=$(cat .tmp_notify.md)
exec bash notify "$MSG"
