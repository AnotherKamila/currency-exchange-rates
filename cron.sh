#!/bin/sh

cd "$(dirname "$0")"
. venv/bin/activate
./getrates.py rates.csv
git commit -m "[automatic commit] rates for $(date +%Y-%m-%d)" -o -- rates.csv
