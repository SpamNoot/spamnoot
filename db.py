import sqlite3
from sqlite3.dbapi2 import PARSE_DECLTYPES
import click
from flask import current_app, g
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash


def get_db():
    if 'database' not in g:
        g.database = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types = sqlite3.PARSE_DECLTYPES
        )
        g.database.row_factory = sqlite3.Row
    return g.database
def close_db(e=None):
    database = g.pop('db', None)
    if database is not None:
        database.close()

def init_db():
    database = get_db()
    with current_app.open_resource('schema.sql') as f:
        database.executescript(f.read().decode('utf8'))
        database.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    ("admin", generate_password_hash("admin")),
                )
        database.commit()
    
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear all data and create new tables"""
    init_db()
    click.echo('Database successfully initialized.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def add_note(text, userid):
    database = get_db()
    database.execute(
        "INSERT INTO notes (note, ownerid) VALUES (?, ?)",
        (text, userid),
    )
    database.commit()
