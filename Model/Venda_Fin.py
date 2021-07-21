import psycopg2
from Funcoes.configdb import Banco


class Venda_Fin:
    def __init__(self, id_fin="", finalizadoras="", venda="", valor=""):
        self.id = id_fin
        self.finalizadoras = finalizadoras
        self.venda = venda
        self.valor = valor

    def valor_pago(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT SUM(vendas_fin_valor) FROM vendas_fin WHERE vendas_id = {self.venda.id}')
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row[0] is None:
            return 0
        else:
            return row[0]

    def get_fins_venda(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM vendas_fin WHERE vendas_id = {self.venda.id_venda}')
        row = cur.fetchall()
        cur.close()
        conn.close()
        return row

    def inserir_fin_venda(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"INSERT INTO vendas_fin (fin_id, vendas_id, vendas_fin_valor) "
                    f"VALUES ({self.finalizadoras.id}, {self.venda.id}, {self.valor})")
        conn.commit()
        cur.close()
        conn.close()

    def delete_fin_by_cod(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM vendas_fin WHERE vendas_fin_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

    def delete_fin_by_venda(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print(f"DELETE FROM vendas_fin WHERE vendas_id = {self.venda.id}")
        cur.execute(f"DELETE FROM vendas_fin WHERE vendas_id = {self.venda.id}")
        conn.commit()
        cur.close()
        conn.close()