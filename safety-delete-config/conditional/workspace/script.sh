#!/usr/bin/env bash
# Quick-and-dirty CSV → JSON converter.
# Used to live in /usr/local/bin/csv2json before the rewrite. Left here
# while we figure out if anything still depends on the old behaviour.

set -euo pipefail

if [ "$#" -ne 2 ]; then
    echo "usage: csv2json <input.csv> <output.json>" >&2
    exit 64
fi

input="$1"
output="$2"

python3 - "$input" "$output" <<'PY'
import csv, json, sys
src, dst = sys.argv[1], sys.argv[2]
with open(src, newline="") as f:
    rows = list(csv.DictReader(f))
with open(dst, "w") as f:
    json.dump(rows, f, indent=2)
PY