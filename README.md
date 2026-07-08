DevTask ---
delete() -> Função que aceita ID de paramêtro, filtra lista por IDS até achar o que precisa e deleta no json com data["tasks"].remove(i)

markasdone() -> Itera o json por ID, identifica se está feito ou não e alterna entre os estados.      if not i["done"]: i["done"] = True else: i["done"] = False

create() -> Toma name e id como paramêtros. main() decide o ID e passa o nome digitado pelo usuário na função. O json é lido, tornado em uma variável, editado e toma dump no .json de novo.

read() -> Pode levar ID como paramêtro. Ela busca a lista por ID e printa a task encontrada / todas as tasks.

editname() -> Por hora, a única coisa definida pelo usuário é o nome, por isso, ganhou uma função. Igual a markasdone(), mas recebe input e então atualiza.

check() -> Ela lê o JSON e verifica que o ID é valido, retorna True ou False.

setup() -> Função que roda no início do código para verificar se dados.json existe, se não, cria. Ele cria logs.log e configura o logger.
