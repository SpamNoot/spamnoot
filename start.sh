export FLASK_APP="server.py"
export FLASK_ENV="development"

FILE=./instance/db.sqlite

if ! [ -f "$FILE" ]; then
    flask init-db
fi

sh ./browser.sh&

flask run
