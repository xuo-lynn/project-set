#!/bin/bash/env bash
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip3 install -r requirements.txt
flask run --host=0.0.0.0
