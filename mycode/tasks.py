from random import randint
from dataclasses import dataclass, field

@dataclass
class Task:
    nome: str
    id: int = field(default_factory=lambda: randint(1111, 9999))
    done: bool = False

    def to_dict(self) -> dict:
        return {
            "nome": self.nome,
            "id": self.id,
            "done": self.done
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(nome=data["nome"], id=data["id"], done=data["done"])
