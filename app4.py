from fastapi_offline import FastAPIOffline
import sqlite3



app = FastAPIOffline()



@app.post("/users")
def create_user(name: str, age: int):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()



    cursor.execute(
        "INSERT INTO users (name, age) VALUES (?, ? )",(name, age))

    conn.commit()
    conn.close()

    return {"message": "User created"}





@app.get("/users")
def get_users():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    return {"users": users}





@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, age: int):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?",(name, age, user_id) )

    conn.commit()
    conn.close()

    return {"message": "User updated" }





@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id = ?",(user_id,))

    conn.commit()
    conn.close()

    return {"message": "User deleted"}