#!/usr/bin/env bash
set -e

python3 -m pip install -r requirements.txt
python3 -m pytest -p no:cacheprovider
rm -r test/__pycache__
rm -r app/__pycache__
