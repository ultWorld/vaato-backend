#!/bin/bash

python -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

uvicorn main:app --reload --port 3000
