from dataclasses import asdict
from time import sleep

import requests

from mycode.constants import LOCALHOST
from mycode.exceptions import TaskNotFoundError
from mycode.helpers import localhost_up, raise_for_api, setup, show_tasks
from mycode.logger import logs
from mycode.tasks import Task


def main() -> None:
    logger = logs()
    storage = Storage()
    try:
        while True:
            print("1. Criar Tarefa")
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
                requests.post(f"{LOCALHOST}/tasks", json=asdict(task))

                logger.process(f"Criou task '{nome}' com ID {task.id}")
                print(f"Task '{nome}' criada com ID {task.id}!")

            elif esc == "2":
                show_tasks()

                task_id = input("Enter para voltar ou ID para alternar conclusão: ").strip()
                if not task_id.isdigit():
                    print("Insira um id de task válido!")
                    continue

                try:
                    response = requests.get(f"{LOCALHOST}/tasks",params={"id": int(task_id)})
                    raise_for_api(response)

                    items = response.json()["items"]
                    if not items:
                        raise TaskNotFoundError(f"Task de ID {task_id} não encontrada.")

                    task = Task(**items[0])
                    response = requests.patch(f"{LOCALHOST}/tasks/{task_id}",json={"done": not task.done})
                    raise_for_api(response)
                    logger.process(f"Alternou conclusão da task ID {task_id}")

                except TaskNotFoundError:
                    print("Task não encontrada.")

            elif esc == "3":
                show_tasks()

                resp = input("ID da task para editar: ").strip()
                if not resp.isdigit():
                    print("ID inválido!")
                    continue
                novo_nome = input("Novo nome: ").strip()
                if not novo_nome:
                    print("Nome inválido!")
                    continue
                try:
                    requests.patch(f"{LOCALHOST}/tasks/{resp}", json={"nome": novo_nome})
                    logger.process(f"Renomeou task ID {resp} para '{novo_nome}'")
                    print("Nome atualizado!")
                except TaskNotFoundError:
                    print("ID inválido! Task não encontrada.")

            elif esc == "4":
                show_tasks()

                resp = input("ID da task para excluir: ").strip()
                if not resp.isdigit():
                    print("ID inválido!")
                    continue
                try:
                    requests.delete(f"{LOCALHOST}/tasks/{resp}")
                    logger.process(f"Removeu task ID {resp}")
                    print("Task removida!")
                except TaskNotFoundError:
                    print("ID inválido! Task não encontrada.")

            else:
                print("Opção inválida!")
    finally:
        storage.close()


if __name__ == "__main__":
    localhost_up()
    sleep(1)
    setup()
    print()
    print("DevTask ------------------")
    main()
