from mycode.taskmanager import TaskManager
from mycode.storage import Storage
from mycode.tasks import Task
from mycode.logger import logs
from mycode.exceptions import TaskNotFoundError
import os
import sqlite3


def setup() -> None:
    if not os.path.exists("dados.json"):
        with open("dados.json", "w") as f:
            f.write('{"tasks": []}')
    if not os.path.exists("logs.log"):
        with open("logs.log", "w") as f:
            f.write("")
    # STATUS default 0 para False
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS TASKS (NAME TEXT, ID INTEGER, STATUS BOOLEAN NOT NULL DEFAULT 0 """)
        connection.commit()



def main() -> None:
    setup()
    logger = logs()
    storage = Storage()
    manager = TaskManager(storage=storage)

    while True:
        print("\n1. Criar Tarefa")
        print("2. Listar Tarefas")
        print("3. Editar Tarefa")
        print("4. Excluir Tarefa")
        esc = input(">>> ")

        if esc == "1":
            nome = input("Insira nome da Task: ").strip()
            if not nome:
                print("Nome inválido!")
                continue
            task = Task(nome=nome)
            storage.add(task, "dados.json")
            logger.process(f"Criou task '{nome}' com ID {task.id}")
            print(f"Task '{nome}' criada com ID {task.id}!")

        elif esc == "2":
            manager.list_all()
            resp = input("\nEnter para voltar ou ID para alternar conclusão: ").strip()
            if resp and resp.isdigit():
                try:
                    manager.toggle_done(int(resp))
                    logger.process(f"Alternou conclusão da task ID {resp}")
                except TaskNotFoundError:
                    print("ID inválido! Task não encontrada.")

        elif esc == "3":
            manager.list_all()
            resp = input("ID da task para editar: ").strip()
            if not resp.isdigit():
                print("ID inválido!")
                continue
            novo_nome = input("Novo nome: ").strip()
            if not novo_nome:
                print("Nome inválido!")
                continue
            try:
                manager.update_name(int(resp), novo_nome)
                logger.process(f"Renomeou task ID {resp} para '{novo_nome}'")
                print("Nome atualizado!")
            except TaskNotFoundError:
                print("ID inválido! Task não encontrada.")

        elif esc == "4":
            manager.list_all()
            resp = input("ID da task para excluir: ").strip()
            if not resp.isdigit():
                print("ID inválido!")
                continue
            try:
                manager.delete(int(resp))
                logger.process(f"Removeu task ID {resp}")
                print("Task removida!")
            except TaskNotFoundError:
                print("ID inválido! Task não encontrada.")

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
