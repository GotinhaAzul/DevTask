from fastapi import Depends, FastAPI, HTTPException
from fastapi_pagination import Page, add_pagination, paginate

from mycode.exceptions import TaskNotFoundError
from mycode.schemas import TaskIn, TaskOut, TaskUpdate
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
def list_tasks(taskmanager: TaskManager = Depends(get_manager)) -> Page[TaskOut]:
    return paginate(taskmanager.list_all())


@app.post("/tasks", status_code=201, response_model=TaskOut)
def add_task(task_in: TaskIn, manager: TaskManager = Depends(get_manager)) -> Task:
    task = Task(nome=task_in.nome, done=task_in.done)
    manager.add_task(task)
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
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Task de ID {task_id} não encontrada!")
