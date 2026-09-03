from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi_pagination import Page, add_pagination, paginate

from mycode.exceptions import TaskNotFoundError, TaskValidationError
from mycode.schemas import TaskFilter, TaskIn, TaskOut, TaskUpdate
from mycode.storage import Storage
from mycode.taskmanager import TaskManager
from mycode.tasks import Task

app = FastAPI()
add_pagination(app)

def get_manager():
    storage = Storage()
    try:
        yield TaskManager(storage=storage)
    finally:
        storage.close()


@app.get("/tasks", response_model=Page[TaskOut]) # Não sei porque o return type é unknown.
def list_tasks(
    query: Annotated[TaskFilter, Query(description="Insert search parameters to search for it.")],
    taskmanager: TaskManager = Depends(get_manager),
) -> Page[TaskOut]:

    tasks = taskmanager.get_sorted(query.sort_by, query.descending)

    filtered_tasks = [
        task for task in tasks
        if (query.id is None or task.id == query.id)
        and (query.nome is None or task.nome == query.nome)
        and (query.done is None or task.done == query.done)
    ]

    return paginate(filtered_tasks)


@app.post("/tasks", status_code=201, response_model=TaskOut)
def add_task(task_in: TaskIn, manager: TaskManager = Depends(get_manager)) -> Task:
    task = Task(nome=task_in.nome, done=task_in.done)
    try:
        manager.add_task(task)
    except (ValueError, TaskValidationError):
        raise HTTPException(status_code=422, detail="Task inválida!")
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, manager: TaskManager = Depends(get_manager)) -> None:
    try:
        manager.delete(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Task de ID {task_id} não encontrada!")


@app.patch("/tasks/{task_id}", status_code=200, response_model=TaskOut)
def update_task(task_id: int, data: TaskUpdate, manager: TaskManager = Depends(get_manager)) ->  Task | None:
    try:
        if "nome" in data.model_fields_set and data.nome is not None: # Verifica se o nome veio + se ele não é None
            manager.update_name(task_id, data.nome)
        if "done" in data.model_fields_set and data.done is not None:
            manager.set_done(task_id, data.done)
        return manager.get(task_id)
    except TaskValidationError:
        raise HTTPException(status_code=422, detail=f"Task de nome inválido.")

    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Task de ID {task_id} não encontrada!")
