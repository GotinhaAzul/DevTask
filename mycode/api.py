import sqlite3
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi_pagination import Page, add_pagination, paginate

from mycode.exceptions import TaskNotFoundError, UserAlreadyExistsError, ValidationError
from mycode.logger import LoggingMiddleware
from mycode.schemas import TaskFilter, TaskIn, TaskOut, TaskUpdate, UserIn, UserOut
from mycode.task_storage import Task_Storage
from mycode.taskmanager import TaskManager
from mycode.tasks import Task
from mycode.user_storage import User_Storage
from mycode.usermanager import UserManager
from mycode.users import User

app = FastAPI()
add_pagination(app)
app.add_middleware(LoggingMiddleware)

def get_manager():
    storage = Task_Storage()
    try:
        yield TaskManager(storage=storage)
    finally:
        storage.close()


def get_user_manager():
    storage = User_Storage()
    try:
        yield UserManager(storage=storage)
    finally:
        storage.close()


@app.get("/tasks", response_model=Page[TaskOut]) # Não sei porque o return type é unknown.
def list_tasks(
    query: Annotated[TaskFilter, Query(description="Insert search parameters to search for it.")],
    user_id: int,
    taskmanager: TaskManager = Depends(get_manager),
) -> Page[TaskOut]:

    tasks = taskmanager.get_sorted(query.sort_by, user_id, query.descending)

    filtered_tasks = [
        task for task in tasks
        if (query.id is None or task.id == query.id)
        and (query.nome is None or task.nome == query.nome)
        and (query.done is None or task.done == query.done)
    ]

    return paginate(filtered_tasks)


@app.post("/tasks", status_code=201, response_model=TaskOut)
def add_task(task_in: TaskIn, user_id: int,  manager: TaskManager = Depends(get_manager)) -> Task:
    task = Task(nome=task_in.nome, done=task_in.done)
    try:
        manager.add_task(task, user_id)
    except (ValueError, ValidationError):
        raise HTTPException(status_code=422, detail="Task inválida!")
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, user_id: int, manager: TaskManager = Depends(get_manager)) -> None:
    try:
        manager.delete(task_id, user_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Task de ID {task_id} não encontrada!")


@app.patch("/tasks/{task_id}", status_code=200, response_model=TaskOut)
def update_task(task_id: int, user_id: int, data: TaskUpdate, manager: TaskManager = Depends(get_manager)) ->  Task | None:
    try:
        if "nome" in data.model_fields_set and data.nome is not None: # Verifica se o nome veio + se ele não é None
            manager.update_name(task_id, user_id, data.nome)
        if "done" in data.model_fields_set and data.done is not None:
            manager.set_done(task_id, user_id, data.done)
        return manager.get(task_id, user_id)

    except ValidationError:
        raise HTTPException(status_code=422, detail=f"Task de nome inválido.")

    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Task de ID {task_id} não encontrada!")


@app.post("/register", status_code=201, response_model=UserOut)
def register_user(user_in: UserIn, user_id: int, manager: UserManager = Depends(get_user_manager)) -> User:
    user = User(username=user_in.username, password=user_in.password)
    try:
        manager.add_user(user, user_id)
    except UserAlreadyExistsError:
        raise HTTPException(status_code=409, detail="Usuário já existe!")
    except ValidationError:
        raise HTTPException(status_code=422, detail="Usuário inválido!")
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="USERID ou username já em uso!")
    return user
