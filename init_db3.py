import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect("users_idor.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password_hash TEXT, secret TEXT)")
cur.execute(
    "INSERT INTO users (username, password_hash, secret) VALUES (?, ?, ?)",
    ("admin", generate_password_hash("sup3r_s3cret_pw"), "flag{idor_found}"),
)
cur.execute(
    "INSERT INTO users (username, password_hash, secret) VALUES (?, ?, ?)",
    ("guest", generate_password_hash("guest"), "今日のバイトは18時から"),
)

conn.commit()
conn.close()