import sqlite3
from flask import Flask, request, session, redirect
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = "dev-secret-key"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users_idor.db")
        cur = conn.cursor()
        user = cur.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            session["user_id"] = user[0]
            return redirect(f"/profile?id={user[0]}")
        return "ユーザー名かパスワードが違います"

    return """
        <h1>ログイン</h1>
        <form method="POST">
            <p>ユーザー名: <input name="username"></p>
            <p>パスワード: <input name="password" type="password"></p>
            <button>ログイン</button>
        </form>
    """

@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect("/")

    user_id = request.args.get("id")

    conn = sqlite3.connect("users_idor.db")
    cur = conn.cursor()
    user = cur.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()

    if user is None:
        return "ユーザーが見つかりません"

    return f"""
        <h1>{user[1]} さんのマイページ</h1>
        <p>秘密のメモ: {user[3]}</p>
        <a href="/logout">ログアウト</a>
    """

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5001)