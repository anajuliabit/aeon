#!/usr/bin/env bash
# scripts/tg-chunk.sh — split stdin into <= TG_CHUNK_MAX-char chunks, preferring line
# boundaries (a single overlong line is hard-split), emitted NUL-separated so a bash
# consumer can `mapfile -d ''`. Telegram's 4096 limit counts UTF-16 code units, and
# bash counts characters (1 char = 1 UTF-16 unit for all BMP text), so the 4000
# default caps in the right unit with room for the "(i/n)" part label Task 2 adds.
# (Edge: non-BMP chars — emoji — are 2 UTF-16 units each, so an emoji-dense >2048-char
# chunk could still exceed 4096; that rare case now surfaces as a logged send failure
# rather than a silent drop.) Pure: concatenating the chunks reproduces the input
# exactly. bash-3.2 compatible (no mapfile here).
set -uo pipefail
MAX="${TG_CHUNK_MAX:-4000}"

# Read all of stdin, preserving any trailing newline (command-sub would strip it).
MSG="$(cat; printf x)"; MSG="${MSG%x}"

rest="$MSG"
while [ "${#rest}" -gt "$MAX" ]; do
  window="${rest:0:$MAX}"
  if [[ "$window" == *$'\n'* ]]; then
    head="${window%$'\n'*}"$'\n'   # up to and including the last newline in the window
  else
    head="$window"                 # no newline in range: hard-split at MAX
  fi
  printf '%s\0' "$head"
  rest="${rest:${#head}}"
done
[ -n "$rest" ] && printf '%s\0' "$rest"
exit 0
