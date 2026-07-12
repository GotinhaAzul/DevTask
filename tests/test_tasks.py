from mycode.tasks import Task

def test_tasksee():
    t = Task()
    task = t.createtask("Ola!")
    assert task[0] == "Ola!"
