import sqlite3
import threading

import requests
import uvicorn

from mycode.constants import LOCALHOST, LOCALHOST_NAME, LOCALHOST_PORT
from mycode.exceptions import TaskNotFoundError, TaskValidationError
from mycode.tasks import Task


def setup(filename = 'database.db') -> None:
    # STATUS default 0 para False
    connection = sqlite3.connect(filename)
    try:
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (NAME TEXT, ID INTEGER PRIMARY KEY AUTOINCREMENT, STATUS BOOLEAN NOT NULL DEFAULT 0) """)
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_tasks_id ON tasks(id)") # Reduntante. Vou manter apenas para não me esquecer e caso, no futuro, use uma forma diferente de ID (Irei...)
        connection.commit()
        connection.close()
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
        raise TaskValidationError(detail)

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
