from main import setup
from mycode.storage import Storage
from mycode.tasks import Task
from pathlib import Path


def test_add_and_read(file = "testdatabase.db"):
    setup(file)
    storage = Storage(database=file)
    task = Task(nome="Ola!")
    storage.add(task)
    subject = storage.getbyid(task.id)
    file_path = Path(file)

    assert subject.nome == "Ola!"
    assert subject.id == task.id
    assert subject.done is False

    file_path.unlink(missing_ok=True)

def test_update_and_delete(file="testdatabase.db"):
    setup(file)
    storage = Storage(database=file)
    task = Task(nome="Ola!")
    storage.add(task)
    file_path = Path(file)

    task.nome = "Editada"
    task.done = True
    storage.update(task)
    subject = storage.getbyid(task.id)
    assert subject.nome == "Editada"
    assert subject.done is True

    storage.delete(task.id)
    assert storage.getbyid(task.id) is None
    file_path.unlink(missing_ok=True)
