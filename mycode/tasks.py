from random import randint
from dataclasses import dataclass, field

@dataclass
class Task:
    nome: str
    id: int = field(default_factory=lambda: randint(1111, 9999))
    done: bool = False
