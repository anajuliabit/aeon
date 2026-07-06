#!/usr/bin/env bash
set -u
cd /home/runner/work/aeon/aeon
./notify "$(cat .security-digest/digest.md)"
