from dataclasses import asdict
import sqlite3
import threading

import requests
import uvicorn

from mycode.constants import LOCALHOST, LOCALHOST_NAME, LOCALHOST_PORT
from mycode.exceptions import TaskNotFoundError, UserAlreadyExistsError, ValidationError
from mycode.schemas import UserIn, UserOut
from mycode.tasks import Task
from mycode.users import User


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

    if response.status_code == 401:
        detail = response.json().get("detail", "Login Recusado.")
        raise ValidationError(detail)
    if response.status_code == 409:
        detail = response.json().get("detail", "Conflito de cadastro.")
        raise ValidationError(detail)

    response.raise_for_status()

def startlocalhost():
    uvicorn.run("mycode.api:app", host=LOCALHOST_NAME, port=LOCALHOST_PORT, reload=False)

def localhost_up():
    background_thread = threading.Thread(target=startlocalhost)
    background_thread.start()


def show_tasks(userID: int):
    response = requests.get(f"{LOCALHOST}/tasks", params={"user_id": userID})
    raise_for_api(response)

    tasks = [Task(**item) for item in response.json()["items"]]
    for task in tasks:
        status = "✓" if task.done else "-"
        print(f"[{status}] {task.id}: {task.nome}")

def get_current_user_id(user_id: int):
    return user_id

def login_register_flow():
    print("1. for Login")
    print("2. for Register")
    esc = input()
    match esc:
        case "1":
            user = login()
            return user
        case "2":
            user = register()
            return user

def login():
    username = input("Insira seu username: ")
    password = input("Insira a sua senha: ")
    user = UserIn(username=username, password=password)
    response = requests.post(f"{LOCALHOST}/login", json=asdict(user))
    raise_for_api(response)
    response = response.json()
    user = UserOut(username=response["username"], userID=response["userID"])
    return user

def register():
    username = input("Insira um nome de usuário: ")
    password = input("Insira a sua senha: ")
    user = User(username=username, password=password)
    response = requests.post(f"{LOCALHOST}/register", json={"username": user.username, "password": user.password})
    raise_for_api(response)
    response = response.json()
    user = UserOut(username=response["username"], userID=response["userID"])
    print("Usuário criado com sucesso!")
    return user
