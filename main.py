import sqlite3

from mycode.exceptions import TaskNotFoundError
from mycode.logger import logs
from mycode.storage import Storage
from mycode.taskmanager import TaskManager
from mycode.tasks import Task



def setup(filename = 'database.db') -> None:
    # STATUS default 0 para False
    connection = sqlite3.connect(filename)
    try:
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (NAME TEXT, ID INTEGER PRIMARY KEY AUTOINCREMENT, STATUS BOOLEAN NOT NULL DEFAULT 0) """)
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_tasks_id ON tasks(id)") # Reduntante. Vou manter apenas para não me esquecer e caso, no futuro, use uma forma diferente de ID (Irei...)
        connection.commit()
        connection.close()
    finally:
        connection.close()


def main() -> None:
    setup()
    logger = logs()
    storage = Storage()
    manager = TaskManager(storage=storage)
    try:
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
                manager.add_task(task)
                logger.process(f"Criou task '{nome}' com ID {task.id}")
                print(f"Task '{nome}' criada com ID {task.id}!")

            elif esc == "2":
                manager.helper_show_tasks()
                resp = input("\nEnter para voltar ou ID para alternar conclusão: ").strip()
                if resp and resp.isdigit():
                    try:
                        manager.toggle_done(int(resp))
                        logger.process(f"Alternou conclusão da task ID {resp}")
                    except TaskNotFoundError:
                        print("ID inválido! Task não encontrada.")

            elif esc == "3":
                tasks = manager.list_all()
                for task in tasks:
                    print(f"[{'✓' if task.done else '-'}] {task.id}: {task.nome}")

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
    finally:
        storage.close()


if __name__ == "__main__":
    main()
