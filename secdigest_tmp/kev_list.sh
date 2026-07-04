#!/bin/bash
jq -r --arg s "2026-06-27" '.vulnerabilities[] | select(.dateAdded >= $s) | [.dateAdded, .cveID, .vendorProject, .product, .shortDescription] | @tsv' secdigest_tmp/kev.json
