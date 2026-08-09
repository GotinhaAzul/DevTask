from mycode.tasks import Task


def test_task_creation():
    task = Task(nome="Ola!")
    assert task.nome == "Ola!"
    assert isinstance(task.id, int)
    assert 1111 <= task.id <= 9999
    assert task.done is False
