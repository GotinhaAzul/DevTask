import sqlite3
import threading

import requests
import uvicorn

from mycode.constants import LOCALHOST, LOCALHOST_NAME, LOCALHOST_PORT
from mycode.exceptions import TaskNotFoundError, ValidationError
from mycode.tasks import Task


def setup(filename: str = 'database.db') -> None:
    # STATUS default 0 para False
    connection = sqlite3.connect(filename)
    try:
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (NAME TEXT, ID INTEGER PRIMARY KEY AUTOINCREMENT, STATUS BOOLEAN NOT NULL DEFAULT 0, USERID INTEGER) """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (USERNAME TEXT, PASSWORD TEXT, USERID INTEGER PRIMARY KEY) """)
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_tasks_id ON tasks(id)")
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_users_username ON users(username)")
        columns = [row[1] for row in cursor.execute("PRAGMA table_info(tasks)").fetchall()]
        if "USERID" not in columns:
            cursor.execute("ALTER TABLE tasks ADD COLUMN USERID INTEGER")
        connection.commit()
    finally:
        connection.close()


def json_to_object(payload): # Add type hint later.
    return payload["items"]



def raise_for_api(response: requests.Response) -> None:
    if response.status_code == 404:
        detail = response.json().get("detail", "Task não encontrada.")
        raise TaskNotFoundError(detail)

    if response.status_code == 422:
        detail = response.json().get("detail", "Dados inválidos.")
        raise ValidationError(detail)

    response.raise_for_status()

def startlocalhost():
    uvicorn.run("mycode.api:app", host=LOCALHOST_NAME, port=LOCALHOST_PORT, reload=False)

def localhost_up():
    background_thread = threading.Thread(target=startlocalhost)
    background_thread.start()


def show_tasks():
    response = requests.get(f"{LOCALHOST}/tasks")
    raise_for_api(response)

    tasks = [Task(**item) for item in response.json()["items"]]
    for task in tasks:
        status = "✓" if task.done else "-"
        print(f"[{status}] {task.id}: {task.nome}")

def get_current_user_id(user_id: int):
    return user_id
