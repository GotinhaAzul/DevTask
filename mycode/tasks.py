from dataclasses import dataclass


@dataclass
class Task:
    nome: str
    id: int | None = None
    done: bool = False
