from mycode.exceptions import TaskNotFoundError
from mycode.storage import Storage
from mycode.tasks import Task




class TaskManager:
    def __init__(self, storage: Storage) -> None:
        self._storage = storage
    def list_all(self) -> list[Task]:
        tasks = self._storage.read()
        return tasks

    def toggle_done(self, task_id: int) -> None:
        task = self._storage.getbyid(task_id)
        if task is None:
            raise TaskNotFoundError(f"Task com ID {task_id} não encontrada.")

        task.done = not task.done
        self._storage.update(task)


    def update_name(self, task_id: int, new_name: str) -> None:
        task = self._storage.getbyid(task_id)
        if task is None:
            raise TaskNotFoundError(f"Task com ID {task_id} não encontrada.")

        task.nome = new_name
        self._storage.update(task)

    def delete(self, task_id: int) -> None:
        task = self._storage.getbyid(task_id)
        if task is None:
            raise TaskNotFoundError(f"Task com ID {task_id} não encontrada.")

        self._storage.delete(task_id)

    def add_task(self, task: Task) -> None:
        self._storage.add(task)

    def helper_show_tasks(self):
        tasks = self._storage.read()
        for task in tasks:
            print(f"[{'✓' if task.done else '-'}] {task.id}: {task.nome}")
