from mycode.api import Task_Storage
from mycode.helpers import setup
from mycode.tasks import Task
from mycode.constants import DEMO_USER_ID


def main(filename='database.db'):
    setup(filename)
    storage = Task_Storage(database=filename)
    try:
        if storage.read_sorted("id", DEMO_USER_ID):
            return
        for i in range(5):
            task = Task(nome=str(f"Tarefa {i}"))
            storage.add(task, DEMO_USER_ID)
    finally:
        storage.close()


if __name__ == "__main__":
    main()
