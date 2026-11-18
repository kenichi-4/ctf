import sqlite3
from flask import Flask, request

app = Flask(__name__)

FLAG = "flag{sql_injection_success}"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cur = conn.cursor()
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        print(query, (username, password))
        user = cur.execute(query, (username, password)).fetchone()
        conn.close()

        if user:
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