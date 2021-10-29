from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

app.secret_key = b'\xcb\xd2\x97\xd3\xbb\x86\x88$:\xc3G\x85'


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        if username == 'USER' and password == 'PASSWORD':
            session['user_id'] = 1
            return redirect(url_for('user_page'))
        else:
            return redirect(url_for('login'))
    return render_template("login.html")

@app.route("/user_page")
def user_page():
    return render_template("user_page.html")


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
