import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
cur.execute("INSERT INTO users (username, password) VALUES ('admin', 'sup3r_s3cret_pw')")
cur.execute("INSERT INTO users (username, password) VALUES ('guest', 'guest')")

conn.commit()
conn.close()