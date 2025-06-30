from flask import Flask, render_template, request, redirect, session, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

def get_db():
    conn = sqlite3.connect("todo.db")
    conn.row_factory = sqlite3.Row
    return conn

with get_db() as db:
    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            hash TEXT NOT NULL
        );
    """)
    db.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            task TEXT NOT NULL,
            due_date TEXT,
            priority TEXT,
            complete BOOLEAN NOT NULL DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)

@app.route("/")
def index():
    if "user_id" not in session:
        return redirect("/login")

    db = get_db()
    todos = db.execute("SELECT * FROM todos WHERE user_id = ?", (session["user_id"],)).fetchall()

    total = len(todos)
    completed = len([todo for todo in todos if todo["complete"]])

    progress = int((completed / total) * 100) if total > 0 else 0

    return render_template("index.html", todos=todos, progress=progress)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        if not username or not password or not confirm:
            flash("Fill all fields.")
            return redirect("/register")
        if password != confirm:
            flash("Passwords don’t match.")
            return redirect("/register")

        hash_pw = generate_password_hash(password)
        try:
            db = get_db()
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", (username, hash_pw))
            db.commit()
            flash("Account created! Now login.")
            return redirect("/login")
        except sqlite3.IntegrityError:
            flash("Username already exists.")
            return redirect("/register")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

        if user is None or not check_password_hash(user["hash"], password):
            flash("Invalid username or password.")
            return redirect("/login")

        session["user_id"] = user["id"]
        return redirect("/")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/add", methods=["POST"])
def add():
    if "user_id" not in session:
        return redirect("/login")

    task = request.form.get("task")
    due_date = request.form.get("due_date")
    priority = request.form.get("priority")

    if task:
        db = get_db()
        db.execute("INSERT INTO todos (user_id, task, due_date, priority) VALUES (?, ?, ?, ?)",
                   (session["user_id"], task, due_date, priority))
        db.commit()

    return redirect("/")

@app.route("/complete/<int:todo_id>")
def complete(todo_id):
    if "user_id" not in session:
        return redirect("/login")

    db = get_db()
    db.execute("UPDATE todos SET complete = 1 WHERE id = ? AND user_id = ?", (todo_id, session["user_id"]))
    db.commit()
    return redirect("/")

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    if "user_id" not in session:
        return redirect("/login")

    db = get_db()
    db.execute("DELETE FROM todos WHERE id = ? AND user_id = ?", (todo_id, session["user_id"]))
    db.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run()
