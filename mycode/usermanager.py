from mycode.constants import USER_NAME_MAX_LENGTH, USER_NAME_MIN_LENGTH
from mycode.exceptions import UserAlreadyExistsError, UserNotFoundError, ValidationError
from mycode.user_storage import User_Storage
from mycode.users import User


class UserManager:
    def __init__(self, storage: User_Storage) -> None:
        self._storage = storage

    def delete_user(self, username: str, password: str) -> None:
        user = self._storage.getbyusername(username)
        if user == None:
            raise UserNotFoundError

        if password != user.password:
            raise ValidationError

        self._storage.delete(username)

    def add_user(self, user: User) -> None:
        user.username = user.username.strip()
        if len(user.username) < USER_NAME_MIN_LENGTH or len(user.username) > USER_NAME_MAX_LENGTH:
            raise ValidationError("User com nome grande/pequeno demais.")

        if self._storage.getbyusername(user.username) is not None:
            raise UserAlreadyExistsError(f"User '{user.username}' já existe.")

        self._storage.add(user)

    def get(self, username: str) -> User | None:
        return self._storage.getbyusername(username)

    def verify_user(self, username: str, password: str):
        user = self.get(username)
        if user:
            return user.password == password
