from mycode.tasks import Task


def test_task_creation():
    task = Task(nome="Ola!", id=1111)
    assert task.nome == "Ola!"
    assert isinstance(task.id, int)
    assert task.done is False
