#!/bin/bash

ACTIVATE_FILE="./.env/bin/activate"

# Check if python virtual environment already exists
if ! [ -f "$ACTIVATE_FILE" ] ; then
    python3 -m venv .env
fi

# Activate python venv
# TODO: source does not work from inside a script, only directly from bash
source .env/bin/activate

# Install required python packages into venv
python -m pip install -r "./requirements.txt"

# Set Flask environment variables
export FLASK_APP="server.py"
export FLASK_ENV="development"

# Init database if it does not exist
DB_FILE="./instance/db.sqlite"
if ! [ -f "$DB_FILE" ] ; then
    flask init-db
fi

# Start default browser with address of the web-app
python3 -m webbrowser http://127.0.0.1:5000/ &

flask run

# Deactivates the python venv for the given terminal
deactivate
