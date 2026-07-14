from mycode.storage import Storage
from mycode.tasks import Task
import json
from pathlib import Path


def test_add_and_read(tmp_path):
    storage_file = tmp_path / "tasks.json"
    storage_file.write_text('{"tasks": []}')

    task = Task(nome="Ola!")
    storage = Storage()
    storage.add(task, str(storage_file))

    tasks = storage.read(str(storage_file))
    assert len(tasks) == 1
    assert tasks[0].nome == "Ola!"
    assert tasks[0].id == task.id
    assert tasks[0].done is False


def test_read_returns_task_objects(tmp_path):
    storage_file = tmp_path / "tasks.json"
    storage_file.write_text('{"tasks": [{"nome": "Teste", "id": 42, "done": true}]}')

    tasks = Storage().read(str(storage_file))
    assert isinstance(tasks[0], Task)
    assert tasks[0].nome == "Teste"
    assert tasks[0].id == 42
    assert tasks[0].done is True


def test_save_all_replaces_content(tmp_path):
    storage_file = tmp_path / "tasks.json"
    storage_file.write_text('{"tasks": []}')

    new_tasks = [Task(nome="Updated", id=1, done=True)]
    Storage().save_all(new_tasks, str(storage_file))

    tasks = Storage().read(str(storage_file))
    assert len(tasks) == 1
    assert tasks[0].nome == "Updated"
    assert tasks[0].done is True
