#!/bin/bash
pip install pandas
VIRTUAL_ENV = venv
if [ -d "$VIRTUAL_ENV" ]; then
source ./venv/bin/activate
else
python3 -m venv venv
source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
fi
python3 -Wignore main.py
