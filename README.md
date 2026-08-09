storage.py - Toma conta de realizar as ações CRUD

taskmanager.py - Recebe objetos tasks, os edita e chama storage para adiciona-los no banco de dados

Tasks - dataclass que serve para guardar informações das task do usuário.

logger.py - Log simples, chamado em main.py

seeds.py - Popula o banco de dados com tarefas repetidas para testes, apenas roda se for chamada.
