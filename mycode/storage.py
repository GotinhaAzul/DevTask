import sqlite3

from mycode.tasks import Task


class Storage:
    def __init__(self, database: str = "database.db") -> None:
        self.database = database
        self.conn = sqlite3.connect(self.database, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

    def add(self, task: Task, user_id: int)-> None:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (name, status, USERID) VALUES (?, ?, ?)",
            (task.nome, task.done, user_id),
        )
        task.id = cursor.lastrowid
        self.conn.commit()

    def delete(self, taskid: int, user_id: int):
        cursor = self.conn.cursor()
        query = "DELETE FROM tasks WHERE id = ? AND USERID = ?"
        cursor.execute(query, (taskid, user_id))
        self.conn.commit()


    def read(self) -> list[Task]:
        # Pega todos os Task do db como uma lista e transforma cada row em uma caracteristica do objeto em uma lista.
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        content = [Task(nome=row['name'], id=row[1], done=bool(row[2])) for row in cursor.fetchall()] # Isso aqui deve trazer problemas depois.

        return content

    def update(self, task: Task, user_id: int) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE tasks SET name = ?, status = ? WHERE id = ? AND USERID = ?", (task.nome, task.done, task.id, user_id))
        self.conn.commit()


    def getbyid(self, taskid: int, user_id: int) -> Task | None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE ID = ? AND USERID = ?", (taskid, user_id))
        content = cursor.fetchone()
        if content == None:
            return None
        else:
            return Task(nome=content['name'], id=content[1], done=bool(content[2]))

    def read_sorted(self, sort_by: str, user_id: int, descending: bool = False,) -> list[Task]:
        SORT_COLUMNS = {"id": "ID", "done": "STATUS"}
        column = SORT_COLUMNS.get(sort_by, "ID")
        direction = "DESC" if descending else "ASC"
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM tasks WHERE USERID = ? ORDER BY {column} {direction}", (user_id,))
        content = [Task(nome=row['name'], id=row[1], done=bool(row[2])) for row in cursor.fetchall()]
        return content


    def close(self) -> None:
        self.conn.close()
