from mycode.tasks import Task


def test_task_creation():
    task = Task(nome="Ola!")
    assert task.nome == "Ola!"
    assert isinstance(task.id, int)
    assert 1111 <= task.id <= 9999
    assert task.done is False


def test_to_dict():
    task = Task(nome="Teste", id=1234, done=True)
    d = task.to_dict()
    assert d == {"nome": "Teste", "id": 1234, "done": True}


def test_from_dict():
    d = {"nome": "Teste", "id": 1234, "done": True}
    task = Task.from_dict(d)
    assert task.nome == "Teste"
    assert task.id == 1234
    assert task.done is True
