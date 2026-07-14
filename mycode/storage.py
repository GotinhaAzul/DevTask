import json

from mycode.tasks import Task

class Storage:
    def _write_raw(self, content: dict, filename: str) -> None:
        with open(filename, "w") as f:
            json.dump(content, f, indent=4)

    def _read_raw(self, filename: str) -> dict:
        with open(filename, "r") as f:
            return json.load(f)
 # ------------------------------------
    def add(self, task: Task, filename: str)-> None:
        data = self._read_raw(filename)
        data["tasks"].append(task.to_dict())
        self._write_raw(data, filename)

    def read(self, filename: str) -> list[Task]:
        data = self._read_raw(filename)
        return [Task.from_dict(item) for item in data["tasks"]]

    def save_all(self, tasks: list[Task], filename: str) -> None:
        data = {"tasks": [t.to_dict() for t in tasks]}
        self._write_raw(data, filename)
