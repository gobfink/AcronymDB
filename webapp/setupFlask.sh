#!/bin/bash

# Create a python virtual environment
python3 -m venv flaskvenv

# Activate the virtual environment
source flaskvenv/bin/activate

# Install flask in the virtual environment
pip install flask

# Set the FLASK_APP environment variable
export FLASK_APP=webapp.py

# If we want to permanently set the FLASK_APP variable, see below:
#pip install python-dotenv
#touch .flaskenv # create this file at top level project directory
#FLASK_APP=webapp.py
