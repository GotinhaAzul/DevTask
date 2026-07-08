import json


def create(nome, id):
    dados = {"nome": nome, "id": id}

    # Abre o arquivo como "file"
    with open("dados.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # Adiciona os novos dados
    data["tasks"].append(dados)

    # Salva os dados atualizados
    with open("dados.json", "w") as file:
        json.dump(data, file, indent=4)


def main():
    print("1. Criar Tarefa")
    print("2. Listar Tarefa")
    print("3. Editar Tarefa")
    print("4. Excluir Tarefa")
    esc = str(input(""))  # Linha vazia para o usuário ter a experiência "Interativa".

    if esc == "1":
        nome = str(input("Nome da tarefa a criar: "))
        arquivo = open("dados.json", "r")
        id = 0
        for i in arquivo:  # Isso aqui não é uma boa opção. IDs
            id += 1
        create(nome, id)

    elif esc == "2":
        pass
    elif esc == "3":
        pass
    elif esc == "4":
        pass
    else:
        print("Opção inválida!")


if __name__ == "__main__":
    main()
