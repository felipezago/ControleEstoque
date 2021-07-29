from Model.Endereco import Endereco


class Pessoa(Endereco):
    def __init__(self, cpf="", nome="", fone="", email="", rg="", celular="", tipo=""):
        super().__init__()
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.fone = fone
        self.rg = rg
        self.tipo = tipo
        self.celular = celular


