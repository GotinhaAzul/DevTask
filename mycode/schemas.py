from pydantic import BaseModel, ConfigDict


class TaskOut(BaseModel):
    nome: str
    id: int | None = None
    done: bool = False
    model_config = ConfigDict(from_attributes=True)

class TaskIn(BaseModel):
    nome: str
    done: bool = False

class TaskUpdate(BaseModel):
    nome: str | None = None
    done: bool | None = None


class TaskFilter(BaseModel):
    nome: str | None = None
    done: bool | None = None
    id: int | None = None
