#!/bin/bash
python3 defi-process.py 2>/dev/null | ./notify "$(cat)"
