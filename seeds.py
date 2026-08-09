from mycode.storage import Storage
from mycode.tasks import Task
from main import setup




def main(filename='database.db'):
    setup()
    storage = Storage(database=filename)
    if storage.read():
        return
    for i in range(5):
        task = Task(nome=str(f"Tarefa {i}"))
        storage.add(task)


if __name__ == "__main__":
    main()
