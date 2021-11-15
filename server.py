import os
from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
import common
app = Flask(__name__, instance_relative_config=True)
import db
from db import get_db
db.init_app(app)

app.config.from_mapping(
    SECRET_KEY=b'\xcb\xd2\x97\xd3\xbb\x86\x88$:\xc3G\x85',
    DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
)
app.config.from_pyfile('config.py', silent=True)
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

app.secret_key = b'\xcb\xd2\x97\xd3\xbb\x86\x88$:\xc3G\x85'
app.config['DATABASE']=os.path.join(app.instance_path, 'db.sqlite')


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('user_page', username=username))

        else:
            return redirect(url_for('login'))
    return render_template("login.html")
@app.route("/register.html", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        if not username:
            error = 'Username is required.'
        if not password:
            error = 'Password is required.'
        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} already exists."
            else:
                return redirect(url_for('login'))
    return render_template('register.html')




@app.route("/<username>")
def user_page(username):
    return render_template("user_page.html", username=username)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )