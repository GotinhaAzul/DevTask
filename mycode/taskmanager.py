from mycode.exceptions import TaskNotFoundError, TaskValidationError
from mycode.storage import Storage
from mycode.tasks import Task
from mycode.constants import TASK_NAME_MAX_LENGTH, TASK_NAME_MIN_LENGTH


class TaskManager:
    def __init__(self, storage: Storage) -> None:
        self._storage = storage

    def toggle_done(self, task_id: int, user_id: int) -> None:
        task = self._storage.getbyid(task_id, user_id)
        if task is None:
            raise TaskNotFoundError(f"Task com ID {task_id} não encontrada.")

        task.done = not task.done
        self._storage.update(task, user_id)


    def update_name(self, task_id: int, user_id: int, new_name: str) -> None:
        task = self._storage.getbyid(task_id, user_id)
        if task is None:
            raise TaskNotFoundError(f"Task com ID {task_id} não encontrada.")

        new_name = new_name.strip()
        if len(new_name) < TASK_NAME_MIN_LENGTH or len(new_name) > TASK_NAME_MAX_LENGTH:
            raise TaskValidationError("Nome inválido.")


        task.nome = new_name
        self._storage.update(task, user_id)

    def delete(self, task_id: int, user_id: int) -> None:
        task = self._storage.getbyid(task_id, user_id)
        if task is None:
            raise TaskNotFoundError(f"Task com ID {task_id} não encontrada.")

        self._storage.delete(task_id, user_id)

    def add_task(self, task: Task, user_id: int) -> None:
        task.nome = task.nome.strip()
        if len(task.nome) >= TASK_NAME_MIN_LENGTH and len(task.nome) <= TASK_NAME_MAX_LENGTH:
            self._storage.add(task, user_id)
        else:
            raise TaskValidationError("Task com nome grande/pequeno demais.")

    def get(self, task_id: int, user_id: int) -> Task | None:
        return self._storage.getbyid(task_id, user_id)

    def set_done(self, task_id: int, user_id: int, done: bool) -> None:
        task = self._storage.getbyid(task_id, user_id)
        if task == None:
            raise TaskNotFoundError(f"Task com ID {task_id} não encontrada.")
        else:
            task.done = done
        self._storage.update(task, user_id)

    def get_sorted(self, sort_by: str, user_id: int,  descending: bool = False):
       return self._storage.read_sorted(sort_by, user_id, descending)
