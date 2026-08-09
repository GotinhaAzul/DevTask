from mycode.tasks import Task
import sqlite3


class Storage:
    def __init__(self, database: str = "database.db") -> None:
        self.database = database
        self.conn = sqlite3.connect(self.database)


    def add(self, task: Task)-> None:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (name, id, status) VALUES (?, ?, ?)",
            (task.nome, task.id, task.done),
        )
        self.conn.commit()

    def delete(self, task: Task):
        cursor = self.conn.cursor()
        query = "DELETE FROM tasks WHERE id = ?"
        id_to_delete = (task.id,)
        cursor.execute(query, id_to_delete)
        self.conn.commit()

    def read(self) -> list:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        return cursor.fetchall()

def update(self, task: Task) -> None:
    cursor = self.conn.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (not task.done, task.id))
    self.conn.commit()
