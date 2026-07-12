from mycode import storage

class taskmanager:
    def alter(self, filename, id, status):
        bau = storage.Storage()
        conteudo = bau.read(filename)
        for i in conteudo["tasks"]:  # Filtra data até achar desejado, então atualiza
            if i["id"] == id:
                if not i["done"]:
                    i["done"] = True
                else:
                    i["done"] = False
        bau.save(conteudo, filename)


    def updatename(self, filename, id):
        bau = storage.Storage()
        conteudo = bau.read(filename)
        for i in conteudo["tasks"]:
            if i["id"] == id:
                name = str(input("Nome: "))
                i["nome"] = name
                break
        bau.save(conteudo, filename)


    def delete(self, filename, id):
        bau = storage.Storage()
        conteudo = bau.read(filename)
        for i in conteudo["tasks"]:
            if i["id"] == id:
                conteudo["tasks"].remove(i)
                break
        bau.save(conteudo, filename)
