from flask import Flask, render_template, request, session, redirect, url_for
import common
app = Flask(__name__)

app.secret_key = b'\xcb\xd2\x97\xd3\xbb\x86\x88$:\xc3G\x85'

users = {"USER": "PAASWORD", "user":  "asdasd", "Alice": "PASSWORD"}


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        if common.can_user_login(username,password, users):
            session['user_id'] = 1
            return redirect(url_for('user_page', username=username))

        else:
            return redirect(url_for('login'))
    return render_template("login.html")


@app.route("/<username>")
def user_page(username):
    return render_template("user_page.html", username=username)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
