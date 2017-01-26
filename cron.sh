#!/bin/sh

cd "$(dirname "$0")"
. venv/bin/activate
export LANG=en_US.UTF-8
./getrates.py rates.csv >> cronlog.txt 2>>cronerr.txt
git commit -m "[automatic commit] rates for $(date +%Y-%m-%d)" -o -- rates.csv >> cronlog.txt 2>>cronerr.txt
git push >> cronlog.txt 2>> cronerr.txt
