DevTask é uma aplicação simples de To-Dos.

Ela está dividida em duas principais partes: Users e Tasks.

# Tasks

As tasks são objetos dataclass (tasks.py) que são modificados e alterados pelo taskmanager e então armazenados em sqlite pelo storage.

A arquitetura simples desse sistema é a seguinte:

CLI -> API -> TaskManager -> Storage

# Users

Os users são dataclass (users.py) gerenciados pelo usermanager e persistidos em sqlite pelo user_storage.

Arquitetura: API -> UserManager -> User_Storage

## POST /register?user_id={id}

Body (`UserIn`):
```json
{"username": "alice", "password": "secret"}
```

- `201` -> `{"username": "alice", "id": 1}`
- `409` -> username ou USERID já em uso
- `422` -> username/senha inválidos

Por enquanto `user_id` vem na request como query param. No futuro será extraído do JWT.

