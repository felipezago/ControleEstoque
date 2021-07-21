import psycopg2
from Funcoes.configdb import Banco


class Vendas:
    def __init__(self, id="", id_venda="", id_prod_serv="", tipo="", qtd="", valor="", desconto="", data_hora=""):
        self.id = id
        self.id_venda = id_venda
        self.id_prod_serv = id_prod_serv
        self.tipo = tipo
        self.qtd = qtd
        self.valor = valor
        self.desconto = desconto
        self.data_hora = data_hora

    def get_vendas_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM vendas WHERE id_venda = \'{self.id_venda}\'')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    def delete_venda_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM vendas WHERE id_venda = {self.id_venda}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def inserir_venda():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"INSERT INTO vendas SELECT * from venda_tmp")
        conn.commit()
        cur.close()
        conn.close()
