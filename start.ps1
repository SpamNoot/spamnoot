# Check if PowerShell is running on Windows or not
if ([System.Environment]::OSVersion.Platform -eq "Win32NT") {
    $ACTIVATE_FILE=".\.env\Scripts\Activate.ps1"
} else {
    $ACTIVATE_FILE=".\.env\bin\Activate.ps1"
}

# Check if python virtual environment already exists
if (-not(Test-Path -Path "$ACTIVATE_FILE" -PathType Leaf)) {
    python -m venv .env
}

# Activate python venv
& $ACTIVATE_FILE

# Install required python packages into venv
python -m pip install -r ".\requirements.txt"

# Set Flask environment variables
$env:FLASK_APP="server.py"
$env:FLASK_ENV="development"

# Init database if it does not exist
$DB_FILE=".\instance\db.sqlite"
if (-not(Test-Path -Path "$DB_FILE" -PathType Leaf)) {
    flask init-db
}

# Start default browser with address of the web-app
Start-Process "http://127.0.0.1:5000/"
# Also works for opening the browser:
# Start-Process -NoNewWindow -FilePath python.exe -ArgumentList "-m webbrowser http://127.0.0.1:5000/"

flask run

# Deactivates the python venv for the given terminal
deactivate
