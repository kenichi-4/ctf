import sqlite3
from flask import Flask, request
from werkzeug.security import check_password_hash

app = Flask(__name__)

FLAG = "flag{sql_injection_success}"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users_hashed.db")
        cur = conn.cursor()
        query = "SELECT * FROM users WHERE username = ?"
        user = cur.execute(query, (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            if user[1] == "admin":
                return f"ようこそ admin さん！ フラグ: {FLAG}"
            return f"ようこそ {user[1]} さん"
        return "ユーザー名かパスワードが違います"

    return """
        <h1>ログイン</h1>
        <form method="POST">
            <p>ユーザー名: <input name="username"></p>
            <p>パスワード: <input name="password" type="password"></p>
            <button>ログイン</button>
        </form>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5001)