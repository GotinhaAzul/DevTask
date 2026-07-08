import json


def delete(taskid):
    with open("dados.json", "r") as file:
        data = json.load(file)

    for i in data["tasks"]:
        if i["id"] == taskid:
            data["tasks"].remove(i)

    with open("dados.json", "w") as file:
        json.dump(data, file, indent=4)
    print(f"Item de id {id} removido!")


def check(id):  # Checagem de existencia de ID
    with open("dados.json", "r") as file:
        data = json.load(file)

    found = False
    for i in data["tasks"]:
        if i["id"] == id:
            found = True
    if not found:
        print("Task de ID inválido! Talvez não exista?")

    return found


def editname(taskid):  # Update task names
    with open("dados.json", "r") as file:
        data = json.load(file)

    read(taskid)  # Usa a função read para exibir apenas a task desejada

    for i in data["tasks"]:
        if i["id"] == taskid:
            name = str(input("Nome: "))
            i["nome"] = name
            print("Atualizado com sucesso!")

    with open("dados.json", "w") as file:  # Salva os dados atualizados
        json.dump(data, file, indent=4)


def create(nome, id):  # Cria tasks
    dados = {"nome": nome, "id": id, "done": False}

    with open("dados.json", "r") as file:  # Abre o arquivo como "file"
        data = json.load(file)

    data["tasks"].append(dados)  # Adiciona os novos dados

    with open("dados.json", "w") as file:  # Salva os dados atualizados
        json.dump(data, file, indent=4)
    print(f"Criou {nome} de ID {id} com sucesso!")


def read(id=None):  # leitura de dados.json
    with open("dados.json", "r") as file:
        tarefas = json.load(file)

        if id is not None:
            for i in tarefas["tasks"]:
                if i["id"] == id:
                    print(i)
                    break

        else:
            for i in tarefas["tasks"]:
                print(i)


def markasdone(taskid):  # Alterna Done entre True ou False
    with open("dados.json", "r") as file:  # Abre o arquivo como "file"
        data = json.load(file)

    for i in data["tasks"]:  # Filtra data até achar desejado, então atualiza
        if i["id"] == taskid:
            if not i["done"]:
                i["done"] = True
            else:
                i["done"] = False

    with open("dados.json", "w") as file:  # Salva os dados atualizados
        json.dump(data, file, indent=4)
    print("Alterado com sucesso!")


def main():
    while True:
        print("1. Criar Tarefa")  # Crie tarefas
        print("2. Listar Tarefa")  # Veja e conclua tarefas
        print("3. Editar Tarefa")  # Edite tarefas
        print("4. Excluir Tarefa")  # Exclua tarefas
        esc = str(input(">>> "))

        if esc == "1":
            nome = str(input("Nome da tarefa a criar: "))
            arquivo = open("dados.json", "r")
            id = 0
            for i in arquivo:  # IDs ficam estranhos, mas nunca iguais.
                id += 1
                create(nome, id)

        elif esc == "2":
            read()
            print("Enter para voltar ao menu.")
            print("Insira ID para alternar entre 'done'")
            id = input(">>> ")
            if id == "" or id == " ":
                continue
            elif check(int(id)):
                markasdone(int(id))

        elif esc == "3":
            read()
            print("Insira ID para editar nome da Task")
            id = int(input(">>> "))
            if check(id):
                editname(id)

        elif esc == "4":
            read()
            print("Insira ID para deletar a Task")
            id = int(input(">>> "))
            if check(id):
                delete(id)

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
