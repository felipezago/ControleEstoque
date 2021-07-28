import psycopg2
from Funcoes.configdb import Banco


class Endereco:
    def __init__(self, rua="", bairro="", numero="", cidade="", estado="", cep=""):
        self.rua = rua
        self.bairro = bairro
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
