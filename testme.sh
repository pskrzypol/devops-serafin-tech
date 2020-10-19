#!/bin/bash

source venv/bin/activate

export FLASK_APP=main.py

python -m flask run

