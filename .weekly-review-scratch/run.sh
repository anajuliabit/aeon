#!/bin/bash
gh api "repos/anajuliabit/aeon/actions/runs?created=2026-07-13T19:00:00Z..2026-07-20T19:30:00Z&per_page=100" --paginate 2>/dev/null | python3 .weekly-review-scratch/aggregate.py
