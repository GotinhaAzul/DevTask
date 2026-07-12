from mycode.storage import Storage
from mycode.tasks import Task
import json
from pathlib import Path

def test_storage(tmp_path):
    t = Task()
    task = t.createtask("Ola!")
    s = Storage()
    fixture = Path(__file__).with_name("teste.json")
    storage_file = tmp_path / fixture.name
    storage_file.write_text(fixture.read_text())
    s.write(task, storage_file)

    assert s.read(storage_file)["tasks"][0] == task

    with storage_file.open("r") as f:
        data = json.load(f)
        assert data["tasks"][0] == task
        assert 1111 <= task[1] <= 9999
        assert isinstance(task[1], int)
        assert task[0] == "Ola!"


def test_save_replaces_document(tmp_path):
    storage_file = tmp_path / "tasks.json"
    storage_file.write_text('{"tasks": [{"id": 1, "nome": "Old", "done": false}]}')

    Storage().save(
        {"tasks": [{"id": 1, "nome": "Updated", "done": True}]},
        storage_file,
    )

    assert Storage().read(storage_file) == {
        "tasks": [{"id": 1, "nome": "Updated", "done": True}]
    }
