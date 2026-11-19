import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect("users_hashed.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password_hash TEXT)")
cur.execute(
    "INSERT INTO users (username, password_hash) VALUES (?, ?)",
    ("admin", generate_password_hash("sup3r_s3cret_pw")),
)
cur.execute(
    "INSERT INTO users (username, password_hash) VALUES (?, ?)",
    ("guest", generate_password_hash("guest")),
)

conn.commit()

for row in cur.execute("SELECT * FROM users"):
    print(row)

conn.close()