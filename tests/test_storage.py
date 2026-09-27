from mycode.tasks import Task
from pathlib import Path
from mycode.task_storage import Task_Storage
from mycode.helpers import setup


def test_add_and_read(file = "testdatabase.db"):
    setup(file)
    storage = Task_Storage(database=file)
    task = Task(nome="Ola!")
    storage.add(task, user_id=0)
    subject = storage.getbyid(task.id, user_id=0)
    file_path = Path(file)

    assert subject.nome == "Ola!"
    assert subject.id == task.id
    assert subject.done is False
    storage.close()
    file_path.unlink(missing_ok=True)

def test_update_and_delete(file="testdatabase.db"):
    setup(file)
    storage = Task_Storage(database=file)
    task = Task(nome="Ola!")
    storage.add(task, user_id=0)
    file_path = Path(file)

    task.nome = "Editada"
    task.done = True
    storage.update(task,user_id=0)
    subject = storage.getbyid(task.id,user_id=0)
    assert subject.nome == "Editada"
    assert subject.done is True

    storage.delete(task.id,user_id=0)

    assert storage.getbyid(task.id,user_id=0) is None
    storage.close()
    file_path.unlink(missing_ok=True)
