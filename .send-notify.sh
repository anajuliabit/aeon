#!/usr/bin/env bash
set -euo pipefail
cd /home/runner/work/aeon/aeon
MSG=$(cat .daily-routine-msg.md)
./notify "$MSG"
