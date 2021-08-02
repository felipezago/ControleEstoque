import psycopg2
from Funcoes.configdb import Banco


def conexao():
    config = Banco()
    params = config.get_params()
    conn = psycopg2.connect(**params)
    return conn
