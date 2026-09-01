from pathlib import Path

from fastapi.testclient import TestClient

from main import setup
from mycode.api import app, get_manager
from mycode.storage import Storage
from mycode.tasks import Task
from mycode.taskmanager import TaskManager


def test_api_list(file="testapi.db"):
    setup(file)
    storage = Storage(database=file)
    storage.add(Task(nome="Tester"))
    manager = TaskManager(storage=storage)

    app.dependency_overrides[get_manager] = lambda: manager
    client = TestClient(app)

    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == [{"nome": "Tester", "id": 1, "done": False}]

    app.dependency_overrides.clear()
    storage.close()
    Path(file).unlink(missing_ok=True)