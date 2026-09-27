from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str
    userID: int | None = None
