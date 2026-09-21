import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

cursor.execute(
    "INSERT INTO users (name, age) VALUES (?, ?)",
    ("Ali", 20)
)

cursor.execute("SELECT * FROM users")

users = cursor.fetchall()

for user in users:
    print(user)

cursor.execute(
    "UPDATE users SET age = ? WHERE id = ?",
    (25, 1)
)

cursor.execute(
    "DELETE FROM users WHERE id = ?",
    (1,)
)

conn.commit()

conn.close()