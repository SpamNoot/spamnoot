# SpamNoot

## 1. What is SpamNoot?

**SpamNoot is a web-based note-taking app.** Users can register and log in, and create notes in the classic sticky note format. A note has a title and a content body.

## 2. List of technologies used in the project

The app uses the Python server _Flask_, with _Jinja_ templates for the rendered HTML/CSS. The database module is _SQLite_, which was chosen because it is built into Python and is easy to work with.

## 3. Setup and running the app

After you clone or download the repository there are a few things you must do to be able to properly run the app. Here is the process:

1. Navigate to the `spamnoot` root directory on the command line.
2. Set the correct environment variables:
   - Linux/macOS terminal:

     ```bash
     export FLASK_APP="server.py"
     export FLASK_ENV="development"
     ```

   - Windows PowerShell:

     ```powershell
     $env:FLASK_APP="server.py"
     $env:FLASK_ENV="development"
     ```

   - Windows Command Prompt:

     ```bat
     set FLASK_APP=server.py
     set FLASK_ENV=development
     ```

3. Run `flask init-db` to initialize the database. Prints _"Database successfully initialized."_ on success.
4. Start the server with `flask run`.
   - If the database has already been initialized once in the app's folder, you can also use `python server.py` to successfully start the server.
5. On startup, _Flask_ prints some lines of info to the terminal. The last line contains the address of the app:
   `Running on http://127.0.0.1:5000/`
6. Navigate to the given address to access SpamNoot.

---

Log in or register, and start taking notes to your heart's content!

Now you can start boosting your productivity! _(as these words are quite fashionable nowadays)_  
