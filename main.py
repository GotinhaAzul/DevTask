import json


def create(nome, id):
    dados = {"nome": nome, "id": id, "done": False}

    with open("dados.json", "r") as file:  # Abre o arquivo como "file"
        data = json.load(file)

    data["tasks"].append(dados)  # Adiciona os novos dados

    with open("dados.json", "w") as file:  # Salva os dados atualizados
        json.dump(data, file, indent=4)


def read(id=None):
    with open("dados.json", "r") as file:
        tarefas = json.load(file)

        if id is not None:
            for i in tarefas["tasks"]:
                if i["id"] == id:
                    print(i)

        else:
            for i in tarefas["tasks"]:
                print(i)


def main():
    print("1. Criar Tarefa")  # Crie tarefas
    print("2. Listar Tarefa")  # Veja e conclua tarefas
    print("3. Editar Tarefa")  # Edite tarefas
    print("4. Excluir Tarefa")  # Exclua tarefas
    esc = str(input(""))  # Linha vazia para o usuário ter a experiência "Interativa".

    if esc == "1":
        nome = str(input("Nome da tarefa a criar: "))
        arquivo = open("dados.json", "r")
        id = 0
        for i in arquivo:  # Isso aqui não é uma boa opção. IDs ficam estranhos.
            id += 1
        create(nome, id)

    elif esc == "2":
        read()

    elif esc == "3":
        pass
    elif esc == "4":
        pass
    else:
        print("Opção inválida!")


if __name__ == "__main__":
    main()
