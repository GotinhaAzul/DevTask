import sqlite3

from mycode.users import User


class User_Storage:
    def __init__(self, database: str = "database.db") -> None:
        self.database = database
        self.conn = sqlite3.connect(self.database, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

    def add(self, user: User, user_id: int)-> None:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password, USERID) VALUES (?, ?, ?)",
            (user.username, user.password, user_id),
        )
        self.conn.commit()
        user.id = user_id


    def delete(self, username: str):
        cursor = self.conn.cursor()
        query = "DELETE FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        self.conn.commit()


    def close(self) -> None:
        self.conn.close()

    def getbyusername(self, username: str) -> User | None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        content = cursor.fetchone()
        if content == None:
            return None
        else:
            return User(username=content["username"], password=content["password"], id=content["USERID"])
