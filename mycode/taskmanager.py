from mycode.exceptions import TaskNotFoundError
from mycode.storage import Storage
from mycode.tasks import Task


class TaskManager:
    def __init__(self, storage: Storage, filename: str = "dados.json"):
        self._storage = storage
        self._filename = filename

    def list_all(self) -> None:
        tasks = self._storage.read(self._filename)
        for task in tasks:
            print(f"[{'✓' if task.done else '-'}] {task.id}: {task.nome}")

    def toggle_done(self, task_id: int) -> None:
        tasks = self._storage.read(self._filename)
        for task in tasks:
            if task.id == task_id:
                task.done = not task.done
                break
        else:
            raise TaskNotFoundError(f"Task com ID {task_id} não encontrada.")
        self._storage.save_all(tasks, self._filename)

    def update_name(self, task_id: int, new_name: str) -> None:
        tasks = self._storage.read(self._filename)
        for task in tasks:
            if task.id == task_id:
                task.nome = new_name
                break
        else:
            raise TaskNotFoundError(f"Task com ID {task_id} não encontrada.")
        self._storage.save_all(tasks, self._filename)

    def delete(self, task_id: int) -> None:
        tasks = self._storage.read(self._filename)
        for i, task in enumerate(tasks):
            if task.id == task_id:
                del tasks[i]
                break
        else:
            raise TaskNotFoundError(f"Task com ID {task_id} não encontrada.")
        self._storage.save_all(tasks, self._filename)
