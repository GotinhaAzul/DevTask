from pathlib import Path

from fastapi.testclient import TestClient

from mycode.api import app, get_manager
from mycode.helpers import setup
from mycode.task_storage import Task_Storage
from mycode.taskmanager import TaskManager
from mycode.tasks import Task


def test_api_list(file="testapi.db"):
    setup(file)
    storage = Task_Storage(database=file)
    storage.add(Task(nome="Tester"), user_id=0)
    manager = TaskManager(storage=storage)

    app.dependency_overrides[get_manager] = lambda: manager
    client = TestClient(app)

    response = client.get("/tasks",params={"user_id": 0})

    assert response.status_code == 200
    assert response.json() == [{"nome": "Tester", "id": 1, "done": False}]

    app.dependency_overrides.clear()
    storage.close()
    Path(file).unlink(missing_ok=True)
