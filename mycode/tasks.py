from random import randint

class Task:
    def createtask(self, nome) -> dict:
        id = randint(1111, 9999) # Voltar aqui depois
        taskelement = {"nome": nome, "id": id, "done": False}
        return taskelement
