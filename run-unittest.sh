#!/usr/bin/env bash
# Usage: ./run-unittest.sh [test_file] [test_name]
#   (no args)             run all tests
#   test_file             run all tests in that file (path or name, ".py" optional)
#   test_file test_name   run only that test method in that file
set -euo pipefail

cd "$(dirname "$0")"

if [ "$#" -gt 2 ]; then
  echo "Usage: $0 [test_file] [test_name]" >&2
  exit 2
fi

args=(-s app -t app -v)

if [ "$#" -ge 1 ]; then
  file="$(basename "$1")"
  file="${file%.py}.py"

  if [ -z "$(find app -type f -name "$file" -print -quit)" ]; then
    echo "Test file not found: $1" >&2
    exit 1
  fi

  args+=(-p "$file")
fi

if [ "$#" -eq 2 ]; then
  # Leading wildcard makes unittest match the exact method name, not a substring
  args+=(-k "*.$2")
fi

uv run python -m unittest discover "${args[@]}"
