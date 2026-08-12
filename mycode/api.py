from fastapi import FastAPI, Depends
from mycode.taskmanager import TaskManager
from mycode.storage import Storage
from mycode.tasks import Task
from mycode.schemas import TaskOut, TaskIn

app = FastAPI()

def get_manager():
    storage = Storage()
    try:
        yield TaskManager(storage=storage)
    finally:
        storage.close()


@app.get("/tasks", response_model=list[TaskOut])
def list_tasks(taskmanager: TaskManager = Depends(get_manager)) -> list[Task]:
    return taskmanager.list_all()


@app.post("/tasks", status_code=201, response_model=TaskOut)
def add_task(task_in: TaskIn, manager: TaskManager = Depends(get_manager)) -> Task:
    task = Task(nome=task_in.nome, done=task_in.done)
    manager.add_task(task)
    return task
