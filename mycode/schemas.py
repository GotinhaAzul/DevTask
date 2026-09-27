from enum import Enum

from pydantic import BaseModel, ConfigDict, Field

from mycode.constants import TASK_NAME_MAX_LENGTH, TASK_NAME_MIN_LENGTH, USER_NAME_MAX_LENGTH, USER_NAME_MIN_LENGTH


class TaskOut(BaseModel):
    nome: str
    id: int | None = None
    done: bool = False
    model_config = ConfigDict(from_attributes=True)

class TaskIn(BaseModel):
    nome: str = Field(min_length=TASK_NAME_MIN_LENGTH, max_length=TASK_NAME_MAX_LENGTH, strip_whitespace=True)
    done: bool = False

class TaskUpdate(BaseModel):
    nome: str | None = Field(default=None, min_length=TASK_NAME_MIN_LENGTH, max_length=TASK_NAME_MAX_LENGTH, strip_whitespace=True)
    done: bool | None = None

class TaskSort(str, Enum):
    id = "id"
    done = "done"


class TaskFilter(BaseModel):
    nome: str | None = None
    done: bool | None = None
    id: int | None = None
    sort_by: TaskSort = TaskSort.id
    descending: bool = False


class UserIn(BaseModel):
    username: str = Field(min_length=USER_NAME_MIN_LENGTH, max_length=USER_NAME_MAX_LENGTH, strip_whitespace=True)
    password: str = Field(min_length=1, max_length=128)


class UserOut(BaseModel):
    username: str
    userID: int | None = None
    model_config = ConfigDict(from_attributes=True)
