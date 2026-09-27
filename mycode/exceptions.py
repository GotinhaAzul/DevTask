class TaskNotFoundError(Exception):
    """Lançada quando uma task com o ID solicitado não existe."""



class ValidationError(Exception):
    """Lançada quando os dados fornecidos são inválidos."""


class UserNotFoundError(Exception):
    """Lançada quando um user com o username solicitado não existe."""


class UserAlreadyExistsError(Exception):
    """Lançada quando o username já está em uso."""
