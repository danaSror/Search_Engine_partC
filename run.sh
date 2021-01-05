#!/bin/bash

python3 -m venv venv
mkdir venv/nltk_data

source venv/bin/activate
pip -V
python3 -m pip install --upgrade pip
pip -V
pip install -r requirements.txt
python3 setup.py
deactivate
