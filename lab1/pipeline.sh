#!/bin/bash

if [ ! -d ".venv" ]; then
	python3 -m venv .venv
	echo "New virtual environment created"
fi

source .venv/bin/activate

pip install --quiet -r requirements.txt

python3 scripts/data_creation.py
python3 scripts/data_preprocessing.py
python3 scripts/model_preparation.py
python3 scripts/model_testing.py
