class TaskNotFoundError(Exception):
    """Lançada quando uma task com o ID solicitado não existe."""



class TaskValidationError(Exception):
    """Lançada quando os dados fornecidos são inválidos."""
