from mycode.tasks import Task
import sqlite3


class Storage:
    def __init__(self, database: str = "database.db") -> None:
        self.database = database
        self.conn = sqlite3.connect(self.database)
        self.conn.row_factory = sqlite3.Row

    def add(self, task: Task)-> None:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (name, id, status) VALUES (?, ?, ?)",
            (task.nome, task.id, task.done),
        )
        self.conn.commit()

    def delete(self, taskid: int):
        cursor = self.conn.cursor()
        query = "DELETE FROM tasks WHERE id = ?"
        id_to_delete = (taskid,)
        cursor.execute(query, id_to_delete)
        self.conn.commit()

    def read(self) -> list[Task]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        content = [Task(nome=row['name'], id=row[1], done=bool(row[2])) for row in cursor.fetchall()]
        return content

    def update(self, task: Task) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE tasks SET name = ?, status = ? WHERE id = ?", (task.nome, task.done, task.id))
        self.conn.commit()

    def getbyid(self, taskid: int) -> Task:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE ID = ?", (taskid,))
        content = cursor.fetchone()
        if content == None:
            return None
        else:
            return Task(nome=content['name'], id=content[1], done=bool(content[2]))
