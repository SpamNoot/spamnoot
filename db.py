import sqlite3
from sqlite3.dbapi2 import PARSE_DECLTYPES
import click
from flask import current_app, g
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types = sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
        db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    ("admin", generate_password_hash("admin")),
                )
        db.commit()
    
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear all data and create new tables"""
    init_db()
    click.echo('Database successfully initialized.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def add_note(text, userid, group="default"):
    database = get_db()
    database.execute(
        "INSERT INTO notes (note, ownerid, st) VALUES (?, ?, ?)",
        (text, userid, group),
    )
    database.commit()

def get_notes(userid):
    database = get_db()
    notes = database.execute(
        'SELECT note FROM notes WHERE ownerid = ?', (userid,)
    ).fetchall()
    return notes

def archive_note(noteid):
    database = get_db()
    database.execute(
        "UPDATE notes\nSET st = 'deleted' WHERE id = (?)",
        (noteid),
    )